---
Item_ID: tt-mixed-strategy-equilibrium
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Mixed-Strategy Equilibrium'
tt_Source: 'von Neumann, J. (1928); Osborne, M.J. (2003) ch. 4.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Score and rank options'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
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
  - Strategy / competition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Nash Equilibrium
  - Mechanism Design
  - Bayesian Games
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
Quick_Notes: 'An equilibrium where players randomize over pure strategies — required when no pure-strategy equilibrium exists (e.g., matching pennies).'
Needs_Processing: false
AI_Instructions: ""
---

# Mixed-Strategy Equilibrium

**One-line summary:** An equilibrium where players randomize over pure strategies — required when no pure-strategy equilibrium exists (e.g., matching pennies).

**When to reach for it:** Adversarial games without pure-strategy equilibria; security games (attacker/defender randomization); penalty kicks; auditing strategy under detection avoidance.

## Purpose

Nash's existence theorem guarantees an equilibrium in finite games, but it may require randomization. In matching pennies, rock-paper-scissors, and many adversarial games, the equilibrium has each player randomizing in specific proportions that make the opponent indifferent. The mathematics is the indifference principle: each pure strategy played with positive probability must yield the same expected payoff. Computing mixed equilibria is harder than pure ones; LP and bimatrix solvers handle 2-player cases.

## How To Use

1) For each player, identify their pure-strategy payoffs given the opponent's strategy. 2) Set the indifference condition: the opponent's mixing probabilities make my pure strategies equally attractive. 3) Solve the resulting linear system for the mixing probabilities. 4) Verify: the resulting profile is a mixed-strategy Nash equilibrium.

## Sources

- von Neumann 1928.
- Osborne 2003 ch. 4.
