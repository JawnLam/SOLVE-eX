---
Item_ID: tt-sensitivity-analysis
Item_Prototype: Thinking_Tool
Title: Sensitivity Analysis
tt_Source: "Operations research tradition (Charnes & Cooper, 1950s); modern practice via DCF / NPV (1960s–) and Monte Carlo (Metropolis & Ulam, 1949)"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Matrix
- Visualization technique
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Industrial / business
- Mathematical / formal
tt_Posture:
- Beginner-friendly
- Expert-required
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
tt_Often_Precedes: []
tt_Often_Follows:
- Expected Value Decision Trees
- Fermi Estimation
tt_Pairs_Well_With:
- Expected Value Decision Trees
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
Quick_Notes: "Systematically varies inputs to a model to discover which drive the conclusion (and which don't). One-way (vary one at a time), two-way (pairs), tornado diagrams, and Monte Carlo (full distribution) are the main forms. The sister tool every EV/NPV/forecast needs."
Needs_Processing: false
AI_Instructions: ''
---

# Sensitivity Analysis

**One-line summary:** A systematic procedure for varying a model's inputs across plausible ranges and observing which drive the output most — exposing where a recommendation is robust and where it hangs on a single uncertain assumption.

**When to reach for it:** After any model-driven recommendation (NPV, EV decision, market sizing, capacity plan, pricing analysis) — and especially before presenting it to a decision-maker.

---

## Purpose Of This Thinking Tool

Sensitivity analysis answers a question every quantitative recommendation depends on: *how robust is the conclusion to its inputs?* A model that recommends Action A might do so across the entire plausible range of inputs (robust) or only at the modal point estimate, flipping at slightly worse assumptions (fragile). Without sensitivity analysis, the difference is invisible — and decision-makers act on the recommendation as if it were robust.

The non-obvious operational insight: most models have 2–3 inputs that drive the answer and 10+ that barely matter. Sensitivity analysis identifies *which* — letting the team focus measurement, defense, and risk management on the genuinely high-leverage variables. The "tornado diagram" — a horizontal bar chart of inputs ordered by how much they swing the output — is the canonical artifact.

The technique grew out of operations research (linear programming sensitivity reports), discounted cash flow valuation (NPV with parameter sweeps), and Monte Carlo simulation (Metropolis & Ulam, 1949). It is now considered table stakes in financial modeling, infrastructure project appraisal, drug-development modeling, and policy analysis.

## Why Use This Thinking Tool

Three failure modes sensitivity analysis prevents:

1. **Point-estimate confidence.** A model output presented as a single number ("$84M NPV") implies false precision. Sensitivity reveals the range and the conditions under which the sign flips.
2. **Argument over the wrong variable.** Stakeholders argue passionately over inputs that barely move the answer; the tornado diagram redirects attention to inputs that actually matter.
3. **Hidden fragility.** A recommendation valid only when growth = 12%, churn = 2%, and CAC = $40 simultaneously is brittle. Sensitivity exposes this; without it, the brittleness ships.

For consulting and capital-allocation work, sensitivity analysis is the diligence move that distinguishes a defensible recommendation from a fragile one. It also provides a structured rebuttal to "but what if X?" questions — the answer is in the diagram.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the model output of interest (NPV, EV, payback, market size, etc.).   |
|    2 | List all model inputs. For each, define a plausible range (low / base / high). |
|    3 | One-way sensitivity: vary each input across its range, hold others at base.    |
|      | Record the output's range. Sort inputs by output-swing magnitude.              |
|    4 | Build a tornado diagram: horizontal bars showing each input's swing,           |
|      | sorted longest at top.                                                         |
|    5 | For the top 2–3 inputs, do two-way sensitivity (vary pairs simultaneously).    |
|    6 | If interactions matter or distributions are non-symmetric: run Monte Carlo —   |
|      | sample inputs from distributions, record the output distribution.              |
|    7 | Identify the *break-even* values: at what input level does the recommendation  |
|      | flip sign?                                                                     |
|    8 | Present: tornado diagram + break-even values + Monte Carlo distribution.       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
SENSITIVITY WORKSHEET

    Model output:  Y = f(X1, X2, ..., Xn)
    Base-case Y = ________

    ONE-WAY SENSITIVITY TABLE

      Input    | Low value | Base | High value | Y at low | Y at high | Swing
      ---------|-----------|------|------------|----------|-----------|------
      X1       |           |      |            |          |           |
      X2       |           |      |            |          |           |
      X3       |           |      |            |          |           |
      X4       |           |      |            |          |           |

      Sort by |Swing| descending → top 2–3 are the high-leverage inputs.

    TORNADO DIAGRAM (sketch)

      X1   ████████████████   (large swing)
      X3   ███████████
      X2   █████
      X4   ██                  (small swing)
      X5   ▌                   (negligible)

    BREAK-EVEN VALUES (where the recommendation flips)
      X1 break-even: ________   (current best estimate ____)
      X2 break-even: ________   (current best estimate ____)
      X3 break-even: ________   (current best estimate ____)

      Distance to break-even (% of base case): if all > ~30%, the
      decision is robust; if any < ~10%, the decision hangs on that input.

    TWO-WAY SENSITIVITY (top 2 inputs, X1 × X2)

                   |  X2_low  |  X2_base |  X2_high
        -----------|----------|----------|----------
        X1_low     |  Y____   |  Y____   |  Y____
        X1_base    |  Y____   |  Y____   |  Y____
        X1_high    |  Y____   |  Y____   |  Y____

        Highlight cells where Y crosses the decision threshold.

    MONTE CARLO (when inputs are correlated or non-symmetric)
      Sample N=10,000 from joint distribution of inputs.
      Record output distribution.
      Report:  P(Y > threshold) = ____
               5th / 50th / 95th percentile of Y = ____ / ____ / ____

THREE PRESENTATION ARTIFACTS (every model output needs all three)

    1. Tornado diagram                — which inputs matter most
    2. Break-even table               — how far from "flip" we are
    3. Output distribution / band     — the realistic range of Y

WHEN TO ESCALATE TO MONTE CARLO (vs. simple one-way)
      • Inputs are correlated (one-way overstates each input's swing in isolation)
      • Outputs are non-linear in inputs
      • Tail risk matters more than mean (Monte Carlo gives you the 95th percentile)
      • Decision threshold is near the mean (need distribution, not point estimate)
```

> **Operational notes:** Three disciplines compound the value. (1) Define plausible ranges before running the analysis — if you choose ranges *after* seeing the result, you'll narrow them to make the answer look robust. Use the team's pre-commitment, the historical range, or external benchmarks. (2) Always include the *worst plausible case*. Not the absolute worst, but the bottom 10%-ile. Decisions that survive bottom-10% conditions are robust; ones that don't need either redesign or explicit risk reserves. (3) When the tornado diagram is dominated by 1–2 inputs, that's the analytical agenda — measure those better, defend their estimates explicitly, and design contingencies for being wrong about them. The other 8 inputs can be fixed at base-case with little loss. Fourth: for high-stakes decisions, supplement sensitivity with explicit *pre-mortem* on the high-leverage variables — what would cause X1 to come in at the low end, and is that scenario plausible?
