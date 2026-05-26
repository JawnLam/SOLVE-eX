#!/usr/bin/env python3
"""new-case-file.py — initialize a new Case File from the template.

Creates a new file in {ROOT}/06-Case-Files/_ACTIVE/ from _TEMPLATE.md
with timestamp and user-supplied slug, pre-filling created/last_updated
fields.

Example:
  python3 new-case-file.py --title "Job decision" --user "user"
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import case_files_dir, find_root  # noqa: E402


def slugify(text: str) -> str:
    """Convert title to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "untitled"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--title", required=True, help="Short title for the case file"
    )
    p.add_argument(
        "--user", default="user", help="User handle (default: 'user')"
    )
    p.add_argument(
        "--slug",
        help="Override the slug; default derives from --title",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    root = find_root()
    cf_dir = case_files_dir(root)
    template = cf_dir / "_TEMPLATE.md"
    active = cf_dir / "_ACTIVE"

    if not template.is_file():
        sys.stderr.write(f"ERROR: template not found at {template}\n")
        return 1

    now = dt.datetime.now()
    stamp = now.strftime("%Y-%m-%d-%H%M")
    iso = now.strftime("%Y-%m-%dT%H:%M:%S")
    slug = args.slug or slugify(args.title)
    cf_id = f"{stamp}-{slug}"
    filename = f"{cf_id}.md"
    target = active / filename

    if target.exists():
        sys.stderr.write(f"ERROR: file already exists: {target}\n")
        return 1

    content = template.read_text()
    # Replace the placeholders in frontmatter
    replacements = [
        ("case_file_id: YYYY-MM-DD-HHMM-user-slug", f"case_file_id: {cf_id}"),
        (
            'case_file_title: "Short title of the question being worked"',
            f'case_file_title: "{args.title}"',
        ),
        ('user_handle: "user"', f'user_handle: "{args.user}"'),
        ("created: YYYY-MM-DDTHH:MM:SS", f"created: {iso}"),
        ("last_updated: YYYY-MM-DDTHH:MM:SS", f"last_updated: {iso}"),
        # The body's heading placeholder
        ("# Case File: [title]", f"# Case File: {args.title}"),
        # Session log session-1 placeholder
        ("### Session 1 — YYYY-MM-DD", f"### Session 1 — {now.strftime('%Y-%m-%d')}"),
        # last_persona_switch
        ("last_persona_switch: YYYY-MM-DDTHH:MM:SS", f"last_persona_switch: {iso}"),
    ]
    for old, new in replacements:
        content = content.replace(old, new)

    active.mkdir(parents=True, exist_ok=True)
    target.write_text(content)
    print(f"Created: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
