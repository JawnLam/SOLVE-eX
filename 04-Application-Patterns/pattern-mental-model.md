---
doc_type: application_pattern
form: Mental model
audience: ai
last_updated: 2026-05-13
---

# Pattern — Mental Model

## What this Form is

A conceptual lens — a way of looking at a situation that reveals something
that wasn't visible from the user's current framing. Mental models do not
have steps to walk or cells to fill. They are *worn*. The user looks at
their situation through the model and notes what they see.

Schema reference: `tt_Form: Mental model`.

## Setup

Get consent:

> "There's a way of looking at this that might be useful. It's called the
> Iceberg Model. Want to hear it?"

Brief, low-pressure. Mental models are quick to introduce; commitment
cost is minimal.

## Engagement

1. **Explain the model in user-relevant terms.** Two or three sentences.
   Use the user's domain language; avoid jargon.

   > "The Iceberg Model says: most situations have what's visible at
   > the top (events), and beneath that, patterns of behavior over
   > time, beneath that the structures that produce those patterns, and
   > beneath that the mental models that hold the structures in place.
   > Most reactive work happens at the event layer; lasting change
   > usually requires going below."

2. **Apply to the user's specific case.** Walk through the model's
   layers using the user's situation.

   > "So if we look at your current case: the event is the job offer
   > that landed last week. What's the pattern underneath that — has
   > something been building over time?"

3. **Ask what they see when they look through the model.** This is the
   work. The model is the lens; the user does the looking.

4. **Note what's revealed.** Mirror back what the model surfaced that
   wasn't surfaced before.

   > "Walking through the layers, you found that the 'pattern over time'
   > you named is actually the same as the 'pattern over time' from your
   > last career transition. That's worth noting."

5. **Confirm the user has absorbed the model.** Mental models are
   reusable. Check that the user can carry the model out of the session:

   > "Want a one-sentence version you can take with you?"

## Completion criteria

User has:
1. Understood the model (can re-state it in their own words).
2. Applied it to their case (looked at their situation through it).
3. Named what they see (the model produced an observation).

## Output capture

```markdown
### Tool Applied: Iceberg Model
Frame: 0
Step: 1.3 (frame the situation)
Started: 2026-05-13T15:23:00

Model explained:
"Events / Patterns over time / Structures / Mental models."

Applied to user's situation:
- Event: job offer arrived last week
- Pattern over time: every 3-4 years user feels like they should be
  doing something different
- Structure: user has been in roles defined by other people's
  expectations
- Mental model: "achievement = approval from authority"

What the user noticed:
"The pattern is the data. I've made this exact decision three times
already with the same kind of agitation."

User's takeaway:
"The job offer is the surface event. The real question is whether I
want another approval-from-authority job, or something else entirely."
```

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User repeats the model but doesn't apply it. | Prompt application: "What does your situation look like through that lens specifically?" |
| Model doesn't fit the situation. | Acknowledge: "This one's not landing — let's try a different angle." Don't force a fit. |
| User uses the model defensively (to dismiss something). | Pause: "I notice the model is being used to push something aside. Want to look at what's getting pushed?" |
| User over-applies the model to all their problems. | Affirm the usefulness, then redirect: "It's a useful lens, but no single lens explains everything. This particular question might benefit from a different angle." |
| Mental model is too abstract for the user's current state. | Switch to a more concrete tool — a Matrix or Sequenced workflow — that lets them work the question rather than just think about it. |

## Example tools (from the library)

- **Iceberg Model** — Events / Patterns / Structures / Mental models.
  Systems thinking lineage. Useful for surfacing the structural causes
  of recurring problems.
- **Inversion** — invert the problem to see it from the opposite
  direction. "What would make this worse?" instead of "what would make
  this better?"
- **Opportunity Cost Reasoning** — every choice forgoes alternatives;
  surface what's being forgone. Useful in Phase 5 evaluation when the
  user is anchored on a single option.
- **Goodhart-Aware Metric Selection** — "When a measure becomes a
  target, it ceases to be a good measure." Useful when the user has
  defaulted to a measurable but distorting criterion.

## When NOT to use a Mental Model

- The user needs to do something, not think about something.
- The user has cognitive load already maxed out; introducing a new
  conceptual frame will overwhelm.
- The model is novel to the user AND complex; teach it in a different
  session, apply it next time.
- The user is in high emotional activation. Models read as cold when
  feelings need room.
