---
Item_ID: tt-hasse-diagram
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Concept Lattice / Hasse Diagram'
tt_Source: 'Hasse, H. (early 20th c.) order-theory canon; FCA practitioner literature.'
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: 'Mathematical / proof reasoning'
tt_Operation: 'Map relational topology'
tt_Cross_Domains: []
tt_Form:
  - Visualization technique
tt_Scale:
  - Solo
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1, 3.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Formal Concept Analysis
  - Causal DAGs
  - Network Centrality Analysis
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
Quick_Notes: 'The standard visualization for a partial order — nodes at vertical positions by rank, edges only for covering relations (no transitive shortcuts shown).'
Needs_Processing: false
AI_Instructions: ""
---

# Concept Lattice / Hasse Diagram

**One-line summary:** The standard visualization for a partial order — nodes at vertical positions by rank, edges only for covering relations (no transitive shortcuts shown).

**When to reach for it:** Visualizing any partially-ordered structure: divisibility lattices, subset lattices, FCA concept lattices, dependency graphs with anti-symmetry.

## Purpose

Hasse diagrams visualize partial orders such that transitive arrows are implicit (omitted). The result is a clean picture where only direct cover relations are drawn. The discipline transfers to many domains where partial orderings show up: dependency analysis, concept hierarchies, divisibility structures, organizational reporting. FCA produces lattices that are best read as Hasse diagrams.

## How To Use

1) Identify the partial order (set + reflexive transitive antisymmetric relation). 2) Place top elements highest, bottom lowest. 3) Draw an edge between x and y if x < y AND no z satisfies x < z < y. 4) Omit transitive edges. 5) Use horizontal position to reduce edge crossings.

## Sources

- Standard order-theory texts.
