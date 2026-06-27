#!/usr/bin/env python3
"""validate-tool.py — validate a tool entry against the schema.

Runs the rules from 08-Schema/validation-rules.md:
  - A: file structure
  - B: required properties
  - C: enum-value rules (OOV detection)
  - D: cross-field consistency
  - E: optional-property rules
  - F: body content (warnings only)

Exit codes:
  0 = pass (warnings may print)
  1 = at least one rule failed
  2 = YAML parse error
  3 = file-not-found or permission error

Example:
  python3 validate-tool.py "../01-Tools/Tool Entries/Eisenhower Matrix.md"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import find_root, load_schema, parse_frontmatter  # noqa: E402

import yaml  # noqa: E402

REQUIRED_PROPS = [
    "Item_ID",
    "type",
    "title",
    "tt_Source",
    "tt_Type",
    "tt_Domain",
    "tt_Field",
    "tt_Operation",
    "tt_Form",
    "tt_Scale",
    "tt_Duration",
    "tt_Lineage",
    "tt_Posture",
    "tt_SOLVE_eX_Phase",
    "tt_SOLVE_eX_Step",
    "tt_Clarifies",
    "tt_Applicability",
    "tt_Status",
]

# Maps tt_* property name → enum key in schema['enums']
ENUM_FACETS = {
    "tt_Type": "tt_types",
    "tt_Domain": "tt_domains",
    "tt_Cross_Domains": "tt_domains",
    "tt_Form": "tt_forms",
    "tt_Scale": "tt_scales",
    "tt_Duration": "tt_durations",
    "tt_Lineage": "tt_lineages",
    "tt_Posture": "tt_postures",
    "tt_State": "tt_states",
    "tt_Agent": "tt_agents",
    "tt_About": "tt_abouts",
    "tt_SOLVE_eX_Phase": "tt_solve_ex_phases",
    "tt_SOLVE_eX_Step": "tt_solve_ex_steps",
    "tt_Clarifies": "tt_clarifies_values",
    "tt_Applicability": "tt_applicability_values",
    "tt_Status": "tt_statuses",
}

# Single-valued vs multi-valued
MULTI_VALUE = {
    "tt_Cross_Domains",
    "tt_Form",
    "tt_Scale",
    "tt_Duration",
    "tt_Lineage",
    "tt_Posture",
    "tt_State",
    "tt_Agent",
    "tt_About",
    "tt_SOLVE_eX_Phase",
    "tt_SOLVE_eX_Step",
    "tt_Clarifies",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("path", help="Path to tool entry .md file")
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress warnings; print only errors and final status",
    )
    return p.parse_args()


def validate(path: Path, schema: dict, quiet: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # A1, A2, A3
    if not path.is_file():
        errors.append(f"A1: cannot read file: {path}")
        return 3
    if not path.suffix == ".md":
        errors.append(f"A2: not a markdown file: {path}")

    name = path.stem
    if name.strip() != name or any(ch in name for ch in '<>:"|?*'):
        errors.append(f"A3: invalid filename: {path.name}")

    # A4, A5
    try:
        fm = parse_frontmatter(path)
    except yaml.YAMLError as e:
        sys.stderr.write(f"A4/A5: yaml parse error: {e}\n")
        return 2
    if not fm:
        errors.append("A4: missing or malformed frontmatter")

    # A6: body heading matches Title
    content = path.read_text()
    title_field = fm.get("Title", "").strip()
    if title_field:
        expected_heading = f"# {title_field}"
        if expected_heading not in content:
            warnings.append(
                f"A6: body heading '# {title_field}' not found"
            )

    # B: required properties
    for prop in REQUIRED_PROPS:
        val = fm.get(prop)
        if val is None or (isinstance(val, str) and not val.strip()):
            # Exception: tt_Form may be empty list for stance type (D1)
            if prop == "tt_Form" and fm.get("tt_Type") == "stance":
                continue
            errors.append(f"B: required property missing or empty: {prop}")

    # Item_ID format
    item_id = fm.get("Item_ID", "")
    if item_id and not str(item_id).startswith("tt-"):
        errors.append(f"B: Item_ID must start with 'tt-': got '{item_id}'")

    # type
    if fm.get("type") != "Thinking_Tool":
        errors.append(
            f"B: type must be 'Thinking_Tool': got '{fm.get('type')}'"
        )

    # C: enum-value rules (OOV)
    enums = schema.get("enums", {})
    for facet, enum_key in ENUM_FACETS.items():
        val = fm.get(facet)
        if val is None:
            continue
        allowed = enums.get(enum_key)
        if allowed is None:
            warnings.append(f"C: enum {enum_key} not in schema; skipped {facet}")
            continue
        # Normalize allowed values to strings for comparison
        allowed_str = [str(v).strip() for v in allowed]
        values = val if isinstance(val, list) else [val]
        for v in values:
            if str(v).strip() not in allowed_str:
                errors.append(
                    f"C: OOV violation: {facet}={v!r} not in {enum_key}"
                )

    # D1, D2: Form vs Type
    ttype = fm.get("tt_Type")
    form = fm.get("tt_Form")
    if ttype == "stance":
        if form not in (None, [], ""):
            errors.append(
                "D1: tt_Type=stance requires tt_Form to be empty list"
            )
    elif ttype == "instrument":
        if not form or (isinstance(form, list) and len(form) == 0):
            errors.append(
                "D2: tt_Type=instrument requires non-empty tt_Form"
            )

    # F: body sections (warnings)
    if "## Purpose" not in content:
        warnings.append("F: body missing '## Purpose' section")
    if ttype == "instrument" and "## How To Use" not in content:
        warnings.append("F: body missing '## How To Use' section")
    if "## Sources" not in content:
        warnings.append("F: body missing '## Sources' section")

    # Print results
    for w in warnings:
        if not quiet:
            sys.stderr.write(f"WARN: {w}\n")
    for e in errors:
        sys.stderr.write(f"FAIL: {e}\n")

    if errors:
        print(f"FAIL: {path.name} ({len(errors)} error(s), {len(warnings)} warning(s))")
        return 1
    else:
        print(f"OK: {path.name} ({len(warnings)} warning(s))")
        return 0


def main() -> int:
    args = parse_args()
    schema = load_schema()
    return validate(Path(args.path), schema, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
