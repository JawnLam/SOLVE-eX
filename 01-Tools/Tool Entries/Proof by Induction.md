---

Item_ID: tt-proof-by-induction
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Proof by Induction
tt_Source: "Mathematical tradition; foundational use by Pascal (17th c.) on Pascal's triangle, formalized by Peano (1889) in axioms of arithmetic. Modern proof-techniques textbooks."
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: Mathematical / proof reasoning
tt_Operation: Derive via formal rules
tt_Cross_Domains:
- Discursive-analytical
- Modes of inquiry
tt_Form:
- Sequenced workflow
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
- Direct Proof
- Proof by Contradiction
- Proof by Construction
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
Quick_Notes: "For claims of the form 'for all natural numbers n, P(n)'. Two parts: (1) base case — prove P(0) or P(1); (2) inductive step — assume P(k); prove P(k+1). The pair establishes P(n) for all n. Variants: strong induction (assume P(j) for all j ≤ k), structural induction (for recursively-defined structures). Used in number theory, combinatorics, computer science (algorithm correctness, program termination)."
Needs_Processing: false
AI_Instructions: ''

---

# Proof by Induction

**One-line summary:** A proof technique for claims about all natural numbers — prove the base case (n=0 or n=1), then prove that P(k) implies P(k+1) — establishing the claim for all n through a chain of implications.

**When to reach for it:** Mathematical claims about all natural numbers (combinatorics, number theory); algorithm correctness proofs in computer science; structural induction over recursively-defined data structures; mathematical analysis; and any case where you need to prove a claim holds for an infinite sequence by establishing each step from the previous.

---

## Purpose Of This Thinking Tool

**Proof by induction** establishes claims of the form "for all natural numbers n ≥ n₀, P(n)" by:

1. **Base case** — prove P(n₀) directly (often P(0) or P(1)).
2. **Inductive step** — prove that if P(k) is true, then P(k+1) is true. (Called the "inductive hypothesis": assume P(k); derive P(k+1).)

The two together establish P(n) for all n ≥ n₀, by chain reasoning: P(n₀) is true (base case); P(n₀) implies P(n₀+1) (inductive step), so P(n₀+1) is true; P(n₀+1) implies P(n₀+2), so P(n₀+2) is true; and so on.

The non-obvious operational insight is that **the inductive step is the heart of the proof.** The base case is usually trivial. The skill is figuring out how to derive P(k+1) from P(k) — what manipulation, addition, or restatement turns the assumed claim at k into the claim at k+1.

A second insight: **induction is the natural-number version of a more general structural-induction principle.** For any recursively-defined structure (lists, trees, programs), the same logic applies: prove the base structures (empty list, leaf node) and prove that if substructures satisfy the property, the whole satisfies it. Used heavily in computer-science proofs.

A third insight: **strong induction is sometimes needed.** Standard induction assumes only P(k) when proving P(k+1). Strong induction assumes P(j) for all j ≤ k. Some claims need the stronger hypothesis. (Example: every integer ≥ 2 has a prime factorization. Standard induction fails because k+1 doesn't decompose into k+1 - 1 plus one factor; strong induction works because k+1 = a·b where a, b ≤ k.)

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "for all n" hand-wave.** Claims about all natural numbers can't be verified by checking specific cases. Induction provides the rigorous foundation.
2. **The base-case neglect.** Some failed inductive proofs skip the base case; without it, the chain doesn't start. The base case is essential, even when "obvious."
3. **The inductive-step circularity.** The inductive step assumes P(k) and proves P(k+1); confused proofs sometimes assume P(k+1) implicitly. Discipline catches this.

For mathematicians, computer scientists, students of formal systems, and anyone working with recursively-defined structures, induction is essential technique.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the claim: "For all n ≥ n₀, P(n)."                                       |
|    2 | Identify n₀ and P(n) precisely.                                                  |
|    3 | Prove the base case: show P(n₀) directly. Usually computational verification.    |
|    4 | Set up the inductive step. Assume P(k) for arbitrary k ≥ n₀ ("inductive          |
|      | hypothesis"). Goal: prove P(k+1).                                               |
|    5 | Prove P(k+1) using P(k). The key manipulation: how does the claim at k+1        |
|      | relate to the claim at k? Often algebraic; sometimes combinatorial.            |
|    6 | Verify each step. Inductive hypothesis P(k) must be used somewhere; if it's   |
|      | not, you have a direct proof, not an inductive one.                            |
|    7 | Conclude: by induction, P(n) holds for all n ≥ n₀. QED.                        |
|    8 | If standard induction fails, try strong induction (assume P(j) for all j ≤ k)  |
|      | or structural induction (on recursively-defined structure).                    |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE INDUCTION STRUCTURE

   THEOREM: For all n ≥ n₀, P(n).

   PROOF (by induction on n):

   Base case (n = n₀):
       Show P(n₀) directly.
       _______________________________________________

   Inductive step:
       Assume P(k) for arbitrary k ≥ n₀.   [Inductive hypothesis]
       Goal: prove P(k+1).
       Step 1: ______________________________________
       Step 2: ______________________________________
       ...
       Therefore P(k+1).

   By mathematical induction, P(n) holds for all n ≥ n₀.
   QED.

THE WORKED EXAMPLE

   THEOREM: For all n ≥ 1, 1 + 2 + 3 + ... + n = n(n+1)/2.

   PROOF (by induction on n):

   Base case (n = 1):
       Left side: 1.
       Right side: 1(1+1)/2 = 1.
       Equal. ✓

   Inductive step:
       Assume 1 + 2 + ... + k = k(k+1)/2.   [Inductive hypothesis]
       Goal: 1 + 2 + ... + (k+1) = (k+1)(k+2)/2.
       
       1 + 2 + ... + (k+1) = (1 + 2 + ... + k) + (k+1)
                           = k(k+1)/2 + (k+1)        [by inductive hyp]
                           = (k+1)(k/2 + 1)
                           = (k+1)(k+2)/2.

   By induction, the formula holds for all n ≥ 1. QED.

   Note: the inductive hypothesis was used explicitly to
   substitute k(k+1)/2 for the partial sum.

THE STRONG-INDUCTION VARIANT

   When standard induction's hypothesis (P(k) only) is
   insufficient:

   THEOREM: Every integer n ≥ 2 has a prime factorization.

   PROOF (by strong induction):

   Base case (n = 2):
       2 is prime. Done. ✓

   Inductive step:
       Assume every j with 2 ≤ j ≤ k has a prime factorization.
       [Strong inductive hypothesis]
       Goal: prove k+1 has a prime factorization.

       Case 1: k+1 is prime. Then k+1 = k+1 (prime
       factorization).
       Case 2: k+1 is composite. Then k+1 = a · b for some
       2 ≤ a, b ≤ k. By inductive hypothesis, a and b have
       prime factorizations. Combining gives a prime
       factorization of k+1.

   By strong induction, every n ≥ 2 has a prime factorization.

   Standard induction wouldn't work because k+1 doesn't
   decompose into k + 1; we need the factor decomposition.

THE STRUCTURAL-INDUCTION VARIANT

   For recursively-defined structures (lists, trees,
   formulas):

   To prove a property P holds for all structures:
   1. Prove P holds for the base case structures (empty list,
       leaf node).
   2. Assume P holds for the substructures (sub-lists, child
       nodes); prove P holds for the structure built from
       them.

   Used heavily in computer-science correctness proofs.

   Example: For all binary trees T, |T| = number of leaves +
   number of internal nodes - 1. Proved by structural induction
   on tree structure.

THE INDUCTIVE-STEP-DEPENDENCE CHECK

   The inductive hypothesis P(k) MUST be used somewhere in
   the proof of P(k+1). If not, you have a direct proof for
   each n, not an inductive one.

   Diagnostic: highlight where in the inductive step you used
   "by inductive hypothesis." If you can't, reconsider whether
   induction is the right technique.

THE COMMON-PITFALLS CATALOG

   1. SKIPPED BASE CASE
        "Obviously P(0) is true." Recovery: explicitly prove
        the base case.

   2. WRONG BASE CASE
        Starting at the wrong n₀. Recovery: verify that P
        actually holds at the chosen base.

   3. INDUCTIVE HYPOTHESIS NOT USED
        Proof of P(k+1) doesn't depend on P(k). Recovery: the
        proof is direct, not inductive.

   4. CIRCULARITY
        Assuming P(k+1) implicitly while proving P(k+1).
        Recovery: trace dependencies carefully.

   5. STRONG INDUCTION CONFUSED WITH STANDARD
        Using P(j) for j < k while claiming standard induction.
        Recovery: explicitly state which form is being used.

   6. STRUCTURAL INDUCTION ON ILL-DEFINED STRUCTURE
        Recursive structure not actually well-founded.
        Recovery: ensure base cases exist; recursion always
        terminates.

THE COMPUTER-SCIENCE APPLICATIONS

   ALGORITHM CORRECTNESS:
       Prove an iterative algorithm produces correct output
       by inducting on iteration number.
       Base: initial state satisfies invariant.
       Step: each iteration preserves invariant.
       Termination: invariant + termination condition →
       correct output.

   PROGRAM TERMINATION:
       Show some natural-number measure decreases on each
       step. By well-ordering of naturals, decrease must
       terminate.

   DATA STRUCTURE PROPERTIES:
       Properties of recursively-defined trees, lists,
       graphs proved by structural induction.

THE OPERATIONAL TEMPLATE

   Claim: For all n ≥ n₀, P(n)
       n₀ = ____________________
       P(n) = __________________

   Base case (P(n₀)):
       Verification: ___________________________________

   Inductive step:
       Assume P(k) (for k ≥ n₀).
       Goal: prove P(k+1).
       Steps using inductive hypothesis:
       _______________________________________________

   Verification: did inductive hypothesis get used? Y / N

   By induction, conclusion: ____________________________
```

> **Operational notes:** Four disciplines. (1) The base case is essential, even when "obvious." Without the base, the chain doesn't start. Always prove it explicitly. (2) The inductive hypothesis must be used in the inductive step. If it's not, you have a direct proof for each n, not an induction. (3) Match technique to claim. Standard induction for natural-number-indexed claims; strong induction when P(k) alone is insufficient; structural induction for recursively-defined structures. (4) Watch for circularity. The inductive step assumes P(k) and derives P(k+1) — making sure P(k+1) isn't assumed implicitly is part of the rigor.
