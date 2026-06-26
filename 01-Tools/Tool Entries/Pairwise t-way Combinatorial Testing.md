---
Item_ID: tt-pairwise-t-way-combinatorial-testing
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Pairwise / t-way Combinatorial Testing'
tt_Source: 'NIST SP 800-142 (Kuhn, Kacker, Lei 2010); Mandl 1985 pairwise paper.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Matrix
tt_Scale:
  - Solo
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
  - Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Covering Array Design
  - Combinatorial Enumeration
  - Morphological Analysis
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
Quick_Notes: 'Sample a large parameter space efficiently by covering every t-way interaction at least once rather than testing every combination.'
Needs_Processing: false
AI_Instructions: ""
---

# Pairwise / t-way Combinatorial Testing

**One-line summary:** Sample a large parameter space efficiently by covering every t-way interaction at least once rather than testing every combination.

**When to reach for it:** Software testing, configuration validation, design-space sampling; whenever full factorial coverage is intractable but multi-factor interactions matter.

## Purpose

Full factorial coverage grows exponentially with parameters; pairwise (t=2) and higher t-way coverage grows logarithmically. NIST research shows most software defects involve interactions of only 2-6 factors. A covering array that touches every 2-way (or 3-way, 4-way) combination catches the bulk of defects at a tiny fraction of the test cost. The discipline is choosing t to balance defect coverage against test count.

## How To Use

1) Enumerate parameters and their values. 2) Choose t (often 2 or 3). 3) Use a covering-array generator to produce minimal test suite that covers every t-way interaction. 4) Execute the suite. 5) Defects involving up-to-t-way interactions are caught.

## Sources

- NIST SP 800-142 (Kuhn, Kacker, Lei 2010).
- Mandl 1985 pairwise paper.
