---
Item_ID: tt-jidoka
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Jidoka (Autonomation)'
tt_Source: 'Ohno, T. Toyota Production System; Liker, J. (2021) The Toyota Way (2nd ed.).'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Engineering / design reasoning'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Mental model
  - Heuristic
tt_Scale:
  - Organizational
tt_Duration:
  - Practice
tt_Lineage:
  - Industrial / business
  - Eastern philosophical
tt_Posture: []
tt_State: []
tt_Agent: []
tt_About:
  - Strategy / competition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Poka-Yoke
  - Statistical Process Control
  - Kaizen
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
Quick_Notes: 'Design systems to stop automatically when an abnormality is detected — surface defects immediately rather than passing them downstream.'
Needs_Processing: false
AI_Instructions: ""
---

# Jidoka (Autonomation)

**One-line summary:** Design systems to stop automatically when an abnormality is detected — surface defects immediately rather than passing them downstream.

**When to reach for it:** Manufacturing line design; software pipelines; service processes where defects can be detected; building quality into the process rather than inspecting it in.

## Purpose

Jidoka (often translated as 'autonomation' — automation with a human touch) is one of two pillars of the Toyota Production System. The principle: a machine, line, or worker should stop automatically when an abnormality occurs. This serves three functions: prevent bad output from propagating downstream; surface the abnormality for immediate root-cause analysis; build quality into the process rather than relying on later inspection. The application generalizes beyond manufacturing: software CI that breaks builds on test failures; service operations with empowered escalation.

## How To Use

1) Identify failure modes and abnormality conditions. 2) Design detection mechanisms (sensors, andon cords, automated tests). 3) When abnormality detected, stop the process. 4) Investigate root cause immediately. 5) Fix; resume. 6) Improve detection over time. 7) Build culture that values stopping over running with defects.

## Sources

- Ohno Toyota Production System.
- Liker 2021 The Toyota Way.
