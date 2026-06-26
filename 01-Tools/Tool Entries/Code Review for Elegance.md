---
Item_ID: tt-code-review-for-elegance
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Code Review for Elegance Rubric
tt_Source: "Synthesis of multiple traditions: Rich Hickey, *Simple Made Easy* (2011); Kent Beck, *Smalltalk Best Practice Patterns* (1997) and the four rules of simple design; Robert Martin, *Clean Code* (2008); Brian Goetz on Java idiom; Donald Knuth on programming-as-literature (*Literate Programming*, 1992)."
tt_Type: instrument
tt_Domain: Aesthetic
tt_Field: Code review for elegance & quality
tt_Operation: Refine a draft / artifact
tt_Cross_Domains:
  - Symbolic systems
  - Phronetic / practical wisdom
tt_Form:
  - Checklist
  - Scoring rubric
tt_Scale:
  - Solo
  - Dyadic
  - Small group
tt_Duration:
  - Single session
tt_Lineage:
  - Design / craft tradition
  - Industrial / business
tt_Posture:
  - Expert-required
  - Collaborative-willing
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Aesthetic / craft
  - Mind / cognition
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1]
tt_Clarifies: ['Path']
tt_Applicability: describable_only
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Design Critique Format
  - Connoisseurship Training
  - Kantian Aesthetic Judgment Frame
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: C
tt_History:
  - "2026-05-11 — initial classification (Zero-Gap Sweep Card 08; closes Field 'Code review for elegance & quality')"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-11
Date_Modified: 2026-05-11
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Distinct from standard code review (correctness, security, performance). This rubric addresses code-as-craft: simplicity (Hickey's 'simple ≠ easy'), Beck's four rules (passes tests, reveals intent, no duplication, fewest elements), naming, locality of reference, surprise minimization. Used to elevate code review beyond bug-hunting into aesthetic discipline. Risk: subjective enough that it requires shared vocabulary in the reviewing team to function."
Needs_Processing: false
AI_Instructions: ""
---

# Code Review for Elegance Rubric

**One-line summary:** A rubric for code review that goes beyond correctness/security/performance into code-as-craft criteria — simplicity vs ease, intent-revealing names, locality, surprise-minimization — so that reviews build aesthetic discrimination, not just catch bugs.

**When to reach for it:** Senior engineering teams where bug-catching review is well-established but craft-level critique has stagnated; design-conscious software organizations; teaching contexts where new engineers need to develop taste, not just correctness; in libraries or APIs whose readability determines downstream adoption.

---

## Purpose Of This Thinking Tool

Most code review focuses on *correctness* (does it work?), *security* (is it exploitable?), and *performance* (is it fast enough?). These are necessary but not sufficient. There is a separate axis: **code-as-craft** — whether the code is *elegant*, whether it *reveals intent*, whether it could be read as literature (Knuth) or sculpture (Hickey).

The non-obvious operational claim: **elegance is not subjective enough to dismiss but not objective enough to automate.** It rewards apprenticeship: developing taste through exposure to clearly-elegant and clearly-inelegant code, in the company of practitioners with developed taste. The rubric is the structured scaffold for that apprenticeship.

Several traditions converge on similar criteria:

- **Beck's Four Rules of Simple Design** (in priority order): passes the tests; reveals intent; no duplication; fewest elements.
- **Hickey's "Simple Made Easy"** (2011): simple = un-braided; easy = familiar. Simple is a property of the code; easy is a property of the relationship between code and reader. Optimize for simple, accept that simple is sometimes initially harder for the reader.
- **Locality of reference**: to understand this code, how far do I have to look? Local code is easier to reason about than code requiring global tracking.
- **Surprise minimization**: principle of least astonishment. Does the code do what its surface suggests?
- **Naming**: do names reveal intent? Is `c` a customer, a count, a coefficient?

A second insight: **elegance dimensions sometimes conflict.** Removing duplication can hurt readability; revealing intent can require more elements. The rubric's value is making these trade-offs *visible*, not pre-resolving them.

## Why Use This Thinking Tool

Three failure modes the rubric prevents:

1. **Bug-only review.** Teams whose review caught bugs but never elevated code quality. The rubric introduces craft as a review dimension.
2. **Taste-as-vibe.** "I think this is ugly" without a vocabulary for *why*. The rubric provides shared terms.
3. **Cleverness-as-elegance.** Code that's short or surprising but actually obscures intent. Hickey's "simple ≠ easy" disentangles.

The rubric's evidence base is craft-tradition (decades of programming-as-craft writing) rather than empirical (the empirical-software-engineering literature has done little on aesthetic quality directly).

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|  1   | Apply standard review first: correctness, security, performance. Don't elevate |
|      | to elegance-review until base-quality is satisfied.                             |
|  2   | Read the code as if for the first time. What does it appear to do? How much   |
|      | global context do you need to verify?                                           |
|  3   | Apply Beck's four rules in order:                                              |
|      |   a. Tests pass? (Should already be true.)                                      |
|      |   b. Reveals intent? Can a reader understand the why, not just the what?       |
|      |   c. No duplication? Is the same concept expressed in only one place?          |
|      |   d. Fewest elements? Could it be simpler without violating earlier rules?     |
|  4   | Apply Hickey's distinction: is this simple (un-braided) or just easy           |
|      | (familiar)? Familiar code that braids concepts has hidden complexity.          |
|  5   | Check locality: to understand this function/class, how far do I have to look?  |
|      | Long chains of indirection are warnings.                                        |
|  6   | Check surprise: does the code's behavior match what its surface suggests?     |
|      | Edge cases that surprise readers are smells.                                    |
|  7   | Check naming: does each name reveal intent? Could a reader know what it does  |
|      | from the name alone?                                                            |
|  8   | Discuss trade-offs visibly. Where two rubric dimensions conflict, the         |
|      | discussion is the value, not the resolution.                                    |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
Code Elegance Review Rubric

REVIEWING:        ______________________________________
LANGUAGE / STACK: ______________________________________

PRE-CHECK (base quality):
   [ ] Tests pass
   [ ] No obvious security issues
   [ ] Performance acceptable for context

ELEGANCE DIMENSIONS (1-5 each; with note):

1. REVEALS INTENT
   Can a fresh reader understand WHY, not just WHAT?
   Score: ___   Note: ___________________________

2. NO DUPLICATION (single source of truth)
   Is the same concept expressed in one place only?
   Score: ___   Note: ___________________________

3. FEWEST ELEMENTS
   Could anything be removed without losing intent / duplication / tests?
   Score: ___   Note: ___________________________

4. SIMPLE vs EASY (Hickey)
   Is this simple (un-braided) or just familiar?
   What concepts are braided that could be separated?
   Score: ___   Note: ___________________________

5. LOCALITY
   To understand this code, how far must I look?
   Score: ___   Note: ___________________________

6. SURPRISE MINIMIZATION
   Does behavior match what the surface suggests?
   Edge-case surprises?
   Score: ___   Note: ___________________________

7. NAMING
   Do names reveal intent? Or are they generic / cryptic?
   Score: ___   Note: ___________________________

OVERALL ELEGANCE: ___ / 35

TRADE-OFFS SURFACED (where 2+ dimensions conflict):
   - ____________________________________________________
   - ____________________________________________________

SUGGESTED REFACTOR (if any):
   _______________________________________________________

NOTE: Elegance review is post-correctness. If base quality
fails, fix that first.
```

> **Operational notes:** (1) **Subjective shared-vocabulary required.** The rubric only works in teams that have built shared aesthetic vocabulary. New teams should start by reviewing exemplars together (a clean small open-source codebase) to align taste. (2) **Don't apply to draft code.** Elegance review on first-draft code crushes momentum. Reserve for code being polished. (3) **Cleverness is not elegance.** A one-liner that requires reverse-engineering is *not* elegant by this rubric; it fails "reveals intent." Hickey's distinction matters: elegant code is often longer than clever code. (4) **Single-axis-blindness.** A reviewer who only sees Locality misses the rest. The rubric forces dimension-coverage.

## Related Tools and Frameworks

- **Design Critique Format** — the broader form; this rubric specializes it for software.
- **Connoisseurship Training** — the apprenticeship-of-taste model; elegance review is one practice site.
- **Kantian Aesthetic Judgment Frame** — theoretical underpinning; code-as-aesthetic-object is a non-trivial claim.
- **After Action Review** — pairs as the retrospective form once code has shipped.

## Sources

- Hickey, R. (2011). *Simple Made Easy* (Strange Loop conference talk).
- Beck, K. (1997). *Smalltalk Best Practice Patterns*. Prentice Hall.
- Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- Knuth, D. (1992). *Literate Programming*. Center for the Study of Language and Information.
- Goetz, B. (various Java-language design talks and writings).
- Norvig, P. (2005). *Solving Every Sudoku Puzzle* — exemplar of elegance writing.
