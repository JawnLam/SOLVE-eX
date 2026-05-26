---
Item_ID: tt-saturation-sweep
Item_Prototype: Thinking_Tool
Title: 'Saturation Sweep (Five-Gate Schema Design)'
tt_Source: 'Original to SOLVE eX Thinking Tools project, 2026-05-09 (see Archive/Saturation Sweep.md). Synthesizes Ranganathan (1933) faceted classification principles, Glaser & Strauss (1967) theoretical saturation, and Cooper (1986) Stage-Gate quality engineering.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Memory & knowledge architecture'
tt_Operation: 'Structure problem space across aspects'
tt_Cross_Domains:
  - Discursive-analytical
tt_Form:
  - Sequenced workflow
  - Checklist
  - Decision tree
tt_Scale:
  - Solo
  - Small group
  - Organizational
tt_Duration:
  - Project
tt_Lineage:
  - Scientific method
  - Western analytic / academic
  - Industrial / business
tt_Posture:
  - Expert-required
  - Collaborative-willing
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Mind / cognition
  - Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
  - Morphological Analysis
  - Pairwise t-way Combinatorial Testing
  - Coherence-Filtered Gap Categorization
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Morphological Analysis
  - Pairwise t-way Combinatorial Testing
  - Theoretical Saturation
  - Coherence-Filtered Gap Categorization
  - Construct Validity Frameworks
  - Formal Concept Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - '2026-05-12 — initial classification (ad-hoc post-Sprint 04 addition; promoted from Archive/Saturation Sweep.md after recognition that the 5-gate methodology used to design schema v1.13.0 is itself a transferable thinking tool)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Five-gate methodology for designing a saturated faceted classification before population — Ontology lock, Per-layer artifacts, Three saturation tests, External corpus test, Decision Log, Final review — that exits with high confidence the schema will not need re-work later.'
Needs_Processing: false
AI_Instructions: ""
---

# Saturation Sweep (Five-Gate Schema Design)

**One-line summary:** A five-gate methodology for designing a saturated faceted classification (taxonomy, ontology, schema) *before* it is populated, producing high confidence that the structure will not need re-work later.

**When to reach for it:** You are designing a faceted classification system (a library taxonomy, a product taxonomy, a research ontology, a controlled vocabulary, a workflow schema) and you want to lock the structure once rather than re-litigate it as the corpus grows. Especially apt when the classification will be used by multiple parties (humans + AI; users + curators; multiple teams) for whom mutual-exclusivity at every layer matters.

## Purpose

Most classification systems drift through endless schema revisions because their initial design was aesthetic rather than methodologically validated. The Saturation Sweep imposes empirical discipline on schema design: every layer must pass three saturation tests (mutual exclusivity, joint exhaustiveness, population stress) before population begins, and the whole system must pass an external corpus test against lists it was not designed around.

The methodology operationalizes a north-star principle: *done = a future-us in N years who picks this up does not need to re-open the schema.* The price is going slowly upfront. The payoff is that the schema does not need to evolve under load — only the population does. The Sweep distinguishes:

- **Internal saturation** (the schema is internally consistent) — caught by Gates 1-2 + 4-5
- **External saturation** (the schema accommodates the actual world) — caught by Gate 3
- **Decision saturation** (every non-obvious choice has captured rationale) — caught by Gate 4

A schema that passes all three is considered locked. Subsequent work populates the schema; it does not redesign it. (Note: this is distinct from corpus saturation — the question of whether enough *entries* have been collected — which is the job of Theoretical Saturation, Pairwise t-way Combinatorial Testing, and Coherence-Filtered Gap Categorization.)

## How To Use

The methodology walks five gates in sequence. No gate proceeds until the prior is fully cleared.

**Gate 0 — Ontology lock (top layer only, one-time).** Decide what *kind* of thing the top layer is. Single-axis (one organizing question) or mixed-axis (convenience grouping). Everything below inherits this answer. Document the choice and its rationale.

**Gate 1 — Four artifacts per layer (written *before* population).** For each hierarchy layer and each facet, lock four artifacts in writing:
  1. **Layer question** — the single question this layer answers.
  2. **Inclusion criteria** — what makes a value belong at this layer.
  3. **Exclusion criteria** — what disqualifies a candidate.
  4. **Granularity rule** — the test for "too coarse" and "too fine."

The discipline of writing these *before* values are listed surfaces ontological confusion early.

**Gate 2 — Three saturation tests per layer.** For each layer's value inventory, run:

| Test                  | Catches                                                                             |
| --------------------- | ----------------------------------------------------------------------------------- |
| Mutual exclusivity    | Fake boundaries between values (a tool that fits in two equally)                   |
| Joint exhaustiveness  | Coverage gaps (a tool that fits in none without torture)                            |
| Population stress     | Vanity categories — every value needs ≥3 real tools, or a documented rare-slot exception |

Iterate the inventory until all three pass.

**Gate 3 — External corpus test (system-level, after every layer passes internally).** Run the saturated schema against ≥6 published lists that the design did not anticipate. *Pass condition: every item finds exactly one canonical Domain + Field, with no torture.* If a gap is caught, fix the schema and re-run. The external corpus test is the construct-validity check (Cronbach & Meehl 1955; Campbell & Fiske 1959): a schema that passes only its designer's tests is method-bound; external triangulation breaks the bind.

**Gate 4 — Decision Log every non-obvious choice.** Log decisions at the moment of decision, not after. The act of writing the rationale frequently reveals the choice was wrong; pre-decision logging surfaces these reversals while they are still cheap.

**Gate 5 — Final saturation review checklist.** Confirm in writing:
  - [ ] Ontology lock from Gate 0 honored throughout
  - [ ] Every layer has its four artifacts (Gate 1)
  - [ ] All three saturation tests pass per layer (Gate 2)
  - [ ] External corpus test passed (Gate 3): ≥6 lists, 100% placement, zero torture
  - [ ] No layer has unjustified rare slots
  - [ ] Facet independence checked (the facets are not collinear)
  - [ ] Decision Log captures rationale for every non-obvious choice (Gate 4)

If any box is unchecked, the schema is not yet saturated.

The methodology was first applied to the SOLVE eX Thinking Tools schema v1.13.0 (2026-05-09) and exited with a saturated 12-Domain / 112-Field / 36-Operation / 9-facet structure that subsequently absorbed +417 entries across three sprints (294 → 676) with **zero schema regressions** — empirical validation that pre-population saturation discipline holds up under sustained load.

## Sources

- Original to SOLVE eX Thinking Tools project, 2026-05-09. Full methodology and worked example preserved at `Archive/Saturation Sweep.md` in the same project.
- Synthesizes: Ranganathan, S. R. (1933). *Colon Classification* — faceted classification principles.
- Synthesizes: Glaser, B. G. & Strauss, A. L. (1967). *The Discovery of Grounded Theory* — theoretical saturation as stopping criterion.
- Synthesizes: Cooper, R. G. (1986). *Winning at New Products* — Stage-Gate quality engineering.
- Compatible with: Zwicky, F. (1969). *Discovery, Invention, Research Through the Morphological Approach* — Morphological Analysis is the design-output that this methodology produces; Saturation Sweep is the methodology that produces it.
- Construct-validity grounding: Cronbach, L. J., & Meehl, P. E. (1955). 'Construct Validity in Psychological Tests.' *Psychological Bulletin*. Campbell, D. T., & Fiske, D. W. (1959). 'Convergent and discriminant validation by the multitrait-multimethod matrix.' *Psychological Bulletin* 56. — Gate 3 is the multimethod portion of MTMM applied to schema validation.
