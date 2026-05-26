#!/usr/bin/env python3
"""case-file-placeholder-lint.py — scan a Case File for residual
template placeholder comments that should have been replaced.

Usage:
    python3 07-Scripts/case-file-placeholder-lint.py <path-to-case-file>

Exit codes:
    0  no residual placeholders (Case File is fully populated)
    1  one or more residual placeholders detected
    2  invalid input (file not found, unreadable, etc.)

Detection rule:
    Matches HTML comments containing the literal token "placeholder",
    case-insensitive. The template introduced by Sprint 11 Card 06 uses
    `<!-- ... placeholder ... -->` for every section that should be
    populated during a session. A Case File closing with any of those
    comments still in place is a sign that the AI either skipped the
    section or the session is incomplete.

This complements chapter 13 §13.3's per-turn quality checks: it runs
once, at session close (chapter 06 §6.13).
"""
import argparse
import re
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(
    r"<!--(?:(?!-->).)*?placeholder(?:(?!-->).)*?-->",
    re.IGNORECASE | re.DOTALL,
)


def scan_file(path: Path) -> list[tuple[int, str]]:
    """Return list of (line_no, placeholder_text) for each residual placeholder."""
    findings: list[tuple[int, str]] = []
    with path.open("r", encoding="utf-8") as fh:
        content = fh.read()

    for match in PLACEHOLDER_RE.finditer(content):
        # Compute the line number from match.start()
        line_no = content[: match.start()].count("\n") + 1
        text = match.group(0).strip()
        if len(text) > 120:
            text = text[:117] + "..."
        findings.append((line_no, text))

    return findings


def format_report(path: Path, findings: list[tuple[int, str]]) -> str:
    lines = [f"case-file-placeholder-lint.py — {path}"]
    lines.append("")
    if not findings:
        lines.append("OK — no residual placeholders detected")
        lines.append(f"Total: 0")
        return "\n".join(lines)

    lines.append(f"FOUND {len(findings)} residual placeholder(s):")
    lines.append("")
    for line_no, text in findings:
        lines.append(f"  line {line_no:4d}  {text}")
    lines.append("")
    lines.append("Recovery: each placeholder represents a section the session")
    lines.append("did not populate. Either populate the section with content")
    lines.append("or remove the placeholder line if the section is not relevant")
    lines.append("to this case.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan a Case File for residual template placeholder comments."
    )
    parser.add_argument("path", help="Path to a Case File markdown file")
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress report; exit code only",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"error: {path} not found", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"error: {path} is not a file", file=sys.stderr)
        return 2

    findings = scan_file(path)
    if not args.quiet:
        print(format_report(path, findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
