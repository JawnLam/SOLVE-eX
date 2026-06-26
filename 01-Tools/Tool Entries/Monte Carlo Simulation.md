---
Item_ID: tt-monte-carlo-simulation
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Monte Carlo Simulation'
tt_Source: 'Metropolis, N. & Ulam, S. (1949) The Monte Carlo Method.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Run experimental cycle'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Solo
  - Organizational
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
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Sensitivity Analysis
  - Bayesian Updating
  - Synthetic Control Method
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
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
Quick_Notes: 'Estimate the distribution of an outcome by sampling input distributions repeatedly and aggregating the resulting outputs.'
Needs_Processing: false
AI_Instructions: ""
---

# Monte Carlo Simulation

**One-line summary:** Estimate the distribution of an outcome by sampling input distributions repeatedly and aggregating the resulting outputs.

**When to reach for it:** Risk modeling, financial pricing, engineering tolerance analysis, project schedule estimation, anywhere analytic solutions are infeasible but sampling is.

## Purpose

Many real-world systems have stochastic inputs whose distributions are estimable but whose closed-form output distributions are intractable. Monte Carlo sampling — draw random inputs, evaluate the system, record the output — converges to the true output distribution as sample size grows. The method is universal: it requires only the ability to simulate one realization. The cost is computational; modern hardware makes large-N Monte Carlo cheap.

## How To Use

1) Identify the stochastic inputs and their distributions. 2) Identify the deterministic computation that maps inputs to outputs. 3) Sample inputs N times (typically 10,000-100,000). 4) Evaluate the output for each sample. 5) Aggregate: histogram, percentiles, tail probabilities. 6) Verify N is large enough by checking estimator stability.

## Sources

- Metropolis & Ulam 1949.
