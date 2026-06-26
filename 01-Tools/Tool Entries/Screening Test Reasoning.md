---
Item_ID: tt-screening-test-reasoning
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: Screening Test Reasoning (Sn/Sp/PPV/NPV)
tt_Source: "Sackett, D. L., et al. (1991). Clinical Epidemiology: A Basic Science for Clinical Medicine. Little, Brown."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Quantitative & probabilistic reasoning
tt_Operation: Calibrate confidence
tt_Cross_Domains: []
tt_Form:
  - Matrix
  - Algorithm
tt_Scale:
  - Solo
tt_Duration:
  - Single session
tt_Lineage:
  - Medical / clinical
  - Mathematical / formal
tt_Posture:
  - Expert-required
tt_State: []
tt_Agent:
  - Solo human
  - Human-AI partnership
tt_About:
  - Risk / uncertainty
  - Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With: []
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-12 — initial classification (Sprint 03 — Deep-Gap Backfill Card 09)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Quantitative reasoning frame for evaluating diagnostic tests — Sensitivity, Specificity, Positive Predictive Value, Negative Predictive Value — where PPV and NPV depend on pre-test probability."
Needs_Processing: false
AI_Instructions: ""
---

# Screening Test Reasoning (Sn/Sp/PPV/NPV)

**One-line summary:** Quantitative reasoning frame for evaluating diagnostic tests — Sensitivity, Specificity, Positive Predictive Value, Negative Predictive Value — where PPV and NPV depend on pre-test probability.

**When to reach for it:** Evaluating or selecting a diagnostic test, interpreting a test result, or counseling a patient about test meaning — especially where pre-test probability varies across populations.

## Purpose

Screening Test Reasoning provides the quantitative frame for understanding diagnostic test performance: (1) Sensitivity = true positives / (true positives + false negatives) — the fraction of disease-present patients the test catches; (2) Specificity = true negatives / (true negatives + false positives) — the fraction of disease-absent patients the test correctly clears; (3) Positive Predictive Value = TP/(TP+FP) — probability of disease given a positive test; (4) Negative Predictive Value = TN/(TN+FN) — probability of no disease given a negative test. Crucial insight: Sn and Sp are properties of the test; PPV and NPV depend on pre-test probability. The same test performs differently in different populations. Bayesian at core.

## How To Use

For a test in question: (1) Look up or compute Sn and Sp. (2) Estimate the pre-test probability of disease in the relevant population. (3) Use the 2x2 table or Bayes' rule to compute PPV and NPV at that pre-test probability. (4) For a positive test, interpret PPV: how confident is the diagnosis? For a negative test, interpret NPV: how confident is the rule-out? (5) Critically: in a low-prevalence population, even a sensitive and specific test has poor PPV — many positives are false. In a high-prevalence population, even a less-good test has good PPV. The cognitive discipline: never interpret a test result without thinking about pre-test probability in the population the patient comes from. Likelihood ratios (LR+ = Sn/(1-Sp), LR- = (1-Sn)/Sp) offer a streamlined version that updates pre-test odds to post-test odds.

## Sources

- Sackett, D. L., et al. (1991). *Clinical Epidemiology: A Basic Science for Clinical Medicine*. Little, Brown.
- Pauker, S. G., & Kassirer, J. P. (1980). 'The threshold approach to clinical decision making.' *NEJM* 302(20).
- Trevethan, R. (2017). 'Sensitivity, Specificity, and Predictive Values.' *Frontiers in Public Health* 5.
