---
Item_ID: tt-brier-scoring
Item_Prototype: Thinking_Tool
Title: Brier Scoring
tt_Source: "Glenn W. Brier 1950 (Verification of Forecasts Expressed in Terms of Probability)"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Calibration & epistemic humility
tt_Operation: Score and rank options
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Algorithm
- Scoring rubric
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Practice
tt_Lineage:
- Mathematical / formal
- Scientific method
tt_Posture:
- Beginner-friendly
- Solo-quiet
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
- Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows:
- Tetlock Superforecasting
- Calibration Training Drills
tt_Pairs_Well_With:
- Tetlock Superforecasting
- Calibration Training Drills
- Bayesian Updating
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition', 'Risk / uncertainty']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Brier score = mean squared error of probability forecasts. Lower is better. Range 0 (perfect) to 1 (worst possible). The proper scoring rule that incentivizes honest probability statements; can be decomposed into calibration and resolution components (Murphy 1973)."
Needs_Processing: false
AI_Instructions: ''
---

# Brier Scoring

**One-line summary:** A proper scoring rule for probability forecasts: the mean squared error between forecast probability and the binary outcome (0 if didn't happen, 1 if it did) — lower is better, and only honest forecasts minimize it.

**When to reach for it:** Closing the loop on any probabilistic forecasting practice — scoring forecasters, comparing forecast methods, training calibration, evaluating prediction-market participants.

---

## Purpose Of This Thinking Tool

Brier scoring is the canonical accountability mechanism for probability forecasts. After resolution, you compute the squared difference between the forecast probability p and the realized outcome (0 or 1). Average over many forecasts; lower scores indicate better forecasts. The score has the *proper* property: a forecaster minimizes their expected score by reporting their honest probability — not by hedging, not by extreme positions.

The non-obvious operational insight is the **decomposition** (Murphy, 1973): Brier score = Reliability − Resolution + Uncertainty. *Reliability* (calibration) measures how well stated confidence matches actual frequencies. *Resolution* measures how much forecasts vary from the base rate (a forecaster who always says 50% has zero resolution). *Uncertainty* is the irreducible variance of the events. A great forecaster has low reliability error (calibrated), high resolution (forecasts confidently when justified), and accepts the irreducible uncertainty.

Used by IARPA tournaments, Good Judgment Project, Metaculus, weather services (where it originated, with Brier in 1950), and increasingly in product/business forecasting where outcomes are recordable.

## Why Use This Thinking Tool

Three failure modes Brier scoring closes:

1. **Forecasts without accountability.** Untracked forecasts cannot improve. Brier provides the metric.
2. **Hedging via verbal fuzziness.** Without numeric forecasts and Brier, forecasters drift to vague language ("likely") that isn't scoreable.
3. **Comparing apples to oranges.** Brier provides a common scale for comparing forecasters across different question sets — with reservations about resolution and base-rate effects.

For consulting and forecasting work, instituting Brier scoring is the institutional move that turns forecasting from intuition-driven to learning-driven. Within a few quarters, scored forecasters improve measurably.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the question with clear resolution criteria and date.                    |
|    2 | Forecaster states probability p (between 0 and 1) of the question resolving YES.|
|    3 | At resolution, record outcome o ∈ {0, 1}.                                       |
|    4 | Compute Brier score for that forecast: B = (p − o)².                            |
|    5 | For multi-class outcomes (3+ categories): B = Σ_i (p_i − o_i)², where o_i is    |
|      | 1 for the realized class and 0 otherwise.                                       |
|    6 | Average across many forecasts to get the forecaster's mean Brier score.         |
|    7 | Decompose into reliability (calibration), resolution, uncertainty for diagnosis.|
|    8 | Compare to a naive baseline (always-base-rate) and to peer forecasters.        |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
BRIER SCORE — THE FORMULA

    Binary outcome:  B = (p − o)²    where p ∈ [0,1], o ∈ {0,1}
                     range: 0 (perfect) to 1 (worst — predicted 0 and it happened, or vice versa)

    Multi-class:     B = Σ (p_i − o_i)²

    Mean Brier over N forecasts:  B̄ = (1/N) Σ B_i

REFERENCE BENCHMARKS

    Score          | Interpretation
    ---------------|--------------------------------------------------------
    0.00           | Perfect (all 0% or 100% forecasts, all correct)
    0.10           | Excellent — Good Judgment Project superforecaster range
    0.20           | Good — typical informed forecaster
    0.25           | Naive baseline — always predict 50%
    0.30+          | Poor — worse than always-50%
    0.50+          | Anti-correlated — confident in wrong direction

DECOMPOSITION (Murphy 1973)

    B = Reliability − Resolution + Uncertainty

      Reliability (lower better) — calibration error.
        Compute by binning forecasts; in each bin, stated p vs. observed frequency.
      Resolution (higher better) — how much forecasts vary from the base rate.
        A forecaster who always says 50% has resolution 0; a confident-and-correct
        forecaster has high resolution.
      Uncertainty — the variance of outcomes given the base rate; irreducible.

DIAGNOSTIC TABLE

      Symptom in Brier           | Likely cause                        | Fix
      ----------------------------|-------------------------------------|---------------------
      High reliability error      | Mis-calibrated (over/underconfident)| Calibration drills
      Low resolution              | Hedging — always near base rate     | Encourage confident
                                  |                                     | predictions when justified
      High uncertainty            | Inherently random domain            | Accept the floor; check
                                  |                                     | if domain is forecastable

SCORING SHEET

      ID | Question                  | Forecast p | Outcome o | Brier (p−o)²
      ---|---------------------------|------------|-----------|--------------
       1 |                           |            |           |
       2 |                           |            |           |
       N |                           |            |           |
                                                       Mean Brier:

FORECASTER LEADERBOARD (with caveats)

      Forecaster | N | Mean Brier | vs. baseline (0.25) | Calibration error
      -----------|---|------------|---------------------|------------------
      A          |   |            |                     |
      B          |   |            |                     |

      Caveat: Brier is sensitive to the question set. Compare forecasters only
      on the SAME questions, or use scaled-Brier (Brier skill score).
```

> **Operational notes:** Three disciplines compound the value. (1) Always compute against a baseline (always-base-rate or always-50%). A raw Brier of 0.18 sounds bad until you see baseline is 0.25 — then it's 30% better than baseline, which is meaningful. The Brier *skill score* = 1 − (B / B_baseline) makes this explicit. (2) Decompose. A high-Brier forecaster who's well-calibrated but hedges (high reliability, low resolution) needs different feedback than a confident-but-wrong forecaster (low reliability, possibly negative resolution contribution). The decomposition tells you which. (3) Compare on the same question set. Cross-comparing forecasters who answered different questions is unreliable — easier questions yield lower scores. For fair comparison, use only overlapping questions or a Brier skill score against the same baseline. Fourth: bin forecasts to assess calibration. Forecasts in the 60–70% bin should be right ~65% of the time; if they're right 50% of the time, that bin is overconfident. Bin-level diagnosis is more actionable than aggregate Brier.
