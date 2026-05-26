#!/usr/bin/env python3
"""validate-case-file.py — validate a Case File against the schema.

Validates the YAML frontmatter and basic structure of a Case File against
the schema established by 06-Case-Files/_TEMPLATE.md. Pairs with
validate-tool.py (which validates Tool Entries against the tool schema).

Validation rules:
  A: file structure (frontmatter present, parses, closed)
  B: required frontmatter keys
  C: enum-value rules (status, persona, clarity states)
  D: cross-field consistency (e.g. resolved → active=false)
  E: optional-property rules (stakes_flags is a list)
  F: body content (at least one Frame heading)
  G: detection_check block (per chapter 13 §13.2 pre-turn-5 detection
     check) — block may live in frontmatter or as a YAML block in body;
     mandatory fields: turn (int), signals_observed (list of 5 entries
     covering all canonical signals), relaxed_scaffolding (bool),
     justification (str). The five canonical signal names are:
     domain_fluency, prior_diagnostic_work, executive_role,
     direct_read_request, framework_fluency.
  H: library-resolution check (per chapter 04 §4.3 anti-compliance-
     theater rule + chapter 13 §13.2 Fabricated tool IDs check) —
     every Tool ID and canonical title cited in the ## Tools Applied
     section MUST resolve to an actual entry in 01-Tools/Tool Entries/.
     Resolves by Item_ID (preferred) and by canonical Title /
     filename-stem (case-insensitive, hyphen/space-tolerant). Entries
     explicitly flagged `[ad-hoc]` (corpus-gap moves per chapter 04
     §4.3) are exempt from resolution.
  J: standard-mode surface-naming check (per chapter 04 §4.3.4) —
     when relaxed_scaffolding is false or absent (standard-mode
     default), every canonical title logged in the ## Tools Applied
     section MUST also appear in at least one "AI [persona]: ..."
     line in the ## Session Log. Match is case- and punctuation-
     tolerant via _normalize_title (substring match against the
     normalized concatenation of all AI chat lines). The check is
     skipped when relaxed_scaffolding=true (per chapter 04 §4.3.2
     relaxed mode suppresses surface-naming) or when the Session
     Log contains no AI lines (warning — transcript unavailable,
     cannot verify). Entries flagged `[ad-hoc]` are exempt.
  I: session_mode declaration (per chapter 14 §14.6 — session mode is
     not optional). session_mode MUST be one of the four canonical
     values: production / test / sandbox / multi_session_resumption.
     If session_mode == test, both test_mode and
     do_not_archive_to_production MUST be true. If session_mode != test,
     test_mode MUST be false (or absent). Pre-existing Case Files
     created before Sprint 13 lack the field; Rule I treats absence as
     production (warning, not failure) — the field becomes mandatory
     for Case Files dated after 2026-05-18.
  K: Session Log turn-ordering (Sprint 16 Card 04). Walks the
     `## Session Log` section and asserts `#### Turn N` headers
     appear in monotonically increasing N order. Lists ALL
     out-of-order blocks (does not bail on first). Tessa Sprint 15
     surfaced an out-of-order turn (Turn 4 inserted between Turn 2
     and Turn 3) that no audit script caught.
  L: reverse Rule J — chat-named, not logged (Sprint 16 Card 04).
     For each canonical title from 01-Tools/Tool Entries/ that
     appears in an `AI [persona]: ...` chat line, assert the title
     also appears as a `### [Tool]` entry in the ## Tools Applied
     section. Catches the inverse of Rule J: tools named in chat
     but forgotten in the Tools Applied log. False-positive guard:
     library titles must appear as a standalone canonical reference
     in chat (matched by case- and punctuation-tolerant substring),
     not embedded inside another tool's title.
  M: action-package structural completeness (Sprint 16 Card 04).
     When the Session Log contains an action-package delivery turn
     (detected via the `### Anticipative Solution (Step 4.3)` marker
     in the Frame body OR an action-package commitment keyword in
     AI chat), assert that turn's AI chat output contains all four
     §3.1 step 8 components: (a) primary problem named, (b) a
     committed sequence anchor ("Week 1", "Day 1", "Monday", etc.),
     (c) ≥1 stakeholder draft section, (d) today's / immediate
     tasks list. Heuristic regex matching, not full natural-language
     parsing.
  N: timestamp monotonicity (Sprint 16 Card 04). For `#### Turn N`
     headers that include ISO-8601 or HH:MM timestamps in the
     header line or first line after, assert timestamps are
     non-decreasing across consecutive turns.
  O: last_persona_switch structural completeness (Sprint 16 Card
     09). When the `last_persona_switch` frontmatter field is
     populated, it MUST be a mapping with all four required
     fields: `timestamp`, `from`, `to`, `reason`. Bare-timestamp
     values (the pre-Sprint-16 format) are rejected — the
     switch's `from` / `to` / `reason` fields are load-bearing
     audit evidence and cannot be reconstructed post-hoc.
  P: close-protocol audit-trail recording (Sprint 18 Card 03).
     When `status == resolved`, the close-event frontmatter
     fields (`close_signal_source`, `in_persona_clean_exit_present`,
     `close_protocol_audit_trail`) must be populated with content
     consistent with the close that actually fired. Three branches:
     (a) `operator_control_turn` + `in_persona_clean_exit_present:
     true` requires a visible reflection-invitation delivery in the
     Session Log AI lines; (b) `operator_control_turn` + `in_persona_
     clean_exit_present: false` requires `close_protocol_audit_trail.
     reflection_invitation_text` non-empty in frontmatter (this is
     the suppressed-to-operator path where no chat delivery exists);
     (c) `in_persona_clean_exit_only` requires a visible reflection-
     invitation delivery in the Session Log AI lines. When
     `close_signal_source` is absent on a resolved Case File, Rule P
     attempts inference from Session Log content (operator close
     signal phrases vs in-persona clean-exit utterances) and then
     applies the same branch validation — this catches the Sprint 17
     panel pattern where the close protocol's audit-trail step was
     skipped silently. The rule does not fire on `status != resolved`.

Exit codes:
  0 = pass (warnings may print)
  1 = at least one rule failed
  2 = YAML parse error
  3 = file not found or permission error

Example:
  python3 validate-case-file.py "../06-Case-Files/_ARCHIVED/example-job-decision.md"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import find_root  # noqa: E402

import yaml  # noqa: E402

REQUIRED_KEYS = [
    "case_file_id",
    "case_file_title",
    "user_handle",
    "created",
    "last_updated",
    "status",
    "session_count",
    "total_turns",
    "schema_version",
    "goal_stack",
    "active_persona",
]

STATUS_VALUES = {"active", "paused", "resolved", "abandoned"}
PERSONA_VALUES = {"partner", "counselor", "therapist", "guide", "consultant"}
CLARITY_VALUES = {"unclear", "partially_clear", "clear_but_unstable", "locked"}

CANONICAL_SIGNALS = {
    "domain_fluency",
    "prior_diagnostic_work",
    "executive_role",
    "direct_read_request",
    "framework_fluency",
}

SESSION_MODE_VALUES = {
    "production",
    "test",
    "sandbox",
    "multi_session_resumption",
}

# Sprint 18 Card 08 — schema-frozen-at: v2.0. Adding new schema_version values
# requires migration-script discipline per 00-Instructions/19-governance-and-quality.md.
# Pre-Sprint-18 CFs may have unversioned ("1.0") or empty schema_version; accept
# both legacy and the Sprint 18 frozen form ("1.0-frozen"). Reject explicit unknown
# values to prevent silent schema-drift.
KNOWN_SCHEMA_VERSIONS = {"1.0", "1.0-frozen"}


def _normalize_title(s: str) -> str:
    """Case- and punctuation-insensitive title key (spaces/hyphens/underscores collapsed)."""
    return re.sub(r"[\s\-_]+", "", s).lower()


def _title_aliases_raw(title: str) -> list[str]:
    """Return case-preserved aliases for a (possibly compound) tool title.

    Sprint 18 Card 06: used by Rule J's canonical-vs-descriptive distinction.
    Title-cased canonical naming is detected by substring match in raw AI chat
    text (case-sensitive); descriptive phrasal use is detected via the
    normalized (case-insensitive) match. The two helpers run in parallel —
    `_title_aliases` returns normalized forms for the descriptive layer;
    `_title_aliases_raw` returns the original-case forms for the canonical
    layer. Splits on top-level `/` only (slashes inside parens are preserved
    as part of the canonical name).
    """
    if not title:
        return []
    aliases: list[str] = [title.strip()]
    paren_depth = 0
    parts: list[str] = []
    current: list[str] = []
    for ch in title:
        if ch == "(":
            paren_depth += 1
            current.append(ch)
        elif ch == ")":
            paren_depth = max(paren_depth - 1, 0)
            current.append(ch)
        elif ch == "/" and paren_depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    if len(parts) > 1:
        for p in parts:
            if p and p != title.strip():
                aliases.append(p)
    seen: set[str] = set()
    result: list[str] = []
    for a in aliases:
        if a and a not in seen:
            seen.add(a)
            result.append(a)
    return result


def _check_tool_surfaced_annotation(fm, title: str) -> int | None:
    """Sprint 18 Card 12 — Rule J ↔ §6.4.0 spec contract enforcement.

    When the §6.4.0 placeholder pattern is used in the Session Log (AI
    [persona]: [full verbatim response delivered in chat — see turn-N chat
    output]), the verbatim canonical-title is not present in the literal
    AI text. The spec contract (Sprint 15 Card 07 §6.4.0) is that
    `tool_surfaced_in_chat` frontmatter annotation IS equivalent evidence
    of canonical-title surface presence — "structured-data attestation by
    the AI, accepted as equivalent to text-presence in chat."

    This helper checks the annotation array for an entry whose `tool`
    matches the canonical title being validated (via canonical or
    compound-title alias) AND whose structure is complete (`turn` is an
    int, `evidence` is non-empty). Returns the annotated turn number if
    matched, else None.

    Falsification guard: annotation without `evidence` content is NOT a
    valid shortcut. The AI must attest in writing that the tool was
    surfaced, with a brief evidence string describing the surface. The
    annotation IS the structured-data attestation per spec.
    """
    if not isinstance(fm, dict):
        return None
    annotations = fm.get("tool_surfaced_in_chat")
    if not isinstance(annotations, list):
        return None
    if not title:
        return None
    title_aliases_norm = _title_aliases(title)
    if not title_aliases_norm:
        return None
    for entry in annotations:
        if not isinstance(entry, dict):
            continue
        entry_tool = entry.get("tool")
        if not isinstance(entry_tool, str):
            continue
        entry_tool_norm = _normalize_title(entry_tool)
        if entry_tool_norm not in title_aliases_norm:
            continue
        # Structural completeness: turn must be int, evidence must be non-empty str
        turn = entry.get("turn")
        evidence = entry.get("evidence")
        if not isinstance(turn, int):
            continue
        if not isinstance(evidence, str) or not evidence.strip():
            continue
        return turn
    return None


def _title_aliases(title: str) -> list[str]:
    """Return normalized aliases for a (possibly compound) tool title.

    Sprint 18 Card 05: compound-title aliases. Library entries with a
    `Title:` field of the form `"X / Y"` (e.g., `Title: Critical Chain /
    Critical Path` paired with filename `Critical Path.md`) should be
    matchable by EITHER side of the slash, plus the full title. Rules J
    and L consult this helper so chat-form references like "Critical
    Path" match a Tools Applied entry of "Critical Chain / Critical Path"
    (and vice versa).

    Top-level slashes only — slashes inside parentheses (e.g.,
    "PMI (Plus / Minus / Interesting)") are NOT split, because those
    parenthetical sub-lists are part of the canonical title, not
    alternative names. Returns a deduplicated list of normalized aliases
    in order: full title first, then each top-level split component.
    """
    if not title:
        return []
    full = _normalize_title(title)
    aliases: list[str] = [full]
    paren_depth = 0
    parts: list[str] = []
    current: list[str] = []
    for ch in title:
        if ch == "(":
            paren_depth += 1
            current.append(ch)
        elif ch == ")":
            paren_depth = max(paren_depth - 1, 0)
            current.append(ch)
        elif ch == "/" and paren_depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        parts.append("".join(current).strip())
    if len(parts) > 1:
        for p in parts:
            norm = _normalize_title(p)
            if norm and norm != full:
                aliases.append(norm)
    seen: set[str] = set()
    result: list[str] = []
    for a in aliases:
        if a and a not in seen:
            seen.add(a)
            result.append(a)
    return result


def _filename_to_tt_id(stem: str) -> str:
    """Derive the canonical tt_ID convention from a filename stem.

    Convention: lowercase, whitespace/underscores collapsed to '-', punctuation
    stripped (apostrophes, slashes, parens), prefixed with 'tt-'. This matches
    the existing corpus convention observed in the 600+ Tool Entries.
    Example: 'Pre-Mortem' → 'tt-pre-mortem'; 'Weighted Decision Matrix' →
    'tt-weighted-decision-matrix'.
    """
    slug = re.sub(r"[^\w\s-]", "", stem)
    slug = re.sub(r"[\s_]+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return f"tt-{slug.lower()}"


def _build_tool_index():
    """Build (by_id, by_title) maps from filenames in 01-Tools/Tool Entries/.

    Filename-only resolution — no frontmatter parsing — avoids the Dropbox
    CloudStorage I/O throttling problem documented in trelloplan-resume v31
    (sequential single-process reads stall at ~30 files/min on the corpus).
    Tool entries follow the convention `<Title>.md` with Title matching the
    `Title` frontmatter field and Item_ID derived as `tt-<slugified-title>`.
    Index is built in O(N) directory listing time and uses no file reads.

    Returns ({}, {}) if the directory cannot be located.
    """
    try:
        root = find_root()
    except RuntimeError:
        return {}, {}
    entries_dir = root / "01-Tools" / "Tool Entries"
    if not entries_dir.is_dir():
        return {}, {}
    by_id: dict[str, str] = {}
    by_title: dict[str, str] = {}
    try:
        names = [p.name for p in entries_dir.iterdir() if p.suffix == ".md"]
    except OSError:
        return {}, {}
    for name in names:
        stem = name[:-3]  # strip .md
        title_key = _normalize_title(stem)
        by_title.setdefault(title_key, name)
        id_key = _filename_to_tt_id(stem)
        by_id.setdefault(id_key, name)
    return by_id, by_title


# Template placeholders to ignore in the ## Tools Applied section
_TOOLS_APPLIED_PLACEHOLDER_TITLES = {
    "[tool name]",
    "tool name",
}
_TOOLS_APPLIED_PLACEHOLDER_IDS = {
    "tt-tool-slug",
}
_AD_HOC_MARKER_RE = re.compile(r"\[ad-?hoc\]", re.IGNORECASE)


def extract_tools_applied_entries(body: str):
    """Walk the ## Tools Applied section; yield (title, tt_id_or_None, line_no, is_ad_hoc) per H3 entry.

    Returns None if the section is absent (Rule H exits cleanly — not all
    sessions surface tools). Template placeholder entries (`### [Tool Name]`
    with `Tool ID: tt-tool-slug`) are skipped.
    """
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Tools Applied"):
            start = i + 1
            break
    if start is None:
        return None

    entries = []
    current_title: str | None = None
    current_id: str | None = None
    current_line = 0
    current_ad_hoc = False

    def _close():
        nonlocal current_title, current_id, current_line, current_ad_hoc
        if current_title is None:
            return
        title_l = current_title.lower().strip()
        is_placeholder = (
            title_l in _TOOLS_APPLIED_PLACEHOLDER_TITLES
            or (current_id and current_id.lower() in _TOOLS_APPLIED_PLACEHOLDER_IDS)
        )
        if not is_placeholder:
            entries.append((current_title, current_id, current_line, current_ad_hoc))
        current_title = None
        current_id = None
        current_line = 0
        current_ad_hoc = False

    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("## ") and i > start:
            break
        if stripped.startswith("### "):
            _close()
            current_title = stripped[4:].strip().rstrip(":")
            current_line = i + 1
            current_ad_hoc = bool(_AD_HOC_MARKER_RE.search(current_title))
            # Strip the marker from the title for resolution purposes
            if current_ad_hoc:
                current_title = _AD_HOC_MARKER_RE.sub("", current_title).strip()
        elif stripped.lower().startswith("tool id:"):
            val = stripped.split(":", 1)[1].strip().strip("`")
            if val:
                current_id = val
        i += 1
    _close()
    return entries


def find_detection_check_in_body(body: str):
    """Return the parsed detection_check dict from body, or None if absent.

    Looks first in fenced ``` yaml / yml ``` blocks (the canonical Case File
    rendering per chapter 13 §13.2). Falls back to a bare top-level
    ``detection_check:`` block terminated by the next non-indented,
    non-blank line — lookahead-based termination, per the lint-design
    discipline added in trelloplan-resume v34. Returns the value of the
    ``detection_check`` key (the inner dict), not the wrapper.
    """
    # Pass 1: fenced code blocks (most common form in Case Files)
    fenced_pattern = re.compile(r"```ya?ml\s*\n(.*?)\n```", re.DOTALL)
    for block in fenced_pattern.findall(body):
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict) and "detection_check" in data:
            return data.get("detection_check")

    # Pass 2: bare top-level detection_check: with indented children
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("detection_check:"):
            continue
        block_lines = [line]
        j = i + 1
        while j < len(lines):
            cont = lines[j]
            stripped = cont.strip()
            if not stripped:
                # blank line — peek ahead; continue iff next non-blank is indented
                peek = j + 1
                while peek < len(lines) and not lines[peek].strip():
                    peek += 1
                if peek < len(lines) and lines[peek][:1] in (" ", "\t", "-"):
                    block_lines.append(cont)
                    j += 1
                    continue
                break
            if cont[:1] in (" ", "\t", "-"):
                block_lines.append(cont)
                j += 1
                continue
            break  # non-indented, non-blank — next top-level key
        try:
            data = yaml.safe_load("\n".join(block_lines))
        except yaml.YAMLError:
            return None
        if isinstance(data, dict) and "detection_check" in data:
            return data.get("detection_check")
    return None


_AI_LINE_RE = re.compile(r"^AI\s*\[[^\]]+\]\s*:\s*(.*)$")


def extract_ai_chat_text(body: str) -> str:
    """Concatenate all AI-prefixed chat content from the ## Session Log.

    Returns a single string with all `AI [persona]: ...` content joined
    by newlines. Multi-line AI responses are captured by absorbing
    continuation lines until the next User: / AI[/ #### / ## marker.
    Returns an empty string if the Session Log section is absent or
    contains no AI lines.

    Used by Rule J (chapter 04 §4.3.4 standard-mode surface-naming
    check) — the returned text is normalized and substring-searched
    for canonical tool titles from the ## Tools Applied section.
    """
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Session Log"):
            start = i + 1
            break
    if start is None:
        return ""

    chunks: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        # Section boundary — leaving Session Log
        if line.startswith("## ") and i > start:
            break
        stripped = line.lstrip()
        m = _AI_LINE_RE.match(stripped)
        if m:
            chunks.append(m.group(1).strip())
            # Absorb continuation lines until next User: / AI[ / heading marker
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                next_stripped = next_line.lstrip()
                if (
                    next_stripped.startswith("User:")
                    or _AI_LINE_RE.match(next_stripped)
                    or next_line.startswith("## ")
                    or next_line.startswith("### ")
                    or next_line.startswith("#### ")
                ):
                    break
                chunks.append(next_line.strip())
                j += 1
            i = j
            continue
        i += 1
    return "\n".join(c for c in chunks if c)


_TURN_HEADER_RE = re.compile(r"^####\s+Turn\s+(\d+)\b(.*)$", re.IGNORECASE)
_ISO_TIMESTAMP_RE = re.compile(
    r"\b(\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:?\d{2})?)\b"
)


def extract_session_log_turn_headers(body: str) -> list[tuple[int, int, str | None]]:
    """Return list of (turn_number, line_no_1based, timestamp_or_None) for
    each `#### Turn N` header inside the `## Session Log` section.

    Used by Rule K (turn-ordering) and Rule N (timestamp monotonicity).
    The timestamp is extracted from the header line itself OR from the
    immediately-following line if the header doesn't include one.
    line_no_1based is body-line offset; callers convert to file-line if
    needed.
    """
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Session Log"):
            start = i + 1
            break
    if start is None:
        return []

    out: list[tuple[int, int, str | None]] = []
    i = start
    while i < len(lines):
        line = lines[i]
        if line.startswith("## ") and i > start:
            break
        m = _TURN_HEADER_RE.match(line)
        if m:
            turn_n = int(m.group(1))
            ts: str | None = None
            ts_match = _ISO_TIMESTAMP_RE.search(m.group(2) or "")
            if ts_match:
                ts = ts_match.group(1)
            elif i + 1 < len(lines):
                ts_next = _ISO_TIMESTAMP_RE.search(lines[i + 1])
                if ts_next:
                    ts = ts_next.group(1)
            out.append((turn_n, i + 1, ts))
        i += 1
    return out


def extract_tool_library_titles(scripts_dir: Path) -> list[str]:
    """Return list of canonical tool titles from 01-Tools/Tool Entries/.

    The canonical title is the filename stem (no extension). Used by
    Rule L (reverse Rule J) to detect tools named in chat but forgotten
    in the Tools Applied log.

    scripts_dir is the directory containing this script; the tool
    entries live at scripts_dir.parent / "01-Tools" / "Tool Entries".
    Returns an empty list if the directory does not exist (Rule L
    becomes a no-op — safer than failing the validator on a missing
    corpus).
    """
    tools_dir = scripts_dir.parent / "01-Tools" / "Tool Entries"
    if not tools_dir.is_dir():
        return []
    return [p.stem for p in tools_dir.glob("*.md") if p.is_file()]


def extract_ai_chat_by_turn(body: str) -> list[tuple[int, str]]:
    """Return list of (turn_number, ai_text_chunk) tuples for AI chat lines
    in the ## Session Log, partitioned by user-turn.

    Turn-numbering convention: counter starts at 0 (covers any pre-flight /
    setup AI lines before the first substantive User: line); increments
    to 1 on the first User: line encountered; increments on each
    subsequent User: line. Each AI [persona]: chat line (and its
    continuation lines absorbed exactly as extract_ai_chat_text does)
    is tagged with the current counter value, so AI turn-2 response
    has turn_number=2, etc.

    Used by the Sprint 16 Card 03 Rule J timing sub-check — for each
    Tools Applied entry, the first turn at which its canonical title
    appears in chat must be ≤5 in standard mode (chapter 04 §4.3.4
    first-invocation rule).
    """
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Session Log"):
            start = i + 1
            break
    if start is None:
        return []

    turn = 0
    result: list[tuple[int, str]] = []
    pending_chunks: list[str] = []
    pending_turn: int | None = None

    def flush() -> None:
        nonlocal pending_chunks, pending_turn
        if pending_chunks and pending_turn is not None:
            joined = "\n".join(c for c in pending_chunks if c)
            if joined:
                result.append((pending_turn, joined))
        pending_chunks = []
        pending_turn = None

    i = start
    while i < len(lines):
        line = lines[i]
        # Section boundary — leaving Session Log
        if line.startswith("## ") and i > start:
            flush()
            break
        stripped = line.lstrip()
        # User: / user: line increments the turn counter (and closes any
        # open AI chunk)
        if stripped.startswith("User:") or stripped.startswith("user:"):
            flush()
            turn += 1
            i += 1
            continue
        # AI [persona]: line — start a new AI chunk tagged with current turn
        m = _AI_LINE_RE.match(stripped)
        if m:
            flush()
            pending_turn = turn
            pending_chunks.append(m.group(1).strip())
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                next_stripped = next_line.lstrip()
                if (
                    next_stripped.startswith("User:")
                    or next_stripped.startswith("user:")
                    or _AI_LINE_RE.match(next_stripped)
                    or next_line.startswith("## ")
                    or next_line.startswith("### ")
                    or next_line.startswith("#### ")
                ):
                    break
                pending_chunks.append(next_line.strip())
                j += 1
            i = j
            continue
        i += 1
    flush()
    return result


# ---------------------------------------------------------------
# Sprint 18 Card 03 — Rule P helpers
# ---------------------------------------------------------------

# Canonical reflection-invitation phrasings from chapter 06 §6.13
# step 3 (verbose) and §6.13.1 (single-line). Match is case-insensitive
# substring against AI chat lines. Partial-match fragments tolerate
# minor punctuation / whitespace drift.
_INVITATION_FRAGMENTS = (
    "anything about how this session went you'd want a future you to know",
    "anything you want noted before close",
    "anything you'd want noted before close",
    "anything you'd want a future you to know",
)

# Operator close-turn signal phrases (used by inference when
# close_signal_source frontmatter is absent).
_OPERATOR_CLOSE_PHRASES = (
    "test complete",
    "holodeck closed",
    "close the session",
    "session complete",
    "end the test",
)

# In-persona clean-exit utterance fragments. Sourced from chapter
# 02 §2.12 success signals and chapter 06 §6.13.1 clean-exit list.
_IN_PERSONA_CLEAN_EXIT_FRAGMENTS = (
    "i think i have what i need",
    "i think we're good",
    "we're good for now",
    "this is enough for me",
    "this is enough",
    "i'm done",
    "i am done",
    "that's it",
    "thanks, that's it",
    "after that i'm done",
    "i have what i need",
)


_SESSION_LOG_TERMINATORS = (
    "## Reflections",
    "## Next Steps",
    "## Frame ",
)


def _extract_session_log_text(body: str) -> str:
    """Return the concatenated lowercase text of the Session Log scope.
    Used by Rule P helpers to scan AI + User lines for canonical phrases.

    Sprint 19 Card 04-F Fix 1: terminator changed from any `## ` header to
    the specific canonical post-Session-Log sections (`## Reflections`,
    `## Next Steps`, `## Frame `). Intervening `## ` sections (e.g.
    `## Tools Applied`) are now passed through so `#### Turn N` blocks
    placed after them remain visible to Rule P. Closes the Tessa
    Card 04-E false-negative where an inline `## Tools Applied` between
    turns hid subsequent close signals."""
    lines = body.splitlines()
    in_section = False
    chunks: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("## Session Log"):
            in_section = True
            continue
        if in_section and any(stripped.startswith(t) for t in _SESSION_LOG_TERMINATORS):
            break
        if in_section:
            chunks.append(line)
    return "\n".join(chunks).lower()


def _extract_ai_chat_text(body: str) -> str:
    """Return concatenated lowercase AI chat content from Session Log.
    Walks ^AI [persona]: lines + their continuation paragraphs; stops
    each chunk at the next User: / AI: / heading. Used by Rule P
    Branches (a) and (c) to verify visible invitation delivery.

    Sprint 19 Card 04-F Fix 1: terminator changed from any `## ` header
    to `_SESSION_LOG_TERMINATORS` (`## Reflections`, `## Next Steps`,
    `## Frame `). Intervening `## ` sections like `## Tools Applied`
    are now passed through so AI chat lines in `#### Turn N` blocks
    after them remain visible to Rule P invitation-delivery detection."""
    lines = body.splitlines()
    in_section = False
    ai_chunks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if not in_section:
            if stripped.startswith("## Session Log"):
                in_section = True
            i += 1
            continue
        if any(stripped.startswith(t) for t in _SESSION_LOG_TERMINATORS):
            break
        m = _AI_LINE_RE.match(stripped)
        if m:
            ai_chunks.append(m.group(1).strip())
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                next_stripped = next_line.lstrip()
                if (
                    next_stripped.startswith("User:")
                    or next_stripped.startswith("user:")
                    or _AI_LINE_RE.match(next_stripped)
                    or next_line.startswith("## ")
                    or next_line.startswith("### ")
                    or next_line.startswith("#### ")
                ):
                    break
                ai_chunks.append(next_line.strip())
                j += 1
            i = j
            continue
        i += 1
    return "\n".join(ai_chunks).lower()


def _session_log_has_invitation_delivery(body: str) -> bool:
    """Return True iff at least one canonical reflection-invitation
    fragment appears in an AI chat line within the Session Log."""
    ai_text = _extract_ai_chat_text(body)
    return any(frag in ai_text for frag in _INVITATION_FRAGMENTS)


def _is_valid_cpat(cpat) -> bool:
    """Return True iff close_protocol_audit_trail is a mapping with
    non-empty reflection_invitation_text. Other fields
    (milestone_check_in_text, recorded_at, etc.) are not required by
    Rule P (b)."""
    if not isinstance(cpat, dict):
        return False
    text = cpat.get("reflection_invitation_text")
    if not isinstance(text, str):
        return False
    return bool(text.strip())


def _infer_close_signal_source(body: str) -> tuple:
    """Infer close_signal_source from Session Log content when the
    frontmatter field is absent. Returns (source, in_persona_present)
    where source is one of 'operator_control_turn',
    'in_persona_clean_exit_only', 'hybrid_turn', or None if no signal
    is detectable. in_persona_present is bool (True only when
    operator_control_turn coexists with an in-persona clean-exit
    utterance from an earlier turn)."""
    log_text = _extract_session_log_text(body)
    has_operator = any(phrase in log_text for phrase in _OPERATOR_CLOSE_PHRASES)
    has_in_persona = any(frag in log_text for frag in _IN_PERSONA_CLEAN_EXIT_FRAGMENTS)

    if has_operator and has_in_persona:
        return ("operator_control_turn", True)
    if has_operator:
        return ("operator_control_turn", False)
    if has_in_persona:
        return ("in_persona_clean_exit_only", False)
    return (None, False)


def validate(path: Path, quiet: bool = False) -> int:
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 3

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        return 3

    # A: file structure — parse frontmatter directly here so we can also get body
    if not text.startswith("---\n"):
        print(f"ERROR [A]: no frontmatter (file does not start with '---') in {path.name}", file=sys.stderr)
        return 1
    end = text.find("\n---\n", 4)
    if end == -1:
        print(f"ERROR [A]: unterminated frontmatter (no closing '---') in {path.name}", file=sys.stderr)
        return 1
    front = text[4:end]
    body = text[end + 5:]
    try:
        fm = yaml.safe_load(front)
    except yaml.YAMLError as e:
        print(f"ERROR [A]: YAML parse failure: {e}", file=sys.stderr)
        return 2

    if fm is None:
        print(f"ERROR [A]: empty frontmatter in {path.name}", file=sys.stderr)
        return 1

    if not isinstance(fm, dict):
        print(f"ERROR [A]: frontmatter is not a YAML mapping in {path.name}", file=sys.stderr)
        return 1

    failures = 0
    warnings = 0

    # B: required keys
    for key in REQUIRED_KEYS:
        if key not in fm:
            print(f"FAIL [B]: missing required key '{key}'")
            failures += 1

    # C: enum values
    status = fm.get("status")
    if status is not None and status not in STATUS_VALUES:
        print(f"FAIL [C]: status='{status}' not in {sorted(STATUS_VALUES)}")
        failures += 1

    active_persona = fm.get("active_persona")
    if active_persona is not None and active_persona not in PERSONA_VALUES:
        print(f"FAIL [C]: active_persona='{active_persona}' not in {sorted(PERSONA_VALUES)}")
        failures += 1

    goal_stack = fm.get("goal_stack")
    if goal_stack is not None and isinstance(goal_stack, list):
        for idx, frame in enumerate(goal_stack):
            if not isinstance(frame, dict):
                print(f"FAIL [C]: goal_stack[{idx}] is not a mapping")
                failures += 1
                continue
            for clarity_key in ("origin_clarity", "destination_clarity"):
                cv = frame.get(clarity_key)
                if cv is not None and cv not in CLARITY_VALUES:
                    print(
                        f"FAIL [C]: goal_stack[{idx}].{clarity_key}='{cv}' "
                        f"not in {sorted(CLARITY_VALUES)}"
                    )
                    failures += 1

    # D: cross-field consistency
    if status == "resolved":
        if goal_stack and isinstance(goal_stack, list):
            for idx, frame in enumerate(goal_stack):
                if isinstance(frame, dict) and frame.get("active") is True:
                    print(
                        f"FAIL [D]: status=resolved but goal_stack[{idx}].active=true; "
                        f"resolved case files should have all frames closed"
                    )
                    failures += 1

    # E: optional-property rules
    stakes_flags = fm.get("stakes_flags")
    if stakes_flags is not None and not isinstance(stakes_flags, list):
        print(f"FAIL [E]: stakes_flags must be a list, got {type(stakes_flags).__name__}")
        failures += 1

    # B-extended: schema_version validation (Sprint 18 Card 08 — schema freeze).
    # Reject explicit unknown values to prevent silent schema drift. Pre-Sprint-18
    # Case Files may declare "1.0"; Sprint 18+ Case Files generated from the
    # frozen template declare "1.0-frozen". Both are accepted; any other value
    # fails validation per the schema-freeze policy documented in chapter 19.
    schema_version_val = fm.get("schema_version")
    if schema_version_val is not None:
        sv_str = str(schema_version_val).strip()
        if sv_str and sv_str not in KNOWN_SCHEMA_VERSIONS:
            print(
                f"FAIL [B]: schema_version={schema_version_val!r} is not in the "
                f"known-schema-versions set {sorted(KNOWN_SCHEMA_VERSIONS)}. "
                f"Sprint 18 Card 08 schema freeze: any schema-version bump "
                f"requires migration-script discipline per chapter 19. Recovery: "
                f"set schema_version to '1.0-frozen' (Sprint 18+ canonical) or "
                f"'1.0' (legacy)."
            )
            failures += 1

    # I: session_mode declaration (chapter 14 §14.6)
    session_mode = fm.get("session_mode")
    test_mode = fm.get("test_mode")
    do_not_archive = fm.get("do_not_archive_to_production")
    if session_mode is None:
        # Field absent — pre-Sprint-13 Case Files lack the field; treat as
        # production with a warning so legacy files do not retroactively fail.
        print(
            "WARN [I]: 'session_mode' frontmatter field is absent — treating as "
            "production. Add 'session_mode: production' to silence this warning "
            "(mandatory for Case Files created after 2026-05-18 per chapter 14)."
        )
        warnings += 1
    elif session_mode not in SESSION_MODE_VALUES:
        print(
            f"FAIL [I]: session_mode='{session_mode}' not in "
            f"{sorted(SESSION_MODE_VALUES)} (chapter 14 §14.6)"
        )
        failures += 1
    else:
        # Cross-field consistency: test-mode flagging
        if session_mode == "test":
            if test_mode is not True:
                print(
                    f"FAIL [I]: session_mode='test' requires test_mode=true, "
                    f"got test_mode={test_mode!r}"
                )
                failures += 1
            if do_not_archive is not True:
                print(
                    f"FAIL [I]: session_mode='test' requires "
                    f"do_not_archive_to_production=true, got {do_not_archive!r}"
                )
                failures += 1
        else:
            if test_mode is True:
                print(
                    f"FAIL [I]: test_mode=true but session_mode='{session_mode}' "
                    f"(test_mode may only be true when session_mode=test)"
                )
                failures += 1

    # F: body content (warnings)
    if "## Frame" not in body and "# Frame" not in body:
        print(f"WARN [F]: no '## Frame' or '# Frame' heading in body — body may be empty or malformed")
        warnings += 1

    # G: detection_check block (chapter 13 §13.2 pre-turn-5 detection check)
    detection_check = fm.get("detection_check")
    if detection_check is None:
        detection_check = find_detection_check_in_body(body)

    if detection_check is None:
        print(
            "FAIL [G]: missing 'detection_check' block "
            "(chapter 13 §13.2 pre-turn-5 detection check was bypassed); "
            "recovery: back-fill with `back_filled_at_turn: N` marker"
        )
        failures += 1
    elif not isinstance(detection_check, dict):
        print(f"FAIL [G]: detection_check must be a mapping, got {type(detection_check).__name__}")
        failures += 1
    else:
        # Required fields
        turn_val = detection_check.get("turn")
        if turn_val is None or not isinstance(turn_val, int):
            print(f"FAIL [G]: detection_check.turn must be an integer, got {turn_val!r}")
            failures += 1

        relaxed = detection_check.get("relaxed_scaffolding")
        if relaxed is None or not isinstance(relaxed, bool):
            print(f"FAIL [G]: detection_check.relaxed_scaffolding must be a boolean, got {relaxed!r}")
            failures += 1

        justification = detection_check.get("justification")
        if not isinstance(justification, str) or not justification.strip():
            print("FAIL [G]: detection_check.justification must be a non-empty string")
            failures += 1

        signals = detection_check.get("signals_observed")
        if not isinstance(signals, list):
            print(f"FAIL [G]: detection_check.signals_observed must be a list, got {type(signals).__name__}")
            failures += 1
        else:
            seen_signals = set()
            for idx, entry in enumerate(signals):
                if not isinstance(entry, dict):
                    print(f"FAIL [G]: detection_check.signals_observed[{idx}] is not a mapping")
                    failures += 1
                    continue
                name = entry.get("signal")
                fired = entry.get("fired")
                evidence = entry.get("evidence")
                if name is None:
                    print(f"FAIL [G]: detection_check.signals_observed[{idx}] missing 'signal' field")
                    failures += 1
                elif name not in CANONICAL_SIGNALS:
                    print(
                        f"FAIL [G]: detection_check.signals_observed[{idx}].signal='{name}' "
                        f"is not canonical (must be one of {sorted(CANONICAL_SIGNALS)})"
                    )
                    failures += 1
                else:
                    seen_signals.add(name)
                if fired is None or not isinstance(fired, bool):
                    print(f"FAIL [G]: detection_check.signals_observed[{idx}].fired must be a boolean, got {fired!r}")
                    failures += 1
                if not isinstance(evidence, str) or not evidence.strip():
                    print(f"FAIL [G]: detection_check.signals_observed[{idx}].evidence must be a non-empty string")
                    failures += 1
            missing = CANONICAL_SIGNALS - seen_signals
            if missing:
                print(
                    f"FAIL [G]: detection_check.signals_observed missing canonical signals: "
                    f"{sorted(missing)} (all 5 must appear, even when fired=false)"
                )
                failures += 1

    # H: library-resolution check (anti compliance-theater)
    tools_entries = extract_tools_applied_entries(body)
    if tools_entries:  # None = absent section (no-op), [] = present but empty
        by_id, by_title = _build_tool_index()
        if not by_id and not by_title:
            print(
                "WARN [H]: tool index could not be built (01-Tools/Tool Entries/ "
                "not found from find_root()) — skipping library resolution"
            )
            warnings += 1
        else:
            for title, tt_id, line_no, is_ad_hoc in tools_entries:
                if is_ad_hoc:
                    continue  # [ad-hoc] entries exempt per chapter 04 §4.3
                resolved = False
                resolution_via = None
                if tt_id and tt_id.lower() in by_id:
                    resolved = True
                    resolution_via = f"Item_ID={tt_id}"
                if not resolved and title:
                    key = _normalize_title(title)
                    if key in by_title:
                        resolved = True
                        resolution_via = f"Title='{title}'"
                if not resolved:
                    id_clause = f" Tool ID='{tt_id}'" if tt_id else ""
                    print(
                        f"FAIL [H]: line {line_no}: Tools Applied entry "
                        f"'### {title}'{id_clause} does not resolve to any entry "
                        f"in 01-Tools/Tool Entries/ (neither by Item_ID nor by "
                        f"canonical Title / filename). Recovery: (a) replace "
                        f"with the correct canonical title via find-tools.py, "
                        f"or (b) flag as ad-hoc by appending '[ad-hoc]' to the "
                        f"H3 header (per chapter 04 §4.3 corpus-gap protocol)."
                    )
                    failures += 1

    # J: standard-mode surface-naming check (chapter 04 §4.3.4)
    #
    # Skipped in relaxed-scaffolding mode (chapter 04 §4.3.2 suppresses
    # chat-naming there). In standard mode, every Tools Applied entry
    # must have its canonical title appear in some "AI [persona]: ..."
    # line in the ## Session Log. Ad-hoc entries are exempt.
    #
    # Sprint 17 Card 03 single-frame relaxation: when frontmatter sets
    # `s2_single_frame_relaxation: true` (single-frame-coherent case per
    # chapter 03 §3.1 Step 8a S2), the by-turn-5 timing sub-check
    # relaxes — per-tool FAIL [J/timing] is suppressed for tools first
    # named after turn 5; instead an aggregate check fires (count of
    # distinct tools first-named in turns 1-5 must be ≥ 2).
    if tools_entries:
        relaxed_for_j = None
        if isinstance(detection_check, dict):
            relaxed_for_j = detection_check.get("relaxed_scaffolding")
        is_relaxed_mode = relaxed_for_j is True
        s2_relaxed = bool(fm.get("s2_single_frame_relaxation")) if isinstance(fm, dict) else False
        s2_relaxed_reason = fm.get("s2_single_frame_relaxation_reason") if isinstance(fm, dict) else None
        if s2_relaxed and not (isinstance(s2_relaxed_reason, str) and s2_relaxed_reason.strip()):
            print(
                "WARN [J]: 's2_single_frame_relaxation: true' is set without "
                "a written 's2_single_frame_relaxation_reason' — the "
                "single-frame-coherent justification must be documented per "
                "chapter 04 §4.3.4 (Sprint 17 Card 03) and chapter 03 §3.1 "
                "Step 8a S2. Premature relaxation is a frame-laziness failure."
            )
            warnings += 1
        if not is_relaxed_mode:
            ai_chat = extract_ai_chat_text(body)
            if not ai_chat.strip():
                print(
                    "WARN [J]: standard-mode surface-naming check skipped — "
                    "## Session Log has no 'AI [persona]: ...' lines "
                    "(transcript unavailable, cannot verify per chapter 04 "
                    "§4.3.4)."
                )
                warnings += 1
            else:
                ai_chat_norm = _normalize_title(ai_chat)
                # Sprint 16 Card 03: also extract per-turn AI chat for the
                # timing sub-check (first-naming turn must be ≤5 per
                # chapter 04 §4.3.4 first-invocation rule).
                ai_chat_by_turn = extract_ai_chat_by_turn(body)
                ai_by_turn_norm = [
                    (turn_n, _normalize_title(text))
                    for turn_n, text in ai_chat_by_turn
                ]
                # Sprint 17 Card 03: track distinct tools first-named in
                # turns 1-5 for the aggregate check under
                # s2_single_frame_relaxation.
                j_timing_by_turn_5_titles: set[str] = set()
                for title, tt_id, line_no, is_ad_hoc in tools_entries:
                    if is_ad_hoc:
                        continue
                    if not title:
                        continue
                    # Sprint 18 Card 05: compound-title alias matching. Accept
                    # any alias (full title or either side of a top-level slash)
                    # as evidence of canonical naming in chat.
                    # Sprint 18 Card 06: canonical-vs-descriptive distinction.
                    # Canonical = Title-cased substring in raw AI chat (counts
                    # toward §4.3.4 timing target); descriptive phrasal =
                    # only normalized (case-insensitive) substring match
                    # (INFO output; does NOT count toward target). Both still
                    # satisfy Rule J's existence check.
                    title_aliases = _title_aliases(title)
                    title_norm = title_aliases[0] if title_aliases else ""
                    title_aliases_raw = _title_aliases_raw(title)
                    canonical_in_chat = bool(
                        title_aliases_raw
                        and any(a and a in ai_chat for a in title_aliases_raw)
                    )
                    normalized_in_chat = bool(
                        title_aliases
                        and any(alias in ai_chat_norm for alias in title_aliases)
                    )
                    descriptive_phrasal_only = (
                        normalized_in_chat and not canonical_in_chat
                    )
                    if not normalized_in_chat:
                        # Sprint 18 Card 12 — Rule J ↔ §6.4.0 spec contract
                        # enforcement. When the placeholder pattern is used in
                        # the Session Log, the verbatim canonical title is
                        # absent from AI [persona]: lines. The §6.4.0 spec
                        # contract (Sprint 15 Card 07) treats a structurally
                        # complete `tool_surfaced_in_chat` annotation as
                        # equivalent evidence. Check that pathway before FAIL.
                        annotation_turn = _check_tool_surfaced_annotation(fm, title)
                        if annotation_turn is not None:
                            print(
                                f"INFO [J]: canonical-title '{title}' at turn "
                                f"{annotation_turn} accepted via "
                                f"tool_surfaced_in_chat annotation (placeholder "
                                f"pattern, §6.4.0 — Sprint 18 Card 12 spec "
                                f"contract enforcement). Equivalent to verbatim "
                                f"presence per Sprint 15 Card 07."
                            )
                            # Annotation accepted; treat as canonical-naming
                            # presence for both Rule J existence + Sprint 16
                            # Card 03 timing sub-check.
                            if title_norm and annotation_turn <= 5:
                                j_timing_by_turn_5_titles.add(title_norm)
                            continue
                        id_clause = f" Tool ID='{tt_id}'" if tt_id else ""
                        print(
                            f"FAIL [J]: line {line_no}: Tools Applied entry "
                            f"'### {title}'{id_clause} is logged but its "
                            f"canonical title does not appear verbatim in any "
                            f"'AI [persona]: ...' line in the ## Session Log "
                            f"(standard-mode surface-naming required per "
                            f"chapter 04 §4.3.4) AND no equivalent "
                            f"`tool_surfaced_in_chat` annotation is present "
                            f"(§6.4.0 placeholder-pattern pathway). Recovery: "
                            f"(a) name the tool by its canonical title in the "
                            f"next AI response; (b) populate "
                            f"`tool_surfaced_in_chat` with `tool: '{title}'`, "
                            f"`turn: <N>`, `evidence: '<brief>'` per the "
                            f"§6.4.0 placeholder pattern; or (c) set "
                            f"detection_check.relaxed_scaffolding=true if the "
                            f"session was sophisticated-user relaxed mode."
                        )
                        failures += 1
                        continue
                    if descriptive_phrasal_only:
                        # Find the first turn where the normalized form appears
                        # to attach a turn number to the INFO message.
                        first_phrasal_turn: int | None = None
                        for turn_n, text_norm in ai_by_turn_norm:
                            if any(a in text_norm for a in title_aliases):
                                first_phrasal_turn = turn_n
                                break
                        turn_clause = (
                            f" at turn {first_phrasal_turn}"
                            if first_phrasal_turn is not None
                            else ""
                        )
                        print(
                            f"INFO [J]: descriptive phrasal use of "
                            f"'{title}'{turn_clause} — not counted toward "
                            f"canonical naming target (Sprint 18 Card 06 — "
                            f"chapter 04 §4.3.4 canonical-naming definition). "
                            f"Recovery if canonical naming desired: use the "
                            f"Title-cased canonical form as a named "
                            f"methodology, not the lowercase-hyphenated "
                            f"activity-shape phrasing."
                        )
                        # Treat as Rule J pass but exclude from timing-count
                        # (skip the j_timing_by_turn_5_titles addition below).
                        continue
                    # Sprint 16 Card 03 timing sub-check — first-naming
                    # turn must be ≤5. Find the earliest turn in which
                    # the canonical title appears in AI chat.
                    # Sprint 17 Card 03: under s2_single_frame_relaxation,
                    # the per-tool FAIL is suppressed; an aggregate count
                    # check fires after the loop (≥ 2 distinct tools
                    # first-named in turns 1-5).
                    if title_norm:
                        first_turn: int | None = None
                        for turn_n, text_norm in ai_by_turn_norm:
                            if title_norm in text_norm:
                                first_turn = turn_n
                                break
                        if first_turn is not None and first_turn <= 5:
                            j_timing_by_turn_5_titles.add(title_norm)
                        if first_turn is not None and first_turn > 5:
                            if s2_relaxed:
                                # Per-tool failure suppressed under
                                # single-frame relaxation; aggregate
                                # count check below enforces the ≥ 2
                                # floor instead.
                                pass
                            else:
                                id_clause = f" Tool ID='{tt_id}'" if tt_id else ""
                                print(
                                    f"FAIL [J/timing]: line {line_no}: Tools "
                                    f"Applied entry '### {title}'{id_clause} "
                                    f"first appears in AI chat at turn "
                                    f"{first_turn} — past the by-turn-5 "
                                    f"timing target (chapter 04 §4.3.4 first-"
                                    f"invocation rule, Sprint 16 Card 03). "
                                    f"Recovery: surface lightly-applied moves "
                                    f"at the moment of first invocation, not "
                                    f"deferred to a later turn 'where the "
                                    f"tool earns its place.' Set "
                                    f"detection_check.relaxed_scaffolding="
                                    f"true if the session was sophisticated-"
                                    f"user relaxed mode. Or set "
                                    f"s2_single_frame_relaxation=true in "
                                    f"frontmatter (with reason documented) "
                                    f"if the case is single-frame coherent "
                                    f"per chapter 03 §3.1 Step 8a S2 "
                                    f"(Sprint 17 Card 03)."
                                )
                                failures += 1
                # Sprint 17 Card 03 aggregate check: under
                # s2_single_frame_relaxation, the by-turn-5 distinct-count
                # must still be ≥ 2 (the relaxation floor). The baseline
                # ≥ 3 target is enforced per-tool above; under relaxation
                # we accept ≥ 2 as the new floor.
                if s2_relaxed and len(j_timing_by_turn_5_titles) < 2:
                    print(
                        f"FAIL [J/timing]: under s2_single_frame_relaxation, "
                        f"only {len(j_timing_by_turn_5_titles)} distinct "
                        f"canonical-title chat mention(s) appear in turns 1-5 "
                        f"— the single-frame-relaxation floor is ≥ 2 (chapter "
                        f"04 §4.3.4 Sprint 17 Card 03). Recovery: name at "
                        f"least 2 distinct tools by canonical title in turns "
                        f"1-5, or clear s2_single_frame_relaxation if the "
                        f"case is not genuinely single-frame coherent."
                    )
                    failures += 1

    # K: Session Log turn-ordering (Sprint 16 Card 04)
    turn_headers = extract_session_log_turn_headers(body)
    if turn_headers:
        # Compute body→file line offset (frontmatter ends at the `\n---\n`
        # boundary found earlier; body line numbers are 1-based relative
        # to body start, so file line = body_line + (frontmatter_lines + 2)).
        body_start_file_line = text[:end + 5].count("\n") + 1
        out_of_order = []
        prev = None
        for turn_n, body_line, _ts in turn_headers:
            if prev is not None and turn_n < prev:
                file_line = body_start_file_line + body_line - 1
                out_of_order.append((turn_n, file_line))
            prev = max(prev, turn_n) if prev is not None else turn_n
        for turn_n, file_line in out_of_order:
            print(
                f"FAIL [K]: line {file_line}: '#### Turn {turn_n}' "
                f"appears after a higher turn number — Session Log turn "
                f"headers must be monotonically increasing (Sprint 16 "
                f"Card 04). Recovery: reorder the turn block to match "
                f"the chronological sequence."
            )
            failures += 1

    # N: timestamp monotonicity (Sprint 16 Card 04)
    if turn_headers:
        body_start_file_line = text[:end + 5].count("\n") + 1
        prev_ts = None
        prev_turn = None
        for turn_n, body_line, ts in turn_headers:
            if ts is None:
                continue
            if prev_ts is not None and ts < prev_ts:
                file_line = body_start_file_line + body_line - 1
                print(
                    f"FAIL [N]: line {file_line}: '#### Turn {turn_n}' "
                    f"timestamp {ts!r} is earlier than the previous "
                    f"turn ({prev_turn}) timestamp {prev_ts!r}. Session "
                    f"Log timestamps must be non-decreasing (Sprint 16 "
                    f"Card 04). Recovery: correct the timestamp or "
                    f"reorder the turn block."
                )
                failures += 1
            prev_ts = ts
            prev_turn = turn_n

    # L: reverse Rule J — chat-named, not logged (Sprint 16 Card 04)
    # Scan AI chat for any canonical library title that's not in
    # Tools Applied entries. Skip in relaxed-mode sessions (parallel
    # to Rule J's relaxed-mode skip — relaxed mode suppresses chat-
    # naming, so reverse-Rule-J would over-fire in that mode).
    #
    # False-positive guard: match canonical titles as word-boundary
    # phrases in original chat text (not normalized-substring), and
    # skip incidental-mention contexts ("closest library entry",
    # "nearest analog to X is", "not in 01-Tools/", "ad-hoc relative
    # to library") so the rule only flags declarative tool uses.
    if tools_entries is not None:
        relaxed_for_l = None
        if isinstance(detection_check, dict):
            relaxed_for_l = detection_check.get("relaxed_scaffolding")
        is_relaxed_for_l = relaxed_for_l is True
        if not is_relaxed_for_l:
            scripts_dir = Path(__file__).resolve().parent
            library_titles = extract_tool_library_titles(scripts_dir)
            if library_titles:
                ai_chat = extract_ai_chat_text(body)
                # Sprint 18 Card 05: build alias set covering compound-title
                # variations of every logged title. When a Tools Applied entry
                # has H3 header "### Critical Chain / Critical Path", any of
                # {full normalized form, "criticalchain", "criticalpath"}
                # counts as having logged the tool. Without alias coverage,
                # Rule L spuriously flags chat-form references to compound-
                # title tools.
                logged_titles_norm: set[str] = set()
                for t, _id, _ln, _ah in tools_entries:
                    if not t:
                        continue
                    for alias in _title_aliases(t):
                        logged_titles_norm.add(alias)
                # Incidental-mention context patterns — when a canonical
                # title appears within ~80 chars of these phrases, the
                # AI is naming the tool as a library reference, not
                # applying it as an analytical move.
                incidental_context_re = re.compile(
                    r"(closest\s+library\s+entry|nearest\s+analog|"
                    r"not\s+(?:in|currently\s+in)\s+(?:01-Tools|"
                    r"the\s+(?:library|corpus))|ad-?hoc\s+relative\s+"
                    r"to\s+(?:library|corpus)|corpus\s+gap|"
                    r"the\s+library\s+does\s+not\s+contain|"
                    r"recommendation\s+for\s+corpus)",
                    re.IGNORECASE,
                )
                for canonical in library_titles:
                    canon_norm = _normalize_title(canonical)
                    if not canon_norm:
                        continue
                    # Length guard: skip ≤4 normalized chars to reduce
                    # false positives on short tokens like "TRE" or
                    # "RICE" that occur as fragments in unrelated words.
                    if len(canon_norm) <= 4:
                        continue
                    # Word-boundary, case-insensitive phrase match.
                    # Hyphens are matched literally (treated as word
                    # chars under \b in re).
                    pattern = re.compile(
                        r"\b" + re.escape(canonical) + r"\b",
                        re.IGNORECASE,
                    )
                    match = pattern.search(ai_chat)
                    if not match:
                        continue
                    if canon_norm in logged_titles_norm:
                        continue
                    # Check incidental-mention context within ±100 chars
                    start = max(0, match.start() - 100)
                    end_idx = min(len(ai_chat), match.end() + 100)
                    context_window = ai_chat[start:end_idx]
                    if incidental_context_re.search(context_window):
                        continue
                    print(
                        f"FAIL [L]: canonical title '{canonical}' "
                        f"appears in AI chat but is NOT logged as a "
                        f"### [Tool] entry in ## Tools Applied "
                        f"(Sprint 16 Card 04 reverse Rule J). "
                        f"Recovery: add a `### {canonical}` entry "
                        f"with the matching Tool ID to Tools "
                        f"Applied, OR if the chat mention was "
                        f"incidental (not an applied move), rephrase "
                        f"to avoid the canonical-title pattern in chat."
                    )
                    failures += 1

    # M: action-package structural completeness (Sprint 16 Card 04)
    # Detect action-package delivery turn via the chapter 09 §4.3
    # "delivered as action package at turn N" marker in Frame body OR
    # the keyword "action package" in AI chat. When detected, scan the
    # AI chat output for the 4 §3.1 step 8 components.
    ap_marker_re = re.compile(
        r"delivered as action package at turn (\d+)|"
        r"action[- ]package commitment|"
        r"action package delivery",
        re.IGNORECASE,
    )
    ap_match = ap_marker_re.search(body)
    if ap_match:
        ai_chat_by_turn_for_m = extract_ai_chat_by_turn(body)
        # Rule M precision: only FAIL when the action-package turn is
        # unambiguously identifiable. Two confidence levels:
        #   HIGH: marker explicitly names "at turn N" → check that turn
        #   MEDIUM: an AI chat line contains a "see turn-N chat output"
        #     annotation → that turn IS annotation-form by definition,
        #     so structural verification is impossible — emit WARN, not
        #     FAIL (the verbatim lives outside the CF).
        #   LOW: no turn-name found → emit WARN, do not FAIL on highest
        #     turn heuristic (turn-numbering for the action-package can
        #     drift across CF formats, e.g., highest turn is often the
        #     close turn, not the action-package turn).
        target_turn = None
        confidence: str = "LOW"
        try:
            target_turn = int(ap_match.group(1)) if ap_match.group(1) else None
        except (IndexError, TypeError):
            target_turn = None
        if target_turn is not None:
            confidence = "HIGH"
        else:
            see_turn_re = re.compile(
                r"see\s+turn[-\s]+(\d+)\s+chat\s+output", re.IGNORECASE
            )
            for tn, ai_text in ai_chat_by_turn_for_m:
                m_st = see_turn_re.search(ai_text)
                if m_st:
                    try:
                        target_turn = int(m_st.group(1))
                        confidence = "MEDIUM"
                    except ValueError:
                        pass
                    break
        if confidence == "LOW":
            print(
                f"WARN [M]: action-package marker detected but the "
                f"action-package turn is not unambiguously identifiable "
                f"in this Case File. Rule M cannot verify §3.1 step 8 "
                f"structural completeness without a clear turn anchor; "
                f"defer to Card-12 acceptance-gate review (Sprint 16 "
                f"Card 04 heuristic-precision guard)."
            )
            warnings += 1
            chat_to_check = ""
        elif confidence == "MEDIUM":
            print(
                f"WARN [M]: action-package delivery at turn {target_turn} "
                f"is annotation-form ('see turn-{target_turn} chat "
                f"output' marker) — the verbatim response lives outside "
                f"the Case File. Rule M cannot verify §3.1 step 8 "
                f"completeness on annotation-form turns; defer to "
                f"Card-12 acceptance-gate review."
            )
            warnings += 1
            chat_to_check = ""
        else:
            chat_to_check = "\n".join(
                text for tn, text in ai_chat_by_turn_for_m if tn == target_turn
            )

        if chat_to_check.strip():
            # Meta-annotation skip: if the entire chat content for this
            # action-package turn is annotation-form (e.g.,
            # "[full verbatim response delivered in chat — see turn-N
            # chat output]"), the structural-completeness check cannot
            # verify the actual chat — Rule M skips. The verbatim chat
            # lives outside the Case File and must be checked separately
            # (typically by Card 12 acceptance-gate review).
            non_annotation_chat = re.sub(
                r"\[(?:full\s+verbatim\s+response\s+delivered|"
                r"delivered\s+(?:in\s+chat|verbatim)|"
                r"see\s+turn-\d+\s+chat\s+output)[^\]]*\]",
                "",
                chat_to_check,
                flags=re.IGNORECASE,
            ).strip()
            if not non_annotation_chat:
                # All chat was annotation-form — defer to acceptance-gate
                # review; do not flag as a Rule M failure.
                chat_to_check = ""
        if chat_to_check.strip():
            chat_lower = chat_to_check.lower()
            components_missing = []
            # (a) primary problem named
            if not re.search(r"\bprimary problem\b|\bcore problem\b|\bthe\s+problem\s+is\b", chat_lower):
                components_missing.append("primary problem")
            # (b) committed sequence anchor
            if not re.search(r"\b(week\s*1|day\s*1|monday|tomorrow|today|by\s+\w+day)\b", chat_lower):
                components_missing.append("committed sequence anchor")
            # (c) ≥1 stakeholder draft section
            # Sprint 17 Card 04: case-insensitive + expanded lexical
            # surface. Accept stakeholder-draft signals in any of the
            # standard shapes the AI uses to title a draft section
            # (H3 heading, inline label, bracketed title). The
            # case-sensitive pre-Sprint-17 pattern forced Mara to
            # rewrite the section title twice ("Draft outreach
            # message" vs "draft outreach message").
            stakeholder_draft_patterns = [
                # H3 heading with action-package noun
                r"###\s*\[?[a-z][\w\s/-]*\]?\s*"
                r"(?:offer|outreach|conversation|brief|"
                r"opening\s+message|outreach\s+script|"
                r"introduction(?:\s+message)?|invitation|"
                r"talking\s+points|draft\s+message)",
                # Inline "stakeholder X" phrase
                r"stakeholder\s+"
                r"(?:draft|brief|opening|message|outreach|"
                r"conversation|talking\s+points)",
                # Inline "draft X" phrase
                r"draft\s+"
                r"(?:message|outreach|email|opening|conversation|"
                r"introduction|invitation|talking\s+points)\b",
                # Inline "opening X" / "outreach X" / "introduction X"
                # phrases (Mara's "opening message" naming style)
                r"\bopening\s+(?:message|conversation|outreach)\b",
                r"\boutreach\s+(?:message|script|email|conversation)\b",
                r"\bintroduction\s+(?:message|email|outreach)\b",
                r"\binvitation\s+(?:message|email|to)\b",
                r"\btalking\s+points\b",
            ]
            if not any(
                re.search(p, chat_to_check, re.IGNORECASE)
                for p in stakeholder_draft_patterns
            ):
                components_missing.append("stakeholder draft section")
            # (d) today's tasks list
            if not re.search(r"\b(today|monday morning|today's|immediate)\s*[:—-]|(?:\btask|\bnext step)s?\s*[:—-]", chat_lower):
                components_missing.append("immediate tasks list")
            if components_missing:
                turn_label = f"turn {target_turn}" if target_turn else "the session"
                print(
                    f"FAIL [M]: action-package delivery detected at "
                    f"{turn_label} but the AI chat output is missing "
                    f"§3.1 step 8 component(s): "
                    f"{', '.join(components_missing)}. Sprint 16 Card 04 "
                    f"action-package structural completeness check. "
                    f"Recovery: amend the delivery turn (or follow-up "
                    f"turn) to surface the missing component(s) before "
                    f"close."
                )
                failures += 1

    # O: last_persona_switch structural completeness (Sprint 16 Card 09)
    # When populated, last_persona_switch must be a mapping with all four
    # required fields. Bare-timestamp values (the pre-Sprint-16 format)
    # are rejected because the switch context (from / to / reason) is
    # load-bearing audit evidence — bare timestamps lose it.
    lps = fm.get("last_persona_switch")
    if lps is not None:
        if not isinstance(lps, dict):
            print(
                f"FAIL [O]: last_persona_switch must be a mapping with "
                f"fields {{timestamp, from, to, reason}}, got "
                f"{type(lps).__name__}: {lps!r}. Sprint 16 Card 09 "
                f"structural completeness — bare-timestamp format is "
                f"rejected. Recovery: convert to the structured object "
                f"format (chapter 06 _TEMPLATE.md)."
            )
            failures += 1
        else:
            required_lps_fields = ("timestamp", "from", "to", "reason")
            missing_lps = [f for f in required_lps_fields if f not in lps]
            if missing_lps:
                print(
                    f"FAIL [O]: last_persona_switch is missing required "
                    f"field(s): {missing_lps}. All four fields "
                    f"(timestamp, from, to, reason) MUST be present when "
                    f"the switch is populated (Sprint 16 Card 09)."
                )
                failures += 1
            else:
                # Sanity-check non-empty string fields
                for fld in ("to", "reason"):
                    val = lps.get(fld)
                    if not isinstance(val, str) or not val.strip():
                        print(
                            f"FAIL [O]: last_persona_switch.{fld} must "
                            f"be a non-empty string, got {val!r}."
                        )
                        failures += 1

    # O (extension, Sprint 17 Card 08): audit_known_coverage_gaps
    # structural completeness. When populated, each entry must be a
    # mapping with the 6 required fields (script, flagged_phrase, mode,
    # spec_status, gap_diagnosis, remediation_decision); line and
    # user_invitation_present are optional. Schema documented in
    # chapter 06 §6.13 step 0.1.
    akcg = fm.get("audit_known_coverage_gaps")
    if akcg is not None and akcg != []:
        if not isinstance(akcg, list):
            print(
                f"FAIL [O]: audit_known_coverage_gaps must be a list (or [] "
                f"if empty), got {type(akcg).__name__}: {akcg!r} "
                f"(Sprint 17 Card 08). Recovery: convert to YAML list "
                f"format per _TEMPLATE.md schema."
            )
            failures += 1
        else:
            required_akcg_fields = (
                "script",
                "flagged_phrase",
                "mode",
                "spec_status",
                "gap_diagnosis",
                "remediation_decision",
            )
            allowed_modes = {"standard", "relaxed", "n/a"}
            allowed_spec_status = {"permitted", "required", "forbidden"}
            for idx, entry in enumerate(akcg):
                if not isinstance(entry, dict):
                    print(
                        f"FAIL [O]: audit_known_coverage_gaps[{idx}] must be "
                        f"a mapping, got {type(entry).__name__}: {entry!r} "
                        f"(Sprint 17 Card 08)."
                    )
                    failures += 1
                    continue
                missing_akcg = [
                    f for f in required_akcg_fields if f not in entry
                    or not str(entry.get(f) or "").strip()
                ]
                if missing_akcg:
                    print(
                        f"FAIL [O]: audit_known_coverage_gaps[{idx}] is "
                        f"missing required field(s): {missing_akcg}. "
                        f"All 6 fields (script, flagged_phrase, mode, "
                        f"spec_status, gap_diagnosis, remediation_decision) "
                        f"MUST be present per chapter 06 §6.13 step 0.1 "
                        f"(Sprint 17 Card 08)."
                    )
                    failures += 1
                    continue
                # Enum sanity-checks
                mode_val = str(entry.get("mode") or "").strip().lower()
                if mode_val not in allowed_modes:
                    print(
                        f"FAIL [O]: audit_known_coverage_gaps[{idx}].mode "
                        f"must be one of {sorted(allowed_modes)}; got "
                        f"{entry.get('mode')!r} (Sprint 17 Card 08)."
                    )
                    failures += 1
                spec_status_val = str(entry.get("spec_status") or "").strip().lower()
                # spec_status may contain trailing prose (Sprint 16 Yelena
                # used "permitted — chapter 13 §13.2 ..."); accept the
                # canonical prefix.
                if not any(
                    spec_status_val.startswith(s) for s in allowed_spec_status
                ):
                    print(
                        f"FAIL [O]: audit_known_coverage_gaps[{idx}]."
                        f"spec_status must start with one of "
                        f"{sorted(allowed_spec_status)}; got "
                        f"{entry.get('spec_status')!r} (Sprint 17 Card 08)."
                    )
                    failures += 1

    # P: close-protocol audit-trail recording (Sprint 18 Card 03)
    # Fires only when status == resolved. Three branches based on
    # close_signal_source (declared in frontmatter, or inferred from
    # Session Log content when absent).
    status_val = (fm.get("status") or "").strip().lower()
    if status_val == "resolved":
        close_signal_source = fm.get("close_signal_source")
        in_persona_clean_exit_present = bool(fm.get("in_persona_clean_exit_present"))
        cpat = fm.get("close_protocol_audit_trail")

        if close_signal_source is None or (isinstance(close_signal_source, str) and not close_signal_source.strip()):
            inferred_source, inferred_in_persona = _infer_close_signal_source(body)
            if inferred_source is None:
                print(
                    f"FAIL [P]: status=resolved but close_signal_source "
                    f"frontmatter field is absent and Session Log content "
                    f"does not contain a recognizable close signal "
                    f"(operator 'Test complete' / 'Holodeck closed' OR "
                    f"in-persona clean-exit utterance). Sprint 18 Card 03 "
                    f"§14.2 requires close_signal_source ∈ "
                    f"{{operator_control_turn, in_persona_clean_exit_only, "
                    f"hybrid_turn}} when status=resolved."
                )
                failures += 1
                close_signal_source = None
            else:
                close_signal_source = inferred_source
                in_persona_clean_exit_present = inferred_in_persona
                print(
                    f"WARN [P]: status=resolved but close_signal_source "
                    f"frontmatter field absent — inferred "
                    f"close_signal_source={inferred_source!r} from Session "
                    f"Log content (Sprint 17 carry-forward). Recovery: "
                    f"populate the frontmatter field explicitly per chapter "
                    f"14 §14.2 Audit-trail recording sub-section."
                )
                warnings += 1

        if close_signal_source == "operator_control_turn":
            if in_persona_clean_exit_present:
                # Branch (a): hybrid path — visible delivery required in Session Log
                if not _session_log_has_invitation_delivery(body):
                    print(
                        f"FAIL [P]: close_signal_source=operator_control_turn "
                        f"with in_persona_clean_exit_present=true but no "
                        f"reflection-invitation delivery found in Session "
                        f"Log AI lines. Sprint 18 Card 03 §14.2 hybrid-turn "
                        f"path: when the operator's close signal carries a "
                        f"quoted in-persona clean-exit utterance, the "
                        f"invitation IS delivered to the in-persona test "
                        f"user via the AI chat line."
                    )
                    failures += 1
            else:
                # Branch (b): canonical suppressed-to-operator — CPAT required
                if not _is_valid_cpat(cpat):
                    print(
                        f"FAIL [P]: close_signal_source=operator_control_turn "
                        f"with in_persona_clean_exit_present=false REQUIRES "
                        f"close_protocol_audit_trail with non-empty "
                        f"reflection_invitation_text. Sprint 18 Card 03 §14.2 "
                        f"suppressed-to-operator path: no chat-side delivery "
                        f"exists, so the frontmatter audit-trail entry IS the "
                        f"audit-completeness signal. Got "
                        f"close_protocol_audit_trail={cpat!r}."
                    )
                    failures += 1
        elif close_signal_source == "in_persona_clean_exit_only":
            # Branch (c): visible delivery required in Session Log
            if not _session_log_has_invitation_delivery(body):
                print(
                    f"FAIL [P]: close_signal_source=in_persona_clean_exit_only "
                    f"but no reflection-invitation delivery found in Session "
                    f"Log AI lines. Sprint 18 Card 03 §14.2 + §6.13.1: "
                    f"in-persona close MUST deliver the invitation as a "
                    f"direct chat question to the in-persona test user "
                    f"(verbose §6.13 step 3 or single-line §6.13.1 variant)."
                )
                failures += 1
        elif close_signal_source == "hybrid_turn":
            # Hybrid turn (both signals in same operator turn) — visible delivery required
            if not _session_log_has_invitation_delivery(body):
                print(
                    f"FAIL [P]: close_signal_source=hybrid_turn requires "
                    f"visible reflection-invitation delivery in Session Log "
                    f"AI lines (§14.2 hybrid rule: in-persona utterance "
                    f"governs, invitation delivered to in-persona test user)."
                )
                failures += 1
        elif close_signal_source is not None:
            print(
                f"FAIL [P]: close_signal_source must be one of "
                f"{{operator_control_turn, in_persona_clean_exit_only, "
                f"hybrid_turn}}; got {close_signal_source!r}."
            )
            failures += 1

    # Q: financial_catastrophe routing-grade restoration (Sprint 19 Card 04-D)
    #
    # Trigger: any stakes_flags_logging OR stakes_flags_routing entry with
    # category=<X>_pending_regime AND routed=false.
    #
    # Check: if any subsequent turn in the body shows regime-clarifying
    # signals (explicit regime mention, SOX-applicability assertion, GAAP-
    # restatement language, materiality recomputation, IPO-track regime
    # declaration, Exchange Act reporting assertion, Form 8-K Item 4.02
    # mention), the frontmatter MUST contain a subsequent entry restoring
    # the routing-grade category (with routed=true) OR explicitly
    # downgrading to a different stakes category. Leaving the entry as
    # _pending_regime with routed=false indefinitely is the regression
    # this rule catches (Yelena Sprint 19 Case File at
    # `06-Case-Files/_ACTIVE/test_mode_20260524_012339_gc-arr-overstatement.md`
    # was the canonical case: turn-1 financial_catastrophe_pending_regime
    # was never restored after the turn-2 IPO-track-private regime
    # clarification).
    #
    # If no clarifying signal present, the pending state may be legitimate
    # (regime genuinely uncharacterized) — emit WARN only.
    _CLARIFYING_REGIME_PATTERNS = [
        re.compile(r"\b[Rr]egime\s*:", re.IGNORECASE),
        re.compile(r"\bSOX\s+(?:applies|applicability|exposure|carve-?out|disqualified|preempted)", re.IGNORECASE),
        re.compile(r"\bASC\s+606\b", re.IGNORECASE),
        re.compile(r"\bGAAP\s+(?:restatement|consolidation|materiality|recompute|recomputed)", re.IGNORECASE),
        re.compile(r"\bmateriality\s+(?:recompute|recomputation|recomputed|recalculated|locked|clarified)", re.IGNORECASE),
        re.compile(r"\bForm\s+8-K\s+Item\s+4\.02", re.IGNORECASE),
        re.compile(r"\bIPO-track\s+(?:private|public)", re.IGNORECASE),
        re.compile(r"\bExchange\s+Act\s+reporting", re.IGNORECASE),
        re.compile(r"\bDelaware\s+C-corp\b", re.IGNORECASE),
    ]
    for flag_field in ("stakes_flags_logging", "stakes_flags_routing"):
        entries = fm.get(flag_field)
        if not isinstance(entries, list):
            continue
        for idx, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            category = entry.get("category", "")
            routed = entry.get("routed")
            if not (isinstance(category, str)
                    and category.endswith("_pending_regime")
                    and routed is False):
                continue
            pending_turn = entry.get("turn")
            base_category = category[: -len("_pending_regime")]
            # Check 1: any subsequent entry in the same field restoring or
            # downgrading the stakes category?
            has_restoration = False
            for later_entry in entries[idx + 1:]:
                if not isinstance(later_entry, dict):
                    continue
                later_cat = later_entry.get("category", "")
                if not isinstance(later_cat, str):
                    continue
                # Routing-grade restoration: same base category, routed=true
                if later_cat == base_category and later_entry.get("routed") is True:
                    has_restoration = True
                    break
                # Explicit downgrade: any other category named for this
                # stakes-family (different from the original pending category)
                if later_cat and later_cat != category:
                    has_restoration = True
                    break
            if has_restoration:
                continue
            # Check 2: did the body show regime-clarifying signals?
            clarifying_found = any(
                pattern.search(body) for pattern in _CLARIFYING_REGIME_PATTERNS
            )
            if clarifying_found:
                print(
                    f"FAIL [Q]: stakes-flag '{category}' at {flag_field}[{idx}] "
                    f"(turn {pending_turn}) not restored to routing-grade "
                    f"({base_category} with routed=true) or downgraded after "
                    f"regime-clarifying signal in subsequent turns. "
                    f"Sprint 19 Card 04-D Rule Q: when disclosure-regime "
                    f"clarifies, the pending stakes-flag MUST be updated in "
                    f"frontmatter to either the routing-grade category or an "
                    f"explicit downgrade. Leaving it as '_pending_regime' "
                    f"with routed=false indefinitely is the regression this "
                    f"rule closes (Yelena Sprint 19 canonical case)."
                )
                failures += 1
            else:
                print(
                    f"WARN [Q]: stakes-flag '{category}' at {flag_field}[{idx}] "
                    f"(turn {pending_turn}) is pending and no regime-clarifying "
                    f"signal detected in subsequent body turns. Pending state "
                    f"may be legitimate (regime genuinely uncharacterized)."
                )
                warnings += 1

    if failures == 0 and not quiet:
        print(f"OK: {path.name} ({warnings} warning(s))")
    elif failures > 0:
        print(f"FAILED: {path.name} ({failures} failure(s), {warnings} warning(s))")

    return 1 if failures > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Case File against the SOLVE eX Case File schema."
    )
    parser.add_argument("path", type=Path, help="Path to a Case File .md file")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress per-file OK output (still print failures and warnings)",
    )
    args = parser.parse_args()

    # Resolve relative paths against the root if not absolute
    path = args.path
    if not path.is_absolute():
        try:
            root = find_root()
            candidate = (root / path).resolve()
            if candidate.is_file():
                path = candidate
        except RuntimeError:
            pass

    return validate(path, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
