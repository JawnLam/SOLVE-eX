---
Item_ID: tt-differential-diagnosis
Item_Prototype: Thinking_Tool
Title: Differential Diagnosis
tt_Source: "Medical tradition; foundational analyses by Lawrence Weed (problem-oriented medical record); modern clinical-reasoning literature: Pat Croskerry, Geoffrey Norman."
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: Clinical reasoning
tt_Operation: Categorize situation type
tt_Cross_Domains:
- Discursive-analytical
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Question bank
- Decision tree
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Western analytic / academic
- Scientific method
tt_Posture:
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
tt_Often_Precedes:
- Evidence Pyramids
tt_Often_Follows: []
tt_Pairs_Well_With:
- Evidence Pyramids
- Bayesian Updating
- Clinical Heuristics
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Body / embodiment', 'Decision / choice']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Generate a list of candidate diagnoses (the differential), then progressively narrow through tests / observations. Operational rules: 'common things are common' (favor higher-prevalence diagnoses); 'don't miss diagnoses' (always include serious / treatable conditions even if low probability); use Bayesian updating as evidence accumulates. Avoids both premature closure (stopping at first plausible diagnosis) and analysis paralysis (failing to narrow). Transfer: works for any diagnostic problem, not just medical."
Needs_Processing: false
AI_Instructions: ''
---

# Differential Diagnosis

**One-line summary:** A diagnostic method that generates a list of candidate diagnoses (the differential) and progressively narrows through tests, observations, and Bayesian updating — balancing the goals of "common things are common" with "don't miss diagnoses" that are dangerous if untreated.

**When to reach for it:** Medical / clinical practice (foundational); IT troubleshooting (analogous structure); root-cause analysis in operations / quality / safety; any diagnostic problem where multiple causes could produce observed symptoms.

---

## Purpose Of This Thinking Tool

Differential diagnosis is the foundational method of medical clinical reasoning. The structure:

1. **Generate the differential** — list candidate diagnoses that could explain the presentation
2. **Estimate priors** — how common is each? (Base rates matter.)
3. **Identify "don't miss" diagnoses** — serious / treatable conditions that must be excluded even if low probability
4. **Test / observe** — gather information that distinguishes among candidates
5. **Update** — adjust probabilities based on evidence (Bayesian)
6. **Narrow** — eliminate inconsistent candidates; focus on remaining
7. **Diagnose** — when probability is high enough for the relevant diagnosis to drive treatment

The non-obvious operational insight is that **the discipline balances two distinct failure modes:**

- **Premature closure** — accepting the first plausible diagnosis without ruling out alternatives. Common error in time-pressured clinical contexts; produces missed diagnoses.
- **Analysis paralysis** — endless testing without converging on a diagnosis. Produces delayed treatment and unnecessary procedures.

The differential structure addresses both: the explicit list prevents premature closure (you can see what alternatives haven't been ruled out); the prioritization by probability and danger prevents paralysis (you focus on the highest-yield narrowing tests, not all possible tests).

A second insight: **"common things are common" + "don't miss diagnoses" together produce the right priority order.** The most common diagnosis matching the symptoms gets primary investigation; serious-but-less-common diagnoses get explicit exclusion if their tests are tractable. The combination prevents both the overuse of low-yield tests and the under-attention to dangerous conditions.

A third insight: **the structure transfers beyond medicine.** IT troubleshooting (what could be causing this error?), engineering root-cause analysis (what could explain this failure?), and ethics-committee case analysis (what type of case is this?) all use the same logic — generate alternatives, test progressively, narrow through evidence.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The premature-closure trap.** Accepting the first plausible diagnosis misses real alternatives. The differential list keeps alternatives visible.
2. **The "everything could be everything" paralysis.** Without prioritization, testing all possibilities is impractical. The framework's prioritization (probability + danger) makes the search tractable.
3. **The base-rate neglect.** Reasoning from symptoms to diagnoses without considering prior probabilities produces "rare disease" overweighting. Bayesian updating with explicit priors corrects this.

For physicians, IT engineers, root-cause analysts, and any diagnostician, differential diagnosis is foundational. The discipline of explicit alternatives + progressive narrowing transfers across domains.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | List the presentation. Symptoms, signs, context, history. Be specific.          |
|    2 | Generate the differential. Include common diagnoses matching the presentation,  |
|      | plus serious / treatable conditions ("don't miss").                             |
|    3 | Estimate priors for each. Use base rates from the relevant population.           |
|    4 | Identify discriminating tests. Which tests / observations would change the      |
|      | probability of one diagnosis vs. another?                                       |
|    5 | Run the highest-yield test first. Yield = expected information change × ease.   |
|    6 | Update probabilities with results. Consistent with diagnosis A? Probability     |
|      | rises. Inconsistent? Probability falls. Bayesian.                                |
|    7 | Narrow. Eliminate diagnoses inconsistent with evidence. Continue testing on     |
|      | remaining candidates.                                                            |
|    8 | Diagnose when one diagnosis dominates probability AND drives appropriate        |
|      | treatment. Don't continue testing once treatment is clear.                       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE DIFFERENTIAL TEMPLATE

   Presentation: ______________________________________________

   DIFFERENTIAL DIAGNOSIS:
   1. _____________________ Prior probability: _________
   2. _____________________ Prior probability: _________
   3. _____________________ Prior probability: _________
   ...

   "DON'T MISS" diagnoses (must exclude even if low prior):
   _____________________ (rationale: _________________)
   _____________________ (rationale: _________________)

   DISCRIMINATING TESTS:
   Test:                 What it discriminates between:
   _____________________ _____________________________
   _____________________ _____________________________

   PROBABILITY UPDATE AFTER EACH TEST:
   Test result:          Updated probabilities:
   _____________________ _____________________________

   CURRENT WORKING DIAGNOSIS:
   _____________________________________________________
   Confidence: _________________________________________
   Treatment plan / further testing: ___________________

THE PRIORITIZATION RULE

   For each diagnosis, consider:
       Prior probability (base rate × pre-test fit)
       Danger if missed (severity × treatability × time-sensitivity)

   Test priority = (Prior × Danger × Discrimination value) / Cost

   Highest-priority test gets run first.

   Common things are common: high priors get attention.
   Don't miss diagnoses: high danger gets explicit exclusion.

   Both rules together produce the right priority sequence.

THE COMMON-DIAGNOSIS STARTING POINTS

   In medicine, common things really are common:
       Headache → tension, migraine, sinus, viral infection
                  (much rarer: tumor, hemorrhage, meningitis)
       Chest pain → musculoskeletal, GERD, anxiety
                    (don't miss: MI, PE, dissection)
       Fatigue → sleep, depression, viral, anemia
                 (don't miss: hypothyroid, malignancy, cardiac)

   For each common presentation, there's a learned pattern of
   common diagnoses + don't-miss conditions. Mature clinical
   training teaches both.

   Same structure transfers:
   IT troubleshooting:
       Slow web app → high CPU on app server, DB query
                       slow, network latency
                       (don't miss: cache miss, deadlock,
                       memory leak escalating)

   Operations:
       Production line failure → operator error, equipment
                                  drift, material variation
                                  (don't miss: control
                                  software bug, SCADA issue)

THE BAYESIAN UPDATE PATTERN

   For each test result:

   Posterior P(disease | result) = 
       (Sensitivity × Prior P(disease)) /
       (Sensitivity × Prior + (1 - Specificity) × (1 - Prior))

   Practical: track probabilities ordinally if not numerically.
   - Result strongly supports A: A's probability rises substantially.
   - Result inconsistent with B: B's probability falls substantially.
   - Result ambiguous: small or no probability change.

   Updates compound. After several tests, one diagnosis often
   dominates while others fade.

THE WHEN-TO-STOP RULE

   Continue narrowing until:
   1. One diagnosis has high probability AND
   2. The treatment for that diagnosis is clear AND
   3. The cost of further testing exceeds the value of further
       certainty.

   Stopping criterion is treatment-driven, not certainty-driven.
   You don't need 100% certainty before treatment if treatment
   for the dominant diagnosis is clearly correct.

   Common error: continuing to test past the treatment-decision
   threshold. Adds cost without changing care.

THE COMMON FAILURE MODES

   1. PREMATURE CLOSURE
        Accepting first plausible diagnosis. Recovery: explicit
        differential; test alternatives.

   2. ANCHORING
        Sticking with initial diagnosis after evidence shifts.
        Recovery: re-evaluate differential after each test.

   3. AVAILABILITY BIAS
        Recent / memorable diagnoses overweighted. Recovery:
        use base rates explicitly.

   4. BASE-RATE NEGLECT
        Reasoning from symptoms to diagnoses without priors.
        Recovery: explicit Bayesian framing.

   5. ANALYSIS PARALYSIS
        Endless testing. Recovery: stopping rule
        (probability × treatment-relevance > test cost).

   6. SKIPPING "DON'T MISS"
        Failing to exclude serious diagnoses even when low
        probability. Recovery: explicit "don't miss" list.

THE NON-MEDICAL TRANSFER

   For any diagnostic problem:

   1. List candidate causes (the differential).
   2. Estimate prior probability of each.
   3. Identify "don't miss" causes (serious if true).
   4. Identify discriminating tests / observations.
   5. Run highest-yield test first.
   6. Update probabilities; narrow.
   7. Diagnose when one cause dominates and treatment is clear.

   Same structure. Different domain. The discipline transfers
   directly.
```

> **Operational notes:** Four disciplines. (1) Generate the differential explicitly. The list itself prevents premature closure — you can see what hasn't been ruled out. Skip this step and you will accept the first plausible answer. (2) "Common things are common" + "don't miss" together. Common diagnoses get primary investigation; serious-but-rare diagnoses get explicit exclusion. The combination prevents both the missed-rare-disease and the unnecessary-rare-disease-testing failures. (3) Stop on treatment-relevance, not certainty. Continue narrowing until one diagnosis is dominant AND treatment is clear. Beyond that, additional testing adds cost without changing care. (4) The structure transfers. IT troubleshooting, root-cause analysis, ethics case analysis, business diagnosis all use the same moves. Medical practice is the most-developed instance, but the discipline is domain-general.
