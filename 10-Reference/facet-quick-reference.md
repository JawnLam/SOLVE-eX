---
doc_type: reference
doc_purpose: facet_quick_reference
audience: ai_and_human
read_order: 4
last_updated: 2026-05-14
schema_version: "1.14.0"
note: "tt_Quality_Tier (added in v1.15.0 by Sprint 08 Card 16) is documented at the bottom of this file pending Card 16 schema bump."
---

# Facet Quick Reference

A one-page-per-facet reference for the SOLVE eX tool schema. For the
canonical enumerated values, see `{ROOT}/08-Schema/facet-enums.md`. This
file is the **discriminator-and-use-case** view: what each facet
discriminates between, and when an AI surfacing a tool would filter on it.

For the full schema source, see `{ROOT}/08-Schema/Master_Schema.yaml`.

---

## tt_Type (single-value)

**Discriminates:** Whether the tool is a *thing to apply* (instrument)
or a *mode to enter* (stance).

**Values:** `instrument`, `stance`.

**When to filter:** Stance tools have no `tt_Form` and are governed by
the `pattern-stance-embodied.md` application pattern. Filter on
`tt_Type` when the session needs a posture-shift rather than a
fillable artifact.

---

## tt_Domain (single-value, 12 values)

**Discriminates:** The cognitive register the tool operates in.

**Sample values:** `Discursive-analytical`, `Embodied / somatic`,
`Contemplative`, `Aesthetic`, `Phronetic / practical wisdom`.

**When to filter:** Match the user's current register. A user in a
spreadsheet mood (`Discursive-analytical`) is not served by a
`Contemplative` tool, and vice versa.

**Note:** `tt_Cross_Domains` (multi-value, optional) holds secondary
domains for tools that span registers.

---

## tt_Form (multi-value, 16 values)

**Discriminates:** The application pattern that governs how the tool
is enacted. Empty if `tt_Type = stance`.

**The 16 values map 1:1 to pattern files** in
`{ROOT}/04-Application-Patterns/`:

| `tt_Form` | Pattern file |
|-----------|--------------|
| Matrix | `pattern-matrix.md` |
| Canvas | `pattern-canvas.md` |
| Sequenced workflow | `pattern-sequenced-workflow.md` |
| Question bank | `pattern-question-bank.md` |
| Dialogue protocol | `pattern-dialogue-protocol.md` |
| Mental model | `pattern-mental-model.md` |
| Scoring rubric | `pattern-scoring-rubric.md` |
| Visualization technique | `pattern-visualization-technique.md` |
| Decision tree | `pattern-decision-tree.md` |
| Narrative template | `pattern-narrative-template.md` |
| Heuristic | `pattern-heuristic.md` |
| Algorithm | `pattern-algorithm.md` |
| Mnemonic | `pattern-mnemonic.md` |
| Game / simulation | `pattern-game-simulation.md` |
| Practice / ritual | `pattern-practice-ritual.md` |
| Checklist | (falls back to `pattern-sequenced-workflow.md`) |

**When to filter:** Once a tool is surfaced, the AI loads the matching
pattern file before introducing the tool to the user. Filter on
`tt_Form` when the user has indicated a preference for a particular
mode of work (e.g., "let's do a matrix").

---

## tt_Scale (multi-value, 7 values)

**Discriminates:** The unit of analysis the tool operates on
(individual, dyad, small group, organization, society, etc.).

**When to filter:** Match the scope of the user's question. A
personal-decision tool is wasted on an org-design question; a
multi-stakeholder tool is wasted on a solo reflection.

---

## tt_Duration (multi-value, 5 values)

**Discriminates:** How long the tool typically takes to apply.

**When to filter:** Filter on duration when time-pressure is part of
the diagnosis. Operator-mode under tight time budget benefits from
shorter-duration tools.

---

## tt_Lineage (multi-value, 15 values)

**Discriminates:** The tradition or discipline the tool comes from
(behavioral economics, contemplative traditions, military strategy,
philosophy, clinical psychology, etc.).

**When to filter:** Match the user's epistemic comfort zone. A user
allergic to woo-coded language benefits from `Empirical / analytical`
lineage tools; a user open to contemplative work benefits from
`Contemplative` lineage tools.

---

## tt_Posture (multi-value, 9 values)

**Discriminates:** The stance toward the problem the tool encourages
(analytic, generative, reflective, decisive, etc.).

**When to filter:** Match the user's current phase-step needs.
Generative posture in divergent phases (Phase 4.2 — idea formation);
decisive posture in convergent phases (Phase 5.2 — decision tool).

---

## tt_State (multi-value, 7 values, OPTIONAL)

**Discriminates:** The user's mental or emotional state the tool is
appropriate for.

**When to filter:** Match the user's current emotional state. A tool
keyed to `regulated` is contraindicated when the user is in
`overwhelmed` or `grieving`.

---

## tt_Agent (multi-value, 6 values, OPTIONAL)

**Discriminates:** Who or what runs the tool — user solo, user with
the AI, user with another person, a group, an organization.

**When to filter:** Match the actual application context. A
solo-only tool is wasted on a session intended to inform a team
conversation.

---

## tt_About (multi-value, 14 values, OPEN-EXTENSIBLE)

**Discriminates:** The subject matter the tool addresses (career,
relationships, finance, health, learning, etc.).

**When to filter:** Substantive content match. Use sparingly — most
real situations cross multiple `tt_About` values; filtering too
narrowly drops good fits.

---

## tt_SOLVE_eX_Phase (multi-value, 7 values)

**Discriminates:** Which of the six SOLVE eX phases (Search, Order,
Look, Verify/Validate, Execute) plus the cross-cutting "any" the tool
applies to.

**When to filter:** This is the primary phase-step matching facet.
Filter on the user's current Phase (per the Case File's working
diagnosis).

---

## tt_SOLVE_eX_Step (multi-value, 22 values)

**Discriminates:** Which specific step within a phase the tool
applies to (e.g., `1.1`, `5.2`, `6.3`).

**When to filter:** Sharper filter than `tt_SOLVE_eX_Phase`. Use when
the working diagnosis names the specific step.

---

## tt_Clarifies (multi-value, 5 values)

**Discriminates:** Which of the four diagnostic-frame elements the
tool clarifies — Origin, Destination, Path, Action — plus `None` for
tools that don't fit the four-element model.

**When to filter:** This is the primary diagnostic-need filter. The
diagnostic loop's step 7 surfaces which of the four needs the most
clarification work; filter `tt_Clarifies` on that value.

---

## tt_Applicability (single-value, 3 values)

**Discriminates:** How directly the tool can be applied in
conversation.

**Values:** `runtime_applicable` (AI walks the tool with the user in
session), `describable_only` (AI describes; user applies on their
own), `requires_tradition_transmission` (the depth requires a teacher-
student lineage; AI orients only).

**When to filter:** Filter on `runtime_applicable` by default. Use
`describable_only` when the user has the capacity to do the work on
their own and the conversation can hand off cleanly. Use
`requires_tradition_transmission` only when explaining what's out
there, never when intending to apply.

**Note:** The describe-vs-transmit distinction is load-bearing for
`pattern-practice-ritual.md` and `pattern-stance-embodied.md`.

---

## tt_Status (single-value, 4 values)

**Discriminates:** The lifecycle state of the tool entry in the
library.

**Values:** `active` (in use), `deprecated` (superseded but not yet
removed), `experimental` (new addition under evaluation), `archived`
(historical).

**When to filter:** Filter on `active` by default. `experimental`
tools may surface for advanced users; `deprecated` and `archived`
tools surface only when explicitly requested or for historical
context.

---

## tt_Quality_Tier (single-value, 4 values) — added Sprint 08 v1.15.0

**Discriminates:** A curated quality assessment for tool entries,
independent of `tt_Status`.

**Values (per v1.15.0):**

| Tier | Meaning |
|------|---------|
| `A` | High-quality, well-vetted, frequently load-bearing in real sessions |
| `B` | Solid; appropriate fit for most use cases |
| `C` | Workable; included for completeness; check fit carefully |
| `D` | Marginal; included for breadth; consider alternatives first |

**When to filter:** Tier-aware ranking is implemented in
`find-tools.py`. By default, the script ranks tier `A` above `B`
above `C` above `D` when other facets are equal. Filter explicitly on
`tt_Quality_Tier` only when the user has indicated they want to see
all tools regardless of curated quality, or only A-tier tools.

**Note:** `tt_Quality_Tier` is independent of `tt_Status` — a tool can
be `A`-tier and `experimental`, or `D`-tier and `active`. The tiering
is curated quality; the status is lifecycle.

**Reference:** see Sprint 08 Card 16 documentation for tier
definitions and the audit process that assigned tiers to the 677
initial library entries.

---

## How to use this reference

For interactive filtering, use `find-tools.py` (see
`{ROOT}/07-Scripts/find-tools.py`). The CLI accepts each of these
facets as flags.

For canonical enumerated values, see
`{ROOT}/08-Schema/facet-enums.md`. Tool entries must use the exact
strings from that file; OOV values fail validation.

For the schema source itself, see
`{ROOT}/08-Schema/Master_Schema.yaml`. Bump the version when adding
new facets or values.
