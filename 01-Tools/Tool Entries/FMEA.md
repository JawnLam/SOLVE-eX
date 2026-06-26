---
Item_ID: tt-fmea
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: FMEA (Failure Mode and Effects Analysis)
tt_Source: "McDermott, R. E., et al. (2009). The Basics of FMEA (2nd ed.). Productivity Press."
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Engineering / design reasoning
tt_Operation: Score and rank options
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
  - Collaborative-willing
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
Quick_Notes: "Risk-engineering method — systematically enumerate component failure modes, score Severity, Occurrence, Detection; multiply for Risk Priority Number; prioritize mitigation against high-RPN items."
Needs_Processing: false
AI_Instructions: ""
---

# FMEA (Failure Mode and Effects Analysis)

**One-line summary:** Risk-engineering method — systematically enumerate component failure modes, score Severity, Occurrence, Detection; multiply for Risk Priority Number; prioritize mitigation against high-RPN items.

**When to reach for it:** Designing or auditing a safety-critical engineering system where systematic enumeration of failure modes and risk-prioritized mitigation is required, and ad-hoc risk imagination would miss critical failure paths.

## Purpose

FMEA (Failure Mode and Effects Analysis) is a risk-engineering method originated in 1940s US military and aerospace (MIL-P-1629, 1949), now ubiquitous in safety-critical engineering. For each component or process step: (1) Identify possible failure modes; (2) For each failure mode, identify effects (what happens if this fails?); (3) Score Severity (1-10, how bad if the failure occurs); (4) Score Occurrence (1-10, how often is it expected); (5) Score Detection (1-10 inverted, how likely is the failure to be detected before consequence); (6) Multiply S × O × D = Risk Priority Number (RPN); (7) Rank failure modes by RPN and prioritize mitigation for highest. The discipline produces a comprehensive risk register tied to specific mitigations.

## How To Use

Assemble a cross-functional team (design, manufacturing, quality, often customer-facing). Decompose the system or process into components or steps. For each: brainstorm possible failure modes. For each failure mode: identify effects on the rest of the system and on the end-user. Score Severity (1-10), Occurrence (1-10), Detection (1-10 where 10 = unlikely to be detected). Compute RPN = S × O × D. Sort the FMEA table by RPN descending. Address highest-RPN items: can severity be reduced (design change)? Can occurrence be reduced (process improvement)? Can detection be improved (better testing, monitoring)? Re-score after mitigation. Iterate until residual RPN is acceptable. FMEA documents are living documents updated through the product/process lifecycle.

## Sources

- MIL-P-1629 (1949). Procedures for Performing a Failure Mode, Effects, and Criticality Analysis.
- McDermott, R. E., et al. (2009). *The Basics of FMEA* (2nd ed.). Productivity Press.
- AIAG-VDA FMEA Handbook (2019).
