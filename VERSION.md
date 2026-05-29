---
solve_ex_version: "2.1.0"
master_plan_version: "3.0 STABLE"
schema_version: "1.14.0"
schema_status: "FROZEN"
release_date: 2026-05-29
release_phase: "Minor Release — additive content extension"
ship_sprint: "Sprint 02 (public-release iteration) — ADAPT Loop Integration"
---

# SOLVE eX Version

This is SOLVE eX **v2.1.0** — minor release (additive content extension to v2.0 ship release at v3.0 STABLE freeze).

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Software / corpus**   | v2.1.0        | Minor release — additive content extension at v3.0 STABLE freeze       |
| **Master plan**         | v3.0 STABLE   | Frozen at Sprint 18 close-out; locked at Sprint 19 ship; unchanged     |
| **Schema**              | v1.14.0       | FROZEN — see schema-freeze policy below; unchanged                     |
| **Application Patterns**| 1.0           | + 1 new integrative-session-design pattern (ADAPT Loop)                |
| **Question Banks**      | 1.0           |                                                                        |
| **Personas**            | 1.0           |                                                                        |
| **Case File schema**    | 1.0           |                                                                        |
| **Utility scripts**     | 1.0           |                                                                        |
| **Release date**        | 2026-05-29    |                                                                        |

## Schema-freeze policy

The v1.14.0 schema is **frozen** as of Sprint 19 ship. Any post-ship schema
change requires:

1. An explicit master-plan version bump (v3.x), AND
2. A documented migration crosswalk in `99-Archive/`, AND
3. A migration script in `07-Scripts/`.

Patch-level adjustments that do not change the schema (additional tool
entries within the existing schema, additional sample sessions, additional
question banks within the existing controlled vocabulary, doc clarifications)
do not require a version bump.

## What is in this version

- Folder architecture per master plan Part 3 (12 numbered subfolders +
  99-Archive)
- 14 of 14 Operating Manual chapters in `00-Instructions/` (00 through 14
  + 19, plus `00-cross-chapter-dependencies.md` index)
- 677 thinking tools in `01-Tools/Tool Entries/` (Sprint 05 schema-validated;
  schema v1.14.0)
- Process Framework with all 6 phases / 21 steps documented in
  `02-Process-Framework/`
- Question banks in `03-Question-Banks/` (by-phase-step + by-clarification-need
  + overview)
- Application Patterns in `04-Application-Patterns/`
- Five operational personas in `05-Personas/` (Partner, Counselor, Therapist,
  Guide, Consultant + switching rules + overview)
- Case File template + active workspace + archived examples in `06-Case-Files/`
- Utility scripts in `07-Scripts/` (Python 3.10+, pyyaml only): validation,
  audit, session management, lint suite
- Schema definitions in `08-Schema/` (v1.14.0)
- Sample sessions in `09-Sample-Sessions/`
- Reference material in `10-Reference/` (glossary, FAQ)
- Sprint-by-sprint build history in `99-Archive/`

## Compatibility

- **AI:** any capable assistant that can read markdown and parse YAML
  frontmatter (Claude Sonnet/Opus class, GPT-4 class and above)
- **OS:** Mac, Windows, Linux
- **Python (optional, for utility scripts only):** 3.10+; only third-party
  dependency is `pyyaml`
- **Network:** none required (self-contained corpus)

## Sprint history

The build history is documented in the master plan at **Part 17.5 (Sprint
History)** and in `99-Archive/`. Each sprint has its own archive folder
(`99-Archive/sprint-NN/`) capturing the cards executed, artifacts produced,
acceptance-gate outcomes, and protocol amendments. Sprint 19 is the ship
sprint. Any future post-ship work (patch updates, additive content within
the v3.0 STABLE constraint, or a v3.x bump) is gated by the freeze policy
documented above and in `CONTRIBUTING.md`.

## How to update

Once v3.0 STABLE is shipped, future updates fall into three categories:

1. **Patch updates** (no schema change, no chapter restructuring) — drop-in
   replacement of affected files.
2. **Minor updates within v3.x** (additive schema fields, new patterns, new
   personas) — drop-in replacement of affected files plus inspection of the
   `99-Archive/sprint-NN/` notes for that update.
3. **Major updates (v4.x)** — require migration. See the migration crosswalk
   under `99-Archive/migrations/` and run the relevant schema-migration
   script under `07-Scripts/`. User-authored Case Files in
   `06-Case-Files/_ACTIVE/` are retained across all update types.

## License

See `LICENSE.md`.
