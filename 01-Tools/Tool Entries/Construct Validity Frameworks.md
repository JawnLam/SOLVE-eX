---
Item_ID: tt-construct-validity-frameworks
Item_Prototype: Thinking_Tool
Title: Construct Validity Frameworks
tt_Source: "Cronbach & Meehl 1955 (Construct Validity in Psychological Tests); Campbell & Fiske 1959 (multitrait-multimethod matrix)"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Stress-test a position
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Question bank
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Western analytic / academic
- Scientific method
tt_Posture:
- Expert-required
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
- Human group
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- KPI Design
tt_Often_Follows: []
tt_Pairs_Well_With:
- KPI Design
- Goodhart-Aware Metric Selection
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human', 'Human group'], tt_About=['Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "The discipline of asking 'does my measure actually measure what I claim it does?' Cronbach & Meehl distinguished four validity types: content, criterion, convergent, discriminant. The MTMM matrix (multitrait-multimethod) is the canonical empirical test."
Needs_Processing: false
AI_Instructions: ''
---

# Construct Validity Frameworks

**One-line summary:** A discipline for evaluating whether a measurement actually captures the abstract concept it claims to measure — using content, criterion, convergent, and discriminant validity tests, plus the multitrait-multimethod matrix.

**When to reach for it:** Designing surveys, KPIs, performance measures, or any quantitative indicator where the gap between "what we measure" and "what we mean" carries operational consequences.

---

## Purpose Of This Thinking Tool

Construct validity asks the most underrated question in measurement: *does this measure actually measure what we claim it does?* Many measures are reliable (consistent) and operational (well-defined), yet measure something different from what their name suggests. "Engagement score" might predict tenure but reflect something closer to "satisfaction with manager" — a related but distinct construct. Without construct-validity discipline, organizations optimize for proxies instead of the things proxies were supposed to represent.

The non-obvious operational insight is that construct validity is *empirical*, not definitional. You don't establish it by defining the construct carefully; you establish it by demonstrating that the measure (a) covers the construct's content (content validity), (b) predicts criterion outcomes that the construct should predict (criterion validity), (c) correlates with other measures of the same construct (convergent validity), and (d) does NOT correlate with measures of distinct-but-related constructs (discriminant validity).

Cronbach and Meehl (1955) formalized the concept; Campbell and Fiske (1959) added the multitrait-multimethod (MTMM) matrix as the empirical test. The framework is foundational in psychometrics, social science, and increasingly in organizational measurement design.

## Why Use This Thinking Tool

Three failure modes the discipline prevents:

1. **Name-fallacy.** A measure called "innovation index" doesn't necessarily measure innovation. The discipline forces evidence over labels.
2. **Single-method confound.** A construct measured only one way (e.g., self-report survey) often reflects the *method* (response bias, social desirability) more than the construct.
3. **Drift over time.** A measure validated once stays in use as the underlying conditions shift; periodic re-validation catches drift.

For consulting and operations work, construct-validity discipline is what separates a measurement system that drives the right behavior from one that drives unintended optimization. It also surfaces situations where the construct itself isn't well-defined — that's a prior problem to solve before measurement.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the construct precisely. What do you mean by [innovation / engagement /  |
|      | quality]? Aim for a definition a stranger could read and apply.                 |
|    2 | Specify the measure: how is it computed, from what source, on what schedule?    |
|    3 | Content validity: does the measure cover the breadth of the construct?         |
|      | Identify expected facets and verify each is reflected in the measure.           |
|    4 | Criterion validity: what outcomes should the construct predict? Test the        |
|      | measure's predictive power against those outcomes.                              |
|    5 | Convergent validity: take a second, methodologically-different measure of the   |
|      | same construct. They should correlate strongly.                                 |
|    6 | Discriminant validity: take a measure of a different construct. They should     |
|      | correlate less than the convergent pair.                                        |
|    7 | Build the MTMM matrix: traits × methods. Check that same-trait-different-method |
|      | correlations exceed different-trait-same-method correlations.                   |
|    8 | If validity fails: the measure or the construct (or both) needs revision. Don't|
|      | scale measurement until validity is acceptable.                                 |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
CONSTRUCT-VALIDITY WORKSHEET

    Construct name: ________________________________________________________
    Construct definition (one paragraph): __________________________________

    Measure: _______________________________________________________________
      Source / data: _______________________________________________________
      Computation: _________________________________________________________
      Scale / range: _______________________________________________________

    CONTENT VALIDITY
      Expected facets of the construct:
        a. ________________________________________________________________
        b. ________________________________________________________________
        c. ________________________________________________________________
      For each, where does the measure capture it?
        a. _______________   b. _______________   c. _______________
      Coverage rate:  ___ / ___ facets covered

    CRITERION VALIDITY
      Outcomes the construct should predict:
        Y1: ______________________________  Correlation with measure: ____
        Y2: ______________________________  Correlation with measure: ____
        Y3: ______________________________  Correlation with measure: ____

    CONVERGENT VALIDITY
      Alternative measure of same construct: ____________________________
      Correlation between measures: ____  (target: > 0.6)

    DISCRIMINANT VALIDITY
      Measure of distinct-but-related construct: ________________________
      Correlation: ____   (should be smaller than convergent correlation)

    MTMM MATRIX (multitrait-multimethod) — an example for two traits, two methods

                       Trait1/M1  Trait1/M2  Trait2/M1  Trait2/M2
       Trait1/M1            1.0
       Trait1/M2            ____      1.0                          ← convergent (high)
       Trait2/M1            ____      ____      1.0                ← method (lower)
       Trait2/M2            ____      ____      ____       1.0     ← discriminant (lowest)

       Pattern check:
         Same-trait-diff-method (convergent) > Diff-trait-same-method (method) >
         Diff-trait-diff-method (discriminant) ≈ 0

       If the pattern doesn't hold, the measure may be capturing method or the
       trait/construct distinction may be artificial.

VALIDITY DIAGNOSIS

    Symptom                                       | Likely problem
    ----------------------------------------------|--------------------------------
    Content coverage gaps                         | Measure too narrow
    No criterion correlation                      | Measure or construct not predictive
    Low convergent correlation                    | Measures not capturing same construct
    High method-fixed-effect (column variance)    | Method bias dominates trait
    High discriminant correlation                 | Two constructs aren't distinct

REMEDIATION OPTIONS

    [ ] Expand measure to cover missing facets
    [ ] Reduce method bias by triangulating across data sources
    [ ] Refine construct definition (constructs may be conflated)
    [ ] Replace measure if structural problems can't be fixed
    [ ] Acknowledge measure as proxy and report alongside the construct it stands for
```

> **Operational notes:** Three disciplines. (1) The single most diagnostic test is the multi-method check. If your construct can only be measured one way (one survey, one observed metric), method-vs-construct is confounded. Always seek at least one second method — even crude — to triangulate. (2) Define the construct *before* designing the measure. Many measurement programs design metrics that are easy to compute, then retrofit a definition. The result is operationally tight but constructively meaningless. (3) Re-validate periodically. Constructs and their measures drift apart as conditions change (employee surveys done in office vs. remote era, NPS in B2C vs. B2B). Annual or post-major-change re-validation catches drift before policies based on the measure go awry. Fourth: when validity is low, the temptation is to dismiss the measure and pick a new one. Often the construct itself is poorly specified — a "wellbeing index" that doesn't validate may reflect that wellbeing isn't a unitary construct, requiring decomposition into recognizable sub-constructs.
