---
Item_ID: tt-causal-dags
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Causal DAGs
tt_Source: "Judea Pearl 1995–2009 (Causality, 2009); Sewall Wright 1921 (path analysis precursor)"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Causal & diagnostic reasoning
tt_Operation: Map relational topology
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Visualization technique
- Algorithm
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Mathematical / formal
- Scientific method
tt_Posture:
- Expert-required
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Instrumental Variables
- Sensitivity Analysis
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
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Pearl's directed acyclic graphs encode causal assumptions as nodes and arrows. The do-calculus (do(X)) and back-door criterion convert observational data into causal estimates by identifying which variables to control for — and crucially, which to NOT control for (colliders)."
Needs_Processing: false
AI_Instructions: ''
---

# Causal DAGs

**One-line summary:** A directed acyclic graph in which nodes are variables and arrows assert direct causal influence — making causal assumptions explicit, auditable, and computable via the back-door / front-door criteria.

**When to reach for it:** Any time you need to estimate a causal effect from observational data (no RCT available), reason about confounders and colliders, design an experiment, or expose hidden assumptions in a regression specification.

---

## Purpose Of This Thinking Tool

A causal DAG (Directed Acyclic Graph) makes the implicit causal model that lurks behind every regression *visible*. You draw nodes for variables and arrows for direct causal effects. Once the graph is on the page, Judea Pearl's do-calculus tells you mechanically which variables you must condition on, which you must *not* condition on, and whether the causal effect is identified at all from your data.

The non-obvious operational insight: controlling for a "common-effect" variable (a *collider*) actively introduces bias rather than reducing it. This is the opposite of the textbook regression habit ("throw in every plausible covariate"). The DAG makes this discipline visual — once you see the V-structure (X → Z ← Y), you immediately see why controlling for Z spuriously couples X and Y. The back-door criterion (block all "non-causal paths" from X to Y by conditioning on a sufficient set, but never on a descendant of X) is the algorithmic form.

The framework dates from Sewall Wright's 1921 path analysis but was made fully rigorous by Pearl in the 1990s with the do-operator (do(X=x) = "intervene to set X to x", distinct from observation). Today it is the lingua franca of causal inference in epidemiology, economics, and ML.

## Why Use This Thinking Tool

Three regression-era failures DAGs prevent:

1. **Collider bias (M-bias).** Conditioning on a downstream common effect creates spurious correlation between its parents. Most "controversial" findings in social science where a known effect reverses sign on inclusion of a covariate are M-bias, not deep insight.
2. **Mediator-as-confounder confusion.** Controlling for a mediator on the causal path X → M → Y removes part of the causal effect you wanted to estimate. The DAG exposes whether a node is on or off the causal path.
3. **Implicit assumptions.** Every regression has a causal interpretation that is *true conditional on assumptions*. The DAG forces those assumptions onto the page where they can be challenged. "We need this to identify the effect — does anyone disagree with arrow X → Y?" is a productive meeting; "let's run the regression" isn't.

For consulting and policy work, DAGs convert vague causal claims ("training drives retention") into checkable models ("training → engagement → retention; tenure confounds both"). Once the DAG is shared, decisions about data collection, controls, and intervention design become traceable.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | List the variables in the system: treatment X, outcome Y, candidate covariates. |
|    2 | Draw an arrow A → B if you believe A directly causes B (no mediator).           |
|    3 | Verify acyclicity — no variable can cause itself through a chain.               |
|    4 | Identify *paths* from X to Y: causal paths (forward) and back-door paths (with  |
|      | an arrow into X somewhere).                                                     |
|    5 | Apply the back-door criterion: find a set Z such that (a) Z blocks every        |
|      | back-door path, (b) Z contains no descendant of X.                              |
|    6 | If such Z exists → the causal effect P(Y | do(X)) is identified by adjusting    |
|      | for Z. If not → consider front-door, instrumental variables, or admit          |
|      | non-identifiability.                                                            |
|    7 | Stress-test the DAG: ask "what's missing?" Add unmeasured confounders as        |
|      | nodes (often drawn dashed). Re-check identifiability.                           |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
DAG ELEMENT TEMPLATE (build your own)

    Variables (nodes):
        X = ____________________________   (treatment / cause of interest)
        Y = ____________________________   (outcome)
        Z₁ = ___________________________   (candidate covariate)
        Z₂ = ___________________________
        U  = ___________________________   (unmeasured confounder, drawn dashed)

    Arrows (direct causal effects):
        X → Y   ?     X → Z₁  ?     Z₁ → X  ?     Z₁ → Y  ?
        Z₂ → X  ?     Z₂ → Y  ?     X → Z₂ ← Y (collider!) ?
        U → X   ?     U → Y   ?

PATH CLASSIFICATION (the analytic workhorse)

    A path between X and Y is BLOCKED if:
      • It contains a chain (X → Z → Y) or fork (X ← Z → Y) where Z is conditioned on
      • It contains a collider (X → Z ← Y) where Z (and its descendants) are NOT conditioned on
    Otherwise the path is OPEN (transmits association, possibly non-causal).

BACK-DOOR ADJUSTMENT WORKSHEET

    Causal paths from X to Y (forward arrows only):
      1. _________________________________________
      2. _________________________________________

    Back-door paths (start with arrow into X):
      1. X ← _____ → Y                  block by conditioning on: ____
      2. X ← _____ → _____ → Y          block by conditioning on: ____
      3. X ← _____ ← _____ → Y          block by conditioning on: ____

    Adjustment set Z = {_______________________________}
    Check: every back-door path blocked?  ___
    Check: Z contains no descendant of X?  ___
    Identifiable?  □ YES — adjust for Z   □ NO — try IV, front-door, or RCT

COMMON DAG PATTERNS TO RECOGNIZE

    Confounder:        X ← Z → Y          (must condition on Z)
    Mediator:          X → M → Y          (do NOT condition on M if estimating total effect)
    Collider:          X → C ← Y          (do NOT condition on C; conditioning creates bias)
    Instrument:        Z → X → Y, Z⊥Y|X   (use IV if X has unmeasured confounders w/ Y)
    M-structure:       X → C ← Y, with Z₁→C, Z₂→C — conditioning on C, Z₁, or Z₂ may bias
```

> **Operational notes:** Resist the regression instinct to add controls. Each candidate covariate must earn its place — it confounds (condition on it), mediates (don't condition if you want total effect), or is a collider (NEVER condition on it). When unmeasured confounders are likely, switch to instrumental variables, front-door criterion, or be honest that you have an association, not a causal estimate. Two more practical moves: (1) build the DAG with the team *before* looking at data — you want assumptions, not data-fits; (2) draw two DAGs reflecting two reasonable theories and check whether the answer is robust to which is true. If yes, you have a finding; if no, you have a research question.
