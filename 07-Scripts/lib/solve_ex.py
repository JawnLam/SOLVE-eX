"""Shared helpers for SOLVE eX v2.0 utility scripts.

Provides root-discovery (walk up from script path looking for
AI-BOOTSTRAP.md), tool-entry parsing, and schema loading. Pure stdlib +
pyyaml.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "ERROR: pyyaml not installed. Install with: pip install pyyaml\n"
    )
    sys.exit(3)


def find_root(start: Path | None = None) -> Path:
    """Walk up from `start` until we find a directory containing AI-BOOTSTRAP.md.

    If start is None, use the script's parent directory.
    """
    if start is None:
        # __file__ is solve_ex.py; parent is lib/; parent.parent is 07-Scripts/
        start = Path(__file__).resolve().parent
    current = start
    for _ in range(20):
        if (current / "AI-BOOTSTRAP.md").is_file():
            return current
        if current.parent == current:
            break
        current = current.parent
    raise RuntimeError(
        f"Could not find SOLVE eX root (no AI-BOOTSTRAP.md found walking up from {start})"
    )


def tool_entries_dir(root: Path | None = None) -> Path:
    if root is None:
        root = find_root()
    return root / "01-Tools" / "Tool Entries"


def case_files_dir(root: Path | None = None) -> Path:
    if root is None:
        root = find_root()
    return root / "06-Case-Files"


def schema_path(root: Path | None = None) -> Path:
    if root is None:
        root = find_root()
    return root / "08-Schema" / "Master_Schema.yaml"


def load_schema(root: Path | None = None) -> dict[str, Any]:
    with open(schema_path(root)) as f:
        return yaml.safe_load(f)


def parse_frontmatter(path: Path) -> dict[str, Any]:
    """Parse YAML frontmatter from a markdown file.

    Returns the parsed frontmatter dict, or empty dict if no frontmatter.
    Raises yaml.YAMLError on malformed YAML.
    """
    with open(path) as f:
        content = f.read()
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}
    front = content[4:end]
    data = yaml.safe_load(front)
    return data if isinstance(data, dict) else {}


def iter_tool_entries(root: Path | None = None):
    """Yield (path, frontmatter) for every tool entry. Skips on parse errors."""
    for path in sorted(tool_entries_dir(root).glob("*.md")):
        try:
            fm = parse_frontmatter(path)
            yield path, fm
        except Exception as e:
            sys.stderr.write(f"WARN: failed to parse {path.name}: {e}\n")
            continue
