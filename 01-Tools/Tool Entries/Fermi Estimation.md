---
Item_ID: tt-fermi-estimation
Item_Prototype: Thinking_Tool
Title: Fermi Estimation
tt_Source: "Enrico Fermi (1930s–40s, popularized via Manhattan Project anecdotes)"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Heuristic
tt_Scale:
- Solo
- Small group
tt_Duration:
- Snap
- Single session
tt_Lineage:
- Scientific method
- Industrial / business
tt_Posture:
- Beginner-friendly
- Time-pressured-OK
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
- Sensitivity Analysis
- Expected Value Decision Trees
tt_Often_Follows: []
tt_Pairs_Well_With:
- Base Rate Reasoning
- Sensitivity Analysis
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
Quick_Notes: "Order-of-magnitude estimation by decomposing a quantity into a chain of factors, each estimated within an order of magnitude. The key insight: log-error in factors averages out, so a chain of weak guesses produces a surprisingly strong estimate."
Needs_Processing: false
AI_Instructions: ''
---

# Fermi Estimation

**One-line summary:** Order-of-magnitude estimation of an unknown quantity by decomposing it into a chain of factors, each guessed within ~10×, multiplied together — relying on errors to partially cancel.

**When to reach for it:** When you need a defensible quantitative answer in minutes without data — sizing a market, judging plausibility of a claim, screening an opportunity, deciding whether a measurement is worth doing.

---

## Purpose Of This Thinking Tool

Fermi estimation gets credible numbers from no data. Decompose the target quantity into a multiplicative chain of factors you have *some* intuition about — each estimated to within an order of magnitude. Multiply them together. Because per-factor errors are roughly log-normal and partially independent, they cancel rather than compound. The classic example: Fermi estimating the yield of the Trinity nuclear test by tossing strips of paper at the moment of detonation and counting how far they blew. He hit within a factor of two of the eventual instrumented number.

The non-obvious operational insight: most quantities people *think* require data are actually within reach of a 4-step decomposition into populations, rates, and per-unit values. "How many piano tuners in Chicago?" decomposes into population × pianos-per-household × tunings-per-piano-per-year × tunings-per-tuner-per-year. None of those numbers is precisely known, but each is constrainable to within 10×, and the product is usually within 3× of the true answer.

The discipline became a touchstone of the Manhattan Project culture and was adopted by physics, consulting, product management, and rationalist communities. Its modern descendants: market sizing (TAM/SAM/SOM), back-of-envelope feasibility checks, "magnitude smell tests" before deeper analysis.

## Why Use This Thinking Tool

Three failure modes Fermi estimation prevents:

1. **Analysis paralysis.** Teams stall on "we need more data" when an order-of-magnitude estimate would already screen the decision. Fermi unblocks: an answer in 20 minutes is usually enough to decide whether deeper analysis is worth doing.
2. **Authority-driven numbers.** Without a Fermi check, executive intuitions ("this is a $1B market") propagate as facts. A quick decomposition either supports the number or surfaces the missing factor.
3. **Vendor-supplied estimates.** Numbers from sales decks, market reports, and pitches anchor strongly. A Fermi computation produces an independent estimate; if the two diverge by more than 10×, dig.

For consulting work, Fermi estimation is the single highest-leverage analytical move per minute. Most major recommendations rest on a quantity that can be Fermi-checked in 5 minutes; failing to do so is malpractice.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the target quantity Q with explicit units.                                |
|    2 | Decompose Q into a chain of factors:  Q = F1 × F2 × F3 × ...                    |
|      | Aim for 3–5 factors. Each should be something you can estimate.                 |
|    3 | For each factor, write a *low* / *best* / *high* estimate (each within ~10×).   |
|    4 | Compute the geometric mean (product of best estimates) — that's your Fermi.    |
|    5 | Optionally compute low and high bounds (multiply lows; multiply highs).        |
|    6 | Sanity-check via an alternative decomposition: re-derive Q a different way.    |
|      | If the two estimates agree within 3×, you're calibrated.                       |
|    7 | Decide: is the precision sufficient for the decision? If yes, ship. If no,    |
|      | identify the highest-leverage factor and tighten that one.                     |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
FERMI WORKSHEET

    Target quantity Q = ____________________________________  units: ___________

    Decomposition:  Q = ___________ × ___________ × ___________ × ___________

    Factor estimates:
                              | low    | best   | high
      F1: __________________  | _____  | _____  | _____
      F2: __________________  | _____  | _____  | _____
      F3: __________________  | _____  | _____  | _____
      F4: __________________  | _____  | _____  | _____

    Best estimate:  Q ≈  ______  (= F1_best × F2_best × ...)
    Low bound:      Q ≥  ______  (= F1_low × F2_low × ...)
    High bound:     Q ≤  ______  (= F1_high × F2_high × ...)

    SANITY-CHECK (alternative decomposition)
      Q = ___________ × ___________ × ___________
      Re-estimate:  Q ≈ ______
      Agrees within 3×?  □ yes  □ no — investigate disagreement

    HIGHEST-LEVERAGE FACTOR
      Which factor has the widest log-range (high/low ratio)?  ____
      That's the one worth tightening if precision matters.

LANDMARK QUANTITIES (memorize a dozen — they anchor most estimates)

      US population:           ~330 M             World population:        ~8 B
      US households:           ~130 M             US workforce:            ~160 M
      US GDP:                  ~$28 T             Global GDP:              ~$105 T
      Days/year:               365                Hours/year work:         ~2,000
      Seconds/year:            ~3.15 × 10⁷        Square miles US:         ~3.8 M
      Drivers in US:           ~230 M             Cars on road US:         ~280 M
      US adults online:        ~250 M             Smartphone users global: ~5 B
      Median US household income:  ~$74 K
      Median US house price:       ~$420 K

CALIBRATION DRILL (do this monthly)
      Estimate a quantity → look up the truth → log the log-error.
      Target: median |log10(estimate / truth)| ≤ 0.5  (i.e., within ~3×).
```

> **Operational notes:** Three skills compound the value. (1) Memorize a dozen landmark quantities (population, GDP, workforce, etc.) — anchors that prevent wild errors. (2) Always do the alternative decomposition. If two derivations of the same quantity differ by 10×, one of them is wrong; finding which is the actual analytical work. (3) Spend less time inside a single estimate than you think — the marginal value of refining a factor from "between 5 and 50" to "between 8 and 30" is small if other factors have similar uncertainty. Push for breadth (3 factors well-estimated) over depth (one factor sourced perfectly). Finally, calibrate yourself: keep a log of estimates vs. eventual truth. Most people are 10× *over*-confident in narrow-range answers; calibration training fixes this in weeks.
