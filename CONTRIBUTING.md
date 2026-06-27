# Contributing to SOLVE eX v2.0

SOLVE eX v2.0 ships as **v3.0 STABLE** (master plan version). Schema
(v1.14.0) and validator behavior are locked. This document describes when
a contribution is in-scope at v3.0 STABLE, when it requires a v3.x version
bump, and how to propose either kind.

For runtime usage and the freeze policy itself, see `OPERATOR-GUIDE.md`
§5. For release history, see `CHANGELOG.md`.

---

## 1. When to propose a v3.x change

A v3.x version bump is required when the contribution changes the
**specification** rather than its content. The triggers:

- **A new failure mode surfaces** in real sessions that existing rules
  (chapter 13, Class A/B/C/D taxonomy, schema rules A–P) do not catch.
  Closing the gap requires either a new rule, an extended rule, or a new
  surface-class — all of which change the spec.
- **A new persona** is needed (e.g., a "Mediator" persona for
  multi-stakeholder conflicts), which extends `05-Personas/` and the
  switching-rule contract in chapter 07.
- **A new application pattern** is needed (e.g., a "Negotiation Protocol"
  pattern), which extends `04-Application-Patterns/` and chapter 05.
- **A new phase or step** is needed in the Process Framework, which
  changes the canonical decomposition.
- **A schema field** is added, removed, renamed, or has its type changed.
- **Validator exit-code semantics** change.
- **Cross-chapter dependencies** are added or restructured.

A v3.x change is a deliberate spec evolution. It is not a casual
addition. It requires a sprint cycle with an acceptance gate panel
re-run (Yelena + Tessa + Mara fresh sessions) to confirm the change
holds in real session conditions.

---

## 2. When NOT to propose a change

The v3.0 schema is frozen. Do NOT:

- Invent new schema fields on tool entries (e.g., the `tt_Quality_Tier`
  facet is deferred to v3.x; do not add it to v1.14.0 entries).
- Rename existing schema fields.
- Change validator exit codes.
- Restructure the chapter numbering in `00-Instructions/`.
- Change persona names, swap their voice characteristics, or alter the
  switching rules.
- Change phase or step numbering in the Process Framework.
- Modify Hugo properties or Hugo_* prototypes (if any exist — these are
  immutable; see project-side memory for the full immutability rule).

These changes silently break downstream tools, audit scripts, and
session-runners that depend on the locked surfaces. If you believe one
of these changes is necessary, see §1 — it is a v3.x bump, not an
in-scope contribution.

---

## 3. What IS in-scope at v3.0 STABLE

The following kinds of contributions do NOT require a version bump:

| Contribution                                                    | File path convention                                                                                                       |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| New tool entry conforming to v1.14.0 schema                     | `01-Tools/Tool Entries/[Tool Name].md`. Run `python3 07-Scripts/validate-tool.py` before committing.                       |
| New sample session                                              | `09-Sample-Sessions/sample-NN-[short-name].md`. Sequential numbering.                                                       |
| New question bank entry within existing controlled vocabulary   | `03-Question-Banks/by-phase-step/phase-N-step-M/[question-set].md` OR `03-Question-Banks/by-clarification-need/[need].md`. |
| New question bank category within existing taxonomy             | Add to existing folder structure. Do NOT create new top-level folders.                                                     |
| New Case File archived example                                  | `06-Case-Files/_ARCHIVED/[descriptive-name].md`. Anonymize identifying details.                                            |
| Doc clarification, typo fix, README improvement                 | Edit in place.                                                                                                              |
| New utility script using existing schema + exit-code conventions | `07-Scripts/[name].py`. Update `07-Scripts/README.md`. Follow existing docstring header convention.                       |
| Sprint archive (post-acceptance-gate)                           | `99-Archive/sprint-NN/sprint-NN-acceptance-gate.md` + related files. Sprint 18+ uses subfolder; earlier sprints used flat. |

---

## 4. How to propose a change

### 4.1 In-scope contribution (no version bump)

1. **Locate the right path** per §3.
2. **Conform to existing conventions.** Read 2-3 existing entries in the
   target folder first to match voice, structure, and metadata format.
3. **Run the relevant validation script.** For tool entries:
   `python3 07-Scripts/validate-tool.py "[file]"` must exit 0. For sample
   sessions: `python3 07-Scripts/voice-neutrality-lint.py "[file]"` must
   exit 0. For Case Files: full audit chain
   (`post-session-audit.py --max-iterations 3`) must exit 0.
4. **No changelog entry needed** for additive in-scope contributions
   unless the addition is substantive (e.g., a new tool category, a
   sample session demonstrating a new edge case worth documenting).

### 4.2 v3.x version bump

1. **Open a sprint** following the protocol in `trelloplan-create.md` /
   `trelloplan-resume.md`. The sprint scope must explicitly include the
   spec change.
2. **Draft the master plan amendment** in the sprint's planning phase.
   Cite the precipitating failure mode (panel run finding, real-session
   observation, schema-pressure pattern) as evidence the bump is warranted.
3. **Author the spec change** — new rule, extended chapter section, new
   schema field, etc. — as the sprint's substantive deliverable.
4. **Extend the relevant validation script** to enforce the new rule. The
   validator change is NOT optional; un-enforced spec is dead spec.
5. **Add a regression test** to `07-Scripts/test-regex-coverage.py` (for
   regex-based rules) or to the relevant script's `tests/` subfolder.
6. **Run the acceptance-gate panel** (Yelena + Tessa + Mara fresh
   sessions via Codex + Claude Desktop). The change must hold in real
   session conditions, not just in unit tests. A panel regression
   indicates the change is incomplete or wrong.
7. **Update the master plan CHANGELOG** with the new v3.x version
   number, the precipitating finding, the spec change, and the panel
   confirmation.
8. **Update root `CHANGELOG.md`** (this corpus's CHANGELOG, not the
   master plan's) with a brief entry pointing to the master plan
   CHANGELOG for full detail.
9. **Update `VERSION.md`** with the new master plan version and
   schema version (if applicable).

### 4.3 Migration crosswalks (when schema changes)

If the v3.x bump changes the schema, a **migration crosswalk** is
required. Conventions:

- Crosswalk file: `99-Archive/migrations/v1.14.0-to-v[new-version].md`.
- Migration script: `07-Scripts/migrate-schema-v[new-version].py`.
- The crosswalk documents the field-by-field mapping; the script
  performs the mechanical conversion.
- Existing user-authored Case Files in `06-Case-Files/_ACTIVE/` are
  retained across schema migrations — the migration script touches
  system files only.

---

## 5. Voice and tone conventions

When authoring content that may end up in AI-readable surfaces (tool
entries, chapter prose, application patterns), respect the chapter 13
voice-neutrality taxonomy:

- **Class A — composition-meta:** Banned in chat-visible surfaces. Do
  NOT emit infrastructure announcements, sysadmin-style state lists,
  composition-of-self meta-commentary.
- **Class B — voice projection:** Banned in chat-visible surfaces. No
  authorial personality, no aphorisms, no jokes, no sentimentality.
- **Class C — Phase 0 readiness leaks:** Banned. Readiness statements
  are user-facing prose, not key:value system-state fields.
- **Class D — adjective injection / paraphrasing with emotional
  coloring:** Banned. Reflect the user's words; do not add adjectives
  they did not use.

Operator-facing docs (this file, `OPERATOR-GUIDE.md`, `README.md`,
`INSTALL.md`, `CHANGELOG.md`) are NOT chat-visible AI surfaces and have
looser tone rules — direct, explanatory prose is fine. But material that
moves into AI-readable surfaces (tool entries, chapter content, sample
sessions, persona files) must conform to chapter 13.

---

## 6. Reporting failures

If you discover a failure mode the existing spec does not catch:

1. **Capture the leak verbatim.** Copy the AI's exact emitted text
   (the violation, not your paraphrase). This becomes the canonical
   test case for the regex/rule that will close the gap.
2. **Open an issue** (project-internal tracker or a `99-Archive/issues/`
   markdown file if no tracker exists).
3. **Classify the failure** by Class A/B/C/D or by schema rule (A–P).
   If it doesn't fit existing classes, note that — a new class or rule
   may be needed.
4. **Propose a fix** per §4.2 (v3.x bump) if the gap requires spec
   change, or per §4.1 (in-scope) if it's a content-only fix.
5. **The next panel run validates the fix.** The acceptance-gate panel
   re-runs the canonical test cases; the new failure case must be in
   the panel's regression suite.

### Discipline: do NOT propose more regex patterns to close L1 leaks

**If the failure you discover is a NEW shape of cognitive-load-correlated
compose-time discipline degradation** (see `OPERATOR-GUIDE.md` §7 — L1
Known Limitation), the appropriate response is NOT to propose another
regex pattern. The L1 architectural pattern means new shapes emerge
faster than regex coverage can chase, and each new pattern adds
maintenance burden + collateral false-positive risk. Sprint 19 Card
04-B Pattern U decision (skip "switching gears") and Sprint 19 Card
04-F Fix 2 (Pattern D over-fire on audit-trail prose, scoped via
placeholder detection) are the canonical examples of this discipline.

Instead:

- Add the new shape to the L1 documented surfaces in `OPERATOR-GUIDE.md`
  §7 as evidence (not as a fix).
- If the cumulative cross-surface degradation is significant
  downstream, propose a v3.x bump (per §1 above) targeting the
  architectural root cause: compose-time runtime hook + spec-contract
  conversion of regex-enumeration cards.

The spec-contract cards (Card 12 Rule J ↔ §6.4.0, Card 03 Rule P,
Card 04 Rule D, Card 04-D Rule Q) hold uniformly across cohorts in
Sprint 19 panel evidence. New spec contracts are the in-scope-for-
v3.x response to L1 patterns; new regex enumeration is the
out-of-scope-for-this-iteration response.

---

## 7. Content zones (OVE Convention 8)

Every file in this repo belongs to one of four zones. Knowing which zone a file is in tells you whether the release owns it (the engine) or the operator owns it.

### Engine Zone — release-owned; updated by `git pull`

| Path pattern | Notes |
|--------------|-------|
| `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md` | Front-door docs |
| `00-Instructions/` through `05-Personas/` | Engine corpus (instructions, tools, process framework, question banks, application patterns, personas) |
| `07-Scripts/` | Optional utility scripts (validation, audit) |
| `08-Schema/` | Schema definitions |
| `09-Sample-Sessions/`, `10-Reference/` | Shipped reference material |
| `99-Archive/` | Sprint history and prior-iteration archives |
| `_types/` | OVE Convention 6 — SOLVE-eX's Type definitions (currently: `Thinking_Tool.md`) |
| `.gitignore` | Engine-zone file |

**Engine Zone files do not get hand-edited by operators.** Customizations belong in `06-Case-Files/` (your case work) or in a fork.

### Operator-Private Zone — gitignored; never tracked

| Pattern | Why |
|---------|-----|
| `_USER.md` (if present) | Operator profile; identity, preferences, personal context (F3) |
| `06-Case-Files/_ACTIVE/**` | Active case-file work; client/context-specific |
| `06-Case-Files/_DRAFT/**` | Draft case files; operator working state |
| `.DS_Store`, IDE caches | Filesystem-noise |
| `.venv/`, `__pycache__/` | Python artifacts |

These patterns are in `.gitignore`. The `_RESOLVED/` and `_REFERENCE/` subdirectories of `06-Case-Files/` may contain shipped reference cases (Shipped Examples Zone); operator-specific resolved cases are gitignored per pattern.

### Operator-Extension Zone — operator-created; survives `git pull`

The OV is designed to be extended in `06-Case-Files/`.

| Pattern | Notes |
|---------|-------|
| `06-Case-Files/_ACTIVE/<your-case>/` | Active case work; not in the release; untracked |
| `06-Case-Files/_RESOLVED/<your-case>/` | Your resolved cases; tracked once `git add -f`'d |
| Custom tools in `01-Tools/Tool Entries/<your-tool>.md` | Operator-authored Tool Entries (if you fork to extend the canonical library) |

`git pull` never touches `_ACTIVE/` and `_DRAFT/` because they're gitignored. Other operator extensions need a fork to persist across pulls.

### Shipped Examples Zone — release-owned; updated by `git pull`

| Path | Notes |
|------|-------|
| `09-Sample-Sessions/**` | Worked-example sessions demonstrating the OV |
| `06-Case-Files/_REFERENCE/**` | Reference case files (illustrative; not operator-private) |
| `01-Tools/Tool Entries/**` | The canonical 30+ Tool Entries (Thinking Tools library) |

**Shipped Examples are reference implementations.** If you want to riff on one, copy it into your own case-file folder under `_ACTIVE/`.

---

## Version

This contribution guide ships with SOLVE eX v2.1.2 / master plan v3.0
STABLE. See `VERSION.md` and `CHANGELOG.md`.
