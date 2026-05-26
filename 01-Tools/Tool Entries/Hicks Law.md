---
Item_ID: tt-hicks-law
Item_Prototype: Thinking_Tool
Title: 'Hick''s Law'
tt_Source: 'Hick, W.E. (1952) ''On the rate of gain of information.'' *Quarterly Journal of Experimental Psychology*; HCI design canon.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Engineering / design reasoning'
tt_Operation: 'Categorize situation type'
tt_Cross_Domains: []
tt_Form:
  - Heuristic
  - Mental model
tt_Scale:
  - Solo
  - Organizational
tt_Duration:
  - Single session
tt_Lineage:
  - Scientific method
  - Design / craft tradition
tt_Posture: []
tt_State: []
tt_Agent: []
tt_About:
  - Decision / choice
  - Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Tradeoff Analysis
  - Forcing Function
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 02)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Decision time grows logarithmically with the number of choices — too many options slow users and degrade decision quality.'
Needs_Processing: false
AI_Instructions: ""
---

# Hick's Law

**One-line summary:** Decision time grows logarithmically with the number of choices — too many options slow users and degrade decision quality.

**When to reach for it:** Menu design, UI/form design, command-set design; product packaging; any context where presenting more options is assumed to help users.

## Purpose

Hick's empirical law sets a quantitative cost on option proliferation. The logarithmic form means modest increases in option count are tolerable but large ones are catastrophic — and the cost is paid every time the choice is encountered. The design implication: aggressively prune option counts, hierarchically nest where pruning is impossible, default-select common cases. 'More options' as an unqualified good is an anti-pattern.

## How To Use

1) Count the choices presented at each decision point. 2) If many, hierarchically group (categorize) or prune. 3) Provide sensible defaults; let users override if needed. 4) Test response-time and error-rate impact of option count.

## Sources

- Hick, W.E. (1952).
- Norman, D. (1988) *The Design of Everyday Things*.
