---
Item_ID: tt-kpi-design
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: KPI Design
tt_Source: "Drucker 1954 (Management by Objectives); Doerr (OKRs at Intel/Google); Kaplan & Norton 1992 (Balanced Scorecard)"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Refine a draft / artifact
tt_Cross_Domains: []
tt_Form:
- Sequenced workflow
- Checklist
tt_Scale:
- Small group
- Organizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Industrial / business
tt_Posture:
- Beginner-friendly
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
- Human group
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Goodhart-Aware Metric Selection
tt_Often_Follows:
- Construct Validity Frameworks
tt_Pairs_Well_With:
- Goodhart-Aware Metric Selection
- Construct Validity Frameworks
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human', 'Human group'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "The discipline of choosing metrics that drive desired behavior rather than perverse local-optimization. Pair every output KPI with an input KPI and a guardrail KPI; specify the action triggered by each threshold."
Needs_Processing: false
AI_Instructions: ''
---

# KPI Design

**One-line summary:** A discipline for selecting and structuring key performance indicators so that what gets measured produces the behavior the organization actually wants — pairing output metrics with input drivers and guardrails.

**When to reach for it:** Designing performance dashboards, OKRs, executive review packages, departmental scorecards, or any system that will use metrics to drive behavior — and especially when re-designing a system that's producing perverse behavior.

---

## Purpose Of This Thinking Tool

KPIs work because they channel attention. They fail when they channel attention toward the metric instead of the underlying objective. KPI design is the discipline that gets the channeling right by structuring metrics into three roles:

- **Output KPIs** — measure the result you actually care about (revenue, retention, cycle-time)
- **Input KPIs** — measure the leading drivers the team can influence directly (calls made, code reviewed, customers visited)
- **Guardrail KPIs** — measure things that should NOT degrade as the output is pursued (quality, cost, ethics, fairness)

The non-obvious operational insight is that *output KPIs alone produce perverse behavior*. Customers acquired (output) without retention guardrail leads to churn-trap. Code shipped (output) without quality guardrail leads to bug-debt. The structure prevents this by making the trade-offs visible at the dashboard level.

Drucker formalized objectives-driven management in the 1950s; OKRs (Doerr's adaptation at Intel) and the Balanced Scorecard (Kaplan & Norton 1992) gave structured forms. The current generation of KPI design synthesizes these with construct-validity discipline and Goodhart's law awareness.

## Why Use This Thinking Tool

Three failure modes structured KPI design prevents:

1. **Lagging-indicator-only dashboards.** Output-only metrics don't tell the team how to act; pairing with input KPIs makes them actionable.
2. **Single-axis optimization.** Output without guardrails invites local optimization at global cost. Guardrails preserve the "while not breaking" constraints.
3. **Goal cascade incoherence.** Without explicit input/output structure, sub-team KPIs can sum to less than the parent KPI; the structure catches mismatches.

For consulting and operations work, KPI design is the highest-leverage routine activity in the management system — the metrics shape behavior every day, and bad metrics produce bad behavior at scale.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the objective in plain language. What outcome does this team / org want?  |
|    2 | Pick the output KPI: the metric closest to the objective itself.                |
|    3 | Identify input KPIs: leading drivers the team can directly influence that      |
|      | should produce the output.                                                      |
|    4 | Identify guardrail KPIs: things that should NOT degrade as the output is        |
|      | pursued. List at least 2 — quality and one other (cost, ethics, fairness).     |
|    5 | For each KPI, specify: definition, computation, threshold, decision triggered.  |
|    6 | Pre-mortem: how could this set of KPIs produce gaming behavior? What would      |
|      | "win on metrics, lose on objective" look like?                                  |
|    7 | Add anti-gaming guardrails to address the pre-mortem findings.                  |
|    8 | Schedule periodic re-validation: do the input KPIs still drive the output?     |
|      | Are the guardrails still binding the right behavior?                           |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
KPI DESIGN CANVAS

    Team / org:  ____________________________________________________________
    Objective (plain language): _____________________________________________

    OUTPUT KPI (what we ultimately want)
      Name:        _________________________________________________________
      Definition:  _________________________________________________________
      Source:      _________________________________________________________
      Cadence:     _________________________________________________________
      Threshold / target: __________________________________________________
      Decision triggered when missed: ______________________________________

    INPUT KPI(s) (leading drivers)
      Input 1:  ____________________________   target: _____   action: _____
      Input 2:  ____________________________   target: _____   action: _____
      Input 3:  ____________________________   target: _____   action: _____

    GUARDRAIL KPI(s) (must NOT degrade)
      Guardrail 1 (quality):    ___________________________  threshold: _____
      Guardrail 2 (cost):       ___________________________  threshold: _____
      Guardrail 3 (ethics/fair): ___________________________  threshold: _____

    PRE-MORTEM (gaming check)
      How could a team "win" the output KPI without achieving the objective?
        Scenario 1: __________________________________________________________
        Mitigation: __________________________________________________________

      How could a team game the input KPIs without producing output?
        Scenario 2: __________________________________________________________
        Mitigation: __________________________________________________________

      What guardrail is missing?  __________________________________________

    HIERARCHY CHECK (when KPIs cascade across teams)
      Parent output KPI:                    ______________________
      Sub-team A output KPI:                ______________________
      Sub-team B output KPI:                ______________________
      Sub-team C output KPI:                ______________________

      Check: do sub-team outputs *sum* (or otherwise compose) to parent?
        □ yes — cascade is coherent
        □ no — there's a gap or overlap; investigate

KPI DEFINITION TEMPLATE (per KPI)

      Name:                  _____________________________________________
      Construct it measures: _____________________________________________
      Operational definition: ____________________________________________
      Numerator:             _____________________________________________
      Denominator:           _____________________________________________
      Inclusion / exclusion: _____________________________________________
      Refresh cadence:       _____________________________________________
      Owner:                 _____________________________________________
      Review cadence:        _____________________________________________
      Threshold meaning:     _____________________________________________
      Action when below:     _____________________________________________
      Action when above:     _____________________________________________

ANTI-PATTERN CHECKLIST

      [ ] Output-only dashboard with no input drivers
      [ ] No guardrails, only output
      [ ] Identical KPIs at every level (cascading copy-paste)
      [ ] More than 5–7 KPIs per dashboard (attention dilution)
      [ ] KPI thresholds without an associated decision rule
      [ ] No periodic re-validation
```

> **Operational notes:** Three disciplines. (1) Always pair output with input. Output-only dashboards tell you the score after the game; input-paired dashboards tell you what to do during it. The team needs the latter. (2) Always include at least two guardrails. The most common organizational failure is optimizing output at the expense of an unmonitored constraint (quality, cost, ethics, fairness). The pre-mortem is the discipline that catches this — ask "if a team optimized hard against this output KPI, what would they sacrifice?" The answer is your missing guardrail. (3) Cap KPI count. 3–7 KPIs per team / dashboard is the sweet spot; beyond that, attention fragments and no metric drives behavior. If you have more, you have priorities, not KPIs. Fourth: tie KPIs to *decisions*, not just to status. A KPI without an associated decision rule (what changes when it crosses threshold?) is decorative. The decision-trigger discipline forces the question of why the metric is on the dashboard at all.
