#!/usr/bin/env python3
"""portability-check.py — scan the corpus for hard-coded paths.

The SOLVE eX corpus uses `{ROOT}` as a placeholder for the deployment root.
Any hard-coded absolute paths (e.g. `/Users/...`, `/Volumes/...`, drive letters)
in the *content* files break portability across deployments.

This script greps the corpus and reports any matches. By default it scans:
  - 00-Instructions/
  - 01-Tools/Tool Entries/
  - 03-Question-Banks/
  - 04-Application-Patterns/
  - 05-Personas/
  - 09-Sample-Sessions/
  - 10-Reference/

It excludes:
  - 06-Case-Files/ (real user paths may appear in archived case files)
  - 07-Scripts/   (Python scripts may need absolute paths via find_root())
  - 08-Schema/    (schema files; same exclusion logic as scripts)
  - 99-Archive/   (archived material)
  - hidden directories (.git, .obsidian, etc.)

Exit codes:
  0 = clean (no hard-coded paths in scanned content)
  1 = hard-coded paths found
  3 = corpus not locatable

Example:
  python3 portability-check.py
  python3 portability-check.py --verbose
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import find_root  # noqa: E402


SCAN_DIRS = [
    "00-Instructions",
    "01-Tools/Tool Entries",
    "03-Question-Banks",
    "04-Application-Patterns",
    "05-Personas",
    "09-Sample-Sessions",
    "10-Reference",
]


HARDCODED_PATH_PATTERNS = [
    # macOS user-home and external volumes
    r"/Users/[A-Za-z0-9_\-]+",
    r"/Volumes/[A-Za-z0-9_\- ]+",
    # Linux user-home
    r"/home/[A-Za-z0-9_\-]+",
    # Windows drive letters
    r"[A-Z]:\\\\",
    r"[A-Z]:/",
    # Dropbox conventions that suggest a specific user
    r"Library/CloudStorage/Dropbox",
    r"1nBox - DropBox",
]


def compile_patterns() -> list[re.Pattern]:
    return [re.compile(p) for p in HARDCODED_PATH_PATTERNS]


def scan_file(path: Path, patterns: list[re.Pattern]) -> list[tuple[int, str, str]]:
    """Return list of (line_no, pattern_str, matched_text) tuples."""
    hits = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return hits
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pat in patterns:
            m = pat.search(line)
            if m:
                hits.append((lineno, pat.pattern, m.group(0)))
    return hits


def scan_dir(root: Path, subdir: str, patterns: list[re.Pattern], verbose: bool) -> int:
    target = root / subdir
    if not target.is_dir():
        if verbose:
            print(f"SKIP: {subdir} (not present)")
        return 0
    total_hits = 0
    for md in sorted(target.rglob("*.md")):
        rel = md.relative_to(root)
        hits = scan_file(md, patterns)
        for lineno, pat, matched in hits:
            print(f"{rel}:{lineno}: matched /{pat}/  →  {matched}")
            total_hits += 1
    return total_hits


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan the SOLVE eX corpus for hard-coded paths that break portability."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-directory scan progress",
    )
    args = parser.parse_args()

    try:
        root = find_root()
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 3

    patterns = compile_patterns()
    total_hits = 0
    for subdir in SCAN_DIRS:
        if args.verbose:
            print(f"Scanning: {subdir}")
        total_hits += scan_dir(root, subdir, patterns, args.verbose)

    if total_hits == 0:
        print(f"OK: corpus is portable ({len(SCAN_DIRS)} directories scanned, 0 hard-coded paths)")
        return 0
    else:
        print(f"FAIL: {total_hits} hard-coded path(s) found across the corpus")
        return 1


if __name__ == "__main__":
    sys.exit(main())
