---
Item_ID: tt-coherence-filtered-gap-categorization
Item_Prototype: Thinking_Tool
Title: 'Coherence-Filtered Gap Categorization'
tt_Source: 'Original to SOLVE eX Thinking Tools project, 2026-05-12 (pairwise-outliers.md). Refines Zwicky, F. (1969) Discovery, Invention, Research Through the Morphological Approach.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Combinatorial / enumerative reasoning'
tt_Operation: 'Categorize situation type'
tt_Cross_Domains:
  - Discursive-analytical
tt_Form:
  - Matrix
  - Sequenced workflow
tt_Scale:
  - Solo
  - Small group
  - Organizational
tt_Duration:
  - Workshop
  - Project
tt_Lineage:
  - Scientific method
  - Western analytic / academic
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Mind / cognition
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
  - Theoretical Saturation
tt_Often_Follows:
  - Morphological Analysis
  - Pairwise t-way Combinatorial Testing
tt_Pairs_Well_With:
  - Morphological Analysis
  - Pairwise t-way Combinatorial Testing
  - Theoretical Saturation
  - Cross-Impact Analysis
  - Formal Concept Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (ad-hoc post-Sprint 04 addition; the one genuinely-original tool surfaced by the Sprint 01-04 retrospective)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Tri-modal classification of empty cells in a morphological matrix — Incoherent / Searched-Unfound / Reachable — refining Zwickys binary cross-consistency assessment to discipline research-effort allocation.'
Needs_Processing: false
AI_Instructions: ""
---

# Coherence-Filtered Gap Categorization

**One-line summary:** Tri-modal classification of empty cells in a morphological matrix — Incoherent (correct vacancy) / Searched-Unfound (legitimate gap) / Reachable (research target) — refining Zwicky's binary cross-consistency assessment.

**When to reach for it:** Any morphological / combinatorial saturation work where the matrix has many empty cells and the live question is *"which empty cells should we invest research effort in?"* — and Zwicky's binary "consistent / inconsistent" partition is too coarse to discipline that investment.

## Purpose

Zwicky's Morphological Analysis classifies cells of an n-dimensional matrix as consistent (logically possible) or inconsistent (logically impossible). This binary partition is sufficient when the goal is producing a list of valid configurations. But for **saturation auditing** of a classification system — where the matrix represents a populated library of instances and empty cells represent either correct vacancies or research gaps — the binary partition conflates two very different kinds of empty cells, and provides no language for the third.

Coherence-Filtered Gap Categorization adds the missing distinctions:

- **Category A — Conceptually Incoherent.** The (value_A × value_B) combination is internally contradictory, definitionally impossible, or schema-precluded. *Example:* `tt_Type=stance × tt_Form=anything` — stances have empty Form by schema definition. These are not gaps. They are correct vacancies. Research effort should NEVER be invested here. Document the reason once; ignore in all future audits.

- **Category B — Coherent-but-Searched-Unfound.** The combination is logically plausible. Research has been conducted at the threshold appropriate to the saturation level. No credibly-attested instance was found. *Example:* `Operation=Cultivate emotion × Lineage=Mathematical / formal` — possible in principle but the search returned no real-world tool. These are documented as legitimate outliers with the search-trace recorded, then parked. Re-open only if the saturation threshold changes or a new source surfaces.

- **Category C — Coherent-and-Reachable.** The combination is plausible AND there is reasonable expectation that real-world instances exist but have not yet been surfaced. *Example:* `Operation=Sense the body × Lineage=Indigenous` when the corpus has sampled few indigenous traditions — body-attention practices exist in many such traditions; the corpus simply hasn't reached them. These are the natural next-sprint research targets.

The tri-modal partition disciplines research-effort allocation: Category A is permanently ignored; Category B is parked with documentation; Category C absorbs the research budget. Without this filter, naive "fill all empty cells" approaches waste effort on Category A vacancies and conflate Category B's exhaustion-of-search with Category C's not-yet-tried.

## How To Use

1. Compute the empty cells of the morphological matrix (e.g., via pairwise t-way combinatorial coverage analysis).
2. For each empty cell, ask: *is the (value_A × value_B) combination internally contradictory, definitionally impossible, or schema-precluded?* If yes → **Category A.** Record the reason for the vacancy in a one-line annotation.
3. For remaining cells, ask: *has research been conducted at the threshold appropriate to the saturation level, with no credibly-attested instance found?* If yes → **Category B.** Document the search trace (what was looked for, where, what threshold), and the specific reason for non-finding.
4. Remaining cells → **Category C.** These become the research targets for the next saturation sprint. Order by expected yield-per-search-call where possible.
5. Re-run after each saturation sprint: Category A entries are unchanged; some Category C entries promote to Category B (searched, not found) or to populated cells (filled); occasionally a Category B re-opens because a new source surfaces a candidate.

The categorization output is itself an artifact — `pairwise-outliers.md` in the originating project documents 2,500+ empty cells partitioned this way.

## Sources

- Original to SOLVE eX Thinking Tools project, 2026-05-12. First documented in `pairwise-outliers.md` during Sprint 01 (Pairwise-Gap Audit Card 09) and refined across Sprints 03 + 04.
- Refines: Zwicky, F. (1969). *Discovery, Invention, Research Through the Morphological Approach*. Macmillan.
- Compatible with: Ritchey, T. (2011). *Wicked Problems – Social Messes: Decision Support Modelling with Morphological Analysis*. Springer.
- Related to (but distinct from): Theoretical Saturation (Glaser & Strauss 1967) — which is the stopping criterion; Coherence-Filtered Gap Categorization is the within-matrix research-target selector that operates while sampling continues.
