---
doc_type: application_pattern
form: Scoring rubric
audience: ai
last_updated: 2026-05-14
---

# Pattern — Scoring Rubric

## What this Form is

A weighted-scoring instrument that compares a set of options
against a set of criteria, produces a ranked output, and — critically
— ends with a gut-check against the user's intuition. Scoring
rubrics differ from matrix tools by producing a quantitative
ordering; they differ from decision trees by treating options as
peers rather than as branches in a tree.

Schema reference: `tt_Form: Scoring rubric` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Scoring Rubric pattern when the tool's `tt_Form` is
`Scoring rubric`, and:

- The user has 3+ options and the comparison is non-trivial.
- The user can name multiple criteria but is not sure how to weigh
  them against each other.
- The user has a gut sense of the right answer and wants to either
  confirm it or surface why the gut and the analysis disagree.
- The decision has enough at stake to warrant the explicit work;
  scoring rubrics are heavyweight for low-stakes calls.

## Preparation steps

1. **Establish the options.** Make sure the option set is exhaustive
   in a meaningful sense. Missing a viable option upstream poisons
   the rubric.
2. **Establish the criteria.** Pull criteria from the user's named
   values, not from a generic list. If the user has not yet named
   what matters, return to Phase 2 (Establish requirements) before
   scoring.
3. **Establish weights.** Weights are the user's, not the AI's. The
   AI surfaces the trade — "how much more does autonomy matter than
   compensation?" — but the user assigns.

## Application steps

1. **Name the rubric and explain the structure — one sentence.**

   > "Let's score your three options against the criteria you
   > named. We'll weight the criteria, score each option, and look
   > at the totals — then check the result against your gut."

2. **List options on one axis, criteria on the other.** A table
   with options as rows and criteria as columns (or vice versa).
   Show the structure before any scoring happens.

3. **Set the weights.** For each criterion, ask the user to
   assign a weight (1–5 or 1–10; pick one and stick with it).
   Weights need not sum to a target; they are relative.

4. **Score each option on each criterion.** Walk the table cell by
   cell. Use a 1–5 or 1–10 scale (match the weights scale). Capture
   the user's reasoning when scoring is hard ("why does Option A
   get a 3 here, not a 5?") — that reasoning is often more
   diagnostic than the score.

5. **Compute weighted totals.** For each option: sum across
   criteria of (score × weight). The output is a ranked list.

6. **Compare to gut.** This is the load-bearing step.

   > "The scoring says Option B is the winner by a meaningful
   > margin. Before we treat that as the answer — what does your
   > gut say? Does this match it, or does it feel off?"

7. **Handle the mismatch (if any).** If the gut and the rubric
   agree: the rubric is confirming the gut, and the work is
   sharpening the user's articulation of why. If the gut and the
   rubric disagree: the criteria, the weights, or the option set
   are wrong. Walk back and surface which.

## Completion criteria

The rubric is filled AND the user has compared the rubric result
against their gut AND any discrepancy has been examined. A rubric
without the gut-check is half-applied; a gut-check without examining
the discrepancy is half-finished.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Weighted Decision Matrix (job offer evaluation)
Frame: 0
Step: 5.1 (criteria) / 5.2 (decision tool)
Started: 2026-05-14T16:00:00
Completed: 2026-05-14T16:35:00

Criteria + weights:
| Criterion       | Weight (1–5) |
|-----------------|--------------|
| Compensation    | 3            |
| Autonomy        | 5            |
| Manager quality | 4            |
| Geographic fit  | 2            |

Filled rubric (1–5 scale):
| Option         | Comp×3 | Auton×5 | Mgr×4 | Geo×2 | Total |
|----------------|--------|---------|-------|-------|-------|
| Offer A        | 4 (12) | 4 (20)  | 3 (12)| 5 (10)| 54    |
| Offer B        | 3 (9)  | 5 (25)  | 4 (16)| 3 (6) | 56    |
| Stay (current) | 5 (15) | 2 (10)  | 5 (20)| 5 (10)| 55    |

Result: Offer B narrowly leads (56 / 55 / 54 — within noise).

Gut check:
- User's gut: "Offer B feels right."
- Rubric: Offer B narrowly wins.
- Match. The rubric confirms the gut; the work was articulating why
  (autonomy weighs heavily even though comp is lower).
```

## Common variations

- **AHP (Analytic Hierarchy Process)** — pairwise comparison of
  criteria to derive weights, then standard scoring. Heavier
  ceremony; use when weights are genuinely contested.
- **Kepner-Tregoe Decision Analysis** — separates "must-haves"
  (binary screens) from "wants" (weighted scoring). Use when the
  option set has hard constraints.
- **Brier Scoring** — for evaluating probabilistic forecasts rather
  than option choices. Different application; same shape.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User's gut and the rubric disagree | This is the rubric working. Surface which is wrong: criteria missing, weights miscalibrated, option set incomplete, or gut overcorrecting. Often the gut knows a criterion the user hasn't articulated. |
| Weights all the same | Either the criteria are not differentiated, or the user is hedging. Surface: "If you had to make one criterion matter more than the others, which?" |
| Scores all the same for one option | Either the option is uninformative, or the scoring scale is too coarse. Sometimes both. |
| User wants to add a tie-breaking criterion mid-scoring | Pause and ask why. Often the right move is to add the criterion, redo the affected rows, and continue. Sometimes the impulse signals the criteria set was wrong. |
| Rubric "confirms" what the user wants to do | Watch for confirmation theater — weights tuned post-hoc to produce the desired ranking. Surface with: "If you'd weighted [criterion] one point higher, the result flips — does that change your read?" |
| User wants the rubric to make the decision | The rubric supports the decision; it does not replace the user. Cross-persona principle: the AI never substitutes its judgment for the user's. The numbers are inputs, not verdicts. |

## Example tools (from the library)

- **Weighted Decision Matrix** — the canonical option×criterion
  scoring tool. Works well for any 3-to-7 option choice with
  multiple criteria.
- **AHP (Analytic Hierarchy Process)** — pairwise criterion
  comparison derives weights; use when the user genuinely cannot
  rank criteria directly.
- **Kepner-Tregoe** — must-have/want separation; use when there
  are hard constraints (e.g., "the role must be remote") that
  should screen options before scoring.

## When NOT to use a Scoring Rubric

- The decision has 1–2 options. Use a different tool; rubrics need
  contrast to work.
- The user is dysregulating around the decision. Scoring is
  cognitive work; if emotion is dominant, switch to Therapist
  persona and revisit.
- The criteria are not stable yet (the user is still figuring out
  what matters). Score work is downstream of values work.
- The user's gut is loud and the user is signaling they already
  know. The rubric would only delay the decision; back to
  Consultant persona and operationalize.
- The decision is reversible and cheap. Rubric overhead exceeds
  the decision's stakes.
