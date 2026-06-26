---
Item_ID: tt-fractional-factorial-design
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Fractional Factorial Design'
tt_Source: 'Finney 1945; Box, Hunter & Hunter (1978) Statistics for Experimenters.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Decompose hierarchically'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Matrix
tt_Scale:
  - Small group
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
  - Taguchi Orthogonal Arrays
  - Latin Square Design
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
Quick_Notes: 'Run a carefully chosen fraction of a full factorial experiment — sufficient to estimate main effects and low-order interactions at much lower cost.'
Needs_Processing: false
AI_Instructions: ""
---

# Fractional Factorial Design

**One-line summary:** Run a carefully chosen fraction of a full factorial experiment — sufficient to estimate main effects and low-order interactions at much lower cost.

**When to reach for it:** Industrial experimentation where full factorial is unaffordable but factor effects must still be estimated; screening designs to identify which factors matter before deeper study.

## Purpose

Full factorial experiments scale as 2^k or larger; fractional factorials run 2^(k-p) by aliasing higher-order interactions with main effects, accepting that you'll lose ability to distinguish them in exchange for many fewer runs. Resolution III, IV, V designs specify which interactions can be cleanly estimated. The method is the workhorse of industrial DoE where 7-15 factors must be screened on a budget.

## How To Use

1) Identify factors and their levels (typically 2 each). 2) Choose resolution based on which interactions matter. 3) Generate the fractional design using standard tables or software. 4) Execute runs. 5) Analyze main effects and confirmed-resolution interactions. 6) Follow up with focused designs on important factors.

## Sources

- Box, Hunter & Hunter 1978.
