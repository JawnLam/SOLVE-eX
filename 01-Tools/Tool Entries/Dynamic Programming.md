---
Item_ID: tt-dynamic-programming
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Dynamic Programming (Bellman)'
tt_Source: 'Bellman, R. (1957) Dynamic Programming.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Decision analysis'
tt_Operation: 'Decompose hierarchically'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Solo
tt_Duration:
  - Project
tt_Lineage:
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Decision / choice
  - Time / future
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Markov Decision Process
  - Backward Induction
  - Linear Programming
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
Quick_Notes: 'Solve multi-stage optimization by working backward from the terminal state, building optimal sub-problem solutions and combining via the Bellman equation.'
Needs_Processing: false
AI_Instructions: ""
---

# Dynamic Programming (Bellman)

**One-line summary:** Solve multi-stage optimization by working backward from the terminal state, building optimal sub-problem solutions and combining via the Bellman equation.

**When to reach for it:** Sequential decision problems with overlapping sub-problems: shortest-path, scheduling, resource-allocation-over-time, optimal control, RL value-iteration.

## Purpose

When a problem decomposes into stages and the optimal solution at each stage depends only on the current state (Markov property), Dynamic Programming exploits the structure: compute optimal value at the terminal state, work backward, at each step combining the immediate cost with the previously-computed optimal continuation. The technique trades memory for computation and turns exponential brute-force into polynomial-time recursive solutions for many problems.

## How To Use

1) Decompose into stages. 2) Define state, action, transition, and reward at each stage. 3) Write the Bellman equation: V(s) = max_a [r(s,a) + gamma * E V(s')]. 4) Solve backward from the terminal stage. 5) The optimal policy is extracted from the value function.

## Sources

- Bellman, R. (1957) Dynamic Programming.
