---
Item_ID: tt-network-flow
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Network Flow (Ford-Fulkerson Max-Flow Min-Cut)'
tt_Source: 'Ford, L.R. & Fulkerson, D.R. (1956) max-flow min-cut theorem.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Systems / cybernetic thinking'
tt_Operation: 'Locate intervention leverage'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Visualization technique
tt_Scale:
  - Organizational
tt_Duration:
  - Project
tt_Lineage:
  - Mathematical / formal
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
  - Theory of Constraints
  - Critical Path
  - Linear Programming
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
Quick_Notes: 'Compute the maximum flow from source to sink in a capacitated network — equals the minimum cut (the bottleneck set of edges).'
Needs_Processing: false
AI_Instructions: ""
---

# Network Flow (Ford-Fulkerson Max-Flow Min-Cut)

**One-line summary:** Compute the maximum flow from source to sink in a capacitated network — equals the minimum cut (the bottleneck set of edges).

**When to reach for it:** Transportation problems, supply chain analysis, telecommunications routing, project scheduling, bipartite matching, image segmentation.

## Purpose

Max-flow min-cut is one of the most-applied theorems in OR: in any network with edge capacities, the maximum flow from source to sink equals the capacity of the minimum-capacity cut. The cut identifies the bottleneck. The same algorithm solves bipartite matching, project-scheduling critical-path, and many other problems via reduction. Modern algorithms (push-relabel, etc.) solve large instances quickly.

## How To Use

1) Model as a directed graph with capacities on edges. 2) Identify source and sink nodes. 3) Run a max-flow algorithm (Ford-Fulkerson, push-relabel). 4) Read the maximum flow value and the corresponding minimum cut. 5) The min-cut edges are the bottleneck — interventions target those.

## Sources

- Ford & Fulkerson 1956.
