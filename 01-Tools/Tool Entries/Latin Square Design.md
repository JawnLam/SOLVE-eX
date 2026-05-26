---
Item_ID: tt-latin-square-design
Item_Prototype: Thinking_Tool
Title: 'Latin Square Design'
tt_Source: 'Fisher, R.A. (1926) Arrangement of field experiments. Journal of the Ministry of Agriculture.'
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
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Design of Experiments
  - Fractional Factorial Design
  - Covering Array Design
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 03)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'An n x n grid where each treatment appears exactly once per row and per column — controls for two blocking factors with one treatment.'
Needs_Processing: false
AI_Instructions: ""
---

# Latin Square Design

**One-line summary:** An n x n grid where each treatment appears exactly once per row and per column — controls for two blocking factors with one treatment.

**When to reach for it:** Agricultural and clinical experiments with two known nuisance variables (rows = field positions, columns = times of day, treatments = fertilizers); efficiency-focused designs.

## Purpose

When you have one treatment factor and two known sources of nuisance variation, a Latin Square uses one observation per (row, column) combination but ensures every treatment appears equally in every row and column. This blocks out both nuisance variables with fewer observations than a full factorial would require. The design assumes no interaction between blocking factors and treatment.

## How To Use

1) Identify treatment factor and two blocking factors. 2) Choose grid size n equal to number of treatment levels. 3) Construct the Latin Square (standard or randomized). 4) Assign treatments per the square. 5) Run experiment. 6) Analyze with the appropriate ANOVA.

## Sources

- Fisher, R.A. (1926).
