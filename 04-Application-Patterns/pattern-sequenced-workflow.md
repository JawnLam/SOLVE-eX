---
doc_type: application_pattern
form: Sequenced workflow
audience: ai
last_updated: 2026-05-13
---

# Pattern — Sequenced Workflow

## What this Form is

A multi-step procedure where each step depends on the previous one. The
user (with the AI's guidance) advances through the steps in order. Each
step produces output that feeds the next.

Schema reference: `tt_Form: Sequenced workflow`.

## Setup

Get consent and outline:

> "There's a step-by-step process called the Pre-Mortem that might help
> here. It has four stages — imagining failure, identifying causes,
> ranking them by likelihood, and designing safeguards. Want to walk
> through it?"

If the user says yes, briefly outline all the steps before starting. The
overview prevents the user from feeling jerked from step to step.

## Engagement

1. **Run step 1.** Ask whatever the step's first prompt is. Pause for
   the user's answer.

   > "Imagine it's a year from now and this plan failed badly. Don't
   > rationalize — just say it. What happened?"

2. **Capture the output.** Reflect what the user said in their own words.
   Write to Case File.

3. **Pause for clarity.** Before moving to step 2, confirm step 1's
   output feels complete.

   > "Got that. Anything you want to add before we move to the next
   > step?"

4. **Move to step 2.** Repeat the cycle.

5. **Track step number visibly when helpful.** For longer workflows
   (5+ steps), occasionally mention progress: "We're three of four steps
   through."

6. **At the end, synthesize.** Pull together what each step produced.

   > "So putting it together: you imagined the plan failed because of
   > X; the most likely causes were A and B; and the safeguards you'd
   > add are C and D. Does that capture it?"

## Completion criteria

All steps run AND output of each step recorded AND a synthesis or
takeaway has been named by the user (not just the AI).

## Output capture

Write to the Case File for each step. Example:

```markdown
### Tool Applied: Pre-Mortem
Frame: 0
Step: 5.3 (validate decision)
Started: 2026-05-13T15:23:00

Stage 1 — Imagined failure:
"In a year, the offer would have been the wrong call because my partner's
work situation changed and we had to relocate."

Stage 2 — Causes:
- Partner's job stability was assumed but not verified
- I underweighted the geographic flexibility criterion

Stage 3 — Likelihood ranking:
- Partner's job change: medium-high
- Geographic flexibility I'm underweighting: high

Stage 4 — Safeguards:
- Have an explicit conversation with partner about job change scenarios
- Add geographic flexibility back into the decision matrix with higher weight

Completed: 2026-05-13T15:42:00
```

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User stalls at a step (e.g., can't imagine failure scenarios). | Offer a prompt: "Maybe start with the smallest possible failure — what's a way this could disappoint even slightly?" |
| User wants to skip a step. | Allow it but log the skip: "Want to come back to step 3 later, or skip it entirely? I'll note that we did or didn't." |
| User races through steps without engaging. | Slow down explicitly: "I want to make sure we don't rush step 2. Can you spend a moment with it — what's actually true here, not the polished version?" |
| Output of step N invalidates step N-1. | This is a feature. Loop back: "What you just said about the cause is making me think the failure you described earlier might be different. Want to revise it?" |
| Workflow is too long for one session. | Pause at a clean step boundary. Update Case File to show where you stopped. Resume next session. |

## Example tools (from the library)

- **Pre-Mortem** — imagine failure / identify causes / rank / design
  safeguards. Excellent for Phase 5.3 validation.
- **Five Whys** — ask "why" five times to drill from symptom to root cause.
  Phase 4.1 work; simple but disciplined.
- **Naikan** — three-question retrospective (what did I receive / what
  did I give / what trouble did I cause). Phase 6.4 or as a Practice/Ritual
  variant. Note Naikan sits on the boundary between Sequenced workflow
  and Practice/ritual; use this pattern for short-form Naikan and the
  practice-ritual pattern (Phase 2) for the multi-day version.

## When NOT to use a Sequenced Workflow

- The user is in high emotional activation. Switch to Therapist persona;
  the workflow can wait.
- The user has demonstrated resistance to step-by-step structures.
  Switch to a Mental Model pattern or a Question Bank pattern.
- The user has already done most of the steps independently in their
  own thinking. Don't make them re-walk; pick up where they left off.
