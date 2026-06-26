---
Item_ID: tt-mutual-information
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Mutual Information / Information Gain'
tt_Source: 'Shannon, C.E. (1948); Cover, T. & Thomas, J. (2006) Elements of Information Theory ch. 2.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Quantitative & probabilistic reasoning'
tt_Operation: 'Score and rank options'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
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
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Shannon Entropy
  - KL Divergence
  - Decision Trees
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
Quick_Notes: 'How much knowing one variable reduces uncertainty about another — I(X;Y) = H(X) - H(X|Y), in bits.'
Needs_Processing: false
AI_Instructions: ""
---

# Mutual Information / Information Gain

**One-line summary:** How much knowing one variable reduces uncertainty about another — I(X;Y) = H(X) - H(X|Y), in bits.

**When to reach for it:** Feature selection in ML; measuring dependence between variables (non-linear dependence detection); decision-tree splits (information gain); evaluating predictive content.

## Purpose

Mutual information quantifies the reduction in uncertainty about X gained from knowing Y. Unlike correlation, it captures non-linear dependence and works for arbitrary distributions. Information gain (a specific use of mutual information) is the basis for decision-tree split criteria. The measure is symmetric: I(X;Y) = I(Y;X). Higher mutual information indicates stronger statistical dependence.

## How To Use

1) Estimate the joint distribution p(x,y) and marginals p(x), p(y). 2) Compute I(X;Y) = sum over x,y of p(x,y) * log_2(p(x,y) / (p(x)*p(y))). 3) Higher values indicate stronger dependence. 4) Use to rank features by predictive value, or as a non-parametric dependence test.

## Sources

- Cover & Thomas 2006 ch. 2.
