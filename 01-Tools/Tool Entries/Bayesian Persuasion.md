---
Item_ID: tt-bayesian-persuasion
Item_Prototype: Thinking_Tool
Title: 'Bayesian Persuasion (Kamenica-Gentzkow)'
tt_Source: 'Kamenica, E. & Gentzkow, M. (2011) American Economic Review.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Sequence multi-party persuasion'
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
  - Other / relationship
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Signaling Games
  - Mechanism Design
  - Bayesian Games
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 06)'
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'A sender designs an information policy (signal structure) to commit to before observing state — choosing how to reveal information to influence a receiver''s action.'
Needs_Processing: false
AI_Instructions: ""
---

# Bayesian Persuasion (Kamenica-Gentzkow)

**One-line summary:** A sender designs an information policy (signal structure) to commit to before observing state — choosing how to reveal information to influence a receiver's action.

**When to reach for it:** Designing disclosure policies (regulatory disclosure, product testing); strategic information design in marketing; courtroom argument structuring; designing recommender-system transparency.

## Purpose

Standard signaling games have the sender choose a signal after observing private information. Bayesian Persuasion has the sender commit to an information policy before observing — like designing a test that randomly reveals types. The framework shows that even a sender with no private information can systematically influence the receiver's beliefs and actions by choosing how to bundle states into observable signals. The theory has reshaped information economics.

## How To Use

1) Define states, sender's preferences over receiver actions, receiver's preferences over states. 2) Sender chooses a signal structure (mapping from states to signals). 3) Receiver Bayesian-updates on signal, takes optimal action. 4) Sender's optimization picks the signal structure maximizing expected utility given the induced receiver action. 5) Concavification of the sender's value function over receiver beliefs identifies the optimum.

## Sources

- Kamenica & Gentzkow 2011 AER.
