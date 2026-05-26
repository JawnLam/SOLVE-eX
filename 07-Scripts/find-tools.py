#!/usr/bin/env python3
"""find-tools.py — query the SOLVE eX tool library by facet.

Examples:
  python3 find-tools.py --phase 2 --clarifies Destination
  python3 find-tools.py --step 5.3 --applicability runtime_applicable
  python3 find-tools.py --domain "Inner / psychological work" --form "Sequenced workflow"
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from solve_ex import iter_tool_entries, find_root  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Query the SOLVE eX tool library by facet."
    )
    p.add_argument("--phase", help="tt_SOLVE_eX_Phase value (1-6 or 'any')")
    p.add_argument("--step", help="tt_SOLVE_eX_Step value (e.g., 1.1, 5.3, any)")
    p.add_argument(
        "--clarifies",
        choices=["Origin", "Destination", "Path", "Action", "None"],
        help="tt_Clarifies value",
    )
    p.add_argument(
        "--applicability",
        choices=[
            "runtime_applicable",
            "describable_only",
            "requires_tradition_transmission",
        ],
        help="tt_Applicability value",
    )
    p.add_argument("--domain", help="tt_Domain value")
    p.add_argument("--field", help="tt_Field value")
    p.add_argument("--operation", help="tt_Operation value")
    p.add_argument("--form", help="tt_Form value (e.g., Matrix, Mental model)")
    p.add_argument(
        "--type",
        dest="ttype",
        choices=["instrument", "stance"],
        help="tt_Type value",
    )
    p.add_argument(
        "--tier",
        choices=["A", "B", "C", "D"],
        help="tt_Quality_Tier value (filter to a single tier)",
    )
    p.add_argument(
        "--no-tier-sort",
        action="store_true",
        help="Disable default tier-aware ranking (A > B > C > D)",
    )
    p.add_argument(
        "--limit", type=int, default=50, help="Max results (default 50)"
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="Print frontmatter excerpts, not just titles",
    )
    p.add_argument(
        "--name",
        help="Case-insensitive substring match against tool filename stem "
        "(Sprint 18 Card 05). Implies --verbose. Use to look up a specific tool "
        "by name and surface its tt_Pairs_Well_With umbrella relationships.",
    )
    return p.parse_args()


def value_matches(facet_value, filter_value) -> bool:
    """Return True if filter_value is present in facet_value.

    facet_value may be a scalar, a list, or None.
    Numeric tt_SOLVE_eX_Phase values can compare against str filters.
    """
    if facet_value is None:
        return False
    if isinstance(facet_value, list):
        # Compare each item as string
        return any(str(v).strip() == str(filter_value).strip() for v in facet_value)
    return str(facet_value).strip() == str(filter_value).strip()


def main() -> int:
    args = parse_args()
    filters = {
        "tt_SOLVE_eX_Phase": args.phase,
        "tt_SOLVE_eX_Step": args.step,
        "tt_Clarifies": args.clarifies,
        "tt_Applicability": args.applicability,
        "tt_Domain": args.domain,
        "tt_Field": args.field,
        "tt_Operation": args.operation,
        "tt_Form": args.form,
        "tt_Type": args.ttype,
        "tt_Quality_Tier": args.tier,
    }
    active_filters = {k: v for k, v in filters.items() if v is not None}
    if not active_filters and not args.name:
        sys.stderr.write(
            "ERROR: provide at least one --filter or --name (see --help)\n"
        )
        return 2

    # Sprint 18 Card 05: --name mode implies verbose output (umbrella hint
    # is the load-bearing reason to query by name).
    if args.name:
        args.verbose = True

    root = find_root()
    matches: list[tuple[str, dict]] = []
    name_query = (args.name or "").strip().lower()
    for path, fm in iter_tool_entries(root):
        if name_query and name_query not in path.stem.lower():
            continue
        ok = True
        for facet, want in active_filters.items():
            if not value_matches(fm.get(facet), want):
                ok = False
                break
        if ok:
            matches.append((path.stem, fm))

    if not matches:
        print("(no tools match the filters)")
        return 0

    # Tier-aware sort (default): A > B > C > D, then alphabetical by title.
    # Untiered entries sort after D.
    if not args.no_tier_sort:
        tier_order = {"A": 0, "B": 1, "C": 2, "D": 3}
        matches.sort(
            key=lambda item: (
                tier_order.get(item[1].get("tt_Quality_Tier"), 4),
                item[0],
            )
        )

    for title, fm in matches[: args.limit]:
        if args.verbose:
            quick = fm.get("Quick_Notes") or fm.get("tt_Source") or ""
            print(f"{title}")
            print(f"  Domain: {fm.get('tt_Domain', '?')}")
            print(f"  Form:   {fm.get('tt_Form', '?')}")
            print(f"  Phase:  {fm.get('tt_SOLVE_eX_Phase', '?')}")
            print(f"  Step:   {fm.get('tt_SOLVE_eX_Step', '?')}")
            print(f"  Clarifies: {fm.get('tt_Clarifies', '?')}")
            print(f"  Applicability: {fm.get('tt_Applicability', '?')}")
            print(f"  Quality Tier:  {fm.get('tt_Quality_Tier', '?')}")
            if quick:
                short = quick.split("\n")[0][:120]
                print(f"  Notes:  {short}")
            # Sprint 18 Card 05: tt_Pairs_Well_With umbrella auto-flag.
            # When the entry declares pair relationships, surface each one as
            # a potential umbrella hint so the runner can consider whether the
            # umbrella concept (e.g., Customer Discovery for Mom Test) also
            # applies. The hint is INFO-level — runner judgment retained.
            pairs = fm.get("tt_Pairs_Well_With")
            if isinstance(pairs, list) and pairs:
                cleaned_pairs = [str(p).strip() for p in pairs if str(p).strip()]
                if cleaned_pairs:
                    print(
                        f"  Note: {title} declares tt_Pairs_Well_With "
                        f"[{', '.join(cleaned_pairs)}] — consider whether an "
                        f"umbrella concept also applies:"
                    )
                    for pair in cleaned_pairs:
                        print(
                            f"    - {pair} (umbrella) pairs with {title} per "
                            f"tt_Pairs_Well_With — apply if substantively "
                            f"engaged."
                        )
            print()
        else:
            print(title)

    if len(matches) > args.limit:
        print(f"\n... and {len(matches) - args.limit} more (raise --limit to see)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
