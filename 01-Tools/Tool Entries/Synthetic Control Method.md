---
Item_ID: tt-synthetic-control-method
Item_Prototype: Thinking_Tool
Title: 'Synthetic Control Method'
tt_Source: 'Abadie, A. & Gardeazabal, J. (2003) American Economic Review; Abadie, A., Diamond, A. & Hainmueller, J. (2010) JASA.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Compare against paradigm case'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Organizational
  - Civilizational
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
  - Risk / uncertainty
  - Time / future
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Difference-in-Differences
  - Regression Discontinuity Design
  - Counterfactual Reasoning
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
Quick_Notes: 'Construct a synthetic control from a weighted combination of donor units that closely matches the treated unit''s pre-treatment trajectory; compare post-treatment.'
Needs_Processing: false
AI_Instructions: ""
---

# Synthetic Control Method

**One-line summary:** Construct a synthetic control from a weighted combination of donor units that closely matches the treated unit's pre-treatment trajectory; compare post-treatment.

**When to reach for it:** Single-unit or small-N policy interventions where standard control-group methods don't apply; place-based policy evaluation; regional or national policy effects.

## Purpose

Many policy interventions affect a single unit (a state, a country, a city) and have no obvious control. Synthetic control constructs a weighted combination of similar donor units that, in the pre-period, matches the treated unit on outcome and key covariates. The post-period divergence between the treated unit and its synthetic control is the estimated effect. The method has become standard for case-study quantification in policy economics.

## How To Use

1) Identify the treated unit and donor pool. 2) Match pre-treatment outcomes and covariates by choosing donor-pool weights that minimize the pre-period gap. 3) Apply the same weights post-treatment to construct counterfactual trajectory. 4) The gap is the estimated treatment effect. 5) Placebo tests on donor units assess significance.

## Sources

- Abadie & Gardeazabal 2003.
- Abadie, Diamond & Hainmueller 2010 JASA.
