---
Item_ID: tt-queueing-theory
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Queueing Theory'
tt_Source: 'Erlang, A.K. (1909); Kleinrock, L. (1975) Queueing Systems; Hillier-Lieberman ch. 17-18.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Systems / cybernetic thinking'
tt_Operation: 'Categorize situation type'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Mental model
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
  - Strategy / competition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Statistical Process Control
  - Theory of Constraints
  - Monte Carlo Simulation
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
Quick_Notes: 'Mathematical models of waiting lines — arrival rates, service rates, server counts, queue disciplines — predict wait times, utilization, and throughput.'
Needs_Processing: false
AI_Instructions: ""
---

# Queueing Theory

**One-line summary:** Mathematical models of waiting lines — arrival rates, service rates, server counts, queue disciplines — predict wait times, utilization, and throughput.

**When to reach for it:** Capacity planning for systems with stochastic demand: call centers, hospitals, manufacturing lines, server farms, customer-service operations.

## Purpose

Queueing theory provides closed-form analysis for stochastic-arrival, stochastic-service systems. M/M/1, M/M/c, and other Kendall-notation models give exact formulas for utilization, expected wait time, and queue length given arrival rate (lambda) and service rate (mu). The counterintuitive result: as utilization approaches 100%, wait time grows asymptotically, so designing systems for near-100% utilization produces catastrophic waits. The discipline is using the formulas rather than relying on intuition about queues.

## How To Use

1) Estimate arrival rate (lambda) and service rate (mu). 2) Choose the model (M/M/1 for single server, M/M/c for c servers, etc.). 3) Compute utilization rho = lambda / (c*mu). 4) Apply the model's formulas for L (queue length), W (wait time). 5) Design for utilization that gives acceptable wait time, typically 70-85% in service contexts.

## Sources

- Kleinrock 1975 Queueing Systems.
