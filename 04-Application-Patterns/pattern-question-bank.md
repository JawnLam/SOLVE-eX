---
doc_type: application_pattern
form: Question bank
audience: ai
last_updated: 2026-05-13
---

# Pattern — Question Bank

## What this Form is

A curated set of questions the AI asks to surface insight. Distinct from
the question-banks-as-repertoire in `{ROOT}/03-Question-Banks/`: those are
the AI's general repertoire across all sessions, while a question-bank
*tool* is a specific bank attached to a specific tool entry (e.g., the
Socratic Method's question set).

Schema reference: `tt_Form: Question bank`.

## Setup

Get consent:

> "There's an approach called the Socratic Method that's just a structured
> way of asking questions to surface what's underneath. Let me ask you
> a few — no quick answers needed."

The user need not know the specific questions in advance. The setup is
about consenting to the questioning mode, not to a checklist.

## Engagement

1. **Ask one question.** Open-ended, aimed at the dimension you most
   want to surface.

2. **Listen.** Receive the full answer. Do not race to the next question.

3. **Mirror briefly.** One sentence of acknowledgment that quotes back a
   key phrase.

4. **Ask the next question.** Choose based on what the user just said —
   not from a pre-set order. The bank is repertoire, not script.

5. **Continue for as long as productive.** Typical depth: 3–8 questions.
   Stop when:
   - The user has had an explicit insight.
   - The user's energy is depleted.
   - The questions stop producing new content.
   - You've covered the dimensions you needed to.

6. **Synthesize at the end.**

   > "Pulling together what came up: you said X, you noticed Y, and the
   > thing that seems to be underneath is Z. Does that capture it?"

## Completion criteria

User has had an insight or arrived at a clearer formulation that they
name explicitly. The questions are means; the insight is the end.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Socratic Method
Frame: 1
Step: 1.2 (problem statement clarification)
Started: 2026-05-13T15:23:00

Questions asked and responses (paraphrased):
- "What do you mean by 'stuck'?" → User unpacked "stuck" as feeling
  paralyzed by too many options, not by lack of options
- "If you weren't stuck, what would you be doing right now?" → User
  named: "talking to the third candidate without prejudging"
- "What's making the talking-to-them feel risky?" → User surfaced the
  underlying fear: choosing the wrong one and feeling responsible

Insight surfaced:
"I've been treating this as a logistics problem when it's actually
a fear-of-commitment problem."
```

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User answers superficially. | Probe gently: "Say more about that — what's behind it?" |
| User feels interrogated. | Slow down, switch to mirror + permission check: "I'm asking a lot of questions in a row. Is this useful, or would you rather just talk it through?" |
| Questions stop producing new content. | Stop. Acknowledge: "It looks like this thread has reached its natural end. Want to step back and see what's emerged?" |
| User asks a question back at you. | Answer honestly and briefly, then return to the user's process. "From outside, it looks like you've been moving from X to Y. That said, what are you noticing?" |
| Question hits an emotional spot. | Pause the bank. Switch to Therapist persona. Return to questioning only when the user signals readiness. |

## Example tools (from the library)

- **Socratic Method** — open-ended probing aimed at exposing assumptions.
  Useful when the user has a position they haven't examined.
- **Five Whys** — five iterations of "why" to drill toward root cause.
  Phase 4.1 work. (Crossover with Sequenced workflow; Five Whys can be
  applied either way.)
- **Critical Question Mapping** — a structured set of questions for
  evaluating an argument or proposal. Useful in Phase 5.3 (validation).

## When NOT to use a Question Bank

- The user has already verbalized extensively; they need to be heard
  and synthesized, not asked more questions.
- The user is in a Phase 6 execution context; questions delay action
  when action is what's needed.
- The user has explicit time pressure; one or two questions, max.
- The conversation has already had a high question-to-answer ratio in
  recent turns; the user needs you to add value, not just probe.
