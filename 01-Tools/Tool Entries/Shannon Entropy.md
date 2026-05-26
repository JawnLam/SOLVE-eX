---
Item_ID: tt-shannon-entropy
Item_Prototype: Thinking_Tool
Title: 'Shannon Entropy'
tt_Source: 'Shannon, C.E. (1948) A Mathematical Theory of Communication. Bell System Technical Journal.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: 'Quantitative & probabilistic reasoning'
tt_Operation: 'Score and rank options'
tt_Cross_Domains: []
tt_Form:
  - Algorithm
  - Mental model
tt_Scale:
  - Solo
tt_Duration:
  - Single session
tt_Lineage:
  - Mathematical / formal
  - Scientific method
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent: []
tt_About:
  - Mind / cognition
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Mutual Information
  - KL Divergence
  - Maximum Entropy Principle
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
Quick_Notes: 'Quantify the average uncertainty (in bits) of a random variable — H(X) = -sum p(x) log p(x).'
Needs_Processing: false
AI_Instructions: ""
---

# Shannon Entropy

**One-line summary:** Quantify the average uncertainty (in bits) of a random variable — H(X) = -sum p(x) log p(x).

**When to reach for it:** Information theory; coding theory; ML model evaluation; measuring diversity, surprise, or unpredictability in any discrete distribution.

## Purpose

Shannon's entropy is the average bits of information per symbol from a source. It quantifies uncertainty: a uniform distribution maximizes entropy; a degenerate one (probability 1 on one outcome) has zero. The measure underlies compression bounds (Source Coding Theorem), channel capacity, and many information-theoretic methods. As a thinking tool, entropy gives precise vocabulary for 'how much uncertainty does this random variable carry?'

## How To Use

1) Specify the probability distribution p(x). 2) Compute H(X) = -sum over x of p(x) * log_2(p(x)). 3) Units are bits. 4) Interpret: higher entropy = more uncertainty / unpredictability / diversity. 5) Compare across distributions for relative-information assessment.

## Sources

- Shannon 1948.
