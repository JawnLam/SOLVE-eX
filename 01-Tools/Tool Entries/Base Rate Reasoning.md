---
Item_ID: tt-base-rate-reasoning
Item_Prototype: Thinking_Tool
Title: Base Rate Reasoning
tt_Source: "Kahneman & Tversky 1973 'On the psychology of prediction'; reference-class forecasting (Flyvbjerg)"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Heuristic
- Sequenced workflow
tt_Scale:
- Solo
- Small group
tt_Duration:
- Snap
- Single session
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Risk / uncertainty
- Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Bayesian Updating
- Expected Value Decision Trees
tt_Often_Follows: []
tt_Pairs_Well_With:
- Bayesian Updating
- Pre-Mortem
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Risk / uncertainty', 'Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "The discipline of starting any forecast or judgment from the base rate of similar cases — i.e., 'reference-class forecasting' (Kahneman/Flyvbjerg). The single highest-leverage move against optimism bias and the planning fallacy."
Needs_Processing: false
AI_Instructions: ''
---

# Base Rate Reasoning

**One-line summary:** Anchor any forecast or estimate to the historical base rate of a relevant reference class of similar cases — and adjust from there only on the strength of specific evidence.

**When to reach for it:** Project timelines, M&A success forecasts, hiring decisions, startup outcomes, drug-trial probabilities, IPO returns — any situation where similar cases have been observed and recorded.

---

## Purpose Of This Thinking Tool

The "outside view," in Kahneman's terminology: instead of building up a forecast from the inside (modeling your specific situation), you find a reference class of similar past cases and start from their distribution. The base rate is the prior; specific features of your case become evidence that may or may not justify deviating from it.

The non-obvious operational insight: people are systematically overconfident on the inside view. Project planners imagine the project unfolding successfully and arrive at an aggressive timeline; M&A teams highlight what's special about *this* deal. The outside view asks the un-flattering question: "Of all projects/deals/launches that looked like this one going in, what fraction came in on time / hit expectations / succeeded?" That number is almost always less optimistic than the inside view's number.

Reference-class forecasting (Bent Flyvbjerg's formalization for infrastructure projects) operationalizes this: pick a reference class, get the actual outcome distribution, anchor the forecast there, and adjust only with specific evidence that distinguishes your case. Adopted by McKinsey, the UK Treasury (Green Book), and increasingly in venture capital screening.

## Why Use This Thinking Tool

Three failure modes base-rate reasoning prevents:

1. **Inside-view optimism.** Without an outside view, forecasts assume modal-best execution. The base rate captures actual delivery.
2. **Vivid evidence overweighting.** A single dramatic case ("I've seen this work") dominates intuition. The base rate forces the comparison to *all* cases, not the memorable ones.
3. **Reference-class denial.** "This time is different" is sometimes true and usually wrong. The discipline forces an explicit defense: which features make the case different, and how would those features have predicted deviation in past cases?

For consulting and policy work, this is the antidote to the planning fallacy. It also exposes deals/projects that *only* work under inside-view assumptions, which is itself diagnostic.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the question: what specifically are you trying to forecast?              |
|    2 | Identify a reference class — historical cases similar enough to be informative. |
|      | Aim for ≥10 cases; quality of match beats quantity.                             |
|    3 | Gather the actual outcome distribution: median, range, and tail.                |
|    4 | Anchor your forecast at the reference-class median (or full distribution).      |
|    5 | List specific features of your case that differ from the reference class.       |
|    6 | For each, ask: would this feature have shifted past cases' outcomes? By how much?|
|    7 | Adjust the base rate by the *justified* amount, not the gut-felt amount.        |
|    8 | Document: reference class, base rate, adjustments, final forecast. The audit   |
|      | trail is the deliverable.                                                       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
REFERENCE-CLASS FORECASTING WORKSHEET

    Question: ________________________________________________________________

    REFERENCE CLASS
      Definition (what makes a case "similar"?): __________________________
      Number of cases in class: ________
      Source of data:           ________________________________________

    BASE RATE DISTRIBUTION (for the outcome of interest)
      Median:                 ________
      25th / 75th percentile: ________ / ________
      Range:                  ________ to ________
      Tail behavior:          ________________________________________

    INSIDE-VIEW ESTIMATE (what would you have said without the base rate?)
      Estimate:               ________
      Difference from median: ________  (← this is your optimism delta)

    ADJUSTMENTS (each must be justified by past-case evidence)
      Feature                 | Adjustment | Justification
      ------------------------|------------|----------------------------------
                              |            |
                              |            |

    FINAL FORECAST = base-rate-median + adjustments = ________

    REFERENCE-CLASS HEALTH CHECKS
      [ ] ≥10 cases in class
      [ ] Class chosen *before* looking at outcome — not gerrymandered to support a number
      [ ] Outcome data verified, not estimated from memory
      [ ] Adjustments could be defended in writing to a skeptical reviewer

EXAMPLE BASE RATES (memorize a few — they anchor lots of decisions)

    Domain                                   | Base rate (typical)
    -----------------------------------------|------------------------
    Software project on-time delivery        | ~20–40% on time / on budget
    Major IT projects within 10% of estimate | ~7%
    M&A deals create value for acquirer     | ~30–50%
    VC-backed startup returns 1×+            | ~30%
    VC-backed startup returns 10×+           | ~5%
    Drug enters Phase I → reaches market     | ~10–15%
    Major infrastructure projects on budget  | ~10–20% (Flyvbjerg)
    Strategic plan executed as written       | ~30%
```

> **Operational notes:** The single strongest move is *picking the reference class before looking at outcomes*. People who pick the class after seeing the distribution will gerrymander toward the answer they wanted. Define the class on independent criteria — type of project, scale, sector, team size — then accept whatever distribution comes out. Second: never adjust the base rate by more than 30–40% on the inside view's strength alone; if your case is "really different," the burden of proof is to show *which* differing feature, how it predicted past deviations, and by how much. Third: when a stakeholder objects "but our case is different," ask "which 3 features make it different, and what's the past evidence those features matter?" If they can't answer, the inside-view claim collapses. Fourth: small reference classes (n<10) are noisy; use distribution-of-medians or bootstrap to get a sense of the uncertainty. Fifth: reference-class forecasting is also a *political* tool — it depersonalizes a forecast that would otherwise read as criticism of the team's plan.
