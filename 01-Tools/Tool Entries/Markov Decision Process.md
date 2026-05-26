---
Item_ID: tt-markov-decision-process
Item_Prototype: Thinking_Tool
Title: 'Markov Decision Process (MDP)'
tt_Source: 'Bellman 1957; Puterman, M.L. (1994) Markov Decision Processes.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Decision analysis'
tt_Operation: 'Project alternative futures'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Mental model
tt_Scale:
  - Solo
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
  - Decision / choice
  - Time / future
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1, 4.4]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Dynamic Programming
  - Bayesian Updating
  - Recognition-Primed Decision
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 05)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'A formal model for sequential decisions under uncertainty — states, actions, transition probabilities, rewards — solved by dynamic programming or RL.'
Needs_Processing: false
AI_Instructions: ""
---

# Markov Decision Process (MDP)

**One-line summary:** A formal model for sequential decisions under uncertainty — states, actions, transition probabilities, rewards — solved by dynamic programming or RL.

**When to reach for it:** Inventory management, equipment-replacement decisions, medical treatment over time, robotics planning, anything where state evolves stochastically based on actions taken.

## Purpose

MDPs formalize sequential decision-making where the system has Markov state, actions stochastically transition the state, and rewards accumulate. The mathematical structure (Bellman equation, value/policy iteration) admits exact solutions for small problems and approximations (RL, function approximation) for large ones. The framework is the canonical formulation behind reinforcement learning and much of modern AI planning.

## How To Use

1) Define state space S, action space A. 2) Specify transition probabilities P(s'|s,a). 3) Specify reward function R(s,a). 4) Choose discount factor gamma. 5) Solve via value iteration, policy iteration, or RL for large state spaces. 6) Extract optimal policy pi*(s).

## Sources

- Puterman 1994 Markov Decision Processes.
