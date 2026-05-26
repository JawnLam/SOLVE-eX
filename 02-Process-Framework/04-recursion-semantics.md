---
doc_type: process_framework
doc_purpose: recursion_semantics
audience: ai_and_human
read_order: 4
last_updated: 2026-05-13
---

# Recursion Semantics

SOLVE eX is fractal. A frame's clarification work may itself require its
own SOLVE eX cycle. That cycle is a **sub-frame**. Sub-frames may
themselves require their own sub-frames. The stack of frames is the
**goal-stack**.

This chapter specifies what the recursion is, why it exists, and how to
operate the goal-stack.

## Why recursion exists

The dominant failure mode in human decision-making is being in the wrong
phase. The second-most-common failure is **trying to resolve a question
that is not yet well-formed**.

Example: "What career should I pursue?" The user cannot answer this
without first being clear on what they value in work. "What do I value
in work?" is itself a SOLVE eX-shaped question with its own endpoints and
phases. It is also independently runnable.

Recursion lets the system pause the parent question, run the prerequisite
question to resolution, then resume the parent with the prerequisite's
output as input.

## The goal-stack

The goal-stack is an ordered list of frames. Only one frame is active at
a time — the top of the stack. The Case File stores the stack in
frontmatter:

```yaml
goal_stack:
  - frame_id: 0
    origin: "Unhappy at job"
    origin_clarity: locked
    destination: "Satisfying career path"
    destination_clarity: partially_clear
    phase_step: "2.2"
    active: false
  - frame_id: 1
    origin: "I don't know what I value in work"
    origin_clarity: locked
    destination: "I have a working values inventory"
    destination_clarity: clear_but_unstable
    phase_step: "4.2"
    parent_frame: 0
    active: true
```

In this snapshot, Frame 1 is the active sub-frame; Frame 0 is paused
waiting for Frame 1 to resolve.

## Push: opening a sub-frame

When you push a sub-frame:

1. The parent frame becomes inactive (`active: false`).
2. A new frame is created with a unique `frame_id` (one more than the
   highest current id).
3. The new frame's `parent_frame` points to the parent.
4. The new frame becomes active (`active: true`).
5. The Case File body gets a new `## Frame N — {short title}` section.

The user is informed of the push explicitly:

> "It sounds like there's a question underneath this one — about what
> you actually value in work. Want to pause the career question for a
> bit and work on that one first, or hold it for later?"

If the user declines the push, do not force it. Stay in the parent frame
and try a different approach.

## Pop: resolving a sub-frame

A sub-frame pops when:

- Its Destination is Locked (i.e., the sub-question is resolved).
- The user explicitly asks to return to the parent.
- The sub-frame is failing and the user is exhausted.

On pop:

1. The popped frame becomes inactive (`active: false`) and its `status`
   in the goal-stack reflects the resolution (`resolved` / `paused` /
   `abandoned`).
2. The parent frame's `parent_frame` chain locates the next-up frame.
3. That frame becomes active again (`active: true`).
4. The popped frame's output (the resolved Destination) is fed into the
   parent frame as input.

The user is informed:

> "We've got a working values inventory now (meaningful work, autonomy,
> proximity to family). Want to bring that back to the career question?"

## Stack depth

There is no hard cap on stack depth. The system flags depth >5 to the
user:

> "We've gone three sub-problems deep. Are we still on the right track,
> or should we surface back to the original question?"

Past depth 5, the user is usually exhausted, fragmented, or being led
astray. Check in.

## Frame breadcrumbs

The active frame is shown to the user as a breadcrumb when helpful:

> "You're working on: [Frame 2: values inventory] ← came from [Frame 1:
> career clarity] ← came from [Frame 0: unhappy at job]."

This visibility prevents the user from feeling lost in their own thinking.
Surface breadcrumbs:

- When depth ≥ 2 and the user signals confusion.
- After a successful push, to confirm the move.
- When popping, to confirm where they're returning to.
- When the user asks "wait, what were we doing?"

Do NOT surface breadcrumbs every turn. Internal tracking is constant;
external display is contextual.

## What a frame inherits from its parent

A child frame inherits:

- The user's profile (handle, prior reflections, communication style).
- The session's emotional baseline.
- The active persona unless the child frame demands a different one.
- The Case File context.

A child frame does **not** inherit:

- The parent frame's Origin and Destination (the child has its own).
- The parent frame's phase-step (the child runs its own SOLVE eX cycle).
- The parent frame's tools-applied list (each frame logs its own).

## Sibling frames

Pushing two sub-frames from the same parent is possible but rare. The
common case: one sub-frame at a time.

If a session has unrelated questions that surface in parallel:

- If they are genuinely independent, encourage the user to open them as
  separate Case Files (don't entangle).
- If they are related (one is causal to the other), push one as a child
  of the other.

## Recursion depth and persona

Deeper frames often have higher emotional weight (the user is engaging
fundamental questions). Watch for Therapist persona triggers especially
in deep frames.

## Recursion and the Case File

Each frame has its own `## Frame N — {title}` body section. Resolved
frames are NOT deleted on pop — they remain in the Case File as part of
the session's record. The user can read later how earlier frames were
resolved.

The `Tools Applied` section is global (one section for the whole
session) but tools are tagged with `Frame: N` so the record is
disentangleable.

## When NOT to recurse

Some questions look like they need a sub-frame but actually need a
different move:

- **The user is venting.** A push of a sub-frame in the middle of venting
  is a misread. Mirror first, push later if needed.
- **The user wants action, not introspection.** "I don't want to figure
  out what I value, I want to know whether to take this offer." Respect
  it. Work the surface frame.
- **The "sub-frame" is actually a re-statement of the parent frame.**
  If a candidate sub-frame's Destination is identical to or trivially
  derivable from the parent's, you do not have a sub-frame; you have a
  re-framing within the same frame.

When unsure, ask the user. "Should we treat this as a separate question
to work on first, or fold it back into the main thread?"

## Recursion in MVP vs. Phase 2

MVP supports recursion fully (stack push, stack pop, breadcrumbs,
per-frame tracking in Case File). Phase 2 adds tooling around it:

- `07-Scripts/show-stack.py` — visualize the current stack from a Case
  File.
- Multi-frame Case File summaries (`case-file-summary.py`).
- Richer breadcrumb formatting.

The recursion semantics themselves are stable in MVP.
