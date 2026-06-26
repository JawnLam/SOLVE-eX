---
Item_ID: tt-quadratic-voting
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: Quadratic Voting
tt_Source: "Lalley, S., & Weyl, G. (2018). \"Quadratic Voting: How Mechanism Design Can Radicalize Democracy.\" American Economic Association Papers & Proceedings."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Strategic & game-theoretic reasoning
tt_Operation: Aggregate parallel judgments
tt_Cross_Domains:
  - Phronetic / practical wisdom
tt_Form:
  - Scoring rubric
  - Sequenced workflow
tt_Scale:
  - Large group
  - Organizational
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
  - Industrial / business
tt_Posture:
  - Collaborative-willing
tt_State: []
tt_Agent:
  - Crowd / market
  - Human group
tt_About:
  - Power / politics
  - Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Prediction Markets
  - Auction Design
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-12 — initial classification (Sprint 01 — Pairwise-Gap Audit Card 08)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Voting mechanism where each voter gets a budget of \"voice credits\" to allocate across votes; the cost of N votes on one item is N². Lets voters express intensity, not just preference."
Needs_Processing: false
AI_Instructions: ""
---

# Quadratic Voting

**One-line summary:** Voting mechanism where each voter gets a budget of "voice credits" to allocate across votes; the cost of N votes on one item is N². Lets voters express intensity, not just preference.

**When to reach for it:** When a group decision involves multiple items and the strength of preference matters — budget allocation among public goods, priority-setting among features, governance in DAOs and online communities. Especially useful when standard majority voting would suppress minority intensity preferences.

## Purpose

One-person-one-vote weighs each voter equally per question but treats every preference as equally intense — a voter mildly preferring A and a voter desperate about A both get one vote. Quadratic voting (Weyl) lets voters "buy" extra votes from a fixed budget, but at quadratic cost — so concentrating all credits on one issue yields diminishing returns. The resulting outcome reflects intensity-weighted preferences, with theoretical efficiency properties.

## How To Use

1. **Allocate voice credits** to each voter (e.g., 100 credits per voter per cycle).
2. **For each issue**, voters choose how many votes to cast — positive or negative.
3. **Cost = vote-count²** in credits. So 1 vote costs 1 credit, 2 votes cost 4, 5 votes cost 25.
4. **Sum votes** across voters per item. Items with positive net votes pass.
5. **Track credit balances** across decisions if cycle-based.

Used in Colorado's 2019 legislative-priority experiment, RadicalxChange experiments, Gitcoin grants, several DAOs.

## Sources

- Lalley, S., & Weyl, E. G. (2018). "Quadratic Voting: How Mechanism Design Can Radicalize Democracy." *AEA Papers and Proceedings* 108: 33–37.
- Posner, E. A., & Weyl, E. G. (2018). *Radical Markets*. Princeton University Press. Chapter 2.
