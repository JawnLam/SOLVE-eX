---
Item_ID: tt-mills-methods
Item_Prototype: Thinking_Tool
Title: Mill's Methods
tt_Source: "John Stuart Mill 1843 (A System of Logic)"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Empirical / scientific method
tt_Operation: Run experimental cycle
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Algorithm
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Project
tt_Lineage:
- Western analytic / academic
- Scientific method
tt_Posture:
- Beginner-friendly
- Expert-required
tt_State: []
tt_Agent:
- Solo human
- Human group
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Causal DAGs
- Forensic Chain of Custody
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
Quick_Notes: "Five canons of inductive inference: Agreement, Difference, Joint Method, Residues, Concomitant Variation. The discipline that pre-statistical investigators (epidemiology, criminal investigation, troubleshooting) used to localize cause from comparison of cases."
Needs_Processing: false
AI_Instructions: ''
---

# Mill's Methods

**One-line summary:** Five canons of inductive inference (Agreement, Difference, Joint, Residues, Concomitant Variation) for localizing the cause of an effect by structured comparison of cases.

**When to reach for it:** Pre-experimental investigations where you can't randomize but can compare cases — outage diagnosis, epidemiological inquiry, market-anomaly investigation, post-incident root-cause analysis, customer-segment behavior puzzles.

---

## Purpose Of This Thinking Tool

Mill's *System of Logic* (1843) gave a systematic vocabulary to the kind of inferential moves practitioners had been making informally for centuries. The five methods — Agreement, Difference, Joint, Residues, Concomitant Variation — are different patterns for inferring cause from observed cases. They're the inductive-logic toolkit that underlies modern epidemiology (John Snow's cholera-pump localization), industrial troubleshooting (Kepner-Tregoe's Problem Analysis), and bench-science thought-experiments.

The non-obvious operational insight is that each method exploits a different observed pattern, and choosing the right one depends on what data is available. *Agreement* uses the shared feature across cases sharing the effect. *Difference* uses the lone feature distinguishing a case with the effect from one without. *Joint* combines the two. *Residues* subtracts off known causes from a complex effect. *Concomitant Variation* uses the dose-response pattern (more X → more Y).

These methods don't *prove* causation (correlation can deceive even Mill's structured comparisons), but they vastly narrow the hypothesis space and prioritize where to invest experimental effort.

## Why Use This Thinking Tool

Three failure modes the methods prevent:

1. **Unstructured "compare and contrast" diagnosis.** Many investigations rely on intuitive comparison; Mill names the patterns and forces them onto the page.
2. **Premature single-cause fixation.** The methods often surface that *several* features changed together, suggesting the cause is conjunctive — a finding the team would otherwise miss.
3. **Skipping cheap inference.** Where data is observational and randomization isn't possible, Mill's methods are the structured inferential tool — using them is much cheaper than running an experiment.

For consulting, root-cause analysis, and operations work, these methods turn "we have a bunch of cases" into actionable causal hypotheses. Particularly valuable when the team has more cases than time/budget for experimental investigation.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Inventory available cases. For each, record which features were present and    |
|      | whether the effect of interest occurred.                                        |
|    2 | Pick the right method based on what your data supports:                         |
|      |    Agreement — multiple cases with the effect; what feature is shared?         |
|      |    Difference — one with effect, one without, near-identical otherwise         |
|      |    Joint — apply both Agreement and Difference                                 |
|      |    Residues — subtract known causes from a complex effect to isolate residue   |
|      |    Concomitant Variation — does effect intensity track with feature intensity? |
|    3 | Apply the chosen method to localize candidate causes.                          |
|    4 | Treat the result as a hypothesis, not a verdict — confounders may produce      |
|      | spurious patterns.                                                              |
|    5 | Confirm with experimental intervention if possible (RCT-like).                 |
|    6 | If multiple candidates remain, design a discriminating observation that would  |
|      | distinguish them.                                                               |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FIVE METHODS — REFERENCE CARD

    1. METHOD OF AGREEMENT
       If two or more cases have the effect E, and the only feature they share is X,
       then X is the (probable) cause.
       Pattern:   Case A: features {X, P, Q} → E
                  Case B: features {X, R, S} → E
                  → X is candidate cause.

    2. METHOD OF DIFFERENCE
       If one case has E and another nearly identical case does not, and the only
       feature differing is X, then X is the (probable) cause.
       Pattern:   Case A: features {X, P, Q} → E
                  Case B: features {  P, Q} → ¬E
                  → X is candidate cause. (Strongest of Mill's inferences.)

    3. JOINT METHOD OF AGREEMENT AND DIFFERENCE
       Combine the two: cases with E share X and lack other shared features;
       cases without E lack X. Doubly supported candidate cause.

    4. METHOD OF RESIDUES
       If the effect E has known sub-causes (a, b, c) accounting for parts of it,
       and the residue of E (after subtracting their known contributions) remains,
       then the residue is caused by some additional factor.
       Pattern:   E = a-component + b-component + ?
                  → ? is candidate cause for the residue.

    5. METHOD OF CONCOMITANT VARIATION
       If the effect E varies systematically with feature X (intensity, frequency),
       then X and E are causally related (or share a common cause).
       Pattern:   X low  → E low
                  X med  → E med
                  X high → E high
                  → X is candidate cause (or co-effect of common cause).

CASE COMPARISON GRID (the artifact)

    Case  | Feat A | Feat B | Feat C | Feat D | Feat E | Effect E?
    ------|--------|--------|--------|--------|--------|---------
    1     |   ✓    |   ✓    |   ✗    |   ✓    |   ✗    |    Y
    2     |   ✓    |   ✗    |   ✓    |   ✓    |   ✗    |    Y
    3     |   ✗    |   ✓    |   ✗    |   ✓    |   ✓    |    N
    4     |   ✓    |   ✗    |   ✗    |   ✓    |   ✓    |    Y
    5     |   ✗    |   ✓    |   ✓    |   ✓    |   ✗    |    N

    Apply Agreement: which feature is shared across all Y-cases (1,2,4)?  ___
    Apply Difference: pair Y vs N cases that differ minimally; what's the diff?
    Apply Concomitant Variation: any quantitative feature tracking E intensity?

CAVEATS (Mill's known limits)

    • Confounding: a feature correlated with the true cause looks causal under these methods.
    • Joint causes: a cause may require conjunction of features; Mill's methods can miss this.
    • Time order: methods don't establish that X preceded E; verify temporally.
    • Selection: cases observed are not random; selection bias is unaccounted for.
```

> **Operational notes:** Three disciplines. (1) The Method of Difference is the strongest — when you can find two near-identical cases differing only in feature X and outcome E, you have a strong causal inference (essentially a one-shot quasi-experiment). Hunt for this pattern aggressively in observational data. (2) Watch for confounders. A feature that always co-occurs with the true cause will appear causal under Agreement and Difference alike. Always ask "what could be hiding behind this feature?" — and where possible, find a case that decouples them. (3) Mill's methods produce hypotheses, not certainties. Use them to *prioritize* which causal candidate to test experimentally — not as a substitute for the test. Fourth: in practice, you'll often have ragged data where no two cases are nearly identical. The Joint Method, supplemented by the case-comparison grid above, is the workhorse for messy real-world investigations. Fifth: epidemiology's classic Bradford Hill criteria (strength, consistency, specificity, temporality, biological gradient, plausibility, coherence, experiment, analogy) extend Mill's inferential logic — worth pairing if you're doing causal inference at population scale.
