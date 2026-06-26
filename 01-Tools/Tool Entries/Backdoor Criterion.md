---
Item_ID: tt-backdoor-criterion
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Backdoor Criterion (Pearl)'
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
  - Frontdoor Criterion
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 05)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Identify a set of variables that, when conditioned on, blocks all back-door (confounding) paths between treatment and outcome — the most-used identification rule in causal inference.'
Needs_Processing: false
AI_Instructions: ""
---

# Backdoor Criterion (Pearl)

**One-line summary:** Identify a set of variables that, when conditioned on, blocks all back-door (confounding) paths between treatment and outcome — the most-used identification rule in causal inference.

**When to reach for it:** Observational studies where confounding bias is suspected; deciding which covariates to adjust for in a regression; evaluating whether a study's identification strategy is credible.

## Purpose

The backdoor criterion is the most-used special case of Pearl's do-calculus: if you can find a set Z of variables that (a) blocks every path from treatment to outcome that starts with an arrow into the treatment, and (b) contains no descendants of the treatment, then conditioning on Z identifies the causal effect. The rule formalizes 'controlling for confounders' and provides a precise graphical criterion for which controls are sufficient and which over-adjust.

## How To Use

1) Draw the causal DAG. 2) Identify the treatment T and outcome Y. 3) List all back-door paths from T to Y (paths starting with an arrow into T). 4) Find a set Z that blocks all such paths and contains no descendants of T. 5) Conditioning on Z gives an unbiased estimate of T's effect on Y. 6) If no such Z exists, the backdoor criterion fails; try the frontdoor criterion or instrumental variables.

## Sources

- Pearl 2009 Causality ch. 3.
