---
doc_type: process_framework
doc_purpose: phases_spec
audience: ai_and_human
read_order: 1
last_updated: 2026-05-13
---

# The Six SOLVE eX Phases

The six phases are the structural skeleton of a frame's work. A frame
need not visit all six — simple frames may resolve at Phase 2 or Phase 4 —
but the order is meaningful when phases are visited.

| # | Letter | Title | Core question |
|---|--------|-------|---------------|
| 1 | **S**  | State | What is the current situation? |
| 2 | **O**  | Objective | What is the desired outcome? |
| 3 | **L**  | Learn | What facts and data are relevant? |
| 4 | **V**  | Vision | What are the possible paths or solutions? |
| 5 | **E**  | Evaluate | Which path or solution is best? |
| 6 | **eX** | eXecute | How is it put into action? |

## Phase 1 — State (the Origin work)

The frame's Origin — "where you are" — gets articulated. Phase 1 surfaces
the user's current situation, problem statement, and framing. The end of
Phase 1 leaves the user with a clear sense of *what is*.

A locked Phase 1 has:

- A coherent description of the current situation (Step 1.1).
- A compressed one-sentence problem statement (Step 1.2).
- An explicit frame for the situation (Step 1.3) — i.e., an answer to
  "one way to look at this is…"

## Phase 2 — Objective (the Destination work)

The frame's Destination — "where you want to be" — gets articulated. Phase
2 surfaces *why* the user cares, *what* they actually want, and *what
must be true* for any acceptable outcome.

A locked Phase 2 has:

- Articulated reasons to resolve the situation (Step 2.1).
- A coherent goal statement (Step 2.2).
- Explicit requirements for any acceptable outcome (Step 2.3).

Phase 2 is the most frequently under-developed phase in user-led
decision-making. People act on goals they have not articulated. The
system's value is highest in this phase precisely because users skip it.

## Phase 3 — Learn (fact-gathering)

Once both endpoints are locked, the path between them needs information.
Phase 3 surfaces the facts and data the user needs to chart a path:

- Step 3.1 — current facts and data
- Step 3.2 — past facts and data (history)
- Step 3.3 — systems facts and data (how things work)
- Step 3.4 — future facts and data (trends, projections)

Phase 3 is where assumptions get tested against reality. Users often
believe they are in Phase 4 ("what should I do?") when they are actually
in Phase 3 ("I do not yet know enough to choose").

## Phase 4 — Vision (divergent path generation)

Phase 4 is divergent: surface many possibilities, defer judgment.

- Step 4.1 — root cause analysis (why is the gap there?)
- Step 4.2 — idea formation (what could be done?)
- Step 4.3 — anticipative solution crafting (what would resolve this?)
- Step 4.4 — idea refinement (sharpen and combine ideas)

The mistake of premature convergence kills Phase 4. The user wants to
"just pick one"; the system's job is to insist on inventory before
selection.

## Phase 5 — Evaluate (convergent option assessment)

Phase 5 is convergent: assess options against criteria.

- Step 5.1 — define evaluation criteria
- Step 5.2 — select decision tools (matrix, scoring rubric, decision tree,
  expected value, etc.)
- Step 5.3 — validate decision impact (against the user's gut, against
  reversibility, against second-order effects)

Phase 5's most important step is 5.3, the gut-check. A decision that
scores well on a rubric but feels wrong to the user is usually scoring
the wrong criteria. The system never overrides the gut-check; it surfaces
the mismatch and asks what the user wants to do with it.

## Phase 6 — eXecute (action and follow-up)

Phase 6 is implementation.

- Step 6.1 — design and test the solution (small experiments first when
  possible)
- Step 6.2 — create an action plan (concrete, time-bound)
- Step 6.3 — implement the action plan
- Step 6.4 — conduct follow-up and feedback (did it work? what changed?)

Phase 6 often extends across multiple sessions. The Case File's
resumption protocol (chapter 06, §6.5) is built for this.

## Phase visits are not mandatory

A frame may need only a subset of phases. Examples:

- **A "define your values" frame** may resolve at Phase 4 with a vision
  inventory and no need for evaluation or execution.
- **A "compare two job offers" frame** with both Origin and Destination
  already locked may start at Phase 5 directly.
- **A "what do I even want" frame** may iterate Phases 1 and 2 indefinitely
  without ever reaching Phase 3.

The six phases are scaffold, not mandatory tour.

## Phase order is not strictly linear

Phases revisit. A Phase 5 evaluation may reveal that the Phase 2 goal
statement was incomplete; the frame jumps back to Phase 2. A Phase 3
fact-finding may reveal that the Phase 1 problem was misframed.

The diagnostic loop (`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`,
step 6) handles these jumps explicitly. Jumping back is normal, not a
failure.

## Phase-to-tool mapping

Each tool in `{ROOT}/01-Tools/Tool Entries/` is tagged with
`tt_SOLVE_eX_Phase` (one or more phases where the tool fits). The Tool
Selector uses this as a second-cut filter after `tt_Clarifies`. See
`{ROOT}/00-Instructions/01-the-cognitive-model.md` §1.6.

Examples of phase-affinity:

- **Phase 1 tools:** Context Clarity Navigator, Situation Analysis, Five
  Whys (for problem-framing), 5W1H, Iceberg Model.
- **Phase 2 tools:** Eulogy Exercise, Ikigai, Schwartz Values Survey,
  Regret Minimization Framework, Three Horizons.
- **Phase 3 tools:** PESTEL, SWOT, Historical Trend Analysis, Causal Loop
  Diagram.
- **Phase 4 tools:** SCAMPER, TRIZ, Lateral Thinking, Six Thinking Hats
  (for divergent), De Bono's PO.
- **Phase 5 tools:** Eisenhower Matrix, Decision Matrix, Expected Value
  Decision Tree, Pre-Mortem (for gut-check), Pros-Cons.
- **Phase 6 tools:** Implementation Intentions, If-Then Planning, GTD
  Weekly Review, After-Action Review.

The full mapping is in the library's frontmatter; do not memorize it.
Query at runtime via `tt_SOLVE_eX_Phase` facets.
