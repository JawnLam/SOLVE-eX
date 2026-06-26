---
Item_ID: tt-shapley-value
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Shapley Value (Cooperative Game Theory)'
tt_Source: 'Shapley, L.S. (1953) A Value for n-Person Games.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Score and rank options'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
tt_Scale:
  - Small group
  - Organizational
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Group / organization
  - Decision / choice
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Coalition Mapping
  - Mechanism Design
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
Quick_Notes: 'The unique fair allocation of cooperative game value satisfying efficiency, symmetry, dummy, and additivity axioms — averages each player''s marginal contribution across all orderings.'
Needs_Processing: false
AI_Instructions: ""
---

# Shapley Value (Cooperative Game Theory)

**One-line summary:** The unique fair allocation of cooperative game value satisfying efficiency, symmetry, dummy, and additivity axioms — averages each player's marginal contribution across all orderings.

**When to reach for it:** Profit-sharing in alliances; cost-allocation across users of a shared resource; feature-importance in ML (SHAP values); influence attribution in social or political networks.

## Purpose

When n agents cooperate to produce joint value, how should the value be divided? Shapley showed there is a unique allocation satisfying four reasonable axioms: efficient (all value allocated), symmetric (equal contributors get equal shares), dummy (zero contributors get nothing), additive (works on game sums). The Shapley value computes each agent's average marginal contribution across all possible orderings. The same math has found wide use in feature attribution (SHAP) and network influence analysis.

## How To Use

1) Define the characteristic function v(S) — the value any subset S of players can achieve. 2) For each player i, compute marginal contribution v(S + i) - v(S) across all subsets S not containing i. 3) Average over all orderings of players. 4) The result is player i's Shapley value. 5) Use as the fair share for allocation.

## Sources

- Shapley 1953.
