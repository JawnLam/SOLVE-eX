---
Item_ID: tt-structural-causal-models
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Structural Causal Models (SCM)'
tt_Source: 'Pearl, J. (2009) Causality ch. 1; Pearl, J. & Mackenzie, D. (2018) The Book of Why.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Map relational topology'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Visualization technique
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
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Causal DAGs
  - Do-Calculus
  - Counterfactual Reasoning
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
Quick_Notes: 'A causal DAG augmented with structural equations specifying how each variable is generated from its parents — the full data-generating process.'
Needs_Processing: false
AI_Instructions: ""
---

# Structural Causal Models (SCM)

**One-line summary:** A causal DAG augmented with structural equations specifying how each variable is generated from its parents — the full data-generating process.

**When to reach for it:** Causal modeling beyond graph-only DAGs; counterfactual analysis requiring functional forms; mediation and effect-decomposition where the structure of the relationships matters.

## Purpose

DAGs encode the qualitative causal structure; SCMs add the functional form. With an SCM, you can answer not just associational and interventional queries (P(Y) and P(Y|do(X))) but also counterfactual queries (P(Y=y | did X=x' instead of x)). The third-rung counterfactual reasoning Pearl identifies requires the SCM's full structure. The framework is the most general causal-model representation used in machine-learning research.

## How To Use

1) Build the DAG. 2) Specify a structural equation for each variable: V = f_V(parents(V), U_V) where U_V is an exogenous error term. 3) Specify the joint distribution of U variables. 4) Apply for interventional queries (replace parent equations) or counterfactual queries (impose specific U values and replay).

## Sources

- Pearl 2009 Causality ch. 1.
- Pearl & Mackenzie 2018 The Book of Why.
