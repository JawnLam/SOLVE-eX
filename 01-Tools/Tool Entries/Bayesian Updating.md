---
Item_ID: tt-bayesian-updating
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Bayesian Updating
tt_Source: "Thomas Bayes (1763, posthumous); Pierre-Simon Laplace 1812"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Algorithm
- Mental model
tt_Scale:
- Solo
- Small group
tt_Duration:
- Snap
- Single session
tt_Lineage:
- Mathematical / formal
- Scientific method
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
tt_Often_Precedes:
- Expected Value Decision Trees
tt_Often_Follows:
- Base Rate Reasoning
tt_Pairs_Well_With:
- Base Rate Reasoning
- Tetlock Superforecasting
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
Quick_Notes: "P(H|E) = P(E|H) × P(H) / P(E). The mathematical engine for revising belief in light of evidence. The hardest discipline is honoring the prior — base rates dominate when evidence is weak, but human intuition flips them."
Needs_Processing: false
AI_Instructions: ''
---

# Bayesian Updating

**One-line summary:** A formal procedure for revising the probability of a hypothesis when new evidence arrives — multiplying the prior probability by the likelihood ratio and re-normalizing.

**When to reach for it:** Diagnostic situations (medical tests, security alerts, due-diligence findings), forecasting updates as news comes in, courtroom-style evidence weighing, and any reasoning where the question is "how much should I update?"

---

## Purpose Of This Thinking Tool

Bayes' theorem is the only mathematically coherent way to combine a prior belief with new evidence. The formula — P(H|E) = P(E|H) × P(H) / P(E) — has three operational components: the **prior** P(H) (what you believed before), the **likelihood** P(E|H) (how strongly the evidence supports the hypothesis vs. its alternatives), and the **posterior** P(H|E) (your revised belief).

The non-obvious operational insight: most belief errors are not about the new evidence — they're about the prior. When base rates are skewed (a rare disease, a rare attacker, a rare event), even strong evidence produces a moderate posterior, because the prior dominates. This is why a 99%-accurate test for a 1-in-10,000 condition still produces mostly false positives. People's intuition routinely ignores priors and treats the test result as conclusive; Bayes corrects this.

The tradition begins with Thomas Bayes (1763, posthumous publication) and was developed into modern form by Laplace. The 20th century saw extensive use in cryptanalysis (Turing at Bletchley), forecasting, medical diagnosis, machine learning, and rationalist epistemology.

## Why Use This Thinking Tool

Three failure modes Bayesian updating prevents:

1. **Base-rate neglect.** Without explicit priors, even a careful analyst over-weights vivid recent evidence and ignores how *rare* the hypothesis is at baseline. Bayes makes the prior a required input.
2. **Single-piece-of-evidence anchoring.** A single test, a single anecdote, a single signal can flip belief if the prior is invisible. Bayes forces the question: how strong is this evidence on the *likelihood-ratio* scale?
3. **Updating without revision rules.** Many teams "incorporate new information" without a formula, leading to either no update or wild swings. Bayes provides a discipline.

For consulting and decision work, the form most often used is the *odds form*: posterior odds = prior odds × likelihood ratio. This avoids the awkward normalization and keeps reasoning fluent during rapid-fire updates.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State hypothesis H precisely. State alternative ¬H or competing H'.             |
|    2 | Set the prior P(H) — the base rate or the belief before this evidence.          |
|    3 | Identify the new evidence E. Be specific about what was observed.               |
|    4 | Estimate the likelihood ratio:  LR = P(E|H) / P(E|¬H).                          |
|    5 | Convert the prior to odds: O(H) = P(H) / (1 − P(H)).                            |
|    6 | Update: posterior odds = prior odds × LR.                                       |
|    7 | Convert posterior odds back to probability if needed.                           |
|    8 | If multiple independent pieces of evidence: multiply LRs sequentially.         |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
BAYES WORKSHEET (odds form — fastest in practice)

    Hypothesis H:       _____________________________________________________
    Alternative ¬H:     _____________________________________________________

    PRIOR
      P(H)    = ______        Prior odds O(H) = P(H) / (1 − P(H)) = ______

    EVIDENCE & LIKELIHOOD RATIO
      Evidence E:          ___________________________________________________
      P(E | H)   = ______
      P(E | ¬H)  = ______
      Likelihood ratio LR = P(E|H) / P(E|¬H) = ______

    UPDATE
      Posterior odds  = O(H) × LR  = ______
      Posterior P(H|E) = posterior odds / (1 + posterior odds) = ______

    ITERATIVE UPDATE (multiple independent pieces of evidence)
      Start with prior odds O(H).
      For each new piece E_i, multiply by LR_i.
      Independence check: does each LR_i remain valid given prior evidence?

LIKELIHOOD-RATIO INTUITION TABLE

      LR    | Interpretation
      ------|-----------------------------------------------------------------
       100  | Strong evidence — flips most moderate priors
        10  | Substantial — typical "positive test" for many diagnostics
         3  | Modest — one consistent observation
         1  | No evidence — observation is equally likely under H or ¬H
       0.3  | Modest evidence against
      0.01  | Strong evidence against

CLASSIC COUNTER-INTUITIVE EXAMPLE

      Disease prevalence (prior):  P(D) = 1/1000
      Test sensitivity:            P(+|D) = 0.99
      Test specificity:            P(−|¬D) = 0.95  →  P(+|¬D) = 0.05

      Prior odds = 1/999
      LR = 0.99 / 0.05 ≈ 20
      Posterior odds = 20/999 ≈ 1/50  →  P(D|+) ≈ 2%

      A "positive" 99%-accurate test for a rare disease still leaves
      a 98% chance you're healthy. Most clinicians get this wrong.
```

> **Operational notes:** Three disciplines compound the value. (1) Always state the prior numerically before looking at the evidence; *don't* let evidence influence what prior you write down — that defeats the math. (2) Use the odds form. Probabilities have an awkward normalization that the odds form sidesteps; it also makes "two pieces of evidence" trivial (multiply LRs). (3) Track *independent* evidence only — correlated evidence (two reports from the same source, two findings from the same dataset) does not multiply cleanly. Stretch each new datapoint with the question "is this independent given the previous evidence?" Fourth: Bayes is for *updating*, not *deciding*. Once you have a posterior, decision theory (expected value over actions × outcomes) takes over. Don't conflate "what do I believe?" with "what should I do?" — they share inputs but answer different questions.
