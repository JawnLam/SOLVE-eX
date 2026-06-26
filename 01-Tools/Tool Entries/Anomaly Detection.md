---
Item_ID: tt-anomaly-detection
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Anomaly Detection
tt_Source: "Statistical process control (Shewhart 1924); operations research; expanded into ML literature (Chandola et al. 2009)"
tt_Type: instrument
tt_Domain: Non-discursive cognition
tt_Field: Pattern recognition & anomaly detection
tt_Operation: Categorize situation type
tt_Cross_Domains:
- Modes of inquiry
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Checklist
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Snap
- Single session
- Practice
tt_Lineage:
- Industrial / business
- Scientific method
tt_Posture:
- Beginner-friendly
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1, 4.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Abductive Inference
- Pre-Mortem
tt_Often_Follows:
- Pattern Recognition
tt_Pairs_Well_With:
- Abductive Inference
- Causal DAGs
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 03 edge-case resolution: tt_Cross_Domains: +Discursive-analytical (see /tmp/edge-case-decisions.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "The cognitive twin of pattern recognition: detecting *deviation* from expected. Shewhart's statistical process control (control charts) is the foundational artifact; the cognitive workflow generalizes to ops, security, finance, medicine, organizational signals."
Needs_Processing: false
AI_Instructions: ''
---

# Anomaly Detection

**One-line summary:** A workflow that surfaces meaningful deviations from a baseline expectation by making the baseline explicit, defining what counts as "different enough," and routing each anomaly to investigation, suppression, or template update.

**When to reach for it:** Operating any system that has a "normal" — production metrics, financial controls, inventory, network traffic, organizational health indicators — and you want early warning when something has shifted beyond noise.

---

## Purpose Of This Thinking Tool

Anomaly detection makes three usually-implicit decisions explicit: (1) what is the baseline, (2) what is the threshold for "anomalous," (3) what is the routing rule when an anomaly fires. The discipline is older than its modern statistical machinery — it descends from Shewhart's 1924 control charts at Bell Labs, the first formalization of "common-cause" vs. "special-cause" variation.

The non-obvious operational insight: most anomaly-detection failures are not about the detector. They're about the *baseline* (which drifts over time, often un-modeled), the *threshold* (set too tight → alert fatigue; too loose → missed signal), and the *routing* (an anomaly without a person and a playbook is just noise). A great detector inside a poorly designed pipeline produces nothing useful.

The cognitive workflow generalizes the statistical machinery: in security ("this login pattern is unusual"), finance ("this transaction is out-of-distribution"), operations ("this latency spike is special-cause"), organizations ("attrition in this team has shifted"), and medicine ("vitals trending"). Same workflow, different baselines.

## Why Use This Thinking Tool

Three patterns the explicit workflow prevents:

1. **Alert fatigue.** Thresholds set conservatively flood operators; they begin ignoring alerts; the one real anomaly is missed. The workflow forces explicit threshold-setting and tracking of false-positive rate.
2. **Baseline drift.** A static baseline becomes wrong as the system evolves; alerts misfire on changes that are now normal. The workflow includes a periodic baseline-refresh step.
3. **Anomaly-without-action.** A detector firing into a console nobody owns is purely decorative. The routing-rule step ensures every detector has a named owner, a playbook, and a feedback loop back into the baseline.

For consulting and operations work, the leverage is institutional: a working anomaly-detection pipeline is a multiplier on every team's situational awareness. A broken one degrades trust in *all* signals.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the signal: what variable is being watched, sampled at what frequency?   |
|    2 | Build a baseline expectation: a distribution, control chart, forecast, or       |
|      | learned model. Document its assumptions and validity window.                    |
|    3 | Choose an anomaly definition: σ-based threshold, percentile rule, change-point  |
|      | test, or model residual. Match the definition to the cost asymmetry.            |
|    4 | Estimate false-positive rate and miss rate from historical data BEFORE         |
|      | deployment. If rates aren't viable, redesign — don't ship.                     |
|    5 | Define the routing: who is paged, what playbook applies, what's the SLA?        |
|    6 | Add a feedback loop: each fired anomaly is labeled (true-positive / FP / new   |
|      | normal). Use labels to update baseline and threshold periodically.              |
|    7 | Re-validate the baseline on a cadence (monthly / quarterly). Drift is normal. |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
ANOMALY-DETECTION CANVAS

    Signal:                ____________________________________________
    Sampling frequency:    _________   Latency to detection target: _____

    BASELINE
      Method:  □ rolling mean ± kσ   □ control chart (Shewhart/EWMA/CUSUM)
               □ percentile-based    □ time-series forecast residual
               □ ML model (state which kind, why)
      Window:                _________
      Known seasonality:     _________________________________________
      Validity window:       _________________________________________
                             (when must this be re-fit?)

    ANOMALY DEFINITION
      Trigger:  __________________________________________________________
      Cost asymmetry:
        Cost of false positive:  _______________________________________
        Cost of missed signal:   _______________________________________
        Implication for threshold:  _____________________________________

    DEPLOYMENT METRICS (estimate from historical data BEFORE shipping)
      False-positive rate:   _________  (per ___ time period)
      Miss rate (estimated): _________
      Median time to detect: _________

    ROUTING
      Owner:        ____________________________________________________
      Playbook:     ____________________________________________________
      SLA:          ____________________________________________________
      Escalation:   ____________________________________________________

    FEEDBACK LOOP
      Each fired anomaly labeled:  □ true positive   □ false positive
                                   □ new normal (update baseline)
      Baseline re-validation cadence:  _________
      Threshold re-tuning cadence:    _________

THE FOUR STATES OF AN ANOMALY (the routing taxonomy)

    State                  | Action
    -----------------------|---------------------------------------------
    True positive, novel   | Investigate; update playbook; possibly file bug
    True positive, recurring| Apply existing playbook; check root cause
    False positive         | Tune threshold; document why fired
    "New normal" (drift)   | Update baseline; suppress; document the shift

COMMON BASELINES BY DOMAIN

    Domain                | Typical baseline method
    ----------------------|----------------------------------------------
    Manufacturing         | Shewhart control charts (X-bar, R, p, c)
    Web/system metrics    | Percentile-based, EWMA, anomaly-detection ML
    Finance / fraud       | Out-of-distribution scoring, rule-based + ML
    Network security      | Behavioral profiles, sequence models
    Org health            | Cohort attrition, eNPS deltas, manager skip-level
    Medical / vitals      | Patient-specific baselines, MEWS / NEWS scores
```

> **Operational notes:** The single highest-leverage move is owning false-positive rate as a *first-class* design constraint. A detector with 5% FP and 10 alerts/hour produces 12 false alarms a day — beyond any human attention budget. Either tighten the threshold (and accept misses), invest in suppression rules, or batch alerts. Second: baselines drift. Treat baseline maintenance as a recurring engineering cost, not a one-time setup. Third: the most dangerous failure mode is silent — a detector that no longer fires because the data pipeline broke upstream. Always run a "heartbeat" check that the detector is alive even when nothing's anomalous. Fourth: pair anomaly detection with the abductive-inference workflow — an anomaly without a hypothesis-generation step turns into "we saw a spike, IDK." Detection without diagnosis is half a system.
