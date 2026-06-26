---
Item_ID: tt-mediation-analysis
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Mediation Analysis (Baron-Kenny, Imai-Keele-Yamamoto)'
tt_Source: 'Baron, R. & Kenny, D. (1986) JPSP; Imai, K., Keele, L. & Yamamoto, T. (2010).'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Decompose hierarchically'
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
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Frontdoor Criterion
  - Causal DAGs
  - Do-Calculus
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
Quick_Notes: 'Decompose the causal effect of treatment on outcome into a direct effect and an indirect effect operating through one or more mediators.'
Needs_Processing: false
AI_Instructions: ""
---

# Mediation Analysis (Baron-Kenny, Imai-Keele-Yamamoto)

**One-line summary:** Decompose the causal effect of treatment on outcome into a direct effect and an indirect effect operating through one or more mediators.

**When to reach for it:** Understanding the mechanism through which an intervention works; testing theoretical models that predict mediated pathways; designing interventions that target the right mediator.

## Purpose

Knowing that a treatment causes an outcome is one question; understanding the mechanism is another. Mediation analysis estimates how much of the treatment effect is direct versus operating through specific mediators. The classical Baron-Kenny approach has been refined by modern causal-mediation analysis (Imai-Keele-Yamamoto) which makes the identifying assumptions explicit. The discipline matters because intervention design depends on the mechanism, not just the total effect.

## How To Use

1) Specify the hypothesized mediator(s). 2) Estimate treatment's effect on mediator. 3) Estimate mediator's effect on outcome controlling for treatment. 4) Estimate treatment's direct effect on outcome controlling for mediator. 5) The indirect effect = (treatment-on-mediator) * (mediator-on-outcome). 6) Use sensitivity analysis for unmeasured mediator-outcome confounding.

## Sources

- Baron & Kenny 1986 JPSP.
- Imai-Keele-Yamamoto 2010.
