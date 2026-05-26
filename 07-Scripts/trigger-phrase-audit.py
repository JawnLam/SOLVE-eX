#!/usr/bin/env python3
"""trigger-phrase-audit.py — verify mandatory-trigger tools surfaced when required.

Scans a Case File's Session Log for mandatory-trigger phrases in user utterances
and verifies the corresponding tool surfaced in the immediately-following AI
response. A trigger that fires without a tool surface AND without a logged
`trigger_fired_tool_skipped` justification is a violation.

The first mandatory-trigger tool wired into the audit is Conviction-vs-Argument
(chapter 04 §4.3.3 — five canonical trigger patterns). Future tools with the
same trigger-list semantics can be added to TRIGGER_TOOLS without rewriting
the audit loop.

Exit codes:
  0 = all triggers handled (tool surfaced OR justified skip logged)
  1 = at least one trigger violation
  2 = invalid Case File (no Session Log, frontmatter parse failure)
  3 = file not found

Example:
  python3 trigger-phrase-audit.py ../06-Case-Files/_ARCHIVED/example-job-decision.md
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import find_root  # noqa: E402

import yaml  # noqa: E402


# ---------------------------------------------------------------------------
# Trigger-tool registry
# Each entry: (tool_id, trigger_patterns, tool_surface_patterns)
#   trigger_patterns: list of compiled regexes that fire on user utterances
#   tool_surface_patterns: list of compiled regexes that confirm tool surface
#     in the AI response (canonical title OR three-layer structure markers)
# ---------------------------------------------------------------------------

CONVICTION_VS_ARGUMENT_TRIGGERS = [
    # Pattern 1: "Am I letting X contaminate Y" + paraphrases
    re.compile(
        r"\b(am i|i'?m)\s+(letting|allowing|having)\s+(my\s+)?\w+.*"
        r"(contaminat|distort|skew|bias|cloud|color|taint|warp)",
        re.IGNORECASE,
    ),
    # Pattern 2: "Am I being biased/influenced/blinded/clouded by..."
    re.compile(
        r"\b(am i|i'?m)\s+being\s+(biased|influenced|blinded|clouded|swayed|colored|skewed)\s+by",
        re.IGNORECASE,
    ),
    # Pattern 3: "Is my [relational thing] pulling/skewing/distorting/coloring my read"
    re.compile(
        r"\bis\s+my\s+(relationship|history|feeling|friendship|loyalty|gratitude|fear|love|trust|attachment|love|loyalty)\s+"
        r"(pulling|skewing|distorting|coloring|biasing|tainting|warping|contaminating|cloud(?:ing)?)",
        re.IGNORECASE,
    ),
    # Pattern 4: "I keep coming back to..." + emotional referent
    re.compile(
        r"\bi\s+keep\s+(coming|going)\s+back\s+to.{0,100}"
        r"\b(friendship|loyalty|gratitude|fear|guilt|obligation|trust|love|history)",
        re.IGNORECASE | re.DOTALL,
    ),
    # Pattern 5: explicit stress-test invitation
    re.compile(
        r"\b(stress[- ]test|check whether|check if)\s+my\s+"
        r"(emotional|relational|feeling|friendship|loyalty|gratitude|fear)\s+"
        r"(contamination|bias|leak|distort|influence|color)",
        re.IGNORECASE,
    ),
    # Bonus pattern 6: "long personal relationship" / "exactly why I needed to bring this" — Sprint 11 Yelena exemplar
    re.compile(
        r"\b(long\s+(personal|professional)\s+relationship.{0,80}exactly\s+why|"
        r"that'?s\s+exactly\s+why\s+i\s+(needed|wanted|had)\s+to\s+(bring|raise|talk))",
        re.IGNORECASE | re.DOTALL,
    ),
]

CONVICTION_VS_ARGUMENT_SURFACE = [
    # Canonical title (standard mode)
    re.compile(r"\bConviction[\s-]+vs[\s.-]+Argument\b", re.IGNORECASE),
    # Three-layer structure markers (relaxed mode — needs ALL three layer signals)
    # We treat presence of all three as a separate check below in _surface_matches
]

# Three-layer markers — used only in relaxed-scaffolding fallback
THREE_LAYER_MARKERS = [
    re.compile(r"\b(conduct|fact|data)[\s-]+read\b", re.IGNORECASE),
    re.compile(r"\b(sequencing|timing|order|sequence)\b", re.IGNORECASE),
    re.compile(r"\b(private\s+conviction|formal\s+argument|conviction\s+vs\.?\s+argument|conviction.+argument)\b", re.IGNORECASE),
]


@dataclass
class TriggerTool:
    tool_id: str  # canonical identifier (e.g. "conviction-vs-argument")
    canonical_title: str
    trigger_patterns: list  # list of compiled regex
    surface_patterns: list  # list of compiled regex (canonical title forms)
    three_layer_required: bool = False  # if true, all THREE_LAYER_MARKERS must match in relaxed mode
    three_layer_markers: list = field(default_factory=list)


TRIGGER_TOOLS = [
    TriggerTool(
        tool_id="conviction-vs-argument",
        canonical_title="Conviction vs Argument",
        trigger_patterns=CONVICTION_VS_ARGUMENT_TRIGGERS,
        surface_patterns=CONVICTION_VS_ARGUMENT_SURFACE,
        three_layer_required=True,
        three_layer_markers=THREE_LAYER_MARKERS,
    ),
]


# ---------------------------------------------------------------------------
# Case File parsing
# ---------------------------------------------------------------------------

USER_LINE_RE = re.compile(r"^User:\s*[\"“‘]?(.*)$")
AI_LINE_RE = re.compile(r"^AI\s*(?:\[[^\]]+\])?\s*:\s*[\"“‘]?(.*)$")


@dataclass
class Turn:
    user_text: str = ""
    user_line_no: int = 0
    ai_text: str = ""
    ai_line_no: int = 0


def parse_frontmatter(text: str):
    """Return (frontmatter_dict, body) or (None, text) if absent/invalid."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None, text[end + 5:]
    if not isinstance(fm, dict):
        return None, text[end + 5:]
    return fm, text[end + 5:]


def extract_session_turns(body: str):
    """Walk the body, find ## Session Log, extract Turn objects pairing User: → next AI:.

    Skips fenced code blocks and HTML comments. Multi-line User/AI utterances
    (continuation lines without a new speaker prefix) are concatenated until
    the next speaker line or blank line.
    """
    lines = body.split("\n")
    # Find Session Log section
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Session Log"):
            start = i + 1
            break
    if start is None:
        return None  # signals: no Session Log section

    turns = []
    current_turn = None  # building the current Turn (user pending AI pairing)
    in_code = False
    in_comment = False
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Stop at next top-level section
        if stripped.startswith("## ") and i > start:
            break
        # Toggle code fence
        if stripped.startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            i += 1
            continue
        # HTML comments
        if "<!--" in line:
            in_comment = True
        if in_comment:
            if "-->" in line:
                in_comment = False
            i += 1
            continue

        um = USER_LINE_RE.match(line)
        am = AI_LINE_RE.match(line)

        if um:
            # Close out a prior un-paired turn (User without AI response — partial turn)
            if current_turn is not None:
                turns.append(current_turn)
            user_text = um.group(1)
            # Accumulate continuation lines
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    break
                if USER_LINE_RE.match(nxt) or AI_LINE_RE.match(nxt):
                    break
                if nxt.strip().startswith("## "):
                    break
                user_text += "\n" + nxt
                j += 1
            current_turn = Turn(user_text=user_text.rstrip('"”’').strip(), user_line_no=i + 1)
            i = j
            continue

        if am:
            ai_text = am.group(1)
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    break
                if USER_LINE_RE.match(nxt) or AI_LINE_RE.match(nxt):
                    break
                if nxt.strip().startswith("## "):
                    break
                ai_text += "\n" + nxt
                j += 1
            if current_turn is not None and not current_turn.ai_text:
                current_turn.ai_text = ai_text.rstrip('"”’').strip()
                current_turn.ai_line_no = i + 1
                turns.append(current_turn)
                current_turn = None
            # else: AI line without preceding User — ignore (welcome-back / bootstrap)
            i = j
            continue

        i += 1

    if current_turn is not None:
        turns.append(current_turn)

    return turns


def extract_skipped_triggers(fm, body: str):
    """Find trigger_fired_tool_skipped entries (frontmatter list, body block, OR ad-hoc grep).

    Returns a set of (turn_number, trigger_id) tuples. The trigger_id matching is
    lenient — accepts either canonical tool_id or descriptive shorthand
    (e.g. 'friendship-contamination').
    """
    skipped = set()
    # Frontmatter
    fm_skipped = (fm or {}).get("trigger_fired_tool_skipped")
    if isinstance(fm_skipped, list):
        for entry in fm_skipped:
            if isinstance(entry, dict):
                turn = entry.get("turn")
                trigger = entry.get("trigger", "")
                if isinstance(turn, int):
                    skipped.add((turn, str(trigger).lower()))
    # Body — look for fenced YAML blocks containing trigger_fired_tool_skipped
    yaml_blocks = re.findall(r"```ya?ml\s*\n(.*?)\n```", body, re.DOTALL)
    for block in yaml_blocks:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        entries = data.get("trigger_fired_tool_skipped")
        if isinstance(entries, list):
            for entry in entries:
                if isinstance(entry, dict):
                    turn = entry.get("turn")
                    trigger = entry.get("trigger", "")
                    if isinstance(turn, int):
                        skipped.add((turn, str(trigger).lower()))
    return skipped


def extract_tool_surfaced_in_chat(fm, body: str):
    """Find tool_surfaced_in_chat annotations (frontmatter list + body YAML blocks).

    Sprint 15 Card 07 — closes the structural-vs-text-presence coverage gap.
    When a Case File's Session Log uses placeholder text (e.g.,
    `AI [Consultant]: [full verbatim response delivered in chat — see
    turn-N chat output]`) rather than verbatim AI text, the text-presence
    scan in `_surface_matches` cannot confirm tool surface. The annotation
    is an alternative verification path: the AI explicitly attests, by
    structured-data annotation, that the tool was named in the (out-of-band)
    chat output.

    Returns a set of (turn_number, tool_id) tuples. The tool_id matching is
    lenient — accepts canonical tool_id, canonical title (case-insensitive),
    or descriptive shorthand.

    Schema (frontmatter or fenced YAML body block):

        tool_surfaced_in_chat:
          - turn: 3
            tool: "conviction-vs-argument"   # canonical tool_id OR title
            evidence: "canonical phrase 'the Conviction-vs-Argument three-layer pass' used explicitly with all three layers applied"
    """
    surfaced = set()
    # Frontmatter
    fm_entries = (fm or {}).get("tool_surfaced_in_chat")
    if isinstance(fm_entries, list):
        for entry in fm_entries:
            if isinstance(entry, dict):
                turn = entry.get("turn")
                tool = entry.get("tool", "")
                if isinstance(turn, int):
                    surfaced.add((turn, str(tool).lower()))
    # Body — look for fenced YAML blocks containing tool_surfaced_in_chat
    yaml_blocks = re.findall(r"```ya?ml\s*\n(.*?)\n```", body, re.DOTALL)
    for block in yaml_blocks:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        entries = data.get("tool_surfaced_in_chat")
        if isinstance(entries, list):
            for entry in entries:
                if isinstance(entry, dict):
                    turn = entry.get("turn")
                    tool = entry.get("tool", "")
                    if isinstance(turn, int):
                        surfaced.add((turn, str(tool).lower()))
    return surfaced


def _annotation_matches(tool: TriggerTool, turn_no: int, surfaced) -> bool:
    """Return True iff a tool_surfaced_in_chat annotation matches this tool+turn.

    Match is lenient: accepts canonical tool_id, canonical title
    (case-insensitive), or substring of either.
    """
    if not surfaced:
        return False
    canonical_lower = tool.canonical_title.lower()
    for (t, tid) in surfaced:
        if t != turn_no:
            continue
        tid_lower = tid.lower()
        if tool.tool_id in tid_lower or tid_lower in tool.tool_id:
            return True
        if canonical_lower in tid_lower or tid_lower in canonical_lower:
            return True
    return False


def _surface_matches(tool: TriggerTool, ai_text: str) -> bool:
    """Return True iff the tool's canonical surface or three-layer markers are present."""
    for pat in tool.surface_patterns:
        if pat.search(ai_text):
            return True
    if tool.three_layer_required and tool.three_layer_markers:
        if all(pat.search(ai_text) for pat in tool.three_layer_markers):
            return True
    return False


# ---------------------------------------------------------------------------
# Main audit
# ---------------------------------------------------------------------------

def audit(path: Path) -> int:
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 3

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        return 3

    fm, body = parse_frontmatter(text)
    if fm is None:
        print(f"ERROR: frontmatter missing or invalid in {path.name}", file=sys.stderr)
        return 2

    turns = extract_session_turns(body)
    if turns is None:
        print(f"ERROR: no '## Session Log' section in {path.name}", file=sys.stderr)
        return 2

    skipped = extract_skipped_triggers(fm, body)
    surfaced_annotations = extract_tool_surfaced_in_chat(fm, body)

    violations = 0
    fires = 0
    # Number turns starting from 1
    for turn_no, turn in enumerate(turns, start=1):
        if not turn.user_text:
            continue
        for tool in TRIGGER_TOOLS:
            fired = False
            matched_pattern_idx = None
            for idx, pat in enumerate(tool.trigger_patterns):
                if pat.search(turn.user_text):
                    fired = True
                    matched_pattern_idx = idx + 1
                    break
            if not fired:
                continue
            fires += 1
            # Check tool surface in the AI response (text-presence scan)
            if turn.ai_text and _surface_matches(tool, turn.ai_text):
                print(
                    f"OK turn={turn_no} tool={tool.tool_id} pattern={matched_pattern_idx} "
                    f"(line {turn.user_line_no}): tool surfaced"
                )
                continue
            # Sprint 15 Card 07: structured annotation as alternative
            # verification path (when AI text is placeholder rather than
            # verbatim — Yelena Sprint 14 turn 3 pattern).
            if _annotation_matches(tool, turn_no, surfaced_annotations):
                print(
                    f"OK turn={turn_no} tool={tool.tool_id} pattern={matched_pattern_idx} "
                    f"(line {turn.user_line_no}): tool surfaced (via tool_surfaced_in_chat annotation)"
                )
                continue
            # Check justified skip
            justified = any(
                t == turn_no and (tool.tool_id in tid or "friendship" in tid or tool.canonical_title.lower() in tid)
                for t, tid in skipped
            )
            if justified:
                print(
                    f"OK turn={turn_no} tool={tool.tool_id} pattern={matched_pattern_idx} "
                    f"(line {turn.user_line_no}): documented skip"
                )
                continue
            # Sprint 17 Card 04 first-invocation rule (chapter 04
            # §4.3.4): before flagging as a miss, walk backward
            # through prior turns' AI text. If the tool's canonical
            # title was already mentioned in some prior AI chat line,
            # treat the current trigger fire as a sub-application of
            # an already-discharged invocation (first-invocation rule
            # has fired; subsequent applications do not require fresh
            # surfacing per chapter 04 §4.3.4). Logs the prior turn
            # for verifiability.
            first_invocation_turn = None
            canonical_lower = tool.canonical_title.lower()
            for prior_no in range(1, turn_no):
                prior_turn = turns[prior_no - 1]
                if prior_turn.ai_text and canonical_lower in prior_turn.ai_text.lower():
                    first_invocation_turn = prior_no
                    break
            if first_invocation_turn is not None:
                print(
                    f"OK turn={turn_no} tool={tool.tool_id} pattern={matched_pattern_idx} "
                    f"(line {turn.user_line_no}): sub-application — first-invocation "
                    f"discharged at turn {first_invocation_turn} (chapter 04 §4.3.4)"
                )
                continue
            # Violation
            print(
                f"FAIL turn={turn_no} tool={tool.tool_id} pattern={matched_pattern_idx} "
                f"(line {turn.user_line_no}): trigger fired but tool did NOT surface AND no "
                f"'trigger_fired_tool_skipped' entry recorded for this turn AND no prior "
                f"AI chat line names the tool by canonical title (first-invocation rule "
                f"per chapter 04 §4.3.4 not satisfied either)"
            )
            violations += 1

    if violations == 0:
        print(f"PASS: {path.name} ({fires} trigger(s) fired, all handled)")
        return 0
    print(f"FAILED: {path.name} ({violations} violation(s) of {fires} trigger(s))")
    return 1


# ---------------------------------------------------------------------------
# Sprint 17 Card 05: --auto-populate flag + coupling enforcement
# ---------------------------------------------------------------------------


def _extract_tools_applied_titles(body: str) -> list[str]:
    """Walk ## Tools Applied; return canonical titles (H3 entries).

    Skips template placeholder ('[Tool Name]') and ad-hoc-marked
    entries (entries whose H3 title is bracketed with [ad-hoc] suffix).
    """
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## Tools Applied"):
            start = i + 1
            break
    if start is None:
        return []
    titles: list[str] = []
    for i in range(start, len(lines)):
        line = lines[i]
        if line.startswith("## "):
            break  # next top-level section
        m = re.match(r"^###\s+(.+?)\s*$", line)
        if m:
            title = m.group(1).strip()
            if title.startswith("[") and title.endswith("]"):
                continue  # template placeholder
            if "[ad-hoc]" in title.lower():
                continue
            titles.append(title)
    return titles


def _extract_ai_chat_by_turn(body: str) -> list[tuple[int, str]]:
    """Return list of (turn_no, ai_text) for each '#### Turn N' block.

    Concatenates all AI [persona]: lines within the turn block.
    """
    lines = body.split("\n")
    turn_blocks: list[tuple[int, list[str]]] = []
    current_turn: int | None = None
    current_ai_lines: list[str] = []
    in_ai_line = False
    for line in lines:
        m = re.match(r"^####\s+Turn\s+(\d+)", line)
        if m:
            if current_turn is not None:
                turn_blocks.append((current_turn, current_ai_lines))
            current_turn = int(m.group(1))
            current_ai_lines = []
            in_ai_line = False
            continue
        if current_turn is None:
            continue
        if re.match(r"^AI\s*(?:\[[^\]]+\])?\s*:", line):
            in_ai_line = True
            current_ai_lines.append(line)
        elif re.match(r"^User\s*:", line):
            in_ai_line = False
        elif re.match(r"^####\s+", line):
            in_ai_line = False
        elif in_ai_line and line.strip():
            current_ai_lines.append(line)
    if current_turn is not None:
        turn_blocks.append((current_turn, current_ai_lines))
    return [(t, "\n".join(ls)) for t, ls in turn_blocks]


def auto_populate(path: Path) -> int:
    """Sprint 17 Card 05: derive tool_surfaced_in_chat from Tools Applied
    + AI chat lines. For each tool in Tools Applied whose canonical title
    appears in an AI chat line, append an entry to tool_surfaced_in_chat
    with the earliest matching turn + a verbatim excerpt as evidence.
    Existing entries are preserved; only missing tools are added.

    Writes the modified file in place. Exit 0 = entries added or no
    additions needed; exit 1 = no Tools Applied / no AI chat (cannot
    derive); exit 2 = file error.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        return 2

    fm, body = parse_frontmatter(text)
    if fm is None:
        print(f"ERROR: frontmatter missing or invalid in {path.name}", file=sys.stderr)
        return 2

    titles = _extract_tools_applied_titles(body)
    if not titles:
        print(f"OK: {path.name} — no ## Tools Applied entries to auto-populate from")
        return 0

    chat_by_turn = _extract_ai_chat_by_turn(body)
    if not chat_by_turn:
        print(f"OK: {path.name} — no '#### Turn N' AI chat lines to scan")
        return 0

    existing = fm.get("tool_surfaced_in_chat") or []
    existing_titles = {
        (e.get("tool") or "").lower().strip()
        for e in existing
        if isinstance(e, dict)
    }

    new_entries = []
    for title in titles:
        if title.lower().strip() in existing_titles:
            continue
        earliest_turn = None
        evidence = ""
        for turn_no, ai_text in sorted(chat_by_turn):
            if re.search(rf"\b{re.escape(title)}\b", ai_text, re.IGNORECASE):
                earliest_turn = turn_no
                m = re.search(
                    rf"([^.!?\n]*\b{re.escape(title)}\b[^.!?\n]*[.!?])",
                    ai_text,
                    re.IGNORECASE,
                )
                evidence = (m.group(1) if m else f"chat mention at turn {turn_no}").strip()
                if len(evidence) > 280:
                    evidence = evidence[:277].rstrip() + "..."
                break
        if earliest_turn is None:
            continue
        new_entries.append({
            "turn": earliest_turn,
            "tool": title,
            "evidence": evidence,
            "source": "auto-populated by trigger-phrase-audit.py --auto-populate (Sprint 17 Card 05)",
        })

    if not new_entries:
        print(
            f"OK: {path.name} — tool_surfaced_in_chat already complete "
            f"({len(existing)} existing entries; 0 new entries to derive)"
        )
        return 0

    # Rewrite the tool_surfaced_in_chat block in place.
    yaml_lines = ["tool_surfaced_in_chat:"]
    all_entries = list(existing) + new_entries
    for entry in all_entries:
        if not isinstance(entry, dict):
            continue
        yaml_lines.append(f"  - turn: {entry.get('turn', 0)}")
        tool_v = entry.get("tool") or ""
        yaml_lines.append(f"    tool: \"{tool_v}\"")
        ev = (entry.get("evidence") or "").replace("\\", "\\\\").replace('"', '\\"')
        yaml_lines.append(f"    evidence: \"{ev}\"")
        if entry.get("source"):
            src = entry["source"].replace('"', '\\"')
            yaml_lines.append(f"    source: \"{src}\"")
    new_block = "\n".join(yaml_lines) + "\n"

    lines = text.split("\n")
    start_idx = None
    end_idx = None
    in_block = False
    for i, line in enumerate(lines):
        if line.startswith("tool_surfaced_in_chat:"):
            start_idx = i
            in_block = True
            continue
        if in_block:
            if line.startswith("  ") or line.startswith("\t") or not line.strip():
                continue
            end_idx = i
            break
    if start_idx is None:
        print(
            f"ERROR: {path.name} — tool_surfaced_in_chat field not found in frontmatter; "
            "add it to _TEMPLATE.md and re-run",
            file=sys.stderr,
        )
        return 2
    if end_idx is None:
        end_idx = len(lines)

    new_text = "\n".join(lines[:start_idx]) + "\n" + new_block + "\n".join(lines[end_idx:])
    path.write_text(new_text, encoding="utf-8")
    print(
        f"OK: {path.name} — auto-populated {len(new_entries)} new tool_surfaced_in_chat "
        f"entry/entries ({len(existing)} pre-existing preserved)."
    )
    for e in new_entries:
        print(f"  + turn {e['turn']}: {e['tool']}")
    return 0


def coupling_check(path: Path) -> int:
    """Sprint 17 Card 05: coupling enforcement. For each ### [Tool] in
    ## Tools Applied (non-ad-hoc), assert that the canonical title
    appears in tool_surfaced_in_chat OR has been logged with [ad-hoc]
    marker. Otherwise exit 1.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        return 2

    fm, body = parse_frontmatter(text)
    if fm is None:
        print(f"ERROR: frontmatter missing or invalid in {path.name}", file=sys.stderr)
        return 2

    titles = _extract_tools_applied_titles(body)
    if not titles:
        print(f"OK [coupling]: {path.name} — no Tools Applied entries to verify")
        return 0

    surfaced = fm.get("tool_surfaced_in_chat") or []
    surfaced_titles = {
        (e.get("tool") or "").lower().strip()
        for e in surfaced
        if isinstance(e, dict)
    }
    violations = []
    for title in titles:
        if title.lower().strip() not in surfaced_titles:
            violations.append(title)

    if violations:
        for t in violations:
            print(
                f"FAIL [coupling]: '### {t}' in Tools Applied has no matching "
                f"tool_surfaced_in_chat entry (Sprint 17 Card 05). "
                f"Recovery: run 'trigger-phrase-audit.py --auto-populate' OR "
                f"add [ad-hoc] marker if the tool was applied without canonical "
                f"library mapping."
            )
        print(
            f"FAILED [coupling]: {path.name} ({len(violations)} of "
            f"{len(titles)} Tools Applied entries lack tool_surfaced_in_chat entries)"
        )
        return 1

    print(
        f"OK [coupling]: {path.name} ({len(titles)} Tools Applied entries all "
        f"have tool_surfaced_in_chat coverage)"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit a Case File for mandatory-trigger compliance."
    )
    parser.add_argument("path", type=Path, help="Path to a Case File .md file")
    parser.add_argument(
        "--auto-populate",
        action="store_true",
        help="Sprint 17 Card 05: derive tool_surfaced_in_chat from Tools "
             "Applied + AI chat (writes file in place).",
    )
    parser.add_argument(
        "--coupling-check",
        action="store_true",
        help="Sprint 17 Card 05: enforce coupling — every Tools Applied "
             "entry must have a tool_surfaced_in_chat entry (or [ad-hoc] "
             "marker). Exit 1 on violations.",
    )
    args = parser.parse_args()

    path = args.path
    if not path.is_absolute():
        try:
            root = find_root()
            candidate = (root / path).resolve()
            if candidate.is_file():
                path = candidate
        except RuntimeError:
            pass

    if args.auto_populate:
        return auto_populate(path)
    if args.coupling_check:
        return coupling_check(path)

    return audit(path)


if __name__ == "__main__":
    sys.exit(main())
