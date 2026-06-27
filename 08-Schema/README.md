---
doc_type: schema_readme
audience: ai_and_human
read_order: 1
last_updated: 2026-05-13
---

# Schema — README

This folder is the **single source of truth** for the data model that governs
every tool entry in `{ROOT}/01-Tools/Tool Entries/` and every facet-driven
script in `{ROOT}/07-Scripts/`.

## Files in this folder

| File | Purpose |
|------|---------|
| `Master_Schema.yaml` | The authoritative schema. Property definitions, enums, types, and global rules. Copied from the Obsidian Vault infrastructure on every release. |
| `facet-enums.md` | Human-readable inventory of the `tt_*` facet enums (Domain, Form, Scale, Duration, Lineage, Posture, State, Agent, About, SOLVE_eX_Phase, SOLVE_eX_Step, Clarifies, Applicability, Status). Generated from `Master_Schema.yaml`. |
| `tool-entry-template.md` | Empty tool-entry template with all required and optional `tt_*` properties pre-stubbed. Copy this when adding a new tool. |
| `validation-rules.md` | The rules used by `07-Scripts/validate-tool.py` — what counts as a valid tool entry, what counts as an OOV violation, what error messages mean. |

## Schema version

Current: **v1.14.0** (locked 2026-05-13, Sprint 05).

**schema-frozen-at: v2.0** (Sprint 18 Card 08, 2026-05-22). The library-entry
schema (`tt_*` namespace, types, validation rules) is FROZEN for the v2.0
ship. Adding new facets, modifying existing facet enums, or changing type
membership requires a schema-version bump + migration script discipline per
`00-Instructions/19-governance-and-quality.md`. The Case File frontmatter
schema is similarly frozen at `schema_version: "1.0-frozen"` (per
`06-Case-Files/_TEMPLATE.md`); `07-Scripts/validate-case-file.py`
`KNOWN_SCHEMA_VERSIONS` enforces the freeze at validation time.

`v1.14.0` adds four properties to make the library SOLVE eX v2.0-ready:

1. `tt_SOLVE_eX_Phase` (multi-value enum: 1–6, any) — phase-affinity routing.
2. `tt_SOLVE_eX_Step` (multi-value enum: 1.1–6.4, any) — step-affinity routing.
3. `tt_Clarifies` (multi-value enum: Origin, Destination, Path, Action, None) —
   first-cut filter in the v2.0 Tool Selector.
4. `tt_Applicability` (single-value enum: runtime_applicable, describable_only,
   requires_tradition_transmission) — whether the AI can guide enactment.

All 677 tool entries are populated at v1.14.0.

## The `tt_*` namespace at a glance

Required for every tool entry:

| Property | Cardinality | Source of values |
|----------|-------------|------------------|
| `Item_ID` | single | derived: `tt-{kebab-title}` |
| `type` | single | literal: `Thinking_Tool` |
| `Title` | single | tool's canonical name |
| `tt_Source` | single | citation(s) |
| `tt_Type` | single | enum `tt_types`: `instrument` or `stance` |
| `tt_Domain` | single | enum `tt_domains` (12 register-clean values) |
| `tt_Field` | single | open-but-curated; see Thinking Tools Index |
| `tt_Operation` | single | open-but-curated (36 canonical values) |
| `tt_Form` | multi-value | enum `tt_forms` (16 values); empty if `tt_Type=stance` |
| `tt_Scale` | multi-value | enum `tt_scales` (7 values) |
| `tt_Duration` | multi-value | enum `tt_durations` (5 values) |
| `tt_Lineage` | multi-value | enum `tt_lineages` (15 values) |
| `tt_Posture` | multi-value | enum `tt_postures` (9 values) |
| `tt_SOLVE_eX_Phase` | multi-value | enum `tt_solve_ex_phases` (1–6, any) |
| `tt_SOLVE_eX_Step` | multi-value | enum `tt_solve_ex_steps` (1.1–6.4, any) |
| `tt_Clarifies` | multi-value | enum `tt_clarifies_values` (5 values) |
| `tt_Applicability` | single | enum `tt_applicability_values` (3 values) |
| `tt_Status` | single | enum `tt_statuses` (`proposed`, `in-progress`, `classified`, `deprecated`) |

Optional but commonly populated: `tt_Cross_Domains`, `tt_State`, `tt_Agent`,
`tt_About`, `tt_Often_Precedes`, `tt_Often_Follows`, `tt_Pairs_Well_With`,
`tt_Replaced_By`, `tt_History`.

See `facet-enums.md` for the full enum tables.

## How the schema is used

- **AI Tool Selector** filters and ranks tool entries against the active
  Case File state, using the facets above. See
  `{ROOT}/00-Instructions/04-the-tool-selection-process.md` (Phase 2).
- **`07-Scripts/validate-tool.py`** rejects entries with missing required
  properties, OOV facet values, or malformed YAML.
- **`07-Scripts/find-tools.py`** queries the library by facet.
- **Schema migration** between versions uses crosswalk files in
  `{ROOT}/99-Archive/` and migration scripts in `07-Scripts/`.

## Editing the schema

Do not edit `Master_Schema.yaml` in this folder directly. It is downstream from
the Obsidian Vault infrastructure (`_Infrastructure For All Vaults/Master_Schema.yaml`).
Edits there propagate here on the next release.

For controlled-vocabulary additions (e.g., a new `tt_Field` value), follow the
Saturation Sweep methodology referenced in the master plan Part 19.3.

## Hugo namespace warning

The `hugo_*` properties and `Hugo_*` prototypes in `Master_Schema.yaml` are
**immutable**. They target a separate static-site generator and are unrelated
to SOLVE eX v2.0. Do not modify them.
