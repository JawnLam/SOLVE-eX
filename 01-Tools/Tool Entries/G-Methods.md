---
Item_ID: tt-g-methods
Item_Prototype: Thinking_Tool
Title: 'G-Methods / G-Computation (Robins)'
tt_Source: 'Robins, J. (1986) Mathematical Modelling; Hernán, M. & Robins, J. (2020) Causal Inference: What If.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Project alternative futures'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Organizational
tt_Duration:
  - Project
tt_Lineage:
  - Scientific method
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Time / future
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [2, 4]
tt_SOLVE_eX_Step: [2.1, 4.1]
tt_Clarifies: ['Destination', 'Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Backdoor Criterion
  - Do-Calculus
  - Mediation Analysis
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
Quick_Notes: 'A family of methods (g-formula, marginal structural models, structural nested models) for estimating causal effects of time-varying treatments under treatment-confounder feedback.'
Needs_Processing: false
AI_Instructions: ""
---

# G-Methods / G-Computation (Robins)

**One-line summary:** A family of methods (g-formula, marginal structural models, structural nested models) for estimating causal effects of time-varying treatments under treatment-confounder feedback.

**When to reach for it:** Longitudinal studies with time-varying treatment, time-varying confounders, and confounder-treatment feedback (treatment affects later confounder values); HIV-treatment optimization, multi-stage policy effects.

## Purpose

Standard regression adjustment fails when treatment affects time-varying confounders that affect later treatment and outcome — the confounder is both a confounder and a mediator. Robins's g-methods solve the problem: the g-formula (standardization across time-varying confounder distributions), IPTW (inverse probability of treatment weighting), and g-estimation (structural nested models) each handle different aspects. The framework is the canonical solution for longitudinal causal inference.

## How To Use

1) Identify time-varying treatment and time-varying confounders. 2) Test for treatment-confounder feedback. 3) If present, choose g-method: g-formula (parametric standardization), MSM with IPTW (weight pseudo-population), or g-estimation. 4) Implement using R packages (ipw, gfoRmula). 5) Sensitivity analysis for unmeasured time-varying confounding.

## Sources

- Robins 1986 Mathematical Modelling.
- Hernán & Robins 2020 Causal Inference: What If.
