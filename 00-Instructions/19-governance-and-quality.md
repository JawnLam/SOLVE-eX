---
doc_type: instruction
doc_purpose: governance_and_quality
audience: ai_and_human
read_order: 19
last_updated: 2026-05-22
---

# 19. Governance and Quality (Sprint 18 Card 08)

This chapter documents the v2.0 ship governance disciplines: schema freeze,
dev-path cleanup conventions, 99-Archive organization. It is read-on-demand
during ship-readiness reviews, not during routine sessions.

## 19.1 Schema freeze policy

**Frozen as of Sprint 18 Card 08 (2026-05-22):**

| Schema | Frozen value | Source of truth | Enforced by |
|--------|--------------|-----------------|-------------|
| Library entry (`tt_*` namespace) | v1.14.0 | `08-Schema/Master_Schema.yaml` | `07-Scripts/validate-tool.py` |
| Case File frontmatter | `1.0-frozen` | `06-Case-Files/_TEMPLATE.md` `schema_version` field | `07-Scripts/validate-case-file.py` Rule B-extended |
| Application pattern schema | implicit | `04-Application-Patterns/*.md` structure | `04-Application-Patterns/_audit.sh` (if any) |
| Rubric | rubric-v2 | `99-Archive/rubric-v2.md` | scoring discipline (test prompt v5) |

### Adding a new schema-version

The schema is FROZEN for v2.0. Adding new frontmatter fields, modifying
existing facet enums, or changing prototype membership requires:

1. **Schema-version bump.** Add the new value to `KNOWN_SCHEMA_VERSIONS`
   in `validate-case-file.py` (or the equivalent allow-list for the
   relevant schema layer).
2. **Migration script.** Write a one-shot `07-Scripts/migrate-<from>-to-<to>.py`
   that converts existing Case Files / Tool Entries from the old schema to
   the new schema version. The script MUST be idempotent (re-running on a
   migrated file is a no-op).
3. **Validation gate.** `validate-case-file.py` (or `validate-tool.py`)
   must accept BOTH the old and new schema-version values until the
   migration is fully applied across the corpus.
4. **Documentation.** Update this chapter's freeze-policy table + the
   schema's README.md (e.g., `08-Schema/README.md`).

### Why this exists

Sprint 13-17 panel runs revealed several schema drift patterns: facets
silently added to Master_Schema.yaml without corresponding validation
updates; new Case File frontmatter fields appearing in some test CFs but
not the template; validation-rules.md falling behind actual enforcement
behavior. The schema freeze locks the v2.0 contract so Sprint 19 ship
carries a known surface — and any post-ship schema change goes through
the migration-script discipline rather than ad-hoc field additions.

## 19.2 Dev-path cleanup conventions

Production code (chapters 00-14 + scripts in 07-Scripts/ + library entries
in 01-Tools/) is held to "ship-ready" standards:

- **No TODO / FIXME / XXX comments** in chapter content or script source.
  If a deferral is needed, document it explicitly in a "Deferred to v3.0"
  section of the relevant document with a Sprint NN cross-reference.
- **Placeholder content** (`[populated by Card NN]`, `<!-- ... -->`) is
  acceptable when load-bearing for the document's structure (e.g., the
  Case File _TEMPLATE.md placeholder blocks ARE the template — production-
  permanent). Otherwise resolve before ship.
- **Hardcoded paths.** Production scripts use `{ROOT}` substitution OR
  walk-up-to-AI-BOOTSTRAP.md resolution (see `lib/solve_ex.py find_root()`).
  Test fixtures and one-off scripts may use absolute paths if scoped to
  `07-Scripts/tests/` or `/tmp/`.
- **test_mode references** in production code paths are tagged with
  `# PRODUCTION-NOTE: test-mode-only` so a future schema audit can
  distinguish test-fixture code from production logic.

## 19.3 99-Archive organization

`99-Archive/` is the deprecated-and-historical surface. Sprint 18 Card 08
established the following conventions:

- **`README.md`** is the index. Lists every artifact with a status
  (CURRENT / LEGACY / RETIRED), date range, and brief description.
- **`sprint-roadmap.md`** is the longitudinal overview — every sprint's
  panel outcome, dispositive validations, ship trajectory in one page.
- **Sprint folders (`sprint-NN/`)** organize each sprint's artifacts.
  Each sprint folder typically contains: `sprint-NN-acceptance-gate.md`
  (the panel run), `sprint-NN-cross-test-analysis.md` (cross-test
  synthesis), `sprint-NN-closeout-handoff.md` (close-out handoff). Some
  sprints have additional files (debriefs, investigations).
- **`legacy/` subfolder** holds superseded artifacts whose canonical
  successor lives elsewhere. Example: `legacy/test-prompts/` for
  test-prompt-v1/v2/v3 once v5 supersedes them.
- **`test-cases/`** holds the persona test-case files (Yelena, Tessa,
  Mara, etc.) that drive panel runs. Not legacy; CURRENT through the
  ship lifetime.

### Reorganization deferred

The Sprint 18 Card 08 99-Archive reorganization (moving 25+ sprint files
into sprint-NN/ folders) is a substantial file-move operation with
risk of breaking cross-references in chapter content. Sprint 18 ships
the README.md index + sprint-roadmap.md + this governance chapter; the
folder reorganization is deferred to Sprint 19 ship-readiness or to a
dedicated reorg sprint post-v2.0.

## 19.4 Next read

See `08-Schema/README.md` for library-entry schema details.
See `99-Archive/README.md` for the archive index.
See `99-Archive/sprint-roadmap.md` for the longitudinal sprint overview.
