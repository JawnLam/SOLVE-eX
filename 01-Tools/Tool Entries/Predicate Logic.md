---

Item_ID: tt-predicate-logic
Item_Prototype: Thinking_Tool
Title: Predicate Logic
tt_Source: "Frege 1879 (Begriffsschrift); refined by Peirce, Russell, Hilbert, Gödel"
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
- Modal Logic
tt_Often_Follows:
- Propositional Logic
tt_Pairs_Well_With:
- Propositional Logic
- Causal DAGs
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Operation remap → 'Derive via formal rules' (Op #34)"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Extends propositional logic with quantifiers (∀, ∃) and predicates over individuals — i.e., reasoning *across* members of a category. The base language of mathematics, contracts, and database queries (SQL is essentially a fragment of predicate logic)."
Needs_Processing: false
AI_Instructions: ''

---

# Predicate Logic

**One-line summary:** A formal system that adds quantifiers (∀ "for all", ∃ "there exists") and predicates over individuals to propositional logic, enabling reasoning about whole classes of things rather than just whole sentences.

**When to reach for it:** When the argument depends on quantification — "every customer", "no employee", "at least one supplier" — and you need to verify whether the inference is sound across the entire class, not just a particular instance.

---

## Purpose Of This Thinking Tool

Predicate logic answers a question propositional logic cannot: *what counts as a counterexample to a rule about a population?* "Every senior engineer should pass the code review threshold" is not one statement — it's an implicit promise that every individual in a set satisfies a property. Predicate logic makes that promise explicit, and lets you check it.

The decisive add over propositional logic is the universal quantifier (∀, "for all") and the existential quantifier (∃, "there exists"), bound to a domain of discourse. This is the language in which mathematics is written, in which legal contracts handle "all parties of the second part", in which SQL queries expressed (`WHERE` and `EXISTS` are existential quantifiers; `GROUP BY ... HAVING` reasons over universals). It's also the language in which argumentation about populations, policies, and cohort behavior becomes precise.

Frege invented this in 1879 to give arithmetic a logical foundation. Russell, Whitehead, Hilbert, and Gödel completed and stress-tested the project across the next 60 years. The result is the bedrock formal system underlying every other rigorous discipline: type theory, theorem proving, logic programming, formal verification.

## Why Use This Thinking Tool

It catches three errors that look identical in natural language:

1. **Universal-existential confusion.** "Customers churn when support is slow" sounds like ∀ but usually means ∃. Forcing the choice clarifies whether the claim is "every slow ticket caused a churn" (false) or "some churns followed slow tickets" (much weaker).
2. **Vacuous truth.** ∀x P(x) is trivially true if there are no x. Many policies ("all qualifying employees receive bonus B") need an existence clause to mean what people think they mean.
3. **Scope confusion.** "Every project has a manager" (∀p ∃m manages(m, p)) is very different from "Some manager runs every project" (∃m ∀p manages(m, p)). Quantifier order matters operationally — the second sentence describes a single-point-of-failure org structure.

For policy design, contracts, and metric definitions, predicate logic is the discipline that prevents shipped ambiguity. Once a metric or rule is formulated in predicate logic, it becomes implementable and auditable.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the domain of discourse — the set of objects under discussion.         |
|    2 | List predicates: properties (P(x)) and relations (R(x,y)) that apply to them.   |
|    3 | Translate quantifiers explicitly: "all"=∀, "some"=∃, "no"=¬∃, "only"=careful.   |
|    4 | Pay close attention to quantifier *order* — ∀∃ ≠ ∃∀ in general.                 |
|    5 | Write premises and conclusion as well-formed formulae.                          |
|    6 | Test by attempted counter-model: invent a small domain where premises hold      |
|      | but conclusion fails. If you can't, the argument is likely valid.               |
|    7 | For policy/contract use: enumerate edge cases (empty set, single element, etc.) |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
QUANTIFIER TRANSLATION TABLE

    Natural language phrase                    | Logical form
    -------------------------------------------|------------------------------
    All As are B                               | ∀x (A(x) → B(x))
    Some A is B                                | ∃x (A(x) ∧ B(x))
    No A is B                                  | ¬∃x (A(x) ∧ B(x))  ≡  ∀x (A(x) → ¬B(x))
    Not all As are B                           | ¬∀x (A(x) → B(x))  ≡  ∃x (A(x) ∧ ¬B(x))
    Only As are B                              | ∀x (B(x) → A(x))
    Every A has some B related to it           | ∀x (A(x) → ∃y R(x, y))
    Some B is related to every A               | ∃y ∀x (A(x) → R(x, y))   [stronger!]

QUANTIFIER NEGATION (De Morgan for quantifiers)

    ¬∀x P(x)  ≡  ∃x ¬P(x)
    ¬∃x P(x)  ≡  ∀x ¬P(x)

VALID INFERENCE RULES

    Universal Instantiation:   ∀x P(x) ⊢ P(a)        (any a in domain)
    Existential Generalization: P(a) ⊢ ∃x P(x)
    Universal Generalization:   P(a) for arbitrary a ⊢ ∀x P(x)

POLICY-AUDIT WORKSHEET

    Domain of discourse: ___________________________________________
    Predicates used:
      A(x) := __________________________________________________
      B(x) := __________________________________________________
      R(x,y) := ________________________________________________

    Policy in natural language:  __________________________________
    Policy as formula:           __________________________________
    Empty-set behavior?  (vacuously true / explicitly excluded)  ___
    Quantifier-order risk?  (∀∃ vs ∃∀ confusion possible?)        ___
    Edge case enumeration:
      [ ] domain has 0 elements
      [ ] domain has exactly 1 element
      [ ] some predicate is everywhere-false
      [ ] some predicate is everywhere-true
```

> **Operational notes:** The single highest-leverage skill is reading "every X has a Y" and immediately asking *which Y per X?*. Almost every policy bug in the wild traces back to ∀∃ vs ∃∀ confusion. Second: in legal and policy contexts, "only" is dangerous — it inverts the conditional ("only employees can vote" = voter → employee, not employee → voter). Third: when stuck, search for a counter-model rather than a proof. A small domain with 2-3 elements is often enough to falsify a tempting but invalid inference.
