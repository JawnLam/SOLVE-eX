---
doc_type: process_framework
doc_purpose: frame_lifecycle
audience: ai_and_human
read_order: 6
last_updated: 2026-05-13
---

# Frame Lifecycle

A frame has a lifecycle. This chapter specifies the states a frame can be
in, the transitions between states, and what the Case File records at
each transition.

## States

| State | Meaning |
|-------|---------|
| **Created** | Frame has been pushed onto the goal-stack with stub Origin and Destination. No work done yet. |
| **Active — Endpoint Clarification** | Phase 1 and Phase 2 work in progress. Both endpoints are being clarified. |
| **Active — Path Work** | Phases 3, 4, 5 work in progress. Both endpoints are Locked (or close); the path between them is being charted. |
| **Active — Execution** | Phase 6 work in progress. The user is acting on the chosen path. |
| **Resolved** | The frame's Destination has been reached (or determined unreachable with clear understanding why). Frame is no longer active. |
| **Paused** | The user wants to stop work on this frame but keep it open for future. |
| **Abandoned** | The user has decided the frame is no longer relevant. |
| **Failed** | Irrecoverable — the user's circumstances changed such that the question no longer applies. |
| **Popped** | Removed from the active stack. Archived in the Case File. (Popped frames may be in any of the resolved / paused / abandoned / failed states.) |

## Transitions

```
Created
  └── (first turn of work) ──> Active — Endpoint Clarification

Active — Endpoint Clarification
  ├── (both endpoints Locked) ──> Active — Path Work
  ├── (user pauses) ──> Paused
  ├── (user abandons) ──> Abandoned
  └── (circumstances change) ──> Failed

Active — Path Work
  ├── (Phase 5 produces a chosen path; user moves to act) ──> Active — Execution
  ├── (user pauses) ──> Paused
  ├── (Phase 5 reveals no viable path) ──> the frame may become Failed, or return to Phase 4 for more options, or push a sub-frame
  └── (jump back to Phase 1/2) ──> Active — Endpoint Clarification

Active — Execution
  ├── (action plan executed; outcome reviewed) ──> Resolved
  ├── (user pauses execution) ──> Paused
  ├── (action fails; user re-plans) ──> back to Active — Path Work (or earlier)
  └── (user abandons) ──> Abandoned

Resolved / Paused / Abandoned / Failed
  └── (frame remains in Case File; may be revisited in a future session)
```

## State transitions and the Case File

Each transition updates the Case File:

| Transition | Case File update |
|-----------|------------------|
| Created | Add `frame_id` to `goal_stack` frontmatter with stubs. Add `## Frame N — {short title}` section to body. |
| Endpoint Clarification ↔ Path Work ↔ Execution | Update `phase_step` field; no state-name field in frontmatter (state is inferable from phase_step + clarity). |
| Resolved | Update goal-stack entry with `status: resolved`. Add a `### Resolution` section to the frame's body block. |
| Paused | Update goal-stack with `status: paused`. Add a `### Pause` section noting where work left off and why. |
| Abandoned | Update goal-stack with `status: abandoned`. Add a `### Abandon` section with the user's reason. |
| Failed | Update goal-stack with `status: failed`. Add a `### Failure` section noting what changed. |
| Popped | Update goal-stack: `active: false`. The frame's resolved/paused/abandoned/failed status is preserved. Parent frame's `active: true` is restored. |

## Frame body structure across lifecycle

A frame's `## Frame N — {short title}` body section grows over the frame's
lifecycle. Sections in roughly the order they appear:

1. `## Frame N — {short title}`
2. `### Frame opened: YYYY-MM-DD-HHMM`
3. `### Origin ({clarity-state})` — populates during Endpoint Clarification
4. `### Destination ({clarity-state})` — populates during Endpoint Clarification
5. `### Reasons to Resolve (Step 2.1)`
6. `### Goal Statement (Step 2.2)`
7. `### Requirements (Step 2.3)`
8. `### Current Facts (Step 3.1)`
9. ... (Steps 3.2, 3.3, 3.4)
10. `### Root Causes (Step 4.1)`
11. `### Ideas (Step 4.2)`
12. `### Refined Options (Step 4.4)`
13. `### Evaluation Criteria (Step 5.1)`
14. `### Decision Tool Used (Step 5.2)`
15. `### Validation (Step 5.3)`
16. `### Action Plan (Step 6.2)`
17. `### Execution Notes (Step 6.3)`
18. `### Follow-up Review (Step 6.4)`
19. `### Resolution` / `### Pause` / `### Abandon` / `### Failure` — at end of lifecycle

Sections that have no content yet are marked `(not yet started)`. They are
not deleted when work skips them — their presence signals that step was
not visited.

## Pause vs. Abandon

The distinction matters:

- **Paused frames** are expected to resume. The Case File preserves enough
  context for a clean resumption. Pause is the right move when the user
  is tired, when time runs out, or when the frame needs an external input
  the user has to gather between sessions.
- **Abandoned frames** are explicitly closed. The user has decided the
  question no longer applies. The Case File records why, but doesn't
  hold context for resumption.

When in doubt, ask: "Are we stopping for now and might come back, or are
you done with this question?"

## Failed frames

Failure is rare and specific: the user's circumstances change so
fundamentally that the question is no longer answerable in its current
form. Example: a frame about whether to take a job offer; the company
withdraws the offer mid-deliberation.

A failed frame is not a system failure — it's an environmental change.
Treat the failure as data:

- Mark the frame `status: failed`.
- Note what changed in `### Failure`.
- Ask the user if a new frame should open ("Is there a different question
  that's surfaced now that the offer is gone?").

## Stale active frames

If a frame has been Active for 4+ sessions without progress, ask whether
to:

- **Pause** it and free attention.
- **Push a sub-frame** that targets the bottleneck.
- **Abandon** it if the user no longer cares.
- **Push through** with a different tool or persona shift.

Long-running active frames are a quality signal worth surfacing.

## Multi-session frames

A frame may span many sessions. The Case File's resumption protocol
(`{ROOT}/00-Instructions/06-the-case-file.md` §6.5) handles cross-session
continuity. Specifically:

- On session start, the resumption check asks the user where to pick up.
- The user's response may transition the frame (e.g., pause → active,
  or active → paused-explicitly).
- The Case File `session_count` and `total_turns` increment.

## Frame metadata audit

Periodically (after each session, or before sharing a Case File), audit
the goal_stack frontmatter:

- Every frame's `active` field is correct.
- Exactly one frame has `active: true` (unless all frames are
  resolved/paused/abandoned/failed, in which case zero).
- Every frame's `parent_frame` resolves to an existing `frame_id`.
- `status` field is consistent with the body's terminal section
  (`### Resolution` / etc.).

`07-Scripts/validate-case-file.py` (Phase 2) automates this audit. In MVP,
do it manually before closing a session.

## What a frame is NOT

- Not a step. Steps are units of work *within* a frame. A frame may
  visit 3 of the 21 steps or all 21; the count says nothing about whether
  it's still one frame.
- Not the same as a session. A session is a unit of time; a frame is a
  unit of question. Sessions can hold multiple frames; frames can span
  multiple sessions.
- Not always nested. A user's session may have only one frame and no
  recursion. Most simple decisions are single-frame.
- Not bound to a particular outcome. A frame's lifecycle accommodates
  resolved, paused, abandoned, and failed outcomes equally.
