---
Item_ID: tt-weighted-decision-matrix
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Weighted Decision Matrix
tt_Source: "Stuart Pugh 1981 (Pugh concept selection method); folk roots in industrial decision-making"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision analysis
tt_Operation: Score and rank options
tt_Cross_Domains: []
tt_Form:
- Matrix
- Scoring rubric
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Industrial / business
- Design / craft tradition
tt_Posture:
- Beginner-friendly
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
tt_Often_Precedes:
- Sensitivity Analysis
tt_Often_Follows: []
tt_Pairs_Well_With:
- AHP (Analytic Hierarchy Process)
- Kepner-Tregoe
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "A.k.a. Pugh matrix or decision matrix. Options as rows, criteria as columns, weights along the top, scores in cells, weighted sum in the right column. The Pugh variant uses +/0/− scoring against a baseline rather than absolute scores — often more robust."
Needs_Processing: false
AI_Instructions: ''
---

# Weighted Decision Matrix

**One-line summary:** A matrix in which options are scored against weighted criteria, the weighted sum of each option's scores producing a ranking — the workhorse multi-criteria decision tool.

**When to reach for it:** Vendor selection, hire-vs-hire choices, design concept down-selection, prioritization between projects with multiple criteria — any decision where 3+ options must be compared on 3+ criteria with different importance.

---

## Purpose Of This Thinking Tool

The weighted decision matrix forces three implicit moves into explicit form: (1) what criteria matter, (2) how much each matters relative to the others (weights), (3) how each option performs on each criterion (scores). The weighted sum collapses the three into a ranking. Crucially, *the value is in the construction* — most disagreements collapse once weights and scores are visible to all stakeholders.

The non-obvious insight: the *Pugh variant* (Stuart Pugh, 1981) is often superior to absolute scoring. Instead of scoring each option 1–10, the team picks one option as a baseline (often the status quo) and scores all others as +1 / 0 / −1 vs. the baseline on each criterion. This dodges scale calibration problems and surfaces relative advantages directly. Used iteratively (re-run with each round's winner as the new baseline), Pugh matrices converge on robust choices rather than ones with peculiar scoring artifacts.

The technique entered design engineering through Pugh's *Total Design* and product-development practice through QFD (Quality Function Deployment). It is now standard in vendor evaluation, RFP scoring, design selection, and procurement.

## Why Use This Thinking Tool

Three failure modes explicit weighted matrices prevent:

1. **Hidden weighting.** Decisions made by gut secretly weight some criteria heavily and others lightly; the matrix surfaces this for inspection.
2. **Loud-criterion dominance.** Absent explicit weights, whichever criterion the loudest stakeholder champions (usually the most recently discussed) dominates.
3. **Apples-to-oranges comparison.** Options often have different strengths on different criteria; without normalization and weighting, comparison is qualitative and prone to flip on framing.

For consulting and procurement work, the matrix is auditable: every score and weight has an owner, can be defended, and can be revised. The artifact survives the meeting; the gut-feel doesn't.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | List the options (rows). Aim for 3–8.                                           |
|    2 | List the decision criteria (columns). Cover hard requirements separately —     |
|      | "must-haves" should be filters, not weighted criteria.                          |
|    3 | Filter options against must-haves. Eliminate any that fail.                     |
|    4 | Assign weights to criteria. Common scales: 1–5 importance; or 100-point split. |
|    5 | Score each option on each criterion. Choose:                                   |
|      |     Absolute scoring: 1–10 (or 1–5)                                            |
|      |     Pugh scoring:  +1 / 0 / −1 vs. a baseline option                           |
|    6 | Compute weighted sum per option. Rank.                                          |
|    7 | Sensitivity-test: change each weight by ±20%; do the rankings flip?            |
|    8 | Document the rationale per cell. The audit trail is the deliverable.           |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
WEIGHTED DECISION MATRIX (absolute scoring)

      Criterion (weight)   |  C1  (w=4) |  C2  (w=5) |  C3  (w=3) |  C4  (w=2) | Σ w·s
      ---------------------|------------|------------|------------|------------|------
      Option A             |     8      |     5      |     7      |     9      |  84
      Option B             |     6      |     8      |     6      |     5      |  82
      Option C             |     9      |     4      |     9      |     6      |  79
      Option D             |     5      |     9      |     5      |     7      |  84

      Rank by Σ w·s:  A & D tied (84) > B (82) > C (79)

PUGH MATRIX (relative scoring vs. baseline)

      Criterion (weight)   |  C1 (4) |  C2 (5) |  C3 (3) |  C4 (2) | Σ
      ---------------------|---------|---------|---------|---------|-----
      Option A (BASELINE)  |   0     |   0     |   0     |   0     |  0
      Option B             |  +1     |  +1     |  −1     |  −1     |  +4
      Option C             |  +1     |  −1     |  +1     |  −1     |  0
      Option D             |  −1     |  +1     |  −1     |  +1     |  0

      B leads. Iterate: make B the new baseline, re-score, repeat.

MUST-HAVE FILTER (apply BEFORE scoring)

      Option | Must-have 1 | Must-have 2 | Must-have 3 | Pass?
      -------|-------------|-------------|-------------|-------
      A      |     YES     |     YES     |     YES     | proceed
      B      |     YES     |     NO      |     YES     | reject
      ...

SENSITIVITY GRID (vary weights by ±20%)

      Top contender holds at:  □ all weight perturbations
                               □ most  □ a few  □ flips easily

      If ranking flips at small weight perturbations, the decision is fragile —
      either tighten weights with stakeholder consensus or admit the options
      are effectively tied.
```

> **Operational notes:** Three disciplines compound the value. (1) Separate must-haves from weighted criteria. A criterion can be either binary (hard requirement; option is filtered out if it fails) or scored (graceful degradation). Mixing them produces incoherent rankings — a heavily weighted "must-have" still permits a high-scoring option that fails the requirement. (2) Build weights *before* listing options. Listing options first biases weights toward criteria where favored options happen to do well. (3) Always run weight sensitivity. Most contested decisions are within 5–10% of being a tie; a robust answer is one that wins at most plausible weight settings, not just the modal one. Fourth: when scores are subjective (vendor "ease of use"), have multiple stakeholders score independently and compare — divergence of >2 points on a 10-point scale is itself diagnostic information about how well-defined the criterion is.
