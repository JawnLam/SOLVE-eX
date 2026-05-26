---
Item_ID: tt-ahp
Item_Prototype: Thinking_Tool
Title: AHP (Analytic Hierarchy Process)
tt_Source: "Thomas L. Saaty 1980 (The Analytic Hierarchy Process)"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision analysis
tt_Operation: Score and rank options
tt_Cross_Domains: []
tt_Form:
- Matrix
- Algorithm
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Workshop
tt_Lineage:
- Mathematical / formal
- Industrial / business
tt_Posture:
- Expert-required
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Decision / choice
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Weighted Decision Matrix
- Sensitivity Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Saaty's pairwise-comparison method derives weights via eigenvector of a comparison matrix, with a consistency ratio (CR) that catches incoherent judgments. More rigorous than ad-hoc weighted matrices but heavier — best when stakes justify the workshop time."
Needs_Processing: false
AI_Instructions: ''
---

# AHP (Analytic Hierarchy Process)

**One-line summary:** A multi-criteria decision method that derives criterion weights and option scores from pairwise comparisons (1–9 scale), aggregating via the principal eigenvector of the comparison matrix and reporting a consistency ratio that flags incoherent judgments.

**When to reach for it:** High-stakes selection decisions (large procurement, site selection, major hire) where you want defensible weights, consistency-checked judgments, and a process that surfaces and quantifies stakeholder disagreements.

---

## Purpose Of This Thinking Tool

A weighted decision matrix asks "how important is criterion C, on a 1–5 scale?" — but humans struggle to assign absolute importance ratings. AHP reframes the question as a series of *pairwise comparisons*: "How much more important is C1 than C2? Use this 1–9 scale: 1 equal, 3 moderate, 5 strong, 7 very strong, 9 extreme." Pairwise judgments are cognitively easier than absolute ratings, and AHP's math derives the weights from the comparison matrix's principal eigenvector.

The non-obvious feature is the **consistency ratio (CR)**. If you said C1 is 3× as important as C2, and C2 is 2× as important as C3, you ought to say C1 is roughly 6× as important as C3. AHP computes a CR that measures how much your judgments deviate from this transitivity. A CR > 0.10 flags incoherence — you should revisit the inconsistent comparisons before using the weights. This is a built-in error check no other multi-criteria method offers.

Saaty developed AHP in the 1970s for the U.S. State Department; it became standard in operations research and is now used for procurement (defense, infrastructure), site selection, R&D portfolio prioritization, and supplier evaluation.

## Why Use This Thinking Tool

Three failure modes AHP addresses better than simpler matrices:

1. **Incoherent weights.** Stakeholders' on-the-fly weight assignments are often non-transitive. AHP catches this and forces correction.
2. **Disagreement compression.** When multiple stakeholders disagree on weights, AHP can derive consensus weights from individuals' pairwise matrices (geometric mean of comparisons), which is mathematically defensible.
3. **Hidden hierarchy.** Many decisions involve criteria *and* sub-criteria. AHP's hierarchical structure aggregates pairwise comparisons cleanly across levels.

For high-stakes consulting work, AHP's defensibility is the leverage. A procurement decision documented as "we used AHP, here are the pairwise comparisons, the CR was 0.06, the weights are these, the option-level scores are these" survives scrutiny that an ad-hoc matrix wouldn't.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Build the hierarchy: Goal → Criteria → (Sub-criteria) → Options.                |
|    2 | Pairwise-compare criteria using Saaty's 1–9 scale. Build n×n matrix A.          |
|      |     A_ij = importance of i over j;  A_ji = 1/A_ij                              |
|    3 | Compute weights as the principal eigenvector of A (or geometric mean of rows). |
|    4 | Compute consistency ratio CR. If CR > 0.10, revisit comparisons.                |
|    5 | For each criterion, pairwise-compare the options on that criterion. Repeat the |
|      | weight-derivation procedure to get option scores per criterion.                 |
|    6 | Aggregate: option_score = Σ (criterion_weight × option_score_on_criterion).    |
|    7 | Rank options by aggregate score.                                                |
|    8 | Sensitivity: vary criterion weights ±20%; check if ranking flips.              |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
SAATY'S 1–9 SCALE (the cognitive primitive)

      1  | Equal importance
      3  | Moderate importance of one over the other
      5  | Strong importance
      7  | Very strong importance
      9  | Extreme importance
   2,4,6,8 | Intermediate values

      Reciprocals:  if i over j is k, then j over i is 1/k.

PAIRWISE COMPARISON MATRIX (criteria; n criteria → n×n matrix)

                C1     C2     C3     C4
       C1   [   1     3      5      4   ]
       C2   [  1/3    1      3      2   ]
       C3   [  1/5   1/3     1     1/2  ]
       C4   [  1/4   1/2     2      1   ]

       Weights (geometric mean of rows, normalized):
         w1 = ____,  w2 = ____,  w3 = ____,  w4 = ____   (sum to 1)

CONSISTENCY RATIO

      Compute λ_max = largest eigenvalue of A (or use AHP shortcut).
      Consistency Index CI = (λ_max − n) / (n − 1)
      Random Index RI (lookup):
          n=3 → 0.58    n=4 → 0.90    n=5 → 1.12    n=6 → 1.24
          n=7 → 1.32    n=8 → 1.41    n=9 → 1.45    n=10 → 1.49

      Consistency Ratio CR = CI / RI

      CR ≤ 0.10  →  acceptable
      CR > 0.10  →  REVISIT incoherent comparisons before proceeding

OPTION-LEVEL PAIRWISE COMPARISON (one matrix per criterion)

      For each criterion C_k, build an analogous m×m matrix comparing options.
      Derive option scores s_k per criterion via the same eigenvector method.

AGGREGATION

      Final score of option j = Σ_k (w_k × s_kj)
      Rank options by final score.

GROUP AHP (multiple stakeholders)

      Each stakeholder builds their own pairwise matrix.
      Aggregate via *geometric mean* of stakeholders' judgments per cell
      (NOT arithmetic mean — geometric preserves the reciprocal property).
      Compute weights from the aggregated matrix.
```

> **Operational notes:** Three considerations. (1) Don't use AHP when stakes are low — it's a 2–4-hour workshop tool, more elaborate than the situation may justify. For routine choices, a simple weighted matrix is fine. Save AHP for procurement, site selection, large hires, R&D portfolio cuts. (2) Cap n at ~7 criteria. With 9+ criteria, the comparison matrix becomes unwieldy (36+ pairwise judgments) and CR almost always exceeds 0.10. Use sub-criteria hierarchically instead. (3) The CR is informational, not a verdict. CR > 0.10 means *some* judgment is inconsistent; the team should locate which pair generated the inconsistency and decide whether the issue is a misjudgment or genuine multidimensional value (in which case decompose that criterion). Fourth caveat: AHP has well-known critiques — rank reversal under option addition, scale interpretation, and aggregation method choice. Treat AHP as a structured discussion driver, not as oracle. The artifact (matrix + CR + weights + audit trail) is the deliverable; the rank is one input to a human decision.
