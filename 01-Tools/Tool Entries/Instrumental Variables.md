---
Item_ID: tt-instrumental-variables
Item_Prototype: Thinking_Tool
Title: Instrumental Variables
tt_Source: "Philip Wright 1928 (corn-and-hog price identification); modern formalization Angrist & Imbens 1990s"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Causal & diagnostic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Algorithm
- Matrix
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Project
tt_Lineage:
- Mathematical / formal
- Scientific method
tt_Posture:
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows:
- Causal DAGs
tt_Pairs_Well_With:
- Causal DAGs
- Sensitivity Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Identifies causal effects in the presence of unmeasured confounding by exploiting a variable Z that affects the treatment X but has NO other path to the outcome Y. The exclusion restriction is untestable from data alone — it must be defended on substantive grounds."
Needs_Processing: false
AI_Instructions: ''
---

# Instrumental Variables

**One-line summary:** A causal-inference technique that recovers the effect of X on Y in the presence of unmeasured confounders by using a third variable Z that affects X but reaches Y *only through* X.

**When to reach for it:** When randomization isn't possible, the treatment of interest is confounded by unobserved variables, but a "natural experiment" exists — a policy change, a lottery, a rule discontinuity — that nudges some people into treatment but is otherwise unrelated to the outcome.

---

## Purpose Of This Thinking Tool

Most observational data are riddled with unmeasured confounders, and standard regression cannot identify a causal effect through them. Instrumental Variables (IV) sidesteps this by finding a variable Z that has *exactly one* causal route to the outcome — through the treatment X. Z's effect on Y is then necessarily transmitted via X, and the causal effect of X on Y is recovered as the ratio of Z's effect on Y to Z's effect on X.

The non-obvious move is the *exclusion restriction*: Z affects Y only through X. This restriction cannot be verified from the data; it must be argued on substantive grounds (legal, biological, institutional). This is what makes IV both powerful and fragile — a weak or invalid instrument produces estimates that look like causal effects but are not.

The technique was invented by Philip Wright in 1928 for agricultural economics (using weather as an instrument for supply to identify demand elasticity) and rediscovered by econometrics. The Angrist-Imbens "Local Average Treatment Effect" framework (1990s) clarified that IV recovers the effect among *compliers* — those whose treatment status was changed by the instrument — not the population average. This subtle scope restriction trips up most first-time users.

## Why Use This Thinking Tool

- **Unblocks causal questions otherwise abandoned.** When you have unmeasured confounding, IV is sometimes the only credible path to a causal estimate. Education economics (lottery-based school admissions), labor economics (Vietnam draft as IV for veteran status), and health economics (distance-to-hospital as IV for treatment) all rest on IV.
- **Honest about scope.** IV explicitly tells you whose causal effect you're estimating: the *compliers*. This is more honest than a confounded regression coefficient claiming population-wide validity.
- **Forces substantive defense of assumptions.** "Why is Z exogenous?" is a serious institutional / legal / biological question, not a statistical one — which is exactly the kind of conversation worth having before a policy is shipped.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the causal question: effect of treatment X on outcome Y.                  |
|    2 | Identify the unmeasured confounder U (the reason regression won't work).        |
|    3 | Find candidate instrument Z: a variable that affects X.                         |
|    4 | Test the three IV conditions:                                                   |
|      |   Relevance: Z is correlated with X (test in data; F-stat > 10 on first stage) |
|      |   Exogeneity: Z is independent of confounders U                                 |
|      |   Exclusion: Z affects Y *only through* X (no direct or indirect side-paths)    |
|    5 | Estimate via two-stage least squares (2SLS) or via Wald estimator               |
|      |   ratio: cov(Z,Y) / cov(Z,X)                                                    |
|    6 | Interpret as the LATE — Local Average Treatment Effect on compliers.            |
|    7 | Sensitivity-analyze: what if the exclusion restriction is slightly violated?    |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
INSTRUMENT-VALIDITY WORKSHEET

    Causal question: Effect of X = ___________________ on Y = ____________________

    Suspected unmeasured confounder U: ___________________________________________

    Candidate instrument Z: _______________________________________________________

    Three-condition audit:
      [ ] RELEVANCE  — Does Z affect X meaningfully?
            First-stage regression of X on Z: coefficient ____, F-stat ____
            Rule of thumb: F > 10. If F < 10, instrument is "weak" and IV biased.

      [ ] EXOGENEITY — Is Z independent of unobserved confounders?
            Argument: ___________________________________________________________
            (cannot be tested in data; defend on substantive grounds)

      [ ] EXCLUSION — Does Z affect Y *only through* X?
            Argument: ___________________________________________________________
            Side-paths to rule out: _____________________________________________

    Estimator (Wald):  β̂_IV = (Y(Z=1) − Y(Z=0)) / (X(Z=1) − X(Z=0))

    Population this estimates (LATE, compliers only):
      Compliers = those whose X status flips when Z flips
      NOT estimated: always-takers, never-takers, defiers

CLASSIC IV EXAMPLES (calibrate your intuition)

    X (treatment)              | Y (outcome)        | Z (instrument)
    ---------------------------|--------------------|-------------------------------
    Veteran status             | Earnings           | Vietnam draft lottery (Angrist 1990)
    Years of schooling         | Earnings           | Quarter-of-birth (Angrist & Krueger)
    Hospital admission         | Mortality          | Distance to hospital (McClellan)
    School quality             | Test scores        | Lottery-based admissions
    Medication adherence       | Health outcome     | Random assignment to encouragement

SENSITIVITY-ANALYSIS PROMPT

    If the exclusion restriction is violated by amount δ
      (Z has a small direct effect on Y), the estimated β̂ is biased by ≈ δ / cov(Z,X).
    Plot β̂ as a function of plausible δ — at what δ does the conclusion flip?
```

> **Operational notes:** The biggest practical mistake is celebrating a strong first stage (Z predicts X) and ignoring the exclusion restriction (Z reaches Y only through X). The exclusion restriction is *the* scientific bet. Defend it like a contract clause — name every conceivable side-path and argue why each is implausible. Second, weak instruments (F < 10) are worse than no IV at all: they amplify any violation of the exclusion restriction. Third, remember the LATE caveat: you're estimating the effect on compliers, who may not be the population the policy maker cares about. If your instrument is "lottery offer", LATE is the effect on people who attend when offered and don't otherwise; the "always-takers" (rich families) and "never-takers" (no interest) are unobserved. Spell this out in any executive summary; otherwise you risk presenting a complier-only estimate as if it generalized.
