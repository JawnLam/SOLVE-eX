---
doc_type: process_framework
doc_purpose: push_pop_rules
audience: ai_and_human
read_order: 5
last_updated: 2026-05-13
---

# Push / Pop / Jump Rules

The diagnostic loop (`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`
step 6) scans every turn for push, pop, and jump signals. This chapter
specifies what those signals are and what triggers them.

## 5.1 Three motions

The goal-stack can move in three ways:

| Motion | Effect | Trigger |
|--------|--------|---------|
| **Push** | Open a sub-frame. Parent paused. | The current frame cannot resolve without first answering a prerequisite question. |
| **Pop** | Close a sub-frame. Parent resumes. | The current frame's Destination is Locked, or the user asks to return, or the frame is failing. |
| **Jump** | Move to an earlier step in the same frame. | New information invalidates a prior step's artifact, or the frame was misformulated. |

## 5.2 Push signals

Push when any of these are present:

1. **The user surfaces a related-but-distinct sub-problem.**

   > "Wait — before I figure out this job thing, I need to figure out
   > whether I even want to keep working."

   → Push: sub-frame is "decide whether to keep working at all."

2. **An endpoint is Unclear AND clarifying it in-frame is failing AND
   the user is willing to take a detour.**

   Symptom: 4+ turns of Phase 1 or 2 work on the same endpoint with no
   progress in clarity state.

   Proposed push: sub-frame whose Destination is "make this endpoint
   clear." Surface the proposal:

   > "We've spent a while trying to land what you actually want from
   > this. It might help to step back and work on a more fundamental
   > question first — what do you value here in the broader sense?
   > Want to try that?"

3. **A tool application reveals an underlying unanswered question.**

   Symptom: a tool that should produce a step's artifact instead produces
   "I don't know what to put here because I haven't figured out X."

   Push: sub-frame whose Destination is "figure out X."

4. **A previously-resolved frame's Destination must be re-derived
   because of new information.**

   Symptom: the user states a fact that invalidates a previously-locked
   element in a parent frame. The parent's locked endpoint downgrades.

   This may push a new sub-frame to re-derive the endpoint, or jump back
   within the parent frame (see §5.4 below).

## 5.3 Pop signals

Pop when any of these are present:

1. **The current frame's Destination is Locked AND its artifact is in
   the Case File.**

   The sub-question is resolved. Pop and return its output to the parent.

2. **The user explicitly asks to return to the parent.**

   > "Okay, this is helpful, but let's get back to the original
   > question."

3. **The current frame is failing AND the user is exhausted.**

   Symptom: 6+ turns in the same frame with no clarity progression, and
   user energy is low.

   Proposed pop: pop with `status: paused` (not resolved). Surface:

   > "We've been working on this for a while and it's not getting
   > traction. Want to set it aside for now and come back to the main
   > question, or take a break and come back to it next session?"

4. **Time pressure forces returning to the higher-level question.**

   If the user has a hard time-budget for the session and the sub-frame
   is taking too long, pop with `status: paused` and acknowledge:

   > "We're running out of time today. Let's hold the values-inventory
   > thread and come back to the career question. We can pick the
   > inventory up next session."

## 5.4 Jump signals

Jump when any of these are present:

1. **New information invalidates a previously-locked element.**

   Example: Phase 2 was locked, the user said the goal was X. In Phase 3
   they learn a fact that makes X unreachable.

   Jump: return to Step 2.2 and re-derive the goal statement with the
   new fact incorporated.

2. **The user reframes the problem mid-process.**

   Example: in Phase 5 evaluation, the user says "actually, what I really
   care about is Y, not what we said in Phase 2."

   Jump: return to Step 2.1 or 2.2 to capture the new framing.

3. **A tool application reveals the problem was misformulated.**

   Example: a root-cause analysis in Phase 4 reveals the Phase 1
   problem statement was symptomatic, not causal.

   Jump: return to Step 1.2 to re-write the problem statement.

## 5.5 The default decision tree

When the diagnostic loop's step 6 detects a candidate signal, run this
mental tree:

```
Is the signal pointing to a NEW question that needs its own answer?
├── Yes → consider Push (§5.2)
└── No → Is it pointing to information that changes a prior step?
         ├── Yes (in current frame) → Jump (§5.4)
         └── No → Is the current frame complete or stuck?
                  ├── Complete (Destination Locked) → Pop (§5.3.1)
                  ├── Stuck and exhausted → Pop with paused (§5.3.3)
                  └── Still in progress → no motion; continue
```

Run this tree when a signal is detected, not every turn. Most turns do
not trigger a motion.

## 5.6 Surfacing a motion to the user

The user is always informed of a motion, with consent invited:

- **Push:** "Want to step back and work on a more fundamental question
  first, or stay on this thread?"
- **Pop (resolved):** "Sounds like we've got what we needed there. Want
  to bring it back to the original question?"
- **Pop (paused):** "We've been at this a while without traction. Want
  to set it aside for now?"
- **Jump:** "It sounds like what you just said changes the goal we'd
  written earlier. Want to take another pass at it?"

If the user declines a proposed motion, respect the decline. Try a
different move.

## 5.7 Motion combinations

Sometimes a turn triggers multiple motions. Examples:

- **Pop then push.** The current sub-frame resolves; the resolution
  reveals another sub-question that must be answered before returning to
  the original parent. Pop, then immediately propose a new push.
- **Jump then push.** A jump back reveals that the earlier step requires
  information the user doesn't have; push a sub-frame to gather it.
- **Push then pop.** Rare. The sub-frame opens, is immediately resolved
  in one turn ("oh, I realize the answer is X now that I said it out
  loud"). Pop in the next turn.

Handle compound motions in two responses, not one. The user needs to
absorb each motion separately.

## 5.8 Anti-patterns

Avoid these:

| Anti-pattern | Why it fails |
|--------------|--------------|
| **Silent push.** Opening a sub-frame without telling the user. | Breaks user agency; user feels lost. |
| **Forced push.** Insisting on a sub-frame the user declined. | User feels coerced; loses trust. |
| **Pop without resolution.** Popping a sub-frame that wasn't actually resolved, just to escape the work. | Parent frame inherits an unresolved input; downstream work is shaky. |
| **Jump without acknowledging the prior step.** Re-doing Step 2.2 without noting that the prior version is being revised. | Case File loses the history of revision; the user feels gaslit. |
| **Push when the user wants action.** "I don't want to figure out my values; I want to know whether to take the offer." Insisting on the values sub-frame anyway. | User leaves the session. |

## 5.9 Motion logging

Every push, pop, and jump is logged in the Case File:

```yaml
# In goal_stack frontmatter (after a push):
goal_stack:
  - frame_id: 0
    active: false
    ...
  - frame_id: 1
    parent_frame: 0
    active: true
    ...
```

And in the body's Session Log:

```markdown
#### Turn 23
User: "Wait — before this job thing, I need to figure out…"

Diagnostic:
- Motion: PUSH
- New frame: 1 ("values inventory")
- Parent: 0
- Strategy: Permission check

AI [Partner]: "It sounds like there's a question underneath…"
```

This record makes the recursion visible to post-session review.

## 5.10 No motion is also a decision

Most turns produce no motion. The frame continues. The phase-step
advances within the frame. The clarity states evolve.

The diagnostic loop is not a motion-detection algorithm; motions are the
exceptional case. Default to "no motion" unless a signal is unambiguous.
