---
Item_ID: tt-convexity-concavity-reasoning
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: 'Convexity-Concavity Reasoning'
tt_Source: 'Jensen''s inequality (mathematical); Taleb, N.N. *Antifragile* technical appendix; standard finance canon.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Quantitative & probabilistic reasoning'
tt_Operation: 'Categorize situation type'
tt_Cross_Domains: []
tt_Form:
  - Heuristic
  - Mental model
tt_Scale:
  - Solo
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
  - Risk / uncertainty
  - Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Antifragility
  - Real Options Analysis
  - Tail-Risk Hedging
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - '2026-05-12 — initial classification (Sprint 04 — Reverse-Audit Against External Collections Card 02)'
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Classify a position by its payoff curve — convex (gains accelerate, losses bounded) is antifragile; concave (gains capped, losses accelerate) is fragile.'
Needs_Processing: false
AI_Instructions: ""
---

# Convexity-Concavity Reasoning

**One-line summary:** Classify a position by its payoff curve — convex (gains accelerate, losses bounded) is antifragile; concave (gains capped, losses accelerate) is fragile.

**When to reach for it:** Designing exposures, evaluating asymmetric bets, structuring policy with non-linear consequences, distinguishing 'cheap optionality' from 'expensive blow-up risk.'

## Purpose

Jensen's inequality formalizes that for a non-linear payoff function, the expected value of the function differs from the function of the expected value. The directional intuition: convex curves benefit from volatility (their expected outcome under noise exceeds the no-noise outcome); concave curves suffer. The discipline is reading every commitment as a payoff curve and asking which direction it points.

## How To Use

1) Sketch the payoff function: outcome vs. magnitude of input variation. 2) Classify: convex (curves up), linear, or concave (curves down)? 3) For convex, accept and embrace volatility — it's wealth-creating in expectation. 4) For concave, suppress volatility — it's destructive. 5) Redesign concave exposures into convex ones where possible (caps, hedges, optionality).

## Sources

- Taleb, N.N. (2012) *Antifragile*, technical appendix on Jensen's inequality.
