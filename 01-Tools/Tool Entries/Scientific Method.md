---
Item_ID: tt-scientific-method
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Scientific Method (RCTs / A-B Testing)
tt_Source: "Bacon 1620 (Novum Organum); Mill 1843; Fisher 1925 (Statistical Methods); modern A/B testing Kohavi & Tang 2020"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Run experimental cycle
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Algorithm
tt_Scale:
- Small group
- Organizational
tt_Duration:
- Project
tt_Lineage:
- Scientific method
- Industrial / business
tt_Posture:
- Beginner-friendly
- Expert-required
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
- Sensitivity Analysis
- Bayesian Updating
tt_Often_Follows:
- Pre-registered Predictions
tt_Pairs_Well_With:
- Causal DAGs
- KPI Design
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
Quick_Notes: "RCTs (Fisher's randomization) and A/B tests (controlled-experiment descendants) are the same logical structure: random assignment to treatment vs. control, pre-specified outcome, statistical test. The discipline is in the *pre-specification* and the *power calculation* before the data arrives."
Needs_Processing: false
AI_Instructions: ''
---

# Scientific Method (RCTs / A-B Testing)

**One-line summary:** Randomly assign units to treatment vs. control, intervene on the treatment, measure a pre-specified outcome, and use a pre-specified statistical test to estimate the causal effect.

**When to reach for it:** Any time you need a *causal* claim ("X causes Y") rather than a correlational one, you can randomize the intervention, and the outcome can be measured with reasonable signal-to-noise.

---

## Purpose Of This Thinking Tool

The randomized controlled trial — and its product-development twin, the A/B test — is the gold standard for causal inference because randomization breaks confounding. If you randomize who gets treatment, then on average the treatment group and control group are identical at baseline; any post-intervention difference is attributable to the intervention.

The non-obvious operational insight is that *most of the rigor lives in pre-specification*, not in the analysis. You commit, before any data arrives, to: the precise outcome metric, the statistical test, the sample size (via power calculation), the stopping rule, the subgroups you'll analyze, and the success threshold. Without pre-specification, the same data can be sliced many ways until *something* looks significant — the "garden of forking paths" / "p-hacking" failure mode that has destroyed credibility in social science and product analytics alike.

Bacon (1620) named the inductive method; Mill (1843) formalized its inferential logic; Fisher (1925) added randomization, blocking, and significance testing; the modern A/B test inherits all of this and adds operational concerns: experiment infrastructure, traffic allocation, telemetry quality, and organizational learning loops.

## Why Use This Thinking Tool

Three failure modes the disciplined version prevents:

1. **Correlation-as-causation.** Without randomization, observed differences could reflect selection bias. The RCT/AB structure neutralizes this.
2. **Garden of forking paths.** Without pre-specification, post-hoc analysis finds "significant" results by chance. Pre-spec freezes the analysis plan before the data exists.
3. **Underpowered tests.** Without a power calculation, a "null result" might mean "no effect" or "we couldn't have detected an effect this size." Power calc forces honesty about detectable-effect floor.

For product, marketing, and policy work, RCTs/AB tests are the highest-quality evidence available — and increasingly tractable as instrumentation improves. They also enforce humility: most well-designed experiments produce smaller effects than founders/designers expect, and that calibration is itself the long-term value.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the causal hypothesis: "X causes Y." Be specific about X (the           |
|      | intervention), Y (the outcome), and the population of units.                    |
|    2 | Pre-specify: outcome metric, test statistic, alpha level, sample size,         |
|      | stopping rule, subgroups, multiple-comparison adjustment.                       |
|    3 | Power calculation: given expected effect size, what N is needed for ≥80% power?|
|      | If N is infeasible, rethink — small experiments can't reliably detect small    |
|      | effects.                                                                        |
|    4 | Randomly assign units to treatment / control. Verify balance on baseline       |
|      | covariates as a sanity check (NOT as license for adjustment).                   |
|    5 | Run the experiment without peeking. Honor the stopping rule.                   |
|    6 | Analyze per the pre-spec. Report effect size, confidence interval, and the     |
|      | pre-specified test result.                                                      |
|    7 | Distinguish primary outcome (success criterion) from exploratory analyses      |
|      | (hypothesis-generating only).                                                   |
|    8 | Replicate before scaling. A single significant result is suggestive; two are   |
|      | meaningfully more credible.                                                     |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
PRE-REGISTRATION TEMPLATE (fill before launch)

    Hypothesis (one sentence): _____________________________________________________

    Population:                _____________________________________________________
    Intervention (treatment):  _____________________________________________________
    Comparison (control):      _____________________________________________________
    Outcome (Y) — primary:     _____________________________________________________
    Outcome — secondary:       _____________________________________________________
    Outcome — exploratory:     _____________________________________________________  (analysis-only; no claim)

    DESIGN
      Randomization unit (user / session / cohort / cluster): __________
      Allocation ratio (50/50 or other):                       __________
      Duration / N target:                                     __________
      Blinding (single / double / open):                       __________

    POWER CALCULATION
      Minimum detectable effect (MDE):    ________
      Baseline rate / variance:           ________
      α (false-positive rate):            ________  (typically 0.05)
      Power (1 − β):                      ________  (typically 0.80)
      Required N:                         ________

    ANALYSIS PLAN
      Test statistic:                    ____________________________________
      Multiple-comparison adjustment:    ____________________________________
      Subgroups (pre-specified only):    ____________________________________
      Stopping rule:                     ____________________________________
      Success threshold (decision rule): ____________________________________

QUALITY-CONTROL CHECKS (run before believing a result)

      [ ] Sample-ratio mismatch (SRM)? Treatment / control assignment ratio differs
          from designed ratio → randomization is broken; do not trust the result.
      [ ] Telemetry sanity? Pre-period A/A test (no intervention) should show ≈0 effect.
      [ ] Novelty / primacy effects? Effect curves over time should stabilize.
      [ ] Heterogeneous treatment effects? Subgroup analysis is hypothesis-generating
          unless pre-specified.

INFERENCE WORKSHEET

      Pre-specified test on primary outcome:       _____________
      Effect estimate:                              _____________
      95% CI:                                       _____________
      Interpretation:
        □ Effect is significant AND practically meaningful  → consider scaling
        □ Effect is significant but small                   → ROI check
        □ CI includes zero                                  → no detectable effect
        □ Underpowered: cannot rule out a real effect       → re-run larger
```

> **Operational notes:** Three disciplines compound the value. (1) Power calculation is non-negotiable. Most "failed" A/B tests are actually underpowered — the test couldn't have detected the realistic effect, regardless of whether one exists. Compute N before launching; if N is infeasible, redesign the experiment or accept that this question can't be answered this way. (2) Sample-ratio mismatch is the #1 silent killer. If you allocated 50/50 but the data shows 49/51, randomization is broken (often because of a downstream filter), and the entire result is suspect. Always check SRM before any other analysis. (3) Distinguish primary from exploratory outcomes ruthlessly. Exploratory subgroup analysis is fine for hypothesis generation but NEVER as the basis for "we found a winning treatment in segment X" — that requires a fresh confirmatory experiment. Fourth: replication before scaling. The literature on "replicated A/B tests at scale" (Microsoft, Google, Booking) shows that ~30–50% of significant single-experiment effects don't replicate. Treat the first significant result as suggestive; ship only after replication.
