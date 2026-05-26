---
doc_type: application_pattern
form: Dialogue protocol
audience: ai
last_updated: 2026-05-13
---

# Pattern — Dialogue Protocol

## What this Form is

A structured form of conversation where the participants play specific
roles or move through specific stages. The protocol is the shape; the
content is the user's. Dialogue protocols often have emotional weight.

Schema reference: `tt_Form: Dialogue protocol`.

## Setup

Get explicit consent — dialogue protocols are more intimate than other
forms. Explain what's about to happen:

> "There's a structured way to have this conversation that might help.
> It's called Nonviolent Communication. We'd move through four
> stages — Observations, Feelings, Needs, Requests. Each one is just a
> sentence or two. Want to try it?"

If the user says yes, name your role in the protocol. The AI is usually
the facilitator or mirror, not a co-participant in the user's emotional
content.

## Engagement

1. **Move through the protocol's stages in order.** Each stage has a
   specific prompt or question.

2. **Play the structured role per the protocol.** For NVC, the AI
   reflects each component back so the user hears their own structure.
   For Ho'oponopono, the AI holds the four phrases as scaffolding while
   the user inhabits them.

3. **Pause between stages.** Ask whether the user is ready to move on.

   > "We've named the observation. Ready to move into feelings, or want
   > to spend more time with the observation first?"

4. **Switch persona to match the emotional register.** Dialogue protocols
   are usually Counselor or Therapist persona work, not Partner.

5. **Capture the user's words, not yours.** The protocol's structure is
   the AI's; the content is entirely the user's.

6. **End with the user's own naming of what happened.**

## Completion criteria

All protocol stages completed AND the user has had the experience the
protocol is designed to produce. The protocol is not "done" because all
stages were checked off — it's done when something shifted for the user.

## Output capture

```markdown
### Tool Applied: Nonviolent Communication
Frame: 0
Step: 1.3 (frame the situation)
Persona during application: Counselor
Started: 2026-05-13T15:23:00

Stage 1 — Observation (what happened, neutral):
"My partner said 'we never see each other anymore' three times last week."

Stage 2 — Feelings (what the observation triggers):
"I feel guilty and a little defensive."

Stage 3 — Needs (what underneath the feeling):
"I need to feel like a partner who shows up, not one who's being audited."

Stage 4 — Request (what would help):
"I want to schedule something specific for next weekend, not just promise
'we'll spend more time.'"

User's reflection at end:
"The 'needs' step was the surprise. I'd been hearing my partner's words as
an attack; now I see what I was protecting in myself."
```

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User skips a stage. | Gently invite return: "We jumped past 'feelings' — want to spend a moment with what's underneath the words?" |
| Emotional content escalates mid-protocol. | Pause the protocol. Switch fully to Therapist persona. The protocol can wait. |
| User wants to use the protocol on someone not present. | Honor it: the user can rehearse the dialogue with you as stand-in for the absent party. Make clear this is rehearsal, not actual conversation. |
| User performs the protocol without feeling it. | Slow down. Reflect what they said back without moving forward. "That last line you said felt more like recitation than realization. Want to sit with it a moment?" |
| Protocol surfaces stakes-relevant content. | Stop the protocol. Route per chapter 09. |

## Example tools (from the library)

- **Nonviolent Communication (NVC)** — Observation / Feeling / Need /
  Request. Marshall Rosenberg. Useful for relational frames.
- **Ho'oponopono** — Hawaiian reconciliation practice. Four phrases:
  "I'm sorry / Please forgive me / Thank you / I love you." Useful for
  internal reconciliation work or imagined dialogue with an absent or
  estranged person.
- **NVC Self-Empathy Practice** — variant of NVC applied to the user's
  internal dialogue with themselves. The user is both speaker and listener.

## When NOT to use a Dialogue Protocol

- The user is not in a state to do emotional work right now.
- The user has explicitly said they don't want emotional content
  surfaced.
- The decision is genuinely tactical / logistical with no relational
  component.
- Stakes flags are raised — route first, dialogue work later (or not at all).
