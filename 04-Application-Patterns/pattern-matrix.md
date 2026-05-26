---
doc_type: application_pattern
form: Matrix
audience: ai
last_updated: 2026-05-13
---

# Pattern — Matrix

## What this Form is

A two-dimensional grid that sorts a set of items along two axes. Each cell
captures a class of items defined by its position. The matrix forces the
user to confront combinations they might not naturally inventory (e.g.,
"important but not urgent" — the cell people most often neglect).

Schema reference: `tt_Form: Matrix` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## Setup

Get the user's consent before introducing the tool:

> "There's a tool called the Eisenhower Matrix that might help here.
> It's a 2×2 grid that sorts things by urgency and importance. Want to
> walk through it together?"

If the user says yes, proceed. If they hesitate or say no, switch tools
or return to questioning.

## Engagement

1. **Explain the axes briefly.** Two short sentences. Avoid jargon.

   > "The horizontal axis is urgency — does this need attention now or
   > can it wait. The vertical axis is importance — does it actually
   > matter to your goals."

2. **Choose an entry cell.** Usually the most natural one for the user's
   situation. For Eisenhower Matrix, that's often "important AND urgent"
   — the cell where most people start.

3. **Walk the cells one at a time.** Ask the user what fills the current
   cell in their case.

   > "Starting with 'important AND urgent' — what in your life right now
   > falls in this box?"

4. **Move to the next cell.** Continue until all cells are filled — or
   explicitly marked "not applicable" — by the user.

5. **Step back.** When all cells are filled, ask the user what they see.

   > "Now that the grid is filled, what stands out? Anything that
   > surprised you?"

## Completion criteria

All cells filled (or explicitly marked N/A), AND the user has spoken to
what they see in the filled grid. The matrix is "complete" only when both
filling and reflecting have happened.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Eisenhower Matrix
Frame: 0
Step: 5.1 (criteria) / 5.2 (decision tool)
Started: 2026-05-13T15:23:00
Completed: 2026-05-13T15:48:00

Filled matrix:
|                | Urgent                          | Not Urgent                      |
|----------------|---------------------------------|---------------------------------|
| **Important**  | "Job offer deadline (next week)" | "Career conversation with spouse" |
| **Not Important** | "Slack notifications"        | "Mowing the lawn"               |

User's reflections:
- "I'd been treating Slack like it was top-left."
- "Career conversation has been in the wrong box."
```

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User can't fill a cell. | The gap is data. Ask: "What's making it hard to think of something for that cell? Is the box not relevant, or have you not been considering things in that box?" |
| User wants to add a third axis ("we should also rate by cost"). | Note the impulse: "That's a different cut. Let's finish this matrix first and then we can do a separate one if it'll help." |
| Cells reveal the framing is wrong. | The matrix did its job. Pause; consider re-framing the problem (chapter 03 §5.4 jump signals). |
| User fills cells with too-broad categories. | Push for specificity: "Within 'important and not urgent,' name one or two concrete things." |
| User insists on placing the same item in multiple cells. | Honor the ambiguity. Note that an item straddles cells. The straddle is itself information about how the framing is working. |

## Example tools (from the library)

- **Eisenhower Matrix** — Urgency × Importance. The classic application.
- **Eisenhower Matrix is not the only 2×2.** Other examples in the library:
  - **Stakeholder Power-Interest Grid** — Power × Interest. For
    identifying which stakeholders need active management.
  - **Ease-Impact Assessment Matrix** — Ease of doing × Impact. For
    initiative prioritization.
- **Weighted Decision Matrix** — Options × Criteria. (Note: this is a
  scoring rubric in form; it uses the matrix shape but the engagement is
  closer to `pattern-scoring-rubric.md`. In MVP, fall back to this
  pattern with care.)

## When NOT to use a Matrix

- The decision has more than 2 meaningful dimensions and can't be
  collapsed.
- The categories are continuous, not discrete.
- The user is in an emotional state where filling a grid feels too
  clinical (use Therapist persona; come back to the matrix later).
- The user explicitly says it doesn't fit how they think (per master
  plan sample-08-user-resistance).
