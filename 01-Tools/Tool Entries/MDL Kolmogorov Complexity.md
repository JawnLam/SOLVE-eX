---
Item_ID: tt-mdl-kolmogorov-complexity
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'MDL / Kolmogorov Complexity Reasoning'
tt_Source: 'Solomonoff, R.J. (1964); Kolmogorov, A.N. (1965); Rissanen, J. (1978).'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Quantitative & probabilistic reasoning'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Heuristic
  - Mental model
tt_Scale:
  - Solo
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Occams Razor
  - Popper Falsifiability
  - Bayesian Updating
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 06)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'The complexity of a string is the length of the shortest program producing it; Minimum Description Length is the practical model-selection corollary — prefer the model with shortest combined description of model + data given model.'
Needs_Processing: false
AI_Instructions: ""
---

# MDL / Kolmogorov Complexity Reasoning

**One-line summary:** The complexity of a string is the length of the shortest program producing it; Minimum Description Length is the practical model-selection corollary — prefer the model with shortest combined description of model + data given model.

**When to reach for it:** Model selection in ML; hypothesis comparison in science; formalizing Occam's Razor; compression-based reasoning about regularities.

## Purpose

Kolmogorov complexity is the formal measure of an object's algorithmic information content. While the underlying complexity is uncomputable, the MDL principle uses approximations to choose models: the best model is the one that compresses the data most. The framework formalizes Occam's razor: a model that compresses data well is preferred because the combined model+data description is shortest. MDL provides a unified framework for statistical inference across diverse model classes.

## How To Use

1) Specify candidate models and their description lengths L(M). 2) For each, compute the length needed to encode data given model L(D|M). 3) Choose the model minimizing L(M) + L(D|M). 4) The shortest total description balances model complexity against fit. 5) Approximations: BIC, AIC, MDL family.

## Sources

- Solomonoff 1964.
- Kolmogorov 1965.
- Rissanen 1978.
