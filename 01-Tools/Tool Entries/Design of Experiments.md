---
Item_ID: tt-design-of-experiments
Item_Prototype: Thinking_Tool
Title: Design of Experiments
tt_Source: "R.A. Fisher, The Design of Experiments (1935); foundational work on randomization, replication, blocking, factorial design. Modern industrial applications: Taguchi methods, response surface methodology."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Engineering / design reasoning
tt_Operation: Stress-test a position
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Algorithm
- Sequenced workflow
- Matrix
tt_Scale:
- Small group
- Organizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Mathematical / formal
- Scientific method
- Industrial / business
tt_Posture:
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Aesthetic / craft
- Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Constraint Satisfaction
- Sensitivity Analysis
- Scientific Method
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Aesthetic / craft', 'Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Statistical method for designing experiments to efficiently learn about how multiple input variables affect outcomes. Full factorial: test all combinations of variables — exponential cost. Fractional factorial: test subset chosen to capture main effects and key interactions. Taguchi: orthogonal arrays for industrial robust design. Key principle: vary multiple factors together (efficient), not one at a time (slow). Used in manufacturing, A/B testing platforms, agriculture, drug development, software performance tuning."
Needs_Processing: false
AI_Instructions: ''
---

# Design of Experiments

**One-line summary:** A statistical methodology for designing experiments that efficiently learn how multiple input variables affect an outcome — varying factors together in structured patterns rather than testing one variable at a time, dramatically reducing the experiments needed for valid conclusions.

**When to reach for it:** Manufacturing process optimization, multi-variate A/B testing in product / web / marketing, agricultural and biological experimentation, drug-trial design, software performance tuning, and any situation where multiple factors affect an outcome and you need efficient empirical learning.

---

## Purpose Of This Thinking Tool

R.A. Fisher's *The Design of Experiments* (1935) established the modern foundations of experimental design. The core insight: **experiments should be designed to efficiently learn about effects, not just to confirm hypotheses.** Naive experimentation tests one variable at a time (OFAT — one factor at a time), which requires exponentially many experiments to map a multi-factor space and misses interactions.

Fisher's principles:

1. **Randomization** — randomly assign experimental units to conditions; protects against unmeasured confounders
2. **Replication** — repeat each condition; quantifies experimental noise
3. **Blocking** — group similar units together to control for nuisance variation
4. **Factorial design** — vary multiple factors simultaneously; efficient and reveals interactions

The non-obvious operational insight is that **factorial designs are exponentially more efficient than OFAT for learning about multiple factors and their interactions.** Testing 5 binary factors with OFAT requires 5 changes (and misses all interactions); a full factorial tests all 2^5 = 32 combinations and reveals interactions. A fractional factorial (2^(5-1) = 16) can capture most main effects and key interactions with half the runs.

Common DoE designs:

- **Full factorial** — test all combinations of all factor levels. Best information; exponential cost.
- **Fractional factorial** — test a carefully-chosen subset. Captures main effects and key interactions.
- **Plackett-Burman** — extreme economy for screening many factors quickly.
- **Response surface methodology** — for optimization within a region; quadratic models.
- **Taguchi orthogonal arrays** — robust design; varies factors and noise variables together.
- **Latin squares / Greco-Latin squares** — for blocking on multiple nuisance variables.

A second insight: **DoE is the structural foundation of modern A/B testing platforms.** Multivariate testing (varying multiple page elements simultaneously) is fractional factorial DoE applied to web. The same principles that govern manufacturing experiments govern multi-variate web experiments.

A third insight: **the design phase is more important than the analysis phase.** Once data is collected, analysis is largely automated. Bad design produces data that no analysis can rescue; good design produces clean data that analysis just summarizes. Spend disproportionate effort designing.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **OFAT inefficiency.** Testing one factor at a time is structurally inefficient — exponentially more experiments for the same learning vs. factorial design. Recognizing this saves substantial effort.
2. **Missed interactions.** Some factors only affect outcomes in combination. OFAT can't detect this; factorial designs can. Pure single-factor analysis often produces wrong recommendations because it misses interactions.
3. **The confounder threat.** Without randomization and blocking, observed correlations between factors and outcomes may be due to confounders. DoE's principles protect against this; ad-hoc experiments often don't.

For manufacturing engineers, biological / agricultural researchers, A/B testing teams, and any quantitative experimenter, DoE is foundational methodology. Modern tools (JMP, Minitab, R packages) make execution accessible; understanding the principles is the design work.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the response. What outcome are you trying to learn about?               |
|    2 | Identify factors (input variables) likely to affect the response.               |
|    3 | Choose factor levels. How many values per factor? (Often 2-3.)                  |
|    4 | Choose design type. Full factorial for few factors. Fractional for many.         |
|      | Plackett-Burman for screening. Response surface for optimization.               |
|    5 | Plan replication. How many runs per condition? Drives statistical power.       |
|    6 | Plan randomization and blocking. Random order; group similar units.             |
|    7 | Run the experiment. Capture all factor settings and the response per run.      |
|    8 | Analyze: ANOVA / regression to identify main effects and interactions. Confirm |
|      | with replication where possible.                                                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FACTORIAL DESIGN STRUCTURE

   For 3 binary factors (A, B, C):

   Run | A | B | C
   ----|---|---|---
   1   | -1| -1| -1
   2   | +1| -1| -1
   3   | -1| +1| -1
   4   | +1| +1| -1
   5   | -1| -1| +1
   6   | +1| -1| +1
   7   | -1| +1| +1
   8   | +1| +1| +1

   Full factorial: 2^3 = 8 runs. Captures all 3 main effects
   plus all 4 interactions (AB, AC, BC, ABC).

   Compare to OFAT:
       Run 1: baseline (-1, -1, -1)
       Run 2: change A (+1, -1, -1)
       Run 3: change B (-1, +1, -1)
       Run 4: change C (-1, -1, +1)

   OFAT: 4 runs, 3 main effects, NO interactions.
   Full factorial: 8 runs, 3 main effects + ALL interactions.

   For more factors, the savings compound: 5 factors full factorial
   = 32 runs vs. fractional half-factorial = 16 runs (still
   captures main effects and key 2-way interactions).

THE DESIGN-CHOICE TABLE

   Goal                      | Recommended design
   --------------------------|----------------------------
   Many factors (>6); few    | Plackett-Burman (screening)
   are likely to matter      |
   Moderate factors (4-6);   | Fractional factorial 2^(k-p)
   limited budget            |
   Few factors (≤4); want    | Full factorial
   all interactions          |
   Need optimization curve   | Response surface methodology
   (quadratic effects)       |
   Robust design (varying    | Taguchi orthogonal arrays
   noise variables)          |

   Match design to goal. Wrong design type wastes effort.

THE RANDOMIZATION-BLOCKING DISCIPLINE

   RANDOMIZATION:
   - Randomly assign experimental units to conditions.
   - Randomize the run order to control for time-related drift.
   - Critical for valid statistical inference.

   BLOCKING:
   - Group similar units together (e.g., same lot of material,
     same day, same operator).
   - Run all conditions within each block; analyze block effects
     separately.
   - Reduces noise from nuisance variables without confounding.

   Without these, observed effects may be artifacts of order /
   time / unit differences. With them, effects are interpretable.

THE INTERACTION-DETECTION

   Two factors A and B interact if A's effect depends on B's level.

   Example:
       A is "temperature" (low / high)
       B is "catalyst type" (X / Y)
       Response is "yield."
       
       At catalyst X: temperature increase → yield up
       At catalyst Y: temperature increase → yield down
       
       This is an interaction. OFAT misses it; factorial reveals it.

   Many real systems have interactions; ignoring them produces
   wrong recommendations. The factorial design is the antidote.

THE SAMPLE-SIZE / REPLICATION DISCIPLINE

   Each unique condition should be replicated to estimate error
   variance. Power analysis (a priori or post hoc) determines
   needed replication.

   Common minimum: 3 replicates per condition for moderate
   effects; more if effects are small or variability is high.

   Insufficient replication produces noisy estimates that may not
   detect real effects (Type II error) or may flag noise as
   effects (Type I error).

THE COMMON-USE INDUSTRIAL APPLICATIONS

   1. Manufacturing process optimization:
       Factors: temperature, pressure, time, catalyst, material
       Response: yield, quality, defect rate
       Method: factorial design → identify settings.

   2. A/B / multivariate web testing:
       Factors: page elements (headline, image, button)
       Response: conversion, click-through, retention
       Method: fractional factorial.

   3. Drug development:
       Factors: dose, frequency, duration
       Response: efficacy, side effects
       Method: factorial within ethical / safety constraints.

   4. Agricultural research:
       Factors: variety, fertilizer, watering, planting density
       Response: yield, quality
       Method: blocked factorial (block by field).

THE COMMON FAILURE MODES

   1. ONE-FACTOR-AT-A-TIME (OFAT)
        Inefficient and misses interactions.
        Recovery: factorial designs.

   2. UNRECOGNIZED CONFOUNDERS
        Time-of-day, operator, batch effects confound results.
        Recovery: randomization + blocking.

   3. INSUFFICIENT REPLICATION
        Single observation per condition; noise overwhelms signal.
        Recovery: power-analysis-based replication.

   4. ANALYSIS WITHOUT DESIGN PLAN
        Running an experiment then figuring out the analysis.
        Recovery: design analysis upfront; software (JMP, Minitab,
        R) can plan AND analyze.

   5. IGNORED INTERACTIONS
        Reporting only main effects when interactions are
        significant. Recovery: include all relevant interactions
        in the model.

THE OPERATIONAL TEMPLATE

   Response: ____________________________________________

   Factors: _____________________________________________
       Factor 1: _________________ Levels: _______________
       Factor 2: _________________ Levels: _______________
       Factor 3: _________________ Levels: _______________

   Design type chosen: __________________________________
   Number of runs: ______________________________________
   Replication per condition: ___________________________
   Randomization plan: __________________________________
   Blocking variables: __________________________________

   Run the experiment.

   Analysis: ANOVA / regression for main effects and interactions.
   Verdict: which factors matter? Which interactions?
   Recommended settings: ________________________________
```

> **Operational notes:** Four disciplines. (1) Vary factors together, not one at a time. Factorial design is structurally more efficient and reveals interactions OFAT misses. The design choice is high-leverage. (2) Randomization and blocking are not optional. Without them, observed correlations may be artifacts. With them, effects are interpretable. The discipline is statistical, not just procedural. (3) Design before running. Once data is collected, analysis is largely mechanical. Bad design produces data no analysis can rescue. Invest disproportionately in the design phase. (4) Capture interactions explicitly. Many real systems have factor-factor interactions; reporting only main effects produces wrong recommendations. Include interaction terms in models; investigate significant ones.
