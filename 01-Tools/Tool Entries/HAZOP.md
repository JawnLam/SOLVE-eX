---
Item_ID: tt-hazop
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: HAZOP (Hazard and Operability Study)
tt_Source: "Kletz, T. (1999). HAZOP and HAZAN: Identifying and Assessing Process Industry Hazards (4th ed.). IChemE."
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Engineering / design reasoning
tt_Operation: Stress-test a position
tt_Cross_Domains: []
tt_Form:
  - Matrix
  - Sequenced workflow
tt_Scale:
  - Small group
  - Organizational
tt_Duration:
  - Workshop
  - Project
tt_Lineage:
  - Industrial / business
  - Scientific method
tt_Posture:
  - Expert-required
  - Adversarial-tolerant
tt_State: []
tt_Agent:
  - Human group
tt_About:
  - Risk / uncertainty
  - Group / organization
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With: []
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-12 — initial classification (Sprint 03 — Deep-Gap Backfill Card 09)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Process-industry hazard analysis applying guide words (No, More, Less, As well as, Part of, Reverse, Other than) to each parameter (Flow, Pressure, Temperature) at each node to generate deviation hypotheses."
Needs_Processing: false
AI_Instructions: ""
---

# HAZOP (Hazard and Operability Study)

**One-line summary:** Process-industry hazard analysis applying guide words (No, More, Less, As well as, Part of, Reverse, Other than) to each parameter (Flow, Pressure, Temperature) at each node to generate deviation hypotheses.

**When to reach for it:** Designing or auditing a process plant (chemical, pharmaceutical, refinery, food production) where systematic enumeration of process deviations and their consequences is required for safety and operability.

## Purpose

HAZOP (Hazard and Operability Study) is a process-industry hazard-analysis method developed by ICI in the 1960s, codified by Trevor Kletz. The systematic application of 'guide words' (No, More, Less, As well as, Part of, Reverse, Other than) to each parameter (Flow, Pressure, Temperature, Level, Composition, etc.) at each node in a process plant. Each guide-word/parameter combination generates a 'deviation' hypothesis (No Flow, More Pressure, Reverse Flow, Other Composition). The team then evaluates: what causes this deviation? What are the consequences? What safeguards exist? What additional safeguards are needed? The systematic application ensures that obvious failure modes are not missed and that less-obvious ones are surfaced.

## How To Use

Assemble a multidisciplinary team: process engineer (chair), operators, safety engineer, instrument engineer, etc. Use a P&ID (piping and instrumentation diagram) marked into 'nodes' (sections of process between major equipment changes). For each node: identify the relevant parameters (Flow, Pressure, Temperature, Level, Composition). For each parameter: apply each guide word systematically. 'No Flow' — what causes it (pump failure, valve closed, blockage)? Consequences (loss of cooling, overheating, vessel rupture)? Safeguards (interlocks, alarms, relief valves)? Recommendations (additional safeguards, design changes). Record in a HAZOP worksheet. Move to the next parameter, then the next node. Comprehensive HAZOP of a complex plant takes weeks; the discipline is the systematic guide-word application.

## Sources

- Kletz, T. (1999). *HAZOP and HAZAN: Identifying and Assessing Process Industry Hazards* (4th ed.). IChemE.
- Crawley, F., & Tyler, B. (2015). *HAZOP: Guide to Best Practice* (3rd ed.). IChemE.
- ICI Engineering procedures (1970s, classified at the time).
