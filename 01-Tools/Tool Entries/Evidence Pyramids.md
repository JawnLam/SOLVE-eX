---
Item_ID: tt-evidence-pyramids
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Evidence Pyramids
tt_Source: "Evidence-based medicine tradition. Origin: Sackett et al., 'Evidence-based medicine: what it is and what it isn't' (BMJ 1996); Cochrane Collaboration; modern formulations (e.g., Greenhalgh, How to Read a Paper)."
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: Clinical reasoning
tt_Operation: Apply question bank
tt_Cross_Domains:
- Modes of inquiry
- Discursive-analytical
tt_Form:
- Mental model
- Heuristic
- Visualization technique
tt_Scale:
- Solo
- Small group
- Civilizational
tt_Duration:
- Single session
tt_Lineage:
- Western analytic / academic
- Scientific method
tt_Posture:
- Beginner-friendly
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Body / embodiment
- Decision / choice
tt_SOLVE_eX_Phase: [5, 6]
tt_SOLVE_eX_Step: [5.1, 6.1]
tt_Clarifies: ['Path', 'Action']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Differential Diagnosis
- Bayesian Updating
- Falsification
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Body / embodiment', 'Decision / choice']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Hierarchy of evidence quality, from highest to lowest: systematic reviews / meta-analyses → randomized controlled trials → cohort studies → case-control studies → case series / reports → expert opinion. Used in evidence-based medicine to weight competing claims by evidence quality. Caveats: pyramids are heuristic; specific study quality matters more than design type alone; some evidence types (mechanism, ecological) are missing from classical pyramid."
Needs_Processing: false
AI_Instructions: ''
---

# Evidence Pyramids

**One-line summary:** A hierarchy of evidence quality — systematic reviews / meta-analyses at the top, expert opinion at the bottom — used to weight competing claims about clinical practice and any empirical question by the strength of the evidence supporting them.

**When to reach for it:** Evidence-based medical practice; literature review and synthesis; assessing competing claims in any empirical domain (policy, business, social science); writing systematic reviews; evaluating expert testimony.

---

## Purpose Of This Thinking Tool

The **evidence pyramid** orders evidence types by quality:

```
                  TOP (highest quality)
                  Systematic reviews / meta-analyses
                  Randomized controlled trials (RCTs)
                  Cohort studies
                  Case-control studies
                  Case series / reports
                  Expert opinion
                  BOTTOM (lowest quality)
```

The non-obvious operational insight is that **evidence quality is partially about study design and partially about how the evidence type addresses confounders.** RCTs are higher than observational studies because random assignment controls for unmeasured confounders. Systematic reviews are higher than single studies because they aggregate across studies and can identify replication patterns. Expert opinion is at the bottom because it's vulnerable to anchoring, motivated reasoning, and small-sample experience.

The pyramid produces practical rules for evidence-based practice:

- **When evidence types disagree, weight by quality.** A meta-analysis of RCTs trumps a single observational study.
- **When higher-quality evidence is missing, use what's available.** Expert opinion isn't worthless; it's just lower in the hierarchy.
- **When evaluating a claim, ask "what's the highest-quality evidence available?"** That's the relevant evidence.

A second insight: **specific study quality matters more than design type alone.** A poorly-designed RCT can be worse than a well-designed cohort study. The pyramid is heuristic; rigorous evidence appraisal looks at internal validity (was the study well-conducted?) and external validity (does it apply to my population?) within the design type.

A third insight: **some evidence types are missing from the classical pyramid.** Mechanistic evidence (does this drug actually work biologically?), ecological evidence (population-level patterns), qualitative evidence (mechanisms of patient experience) all add to picture but don't fit cleanly. Modern evidence frameworks (GRADE, AHRQ) supplement the pyramid with explicit criteria.

The framework extends beyond medicine to any empirical claim. Policy evaluation, marketing analytics, organizational research, and other applied-empirical domains use analogous hierarchies.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The expert-anecdote overweighting.** Expert opinion based on small samples is often wrong. Recognizing its low position in the hierarchy puts it in proportion.
2. **The single-study fixation.** A single positive study often gets cited as if it proves a claim. The pyramid recommends looking for systematic reviews and replication.
3. **The evidence-type confusion.** Different study designs answer different questions; using observational data to answer a causal question (where RCT is the right tool) produces wrong conclusions.

For physicians, researchers, policy-makers, and any consumer of empirical claims, the evidence pyramid is foundational reasoning structure.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the empirical claim. What's being asserted? Causal? Correlational?     |
|      | Mechanistic?                                                                     |
|    2 | Identify the highest-quality evidence available. Search systematic reviews,     |
|      | RCTs, cohort studies, etc.                                                       |
|    3 | Evaluate study quality. Internal validity (was it well-conducted?). External    |
|      | validity (does it apply to your population?).                                    |
|    4 | Weight the evidence. Higher-quality evidence carries more weight; lower         |
|      | doesn't get zero, but it's less decisive.                                        |
|    5 | Look for replication. Is the finding consistent across multiple high-quality    |
|      | studies? Replication strengthens; non-replication weakens.                       |
|    6 | Address competing evidence. Are there high-quality studies disagreeing?         |
|      | Acknowledge and explain.                                                          |
|    7 | Apply with appropriate confidence. High-quality consistent evidence supports    |
|      | confident claims; mixed lower-quality evidence supports tentative claims.       |
|    8 | Update. New evidence shifts the picture; periodically re-evaluate.              |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE CLASSICAL EVIDENCE PYRAMID

                    SYSTEMATIC REVIEWS / META-ANALYSES
                    (synthesize across multiple high-quality
                     studies; highest evidence for therapy /
                     prevention questions)

                    RANDOMIZED CONTROLLED TRIALS (RCTs)
                    (random assignment controls for
                     confounders; gold standard for causal
                     claims about interventions)

                    COHORT STUDIES (prospective)
                    (follow groups over time; observational;
                     vulnerable to confounders; better than
                     case-control for prevalent outcomes)

                    CASE-CONTROL STUDIES
                    (compare cases vs. controls retrospectively;
                     useful for rare outcomes; vulnerable to
                     recall and selection bias)

                    CASE SERIES / CASE REPORTS
                    (descriptions of individual cases; useful
                     for hypothesis generation; weak for
                     causal claims)

                    EXPERT OPINION
                    (anchoring, motivated reasoning, small-
                     sample experience; lowest weight when
                     other evidence available)

THE QUESTION-TYPE-DEPENDENCE

   Different questions favor different evidence types:

   THERAPY / PREVENTION: RCTs are gold standard.
   ETIOLOGY (cause): cohort > case-control.
   DIAGNOSIS: cross-sectional studies of test characteristics.
   PROGNOSIS: cohort studies.
   FREQUENCY: cross-sectional surveys.

   The pyramid implicitly assumes therapy / prevention
   questions; for other questions, the right design varies.

THE QUALITY-WITHIN-DESIGN APPRAISAL

   Beyond design type, study quality matters:

   For RCTs:
       - Random assignment actually random?
       - Allocation concealed?
       - Outcome assessors blinded?
       - Intent-to-treat analysis?
       - Adequate sample size?
       - Loss to follow-up minimal?

   For cohort studies:
       - Selection of comparison group?
       - Loss to follow-up?
       - Confounding addressed?

   For systematic reviews:
       - Comprehensive search?
       - Quality appraisal of included studies?
       - Heterogeneity addressed?

   Rigorous evaluation uses tools like CONSORT (RCTs),
   STROBE (observational), PRISMA (systematic reviews),
   AMSTAR-2 (systematic reviews).

THE GRADE FRAMEWORK (modern evolution)

   Grading of Recommendations Assessment, Development and
   Evaluation (GRADE) refines the pyramid:

   Quality of evidence: HIGH / MODERATE / LOW / VERY LOW
   Strength of recommendation: STRONG / WEAK

   Quality is downgraded for:
       Risk of bias
       Inconsistency across studies
       Indirectness (different population / outcome)
       Imprecision (wide confidence intervals)
       Publication bias

   Quality is upgraded for:
       Large effect size
       Dose-response relationship
       Plausible confounders likely UNDERESTIMATING effect

   GRADE produces more nuanced quality assessments than
   the simple pyramid.

THE COMMON ERRORS

   1. CHERRY-PICKING
        Citing only studies supporting desired conclusion.
        Recovery: systematic search; address competing
        evidence.

   2. SINGLE-STUDY FIXATION
        One positive study treated as conclusive.
        Recovery: look for replication; prefer systematic
        reviews.

   3. CORRELATION-CAUSATION CONFUSION
        Observational evidence cited for causal claims when
        RCTs would be possible.
        Recovery: match design to question type.

   4. EXPERT-OPINION OVERWEIGHT
        Treating expert testimony as decisive.
        Recovery: ask for the underlying evidence; experts
        can be wrong.

   5. P-HACKING / SIGNIFICANCE-CHASING
        Finding p < 0.05 by trying many analyses; statistical
        significance ≠ clinical significance.
        Recovery: pre-registered hypotheses; effect sizes;
        replication.

THE HIERARCHY-IN-PRACTICE

   For a clinical or empirical claim:

   1. Search systematic reviews (Cochrane, PROSPERO, PubMed).
   2. If reviews available: weight conclusions by review quality.
   3. If no reviews: search RCTs; assess quality.
   4. If no RCTs: cohort, then case-control, then case series.
   5. Expert opinion: useful for context, not for primary
       evidence.

   The hierarchy guides search strategy as well as evidence
   weighting.

THE TRANSFER BEYOND MEDICINE

   Policy evaluation:
       Systematic reviews of policy effects > single
       evaluations > expert opinion.

   Marketing analytics:
       Multi-experiment meta-analysis > single A/B test >
       single observational analysis > expert intuition.

   Educational research:
       Cluster RCTs > propensity-score matched cohorts >
       single-site case studies > expert experience.

   Organizational research:
       Multi-organization studies with comparable controls >
       single-organization case studies > expert opinion.

   Same hierarchy logic; different study designs available
   in each domain.

THE OPERATIONAL TEMPLATE

   Empirical claim: ____________________________________

   Highest-quality evidence available: ________________
       Study type: __________________
       Quality assessment: __________

   Replication / consistency check: ____________________

   Competing evidence: _________________________________

   Conclusion (with appropriate confidence): __________

   How to update if new evidence emerges: ______________
```

> **Operational notes:** Four disciplines. (1) Match the question to the design. Therapy questions need RCTs; prognosis needs cohort; frequency needs cross-sectional. The pyramid implicitly assumes therapy questions; use design types appropriate for the actual question. (2) Quality-within-design matters as much as design type. A well-designed cohort can be more valuable than a poorly-designed RCT. Look at internal and external validity, not just design type. (3) Replication is essential. Single studies — even well-designed ones — should be treated tentatively until replicated. Systematic reviews aggregate across studies and identify replication patterns. (4) Modern frameworks (GRADE) refine the simple pyramid. Use them where available; the simple pyramid is adequate for quick orientation but insufficient for rigorous evidence appraisal.
