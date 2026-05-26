---
Item_ID: tt-stock-and-flow-models
Item_Prototype: Thinking_Tool
Title: Stock-and-Flow Models
tt_Source: 'Jay Forrester, MIT (1956 onward); foundational framework of System Dynamics. Key works: Industrial Dynamics (1961), Urban Dynamics (1969), World Dynamics (1971). Donella Meadows et al., Limits to Growth (1972) is the most famous application. Standard simulation tools: Stella, Vensim, AnyLogic.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Systems / cybernetic thinking
tt_Operation: Map relational topology
tt_Cross_Domains: []
tt_Form:
- Sequenced workflow
- Mental model
tt_Scale:
- Solo
- Small group
tt_Duration:
- Workshop
tt_Lineage:
- Western analytic / academic
- Mathematical / formal
tt_Posture:
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows:
- Causal Loop Diagrams
tt_Pairs_Well_With:
- Causal Loop Diagrams
- Feedback Delay Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Quantitative system-dynamics models with stocks (accumulations: population, inventory, debt) and flows (rates of change: birth rate, sales, payments). Stock = integral of net flow over time. Computer simulation produces behavior over time. Reveals dynamics (oscillation, overshoot, exponential growth/collapse) that static analysis can''t predict. Standard for policy modeling, supply chains, ecological systems.'
Needs_Processing: false
AI_Instructions: ''
---

# Stock-and-Flow Models

**One-line summary:** Jay Forrester's foundational system-dynamics framework for quantitative simulation: stocks accumulate (population, inventory, capital, debt), flows change them (birth rate, sales, payments) — and simulating the differential equations over time reveals system behavior (oscillation, overshoot, collapse) that static analysis can't predict.

**When to reach for it:** Policy modeling where dynamics over time matter (climate, public health, economic); supply-chain analysis; population and resource modeling; financial-system stress modeling; corporate strategy with significant time delays; and any context where causal-loop diagrams need to be quantitative — when "how much" and "when" matter, not just "what direction."

---

## Purpose Of This Thinking Tool

**Stock-and-flow models** are the quantitative formalism for system dynamics. The structure:

1. **Stocks** — accumulations that persist over time. Examples: population, water in reservoir, inventory, financial capital, knowledge.
2. **Flows** — rates of change that add to or subtract from stocks. Examples: birth rate (into population), water inflow / evaporation (reservoir), sales / production (inventory).
3. **Auxiliary variables** — calculations connecting stocks to flows (e.g., death rate = population × death rate per capita).
4. **Differential equations** — stock(t+Δt) = stock(t) + (inflows − outflows)Δt, integrated over time.
5. **Simulation** — computer runs the model forward; output is behavior over time.

The non-obvious operational insight is that **stocks and flows have different conservation properties.** Stocks have units (people, dollars, gallons); flows have units per time (births/year, dollars/month, gallons/sec). Confusing them produces nonsense models. Stocks change only via flows; flows can change instantaneously (decisions, events) but stocks change gradually (integrated over time).

A second insight: **stock-and-flow exposes dynamics that linear thinking can't predict.**

- **Delays** (between flow decision and stock change) produce oscillation
- **Reinforcing loops** (e.g., compound interest, viral adoption) produce exponential growth
- **Limits** (carrying capacity) produce S-curves
- **Reinforcing + delayed balancing** produces overshoot-and-collapse (Limits to Growth, climate dynamics)

A third insight: **the framework requires modeling discipline.** Stock-and-flow models are quantitative — they require parameter estimation, numerical integration, validation against observed behavior. Sloppy models produce sloppy predictions; the discipline matters.

A fourth insight: **the framework integrates with causal loop diagrams.** CLDs show structure qualitatively; stock-and-flow models add quantitative dynamics. Often: draw CLD first; identify which loops to quantify; build stock-and-flow.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The static-thinking surprise.** Most analysis treats systems as static; dynamics produce behaviors (oscillation, collapse, lag) that static thinking can't predict.
2. **The "stock vs. flow confusion" error.** Treating stocks (e.g., debt) like flows (e.g., debt service) produces wrong analysis.
3. **The "intuition-only" forecasting failure.** Complex feedback dynamics exceed human intuitive prediction; computer simulation captures them.

For policy analysts, supply-chain managers, climate modelers, corporate strategists with multi-year time horizons, and anyone modeling systems with significant feedback dynamics, stock-and-flow is essential.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the system boundary. What's in / out of the model?                       |
|    2 | Identify key stocks. What accumulates over time?                                 |
|    3 | Identify flows. What changes the stocks?                                          |
|    4 | Add auxiliary variables. Calculations connecting stocks to flow rates.         |
|    5 | Specify equations. Each stock = previous + (inflows − outflows) × time step.   |
|    6 | Estimate parameters. Initial values; flow coefficients.                         |
|    7 | Simulate. Use Stella / Vensim / Python ODE solver. Output: time-series.        |
|    8 | Validate. Compare simulation against observed historical behavior. Refine.    |
|    9 | Run scenarios. What if parameters change? Policy interventions?                |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE STOCK-AND-FLOW NOTATION

   Stock (rectangle):
       ┌─────────────┐
       │   Stock A   │
       └─────────────┘

   Flow (faucet/valve):
       cloud → ⊨ → Stock A → ⊨ → cloud
       (inflow)               (outflow)

   The clouds represent the system boundary (where
   inflows come from / outflows go to).

   Auxiliary variable (often a circle or just
   variable name):
       Used to compute flow rates from stocks and
       parameters.

   Connector (arrow):
       Indicates information flow (not material).

THE EQUATION FORM

   For each stock:
       Stock(t+Δt) = Stock(t) + (Inflow − Outflow) × Δt

   In differential form:
       d(Stock) / dt = Inflow − Outflow

   Flows often depend on stocks:
       Outflow = Stock × outflow_rate
       (e.g., Death Rate = Population × death rate per
       capita)

   Auxiliary variables:
       Variable = function(Stocks, parameters)

   Numerical integration over time gives behavior.

THE WORKED EXAMPLE — POPULATION

   Stock: Population
   Flows: Births (in), Deaths (out)
   Auxiliaries: Birth rate per capita, Death rate per
   capita

   Equations:
       Births(t) = Population(t) × birth_rate_per_capita
       Deaths(t) = Population(t) × death_rate_per_capita
       Population(t+1) = Population(t) + Births(t) −
       Deaths(t)

   With:
       birth_rate_per_capita = 0.025/year
       death_rate_per_capita = 0.01/year
       Initial Population = 1,000,000

   Net growth rate = 0.025 − 0.01 = 0.015/year =
   1.5%/year
   Population doubles every 47 years (rule of 70 / 1.5)

   Adding carrying capacity:
       death_rate_per_capita = 0.01 × (1 +
       (Population / Carrying_capacity)²)
       Death rate increases quadratically as population
       approaches K.

   Now: S-shaped growth toward K.

   This simple model captures population dynamics
   from explosive growth (early) to S-curve approach
   to carrying capacity. Real-world refinements add
   age structure, immigration, etc.

THE COMMON DYNAMIC PATTERNS

   EXPONENTIAL GROWTH:
       Reinforcing loop dominant; no constraints.
       Pattern: stock doubles in fixed time period.
       Examples: viral adoption, compound interest,
       early-stage population growth.

   GOAL-SEEKING (S-CURVE):
       Reinforcing initial; balancing as approached
       limit.
       Pattern: rapid early growth, slowing approach
       to plateau.
       Examples: market saturation, learning curves.

   OSCILLATION:
       Balancing loop with delay.
       Pattern: stock overshoots, undershoots, settles
       (or doesn't).
       Examples: thermostat with slow response;
       inventory cycles in supply chains.

   OVERSHOOT-AND-COLLAPSE:
       Reinforcing growth + delayed balancing
       (resource depletion).
       Pattern: rapid growth, peak, decline beyond
       resource availability.
       Examples: Limits to Growth scenarios,
       speculative bubbles.

   EXPONENTIAL DECAY:
       Outflow proportional to stock; no inflow.
       Pattern: stock approaches zero asymptotically.
       Examples: radioactive decay, brand-loyalty
       erosion without reinforcement.

THE WORKED EXAMPLE — SUPPLY-CHAIN OSCILLATION

   Stocks: Customer demand backlog, Production-in-
   progress, Finished inventory.

   Flows: Customer orders (in), Production starts,
   Production complete, Sales (out).

   Delays:
       Order signal → production start: 1 week
       Production start → production complete: 4 weeks

   When customer demand spikes:
       Orders surge → backlog builds → production
       starts ramped up → 4 weeks later, production
       completes (overshoot, since demand may have
       cooled) → inventory accumulates → production
       cut → 4 weeks later, low inventory when
       customer demand re-surges.

   Result: bullwhip effect — orders oscillate
   massively along supply chain, even when retail
   demand is stable.

   Stock-and-flow simulation reveals the oscillation;
   intuition often misses it.

   Mitigation: reduce delays (faster production),
   share information (downstream visibility), buffer
   stocks (safety inventory).

THE COMMON FAILURE MODES

   1. STOCK-FLOW CONFUSION
        Treating stock as flow or vice versa. Recovery:
        check units (persons vs. persons/year).

   2. MISSING FEEDBACK
        Modeling open loops; missing the closing
        feedback. Recovery: trace each variable's
        downstream effects back to itself.

   3. PARAMETER ARBITRARINESS
        Plausible but unsupported parameters. Recovery:
        validate against historical data; sensitivity
        analysis on uncertain parameters.

   4. OVERFITTING
        Many parameters tuned to match one history;
        no predictive power. Recovery: simpler models;
        validate on held-out data.

   5. ARTIFICIAL EQUILIBRIUM
        Models that converge to neat equilibrium when
        reality oscillates. Recovery: include delays,
        nonlinearities.

   6. NO SCENARIO ANALYSIS
        Single base-case run; no exploration. Recovery:
        run multiple scenarios; sensitivity analysis.

   7. UNVALIDATED MODEL
        Model accepted without comparison to observed
        behavior. Recovery: validate against history;
        explain discrepancies.

THE OPERATIONAL TEMPLATE

   System / problem: __________________________________

   System boundary: ___________________________________

   Stocks (with units):
       Stock 1: __________________ (units: ________)
       Stock 2: __________________ (units: ________)
       ...

   Flows (with units, into/out of which stock):
       Flow 1: ___________________ (units/time: _____)
       Flow 2: ___________________ (units/time: _____)
       ...

   Auxiliary variables:
       _________________________________________________

   Initial values:
       Stock 1 initial: _____ Stock 2 initial: _____

   Parameters with sources:
       _________________________________________________

   Simulation tool: ___________________________________

   Time horizon: ______________________________________

   Validation: simulation matches observed history?
   Y / N

   Scenarios run:
       Base case: _____________________________________
       Alternative 1: _________________________________
       Alternative 2: _________________________________
```

> **Operational notes:** Four disciplines. (1) Distinguish stocks from flows. Stocks accumulate (units: things); flows change them (units: things/time). The unit-check disciplines correct categorization. (2) Validate against observed history. A model that doesn't reproduce observed behavior has no predictive power. The validation step separates useful models from speculative ones. (3) Run scenarios, not just base case. Single-run models hide sensitivity to assumptions. Multi-scenario / sensitivity analysis reveals which parameters matter and bounds uncertainty. (4) Pair with causal loop diagrams. CLDs map structure qualitatively; stock-and-flow simulates dynamics quantitatively. Use both — CLD for understanding, stock-and-flow for simulation.
