---
Item_ID: tt-integer-programming
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Integer Programming'
tt_Source: 'Hillier & Lieberman Introduction to Operations Research ch. 12; Wolsey 1998 Integer Programming.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Decision analysis'
tt_Operation: 'Score and rank options'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Organizational
tt_Duration:
  - Project
tt_Lineage:
  - Mathematical / formal
  - Industrial / business
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Decision / choice
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Linear Programming
  - Combinatorial Enumeration
  - Mechanism Design
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
Quick_Notes: 'Linear Programming with integer (or binary) variables — handles indivisible decisions like ''open a facility yes/no'' or ''assign N workers to shift M.'''
Needs_Processing: false
AI_Instructions: ""
---

# Integer Programming

**One-line summary:** Linear Programming with integer (or binary) variables — handles indivisible decisions like 'open a facility yes/no' or 'assign N workers to shift M.'

**When to reach for it:** Discrete allocation problems: scheduling, routing, facility location, assignment, knapsack-style selection; whenever decisions are not continuously divisible.

## Purpose

Many real decisions are integer-constrained: you can't open 0.7 facilities or hire 2.3 staff. Integer Programming generalizes LP to these problems, at the cost of NP-hard complexity. Modern solvers (branch-and-bound + cutting planes) handle large practical problems efficiently. The discipline is recognizing integer-shape problems and using IP rather than rounding LP solutions (which often produces sub-optimal results).

## How To Use

1) Formulate as LP with some variables required to be integers (or binary). 2) Use an MIP solver (CPLEX, Gurobi). 3) Read the solution; check feasibility. 4) If solve time is excessive, consider Lagrangian relaxation or column generation.

## Sources

- Wolsey 1998 Integer Programming.
