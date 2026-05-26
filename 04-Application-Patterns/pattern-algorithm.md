---
doc_type: application_pattern
form: Algorithm
audience: ai
last_updated: 2026-05-14
---

# Pattern — Algorithm

## What this Form is

A formal computational procedure that takes specified inputs and
produces a specified output via well-defined steps. Algorithms
differ from heuristics by being deterministic (same inputs → same
outputs) and complete (defined behavior for every input case);
they differ from sequenced workflows by being mathematical or
computational rather than dialogical.

Schema reference: `tt_Form: Algorithm` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Algorithm pattern when the tool's `tt_Form` is `Algorithm`,
and:

- The user's question can be reduced to specified inputs and a
  specified output.
- The decision benefits from computational rigor — the answer
  depends on number relationships the user cannot intuit reliably.
- The inputs are knowable (or at least estimable with calibrated
  guesses).
- The user wants the computation, not just a heuristic for the
  answer.

## Preparation steps

1. **Verify the algorithm applies to the user's situation.**
   Algorithms have explicit input shapes; if the user's situation
   doesn't fit the input shape, the algorithm is the wrong tool.
2. **Confirm input availability.** If the algorithm needs a prior
   probability the user can't estimate, the algorithm cannot run.
   Surface the gap; switch tools or pause to gather inputs.
3. **Set expectations about precision.** Most thinking-tool
   algorithms produce calibrated estimates, not certainties. The
   user should know whether they're computing a precise answer or
   a defensible estimate.

## Application steps

1. **Name the algorithm and what it computes.**

   > "Bayesian Updating gives us a way to revise a probability
   > estimate when new evidence comes in. We'll need three
   > numbers: your prior probability before the evidence, the
   > probability of seeing the evidence if the hypothesis is true,
   > and the probability of seeing it if the hypothesis is false.
   > It'll produce your updated probability."

2. **Gather the inputs.** Walk through each input one at a time.
   Capture the user's reasoning when an input is hard to estimate;
   the reasoning is often more diagnostic than the number.

3. **Run the computation.** Show the work. The user benefits from
   seeing the arithmetic — not because they need to verify it, but
   because the intermediate steps often surface intuitions they
   weren't aware of.

   > "Prior: 0.3. Likelihood of evidence given true: 0.8. Likelihood
   > given false: 0.2. Bayes formula: P(true | evidence) = (0.8 × 0.3)
   > / (0.8 × 0.3 + 0.2 × 0.7) = 0.24 / 0.38 = 0.63."

4. **Surface the result and interpret it.** The number alone is
   not the answer. The interpretation — what the number means in
   the user's situation — is the work.

   > "Your updated probability is 0.63 — meaningfully above your
   > prior of 0.3. The evidence is genuinely shifting your belief,
   > not just confirming it."

5. **Sensitivity check.** Show what happens if one input is nudged.
   This calibrates the user's confidence in the result.

   > "If your prior had been 0.2 instead of 0.3, the posterior
   > would be 0.5 — still above prior, but not as decisive. The
   > result is sensitive to your prior."

6. **Compare to intuition (where applicable).** Some algorithms
   produce results the user's intuition can check; others produce
   results that are precisely beyond intuition. For the former,
   gut-check; for the latter, calibrate trust in the algorithm
   instead.

## Completion criteria

The inputs are gathered, the computation is run, the result is
interpreted in the user's situation, AND (where applicable)
sensitivity is examined or the result is gut-checked. An
algorithm's output without interpretation is just arithmetic.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Bayesian Updating (will the deal close?)
Frame: 0
Step: 5.2 (decision tool) / 5.3 (validate)
Started: 2026-05-14T19:00:00
Completed: 2026-05-14T19:20:00

Inputs:
- Prior P(deal closes): 0.40
  Reasoning: "Pre-meeting, I'd have given it 40/60."
- P(this kind of follow-up email | deal closes): 0.75
  Reasoning: "Engaged buyers usually send something like this."
- P(this kind of follow-up email | deal doesn't close): 0.30
  Reasoning: "Polite-decline emails sometimes have this shape too."

Computation:
P(closes | email) = (0.75 × 0.40) / (0.75 × 0.40 + 0.30 × 0.60)
                  = 0.30 / 0.48
                  = 0.625

Result: Updated probability 0.625; meaningful upward revision.

Sensitivity:
- If P(email | closes) had been 0.6 instead of 0.75: posterior = 0.57.
  Still above prior, but less decisive.

Interpretation: The email is evidence — not certainty. User now
holds 60-65% confidence the deal closes, vs. 40% pre-email.
```

## Common variations

- **Probabilistic algorithms** — Bayesian Updating, Monte Carlo
  Simulation. Produce probability distributions.
- **Optimization algorithms** — gradient methods, Blueprint
  Optimization Framework. Produce optimal-parameter answers given
  a defined objective.
- **Game-theoretic algorithms** — Bayesian Games, mechanism design.
  Produce equilibrium strategies given player payoffs.
- **Simulation algorithms** — Monte Carlo, agent-based models.
  Produce distributions over outcomes via repeated sampling.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| Inputs are not actually estimable | The algorithm cannot run on hopes and vibes. Either gather better inputs or switch to a tool that tolerates qualitative inputs (Heuristic, Mental Model). |
| Computation produces precise-looking output from imprecise inputs | False precision is a real failure mode. State the precision honestly: "The computation says 0.625, but your inputs are calibrated estimates — read this as 'around 60-65%,' not 0.625." |
| User treats algorithmic output as more certain than the algorithm warrants | Algorithms compound input uncertainty; the output's precision is bounded by the inputs' precision. Sensitivity check (step 5) is the corrective. |
| Algorithm is run but result is not interpreted | The number alone is not the work. Loop back to interpretation; do not move on with an uninterpreted output. |
| User's intuition strongly contradicts the algorithm's result | The intuition is data. Either the inputs are wrong, the algorithm's assumptions don't fit, or the intuition is reacting to a constraint not in the model. Investigate. |
| Algorithm dragged out beyond its useful precision | Some algorithms (Monte Carlo with many trials) produce diminishing returns. Stop when the precision exceeds the user's input precision; further iterations don't sharpen the answer. |

## Example tools (from the library)

- **Bayesian Updating** — revises a probability estimate when new
  evidence arrives. Use when the user has a prior belief and is
  encountering data that should move it.
- **Monte Carlo Simulation** — runs many randomized trials to
  produce a distribution over outcomes. Use when the user is
  reasoning about ranges of futures (financial planning, risk
  analysis, project timelines).
- **Bayesian Persuasion** — game-theoretic algorithm for the
  sender of a signal in a strategic interaction. Use in negotiation
  or communication-strategy frames where the user is asking "what
  should I disclose / not disclose."

## When NOT to use an Algorithm

- The user's question is qualitative and doesn't reduce to inputs
  and outputs. Algorithms force a precision the question doesn't
  have.
- The user wants speed over rigor. Heuristics are the right
  pattern; algorithms are deliberate work.
- The inputs are unknowable in principle. An algorithm with made-up
  inputs is confident wrongness; switch to a different shape.
- The user is in emotional regulation work. Algorithmic precision
  reads as cold; switch to Therapist persona and revisit when the
  analytic frame re-opens.
- The user has explicitly rejected mathematical framing for the
  question ("I don't want to put numbers on this"). Honor the
  rejection; the question is not analytic for this user.
