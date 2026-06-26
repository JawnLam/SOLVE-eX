---
Item_ID: tt-calibration-training-drills
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Calibration Training Drills
tt_Source: "Lichtenstein, Fischhoff & Phillips 1982 (calibration of probabilities); Hubbard 2014 (How to Measure Anything); Good Judgment Project training protocols"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Calibration & epistemic humility
tt_Operation: Aggregate parallel judgments
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Practice / ritual
- Sequenced workflow
tt_Scale:
- Solo
- Small group
tt_Duration:
- Practice
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
- Solo-quiet
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
- Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Tetlock Superforecasting
tt_Often_Follows: []
tt_Pairs_Well_With:
- Brier Scoring
- Tetlock Superforecasting
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition', 'Risk / uncertainty']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Demonstrably learnable in 4-8 hours of structured practice (Hubbard). 90% confidence intervals are the canonical drill: subject states a 90% CI for an unknown quantity; over many questions, ~90% should contain the truth. Most untrained people are ~50%."
Needs_Processing: false
AI_Instructions: ''
---

# Calibration Training Drills

**One-line summary:** Structured practice that teaches subjects to produce well-calibrated probability estimates and confidence intervals — drilling against questions with known answers, scoring, and feedback until stated confidence matches actual hit rate.

**When to reach for it:** Onboarding decision-makers who'll be asked to express probabilistic forecasts, before any major forecasting effort, or as periodic re-calibration for teams that produce quantified estimates routinely.

---

## Purpose Of This Thinking Tool

Untrained estimators are systematically overconfident. When asked for a "90% confidence interval" for an unknown quantity, untrained subjects' intervals contain the true answer only ~40–50% of the time, not 90%. This is a *calibration* failure: the stated confidence doesn't match the actual hit rate.

The good news is that calibration is teachable. Hubbard's research (and the Good Judgment Project's findings) show that 4–8 hours of structured practice reliably produces calibrated estimators. The training works by tightening the loop between estimate, scoring, and feedback — subjects learn what their own 90% genuinely feels like by being scored on many trials.

The non-obvious operational insight: calibration training is not about *more* knowledge; it's about more *honest* expression of uncertainty. Trained subjects don't suddenly know more facts — they learn to widen intervals when they're uncertain rather than anchoring on a confident-sounding range. The drills work because they make the cost of overconfidence (a "miss" — interval doesn't contain truth) tangible and frequent.

## Why Use This Thinking Tool

Three failure modes calibration training prevents:

1. **Anchored overconfidence in forecasts.** Untrained subjects under-express uncertainty; downstream decisions are made on unreliably narrow ranges.
2. **Cargo-culted point estimates.** Without training, "give me a number" produces overconfident point estimates rather than honest distributions.
3. **Mismatched team calibration.** A team where one person is well-calibrated and others aren't produces forecasts that mix incompatible confidence semantics.

For consulting and decision support, putting decision-makers (and analysts) through calibration training before high-stakes forecasting is one of the highest-leverage analytical investments — small time, large effect, durable.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Establish baseline: 20–40 trivia/general-knowledge questions with numeric        |
|      | answers. Subject states a 90% CI for each.                                      |
|    2 | Score: count how many CIs actually contained the truth. Target = 90%; baseline |
|      | typically 40–60%.                                                               |
|    3 | Introduce the discipline: when uncertain, widen the interval until you'd take  |
|      | a fair bet that it contains truth. The "equivalent bet" test (Hubbard).        |
|    4 | Run a second batch (different questions). Re-score.                            |
|    5 | Add 50% confidence intervals (narrower); subject should hit 50% of these.       |
|    6 | Drill to consistency: 90% CIs should hit ~90%, 50% CIs should hit ~50%, etc.   |
|    7 | Transfer to domain-specific questions: forecast questions in the work          |
|      | domain. Score against actuals over time.                                       |
|    8 | Schedule periodic re-calibration. Skill decays without practice (months, not  |
|      | days).                                                                          |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
CALIBRATION DRILL TEMPLATE

    Drill set: __________________________   Date: __________
    Subject:   __________________________   Confidence level (90%, 50%, etc.): ____

    Question                                | Lower | Upper | Truth | Hit?
    ----------------------------------------|-------|-------|-------|------
    1.                                      |       |       |       |
    2.                                      |       |       |       |
    ...
    20.                                     |       |       |       |

    Hit rate: ___ / 20 = _____%
    Target:                          90%

    DIAGNOSIS BY HIT RATE
      40–60%: severely overconfident — widen intervals dramatically
      60–80%: moderately overconfident — widen ~50%
      80–95%: calibrated; continue practice
      < 40% or > 95% (in opposite direction): something other than calibration

EQUIVALENT-BET TEST (Hubbard)

    For each estimate, ask yourself:
      "Would I rather take this bet:
        (A) win $10,000 if my interval contains the truth, $0 otherwise
        (B) win $10,000 with 90% probability via a clearly-90% mechanism (10-card
            deck where 9 cards win)?"
      If A and B feel equally attractive → interval is genuinely calibrated at 90%.
      If A feels worse  → interval is too narrow; widen.
      If A feels better → interval is too wide; tighten.

CALIBRATION CURVE (post-training assessment)

      Stated confidence  | Actual hit rate
      -------------------|-----------------
      50%                |
      70%                |
      90%                |
      99%                |

      Plot stated vs. actual on a 45° reference line. Calibrated → on the line.
      Above line → underconfident.  Below line → overconfident.

DOMAIN-TRANSFER PROTOCOL

    After general-knowledge drills, drill on:
      • Estimates of past project metrics (pre-known answer for scoring)
      • Predictions for outcomes resolving in 2–8 weeks
      • Probability forecasts on binary questions with verifiable resolution
    Score; recalibrate.

DECAY SCHEDULE
    • Initial training: 4–8 hours over 2–3 sessions
    • Re-drill: 30 minutes monthly for first 6 months
    • Maintenance: 30 minutes quarterly thereafter
```

> **Operational notes:** Three disciplines. (1) Use the equivalent-bet test routinely. It's the single most effective in-the-moment calibration check — far better than abstract reasoning about "is 90% right?" The bet framing engages the loss-aversion machinery that uncovers true beliefs. (2) Don't skip the score-and-feedback step. People learn calibration by experiencing the *gap* between stated and actual hit rate — a single drill set without scoring is wasted. (3) Calibration is a *habit*, not a one-time skill. It decays without practice. Schedule periodic re-drills the same way you'd schedule fire drills — calendar-driven, not event-driven. Fourth: domain transfer is real. Calibration on trivia transfers ~70% to domain forecasting; the remaining 30% requires domain-specific drilling. For high-stakes work (medical, financial, policy), drill on domain-relevant questions where ground truth is eventually knowable. Fifth: in teams, run group drills. Public scoring de-stigmatizes overconfidence and surfaces who needs more practice.
