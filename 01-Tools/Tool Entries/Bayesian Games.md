---
Item_ID: tt-bayesian-games
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Bayesian Games (Harsanyi)'
tt_Source: 'Harsanyi, J.C. (1967-68) Management Science.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Categorize situation type'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Mental model
tt_Scale:
  - Dyadic
  - Inter-organizational
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
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Signaling Games
  - Mechanism Design
  - Bayesian Updating
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
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
Quick_Notes: 'A game where players have private information about their own types — equilibrium analysis treats each type as if it were a separate player.'
Needs_Processing: false
AI_Instructions: ""
---

# Bayesian Games (Harsanyi)

**One-line summary:** A game where players have private information about their own types — equilibrium analysis treats each type as if it were a separate player.

**When to reach for it:** Auctions where bidders have private valuations; negotiations with asymmetric information; principal-agent problems; insurance and adverse-selection contexts.

## Purpose

Harsanyi solved the puzzle of how to analyze games with incomplete information. The trick: replace 'incomplete information' with 'imperfect information about player types' by adding a chance move at the start that draws types. The Bayes-Nash equilibrium has each type playing optimally given their beliefs (Bayesian posteriors) about other players' types. The framework underlies modern auction theory, contract theory, and mechanism design.

## How To Use

1) Specify the type space and prior distribution over types. 2) Specify each player's payoff as a function of types and actions. 3) A Bayes-Nash equilibrium assigns each type an action that maximizes expected payoff given beliefs over other types' actions. 4) Compute via backward induction in extensive form or direct iteration in normal form.

## Sources

- Harsanyi 1967-68 Management Science.
