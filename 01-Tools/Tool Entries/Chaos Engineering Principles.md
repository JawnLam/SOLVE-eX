---
Item_ID: tt-chaos-engineering-principles
Item_Prototype: Thinking_Tool
Title: Netflix Chaos Engineering Principles
tt_Source: "Rosenthal, C., & Jones, N. (2020). Chaos Engineering. O'Reilly."
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Run experimental cycle
tt_Cross_Domains: []
tt_Form:
  - Sequenced workflow
  - Algorithm
tt_Scale:
  - Small group
  - Organizational
tt_Duration:
  - Practice
tt_Lineage:
  - Industrial / business
  - Scientific method
tt_Posture:
  - Expert-required
  - Adversarial-tolerant
tt_State: []
tt_Agent:
  - Human group
  - Human-AI partnership
tt_About:
  - Risk / uncertainty
  - Group / organization
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With: []
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-12 — initial classification (Sprint 03 — Deep-Gap Backfill Card 09)"
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Discipline of experimenting on production systems to build confidence in resilience — five principles: hypothesize steady state, vary real-world events, run in production, automate continuously, minimize blast radius."
Needs_Processing: false
AI_Instructions: ""
---

# Netflix Chaos Engineering Principles

**One-line summary:** Discipline of experimenting on production systems to build confidence in resilience — five principles: hypothesize steady state, vary real-world events, run in production, automate continuously, minimize blast radius.

**When to reach for it:** Operating a complex distributed production system where confidence in resilience under adverse conditions must be earned empirically because static analysis cannot predict emergent failure modes.

## Purpose

Chaos Engineering, developed at Netflix and codified in the Principles of Chaos (2017), is the discipline of experimenting on production systems to build confidence in their capability to withstand turbulent conditions. Five principles: (1) Build a hypothesis around steady-state behavior — what observable measure characterizes 'system working'? (2) Vary real-world events — induce failures that could happen in production (server crash, dependency failure, latency spike). (3) Run experiments in production — staging environments don't capture the full system. (4) Automate experiments to run continuously — one-time experiments quickly become outdated. (5) Minimize blast radius — start small, expand carefully, have abort criteria. Embodied in Netflix tools (Chaos Monkey randomly terminates instances; Chaos Kong takes out an entire AWS region).

## How To Use

(1) Define steady state: identify a measurable outcome that characterizes normal system function — error rate, latency, business metric. (2) Form hypothesis: under the planned perturbation, the system should remain in steady state. (3) Design the experiment: what failure will be induced, on how much of the system, with what fallback if things go wrong. (4) Run in production (or, if not yet ready, in a high-fidelity environment) with abort criteria. (5) Observe: does the system remain in steady state? If yes, confidence increases. If no, learn from the failure mode. (6) Automate: incorporate the experiment into continuous chaos testing. Start small (Chaos Monkey randomly killing instances), expand to larger perturbations (region failure, dependency partition). The discipline: only run experiments when you have monitoring and abort capability; minimize blast radius.

## Sources

- Basiri, A., et al. (2016). 'Chaos Engineering.' *IEEE Software* 33(3).
- Principles of Chaos Engineering (2017). principlesofchaos.org.
- Rosenthal, C., & Jones, N. (2020). *Chaos Engineering*. O'Reilly.
