#!/usr/bin/env python3
"""show-stack.py — render the frame stack of a Case File as an ASCII tree.

Reads a Case File's goal_stack frontmatter and prints a human-readable
tree of frames and sub-frames, showing each frame's clarity states and
current phase-step. Useful for orientation at session resumption.

Exit codes:
  0 = displayed successfully
  1 = no goal_stack found or empty
  2 = YAML parse error
  3 = file not found or permission error

Example:
  python3 show-stack.py "../06-Case-Files/_ARCHIVED/example-job-decision.md"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import find_root  # noqa: E402

import yaml  # noqa: E402


def parse_frontmatter_dict(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("no frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter")
    return yaml.safe_load(text[4:end]) or {}


def render_frame(frame: dict, indent: int = 0) -> list[str]:
    prefix = "    " * indent
    lines = []
    fid = frame.get("frame_id", "?")
    active = "active" if frame.get("active") else "closed"
    phase_step = frame.get("phase_step", "?")
    origin_clarity = frame.get("origin_clarity", "?")
    dest_clarity = frame.get("destination_clarity", "?")
    origin = frame.get("origin", "")
    destination = frame.get("destination", "")

    lines.append(f"{prefix}┌─ Frame {fid} [{active}]  step={phase_step}")
    lines.append(f"{prefix}│  Origin       (clarity: {origin_clarity})")
    if origin:
        lines.append(f"{prefix}│    \"{origin[:80]}\"")
    lines.append(f"{prefix}│  Destination  (clarity: {dest_clarity})")
    if destination:
        lines.append(f"{prefix}│    \"{destination[:80]}\"")
    parent = frame.get("parent_frame")
    if parent is not None:
        lines.append(f"{prefix}│  Parent: frame {parent}")
    lines.append(f"{prefix}└─")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render the frame stack of a Case File as an ASCII tree."
    )
    parser.add_argument("path", type=Path, help="Path to a Case File .md")
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

    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 3

    try:
        fm = parse_frontmatter_dict(path)
    except yaml.YAMLError as e:
        print(f"ERROR: YAML parse failure: {e}", file=sys.stderr)
        return 2
    except (OSError, UnicodeDecodeError, ValueError) as e:
        print(f"ERROR: could not parse {path}: {e}", file=sys.stderr)
        return 3

    goal_stack = fm.get("goal_stack")
    if not goal_stack:
        print(f"WARN: no goal_stack in {path.name}", file=sys.stderr)
        return 1

    case_id = fm.get("case_file_id", "?")
    case_title = fm.get("case_file_title", "?")
    status = fm.get("status", "?")
    persona = fm.get("active_persona", "?")

    print(f"Case File: {case_id}")
    print(f"Title:     {case_title}")
    print(f"Status:    {status}    Active persona: {persona}")
    print()
    print("Frame stack:")
    print()

    for frame in goal_stack:
        if isinstance(frame, dict):
            indent = 1 if frame.get("parent_frame") is not None else 0
            for line in render_frame(frame, indent=indent):
                print(line)

    return 0


if __name__ == "__main__":
    sys.exit(main())
