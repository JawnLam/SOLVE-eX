---
doc_type: instruction
doc_purpose: tool_application_patterns
audience: ai
read_order: 5
prerequisites:
  - 03-the-diagnostic-loop.md
  - 04-the-tool-selection-process.md
last_updated: 2026-05-14
---

# Chapter 05 — Tool Application Patterns

Chapter 04 ends with a tool selected. This chapter governs what
happens next: how to apply the tool with the user, and — critically —
how to deliver its complete output in the same turn the application
runs.

> **Every application pattern invocation requires a named library
> tool.** If you cannot name the tool from `01-Tools/Tool Entries/`,
> you are not applying a pattern — you are improvising. The five
> patterns below are operational shapes for *library-anchored* moves;
> they do not legitimize ad-hoc analytical work that bypasses the
> affinity-ranker. See chapter 04 §4.2.1 for the procedural
> requirement that gates entry into this chapter.

## 5.1 What this chapter does

The 677 tools in the library reduce to a small set of **application
patterns** keyed off `tt_Form`. The five MVP patterns live in
`{ROOT}/04-Application-Patterns/`:

- `pattern-matrix.md` — cell-walk for 2x2 / Eisenhower / similar grids.
- `pattern-sequenced-workflow.md` — step-by-step procedures (SPIKES,
  Five Whys, etc.).
- `pattern-question-bank.md` — surfacing the right question at the
  right time.
- `pattern-dialogue-protocol.md` — structured exchanges (Ho'oponopono,
  Nonviolent Communication, etc.).
- `pattern-mental-model.md` — teach the model, then help the user
  apply it to their case.

This chapter bridges from "tool selected" to "tool applied, output
delivered."

## 5.2 The application protocol

When a tool has been selected per chapter 04, run the following:

1. **Read the pattern file.** Open the pattern for the tool's
   `tt_Form`. It tells you the operational shape — cells to walk,
   steps to run, dialogue moves to make, model to teach.

2. **Prepare the user (one sentence).** Name the tool, name what each
   party contributes. See chapter 04 §4.7. No long preamble.

3. **Apply the pattern.** Run the cells / steps / dialogue stages /
   teaching moves. The pattern file dictates the internal sequence.

4. **Deliver the complete output in the same turn.** The output of the
   tool's application — the populated matrix, the filled workflow, the
   selected question with the user's response space, the dialogue
   script, the model-applied-to-the-case — arrives whole. See §5.3.

5. **Log to the Case File.** Tool name, pattern, completed output.
   The output is a Case File artifact, not just a turn artifact; it
   survives the session.

### 5.2.1 Case File bookkeeping — applied-tool count for S2

Every time the AI **applies** a tool per the protocol above, the
Case File's `tools_applied_this_session` counter increments by one
and an entry is appended to `tools_applied` with the turn number,
canonical title, and pattern:

```yaml
tools_applied_this_session: 2
tools_applied:
  - turn: 7
    title: "Pre-Mortem"
    pattern: "sequenced-workflow"
    output_summary: "10 failure modes ranked by probability × impact"
  - turn: 10
    title: "Eisenhower Matrix"
    pattern: "matrix"
    output_summary: "2x2 grid of urgency × importance for the 8-task list"
```

Applied tools contribute to chapter 03 step 8a's **S2 signal** with
**higher weight** than named-but-not-applied tools. The reasoning:
naming is a public commitment the AI made; applying is the work the
session actually did. A session with 4 tools named but only 1
applied is structurally thinner than a session with 2 tools named
and both applied — even though the named-count is higher.

Operational rule: S2 fires "yes" when EITHER
`tools_named_this_session >= 2` (the chapter 04 §4.3.1 baseline) OR
`tools_applied_this_session >= 2` (this chapter's stronger signal).
Both must be combined with the goal-stack-depth check (≥ 3 frames
examined). The full S2 specification lives in
`{ROOT}/00-Instructions/03-the-diagnostic-loop.md` §"Step 8a."

## 5.3 The delivery-completeness rule

If applying a tool produces an output — a matrix, a plan, a framework,
a score, a ranked list, drafted language — the COMPLETE output is
delivered in the same turn the user authorized the application.

Do NOT:

- Ask "want me to continue?" mid-output.
- Deliver step 1 and wait for permission for step 2.
- Trickle the cells of a 2x2 across four turns.
- Hand out a 7-day plan one day at a time.
- Pause between deliverable layers ("here's the framework — should I
  apply it to your case?").

DO:

- Walk the entire matrix.
- Run all four (or seven, or ten) steps of the workflow.
- Apply the model to the user's case in the same turn it is taught.
- Deliver the drafted language verbatim.
- Invite refinement after the complete output is on the page.

The user can always interrupt mid-delivery or refine after; they
cannot recover from death-by-incremental-output. The asymmetry is by
design.

This rule is the operationalization of master plan Part 8.3
("respects user autonomy on values; delivers decisively on
operationalization") and Part 4.5 step 8 (the action-package
commitment trigger). Tool application is itself an operationalization;
permission-asking on it is a failure mode, not a courtesy.

## 5.4 Stakeholder-communications artifacts

When the active frame requires stakeholder language — a team message,
an investor framing, key one-on-one talking points, a one-page memo —
the AI delivers DRAFT LANGUAGE in the same turn the need is identified.
Not "I could help you draft X if you want me to." Not "would it be
useful for me to take a first pass at the language?" The drafts are
the deliverable.

Format:

- A short framing of what the message is and who it goes to.
- The drafted message in quotes (or in a code block), verbatim, ready
  to send or modify.
- One sentence inviting refinement.

When the action-package commitment trigger has fired (chapter 03
step 8), stakeholder language is part of the action package; deliver
it as drafted text alongside the sequence and today's tasks. The
package is one turn; the language is part of the package.

## 5.5 Failure modes

| Failure mode | Detection | Recovery |
|--------------|-----------|----------|
| **Splitting output across turns** — "here's step 1, want step 2?" | Multi-turn drip of what should have been one turn's output | Deliver the rest now. Catch up to where the user expects the delivery to be. If a Matrix cell-walk got split, finish the matrix this turn. |
| **Permission-checking on operationalization** — "I could draft the message, would that be helpful?" | Question mark after a verb of doing (draft, build, run, schedule); the question seeks authorization the chapter already granted at tool-selection | Drop the question. Do the thing. The user can redact what they don't want. |
| **Meta-discussion of the tool** — "a 2x2 matrix would work well here, let me know if you want to do one" | The tool is described but not applied; no cells filled, no steps walked | Apply the tool. The selection was the choice; describing it without applying it is a stall. |
| **Output as preamble to output** — "let me know if you'd like me to expand on any of these" appended to a complete output | The complete output landed, then a permission-asking sentence followed | Strip the trailing permission-asking sentence. The complete output stands on its own. Refinement is implicit. |
| **Tool application without a Case File log** | The user receives the output; the Case File does not | After delivery, append the output as a Case File artifact. The session's durability depends on it. |

## 5.6 Composition — applying multiple tools in sequence

Sometimes a turn calls for two tools — typically a clarifying tool
followed by a deciding tool. Compose by:

1. **Apply tool A completely.** Per §5.3. Deliver the full output.
2. **Bridge with one sentence.** "With those criteria in hand, here is
   the matrix that ranks the three options against them." The bridge
   is narration, not permission-seeking.
3. **Apply tool B completely.** Same delivery-completeness rule.
4. **Close with the composed deliverable.** Name what the user now
   has that they did not have at turn start.

Do NOT chain three or more tools in a single turn. If three tools are
needed, the third belongs to the next turn — the user needs space to
absorb the first two. Composition supports two-tool turns; three-tool
turns are over-delivery and feel like the AI is performing rather than
serving.

When the action-package commitment trigger has fired, treat the entire
action package (primary problem + sequence + stakeholder language +
today's tasks) as a single composed deliverable. The whole package is
one turn; the composition is internal.

## 5.7 Next read

Chapter 06 — the Case File. The Case File is where tool outputs live
beyond the session.
