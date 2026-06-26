---

Item_ID: tt-direct-proof
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Direct Proof
tt_Source: "Mathematical tradition; Euclid's Elements (~300 BCE) gives early systematic examples. Modern mathematical-reasoning textbooks: Velleman, How to Prove It; Hammack, Book of Proof."
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: Mathematical / proof reasoning
tt_Operation: Derive via formal rules
tt_Cross_Domains:
- Discursive-analytical
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Mental model
- Algorithm
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
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Proof by Contradiction
- Proof by Induction
- Proof by Construction
- Propositional Logic
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Operation remap → 'Derive via formal rules' (Op #34)"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Most basic proof technique: assume the hypothesis, derive the conclusion through a chain of logical steps. Each step justified by axiom, definition, prior theorem, or inference rule. Used for if-then claims (P → Q): assume P, derive Q. Most concrete and widely-applicable proof method; foundation of mathematical practice. Transferable to legal argument, scientific demonstration, and any sustained reasoned argument."
Needs_Processing: false
AI_Instructions: ''

---

# Direct Proof

**One-line summary:** The most basic proof technique — assume the hypothesis, derive the conclusion through a chain of logical steps each justified by axiom, definition, prior theorem, or inference rule — used for if-then claims throughout mathematics and rigorous argument.

**When to reach for it:** Mathematical proofs (foundational); legal argument with formal structure; scientific demonstration of causal claims; rigorous logical analysis; software verification; and any reasoning context where the goal is to establish that a conclusion follows from assumptions.

---

## Purpose Of This Thinking Tool

A **direct proof** of an if-then statement (P → Q) proceeds:

1. **Assume P** (the hypothesis).
2. **Derive intermediate steps** through valid logical inference, with each step justified by:
   - An axiom (foundational assumed truth)
   - A definition (precise meaning of a term)
   - A previously-proved theorem
   - An inference rule (modus ponens, universal instantiation, etc.)
3. **Conclude Q** as the final step.

The non-obvious operational insight is that **the chain of justifications is the proof.** A claim that's true is not yet a proof; the proof is the explicit chain showing how the conclusion follows from the hypothesis using only sanctioned moves. Mathematicians distinguish "I think it's true" from "I have proved it" precisely on this basis.

Direct proof is the foundation of mathematical practice. Most theorems are proved directly; other proof methods (contradiction, induction, construction) are used when direct proof is awkward or impossible.

A second insight: **direct proof requires unpacking definitions.** Many proofs proceed by replacing terms with their definitions and showing how the conclusion's definition follows. The discipline of explicit definition-unpacking is the bulk of many proof attempts.

A third insight: **the same logic applies beyond mathematics.** Legal argument: assume facts; apply applicable law (definitions and rules); derive verdict. Scientific argument: state premises (data + theoretical principles); apply valid inference; conclude. Even rigorous everyday argument follows this structure when held to standard.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "obvious" trap.** Claims that "obviously follow" often don't, or follow through unstated steps that turn out to be wrong. Direct proof requires explicit chains.
2. **The unjustified-step pattern.** Proofs that include steps without justification can hide errors. The discipline of "what justifies this step?" catches them.
3. **The vague-conclusion failure.** "Therefore X" without showing the logical chain leaves the conclusion unsupported. Direct proof produces explicit grounding.

For mathematicians, lawyers, scientists, software engineers, and anyone making rigorous arguments, direct proof is foundational reasoning structure.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the claim to prove. Usually in if-then form: "If P, then Q."              |
|    2 | Identify the hypothesis P and the conclusion Q precisely. Unpack any definitions.|
|    3 | Assume P. Write it explicitly.                                                   |
|    4 | Derive intermediate steps. Each step requires explicit justification: axiom,    |
|      | definition, prior theorem, or inference rule.                                    |
|    5 | When stuck, consider what additional definitions, theorems, or techniques       |
|      | might help. Search for analogous proofs.                                         |
|    6 | Reach Q. Verify it matches the claim's conclusion exactly (not "close enough").  |
|    7 | Review. Does each step have explicit justification? Are there gaps?             |
|    8 | If gaps exist, fill them or restate the claim more carefully.                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE DIRECT-PROOF STRUCTURE

   THEOREM: If P, then Q.

   PROOF:
       Assume P.                                        [Hypothesis]
       Step 1: ___________________________________      [Justification]
       Step 2: ___________________________________      [Justification]
       ...
       Step n: ___________________________________      [Justification]
       Therefore Q.                                      [Conclusion]
       QED.

   The justifications are the proof, not the steps.

THE STANDARD JUSTIFICATIONS

   Axiom — assumed without proof (e.g., parallel postulate)
   Definition — meaning of a term (e.g., even number = 2k)
   Theorem — previously proved
   Inference rule:
       Modus ponens: from P and (P→Q), conclude Q
       Universal instantiation: from ∀x P(x), conclude P(a)
       Existential generalization: from P(a), conclude ∃x P(x)
       (And several others.)

   A step lacking explicit justification is a gap in the proof.

THE WORKED EXAMPLE (simple case)

   THEOREM: If n is an even integer, then n² is also even.

   PROOF:
       Assume n is an even integer. (Hypothesis)
       By definition of even, n = 2k for some integer k.
       Then n² = (2k)² = 4k² = 2(2k²).
       Let m = 2k². Then m is an integer.
       Therefore n² = 2m, so n² is even by definition of even.
       QED.

   Each step has a justification (definition, algebra, definition).
   The chain establishes the conclusion from the hypothesis.

THE DEFINITION-UNPACKING DISCIPLINE

   Many proofs reduce to unpacking definitions:

   Hypothesis: A is in B.
   Definition of B: ... [unpacked condition]
   Apply hypothesis: ... [show condition holds]
   Conclude: A satisfies the condition.

   When stuck, ask: "What does X mean by definition?"
   The answer often opens the path forward.

THE WHEN-DIRECT-DOESN'T-WORK

   Some claims resist direct proof. Alternatives:

   PROOF BY CONTRADICTION:
       Assume the negation; derive a contradiction.
       Useful when negation is easier to manipulate.

   PROOF BY INDUCTION:
       For claims about all natural numbers; prove base
       case + inductive step.

   PROOF BY CONSTRUCTION:
       For existence claims; explicitly exhibit the object.

   See separate entries.

THE PROOF-WRITING DISCIPLINE

   1. Start with explicit statement.
   2. Justify every non-trivial step.
   3. Use definitions explicitly when needed.
   4. Number / label steps for review.
   5. End with explicit verification of conclusion.
   6. Have someone else read; gaps often visible to fresh eye.

THE COMMON FAILURE MODES

   1. SKIPPED STEPS
        "Clearly..." "It follows that..." without justification.
        Recovery: explicit justification for every step.

   2. AMBIGUOUS DEFINITIONS
        Using terms without precise definitions. Recovery:
        unpack definitions explicitly.

   3. CIRCULAR REASONING
        Using the conclusion to prove itself. Recovery: trace
        dependencies; ensure no step depends on the conclusion.

   4. WRONG INFERENCE RULE
        Drawing conclusions that aren't valid (affirming the
        consequent, etc.). Recovery: check inference rules.

   5. NOT-QUITE-Q CONCLUSION
        Reaching something close to but not exactly Q.
        Recovery: check that final step matches claim.

THE NON-MATHEMATICAL APPLICATIONS

   Direct proof structure transfers:

   LEGAL ARGUMENT:
       Hypothesis: facts of the case + applicable law
       Steps: apply legal rules to facts, justify with statute /
       precedent
       Conclusion: legal verdict

   SCIENTIFIC ARGUMENT:
       Hypothesis: data + theoretical premises
       Steps: apply principles, justify with theory / observation
       Conclusion: scientific claim

   ENGINEERING DEMONSTRATION:
       Hypothesis: system specifications + operating conditions
       Steps: apply engineering principles
       Conclusion: system property (safety, performance, etc.)

   Same structure: assume, derive with justification, conclude.

THE OPERATIONAL TEMPLATE

   Claim: ____________________________________________________

   Hypothesis P: _____________________________________________

   Conclusion Q: _____________________________________________

   Definitions to unpack: ____________________________________

   Available theorems: _______________________________________

   Proof outline:
       Step 1: ______________________ Justification: _________
       Step 2: ______________________ Justification: _________
       ...
       Step n: ______________________ Justification: _________

   Conclusion verification: __________________________________

   Review (gaps?): ___________________________________________
```

> **Operational notes:** Four disciplines. (1) Each step needs explicit justification. The justifications are the proof; the steps without them are just claims. The discipline of "why is this step valid?" is the foundational proof skill. (2) Unpack definitions. Many proofs come down to substituting precise definitions for terms and showing how the conclusion's definition follows. When stuck, ask what terms mean. (3) When direct proof doesn't work, switch methods. Some claims are awkward to prove directly but elegant via contradiction, induction, or construction. Recognize when to switch. (4) The structure transfers beyond mathematics. Legal argument, scientific demonstration, engineering analysis all use the same logical structure when held to rigorous standard. Mathematical proof is the most-developed instance, but the discipline applies broadly.
