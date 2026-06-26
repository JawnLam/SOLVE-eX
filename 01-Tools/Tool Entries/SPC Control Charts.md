---
Item_ID: tt-spc-control-charts
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Statistical Process Control (Shewhart Control Charts)'
tt_Source: 'Shewhart, W.A. (1931) Economic Control of Quality of Manufactured Product.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Quantitative & probabilistic reasoning'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Visualization technique
  - Algorithm
tt_Scale:
  - Organizational
tt_Duration:
  - Practice
tt_Lineage:
  - Industrial / business
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Six Sigma DMAIC
  - Goodhart-Aware Metric Selection
  - Sensitivity Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 09)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Plot process measurements over time with control limits; distinguish common-cause variation (in control) from special-cause variation (signal worth investigating).'
Needs_Processing: false
AI_Instructions: ""
---

# Statistical Process Control (Shewhart Control Charts)

**One-line summary:** Plot process measurements over time with control limits; distinguish common-cause variation (in control) from special-cause variation (signal worth investigating).

**When to reach for it:** Monitoring any process where understanding whether variation is signal or noise matters — manufacturing, healthcare metrics, software performance, financial KPIs.

## Purpose

Shewhart's breakthrough: most observed variation is noise (common cause); only some variation is signal (special cause). Without distinguishing them, managers over-react to noise (treating each variation as a problem to solve) and under-react to signal (missing real shifts). Control charts plot data over time with limits at ±3 standard deviations from the mean; points outside the limits or patterns suggesting non-randomness indicate special-cause variation worth investigating. The method underlies modern quality management.

## How To Use

1) Identify the process measurement. 2) Collect baseline data while the process is stable. 3) Compute mean and standard deviation. 4) Plot data with control limits at ±3σ. 5) For new data points: in-control means leave alone; out-of-control means investigate. 6) Use additional rules (Western Electric rules) to detect subtler signals.

## Sources

- Shewhart 1931 Economic Control of Quality.
