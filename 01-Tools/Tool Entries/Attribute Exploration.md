---
Item_ID: tt-attribute-exploration
Item_Prototype: Thinking_Tool
Title: 'Attribute Exploration (FCA-derivative)'
tt_Source: 'Ganter, B. (1991) Attribute exploration with background knowledge.'
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: 'Empirical / scientific method'
tt_Operation: 'Apply question bank'
tt_Cross_Domains: []
tt_Form:
  - Dialogue protocol
  - Sequenced workflow
tt_Scale:
  - Dyadic
  - Small group
tt_Duration:
  - Single session
  - Workshop
tt_Lineage:
  - Mathematical / formal
  - Scientific method
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Mind / cognition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Formal Concept Analysis
  - Delphi Forecasts and Predictions
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 03)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'An interactive expert-elicitation protocol derived from FCA — generates implications and prompts the expert to confirm or counterexample each.'
Needs_Processing: false
AI_Instructions: ""
---

# Attribute Exploration (FCA-derivative)

**One-line summary:** An interactive expert-elicitation protocol derived from FCA — generates implications and prompts the expert to confirm or counterexample each.

**When to reach for it:** Knowledge engineering for expert systems; ontology refinement; codifying tacit domain knowledge into explicit rules.

## Purpose

FCA can be applied not just to existing data but to expert knowledge via Attribute Exploration: the system computes implications consistent with current data, presents each to the expert, and the expert either confirms (the implication is added) or provides a counterexample (the dataset is extended). Iterating converges on a complete attribute logic of the domain. The protocol turns the tacit expertise into explicit implications.

## How To Use

1) Define the attributes of interest. 2) Initialize an empty or seed object x attribute table. 3) The FCA system computes a candidate implication. 4) Expert evaluates: confirm or provide counterexample. 5) Update the table; repeat. 6) Terminates when no new implications can be derived.

## Sources

- Ganter, B. (1991) Attribute exploration with background knowledge.
