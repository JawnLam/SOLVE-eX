---
doc_type: schema_reference
audience: ai_and_human
read_order: 3
last_updated: 2026-05-13
schema_version: "1.14.0"
---

# Tool Entry Validation Rules

These are the rules enforced by `{ROOT}/07-Scripts/validate-tool.py`.

A tool entry is **valid** when every rule below passes. Any failure produces
an error message on stderr and a non-zero exit code.

---

## A. File structure rules

| # | Rule | Failure message |
|---|------|-----------------|
| A1 | File exists and is readable | `cannot read file: {path}` |
| A2 | File ends in `.md` | `not a markdown file: {path}` |
| A3 | Filename uses Title Case with spaces, no leading number, no leading/trailing whitespace, no characters illegal on Windows (`< > : " \| ? *`) | `invalid filename: {filename}` |
| A4 | File begins with YAML frontmatter block delimited by `---` lines | `missing or malformed frontmatter` |
| A5 | YAML frontmatter parses cleanly with `yaml.safe_load` | `yaml parse error at line N: {message}` |
| A6 | File body (after frontmatter) contains a heading `# {Title}` whose text matches the `Title:` frontmatter field | `body heading does not match Title` |

---

## B. Required-property rules

Each property below must be present in the frontmatter (no missing keys, no
`null`/`None` values where a value is expected).

| Property | Cardinality | Validator |
|----------|-------------|-----------|
| `Item_ID` | single | non-empty string starting with `tt-` |
| `Item_Prototype` | single | literal: `Thinking_Tool` |
| `Title` | single | non-empty string |
| `tt_Source` | single | non-empty string |
| `tt_Type` | single | enum value from `tt_types` |
| `tt_Domain` | single | enum value from `tt_domains` |
| `tt_Field` | single | non-empty string |
| `tt_Operation` | single | non-empty string |
| `tt_Form` | multi-value list | enum values from `tt_forms`; **may be empty list IF `tt_Type=stance`** |
| `tt_Scale` | multi-value list (≥1) | each value from `tt_scales` |
| `tt_Duration` | multi-value list (≥1) | each value from `tt_durations` |
| `tt_Lineage` | multi-value list (≥1) | each value from `tt_lineages` |
| `tt_Posture` | multi-value list (≥1) | each value from `tt_postures` |
| `tt_SOLVE_eX_Phase` | multi-value list (≥1) | each value from `tt_solve_ex_phases` |
| `tt_SOLVE_eX_Step` | multi-value list (≥1) | each value from `tt_solve_ex_steps` (note: quoted as strings, e.g. `"1.1"`) |
| `tt_Clarifies` | multi-value list (≥1) | each value from `tt_clarifies_values` |
| `tt_Applicability` | single | enum value from `tt_applicability_values` |
| `tt_Status` | single | enum value from `tt_statuses` |

---

## C. Enum-value rules (OOV detection)

For every property whose validator references an enum from
`{ROOT}/08-Schema/Master_Schema.yaml`, each value in the entry must appear
**verbatim** in the schema's enum list. Out-of-vocabulary values fail with:

> `OOV violation: {Property}={Value} not in {enum_name}`

This is the most common failure class. Causes:

1. Typo (e.g., `Mental Model` vs `Mental model`)
2. Drift (inventing a new value not in the canonical inventory)
3. Schema mismatch (entry written against a different schema version)

**Fix:** open `{ROOT}/08-Schema/facet-enums.md`, find the exact canonical
string, replace verbatim. If you believe the canonical inventory is missing a
genuine value, follow the Saturation Sweep methodology before adding —
**do not silently extend the enum**.

---

## D. Cross-field consistency rules

| # | Rule |
|---|------|
| D1 | If `tt_Type = stance`, then `tt_Form` MUST be an empty list (`[]`) — stances have no Form. |
| D2 | If `tt_Type = instrument`, then `tt_Form` MUST contain at least one Form value. |
| D3 | `tt_Operation` should appear in the canonical 36-operation inventory in `{ROOT}/01-Tools/Index of Thinking Tools.md`. Drift produces a **warning**, not an error (Operation is free-string by schema, curated by convention). |
| D4 | `tt_Status = classified` requires non-empty `# {Title}` body content (at least the One-line summary line). |
| D5 | If any value in `tt_Often_Precedes`, `tt_Often_Follows`, `tt_Pairs_Well_With`, or `tt_Replaced_By` is present, each must reference an existing tool entry file in `{ROOT}/01-Tools/Tool Entries/`. |

---

## E. Optional-property rules

These properties may be empty or absent; if present they must satisfy:

| Property | Validator |
|----------|-----------|
| `tt_Cross_Domains` | each value from `tt_domains` |
| `tt_State` | each value from `tt_states` |
| `tt_Agent` | each value from `tt_agents` |
| `tt_About` | each value from `tt_abouts` |
| `tt_Often_Precedes` | list of tool names (D5 enforces existence) |
| `tt_Often_Follows` | list of tool names |
| `tt_Pairs_Well_With` | list of tool names |
| `tt_Replaced_By` | list of tool names |
| `tt_History` | list of strings; each entry conventionally starts with `YYYY-MM-DD — ` |

---

## F. Body content rules (informational only)

The script issues **warnings** (not errors) when:

- The body lacks a `## Purpose` section.
- The body lacks a `## How To Use` section (waived for `tt_Type=stance`).
- The body lacks a `## Sources` section AND `tt_Source` contains no detail
  beyond a single sentence.

---

## G. Exit codes

| Code | Meaning |
|------|---------|
| `0` | All rules pass (warnings may be printed). |
| `1` | At least one rule from sections A–E failed. |
| `2` | YAML parse error specifically (covers A4–A5). |
| `3` | File-not-found or permission error. |

---

## H. Validation against the full corpus

To validate all 677 entries at once:

```bash
find "{ROOT}/01-Tools/Tool Entries" -name '*.md' -print0 \
  | xargs -0 -n1 python3 "{ROOT}/07-Scripts/validate-tool.py"
```

Or run the corpus audit pattern from Sprint 05's Card 11:

```bash
python3 "{ROOT}/07-Scripts/validate-tool.py" --corpus "{ROOT}/01-Tools/Tool Entries"
```

(Corpus mode is added in Phase 2; the single-file mode is the MVP.)

---

## I. Common failure-recovery patterns

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Entry passes per-file but corpus count drops after a bulk edit | `yaml.safe_load` silently skipped a malformed file via the bulk-edit script's `try/except` | Re-run validate per-file on every file in the corpus; the failing one will surface the YAML error |
| `OOV violation: tt_Domain=Mental Model not in tt_domains` | Confused Domain with Form | `Mental model` is a `tt_Form`, not a `tt_Domain`. Fix the Domain to one of the 12 canonical Domains. |
| `OOV violation: tt_SOLVE_eX_Step=1.1 not in tt_solve_ex_steps` | Step values written as numbers instead of strings | Step values must be YAML strings (`"1.1"`), not numbers (`1.1`), because `1.1` is a float that round-trips lossy. |
| Inner double-quotes break YAML parse | A string value contains an unescaped `"` | Either escape (`\"`) or single-quote-wrap the outer value. |

---

## J. Adding a new validation rule

If a recurring failure mode emerges:

1. Document the failure pattern in this file's section H or I.
2. Add the rule to `validate-tool.py`.
3. Bump the schema patch version (e.g., `1.14.0` → `1.14.1`) in
   `Master_Schema.yaml`.
4. Note the change in `VERSION.md` and `99-Archive/`.
