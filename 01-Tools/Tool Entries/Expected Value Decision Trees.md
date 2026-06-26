---
Item_ID: tt-expected-value-decision-trees
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Expected Value Decision Trees
tt_Source: "Howard Raiffa 1968 (Decision Analysis); Ronald Howard 1966 (decision-tree formalization); roots in von Neumann–Morgenstern utility 1944"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Decision tree
- Algorithm
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Mathematical / formal
- Industrial / business
tt_Posture:
- Beginner-friendly
- Collaborative-willing
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
- Real Options Analysis
tt_Often_Follows:
- Bayesian Updating
- Fermi Estimation
tt_Pairs_Well_With:
- Sensitivity Analysis
- Pre-Mortem
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Risk / uncertainty', 'Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "EV = Σ p_i × v_i. The default workhorse for choices under uncertainty. Powerful when outcomes are roughly fungible (dollars), brittle when they're not (lives, reputation). Always pair with sensitivity analysis."
Needs_Processing: false
AI_Instructions: ''
---

# Expected Value Decision Trees

**One-line summary:** A branching diagram of decisions and chance events, in which every branch carries a probability and value, rolled up via expected value (Σ p × v) to compare options.

**When to reach for it:** Any decision under uncertainty with quantifiable outcomes — go/no-go on a project, pricing under demand uncertainty, R&D portfolio choices, insure-vs-self-insure, A/B test stop rules.

---

## Purpose Of This Thinking Tool

A decision tree forces the structure of an uncertain decision onto the page. Square nodes are decisions you make; circular nodes are chance events outside your control; terminal nodes are outcomes with values. To evaluate, fold the tree backward (right-to-left): at each chance node, take the expected value of its children; at each decision node, take the maximum (or minimum, for cost). The recommended decision is whichever branch has the highest rolled-up expected value.

The non-obvious operational insight: most of the value comes from *building* the tree, not *solving* it. Forcing the team to enumerate decisions, chance events, and terminal outcomes surfaces probability assumptions and value tradeoffs that prose discussions hide. The arithmetic is mechanical; the structure-naming is the work.

The technique was formalized by Howard Raiffa (Harvard Business School) and Ronald Howard (Stanford), grounded in von Neumann–Morgenstern utility theory. Its descendants are everywhere: real-options analysis, A/B test optimal-stopping, search-and-rescue allocation, and clinical decision analysis.

## Why Use This Thinking Tool

Three failure modes EV trees prevent:

1. **Hidden probabilities.** Statements like "X is unlikely" propagate through reasoning unmeasured. The tree forces a number.
2. **Comparing apples to oranges.** Decisions that mix small upside / large downside with the reverse become tractable on a common EV scale (provided values are comparable).
3. **Single-point-estimate planning.** Without a tree, plans assume a modal outcome. The tree makes uncertainty first-class.

For consulting and capital-allocation work, EV decision trees are the canonical artifact for "should we do X?" Used with sensitivity analysis, they become a living document of where the decision is robust and where it hangs on a single uncertain probability.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | List the decisions you can make. Square nodes.                                  |
|    2 | For each decision, list the chance events that follow. Circle nodes.            |
|    3 | Continue branching until you reach terminal outcomes — quantifiable values.     |
|    4 | Assign probabilities to each chance branch (must sum to 1 at each chance node). |
|    5 | Assign values to terminal nodes (dollars, utility, or other comparable scale).  |
|    6 | Fold backward:  EV(chance node) = Σ p_i × value_i;                              |
|                       Decision = argmax (or argmin) of children's EVs.                 |
|    7 | Read off the recommended path and the EV of the optimal strategy.               |
|    8 | Run sensitivity: vary each probability and value within plausible range; flag   |
|      | where the optimal decision flips.                                              |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
DECISION TREE TEMPLATE (ASCII rendering)

    [D]── Decision A ──[C]── 0.6 ── Outcome A1 (value $___)
                          \─ 0.4 ── Outcome A2 (value $___)
                                    EV(A) = 0.6 × $___ + 0.4 × $___ = $___

    [D]── Decision B ──[C]── 0.3 ── Outcome B1 (value $___)
                          \─ 0.5 ── Outcome B2 (value $___)
                          \─ 0.2 ── Outcome B3 (value $___)
                                    EV(B) = ...

    Recommended decision: argmax(EV(A), EV(B), ...) = ___
    EV of optimal strategy: $___

NESTED EXAMPLE (decision after a chance event)

    [D]── Pilot study ──[C]── 0.7 success ──[D]── Scale up   ──[C]── ...
                          \                 \─ Stop          ── EV ___
                          \─ 0.3 fail   ──[D]── Pivot        ──[C]── ...
                                          \─ Kill           ── EV ___

VALUE-OF-INFORMATION (a special EV-tree question)

    Compare two trees:
      A. The decision made *now* with current uncertainty.
      B. The decision made *after* purchasing/learning some piece of info.

    EVPI = EV(B) − EV(A) − cost of info.
    If EVPI > 0, the information is worth buying.

    This tells you when to ship a survey, run an experiment, or pay for due diligence.

SENSITIVITY GRID

      Variable to vary  | Plausible range | EV-optimal flip point | Confidence
      ------------------|-----------------|----------------------|------------
      P(success)        |                 |                      |
      Value of upside   |                 |                      |
      Value of downside |                 |                      |
      Cost of action    |                 |                      |

      Decision is robust if no plausible single-variable change flips the optimum.
```

> **Operational notes:** EV is the right rule when (a) you'll face many similar decisions (the law of large numbers averages out variance), and (b) outcomes are on a comparable scale. When either fails — single irreversible decision, or "outcomes" mix dollars with reputation, lives, or strategic position — EV alone misleads. Pair with: (i) variance / worst-case bounds (avoid bet-the-company tails even if EV-positive), (ii) explicit utility transformation if outcomes are non-linear (declining marginal value of money, especially for individuals), (iii) one-way / two-way doors framing (Bezos) for irreversibility. Second discipline: keep the tree small. Beyond ~5 levels deep or ~20 terminal nodes, the structure outruns the team's ability to estimate probabilities meaningfully. When the tree gets unwieldy, prune by subsuming subtrees into single chance-node summaries. Third: always build the sensitivity grid. A decision that's "EV-positive only if probability of success > 0.55" is very different from one robust across 0.2–0.9.
