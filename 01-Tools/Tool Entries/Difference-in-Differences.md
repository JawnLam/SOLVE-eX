---
Item_ID: tt-difference-in-differences
Item_Prototype: Thinking_Tool
Title: 'Difference-in-Differences (DiD)'
tt_Source: 'Card, D. & Krueger, A. (1994) American Economic Review; Angrist, J. & Pischke, J. (2009) Mostly Harmless Econometrics.'
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
  - Time / future
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Regression Discontinuity Design
  - Synthetic Control Method
  - Propensity Score Matching
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
Quick_Notes: 'Compare the before/after change in a treated group to the before/after change in an untreated control group — subtracts out time trends and group differences.'
Needs_Processing: false
AI_Instructions: ""
---

# Difference-in-Differences (DiD)

**One-line summary:** Compare the before/after change in a treated group to the before/after change in an untreated control group — subtracts out time trends and group differences.

**When to reach for it:** Policy evaluation where treatment is rolled out to some units but not others; natural experiments with a clear timing of policy change; minimum-wage and similar labor-market analyses.

## Purpose

DiD identifies causal effects under the parallel-trends assumption: treated and control groups would have evolved similarly absent the treatment. Pre/post comparison within the treated group conflates treatment effect with time trend; cross-group comparison at one point conflates with permanent group differences. The double difference (treated post - treated pre) - (control post - control pre) removes both. The method is workhorse-grade for policy evaluation when randomized experiments aren't feasible.

## How To Use

1) Identify treated units, control units, and the timing of treatment. 2) Compute pre/post change for treated. 3) Compute pre/post change for control. 4) DiD estimate = (treated change) - (control change). 5) Implement as regression with unit and time fixed effects + interaction. 6) Test the parallel-trends assumption with pre-period data.

## Sources

- Card & Krueger 1994.
- Angrist & Pischke 2009 Mostly Harmless Econometrics.
