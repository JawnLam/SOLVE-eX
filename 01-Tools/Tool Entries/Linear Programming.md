---
Item_ID: tt-linear-programming
Item_Prototype: Thinking_Tool
Title: 'Linear Programming (Dantzig Simplex)'
tt_Source: 'Dantzig, G.B. (1947) simplex algorithm; Hillier-Lieberman Introduction to OR ch. 4.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Decision analysis'
tt_Operation: 'Score and rank options'
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
  - Industrial / business
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Decision / choice
  - Strategy / competition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Integer Programming
  - Dynamic Programming
  - Sensitivity Analysis
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
Quick_Notes: 'Optimize a linear objective subject to linear constraints — Dantzig''s simplex algorithm finds the optimum vertex of the feasible polytope.'
Needs_Processing: false
AI_Instructions: ""
---

# Linear Programming (Dantzig Simplex)

**One-line summary:** Optimize a linear objective subject to linear constraints — Dantzig's simplex algorithm finds the optimum vertex of the feasible polytope.

**When to reach for it:** Resource-allocation problems with linear structure: production planning, blending, transportation, staffing, portfolio construction; whenever a Linear Programming formulation is feasible.

## Purpose

LP solves the canonical optimization problem: max (or min) c'x subject to Ax <= b, x >= 0. When the problem fits the LP form, the simplex algorithm finds the global optimum in practical time on industrial-scale problems. Decades of OR practice have shown how to formulate many real-world allocation problems as LPs. The discipline is recognizing LP-shape problems and using off-the-shelf solvers rather than ad hoc methods.

## How To Use

1) Identify decision variables x. 2) Specify the linear objective c'x. 3) Specify linear inequality constraints Ax <= b. 4) Use a standard solver (CPLEX, Gurobi, OR-Tools). 5) Read the optimal x* and the dual variables. 6) Validate against intuitive expectations.

## Sources

- Hillier & Lieberman Introduction to Operations Research ch. 4.
