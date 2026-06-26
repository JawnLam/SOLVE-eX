---
Item_ID: tt-poka-yoke
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Poka-Yoke (Mistake-Proofing)'
tt_Source: 'Shingo, S. (1986) Zero Quality Control: Source Inspection and the Poka-Yoke System.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Engineering / design reasoning'
tt_Operation: 'Stress-test a position'
tt_Cross_Domains: []
tt_Form:
  - Heuristic
  - Sequenced workflow
tt_Scale:
  - Organizational
tt_Duration:
  - Practice
tt_Lineage:
  - Industrial / business
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
  - Jidoka
  - Forcing Function
  - Checklists
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
Quick_Notes: 'Design devices and procedures that make defects impossible or immediately detectable — mistake-proofing through physical or procedural constraints.'
Needs_Processing: false
AI_Instructions: ""
---

# Poka-Yoke (Mistake-Proofing)

**One-line summary:** Design devices and procedures that make defects impossible or immediately detectable — mistake-proofing through physical or procedural constraints.

**When to reach for it:** Process design where human error is a recurring source of defects; designing checklists, gates, or physical constraints that prevent mistakes; surgical safety; software UX.

## Purpose

Shingo's contribution to Lean: defects don't have to be inspected for and corrected — they can be prevented by design. Poka-yoke devices physically prevent the mistake (e.g., USB connectors that only fit one way), make the mistake obvious before it propagates (e.g., dashboard warnings), or stop the process when the mistake occurs (jidoka). The discipline shifts focus from after-the-fact inspection to upstream design. The technique transfers easily from physical to digital: form validation, type checking, idempotent APIs are software poka-yoke.

## How To Use

1) Identify recurring human errors in the process. 2) For each, ask: can a physical constraint prevent it? Can a check surface it before it propagates? Can the process stop? 3) Design the constraint into the process. 4) Verify the constraint works without introducing new errors. 5) Iterate.

## Sources

- Shingo 1986 Zero Quality Control.
