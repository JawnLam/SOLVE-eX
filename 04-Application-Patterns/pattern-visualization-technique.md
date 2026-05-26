---
doc_type: application_pattern
form: Visualization technique
audience: ai
last_updated: 2026-05-14
---

# Pattern — Visualization Technique

## What this Form is

A drawing-based or spatially-structured method that uses two-
dimensional layout — nodes, edges, regions, gradients, position
— to reveal patterns that linear text obscures. Visualization
techniques differ from matrices by being topologically free (no
fixed grid); they differ from decision trees by being relational
rather than sequential; they differ from canvases by producing the
structure as the user fills, rather than filling a pre-built
template.

Schema reference: `tt_Form: Visualization technique` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Visualization Technique pattern when the tool's `tt_Form`
is `Visualization technique`, and:

- The user's situation has multiple interacting elements whose
  relationships are not obvious from a list.
- Spatial structure (proximity, distance, direction, hierarchy)
  carries information the user benefits from seeing.
- The user can engage with a sketch — either drawing themselves or
  watching one assemble.
- Patterns are likely to emerge from the layout that would be
  invisible in prose.

## Preparation steps

1. **Verify the visualization's shape fits the question.** A causal
   loop diagram fits feedback dynamics; a sociogram fits relational
   structure; a mind map fits open exploration. The shape determines
   what gets surfaced.
2. **Pick the medium honestly.** Live drawing on a whiteboard, a
   shared canvas tool, or text-only ASCII / structured rendering
   each have constraints. State which medium is in use and what it
   trades for what.
3. **Identify the seed.** Most visualizations start with one node
   — the user's primary stakeholder, primary variable, primary
   question. The seed determines what the layout grows from.

## Application steps

1. **Name the visualization and what it produces.**

   > "There's a way to draw this called a Causal Loop Diagram. We
   > sketch the variables and the arrows between them — which thing
   > influences which, and which loops feed back. The shape often
   > shows why things are sticky in ways the prose doesn't."

2. **Build the structure incrementally.** Add one node or one edge
   at a time. The user names what comes next; the AI records and
   structures.

   > "Start with the central variable — what's the thing whose
   > behavior we're trying to explain?"

   Then:

   > "What influences that variable? Each influence is a node with
   > an arrow into the central one."

3. **In text-only contexts, render structurally.** ASCII boxes,
   indented hierarchies, structured text, or markdown tables.
   The rendering matters less than the layout being visible.

   ```
   [Customer requests]
       │ (+)
       ▼
   [Engineering load] ──┐
       │ (+)            │ (-)
       ▼                │
   [Cycle time]         │
       │ (-)            │
       ▼                │
   [Customer satisfaction] ──┘
   ```

4. **Pause and read what's there.** After each layer is added, ask
   the user what they see. Patterns surface in observation, not in
   drawing.

   > "Now that the four variables are on the diagram — what do you
   > notice? Anything that looks different from how you've been
   > thinking about it?"

5. **Trace the patterns explicitly.** Loops, hierarchies, clusters,
   gaps — the structural features the visualization reveals. Name
   them as they emerge.

6. **Capture the diagram in the Case File.** Either as a
   structured-text representation (preferred), an image attachment,
   or a link to the live canvas.

## Completion criteria

The visualization is structurally complete (the relevant nodes and
edges are present), the user has read the diagram and named at
least one pattern the layout revealed, AND the patterns are
captured in the Case File alongside the structural representation.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Causal Loop Diagram (team-velocity question)
Frame: 0
Step: 4.1 (root causes) / 3.3 (systems facts)
Started: 2026-05-14T21:00:00
Completed: 2026-05-14T21:35:00

Diagram structure (text representation):
Variables:
- A: Customer requests
- B: Engineering load
- C: Cycle time
- D: Customer satisfaction

Edges:
- A → B (+): more requests increase load
- B → C (+): more load increases cycle time
- C → D (-): longer cycle time decreases satisfaction
- D → A (-): lower satisfaction decreases new requests

Identified loop: A → B → C → D → A (balancing loop, time-delayed).

Patterns surfaced:
- "There's a balancing loop, not a reinforcing one — high load is
  self-correcting through dissatisfaction. The system doesn't need
  to be fixed; it needs to NOT correct itself."
- "The time delay between cycle time and dissatisfaction is the
  load-bearing variable I'd been missing."
```

## Common variations

- **Causal Loop Diagrams** — feedback structure in systems. Nodes
  are variables; edges are signed influences; loops are
  reinforcing or balancing.
- **Stakeholder maps / Sociograms** — relational structure. Nodes
  are people / groups; edges are relationships, influence, or
  information flow.
- **Mind maps** — free exploration. One central node; branches
  radiate. Used when the user is in divergent thinking.
- **Issue trees** — hierarchical decomposition (also covered in
  pattern-decision-tree.md; the visualization-technique framing
  applies when the user is building rather than analyzing).
- **Spatial gradients** — heatmaps, dot voting, two-dimensional
  positioning of qualitative items. Used when the user is
  expressing intensity or preference rather than structure.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| Diagram becomes too dense to read | The visualization has lost its discriminating power. Either remove low-information nodes/edges or split into multiple smaller diagrams (one per loop, one per stakeholder cluster, etc.). |
| User adds nodes faster than relationships | The user is treating the diagram as a list. Pause and ask about edges: "What's the relationship between these last two nodes?" |
| Patterns don't surface | Either the wrong variables are on the diagram, or the user is still in build mode and hasn't stepped back. Surface explicitly: "Let's pause and read what we have." |
| Medium constraints distort the work | Text-only renderings of complex diagrams lose information. Acknowledge: "The structured-text version captures the topology but not the layout. If a real canvas would help, that's a real next step." |
| AI sketches the diagram and presents it to the user | This is a different tool — the AI summarizing rather than the user drawing. Visualization technique pattern requires the user to participate in the construction; if the AI builds in isolation, switch to a Mental Model pattern instead. |
| Diagram is drawn but never referenced again in the session | A visualization that doesn't get re-read is a doodle. Loop back: "What does this diagram tell you about [the original question]?" |

## Example tools (from the library)

- **Causal Loop Diagrams** — systems-thinking diagrams of
  feedback structure. Use when the question involves dynamics,
  feedback, or "why doesn't this just fix itself."
- **Mind Mapping** — radial exploration around a central concept.
  Use in divergent-thinking phases when the user is generating
  rather than choosing.
- **Influence Sociogram** — diagram of who influences whom in a
  group. Use in stakeholder-mapping work where the relational
  topology matters.

## A note on `tt_Applicability`

Visualization techniques have a particular constraint on the
`tt_Applicability` facet:

- **`runtime_applicable`** is the default; the AI builds the
  visualization with the user during the session.
- **`describable_only`** applies when the visualization requires a
  physical artifact (whiteboard, sticky notes, large paper) the
  conversation cannot produce. In that case, describe the tool and
  hand off; do not pretend the conversation can build the diagram.

Match the application mode to the actual capability of the
current session.

## When NOT to use a Visualization Technique

- The user's situation has 1–3 elements. Visualization is overhead
  for simple cases; a sentence or two does the work better.
- The medium cannot support the diagram. Text-only contexts can
  carry small structured diagrams but not large free-form ones.
  Be honest about the constraint.
- The user is in emotional regulation work. Visualization is
  cognitive; switch to Therapist persona and revisit.
- The user has explicitly resisted diagram-style frameworks ("I
  don't think in pictures"). Honor the resistance; the content can
  come through prose.
- The user's situation is genuinely temporal, not relational. Use
  Sequenced Workflow or a timeline rather than a free-form
  diagram.
