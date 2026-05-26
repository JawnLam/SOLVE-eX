---
doc_type: application_pattern
form: Decision tree
audience: ai
last_updated: 2026-05-14
---

# Pattern — Decision Tree

## What this Form is

A branching structure that maps a decision as a series of nodes
(decision points), branches (options at each node), and terminal
outcomes. Decision trees differ from scoring rubrics by being
sequential rather than parallel — the choice at node 1 changes
what nodes 2 and 3 look like. They differ from matrices by
representing temporality and conditional structure.

Schema reference: `tt_Form: Decision tree` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Decision Tree pattern when the tool's `tt_Form` is
`Decision tree`, and:

- The decision has sequential structure — the first choice
  determines what choices come next.
- The user can identify discrete options at each node, not a
  continuous range.
- Probabilities and values (or rough proxies) can be assigned to
  the terminal outcomes; without them, the tree is shape-only.
- The user wants to reason about expected outcomes across paths,
  not just the immediate next move.

## Preparation steps

1. **Identify the decision node.** The single decision being
   analyzed. Trees with multiple parallel decisions are usually
   two trees.
2. **Bound the time horizon.** A tree that branches 7 layers deep
   loses signal in the leaves. Most useful trees are 2–4 layers.
3. **Identify what "outcome" means.** Money? Time saved? Risk
   reduced? Identity preserved? The unit determines what gets
   counted at the leaves.

## Application steps

1. **Name the tree and the decision being analyzed.**

   > "Let's map this as a decision tree. The starting node is your
   > offer-acceptance decision. We'll branch into accept and
   > decline, then for each branch identify what happens next."

2. **Build the structure first.** Sketch the nodes and branches
   without numbers. The shape matters; the numbers come after.

   ```
   Offer decision
   ├── Accept
   │   ├── Stays > 2 years
   │   └── Leaves < 2 years
   └── Decline
       ├── Current role improves
       └── Current role stagnates
   ```

3. **Add probabilities to each branch.** The user assigns. The
   probabilities at any node should sum to 1.

4. **Add values to terminal outcomes.** The user assigns. Values
   may be quantitative (expected income, hours saved) or
   qualitative ranks ("good" / "bad" / "very good") that get
   converted later.

5. **Calculate expected values.** For each path: probability ×
   value, summed across terminal nodes. The path with the highest
   expected value is the analytic answer.

6. **Compare to gut.** As with scoring rubrics, the load-bearing
   step.

   > "The tree says accepting has the higher expected value. Does
   > that match your gut, or does it feel off?"

7. **Handle mismatch.** If gut and tree disagree, the
   probabilities, values, or branch structure are wrong. Walk back
   and surface which. Often the gut knows a node the user did not
   draw.

## Completion criteria

The tree is structurally complete (all branches end in terminal
outcomes), quantitatively analyzed (probabilities and values
assigned, expected values computed), AND the user has compared the
result against gut intuition AND any discrepancies have been
examined.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Expected Value Decision Tree (offer acceptance)
Frame: 0
Step: 5.2 (decision tool) / 5.3 (validate)
Started: 2026-05-14T17:00:00
Completed: 2026-05-14T17:40:00

Tree structure:
- Offer decision (root)
  - Accept (P = 1.0 at this node)
    - Stays > 2 years (P = 0.7, V = +120k income, +autonomy)
    - Leaves < 2 years (P = 0.3, V = +30k income, -reputation cost)
  - Decline (P = 1.0 at this node)
    - Current role improves (P = 0.4, V = +stability, +0)
    - Current role stagnates (P = 0.6, V = +0, -opportunity cost)

Expected values (qualitative):
- Accept: 0.7 × (high positive) + 0.3 × (low positive, some cost) = moderately high
- Decline: 0.4 × (stable) + 0.6 × (status quo with opportunity cost) = neutral-to-low

Result: Accept has the higher expected value.

Gut check:
- User's gut: "Accepting feels right but I keep stalling."
- Tree: Accept clearly favored.
- Mismatch type: Not value-disagreement; behavioral stall. The tree
  surfaced that the decision is already made — the user is
  experiencing pre-commitment friction, not analytic uncertainty.
```

## Common variations

- **Expected Value Decision Tree** — quantitative; probabilities
  and dollar values at each leaf.
- **Settlement Decision Tree** — used in legal contexts to
  compare litigation vs. settlement; outcomes are dollar values
  with probability ranges.
- **Issue Trees** — structural only; no probabilities or values;
  used in consulting frameworks to decompose a problem rather than
  to choose. Different output than expected-value trees; same
  shape.
- **Probabilistic decision trees with sensitivity analysis** —
  add sliders to probabilities and see how the answer shifts;
  useful when probabilities are contested.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| The tree gets too deep | 5+ layers loses signal. Collapse the bottom layers into "things go well" / "things go poorly" or similar. Detail at the leaves is rarely informative. |
| Probabilities feel made up | They are, in the sense that they're the user's calibrated guesses. Surface that explicitly: "These are your best-guess probabilities — they don't have to be precise. The question is whether the rough ordering changes if you nudge them." |
| Values are all hard to compare | The unit of value is unclear. Stop and ask: "What's the dimension you'd be tracking if you were grading the outcomes a year from now?" The unit usually surfaces. |
| User wants to add chance nodes (uncertainty) mid-build | Honor it; chance nodes belong in decision trees. The distinction between decision nodes (user choice) and chance nodes (probability) is structural. |
| The tree confirms what the user wanted | Same hazard as scoring rubrics — confirmation theater. Surface: "If you'd weighted [terminal outcome] one notch lower, the result flips. Does that change anything?" |
| Tree completes but no gut-check happens | Treat the tree as incomplete. The arithmetic is a means; the gut-check is the work. |
| The decision is irreducibly uncertain | Decision trees collapse when probabilities are pure unknowns. Switch to Pre-Mortem or scenario planning; the decision needs a different shape. |

## Example tools (from the library)

- **Expected Value Decision Trees** — quantitative tree with
  probabilities and value estimates. The canonical application for
  business and personal-finance decisions.
- **Settlement Decision Tree** — used in legal-strategic decisions
  to compare expected value of settlement vs. litigation. Same
  pattern; specialized output.
- **Issue Tree** — structural decomposition tool (consulting-style);
  no probabilities or values at the leaves. Use when the question
  is "what are the parts of this problem" rather than "which path
  has the highest expected value."

## When NOT to use a Decision Tree

- The decision is reversible and quick to recover from. Trees are
  ceremony; reserve them for decisions with meaningful asymmetry
  between paths.
- Probabilities cannot be estimated even roughly. A tree with
  uncalibrated probabilities is a decoration, not a decision aid.
- The user is in emotional regulation work. Trees are cognitive;
  switch to Therapist persona and revisit when the analytic frame
  re-opens.
- The decision is a values question, not a probabilistic question.
  Trees model outcomes, not what the user wants outcomes to mean.
  Switch to Counselor persona and surface the values; revisit the
  tree if the question reframes as analytic.
- The decision is many small calls in a row rather than one
  branching choice. Use Sequenced Workflow instead.
