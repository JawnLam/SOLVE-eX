---
Item_ID: tt-mechanism-design
Item_Prototype: Thinking_Tool
Title: 'Mechanism Design (Hurwicz-Maskin-Myerson)'
tt_Source: 'Hurwicz, L. (1960); Maskin, E. (1977); Myerson, R.B. (1981).'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Strategic & game-theoretic reasoning'
tt_Operation: 'Structure problem space across aspects'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Mental model
tt_Scale:
  - Organizational
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
  - Decision / choice
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Auction Design
  - Mixed-Strategy Equilibrium
  - Bayesian Persuasion
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
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
Quick_Notes: 'Design the rules of a game so that participants'' rational play produces the designer''s desired social outcome — the inverse problem of game theory.'
Needs_Processing: false
AI_Instructions: ""
---

# Mechanism Design (Hurwicz-Maskin-Myerson)

**One-line summary:** Design the rules of a game so that participants' rational play produces the designer's desired social outcome — the inverse problem of game theory.

**When to reach for it:** Auction design, matching-market design, public-goods provision, voting-system design, contract design; anywhere institutional rules are themselves the choice variable.

## Purpose

Standard game theory asks: given the rules, what will players do? Mechanism design asks the inverse: given a desired social outcome, what rules will produce it under players' rational self-interest? Myerson's revelation principle shows that any implementable outcome can be implemented by a direct mechanism where players truthfully report types. The framework underwrites modern auction design (FCC spectrum auctions), matching markets (medical residencies, school choice), and many other institutional designs.

## How To Use

1) Specify the social-choice function (what outcome do we want for each profile of player types?). 2) Identify incentive-compatibility and individual-rationality constraints. 3) Apply revelation principle: design a direct mechanism eliciting truthful reports. 4) Verify the equilibrium implements the desired outcome. 5) Real-world implementation may translate to an indirect mechanism for practical reasons.

## Sources

- Myerson 1981 Mathematics of OR.
- Hurwicz 1960.
