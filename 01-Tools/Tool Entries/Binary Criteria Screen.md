---
Item_ID: tt-binary-criteria-screen
Item_Prototype: Thinking_Tool
Title: Binary Criteria Screen
tt_Source: 'Practitioner method; structurally a simplified variant of Weighted Decision Matrix (Pugh Concept Selection / Multi-Criteria Decision Analysis lineage, mid-20th-century operations research). The binary-screen variant is distinct from weighted multi-axis scoring in that each criterion is evaluated as pass/fail (yes/no) rather than scored on a numeric scale, and the decision-output is "which alternatives survive all named criteria" rather than "which alternative has highest weighted score." Sprint 15 Mara dispositive test surfaced the need: a binary-screen variant deserves its own canonical entry because the structural difference from weighted matrix is operationally significant.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision-theoretic reasoning
tt_Operation: Cut alternatives with explicit criteria
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Matrix
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
tt_Lineage:
- Industrial / business
- Western analytic / academic
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Strategy / competition
- Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Pre-Mortem
tt_Often_Follows:
- Mom Test
- Customer Discovery
- Jobs-to-Be-Done
tt_Pairs_Well_With:
- Weighted Decision Matrix
- Pre-Mortem
- Inversion
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-19 — initial classification (Sprint 16 Card 10, schema v1.15.0); added to corpus to close the binary-vs-weighted decision-matrix gap surfaced by Sprint 15 Mara dispositive test (Mara turn 7 ran a binary-criteria screen against three lanes against three day-30 criteria; Weighted Decision Matrix was the nearest library analog but presumes weighted multi-axis scoring — the binary variant is structurally distinct and warranted its own canonical entry per Mara's quality_check_corrections close-turn note)
Tags:
- '#thinking-tool'
See_Also:
- Weighted Decision Matrix
Date_Added: 2026-05-19
Date_Modified: 2026-05-19
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: Score each named alternative pass/fail against each named criterion. The output is the set of alternatives that pass ALL criteria, NOT the highest-scoring alternative. Use when (a) the criteria are sufficiently distinct that they should not trade off against each other (a violation of any one is disqualifying) and (b) the alternatives are sufficiently small in number that exhaustive screening is feasible. Distinct from Weighted Decision Matrix in that there is no numeric scoring and no weighting — each criterion is a gate, not a dimension on which alternatives are ranked.
Needs_Processing: false
AI_Instructions: ''
---

# Binary Criteria Screen

**One-line summary:** A simplified decision-screen method — evaluate each named alternative as pass/fail against each named criterion, output the alternatives that pass ALL criteria, NOT the highest-scoring one; structurally distinct from Weighted Decision Matrix in that each criterion is a gate rather than a weighted dimension.

**When to reach for it:** Early-stage option-narrowing when the criteria are categorical rather than continuous (regulatory requirement met / not met; ethical constraint satisfied / not; deadline workable / not); finite-option discovery screening (choose among ≤5 alternatives based on disqualifying criteria); contexts where multi-axis weighted scoring would obscure the structure of the decision; and any time you find yourself wanting a Weighted Decision Matrix but the natural answer is "which alternatives are still in the running" rather than "which scored highest."

---

## Purpose Of This Thinking Tool

**Binary Criteria Screen** is a decision-narrowing method that operates by gating, not scoring. The procedure:

1. **Name the alternatives explicitly.** A finite, enumerable set — typically 2–5. The set must be exhaustive of the decision space (if "do nothing" is an option, list it; if "wait" is an option, list it).
2. **Name the criteria explicitly.** Each criterion is a binary pass/fail test. Criteria should be (a) disqualifying when violated, (b) operationally checkable (no ambiguity about whether an alternative meets it), (c) independent (a criterion that's a soft version of another is a weighting in disguise — collapse them).
3. **Score the matrix.** For each alternative × criterion cell, record pass / fail. Do not record degrees; binary only.
4. **Read the surviving set.** The decision-output is the set of alternatives that pass ALL criteria. If multiple pass, the screen has narrowed the decision but not resolved it — proceed to a separate method (Pre-Mortem on the survivors; Weighted Decision Matrix among the survivors; user-judgment call).
5. **Treat the screen's output as evidence, not a verdict.** The screen surfaces which alternatives are even viable; the final choice still requires judgment about which survivor is best.

The non-obvious operational insight is that **the binary screen prevents the weighting trap.** Weighted Decision Matrix introduces a weighting step ("how important is criterion A vs criterion B?") that often does the actual decision-work — the weights determine the winner, not the scores. Binary screening forces the user to articulate which criteria are genuinely disqualifying and which are merely preferred. The disqualifying ones go in the screen; the preferred ones don't.

A second insight: **the screen is most useful when one or more alternatives are "obviously" the right choice but the user wants to verify.** Running the screen often surfaces that the obvious choice fails one of the named criteria — the disqualifying criterion was tacit and the screen made it explicit. Sprint 15 Mara turn 7: three lanes (parent conversations / product build / SEO sprint) screened against three day-30 criteria (produces criterion-relevant evidence / scales to 6-month runway / avoids former-students ethical constraint). Only parent conversations passed all three; the screen made this visible.

A third insight: **the screen is bounded by the number of alternatives and criteria.** With ≥6 alternatives or ≥6 criteria, the matrix becomes hard to read; consider clustering criteria into 3–4 themes or pre-narrowing alternatives. The method is at its best with 3–5 alternatives × 3–4 criteria.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The hidden-weighting trap.** Weighted Decision Matrix often lets the user smuggle the answer in via the weights. Binary screening forces explicitness: a criterion is either disqualifying or it isn't.
2. **The "I'll just trust my gut" anti-method.** When the user has implicit criteria, they apply them inconsistently and post-hoc-rationalize. The screen makes implicit criteria explicit; subsequent decisions are auditable.
3. **The multi-axis scoring overhead.** Weighted scoring is appropriate when criteria genuinely trade off against each other on a continuum. When criteria are categorical (regulatory, ethical, hard-constraint), the scoring overhead obscures the structure of the decision. Binary screening matches the underlying decision shape.

For founders, decision-makers, evaluators, and anyone narrowing a finite option-set against disqualifying criteria, the Binary Criteria Screen is the right method when Weighted Decision Matrix would over-machine the problem.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Enumerate the alternatives explicitly. Include "do nothing" / "wait" if they    |
|      | are options. Aim for 2-5 alternatives.                                          |
|    2 | Enumerate the criteria. Each criterion must be (a) disqualifying when violated, |
|      | (b) operationally checkable, (c) independent of the others. Aim for 3-4.        |
|    3 | If a criterion feels like "more is better" rather than "pass or fail" —         |
|      | reconsider. That criterion belongs in Weighted Decision Matrix, not here.       |
|    4 | Score the matrix. For each cell, record only pass or fail. No degrees.         |
|    5 | Read the surviving set: alternatives that pass ALL criteria.                   |
|    6 | If the survivor set has one alternative: that's the decision (subject to       |
|      | sanity check via Pre-Mortem). If it has multiple: the screen has narrowed but   |
|      | not resolved — proceed to a separate method among the survivors.                |
|    7 | If the survivor set is empty: either the criteria are over-specified (some are  |
|      | not actually disqualifying) or the alternative space is under-specified (a new  |
|      | alternative needs to be added). Either way, iterate.                            |
|    8 | Document the screen as part of the Case File / decision record. The matrix IS  |
|      | the audit trail of which criteria were applied and how.                         |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE BINARY CRITERIA SCREEN

   ALTERNATIVES (rows): finite, 2-5, exhaustive of decision space
   CRITERIA (columns): 3-4, disqualifying-when-violated, independent

   For each cell: PASS or FAIL — no degrees, no weights.

                | Crit A | Crit B | Crit C |  Survives?
   -------------|--------|--------|--------|------------
   Alt 1        | PASS   | PASS   | FAIL   |     no
   Alt 2        | PASS   | PASS   | PASS   |    yes
   Alt 3        | FAIL   | PASS   | PASS   |     no
   Alt 4        | PASS   | FAIL   | PASS   |     no

   READ THE SURVIVING SET.
   If 1 survivor: decision (sanity-check with Pre-Mortem).
   If ≥2 survivors: narrowed; choose another method among them.
   If 0 survivors: iterate (criteria too tight, or add alternatives).
```

## Sources

- Pugh, Stuart. *Total Design: Integrated Methods for Successful Product Engineering* (1991) — Pugh Concept Selection method, the design-engineering lineage of structured criterion-based screening.
- Saaty, Thomas L. *The Analytic Hierarchy Process* (1980) — multi-criteria decision analysis frame from which binary screening is a deliberate simplification.
- Practitioner methodology in early-stage discovery and product strategy work; no single canonical text for the binary-screen variant specifically, which is why Sprint 16 Card 10 adds it as a corpus entry.
