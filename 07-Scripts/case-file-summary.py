#!/usr/bin/env python3
"""case-file-summary.py — produce a 1-paragraph summary of a Case File.

Reads a Case File's frontmatter and synthesizes a single paragraph
suitable for session-2-open or external review. The summary names the
case title, current status, the active frame's clarity states and
phase-step, and the last persona switch.

Exit codes:
  0 = summary produced
  1 = malformed Case File (missing required keys)
  2 = YAML parse error
  3 = file not found or permission error

Example:
  python3 case-file-summary.py "../06-Case-Files/_ARCHIVED/example-job-decision.md"
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


def find_active_frame(goal_stack: list) -> dict | None:
    if not isinstance(goal_stack, list):
        return None
    for frame in goal_stack:
        if isinstance(frame, dict) and frame.get("active"):
            return frame
    # Fallback: first frame if no active flagged
    for frame in goal_stack:
        if isinstance(frame, dict):
            return frame
    return None


def synthesize(fm: dict) -> str:
    title = fm.get("case_file_title", "(untitled case)")
    status = fm.get("status", "unknown")
    session_count = fm.get("session_count", "?")
    total_turns = fm.get("total_turns", "?")
    persona = fm.get("active_persona", "unknown")
    primary_emotional = fm.get("primary_emotional_state", "")
    stakes_flags = fm.get("stakes_flags") or []

    active_frame = find_active_frame(fm.get("goal_stack", []))
    if active_frame is None:
        return f"Case File '{title}'. Status: {status}. No frames in goal_stack."

    fid = active_frame.get("frame_id", "?")
    phase_step = active_frame.get("phase_step", "?")
    origin_clarity = active_frame.get("origin_clarity", "?")
    dest_clarity = active_frame.get("destination_clarity", "?")
    origin = (active_frame.get("origin") or "").strip()
    destination = (active_frame.get("destination") or "").strip()

    parts = []
    parts.append(f"Case File: {title}.")
    parts.append(f"Status: {status} ({session_count} session(s), {total_turns} total turn(s)).")
    parts.append(f"Active frame: {fid}, currently at phase-step {phase_step}.")
    parts.append(f"Origin clarity: {origin_clarity}; Destination clarity: {dest_clarity}.")
    if origin:
        parts.append(f"Origin: \"{origin[:140]}\".")
    if destination:
        parts.append(f"Destination: \"{destination[:140]}\".")
    parts.append(f"Active persona: {persona}.")
    if primary_emotional:
        parts.append(f"Emotional baseline: {primary_emotional}.")
    if stakes_flags:
        parts.append(f"Stakes flags: {', '.join(stakes_flags)}.")

    return " ".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Produce a 1-paragraph summary of a Case File."
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

    required = ["case_file_title", "status", "goal_stack"]
    missing = [k for k in required if k not in fm]
    if missing:
        print(f"ERROR: Case File missing required keys: {missing}", file=sys.stderr)
        return 1

    summary = synthesize(fm)
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
