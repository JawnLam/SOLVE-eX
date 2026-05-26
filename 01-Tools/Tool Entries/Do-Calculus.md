---
Item_ID: tt-do-calculus
Item_Prototype: Thinking_Tool
Title: 'Do-Calculus (Pearl)'
tt_Source: 'Pearl, J. (1995) Biometrika; Pearl, J. (2009) Causality (2nd ed.).'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Derive via formal rules'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Solo
tt_Duration:
  - Project
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
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Causal DAGs
  - Backdoor Criterion
  - Frontdoor Criterion
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
Quick_Notes: 'Pearl''s formal calculus of three rules that derive the causal effect of an intervention from observational data, given a causal DAG.'
Needs_Processing: false
AI_Instructions: ""
---

# Do-Calculus (Pearl)

**One-line summary:** Pearl's formal calculus of three rules that derive the causal effect of an intervention from observational data, given a causal DAG.

**When to reach for it:** Estimating causal effects from observational data with a credible causal model; teaching what does and doesn't license causal inference; identifying when randomization is and isn't needed.

## Purpose

Do-calculus provides three syntactic rules that operate on a causal DAG plus observational distribution to determine which causal effects are identifiable (computable from the data) and which require additional assumptions or experiments. The rules formalize what statisticians had done informally for decades and clarify the exact conditions under which observational data licenses causal conclusions. The framework underlies modern causal-inference machinery (front-door, back-door, instrumental variables, etc.).

## How To Use

1) Draw the causal DAG (which variables cause which). 2) State the target causal query (e.g., P(Y | do(X))). 3) Apply Rule 1 (insertion/deletion of observations), Rule 2 (action/observation exchange), and Rule 3 (insertion/deletion of actions) repeatedly. 4) If the do-operator can be eliminated, the effect is identifiable from observational data. 5) Estimate accordingly.

## Sources

- Pearl 1995.
- Pearl 2009 Causality (2nd ed.).
