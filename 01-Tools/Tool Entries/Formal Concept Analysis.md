---
Item_ID: tt-formal-concept-analysis
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Formal Concept Analysis (FCA)'
tt_Source: 'Wille, R. (1982) Restructuring Lattice Theory. Ganter, B. & Wille, R. (1999) Formal Concept Analysis Mathematical Foundations.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Combinatorial / enumerative reasoning'
tt_Operation: 'Map relational topology'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Visualization technique
tt_Scale:
  - Solo
  - Organizational
tt_Duration:
  - Project
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
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Morphological Analysis
  - Attribute Exploration
  - Combinatorial Enumeration
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
Quick_Notes: 'Derive a concept lattice from an object x attribute incidence matrix — reveals the natural hierarchical structure of a domain.'
Needs_Processing: false
AI_Instructions: ""
---

# Formal Concept Analysis (FCA)

**One-line summary:** Derive a concept lattice from an object x attribute incidence matrix — reveals the natural hierarchical structure of a domain.

**When to reach for it:** Taxonomy discovery, conceptual structure analysis, domain modeling, ontology refinement; analyzing relationships in large categorical datasets.

## Purpose

FCA starts from raw data (objects with their attributes) and computes the lattice of formal concepts — every (object-set, attribute-set) pair such that the object-set has exactly those attributes and the attribute-set is shared by exactly those objects. The result is a hierarchical structure that emerges from the data rather than being imposed. The lattice visualizes natural conceptual hierarchy: which concepts are sub/super of others, which are equivalent, which are orthogonal.

## How To Use

1) Build the object x attribute table. 2) Run an FCA tool (ConExp, Concept Explorer). 3) Examine the concept lattice. 4) Identify base concepts (atomic), composite concepts, and the join/meet structure. 5) Use to refine the domain model.

## Sources

- Wille 1982.
- Ganter & Wille 1999.
