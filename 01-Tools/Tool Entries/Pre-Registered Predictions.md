---
Item_ID: tt-pre-registered-predictions
Item_Prototype: Thinking_Tool
Title: Pre-Registered Predictions
tt_Source: "Pharmaceutical clinical trials (clinicaltrials.gov, 2000); psychology Open Science Framework (Brian Nosek, 2013); Tetlock's IARPA tournaments"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Run experimental cycle
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Practice / ritual
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Project
- Practice
tt_Lineage:
- Scientific method
- Industrial / business
tt_Posture:
- Beginner-friendly
- Adversarial-tolerant
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
tt_Often_Precedes: []
tt_Often_Follows:
- Popper Falsifiability
tt_Pairs_Well_With:
- Popper Falsifiability
- Brier Scoring
- Scientific Method
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human', 'Human group'], tt_About=['Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "The institutional move that turns falsifiability into reality: write down your prediction (and analysis plan) BEFORE the data, time-stamp it, share it. Defeats hindsight bias, p-hacking, garden-of-forking-paths, and motivated revisionism."
Needs_Processing: false
AI_Instructions: ''
---

# Pre-Registered Predictions

**One-line summary:** A practice of writing down hypotheses, predictions, and analysis plans *before* data arrives and time-stamping the record — converting "we predicted this would happen" from a memory-laundering claim into a verifiable one.

**When to reach for it:** Before any test, study, or strategic bet whose outcome you'll later want to learn from. Especially powerful for forecasting practices, A/B test design, post-mortem rigor, and any context where motivated reasoning could otherwise rewrite history.

---

## Purpose Of This Thinking Tool

Pre-registration solves a class of problems that all stem from the same defect: humans are unable to faithfully recall what they predicted before an outcome was known. Hindsight bias makes us remember our predictions as closer to the actual outcome than they were. The garden of forking paths permits an analyst to find a "predicted" pattern in any rich dataset by exploring enough subgroups. Motivated revisionism converts "we got it wrong" into "we anticipated this complication."

The non-obvious operational insight: pre-registration is *cheap* relative to its leverage. A 10-minute write-up at the start of a project — what we predict, what data we'll collect, what analysis we'll run, what decision we'll make — buys structural defense against most retrospective distortions. The discipline is the time-stamping (so the document genuinely existed before the outcome) and the no-edit rule (you can add to it, but you don't revise the original prediction).

The practice originated in pharmaceutical trials (1990s, mandatory for many drugs by 2000), spread to psychology through Brian Nosek and the Open Science Framework, and is now standard across forecasting communities. In business contexts, it's slowly entering as a tool against the chronic problem of "we knew that all along."

## Why Use This Thinking Tool

Three failure modes pre-registration prevents:

1. **Hindsight bias.** Without a written record, teams remember predictions as closer to outcomes than they were. Pre-reg preserves the actual prior belief.
2. **P-hacking / forking paths.** Without a pre-specified analysis plan, post-hoc subgroup analysis finds "significant" results by chance. Pre-reg locks the analysis.
3. **Reframing failures as foresight.** "We were always concerned about X" cannot be supported if the pre-registered document said otherwise.

For consulting, strategy, and forecasting work, pre-registration is the single highest-leverage discipline for organizational learning. Without it, lessons drift; with it, they accumulate against an objective record.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Before launch, write a structured pre-registration document covering: question, |
|      | hypothesis, predictions, data sources, analysis plan, decision rule.            |
|    2 | Time-stamp the document. Email it to a witness, commit it to a versioned       |
|      | repository, or use a pre-registration platform (OSF, AsPredicted, internal).    |
|    3 | Make the document immutable for the original prediction. Additions are fine    |
|      | (with their own time stamps); revisions of the original prediction are not.    |
|    4 | Run the experiment / project / forecast as planned.                            |
|    5 | At resolution, analyze per the pre-spec. Compare prediction to outcome.        |
|    6 | Document what was learned. Distinguish pre-registered findings from exploratory.|
|    7 | If exploratory analyses find something interesting, frame as hypothesis-       |
|      | generating, not confirmatory — and pre-register a follow-up to confirm.        |
|    8 | Periodically audit: do pre-registered predictions and outcomes match your       |
|      | retrospective narratives? Where they diverge, retrospective is wrong.           |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
PRE-REGISTRATION TEMPLATE

    Document ID: ________________________  Time-stamped at: ____________________
    Authors:     ________________________  Witnesses: ___________________________

    QUESTION
      We are trying to learn: __________________________________________________

    HYPOTHESIS / PREDICTION
      Primary hypothesis:                  __________________________________
      Quantitative prediction (numeric):   __________________________________
      Confidence interval (90% CI):        __________________________________
      Alternative hypothesis:              __________________________________

    DATA & MEASUREMENT
      Data source(s):                      __________________________________
      Population / sample:                 __________________________________
      Outcome measure (precise):           __________________________________
      Time horizon:                        __________________________________

    ANALYSIS PLAN
      Statistical test / decision rule:    __________________________________
      Significance level (if applicable):  __________________________________
      Pre-specified subgroups:             __________________________________
      Multiple-comparison correction:      __________________________________
      Stopping rule:                       __________________________________

    DECISION RULE (what we'll do based on outcome)
      If [outcome A]: we will [_________________________]
      If [outcome B]: we will [_________________________]
      If [outcome C]: we will [_________________________]

    ROBUSTNESS / FALSIFICATION
      What outcome would falsify the primary hypothesis?  __________________
      What alternative explanations would be consistent with falsification? _

    SIGNATURE
      Authors sign-off:  _____________________________________________________
      Witness sign-off:  _____________________________________________________
      Date / time:       _____________________________________________________

POST-RESOLUTION ADDENDUM (added after outcome, separately)

      Outcome observed:                    __________________________________
      Match to prediction:                 □ confirmed  □ refuted  □ inconclusive
      Lessons learned (pre-registered):    __________________________________
      Exploratory findings (separate; not  __________________________________
        claimed as confirmed):
      Follow-up pre-registrations needed:  __________________________________

LIGHTWEIGHT VERSIONS (when full template is overkill)

      One-line: "By [date], we predict [outcome] with [X%] confidence. If
                wrong, we will [action]." — emailed to a colleague, time-stamped.

      Three-line forecast: question, numeric forecast, decision rule.
      Logged in a shared spreadsheet with dated entries.
```

> **Operational notes:** Three disciplines. (1) Time-stamping is non-negotiable. The document's defensive value depends on being able to prove it existed before the outcome. Email-to-self, version-controlled commit, or platform pre-registration all work; sticky notes don't. (2) Distinguish confirmatory from exploratory in every report. Pre-registered analyses produce confirmatory findings; everything else is exploratory and should be labeled as such. The label discipline survives the meeting; the verbal qualifier doesn't. (3) Make pre-registration the path of least resistance. A 10-line lightweight template that everyone uses beats a 200-line gold-standard template that nobody fills out. For routine forecasts, a shared spreadsheet with dated entries is enough; reserve the full template for studies / launches / strategic bets. Fourth: when pre-registered predictions fail, that's the moment to learn — but motivated reasoning will hijack the post-mortem unless the pre-reg is in front of you. Read the original document aloud at the post-mortem; the discipline is anchoring on what was actually predicted, not on retrospectively-constructed reasonableness.
