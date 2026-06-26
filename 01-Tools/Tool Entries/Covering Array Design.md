---
Item_ID: tt-covering-array-design
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Covering Array Design'
tt_Source: 'Bose & Bush (1952); Hartman 2005 Software and Hardware Testing Using Combinatorial Covering Suites.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Decompose hierarchically'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Matrix
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
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Pairwise t-way Combinatorial Testing
  - Latin Square Design
  - Design of Experiments
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 03)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Mathematical objects that systematically sample a parameter space such that every t-way value combination appears at least once.'
Needs_Processing: false
AI_Instructions: ""
---

# Covering Array Design

**One-line summary:** Mathematical objects that systematically sample a parameter space such that every t-way value combination appears at least once.

**When to reach for it:** Design of efficient experiments; testing matrix design; survey design where every category-pair must be sampled.

## Purpose

Covering arrays are the combinatorial structures behind t-way testing and similar sampling problems. The design question is: given k factors each with v values, what is the smallest array that covers every t-way combination? Optimal covering arrays are known for small cases; for large cases, greedy or metaheuristic algorithms produce near-optimal arrays. The math is the underpinning; the discipline is using existing solvers rather than rolling your own.

## How To Use

1) Specify factors (k), values per factor (v), and coverage level (t). 2) Use a covering-array tool (ACTS, PICT, allpairs) to generate the array. 3) Each row of the array is one test/experimental condition. 4) Execute. 5) Verify coverage in the realized data.

## Sources

- Bose & Bush 1952.
- Hartman 2005.
