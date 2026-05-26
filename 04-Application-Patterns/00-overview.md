---
doc_type: application_pattern
doc_purpose: overview
audience: ai
read_order: 0
last_updated: 2026-05-14
---

# Application Patterns — Overview

How you apply a thinking tool to a user's situation depends on the tool's
`tt_Form` (or `tt_Type=stance`). This folder contains one pattern file per
form value.

## When to load a pattern

The diagnostic loop (`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`
step 9) chooses a tool. Before introducing the tool to the user, **load
the relevant pattern**:

```bash
# Look up the tool's tt_Form
grep "^tt_Form:" "{ROOT}/01-Tools/Tool Entries/{Tool Title}.md"

# Load the matching pattern
cat "{ROOT}/04-Application-Patterns/pattern-{form-slug}.md"
```

Where `{form-slug}` is the lowercased form value with `/` replaced by `-`
and spaces replaced by `-`. Example: `tt_Form: Sequenced workflow` →
`pattern-sequenced-workflow.md`.

## The 16 tt_Form values (and MVP coverage)

|         tt_Form          |       Pattern file       |  Status |
|--------------------------|--------------------------|---------|
| Matrix                   | pattern-matrix.md            | MVP     |
| Sequenced workflow       | pattern-sequenced-workflow.md| MVP     |
| Question bank            | pattern-question-bank.md     | MVP     |
| Dialogue protocol        | pattern-dialogue-protocol.md | MVP     |
| Mental model             | pattern-mental-model.md      | MVP     |
| Checklist                | pattern-checklist.md         | Phase 2 |
| Scoring rubric           | pattern-scoring-rubric.md    | Shipped |
| Visualization technique  | pattern-visualization-technique.md | Shipped |
| Canvas                   | pattern-canvas.md            | Shipped |
| Decision tree            | pattern-decision-tree.md     | Shipped |
| Narrative template       | pattern-narrative-template.md| Shipped |
| Heuristic                | pattern-heuristic.md         | Shipped |
| Algorithm                | pattern-algorithm.md         | Shipped |
| Mnemonic                 | pattern-mnemonic.md          | Shipped |
| Game / simulation        | pattern-game-simulation.md   | Shipped |
| Practice / ritual        | pattern-practice-ritual.md   | Shipped |

Plus one pattern for `tt_Type: stance` tools (no Form):
- `pattern-stance-embodied.md` (Shipped)

**Status:** All 16 form patterns plus the stance pattern are now
shipped. The pattern library is complete; chapter 04 §4.3's
tool-naming requirement is unconstrained — every `tt_Form` /
`tt_Type` value in the 677-tool library has a matching application
pattern.

## Pattern file structure

Each pattern file has:

1. **What this Form is** — definition + schema reference
2. **Setup** — how to introduce the tool to the user (consent move)
3. **Engagement** — the main loop: what to ask, what to fill, what to do
4. **Completion criteria** — when the tool is "done"
5. **Output capture** — what to write to the Case File
6. **Common failure modes** — what goes wrong; recovery moves
7. **Example tools** — three or more tools from the library that use
   this pattern, with brief notes on what each demands of the pattern

## Tool composition

Some sessions use multiple tools in sequence. The patterns describe
how to apply *one tool*. Composition logic — when to chain Tool A into
Tool B, when to run two tools in parallel for comparison — lives in
`{ROOT}/00-Instructions/05-tool-application-patterns.md` (Phase 2).

Brief composition heuristics for MVP:

- **Output of A feeds B.** Five Whys (root causes) → Eisenhower Matrix
  (sort root causes by urgency/importance).
- **Iterative.** Apply, learn, apply again with refined inputs.
- **Second opinion.** Apply two tools to the same question; compare
  conclusions.

## Phase 2 expansion (now complete)

Phase 2 shipped all remaining form patterns. Pattern coverage is
now complete for every `tt_Form` value and the `tt_Type: stance`
value in the 677-tool library.

The Checklist pattern remains the one exception — `tt_Form: Checklist`
tools currently fall back to `pattern-sequenced-workflow.md`, which
covers their structure cleanly. A dedicated `pattern-checklist.md`
may be added in a later sprint if the sequenced-workflow fallback
proves insufficient in practice.

## Voice consistency across patterns

All patterns share the same voice rules from the Operating Manual:

- Get consent before introducing the tool.
- Ask one question at a time.
- Quote-level accuracy when reflecting user content.
- Update the Case File during and after the tool's run.
- Watch for stakes signals throughout (chapter 09 supersedes any tool
  application).
