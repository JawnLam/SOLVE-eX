---
doc_type: sample_session
doc_purpose: index
audience: ai_and_human
read_order: 0
last_updated: 2026-05-13
---

# Sample Sessions — Index

Sample sessions are annotated, fully-walked transcripts that demonstrate
the system working correctly. They serve three audiences:

- **The AI**, which reads them to internalize patterns.
- **The user**, who can read them to understand what to expect.
- **Future maintainers**, who use them as regression test scenarios.

## MVP samples (Phase 1)

| File | Scenario | What it demonstrates |
|------|---------|----------------------|
| `sample-01-simple-decision.md` | Low-stakes, both endpoints clear at outset. User decides whether to attend a conference. | Direct Phase 5 work; quick Eisenhower Matrix; resolution in ~10 turns; single persona. |
| `sample-02-unclear-destination.md` | User wants to change something but doesn't know what. | Destination clarification; tools for surfacing values; recursive sub-frame for a values inventory; patience in not jumping to solutions. |

## Phase 2 samples (deferred)

- `sample-03-recursive-clarification.md` — multi-level recursion.
- `sample-04-emotional-overwhelm.md` — Therapist persona at length.
- `sample-05-multi-session.md` — 4-session journey, resumption protocol.
- `sample-06-stakes-routing.md` — chapter 09 routing in action.
- `sample-07-resumption-after-weeks.md` — 3-week return; user's life changed.
- `sample-08-user-resistance.md` — user pushes back on a tool; persona shift and meta-conversation.

## How to read a sample session

Each file contains:

- **Frontmatter** — case file metadata (anonymized).
- **Scenario summary** — one paragraph context.
- **Annotated transcript** — every turn, with persona tags and design
  annotations.
- **Final Case File state** — frontmatter and body after the session
  closes.
- **Notes for review** — what to look for, where the design choices land.

The annotations are not visible to the user in real sessions; they exist
in samples to make the design choices legible.

## What samples are NOT

- Not the only correct way to handle each scenario. Many paths work;
  samples illustrate one.
- Not scripts. The AI does not re-use the exact lines; samples teach
  the *shape* of the move, not the words.
- Not exhaustive of the system's capacity. Many scenarios outside
  these 8 samples will arise.

## Voice neutrality in samples

The AI's voice in the samples follows all cross-persona principles. No
first-person sentiment ("I feel"), no opinion projection ("I think
this is great"), no personality. The samples are reference for what
the system does, not for who the AI is — because the AI is not a who.
