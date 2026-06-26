---
Item_ID: tt-regression-discontinuity-design
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Regression Discontinuity Design (RDD)'
tt_Source: 'Thistlethwaite, D. & Campbell, D. (1960); Imbens, G. & Lemieux, T. (2008) Journal of Econometrics.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Run experimental cycle'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Sequenced workflow
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
  - Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Difference-in-Differences
  - Instrumental Variables
  - Propensity Score Matching
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
Quick_Notes: 'Exploit sharp threshold-based treatment assignment — observations just above and just below the threshold serve as natural treatment/control groups.'
Needs_Processing: false
AI_Instructions: ""
---

# Regression Discontinuity Design (RDD)

**One-line summary:** Exploit sharp threshold-based treatment assignment — observations just above and just below the threshold serve as natural treatment/control groups.

**When to reach for it:** Policy evaluation with eligibility cutoffs (test-score thresholds, income thresholds, age thresholds, regulatory thresholds); program impact estimation with assignment rules.

## Purpose

When a treatment is assigned based on whether a continuous score crosses a threshold (test score, age, income), observations just above and just below the threshold are similar in everything except treatment. The discontinuity in outcome at the threshold identifies the causal effect at that threshold. RDD is widely considered one of the most credible quasi-experimental methods because the identification strategy is transparent and the assumptions are testable.

## How To Use

1) Identify the assignment rule and the threshold. 2) Plot the outcome against the running variable. 3) Look for a discontinuity at the threshold. 4) Fit smooth regressions on either side. 5) The estimated jump at the threshold is the causal effect at that point. 6) Robustness checks: bandwidth sensitivity, manipulation test (McCrary), placebo thresholds.

## Sources

- Thistlethwaite & Campbell 1960.
- Imbens & Lemieux 2008.
