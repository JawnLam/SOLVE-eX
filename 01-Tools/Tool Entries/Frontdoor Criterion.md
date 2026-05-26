---
Item_ID: tt-frontdoor-criterion
Item_Prototype: Thinking_Tool
Title: 'Frontdoor Criterion (Pearl)'
tt_Source: 'Pearl, J. (2009) Causality (2nd ed.) ch. 3.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Heuristic
tt_Scale:
  - Solo
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
  - Scientific method
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Mind / cognition
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Causal DAGs
  - Do-Calculus
  - Backdoor Criterion
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 05)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Identify a mediator that the treatment affects, the mediator affects the outcome, and no confounder affects the mediator — licenses causal identification despite unobserved treatment-outcome confounding.'
Needs_Processing: false
AI_Instructions: ""
---

# Frontdoor Criterion (Pearl)

**One-line summary:** Identify a mediator that the treatment affects, the mediator affects the outcome, and no confounder affects the mediator — licenses causal identification despite unobserved treatment-outcome confounding.

**When to reach for it:** Observational studies with unmeasured treatment-outcome confounding but a measurable mediator on the causal path; alternative to backdoor when backdoor fails.

## Purpose

When backdoor adjustment is impossible because key confounders are unmeasured, the frontdoor criterion sometimes rescues identification via a mediator. The mediator must (a) intercept all causal effect of treatment on outcome, (b) have no unblocked back-door path from treatment, and (c) have all back-door paths to outcome blocked by treatment. When the conditions hold, the causal effect is identifiable through a two-step formula involving the treatment-mediator and mediator-outcome relationships.

## How To Use

1) Draw the DAG. 2) Identify a candidate mediator M. 3) Verify (a) all treatment effect on outcome goes through M, (b) no unblocked backdoor from T to M, (c) all backdoor paths from M to Y are blocked by T. 4) If conditions hold, compute the front-door formula: sum over M of P(M|T) * sum over T' of P(Y|M, T') P(T'). 5) Use the result as the identified causal effect.

## Sources

- Pearl 2009 Causality ch. 3.
