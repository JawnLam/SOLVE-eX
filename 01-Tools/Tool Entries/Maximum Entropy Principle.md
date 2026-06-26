---
Item_ID: tt-maximum-entropy-principle
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Maximum Entropy Principle (Jaynes)'
tt_Source: 'Jaynes, E.T. (1957) Physical Review.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Calibration & epistemic humility'
tt_Operation: 'Calibrate confidence'
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
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Shannon Entropy
  - Bayesian Updating
  - Probabilistic Thinking
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
Quick_Notes: 'Given partial information, the prior distribution should maximize Shannon entropy subject to the known constraints — the least-biased prior consistent with what we know.'
Needs_Processing: false
AI_Instructions: ""
---

# Maximum Entropy Principle (Jaynes)

**One-line summary:** Given partial information, the prior distribution should maximize Shannon entropy subject to the known constraints — the least-biased prior consistent with what we know.

**When to reach for it:** Choosing priors in Bayesian analysis; statistical mechanics; natural language modeling; any context requiring a 'maximally uncertain' distribution consistent with known constraints.

## Purpose

Jaynes argued that the prior distribution should encode all the information we have and no more. Maximum entropy formalizes this: among all distributions satisfying known constraints (moments, mean values, etc.), choose the one with maximum entropy. The result is the least-committal distribution — anything else implicitly assumes information we don't have. Famous applications: Gaussian as max-entropy given mean and variance; Boltzmann distribution as max-entropy given energy constraint.

## How To Use

1) State known constraints on the distribution (often expressed as moment conditions). 2) Solve the constrained optimization: maximize H(p) subject to the constraints. 3) The Lagrangian method yields exponential-family solutions for standard moment constraints. 4) Use the resulting distribution as prior or model.

## Sources

- Jaynes 1957 Physical Review.
