---

Item_ID: tt-counterfactual-reasoning
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Counterfactual Reasoning
tt_Source: "David Lewis 1973 (Counterfactuals); Robert Stalnaker 1968; modern causal-inference treatment Pearl 2009 (do-operator)"
tt_Type: instrument
tt_Domain: Speculative / imaginative
tt_Field: Counterfactual reasoning
tt_Operation: Imagine counterfactually
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Question bank
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Western analytic / academic
- Mathematical / formal
tt_Posture:
- Beginner-friendly
- Collaborative-willing
tt_State:
- Speculative-imaginative
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
- Decision / choice
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Pre-Mortem
- Causal DAGs
tt_Often_Follows:
- After Action Review
tt_Pairs_Well_With:
- Modal Logic
- Real Options Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=['Speculative-imaginative'], tt_Agent=['Solo human'], tt_About=['Mind / cognition', 'Decision / choice']"
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Operation remap → 'Imagine counterfactually' (Op #30)"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Lewis–Stalnaker semantics: 'if A had been the case, B would have been' is true iff in the closest possible world where A holds, B also holds. The 'closest world' constraint is what distinguishes counterfactuals from material conditionals."
Needs_Processing: false
AI_Instructions: ''

---

# Counterfactual Reasoning

**One-line summary:** Disciplined reasoning about "what would have happened if X had been different" — by specifying a minimal alteration to the actual world and tracing its causal consequences forward.

**When to reach for it:** Post-mortems, attribution analyses ("did marketing actually cause the lift?"), policy evaluation, learning-from-failure, and any decision review that asks "would this have happened anyway?"

---

## Purpose Of This Thinking Tool

Counterfactual reasoning is the engine behind every causal claim and every learning loop. To say "X caused Y" is to say "if X had not happened, Y would not have happened" — a counterfactual claim about a non-actual world. To learn from a project's success or failure requires asking "would this outcome have occurred anyway?" — again, counterfactual.

David Lewis's 1973 semantics gave the formalism: "if A then B" (counterfactual) is true iff B holds in the *closest possible world* where A holds. "Closest" means minimally altered from the actual world along all dimensions except A. Pearl's causal-inference machinery (do-calculus, structural equation models) gave the computational form: a counterfactual is the value Y would take under the intervention do(X = x'), evaluated within the assumed structural model.

The non-obvious operational insight: a sloppy counterfactual either alters too much ("if we'd had a different team, a different strategy, and twice the budget — outcome would have been Z") or too little ("if we'd just renamed the feature"). The discipline is to specify *one* clean change and let the rest of the world be as it was, then think hard about which downstream effects propagate and which don't.

## Why Use This Thinking Tool

Three failure modes the disciplined version prevents:

1. **Hindsight overconfidence.** "We should have seen it coming" usually compares the actual outcome to a fantasy world where everything else also went well. A real counterfactual specifies *one* change and traces consequences — often discovering the alternative was no better.
2. **Attribution to causes that didn't move.** "Marketing drove the lift" is testable counterfactually: would the lift have occurred without marketing? If yes, the attribution is wrong.
3. **Magical alternatives.** Without the "closest world" constraint, people invent alternatives that violate physical, financial, or organizational reality. The discipline forces the alternative to be reachable from the actual world.

For consulting and post-mortem work, counterfactuals turn "we should have done better" into "what *specifically* would have been different, and would that have been enough?" — which is the only kind of lesson that transfers.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Pick the actual outcome you want to explain or attribute.                       |
|    2 | Identify ONE candidate cause whose role you want to test.                       |
|    3 | Specify the minimal alternative: "what would the world look like if exactly     |
|      | this one variable had been different, and everything not causally downstream of |
|      | it had remained the same?"                                                      |
|    4 | Trace causal consequences forward: which effects propagate? Which do not?       |
|    5 | Estimate the counterfactual outcome in this world.                              |
|    6 | Compare counterfactual outcome to actual outcome. The difference is the        |
|      | causal contribution of the candidate cause.                                     |
|    7 | Stress-test: try a few "nearby" counterfactuals. If they yield wildly           |
|      | different conclusions, the answer is sensitive — admit it.                      |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
COUNTERFACTUAL WORKSHEET

    Actual outcome (Y_actual): ___________________________________________________

    Candidate cause to test (X): _________________________________________________
    X actually took value:  X = x_actual
    Counterfactual value:   X = x' (specify): __________________________________

    THE MINIMAL-ALTERATION CHECK
      Variables held FIXED in the counterfactual world (not causally downstream of X):
        ____________________________________________________________________________
        ____________________________________________________________________________

      Variables that necessarily CHANGE (causally downstream of X):
        ____________________________________________________________________________
        ____________________________________________________________________________

    CAUSAL TRACE
      X = x'  →  effect on M_1: ______________________________________________
              →  effect on M_2: ______________________________________________
              →  effect on Y:   ______________________________________________
                  (Y_counterfactual = ____________)

    CAUSAL CONTRIBUTION
      Y_actual − Y_counterfactual = ________________
      Interpretation: this is what the candidate cause contributed.

    SENSITIVITY CHECK (try nearby counterfactuals)
      What if X = x'' instead?  Y becomes ________
      What if X = x' AND M_1 also held to baseline?  Y becomes ________
      Are conclusions stable across these variations?  □ yes  □ no — flag

    PRE-MORTEM SIBLING (use after a failure)
      What's the closest possible world where this NOT failed?
        Single change:        _________________________________________________
        Resulting Y:          _________________________________________________
        Was that change actually reachable from where we were?  □ yes  □ no

DISTINGUISHING REAL FROM FANTASY COUNTERFACTUALS

    Test                                   | Real        | Fantasy
    ---------------------------------------|-------------|------------------------
    Reachable from actual world (1 step)?  | yes         | no — we'd need many things
    Coheres with known causal structure?   | yes         | no — violates physics/policy/org
    Specifies a single intervention?       | yes         | no — bundles many changes
    Predicts checkable side-effects?       | yes         | no — only the desired result moves
```

> **Operational notes:** The most common error in business post-mortems is the bundled counterfactual — "if we'd had a better team, better timing, and more capital." Such alternatives are not learnable from. Force the team to pick *one* lever and ask whether moving just that lever (with realistic propagation) would have been enough. Often it wouldn't, which is itself a finding. Second: counterfactuals are not material conditionals. "If we had launched in February → we'd have hit Q1" is NOT a P → Q claim — it asserts something about the closest world where we did launch in February. Use Lewis-Stalnaker semantics (closest-world), not classical logic. Third: when comparing strategies, run counterfactuals in both directions ("what if we had done X" and "what if we hadn't done Y") — symmetry of consideration prevents post-hoc attribution to whichever choice we're emotionally invested in.
