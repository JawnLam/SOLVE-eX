---
Item_ID: tt-goodhart-aware-metric-selection
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Goodhart-Aware Metric Selection
tt_Source: "Charles Goodhart 1975 ('any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes'); Marilyn Strathern 1997 popularized form"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Stress-test a position
tt_Cross_Domains: []
tt_Form:
- Sequenced workflow
- Heuristic
tt_Scale:
- Small group
- Organizational
tt_Duration:
- Workshop
tt_Lineage:
- Industrial / business
- Western analytic / academic
tt_Posture:
- Adversarial-tolerant
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
- Human group
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows:
- KPI Design
- Construct Validity Frameworks
tt_Pairs_Well_With:
- KPI Design
- Pre-Mortem
- Inversion
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
Quick_Notes: "When a measure becomes a target, it ceases to be a good measure. The thinking tool: forecast each metric's failure mode under high incentive pressure, then design measure + incentive system together. Manheim & Garrabrant's taxonomy (regressional, extremal, causal, adversarial Goodhart) sharpens the analysis."
Needs_Processing: false
AI_Instructions: ''
---

# Goodhart-Aware Metric Selection

**One-line summary:** A discipline for choosing and structuring metrics with explicit foresight about how they will fail when incentivized — pre-mortem the metric, design counter-pressures, and accept that no single metric survives heavy optimization unscathed.

**When to reach for it:** Before tying any measure to compensation, promotion, or significant resource allocation; when redesigning a metric system that's started producing perverse behavior; or when assessing a vendor or team's claims that rest on a single proxy.

---

## Purpose Of This Thinking Tool

Goodhart's law captures one of the most reliable patterns in human systems: a metric that's predictive when observed casually becomes unreliable once it's incentivized. The reason is not random — it's *adaptive*. Once a metric becomes a target, agents optimize against the metric directly rather than against the underlying construct, and the gap between metric and construct widens.

The non-obvious operational insight is that Goodhart's law is *predictable per metric*. Different metrics fail in different ways, and you can usually anticipate the failure mode. Manheim and Garrabrant's 2018 taxonomy distinguishes:

- **Regressional Goodhart** — agents already at the metric's high tail are noisier; selecting on metric over-selects noise
- **Extremal Goodhart** — relationships that hold near typical values break at the extremes the optimizer pushes toward
- **Causal Goodhart** — the metric correlates with the goal but doesn't cause it; pushing the metric doesn't move the goal
- **Adversarial Goodhart** — agents understand the metric and route around it

For each, the design counter-pressure is different. The thinking tool is to apply the taxonomy explicitly during metric selection: which Goodhart failure is most likely for *this* metric in *this* incentive system?

## Why Use This Thinking Tool

Three failure modes the awareness prevents:

1. **Optimizer-blind metric design.** Picking a metric without forecasting its failure-under-pressure produces predictable misalignment.
2. **Single-metric reliance.** A single metric can always be gamed; multiple metrics with explicit guardrails make gaming costlier.
3. **Late-stage discovery.** Goodhart failures are often discovered only when the underlying objective worsens despite metric improvement — by which time the incentive system has already produced bad behavior.

For consulting and operations work, Goodhart-awareness is the *prudential* discipline that converts metric design from "what looks measurable?" into "what will this measure do when treated as a target?" — a fundamentally different question.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the construct you actually care about (the GOAL, not the metric).      |
|    2 | List candidate metrics. For each, characterize its current (un-pressured)       |
|      | correlation with the goal.                                                      |
|    3 | For each candidate, pre-mortem under heavy incentive: how would agents          |
|      | optimize this metric in ways that don't move the goal?                          |
|    4 | Classify the predicted failure: regressional / extremal / causal / adversarial. |
|    5 | Design counter-pressures for the predicted failure mode (multiple metrics,     |
|      | guardrails, audits, randomization, decoupling incentive from metric).          |
|    6 | If no counter-pressure is sufficient to keep the metric tracking the goal      |
|      | under expected pressure, re-design. Sometimes this means a new construct,      |
|      | sometimes weaker incentive on this metric.                                      |
|    7 | Schedule audits: validate the metric-goal correlation periodically *with        |
|      | incentive in place*. Drift means Goodhart is winning.                           |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
GOODHART AUDIT WORKSHEET

    Goal (the construct we care about): __________________________________
    Candidate metric:                    __________________________________

    Current metric-goal relationship (un-pressured):
      Correlation strength:              _________________________________
      Mechanism:                         _________________________________

    INCENTIVE PRE-MORTEM
      Imagine agents with this metric in compensation / promotion / resource
      allocation. How would they push the metric without moving the goal?

      Hypothesis 1: ___________________________________________________
      Hypothesis 2: ___________________________________________________
      Hypothesis 3: ___________________________________________________

    GOODHART TYPE (Manheim & Garrabrant taxonomy)

      [ ] REGRESSIONAL — selecting top-N performers selects the noisiest, who
                         regress to the mean. (Common in performance ranking.)

      [ ] EXTREMAL    — relationship breaks at the extremes the optimizer pushes
                         toward; effects flip sign or saturate. (Common with
                         dose-response style metrics.)

      [ ] CAUSAL      — metric is correlated with goal but doesn't cause it;
                         pushing metric doesn't move goal. (Common with proxy
                         metrics like "engagement" → "success.")

      [ ] ADVERSARIAL — agents understand the metric and route around it via
                         techniques the metric doesn't capture. (Common with
                         binary or thresholded metrics; agents game the cutoff.)

    COUNTER-PRESSURES (match to type)

      For REGRESSIONAL:  larger sample sizes, multi-period averaging, shrinkage estimators.
      For EXTREMAL:      add guardrails on extremes; pair-with secondary metric that
                          captures the underlying goal directly.
      For CAUSAL:        require demonstrated causal lift, not just correlation;
                          re-validate periodically; replace if causal link weakens.
      For ADVERSARIAL:   multiple, redundant, hard-to-game-jointly metrics; spot
                          audits; randomization; broaden the construct-coverage.

    DESIGN DECISION
      [ ] Use this metric with these counter-pressures
      [ ] Use this metric without strong incentive (status only, not compensation)
      [ ] Replace with a different metric (specify): __________________________
      [ ] Combine with: ______________________________________________________

    AUDIT SCHEDULE
      Re-test metric-goal correlation under incentive: every ___ months
      If correlation drops below ____, redesign

CLASSIC GOODHART CASES (calibrate intuition)

    Example                                | Goodhart type | Failure mode
    ---------------------------------------|---------------|--------------------------
    Lines of code → productivity           | Causal        | More LoC, less productivity
    Customer-call resolution time          | Adversarial   | Hang up "resolved" early
    Hospital wait-time targets             | Adversarial   | Don't admit until ready
    Test scores → educational outcomes     | Causal/Adversarial | Teach to the test
    Bug count → quality                    | Adversarial   | Reclassify bugs as features
    Soviet nail factories (count or weight)| Extremal      | Tiny nails, then giant nails
    Cobra-killing bounty (Delhi)           | Adversarial   | Cobra farming
```

> **Operational notes:** Three disciplines. (1) Pre-mortem under incentive, not under casual observation. The question is not "is this metric correlated with the goal in current data?" — it's "what will it look like 6 months after incentive is attached?" (2) Match counter-pressures to predicted failure type. Throwing all four counter-pressures at every metric is over-engineering; identify the most likely failure mode and address it specifically. (3) Some constructs are too important to entrust to a single metric. For high-stakes objectives (quality, ethics, customer satisfaction), use *multiple* metrics drawing from different methods that would be hard to jointly game — closer to the multitrait-multimethod logic of construct validity. Fourth: schedule re-validation. The most insidious Goodhart failures are slow — the metric keeps "improving" while the underlying goal silently degrades over quarters. The audit is the only way to catch this in time. Fifth: be honest about acceptable Goodhart degradation. Some metrics are worth using even though they'll partially Goodhart-fail, because the alternative is no metric at all. Quantify how much degradation is acceptable, then commit to redesign at that threshold.
