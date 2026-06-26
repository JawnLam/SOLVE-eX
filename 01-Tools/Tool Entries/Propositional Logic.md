---

Item_ID: tt-propositional-logic
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Propositional Logic
tt_Source: "Frege 1879 / Russell-Whitehead 1910 (formalized); ancient roots in Stoic logic (Chrysippus, c. 280 BCE)"
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: Logical / formal reasoning
tt_Operation: Derive via formal rules
tt_Cross_Domains: []
tt_Form:
- Algorithm
- Mental model
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
tt_Lineage:
- Mathematical / formal
- Western analytic / academic
tt_Posture:
- Expert-required
- Solo-quiet
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Predicate Logic
tt_Often_Follows: []
tt_Pairs_Well_With:
- Modal Logic
- Toulmin Model
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Operation remap → 'Derive via formal rules' (Op #34)"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Truth-functional logic over atomic propositions. The substrate beneath every other formal reasoning tool — predicate logic, Boolean circuits, SAT solvers, theorem provers all extend it."
Needs_Processing: false
AI_Instructions: ''

---

# Propositional Logic

**One-line summary:** A formal system for reasoning about whole statements (atoms) using truth-functional connectives (¬, ∧, ∨, →, ↔), in which validity depends only on the structure of the connectives.

**When to reach for it:** When an argument's correctness needs to be verified independent of content — contracts, policy chains, eligibility rules, debugging conditional logic in code, exposing equivocation in rhetoric.

---

## Purpose Of This Thinking Tool

Propositional logic strips an argument down to its skeleton. Each whole sentence becomes a single letter (P, Q, R…), and the only thing that matters is how those letters are connected — by *and*, *or*, *not*, *if-then*, *iff*. If the connective pattern guarantees the conclusion no matter what the letters mean, the argument is valid. If not, it isn't.

This decoupling of form from content is the move. Most everyday disagreements survive precisely because content gets smuggled into the inference: "if the project is over budget, we must replan" feels obviously true because of *what* "over budget" means, not because the inference structure is sound. Propositional logic asks: would the same pattern hold for any P and Q? If so, the inference is licensed. If not, the conviction was carried by the words, not the reasoning.

The tradition runs from the Stoics (Chrysippus around 280 BCE) through medieval logicians, gets re-engineered by Frege (Begriffsschrift, 1879), and reaches modern form in Russell-Whitehead's *Principia Mathematica*. Its 20th-century descendants — Boolean algebra, satisfiability solvers, SMT, model checkers — power most automated verification.

## Why Use This Thinking Tool

Three failure modes propositional logic prevents:

1. **Affirming the consequent.** "If marketing pushed the launch, sales would spike. Sales spiked, so marketing must have pushed it." This is the most common everyday fallacy and propositional logic catches it instantly: P → Q, Q ⊢ P is invalid.
2. **Hidden disjunctions.** When a stakeholder says "we have to do either A or B," the inclusive vs. exclusive *or* matters operationally. Forcing the connective into ∨ vs. ⊕ makes the assumption explicit.
3. **Conditional drift.** Long policy chains (if eligible → if approved → if funded → then deployed) become un-auditable in prose but trivial as a truth table.

For consulting and operations work, the payoff is auditable rules. A 6-step eligibility policy reduced to a propositional formula can be tested against every input combination, exported to code, and shown to legal without ambiguity.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify atomic propositions — full declarative sentences that are true/false.   |
|    2 | Assign each a letter (P, Q, R, ...).                                            |
|    3 | Translate the argument's connectives: not (¬), and (∧), or (∨), if-then (→).    |
|    4 | Write premises as formulae; write the proposed conclusion separately.           |
|    5 | Test validity: build a truth table OR apply known inference rules.              |
|    6 | If any row makes premises true but conclusion false → invalid. Else → valid.    |
|    7 | If invalid, locate the row(s) where it breaks; that's the counterexample.       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
CONNECTIVE TRUTH TABLES (the operational core)

    P  Q  | ¬P | P∧Q | P∨Q | P→Q | P↔Q
    -------+----+-----+-----+-----+-----
    T  T  | F  |  T  |  T  |  T  |  T
    T  F  | F  |  F  |  T  |  F  |  F
    F  T  | T  |  F  |  T  |  T  |  F
    F  F  | T  |  F  |  F  |  T  |  T

VALID INFERENCE RULES (use these as building blocks)

    Modus Ponens:    P → Q,  P  ⊢ Q
    Modus Tollens:   P → Q, ¬Q  ⊢ ¬P
    Hypothetical Syllogism: P → Q, Q → R ⊢ P → R
    Disjunctive Syllogism:  P ∨ Q, ¬P ⊢ Q
    De Morgan's:     ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
                     ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
    Contrapositive:  P → Q  ≡  ¬Q → ¬P

COMMON FALLACIES (catch yourself / others)

    Affirming the consequent:  P → Q, Q ⊢ P     (INVALID)
    Denying the antecedent:    P → Q, ¬P ⊢ ¬Q   (INVALID)

ARGUMENT WORKSHEET

    Premise 1:  __________________________   →  formula: ____________
    Premise 2:  __________________________   →  formula: ____________
    Premise 3:  __________________________   →  formula: ____________
    Conclusion: __________________________   →  formula: ____________

    Truth-table check:
      Rows where all premises = T ............................... ___
      Of those, rows where conclusion = F ....................... ___
      If 0 → VALID.  If ≥1 → INVALID; counterexample row(s): ___
```

> **Operational notes:** The hardest step is step 1 — identifying *atoms*. People reflexively merge two propositions into one ("the launch was late and over budget" is two atoms, not one). Split aggressively. Also: in business prose, "if" is often *iff* in disguise (especially in policies). Always ask whether the converse is also intended; if yes, write ↔, not →. Finally, propositional logic cannot reason about quantifiers ("all", "some", "no") — at the moment you need to reason across instances of a category, switch to predicate logic.
