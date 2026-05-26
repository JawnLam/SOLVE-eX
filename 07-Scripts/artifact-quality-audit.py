#!/usr/bin/env python3
r"""artifact-quality-audit.py — heuristic pre-shipping audit for structured artifacts.

Runs the six checks documented in chapter 13 §13.7 (Artifact-creation quality
gate) against a markdown artifact. The script is HEURISTIC — it surfaces
candidates for AI review rather than producing absolute verdicts. The AI is
expected to read each flagged candidate, judge it against artifact context,
and either fix or justify before surfacing the artifact to the user.

Checks implemented (heuristic-flagging):
  1. Numeric consistency — flag $-denominated figures that lack a derivation
     sentence within the preceding paragraph (arithmetic operators, "of",
     "from", another quantified claim).
  2. Internal consistency — flag artifacts whose framing principles include
     "does not draw conclusions" / "preliminary" / "draft" and that later
     contain conclusion-language like "the right call is" / "Path N is".
  3. Domain-expertise hallucination — flag imperative tactical-content in
     expert-domain contexts (legal/medical/regulatory). Looks for verbs
     ("mirror," "file," "disclose," "delete," "prescribe," "settle,"
     "litigate," "report to," "admit") without an "outside counsel" /
     "uncertainty band" / "consult [domain] specialist" qualifier.
  6. Voice neutrality — delegates to voice-neutrality-lint.py --mode standard
     (artifacts are always mode-standard regardless of originating session).

Checks 4 (citation accuracy) and 5 (length proportionality) are AI-review-only;
this script does not attempt them.

Exit codes:
  0 = no heuristic candidates flagged (artifact clean)
  1 = one or more heuristic candidates flagged for AI review
  2 = invalid artifact path or unreadable file
  3 = subprocess failure (voice-neutrality-lint.py not runnable)

Usage:
  python3 artifact-quality-audit.py <artifact.md>
  python3 artifact-quality-audit.py --self-test
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Tuple

# DOCX namespace constants — stable across Office Open XML versions.
_DOCX_W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _extract_docx_text(path: Path) -> str:
    """Extract paragraph text from a .docx file via stdlib zipfile + ElementTree.

    DOCX is a ZIP archive; `word/document.xml` contains the body, with text in
    `<w:t>` elements nested under `<w:p>` paragraph containers. This walks the
    XML, emits one line per `<w:p>`, joins `<w:t>` contents within each
    paragraph. python-docx would handle this more thoroughly (tables, headers,
    styled runs) but isn't installed on the Mac; stdlib is sufficient for
    voice-neutrality and content audits.

    Returns the extracted text. Raises a clear error if the file isn't a
    valid DOCX (zipfile open failure or missing document.xml).

    Sprint 14 Card 10 Fix 3: previously artifact-quality-audit.py read DOCX
    bytes directly via path.read_text(), producing garbage content + false-
    positive voice-neutrality flags. This helper makes DOCX targets first-
    class.
    """
    try:
        with zipfile.ZipFile(path) as zf:
            with zf.open("word/document.xml") as xml_f:
                tree = ET.parse(xml_f)
    except (zipfile.BadZipFile, KeyError) as e:
        raise ValueError(f"not a valid DOCX archive: {e}") from e
    root = tree.getroot()
    paragraphs: List[str] = []
    for p in root.iter(f"{_DOCX_W_NS}p"):
        runs = [t.text or "" for t in p.iter(f"{_DOCX_W_NS}t")]
        line = "".join(runs)
        paragraphs.append(line)
    return "\n".join(paragraphs)

DOLLAR_RE = re.compile(r"\$[\d,]+(?:\.\d+)?[MBK]?\b", re.IGNORECASE)
DERIVATION_HINT_RE = re.compile(
    r"(?:\d+\s*[%×x*]|of\s+\$|from\s+\$|=\s*\$|times\s+\$|×\s+\$|\b(?:sum|total|product|quotient|equals|equal to|approximately|approx\.?|roughly|about|comprises|consist|breakdown)\b)",
    re.IGNORECASE,
)

# Sprint 15 Card 05 semantic-derivation sub-check (3rd-recurrence $48M class).
# Detect sentences of the shape "$X ... NN% ... of/×/x $Y" — a dollar figure
# derived (or appearing-to-be-derived) by applying a percentage to another
# dollar figure. The existing numeric_consistency_check PASSES these because
# the derivation lexicon ("of $", "%") is present, but the SEMANTIC question
# ("is the % a MULTIPLIER on the headline, or a MAGNITUDE DESCRIPTOR of a
# pattern within affected units?") goes unasked. Sprint 11 / 12 / 14 Yelena
# runs each shipped this class.
# Form A (Sprint 15 ships): "$48M (12% of $400M ARR base)" — $X first.
# Form B (Sprint 16+ carry-forward): "12% × $400M = $48M" — % first.
SEMANTIC_DERIVATION_RE = re.compile(
    r"\$[\d.,]+[KMBT]?\b[^.\n]{0,80}?"
    # NOTE: no \b after `%` — `%` is non-word and the typical follow-on is
    # whitespace (also non-word), so a word boundary there would never match.
    r"\b\d+(?:\.\d+)?%[^.\n]{0,40}?"
    r"(?:of|×|x|times|\*)\s*"
    r"\$[\d.,]+[KMBT]?\b",
    re.IGNORECASE,
)

CONCLUSION_AVOIDANCE_RE = re.compile(
    r"(?:does\s+not\s+draw\s+conclusions|conclusion-avoidance|preliminary|working\s+draft|draft\s+only|not\s+a\s+recommendation|no\s+recommendation\s+is\s+made)",
    re.IGNORECASE,
)
CONCLUSION_LANGUAGE_RE = re.compile(
    r"(?:\b(?:the right call|Path\s*\d|Option\s*[A-D]\s+is\s+(?:the|right|best|correct)|you should|we should|the answer is|the recommendation is)\b)",
    re.IGNORECASE,
)

# Heuristic: imperative tactical verbs commonly appearing in expert-domain prose
TACTICAL_VERBS_RE = re.compile(
    r"\b(?:mirror|file|disclose|delete|prescribe|settle|litigate|report\s+to|admit|deny|prosecute|sue|enjoin|garnish|levy|seize|forfeit|withhold|preempt|terminate|expel|fire|hire|promote|demote|invest|divest|merge|acquire|liquidate)\b",
    re.IGNORECASE,
)
DOMAIN_QUALIFIER_RE = re.compile(
    r"(?:outside\s+counsel|uncertainty\s+band|consult(?:\s+a)?\s+(?:specialist|attorney|lawyer|physician|doctor|accountant|advisor|professional|expert)|advice\s+of\s+counsel|under\s+the\s+supervision)",
    re.IGNORECASE,
)
EXPERT_DOMAIN_CONTEXT_RE = re.compile(
    r"\b(?:legal|regulatory|compliance|crime[- ]fraud|attorney|counsel|medical|clinical|physician|prescription|diagnose|securities|tax|estate|fiduciary|insurance|patent|trademark)\b",
    re.IGNORECASE,
)


def split_into_sentences(text: str) -> List[Tuple[int, str]]:
    """Split text into (line_no, sentence) pairs. Lightweight — not linguistic."""
    sentences: List[Tuple[int, str]] = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        # Skip headers, fenced-code openers, list markers (preserve for context)
        for s in re.split(r"(?<=[.!?])\s+", line):
            sentences.append((lineno, s))
    return sentences


def numeric_consistency_check(text: str) -> List[str]:
    """Flag $-denominated figures without a derivation hint in same paragraph."""
    flags: List[str] = []
    # Paragraph = sequence of non-blank lines
    paragraphs: List[Tuple[int, str]] = []
    cur_lineno = 0
    cur_lines: List[str] = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        if raw.strip():
            if not cur_lines:
                cur_lineno = lineno
            cur_lines.append(raw)
        else:
            if cur_lines:
                paragraphs.append((cur_lineno, "\n".join(cur_lines)))
                cur_lines = []
    if cur_lines:
        paragraphs.append((cur_lineno, "\n".join(cur_lines)))

    for start_lineno, para in paragraphs:
        # Skip fenced code blocks
        if para.startswith("```"):
            continue
        dollars = DOLLAR_RE.findall(para)
        if not dollars:
            continue
        if DERIVATION_HINT_RE.search(para):
            continue
        flags.append(
            f"[check 1: numeric-consistency] line {start_lineno}: paragraph "
            f"contains $-figure(s) {dollars[:3]} with no derivation hint "
            f"(arithmetic operator, 'of $', 'from $', '=$'). AI review: confirm "
            f"derivation is documented elsewhere or add it inline."
        )
    return flags


def semantic_derivation_check(text: str) -> List[str]:
    """Flag $-derived-from-%-of-$ patterns for multiplier-vs-magnitude review.

    Sprint 15 Card 05. Three sprints, three recurrences (Sprint 11, 12, 14)
    of the same artifact-failure shape: a percentage applied as a multiplier
    on a headline when it was actually a magnitude descriptor of a pattern
    within affected units. The existing numeric_consistency_check passes the
    arithmetic; this check raises the semantic question.

    Each match emits a "manual review" warning citing the offending
    derivation chain. The check does not have a verdict — it surfaces a
    candidate for AI semantic review per the chapter 13 §13.7 check 1
    semantic-derivation sub-check.
    """
    flags: List[str] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in SEMANTIC_DERIVATION_RE.finditer(line):
            chain = m.group(0)
            flags.append(
                f"[check 1: semantic-derivation] line {lineno}: "
                f"derivation chain '{chain.strip()}' applies a percentage "
                f"to a $-figure. AI manual review (chapter 13 §13.7 sub-check): "
                f"is the % a MULTIPLIER on the headline, or a MAGNITUDE "
                f"DESCRIPTOR of a pattern within affected units? Cite the "
                f"source-of-derivation step explicitly. Sprint 11/12/14 "
                f"Yelena $48M-class recurrence."
            )
    return flags


def internal_consistency_check(text: str) -> List[str]:
    """Flag artifacts that frame as preliminary then state conclusions."""
    flags: List[str] = []
    avoidance_hits = [(m.start(), m.group(0)) for m in CONCLUSION_AVOIDANCE_RE.finditer(text)]
    conclusion_hits = [(m.start(), m.group(0)) for m in CONCLUSION_LANGUAGE_RE.finditer(text)]
    if avoidance_hits and conclusion_hits:
        # Heuristic: at least one avoidance phrase BEFORE at least one conclusion phrase
        earliest_avoidance = avoidance_hits[0][0]
        later_conclusions = [c for c in conclusion_hits if c[0] > earliest_avoidance]
        if later_conclusions:
            ln = text.count("\n", 0, later_conclusions[0][0]) + 1
            flags.append(
                f"[check 2: internal-consistency] line {ln} (approx): conclusion-language "
                f"'{later_conclusions[0][1]}' appears in an artifact that earlier framed "
                f"itself with conclusion-avoidance language '{avoidance_hits[0][1]}'. "
                f"AI review: reconcile framing principles with downstream conclusions, "
                f"or remove the avoidance framing if conclusions are warranted."
            )
    return flags


def domain_expertise_check(text: str) -> List[str]:
    """Flag tactical-verb imperatives in expert-domain prose without a qualifier."""
    flags: List[str] = []
    # Heuristic: process the text in 200-character sliding windows. A tactical
    # verb within an expert-domain window without a qualifier is a candidate.
    for verb_match in TACTICAL_VERBS_RE.finditer(text):
        win_start = max(0, verb_match.start() - 200)
        win_end = min(len(text), verb_match.end() + 200)
        window = text[win_start:win_end]
        if not EXPERT_DOMAIN_CONTEXT_RE.search(window):
            continue
        if DOMAIN_QUALIFIER_RE.search(window):
            continue
        ln = text.count("\n", 0, verb_match.start()) + 1
        flags.append(
            f"[check 3: domain-expertise] line {ln} (approx): tactical verb "
            f"'{verb_match.group(0)}' appears in expert-domain context "
            f"without 'outside counsel' / 'uncertainty band' / 'consult specialist' "
            f"qualifier in surrounding ~200 chars. AI review: confirm the three-step "
            f"domain-expertise guard (flag domain / state uncertainty / default to "
            f"process-shape) is satisfied here, or add a qualifier."
        )
    return flags


def voice_neutrality_check(path: Path) -> List[str]:
    """Delegate to voice-neutrality-lint.py --mode standard."""
    flags: List[str] = []
    lint_path = Path(__file__).resolve().parent / "voice-neutrality-lint.py"
    if not lint_path.exists():
        flags.append(
            "[check 6: voice-neutrality] WARN: voice-neutrality-lint.py not found "
            f"at {lint_path}; skipping voice check. AI review: confirm artifact "
            "prose passes voice-neutrality manually."
        )
        return flags
    try:
        result = subprocess.run(
            ["python3", str(lint_path), str(path), "--mode", "standard", "--quiet"],
            capture_output=True, text=True, timeout=30,
        )
    except subprocess.SubprocessError as e:
        flags.append(f"[check 6: voice-neutrality] subprocess failed: {e}")
        return flags
    if result.returncode != 0:
        flags.append(
            f"[check 6: voice-neutrality] voice-neutrality-lint.py exited "
            f"{result.returncode}. Re-run without --quiet to see flagged lines: "
            f"python3 voice-neutrality-lint.py {path} --mode standard"
        )
    return flags


def audit_artifact(path: Path) -> Tuple[int, List[str]]:
    flags: List[str] = []
    # DOCX targets (Sprint 14 Card 10 Fix 3): extract text, then audit the
    # extracted text as if it were markdown. The voice-neutrality subprocess
    # gets a temp .md file containing the extracted prose; the in-process
    # checks (numeric / internal / domain) operate on the extracted text
    # directly. Prior behavior was path.read_text() on the DOCX bytes —
    # produced garbage content + false-positive voice-neutrality flags.
    if path.suffix.lower() == ".docx":
        try:
            text = _extract_docx_text(path)
        except ValueError as e:
            flags.append(
                f"[artifact-quality-audit] DOCX extraction failed: {e}; "
                f"skipping all six checks. AI review: confirm artifact "
                f"opens cleanly in Word / Pages before shipping."
            )
            return 2, flags
        flags.extend(numeric_consistency_check(text))
        flags.extend(semantic_derivation_check(text))
        flags.extend(internal_consistency_check(text))
        flags.extend(domain_expertise_check(text))
        # Voice neutrality: write extracted text to a temp .md and run the
        # lint against that. Use NamedTemporaryFile with delete=False so the
        # subprocess can re-open it; clean up explicitly afterward.
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write(text)
            tmp_path = Path(tmp.name)
        try:
            flags.extend(voice_neutrality_check(tmp_path))
        finally:
            try:
                tmp_path.unlink()
            except OSError:
                pass
        return (1 if flags else 0), flags

    # Markdown / text targets — original flow
    text = path.read_text(encoding="utf-8", errors="replace")
    flags.extend(numeric_consistency_check(text))
    flags.extend(semantic_derivation_check(text))
    flags.extend(internal_consistency_check(text))
    flags.extend(domain_expertise_check(text))
    flags.extend(voice_neutrality_check(path))
    return (1 if flags else 0), flags


# ----------------------------------------------------------------------
# Self-test
# ----------------------------------------------------------------------

SELF_TEST_FIXTURES = {
    "a_numeric_error.md": (
        "# Working Draft\n\n"
        "## Section 1\n\n"
        "The exposure is $48M of alleged liability based on the case findings.\n"
    ),  # should flag check 1
    "b_numeric_derived.md": (
        "# Working Draft\n\n"
        "## Section 1\n\n"
        "12% of $400M ARR equals $48M ARR-overstatement quantum.\n"
    ),  # should NOT flag check 1 (and NOT flag semantic-derivation —
        # % appears BEFORE the first $, so Form A doesn't match)
    "c_internal_inconsistency.md": (
        "# Briefing\n\n"
        "## 3.3 Scope\n\n"
        "This report does not draw conclusions.\n\n"
        "## 7 Conclusion\n\n"
        "Path 3 is the right call.\n"
    ),  # should flag check 2
    "d_domain_expertise.md": (
        "# Plan\n\n"
        "## Legal action\n\n"
        "Mirror the documents to a personal device immediately.\n"
    ),  # should flag check 3
    "e_semantic_derivation_48m.md": (
        "# Briefing\n\n"
        "## Exposure summary\n\n"
        "ARR impact: $48M (12% of $400M ARR base)\n"
    ),  # should flag check 1 semantic-derivation sub-check (Sprint 15 Card 05;
        # $48M-class 3rd recurrence canonical fixture).
}


def run_self_test() -> int:
    import tempfile
    expected = {
        "a_numeric_error.md": True,    # at least one flag
        "b_numeric_derived.md": False,  # no flags from checks 1-3 (check 6 may run via subprocess)
        "c_internal_inconsistency.md": True,
        "d_domain_expertise.md": True,
        "e_semantic_derivation_48m.md": True,  # semantic-derivation sub-check
    }
    all_pass = True
    for fixture, content in SELF_TEST_FIXTURES.items():
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(content)
            path = Path(f.name)
        try:
            # Skip voice-neutrality subprocess in self-test (would require working lint)
            text = path.read_text()
            flags: List[str] = []
            flags.extend(numeric_consistency_check(text))
            flags.extend(semantic_derivation_check(text))
            flags.extend(internal_consistency_check(text))
            flags.extend(domain_expertise_check(text))
            has_flag = bool(flags)
            ok = has_flag == expected[fixture]
            status = "PASS" if ok else "FAIL"
            if not ok:
                all_pass = False
            print(f"[{status}] {fixture} -- expected_flag={expected[fixture]} got_flag={has_flag} count={len(flags)}")
            for fl in flags[:3]:
                print(f"    {fl[:140]}")
        finally:
            path.unlink(missing_ok=True)
    return 0 if all_pass else 1


def main(argv: List[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        return run_self_test()
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    path = Path(argv[1]).resolve()
    if not path.is_file():
        print(f"ERROR: not a file: {path}", file=sys.stderr)
        return 2
    code, flags = audit_artifact(path)
    if flags:
        print(f"FLAGS: {len(flags)} heuristic candidate(s) for AI review:")
        for fl in flags:
            print(f"  {fl}")
    else:
        print(f"CLEAN: {path.name} — no heuristic candidates flagged")
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
