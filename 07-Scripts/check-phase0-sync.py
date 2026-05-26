#!/usr/bin/env python3
r"""
check-phase0-sync.py — verify the root `AI-BOOTSTRAP.md` Phase 0 readiness section
remains in sync with its chapter-00 mirror `00-Instructions/00-start-here.md`.

Usage:
    python3 check-phase0-sync.py [corpus-root]
    python3 check-phase0-sync.py --self-test

Exit codes:
    0 — Phase 0 sections are in sync
    1 — Phase 0 sections diverge (substantive content differs)
    2 — invalid corpus path or one of the source files is missing

Sprint 18 Card 01 (SOLVE eX v2.0). Closes the Class C Phase 0 leak that fired
3/3 in the Sprint 17 panel because the Sprint 17 Card 01 amendment landed in the
mirror but not the root.

The script extracts the `## Phase 0: Pre-Flight` section from each file (from
the heading to the next top-level `## ` heading or `---` separator), normalizes
whitespace (line-wrap differences are not substantive), and diffs the result.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

READINESS_HEADING = re.compile(r"^###\s+4\.\s+Mandatory\s+readiness\s+statement", re.IGNORECASE)
NEXT_SUBHEADING = re.compile(r"^###\s+\d+\.")
NEXT_TOP_HEADING = re.compile(r"^##\s+(?!#)")
HORIZONTAL_RULE = re.compile(r"^---\s*$")


def extract_phase0(path: Path) -> str:
    """Extract the Phase 0 readiness statement subsection (§4) — the load-bearing
    content for Class C surface compliance. Earlier subsections (§1 chapter reads,
    §2 environment checks, §3 session-mode declaration) have legitimate
    perspective-dependent wording differences between root and mirror; the
    readiness format and the Class C tolerances callout are what must stay
    identical across the two files."""
    lines = path.read_text(encoding="utf-8").splitlines()
    in_section = False
    captured: list[str] = []
    for line in lines:
        if not in_section:
            if READINESS_HEADING.match(line):
                in_section = True
                captured.append(line)
            continue
        if NEXT_SUBHEADING.match(line) or NEXT_TOP_HEADING.match(line) or HORIZONTAL_RULE.match(line):
            break
        captured.append(line)
    return "\n".join(captured)


def normalize(text: str) -> list[str]:
    """Collapse line-wrap differences while preserving paragraph and code-block
    structure. Inside fenced code blocks (``` ... ```), lines are kept verbatim
    so the readiness-statement format is checked exactly. Outside code blocks,
    consecutive non-blank lines are joined into a single paragraph and internal
    whitespace is collapsed."""
    paragraphs: list[str] = []
    buffer: list[str] = []
    in_fence = False

    def flush() -> None:
        if buffer:
            joined = " ".join(s.strip() for s in buffer)
            joined = re.sub(r"\s+", " ", joined).strip()
            if joined:
                paragraphs.append(joined)
            buffer.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush()
            paragraphs.append(line)
            in_fence = not in_fence
            continue
        if in_fence:
            paragraphs.append(line)
            continue
        if not line.strip():
            flush()
            continue
        buffer.append(line)
    flush()
    return paragraphs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "corpus_root",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
        help="SOLVE eX v2.0 corpus root (defaults to script's parent directory)",
    )
    parser.add_argument("--self-test", action="store_true", help="run built-in self test")
    args = parser.parse_args()

    if args.self_test:
        sample = (
            "## Phase 0: Pre-Flight\n\n"
            "### 1. Earlier\nIntro.\n\n"
            "### 4. Mandatory readiness statement (your first response)\n\n"
            "Output exactly this shape:\n\n"
            "```\nfield: value\n```\n\n"
            "### 5. Next\nUnrelated.\n"
        )
        section = extract_phase0_from_text(sample)
        assert "field: value" in section, section
        assert "Unrelated" not in section, section
        norm = normalize(section)
        assert any("Output exactly this shape:" in p for p in norm), norm
        print("self-test OK")
        return 0

    root = Path(args.corpus_root).resolve()
    root_file = root / "AI-BOOTSTRAP.md"
    mirror_file = root / "00-Instructions" / "00-start-here.md"

    if not root_file.is_file():
        print(f"ERROR: missing {root_file}", file=sys.stderr)
        return 2
    if not mirror_file.is_file():
        print(f"ERROR: missing {mirror_file}", file=sys.stderr)
        return 2

    root_section = extract_phase0(root_file)
    mirror_section = extract_phase0(mirror_file)

    if not root_section:
        print(f"ERROR: no Phase 0 section in {root_file}", file=sys.stderr)
        return 2
    if not mirror_section:
        print(f"ERROR: no Phase 0 section in {mirror_file}", file=sys.stderr)
        return 2

    root_norm = normalize(root_section)
    mirror_norm = normalize(mirror_section)

    if root_norm == mirror_norm:
        print(f"OK: Phase 0 sections in sync ({len(root_norm)} normalized blocks)")
        return 0

    diff = list(
        difflib.unified_diff(
            mirror_norm,
            root_norm,
            fromfile=str(mirror_file.relative_to(root)),
            tofile=str(root_file.relative_to(root)),
            lineterm="",
        )
    )
    print("DIVERGENCE: Phase 0 sections differ:", file=sys.stderr)
    for d in diff:
        print(d, file=sys.stderr)
    return 1


def extract_phase0_from_text(text: str) -> str:
    """Self-test helper — extract the §4 readiness subsection from a string."""
    lines = text.splitlines()
    in_section = False
    captured: list[str] = []
    for line in lines:
        if not in_section:
            if READINESS_HEADING.match(line):
                in_section = True
                captured.append(line)
            continue
        if NEXT_SUBHEADING.match(line) or NEXT_TOP_HEADING.match(line) or HORIZONTAL_RULE.match(line):
            break
        captured.append(line)
    return "\n".join(captured)


if __name__ == "__main__":
    sys.exit(main())
