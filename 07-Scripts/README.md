# Scripts — README

Utility scripts for SOLVE eX v2.0. All run on stock Python 3.10+ with
only `pyyaml` as a third-party dependency.

## MVP scripts (Phase 1)

| Script | Purpose | Usage |
|--------|---------|-------|
| `find-tools.py` | Query the library by facet | `python3 find-tools.py --phase 2 --clarifies Destination` |
| `new-case-file.py` | Create a new Case File from `_TEMPLATE.md` | `python3 new-case-file.py --title "Job decision"` |
| `validate-tool.py` | Validate a tool entry against the schema | `python3 validate-tool.py "../01-Tools/Tool Entries/Eisenhower Matrix.md"` |

## Phase 2 scripts (deferred)

- `validate-case-file.py` — schema-validate a Case File
- `search-questions.sh` — grep across question banks
- `show-stack.py` — visualize the goal-stack from a Case File
- `portability-check.py` — pre-distribution validation
- `list-tools-by-facet.sh` — one-liner facet query
- `case-file-summary.py` — human-readable summary of a Case File

## Conventions

All MVP scripts:

- Print results to stdout.
- Use `--help` for usage.
- Exit code 0 on success, non-zero on failure.
- Do not modify files outside the SOLVE eX folder.
- Do not require network access.
- Find their own SOLVE eX root by walking up from the script's location
  (look for the parent directory that contains `AI-BOOTSTRAP.md`).
  This makes the scripts portable; you can copy the entire folder
  to any path and the scripts still work.

## Dependencies

```bash
pip install pyyaml
```

`pyyaml` is the only third-party dependency. Everything else is stdlib.

## Running on different platforms

- **macOS:** System Python 3.10+ ships with macOS 13+. Install pyyaml
  via `pip3 install pyyaml`.
- **Linux:** Most distributions ship Python 3.10+ in 2024+. On older
  distros, install via package manager. `pip install --user pyyaml`
  if you can't install system-wide.
- **Windows:** Install Python 3.10+ from python.org or the Microsoft
  Store. `py -m pip install pyyaml`.

## Testing

Quick sanity test for each MVP script:

```bash
# find-tools.py — should return a non-empty list
python3 find-tools.py --phase 2 --clarifies Destination

# new-case-file.py — should create a file in _ACTIVE/
python3 new-case-file.py --title "test"
ls ../06-Case-Files/_ACTIVE/

# validate-tool.py — should pass on a real tool entry
python3 validate-tool.py "../01-Tools/Tool Entries/Eisenhower Matrix.md"
```

## Library code

Shared helpers live in `lib/`. MVP `lib/` is minimal — Phase 2 may
introduce a small helper module for repeated YAML parsing.

## Compound-title alias matching (Sprint 18 Card 05)

`validate-case-file.py` Rules J + L use the `_title_aliases()` helper to
accept compound canonical titles. When a tool entry's `Title:` field
contains a top-level `/` (e.g., `Title: Critical Chain / Critical Path`
paired with filename `Critical Path.md`), Rule J + Rule L accept EITHER
half as a valid canonical chat-form reference. Top-level slashes only —
parenthetical sub-lists like `PMI (Plus / Minus / Interesting)` are NOT
split (the slashes are part of the canonical name, not alternative
forms). See `99-Archive/compound-title-tool-entries.md` for the
inventory (45 entries as of Sprint 18 Card 05).

## tt_Pairs_Well_With umbrella hint (Sprint 18 Card 05)

`find-tools.py --name <tool>` (or any verbose query) now surfaces
`tt_Pairs_Well_With` relationships as INFO hints. For each declared
pair, the output emits a line like `Customer Discovery (umbrella) pairs
with Mom Test per tt_Pairs_Well_With — apply if substantively engaged`.
The hint helps the runner consider whether the umbrella concept also
applies — runner judgment retained (the hint is informational, not a
mandate). Example:

```bash
python3 find-tools.py --name "Mom Test"
```
