---
Item_ID: tt-backward-induction
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Backward Induction (Game Theory)'
tt_Source: 'Zermelo, E. (1913); Osborne, M.J. (2003) An Introduction to Game Theory ch. 5.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Decompose hierarchically'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Solo
  - Dyadic
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Decision / choice
  - Strategy / competition
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Subgame Perfect Equilibrium
  - Dynamic Programming
  - Nash Equilibrium
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
Quick_Notes: 'Solve finite extensive-form games by working backward from terminal nodes — at each node, the rational player picks the action with the best outcome assuming rational play forward.'
Needs_Processing: false
AI_Instructions: ""
---

# Backward Induction (Game Theory)

**One-line summary:** Solve finite extensive-form games by working backward from terminal nodes — at each node, the rational player picks the action with the best outcome assuming rational play forward.

**When to reach for it:** Sequential games with finite horizon and perfect information; chess-style decision problems; legal negotiation with deadline; recursive auction analysis.

## Purpose

In finite extensive-form games with perfect information, the rational outcome can be computed by induction from the terminal nodes. At each decision node, the active player picks the action with the highest payoff assuming all subsequent players play their backward-induced strategies. The procedure yields the subgame-perfect equilibrium and is the formal foundation for strategic anticipation. It generalizes to imperfect-information games via more complex equilibrium concepts.

## How To Use

1) Draw the game tree to the terminal nodes. 2) At each terminal node, record the payoff to each player. 3) Move one step back: each player at the prior node picks the action leading to their best terminal. 4) Continue until reaching the root. 5) The path defined is the backward-induction equilibrium.

## Sources

- Zermelo 1913.
- Osborne 2003 An Introduction to Game Theory ch. 5.
