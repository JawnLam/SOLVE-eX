---
Item_ID: tt-propensity-score-matching
Item_Prototype: Thinking_Tool
Title: 'Propensity Score Matching'
tt_Source: 'Rosenbaum, P. & Rubin, D. (1983) Biometrika.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Compare against paradigm case'
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
  - Mind / cognition
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Difference-in-Differences
  - Regression Discontinuity Design
  - Instrumental Variables
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
Quick_Notes: 'Match treated units to similar control units on the probability of treatment given covariates — approximates randomization conditional on observed covariates.'
Needs_Processing: false
AI_Instructions: ""
---

# Propensity Score Matching

**One-line summary:** Match treated units to similar control units on the probability of treatment given covariates — approximates randomization conditional on observed covariates.

**When to reach for it:** Observational data where direct regression adjustment is imprecise due to non-overlapping covariate distributions; treatment-effect estimation in retrospective studies.

## Purpose

Direct regression adjustment can extrapolate outside the support of the data; matching restricts comparison to units with similar covariate profiles. Rosenbaum and Rubin showed that matching on the propensity score (probability of treatment given covariates) is sufficient to balance all observed covariates. The procedure approximates conditional randomization. Limitations: matching only on observed covariates, sensitive to model specification, doesn't address unmeasured confounding.

## How To Use

1) Estimate the propensity score (logistic regression or ML model). 2) Match each treated unit to one or more controls with similar propensity scores (nearest-neighbor, caliper, kernel). 3) Verify covariate balance in the matched sample. 4) Estimate the treatment effect on the matched sample. 5) Sensitivity analysis (Rosenbaum bounds) for unobserved confounding.

## Sources

- Rosenbaum & Rubin 1983 Biometrika.
