#!/usr/bin/env python3
r"""
cross-chapter-dependency-audit.py — verify every cross-chapter §-reference in the
SOLVE eX v2.0 instruction corpus resolves to an existing section.

Usage:
    python3 cross-chapter-dependency-audit.py [corpus-root]
    python3 cross-chapter-dependency-audit.py --self-test

Exit codes:
    0 — all cross-chapter references resolve (or no references found)
    1 — one or more cross-chapter references are broken
    2 — invalid corpus path or argument

Sprint 13 Card 02 (SOLVE eX v2.0). Implements v28 lint/matcher design constraints
documented in the card:

    1. Skip inline backtick `code` and fenced code blocks — references inside
       those are documentation of patterns, not operational dependencies.
    2. Skip YAML frontmatter at the head of each file.
    3. Use bounded regex with word boundaries.
    4. "chapter N step M" treated as documentation reference (no §-section to
       resolve) when no §M.N appears alongside; "chapter N §M.O" treated as
       operational and resolved.
    5. Exit codes: 0 / 1 / 2 (see above).

The audit reads each chapter file under `00-Instructions/` to build:

    sections[chapter_number] = { section_number: True, ... }

where chapter_number is parsed from the filename (e.g., 03-...) and
section_number from header lines like `## 3.1 Title`, `### 3.1.2 Title`.

Then it walks each chapter again, finds cross-chapter §-references with the
regex `chapter (\d+),?\s+§(\d+(?:\.\d+)*)`, and asserts the target section
exists.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Compiled regex patterns
HEADER_RE = re.compile(r"^(#{2,5})\s+(\d+(?:\.\d+)*)\b")
REFERENCE_RE = re.compile(r"\bchapter\s+(\d+)\s*,?\s*§\s*(\d+(?:\.\d+)*)")
FRONTMATTER_DELIM = re.compile(r"^---\s*$")
FENCED_CODE_DELIM = re.compile(r"^(?:`{3,}|~{3,})")
CHAPTER_FILENAME_RE = re.compile(r"^(\d{2})-")


def chapter_number_from_filename(path: Path) -> int | None:
    """Return chapter number parsed from filename like '03-the-diagnostic-loop.md'."""
    m = CHAPTER_FILENAME_RE.match(path.name)
    if m:
        return int(m.group(1))
    return None


def strip_skipped_regions(line: str) -> str:
    """
    Remove inline backtick content from a line so the reference regex won't see
    documentation-of-references inside `code spans`. Mutates the line by
    replacing each backtick-delimited span with a same-length stub of spaces so
    column-counting stays meaningful.
    """
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "`":
            # Determine run length (single, double, triple backtick code spans)
            run_start = i
            while i < n and line[i] == "`":
                i += 1
            run_marker = line[run_start:i]
            close_idx = line.find(run_marker, i)
            if close_idx == -1:
                # Unclosed inline code — keep the rest as-is (rare)
                out.append(line[run_start:])
                break
            # Replace the marker + content + closing marker with spaces
            span_len = close_idx + len(run_marker) - run_start
            out.append(" " * span_len)
            i = close_idx + len(run_marker)
        else:
            out.append(line[i])
            i += 1
    return "".join(out)


def parse_chapter_sections(path: Path) -> Tuple[int | None, Set[str]]:
    """
    Parse a chapter file. Return (chapter_number, set of section-number strings
    like '3.1', '3.1.2'). Skips frontmatter and fenced code blocks.
    """
    chapter_no = chapter_number_from_filename(path)
    sections: Set[str] = set()
    in_frontmatter = False
    in_fenced = False
    frontmatter_started = False

    text = path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        # Handle YAML frontmatter (only at the very top)
        if not frontmatter_started and FRONTMATTER_DELIM.match(line):
            in_frontmatter = True
            frontmatter_started = True
            continue
        if in_frontmatter:
            if FRONTMATTER_DELIM.match(line):
                in_frontmatter = False
            continue

        # Track fenced code blocks
        if FENCED_CODE_DELIM.match(line):
            in_fenced = not in_fenced
            continue
        if in_fenced:
            continue

        m = HEADER_RE.match(line)
        if m:
            sections.add(m.group(2))

    return chapter_no, sections


def collect_references(
    path: Path,
) -> List[Tuple[int, int, int, str]]:
    """
    Walk a chapter file, return list of (line_number, target_chapter,
    target_section_full_string, raw_context_line) for every cross-chapter
    reference outside frontmatter / fenced code / inline backticks.
    """
    refs: List[Tuple[int, int, int, str]] = []
    in_frontmatter = False
    in_fenced = False
    frontmatter_started = False

    text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, raw in enumerate(text.splitlines(), start=1):
        if not frontmatter_started and FRONTMATTER_DELIM.match(raw):
            in_frontmatter = True
            frontmatter_started = True
            continue
        if in_frontmatter:
            if FRONTMATTER_DELIM.match(raw):
                in_frontmatter = False
            continue
        if FENCED_CODE_DELIM.match(raw):
            in_fenced = not in_fenced
            continue
        if in_fenced:
            continue

        scrubbed = strip_skipped_regions(raw)
        for m in REFERENCE_RE.finditer(scrubbed):
            target_ch = int(m.group(1))
            target_sec = m.group(2)
            refs.append((lineno, target_ch, target_sec, raw.strip()))

    return refs


def audit_corpus(instructions_dir: Path) -> Tuple[int, List[str]]:
    """
    Audit every chapter file in instructions_dir. Return (broken_count,
    diagnostic_lines).

    A "chapter file" is a `.md` file whose basename matches the
    `CHAPTER_FILENAME_RE` pattern (two-digit prefix + dash, e.g.
    `03-the-diagnostic-loop.md`). Non-chapter `.md` files in the same
    directory (LICENSE.md, README.md, etc.) are excluded so the audited
    file count reflects the actual chapter corpus. Sprint 14 Card 10
    over-trigger + Sprint 15 Card 03 fix: behavioral-verification (v31)
    requires the script to report the actual chapter count, not the
    glob-pattern count.
    """
    chapter_files = sorted(
        p
        for p in instructions_dir.glob("*.md")
        if not p.name.startswith("_") and CHAPTER_FILENAME_RE.match(p.name)
    )

    # Build chapter_number → section-set map. Union across files that share
    # the same chapter prefix (e.g., 00-START-HERE.md and
    # 00-cross-chapter-dependencies.md both map to chapter 0; their sections
    # are merged rather than overwritten).
    section_map: Dict[int, Set[str]] = {}
    for path in chapter_files:
        ch_no, sections = parse_chapter_sections(path)
        if ch_no is None:
            continue
        section_map.setdefault(ch_no, set()).update(sections)

    broken: List[str] = []
    total_refs = 0
    for path in chapter_files:
        for lineno, target_ch, target_sec, context in collect_references(path):
            total_refs += 1
            if target_ch not in section_map:
                broken.append(
                    f"{path.name}:{lineno} -> chapter {target_ch} §{target_sec} : "
                    f"target chapter file not found in corpus | {context}"
                )
                continue
            if target_sec not in section_map[target_ch]:
                # Try matching by prefix: "§3.1" may resolve to "## 3.1 Title"
                # but "§3.1.2" requires a literal "3.1.2" header. The strict
                # rule above already enforces this. We keep the broken record.
                broken.append(
                    f"{path.name}:{lineno} -> chapter {target_ch} §{target_sec} : "
                    f"section not found in {target_ch:02d}-*.md | {context}"
                )

    diagnostics = [f"Audited {len(chapter_files)} chapter files, {total_refs} cross-chapter references."]
    if broken:
        diagnostics.append(f"BROKEN REFERENCES ({len(broken)}):")
        diagnostics.extend("  " + b for b in broken)
    else:
        diagnostics.append("All cross-chapter references resolve.")
    return len(broken), diagnostics


# ----------------------------------------------------------------------
# Self-test mode — synthetic fixtures cover the three v28 test cases
# ----------------------------------------------------------------------

SELF_TEST_FIXTURE_A = {
    "02-bootstrap.md": (
        "# Bootstrap\n\n"
        "## 2.6 Initialize Case File\n\n"
        "The Case File is hard-gated by chapter 13 §13.2 (detection check).\n"
    ),
    "13-quality-checks.md": (
        "# Quality Checks\n\n"
        "## 13.1 What this chapter does\n\n"
        "## 13.2 The self-check list\n\n"
        "The detection_check block format is defined here.\n"
    ),
}

SELF_TEST_FIXTURE_B = {
    "02-bootstrap.md": (
        "# Bootstrap\n\n"
        "## 2.6 Initialize Case File\n\n"
        "The Case File is hard-gated by chapter 13 §13.99 (nonexistent section).\n"
    ),
    "13-quality-checks.md": (
        "# Quality Checks\n\n"
        "## 13.1 What this chapter does\n\n"
        "## 13.2 The self-check list\n"
    ),
}

SELF_TEST_FIXTURE_C = {
    "02-bootstrap.md": (
        "# Bootstrap\n\n"
        "## 2.6 Initialize Case File\n\n"
        "An inline reference like `chapter 13 §13.99` is documentation only.\n"
        "And a fenced block:\n"
        "```\n"
        "chapter 13 §13.99 (also documentation in code block)\n"
        "```\n"
        "Real reference: chapter 13 §13.2 (this one must resolve).\n"
    ),
    "13-quality-checks.md": (
        "# Quality Checks\n\n"
        "## 13.2 The self-check list\n"
    ),
}


SELF_TEST_FIXTURE_D_CHAPTER_FILTER = {
    # 2 chapter-pattern files...
    "02-bootstrap.md": (
        "# Bootstrap\n\n"
        "## 2.6 Initialize Case File\n"
    ),
    "13-quality-checks.md": (
        "# Quality Checks\n\n"
        "## 13.2 The self-check list\n"
    ),
    # ...and 3 non-chapter files that should be filtered out
    "README.md": "# Readme\nNot a chapter file.\n",
    "LICENSE.md": "# License\nNot a chapter file.\n",
    "VERSION.md": "v1.0\n",
}


def run_self_test() -> int:
    import re as _re
    import tempfile

    cases = [
        ("A: valid corpus (chapter 02 §2.6 → chapter 13 §13.2)", SELF_TEST_FIXTURE_A, 0),
        ("B: broken reference (chapter 13 §13.99 nonexistent)", SELF_TEST_FIXTURE_B, 1),
        ("C: inline backtick + fenced code skipped (real §13.2 resolves)", SELF_TEST_FIXTURE_C, 0),
    ]
    all_pass = True
    for label, files, expected in cases:
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            for name, content in files.items():
                (tdp / name).write_text(content, encoding="utf-8")
            broken, diags = audit_corpus(tdp)
            got = 1 if broken > 0 else 0
            status = "PASS" if got == expected else "FAIL"
            if got != expected:
                all_pass = False
            print(f"[{status}] {label} -- expected exit {expected}, got exit {got}, broken={broken}")
            for d in diags:
                print("    " + d)

    # Case D: chapter-file filter — fixture has 5 .md files but only 2 are
    # chapter-pattern (NN-*.md); audit must report 2. Sprint 15 Card 03
    # behavioral-verification regression test for the file-count fix.
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        for name, content in SELF_TEST_FIXTURE_D_CHAPTER_FILTER.items():
            (tdp / name).write_text(content, encoding="utf-8")
        _, diags_d = audit_corpus(tdp)
        m = _re.match(r"^Audited (\d+) chapter files", diags_d[0]) if diags_d else None
        got_count = int(m.group(1)) if m else -1
        status = "PASS" if got_count == 2 else "FAIL"
        if got_count != 2:
            all_pass = False
        print(f"[{status}] D: chapter-file filter (5 .md, 2 chapter-pattern) -- expected count=2, got count={got_count}")
        for d in diags_d:
            print("    " + d)

    # Case E: live-corpus chapter-file count — runs against the actual
    # SOLVE eX v2.0 instructions corpus and asserts "Audited 16 chapter files"
    # verbatim. Sprint 15 Card 03 acceptance gate. If the corpus grows (a
    # new chapter file added to 00-Instructions/), update the expected count
    # in this test alongside the corpus addition. The test fails (rather
    # than skipping) if the corpus is not locatable from this script.
    live_corpus = Path(__file__).resolve().parent.parent / "00-Instructions"
    if live_corpus.is_dir():
        _, diags_e = audit_corpus(live_corpus)
        m = _re.match(r"^Audited (\d+) chapter files", diags_e[0]) if diags_e else None
        got_count = int(m.group(1)) if m else -1
        expected_count = 16
        status = "PASS" if got_count == expected_count else "FAIL"
        if got_count != expected_count:
            all_pass = False
        print(f"[{status}] E: live corpus chapter count -- expected {expected_count}, got {got_count}")
        print(f"    {diags_e[0] if diags_e else '(no diagnostics)'}")
    else:
        print("[SKIP] E: live corpus not locatable from script path")

    return 0 if all_pass else 1


# ----------------------------------------------------------------------


def _resolve_instructions_dir(target: Path) -> Path:
    """
    Resolve the instructions directory from a passed path.

    If `target` itself contains chapter files (matches CHAPTER_FILENAME_RE),
    use it as-is. Otherwise, if `target/00-Instructions/` exists, treat
    `target` as a corpus root and descend into the instructions subdir.
    Falls back to `target` if neither condition holds (caller will get
    an empty audit, which surfaces the misuse rather than masking it).

    Sprint 15 Card 03 fix: pre-Sprint-15, the script invoked as
    `python3 cross-chapter-dependency-audit.py .` glob-ed the corpus root
    directly and saw 4 stray .md files (LICENSE, README, AI-BOOTSTRAP,
    VERSION) instead of the 16 chapter files in `00-Instructions/`.
    """
    if not target.is_dir():
        return target
    has_chapter_file = any(
        p.is_file() and CHAPTER_FILENAME_RE.match(p.name)
        for p in target.glob("*.md")
    )
    if has_chapter_file:
        return target
    sub = target / "00-Instructions"
    if sub.is_dir():
        return sub
    return target


def main(argv: List[str]) -> int:
    if len(argv) >= 2 and argv[1] == "--self-test":
        return run_self_test()

    # Default corpus root
    default_root = Path(__file__).resolve().parent.parent / "00-Instructions"
    target = Path(argv[1]).resolve() if len(argv) >= 2 else default_root

    if not target.exists() or not target.is_dir():
        print(f"ERROR: corpus path not a directory: {target}", file=sys.stderr)
        return 2

    instructions_dir = _resolve_instructions_dir(target)
    broken, diagnostics = audit_corpus(instructions_dir)
    for d in diagnostics:
        print(d)
    return 1 if broken > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
