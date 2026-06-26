---
Item_ID: tt-community-detection
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Community Detection (Modularity, Louvain)'
tt_Source: 'Newman, M.E.J. & Girvan, M. (2004) Physical Review E; Blondel, V.D. et al. (2008) Louvain method.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Systems / cybernetic thinking'
tt_Operation: 'Decompose hierarchically'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Visualization technique
tt_Scale:
  - Organizational
  - Civilizational
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
  - Group / organization
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Network Centrality Analysis
  - Clustering Percolation Analysis
  - Coalition Mapping
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 06)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Partition a network into densely-connected subgroups (communities) such that within-community connections far exceed between-community connections.'
Needs_Processing: false
AI_Instructions: ""
---

# Community Detection (Modularity, Louvain)

**One-line summary:** Partition a network into densely-connected subgroups (communities) such that within-community connections far exceed between-community connections.

**When to reach for it:** Social network analysis (identifying cliques and clusters); biological network analysis (functional modules); recommendation systems; collaboration analysis; epidemic-spread structure.

## Purpose

Many real networks have community structure: nodes cluster into groups with dense internal connections and sparser external ones. Community detection algorithms (modularity maximization, Louvain, label propagation, spectral methods) find these partitions automatically. Communities reveal hidden structure: research collaborations, ideological clusters, functional modules in protein-interaction networks. The Louvain method (2008) is the most-used due to its speed on large networks.

## How To Use

1) Construct the graph (nodes, weighted or unweighted edges). 2) Choose an algorithm (Louvain is good default). 3) Run the algorithm to get a community assignment per node. 4) Evaluate modularity Q — higher Q means stronger community structure. 5) Visualize and interpret communities; some may be meaningful groups, others artifacts.

## Sources

- Newman & Girvan 2004 Physical Review E.
- Blondel et al. 2008 J. Stat. Mech.
