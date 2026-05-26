---
doc_type: process_framework
doc_purpose: clarity_model
audience: ai_and_human
read_order: 3
last_updated: 2026-05-13
---

# Endpoint Clarity States

Every frame has two endpoints: Origin ("where you are") and Destination
("where you want to be"). Each endpoint exists in one of four clarity
states. The state of each endpoint is reassessed every conversational
turn (see `{ROOT}/00-Instructions/03-the-diagnostic-loop.md`).

## The four states

| State | Meaning | Diagnostic signal |
|-------|---------|-------------------|
| **Unclear** | The user cannot articulate this endpoint at all, or what they articulate is confused or contradictory. | "I don't even know what's going on" / "I keep flipping" / mutually-exclusive statements within 2–3 turns |
| **Partially-clear** | Fragments — words, feelings, vague shapes — but no coherent statement. | "It's something like…" / "Sort of…" / "I'd say…" without commitment |
| **Clear-but-unstable** | A coherent statement that shifts when probed. | The user states the endpoint plainly; under a different question it comes out different |
| **Locked** | A coherent statement that survives stress-testing. The user owns it. | The user re-states the same endpoint in similar terms when asked from different angles; energy of conviction is present |

Clarity is **continuously assessed**. It can degrade. A Locked endpoint
can become Clear-but-unstable when new information arrives. That is not
a failure; that is the model working.

## The clarity matrix

Origin and Destination clarity combine into 16 cells. Specific cells map
to specific recommended next-moves. The diagnostic loop reads from this
matrix in step 9 (response strategy).

| Origin → / Destination ↓ | Unclear | Partially-clear | Clear-but-unstable | Locked |
|--------------------------|---------|-----------------|--------------------|--------|
| **Unclear** | Highest-priority work: clarify ONE endpoint first. Default to Origin (gives the user grounding) unless the user is energized about Destination. | Continue Origin work; touch Destination only when Origin firms up. | Work Origin urgently; Destination is at risk of drift without Origin. | Work Origin urgently; the Destination Locked + Origin Unknown pattern is a paradox — probably misdiagnosed. |
| **Partially-clear** | Work Destination; revisit Origin after. | Both partial — work the one the user has more energy for. | Stabilize Destination first; Origin work parallel. | Continue Origin work; Destination's clarity supports it. |
| **Clear-but-unstable** | Lock Destination first via stress-testing; then revisit Origin. | Stabilize both via stress-testing. | Stress-test both endpoints; iterate. | Stabilize Destination; Origin is ready to support path work. |
| **Locked** | Work Origin — currently impossible to proceed. | Stabilize Destination; Origin support is good. | Stabilize Destination; Origin ready. | **Both Locked. Begin Phase 3 (Learn) on the path between them.** |

## Origin-first default

When both endpoints are Unclear, the system defaults to Origin work first.

Rationale: Origin grounds the user. Destination work without Origin
clarity tends to surface fantasy goals ("I want to be happy") rather
than calibrated goals ("given that I'm exhausted from a five-year
overwork stretch, what would a re-set look like?"). Origin work calibrates
Destination work.

Exception: if the user is energized about Destination ("I know what I
want, I just don't know how to get there"), follow the energy. Origin will
surface in the path-work that follows.

## Stress-testing for "Locked"

To move an endpoint from Clear-but-unstable to Locked, stress-test:

- Restate the endpoint from a different angle. Ask if the restatement
  still feels right.
- Pose an obvious counter-argument. See if the user holds the position.
- Wait silently for the user to revise or affirm. (Silence is information.)
- Project forward 6 months. Ask if the endpoint still makes sense in
  that future light.
- Project to an external party. ("If you told a friend the goal in those
  words, would you believe what you were saying?")

If the endpoint survives 2–3 stress-test moves, mark it Locked. If it
shifts under any of them, downgrade to Clear-but-unstable and try again.

## Degradation handling

If a Locked endpoint downgrades mid-session because of new information,
do not treat this as a setback. Mirror it:

> "Sounds like that goal you locked in earlier is feeling less solid now
> that you've heard the new information. Want to take another pass at it
> before we keep going?"

The Case File frontmatter `*_clarity` fields are updated; the body's
Step 2.2 (Goal Statement) section is updated with a new version under
the prior; the change is logged as a `#### Turn N` event.

## Stagnant Unclear

If an endpoint stays Unclear for 6+ turns in the same frame:

- Consider pushing a sub-frame whose Destination is "make this endpoint
  clear" (see `05-push-pop-rules.md` §5.2).
- Consider switching tools — a different Application Pattern may break
  the stagnation.
- Consider asking the user a meta-question: "Is there something making
  this hard to put into words? Or are we asking the wrong question?"
- Consider the possibility that the endpoint is genuinely Unclear because
  the user does not yet have the information to clarify it — i.e., this
  is a Phase 3 work disguised as a Phase 1 or 2 work.

Stagnation is data. Do not power through it; diagnose it.

## Mutual interaction

Origin and Destination interact:

- A locked Origin makes Destination work easier (the user has a stable
  reference point).
- A locked Destination can sometimes destabilize Origin ("Now that I see
  what I want, where I am suddenly feels different").
- A locked Destination + locked Origin enables Phase 3+ work. Until then,
  Phase 3+ work surfaces tools that the user can't ground.

This is why both endpoints need clarity work, not just one. A "decision
made" without Destination clarity is a guess; a "decision made" without
Origin clarity is fantasy.

## Multi-frame clarity

In a multi-frame session, each frame has its own Origin and Destination
clarity states. A sub-frame's clarity work feeds the parent frame:

- Sub-frame resolves with its Destination Locked → parent frame's
  Destination (or Origin) gains clarity.
- Sub-frame fails to resolve → parent frame's clarity-stuck endpoint may
  need a different sub-frame.

Track each frame's clarity independently in the Case File `goal_stack`
frontmatter.
