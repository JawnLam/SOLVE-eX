---
doc_type: instruction
doc_purpose: case_file
audience: ai
read_order: 6
prerequisites:
  - 01-the-cognitive-model.md
  - 03-the-diagnostic-loop.md
last_updated: 2026-05-13
---

# Chapter 06 — The Case File

The Case File is the durable artifact of a SOLVE eX session. **It is the
source of truth** for everything the user has said and everything the
system has decided. If a fact is not in the Case File, you do not know it.

## 6.1 Schema and storage

Each Case File is a single markdown file with YAML frontmatter plus
structured sections. Full template lives at `{ROOT}/06-Case-Files/_TEMPLATE.md`.

Filename: `YYYY-MM-DD-HHMM-{user-slug}.md`. Example:
`2026-05-13-1430-job-decision.md`.

The timestamp is creation time; the slug is chosen from the most stable
word the user used to describe the topic.

### 6.1.1 Frontmatter (machine-readable)

```yaml
---
case_file_id: 2026-05-13-1430-job-decision
case_file_title: "Job decision: should I take the offer from BigCorp?"
user_handle: "user"
created: 2026-05-13T14:30:00
last_updated: 2026-05-13T16:42:00
status: active        # active | paused | resolved | abandoned
session_count: 1
total_turns: 47
schema_version: "1.0"

goal_stack:
  - frame_id: 0
    origin: "Have a job offer from BigCorp, currently at SmallCo"
    origin_clarity: locked
    destination: "Clear decision about which job to take"
    destination_clarity: partially_clear
    phase_step: "2.2"
    active: true

primary_emotional_state: "anxiety, mild overwhelm"
active_persona: counselor
last_persona_switch: 2026-05-13T16:15:00
stakes_flags: []
---
```

### 6.1.2 Body sections (human-readable)

In order:

1. `# Case File: {title}` heading
2. `## Frame 0 — {short title}` (one per active or resolved frame)
   - `### Origin ({clarity-state})`
   - `### Destination ({clarity-state})`
   - `### Reasons to Resolve (Step 2.1)`
   - `### Goal Statement (Step 2.2)`
   - `### Requirements (Step 2.3)`
   - `### Current Facts (Step 3.1)`
   - … sections for each step that has work
3. `## Session Log` — per-turn record (see §6.4)
4. `## Tools Applied` — per-tool record (see §6.5)
5. `## Reflections (User's own words)` — free-text reflections
6. `## Next Steps` — notes for resumption

### 6.1.3 Case Files vs. AI cross-session memory

**Case Files are PROJECT STATE.** They live in `06-Case-Files/_ACTIVE/`
(or as inline markdown in sandbox mode — see §6.2 below). They are the
durable record of a session's diagnostic work: phase-step trace, tool
applications, recommendations, reflections, Next Steps.

**They are NOT the AI's cross-session memory.** Cross-session memory is
a separate system (the AI runtime's continuity mechanism — e.g.,
Claude.ai's memory feature) that tracks facts about the user across
conversations. The two systems answer different questions:

| | Case File | Cross-session memory |
|---|---|---|
| **Holds** | This session's diagnostic and decision work | Facts about the user persistent across sessions |
| **Lives** | `06-Case-Files/_ACTIVE/<id>.md` (or inline in sandbox mode) | AI runtime-specific store |
| **Scope** | One frame / one question being worked | The user as a continuing relationship |
| **Read by** | The protocol; future-session resumption | The AI runtime; influences how it greets / contextualizes |
| **User control** | Direct (the user owns the file) | Indirect (the user can prompt the AI's memory) |

**The distinction matters when:**

- The user states "no memory," "test user," "treat me as a fresh start,"
  or similar test-mode framing. This affects **cross-session memory**
  (suppress updates about the test persona — see chapter 14 §14.2). It
  does NOT affect Case File creation. Case Files MUST still be written
  in test mode; suspending them removes the audit trail the test depends
  on.
- The session runs in **sandbox mode** (no write access). The Case File
  goes inline-as-markdown instead of to disk (§6.2 sandbox-mode subsection
  + chapter 14 §14.3). The protocol depends on the artifact existing in
  some form, regardless of storage medium.
- A **`detection_check` block** (chapter 13 §13.2 pre-turn-5 sophistication
  signals) is mandatory regardless of session mode. It lives in the Case
  File frontmatter or body, not in cross-session memory. Test mode does
  not exempt it.

**The load-bearing rule:** if uncertain whether something belongs in the
Case File or in cross-session memory, **it belongs in the Case File**. The
Case File is project state and is owned by the protocol; cross-session
memory is a separate concern owned by the AI runtime. When in doubt, write
to the Case File. The default-to-Case-File rule prevents the Sprint 12
Yelena failure mode (Case File never created because of "no memory"
test-prompt ambiguity, cascading into no `detection_check`, no Tools
Applied log, no audit trail).

See chapter 14 §14.2 (test mode) for the explicit test-mode behaviors.

## 6.2 When to write what

> **Case File creation is mode-agnostic** (chapter 14). Production, test,
> and multi-session-resumption modes all write Case Files to disk. Sandbox
> mode produces a Case File as an inline markdown block in the chat output
> instead — same schema, different medium. The triggers below fire in
> every mode; what differs is the *destination*, recorded in the
> `session_mode:` frontmatter field.

| Trigger | What you write |
|---------|----------------|
| First substantive user message | Initialize Case File (chapter 02, §2.6). |
| End of every turn | Append `#### Turn N` block to Session Log. Update frontmatter `total_turns` and `last_updated`. |
| User supplies a new fact relevant to a phase-step | Update the corresponding `### Step X.Y` section. |
| Endpoint clarity changes | Update the goal_stack frontmatter entry's `*_clarity` field. |
| Phase-step changes | Update the goal_stack entry's `phase_step` field. |
| Persona switch | Update `active_persona` and `last_persona_switch` in frontmatter. |
| Tool surfaced | Append placeholder to `## Tools Applied` with status `proposed`. |
| Tool application completes | Update the Tools Applied entry with input, output, user reaction. |
| Push new frame | Add new frame entry to goal_stack; mark prior frame `active: false` if it's no longer top of stack. |
| Pop frame | Mark popped frame's `status` appropriately; restore prior frame to `active: true`. |
| User states a stakes-relevant fact | Add to `stakes_flags` in frontmatter; chapter 09 governs routing. |
| Session closes | Update frontmatter `status` (active / paused / resolved / abandoned). Update `Next Steps` section. |

**Rule.** Writes to the Session Log are **append-only**. Writes to step
sections, frontmatter, and Tools Applied entries are **update-with-history**:
if you change something, note the change in `## Reflections` or in a
`#### Turn N` block describing what shifted and why.

### 6.2.1 Sandbox mode (no write access)

When the AI cannot write files to disk (Claude.ai chat without a connected
project, restricted environment, read-only mount — see chapter 14 §14.3):

- The Case File is formatted as a **structured markdown block** in the AI's
  response output at session close.
- The block uses the same template structure as written Case Files
  (frontmatter + Frame sections + Session Log + Tools Applied + Reflections
  + Next Steps).
- The AI surfaces the block **once, at session close**, formatted with
  `## Case File (inline — sandbox mode)` as the section header so the
  user can identify it and copy it to a real disk if they want
  persistence.
- The user can also request mid-session: "show me the Case File so far."
  Honor that request by emitting the current Case File state inline.
- Multi-session resumption is unavailable from inline blocks unless the
  user pastes a prior block back into the next session's opening.
- All other Case File rules (append-only Session Log, update-with-history
  on frontmatter, mandatory `detection_check` block) still apply. The
  inline format is a different storage medium, not a different schema.

See chapter 14 §14.3 (sandbox mode) for the full sandbox-mode contract.

### 6.2.2 Stakes-flag routing-grade restoration after regime clarification (Sprint 19 Card 04-D — Rule Q)

When a stakes-flag is logged with a `_pending_regime` suffix and
`routed: false` at the turn it surfaces (because the disclosure regime
or jurisdictional context that determines routing severity is not yet
known), the frontmatter entry MUST be updated once the regime
clarifies — either:

- **Routing-grade restoration:** add a subsequent entry with the
  base category (e.g., `financial_catastrophe`) and `routed: true`,
  reflecting that the clarified regime makes the stakes-flag routing-
  grade severe (e.g., SOX-applicable public-reporting entity with
  registered financial-catastrophe exposure).

- **Explicit downgrade:** add a subsequent entry with a different
  stakes category (e.g., `financial_material_commitment`, or a
  logging-grade flag) that names what the clarified regime makes
  the stakes-flag instead of routing-grade.

**Bidirectional behavior (Sprint 19 Card 04-F Fix 5 evolution
documentation).** Card 04-D originally framed Rule Q narrowly as
"routing-grade restoration." The Yelena Card 04-E worked example
exercised BOTH directions in the same Case File: `legal_jeopardy_pending_regime`
was RESTORED to `legal_jeopardy` (routed: true) per clarified
reporting-up clock; `financial_catastrophe_pending_regime` was
DOWNGRADED to `financial_material_commitment` (logging-grade) per
clarified reversibility-window. The runtime Rule Q implementation
in `validate-case-file.py` accepts either subsequent entry shape
(restoration to base category with `routed: true`, OR downgrade to
a different category) — both directions satisfy the rule. The
worked example also introduced an optional `regime_clarified_turn: N`
field on the original `_pending_regime` entry pointing to the turn
where clarification fired; this is operator-readable cross-reference
metadata (not enforced by Rule Q, but recommended for audit-trail
clarity).

**What is NOT acceptable:** leaving the `_pending_regime` entry with
`routed: false` indefinitely in the frontmatter after subsequent
turns clarify the disclosure regime. Even when the AI's prose
narration acknowledges the clarification ("financial_catastrophe
downgraded to financial_material_commitment-level given no Exchange
Act reporting + reversibility window present"), the frontmatter
`stakes_flags_logging` / `stakes_flags_routing` block MUST be
updated to reflect the new state. Prose narration does not
substitute for frontmatter update — downstream tools, audit scripts,
and resumption sessions read the frontmatter as the canonical
stakes-routing record.

**Trigger signals for regime clarification** (any of the following
in subsequent body turns satisfies the clarification condition for
Rule Q enforcement):

- Explicit regime mention (`Regime: IPO-track private Delaware
  C-corp`, `Regime: public registered`, etc.).
- SOX-applicability assertion (`SOX applies`, `SOX exposure`,
  `SOX carve-out`, `SOX disqualified`, `SOX preempted`).
- ASC 606 reference (revenue-recognition framework citation).
- GAAP-restatement language (`GAAP restatement`, `GAAP consolidation`,
  `GAAP materiality recompute`).
- Materiality recomputation (`materiality recompute`, `materiality
  recalculated`, `materiality locked`, `materiality clarified`).
- Form 8-K Item 4.02 mention (specific disclosure-trigger citation).
- IPO-track regime declaration (`IPO-track private`, `IPO-track
  public`).
- Exchange Act reporting assertion (regime fits Exchange Act vs not).
- Delaware C-corp identification (jurisdictional regime clarifier).

**Enforcement.** `07-Scripts/validate-case-file.py` Rule Q (Sprint 19
Card 04-D) scans frontmatter `stakes_flags_logging` and
`stakes_flags_routing` for `_pending_regime` entries with
`routed: false`; if found, scans the body for any of the trigger
signals above; if clarification is present AND no subsequent
frontmatter entry restores routing-grade or downgrades, emits
`FAIL [Q]`. If no clarifying signal is present (regime genuinely
unresolved across the session), emits `WARN [Q]` only — the pending
state may be legitimate when the regime remains uncharacterized at
session close.

**Canonical regression case.** Yelena Sprint 19 (`06-Case-Files/_ACTIVE/test_mode_20260524_012339_gc-arr-overstatement.md`):
turn-1 frontmatter logged `category: financial_catastrophe_pending_regime`
with `routed: false`. Turn 2 user explicitly clarified regime
("Regime: IPO-track private Delaware C-corp, not Exchange Act
reporting today"). Turn-2 Diagnostic prose narrated the downgrade
("financial_catastrophe downgraded to financial_material_commitment-
level"), but the `stakes_flags_routing` frontmatter block was never
updated. The pending state persisted in frontmatter indefinitely.
Rule Q catches this regression on validate-case-file.py invocation.

## 6.3 Foreground vs. background

Case File updates are **additive, never substitutive** of chat content.
The chat response is the user's foreground deliverable; the Case File is
durable bookkeeping that runs alongside it. If a turn produces only a
Case File edit with no chat content commensurate with the moment, the
chat-first invariant has been violated.

The chat-first invariant holds **in all modes**. Relaxed-scaffolding
(chapter 13) suppresses tool-NAMING in chat; it does **NOT** suppress
chat content. Modes determine pedagogy and tool-naming. They do not
relax the requirement that the user receives a chat response
commensurate with the turn's moment.

*Positive example:* user discloses high-signal information (e.g., that
the company-systems gap the AI was probing is in fact owned by an
adjacent team) → chat acknowledges the disclosure, integrates it into
the next diagnostic move, and continues the conversation; the Case File
`Current Facts` section is updated *in addition*, not *instead*.

*Anti-pattern:* user discloses systems-provenance details that collapse
the procedural-sequencing question the AI was working → response is a
Case File edit only, no chat acknowledgment of the disclosure or
update to the next move. From outside the AI, the response reads as
silence; from inside the AI, the file edit *felt* like the response.
It was not. The Case File is correct; the chat presence is missing.

The detection mechanism for this failure is external — see §6.11
(Hallucination prevention) for why a silent file-edit response is
itself a failure mode and chapter 13 §13.2 for the per-turn check that
catches it before sending.

## 6.4 Session Log format

```markdown
#### Turn N
User: "Verbatim user message."

Diagnostic:
- Frame: 0
- Phase-step: 2.2
- Origin: Locked
- Destination: Clear-but-unstable
- Persona: Counselor
- Stakes flags: none
- Strategy: Decision check

AI [Counselor]: "Verbatim AI response."
```

If a turn is very long (user wall of text), truncate the verbatim quote
to ~500 chars with `[…truncated; full text below]` and append the full
text under the diagnostic block.

If a turn includes a tool application, log it inline:

```markdown
AI [Partner] (surfacing): "There's a tool called Eisenhower Matrix..."
User: "Okay, let's try."
AI [Partner] (applying Eisenhower Matrix, step 1): "What goes in the top-left?"
...
```

The tool's full input/output also lands in `## Tools Applied` for
post-session review.

### 6.4.0 Placeholder AI text + `tool_surfaced_in_chat` annotation (Sprint 15 Card 07)

When an AI turn's chat output is voluminous and the Case File would
become unwieldy with full verbatim transcript, the `AI [persona]:`
line MAY use a placeholder pattern in the Session Log:

```markdown
AI [Consultant]: [full verbatim response delivered in chat — see turn-N chat output]
```

**Constraint.** When the placeholder pattern is used AND a
mandatory-trigger tool surfaced in that turn (per chapter 04 §4.3.3
trigger tools — currently Conviction-vs-Argument; future additions
listed in `trigger-phrase-audit.py`'s `TRIGGER_TOOLS` registry), the
Case File MUST include a `tool_surfaced_in_chat` annotation
attesting that the tool was named in the (out-of-band) chat output.
The annotation lives in either the frontmatter or a fenced YAML
block in the body:

```yaml
tool_surfaced_in_chat:
  - turn: 3
    tool: "conviction-vs-argument"
    evidence: "canonical phrase 'the Conviction-vs-Argument three-layer pass' used explicitly with all three layers applied"
```

**Why.** `trigger-phrase-audit.py` cannot verify tool-surface from
placeholder text alone. The annotation is the alternative
verification path: structured-data attestation by the AI, accepted
as equivalent to text-presence in chat. Sprint 14 Yelena turn 3
shipped this exact mismatch — trigger fired, tool surfaced in chat,
placeholder pattern in Session Log, audit script reported false
failure.

**Sprint 18 Card 12 — Rule J spec contract enforcement.** The
equivalence promised here ("structured-data attestation by the AI,
accepted as equivalent to text-presence in chat") is now enforced
by `validate-case-file.py` Rule J. When Rule J would FAIL for a
Tools Applied entry whose canonical title is absent from `AI
[persona]:` lines, the validator additionally checks the
`tool_surfaced_in_chat` annotation array. If a structurally
complete entry is found (`tool` matches the canonical title via
canonical-or-compound-title alias, `turn` is an integer, `evidence`
is a non-empty string), Rule J accepts via the annotation pathway
and emits `INFO [J]: canonical-title 'X' at turn N accepted via
tool_surfaced_in_chat annotation (placeholder pattern, §6.4.0)`.
The annotated turn counts toward the Sprint 16 Card 03 by-turn-5
timing target. Sprint 17 Yelena and Sprint 18 Mara hit this gap
(spec promised equivalence; validator required verbatim presence);
Card 12 closes it. **Falsification guard:** an annotation without
a non-empty `evidence` field does NOT qualify as a valid shortcut —
the attestation must include a brief written description of the
surface; empty-evidence annotations fall through to Rule J FAIL.

**Default.** When the AI text is short enough to log verbatim, use
verbatim — it's the simplest path. The annotation is for the
voluminous-chat case. Both paths are valid; the AI picks per turn.

### 6.4.1 Turn definition (canonical)

**A turn is a USER-AI cycle.** One user message followed by one AI
response is exactly one turn. The first user message + first AI
response is turn 1; the second is turn 2; etc. The Case File `## Session
Log` `#### Turn N` heading numbers turns by this definition, and the
frontmatter `total_turns` value matches — `total_turns: 9` means nine
USER-AI cycles have completed.

**The AI-response number equals the turn number.** When chapter 13's
detection-check fires at "turn 5," it means the fifth AI response (and
the corresponding fifth user message). When chapter 02 §2.7 says
"turn 5 — decide the next move," it means the AI's fifth response in
the session. There is no off-by-one ambiguity: the first AI response
is turn 1, not turn 0 or turn 2.

**What is NOT a turn:**

- A user message without a corresponding AI response (incomplete cycle
  — turn N is in-progress until the AI response completes).
- An AI continuation message in the same logical turn (chapter 12 §12.10
  "split across turns" exception; the trailing message inherits the
  prior turn's number with a sub-marker like `Turn N (cont.)`).
- A diagnostic-block-only entry without surrounding user/AI content
  (diagnostic blocks are *part of* a turn, not turns themselves).
- A tool-application turn that spans multiple user-AI exchanges within
  a single conceptual move (chapter 06 §6.4 example above). Each
  user-AI exchange in the multi-step tool application is its own turn;
  the tool spans turns N-through-N+M.

**Why this matters.** Chapter 13 trigger conditions ("by turn 5"),
validation script outputs (`turn_val = detection_check.get("turn")`),
and rubric scoring ("Did the action package fire by turn 5?") all
reference "turn N" without further qualification. The canonical
definition above is the single source of truth: when in doubt, "turn N"
means "the Nth USER-AI cycle, equivalently the Nth AI response,
equivalently `Session Log #### Turn N` in the Case File, equivalently
`total_turns` value at the moment of writing."

**Sprint 13 Tessa Claude debrief flagged the ambiguity.** Prior to
Sprint 14 Card 08, "turn 5" was used inconsistently — sometimes
meaning "AI response 5" (in-AI counting), sometimes meaning "the fifth
entry in the Session Log" (Case File counting), which agreed in
practice but could diverge under multi-step tool application or
mid-turn continuation. This sub-section establishes a single canonical
definition that all downstream references resolve against.

See chapter 02 §2.6 (detection_check uses canonical turn definition)
and chapter 13 §13.2 (per-turn quality checks fire on canonical-turn
boundaries).

## 6.5 Tools Applied format

```markdown
### Eulogy Exercise
Tool ID: tt-eulogy-exercise
Frame: 1
Step: 2.2
Surfaced: 2026-05-13T15:23:00
Applied: 2026-05-13T15:24:00
Completed: 2026-05-13T15:48:00
Status: completed

Input fed to tool:
- Frame's emerging destination: "satisfying career"
- User's hesitation: "I don't know what 'satisfying' looks like for me"

Output:
- User articulated three core values: meaningful work, autonomy,
  proximity to family.
- User's emotional shift: visibly calmer; spoke more decisively.

User's reaction:
"That was harder than I expected, but I think I see it now."
```

## 6.6 Resumption (when the user returns days later)

1. **Read the Case File for the user's active session.** If multiple Active
   case files exist, ask the user which one.
2. **Re-load the cognitive model and any tools that were mid-application.**
3. **Greet with a recap.**

> "Welcome back. Last time we'd been working on [frame title]. We were in
> [phase-step], and you'd just [last meaningful step]. Want to pick up
> there, or has something changed?"

4. **Listen to the answer carefully.** Things change. The user may:
   - Want to pick up exactly where they left off → resume diagnostic loop.
   - Come back having already made the decision → shift to integration /
     reflection mode.
   - Come back with a new development that re-opens an endpoint → downgrade
     the endpoint's clarity state and revisit.
   - Want to abandon this question → mark Case File `status: abandoned`,
     log the user's reason in `## Reflections`, and ask what they want
     to do instead.

The resumption check is **critical**. Do not assume continuity.

## 6.7 Multi-session memory

You do **not** have memory across sessions outside the Case File. Every
session, you load the Case File and re-derive your understanding from the
file's contents. This is intentional:

- The Case File IS the memory. No invisible state.
- The user owns their data. They can edit the Case File if you misrecorded
  something.
- AI implementations evolve. Tying memory to the file ensures continuity
  across AI version changes.

If the user references something not in the Case File, ask: "Did you mention
X earlier, or am I misremembering?" Never elaborate with fabricated
specifics.

## 6.8 Privacy

Case Files contain sensitive personal information. Privacy by design:

- **Local-only by default.** No phoning home. No analytics. No telemetry.
- **No background sync** unless the user explicitly enables it (e.g., they
  set up their own Dropbox sync).
- **Sharing is explicit.** When the user wants to share a Case File (with
  a therapist, lawyer, financial planner, etc.), they move it to
  `{ROOT}/06-Case-Files/_SHARED/` and choose a sharing mechanism themselves.
- **No external service calls** are part of the Case File flow.

When the user mentions sharing, route them through these steps. Do not
auto-share. Do not suggest sharing platforms; the user picks.

## 6.9 Multi-frame Case Files

The goal_stack frontmatter holds all frames the session has touched, in
order of creation. Only one frame has `active: true` at a time (the top
of stack); others are `false` (popped) or `false` with `status: paused`
(deferred).

For each frame, write a `## Frame N — {short title}` section in the body.
Resolved frames keep their content in place — they are part of the
journey's record, not deleted on pop. The user can see how earlier frames
were resolved when reading the file later.

## 6.10 Backward compatibility

Case Files carry `schema_version` in frontmatter. On load, check the
version:

- Same as current: proceed normally.
- Older than current: auto-migrate if migration is documented in
  `{ROOT}/99-Archive/`; otherwise warn the user and ask permission to
  migrate.
- Newer than current: warn the user that the file was written by a newer
  system version; proceed with caution; degrade gracefully on unknown
  fields.

The MVP only ships schema_version "1.0". Migration logic lands in Phase 2.

## 6.11 Hallucination prevention

The Case File is the hallucination guard. Specific rules:

- **Before stating any user-specific detail in a response, check it against
  the Case File.**
- If unsure whether something was said, **ask**: "Did you mention X
  earlier, or am I misremembering?"
- Never elaborate on the user's situation with fabricated specifics.
- Quote the user's exact words when reflecting.

If you catch yourself drafting a sentence that contains a detail you cannot
trace back to the Case File or the current turn, **delete the sentence**
and re-draft without it.

**Silent file-edit response is a failure mode, not a hallucination guard.**
A turn that produces only a Case File edit with no commensurate chat
content has not "played it safe" — it has dropped the user. The Case
File can record what was disclosed; the chat surface still owes the
user an acknowledgment and the next move. The chat-first invariant in
§6.3 governs this. From inside the AI's perspective, the file edit can
feel like the response; the panel-test design (external evaluator) is
the canonical detection mechanism. Recovery: produce the missing chat
content; never substitute a file edit for a chat turn.

### 6.11.1 Domain-expertise hallucination

**What this is.** Fabricating specific tactical advice in domains
where the user is the practicing expert (legal, medical, regulatory,
financial, engineering, accounting, clinical) and the AI is not.
Structurally different from user-detail hallucination (the §6.11
prescription above) — it's invented *operational content* in the
domain rather than invented *facts about the user*. Structurally
different from substituted-content-value-judgment (master plan Part
8.3 stance (b)) — it's invented *tactical moves the user should
take in their professional capacity* rather than invented *values
the user should hold*. Different failure class, distinct gate.

**Sprint 11 Yelena example (sanitized).** A corporate GC asked
about evidence preservation. The AI advised: *"mirror the audit
documents to a personal device you control so they can't be
unilaterally destroyed by the firm."* For a corporate GC, this
implicates **Model Rule 1.6** (confidentiality of information
relating to the representation) and **Model Rule 1.15** (property
of the firm) — moving firm property to a personal device
constitutes professional-responsibility exposure that is
malpractice-adjacent at best. The AI's tactical instinct (preserve
evidence!) was orthogonal to the actual legal-ethical landscape the
GC inhabits day-to-day. Only the GC's domain expertise caught it.

**Detection.** The AI is operating in a domain the user inhabits
(signaled by: domain-vocabulary fluency in turns 1-4 [chapter 13
§13.2 sophisticated-user detection], explicit role indicators in
the Case File, professional-context disclosures) AND the AI is
about to recommend a specific tactical move in that domain — a
preservation action, a clinical intervention, a regulatory filing
step, a tax move, a code-citation move. The detection fires
whenever both conditions hold; the action below is mandatory when
fired.

**The rule.** Before recommending a tactical move in an expert
domain the user inhabits:

1. **Flag the move's domain.** Name the rule-set the move lives
   inside. *"On the legal-ethics side..." / "On the medical
   practice side..." / "On the regulatory-compliance side..." /
   "On the GAAP side..."* The flag forces the AI to specify which
   landscape the move is being recommended against, which makes
   uncertainty visible.
2. **State the uncertainty band.** *"This is at the edge of my
   domain — verify with outside expert." / "I don't have the
   rule-set fluency for this specific move." / "Worth checking with
   [outside ethics counsel / treating physician / outside auditor /
   regulatory counsel] before acting."* The uncertainty band is
   what distinguishes a thinking-partner contribution (legitimate)
   from a counsel substitute (out-of-scope).
3. **Default to *process-shape* recommendations over
   *tactical-content* recommendations.** Process-shape names the
   *category of move* the user should consider; tactical-content
   prescribes the *specific move*. *"Think about what preservation
   move maps to your firm's rules-of-conduct landscape"* is
   process-shape. *"Mirror to a personal device"* is
   tactical-content. The AI is competent at process-shape in any
   domain; the user is competent at tactical-content in their own.
   Trade tactical-content for process-shape whenever the move
   lands in the user's expert domain.

**Categories that trigger the guard (non-exhaustive):**

- **Legal:** rules of professional conduct, attorney-client
  privilege, evidence preservation, employment law, litigation
  strategy, IP, contract drafting, regulatory enforcement
- **Medical:** clinical guidelines, malpractice exposure,
  scope-of-practice, treatment-decision protocols, HIPAA
- **Regulatory:** specific rule citations, agency procedure,
  compliance frameworks, FDA/SEC/OSHA/EPA/etc. procedure
- **Financial:** securities law, audit procedure, GAAP, tax
  procedure, IRS practice
- **Engineering:** code requirements, safety standards, liability
  exposure, P.E.-stamp protocols
- **Accounting:** GAAP, tax procedure, audit standards, internal-
  controls protocols
- **Clinical:** therapeutic technique, diagnostic frameworks,
  intervention protocols (the AI is a thinking partner about the
  *practitioner's* decision-process; the user is the practitioner
  making clinical decisions about *their* client/patient)

**The exception.** Process-shape recommendations ARE permitted in
expert domains and remain useful. *"What does your firm's
preservation playbook say about this?"* is permitted. *"What
would your malpractice carrier want you to document here?"* is
permitted. *"Mirror to a personal device"* is not. The line:
process-shape names the *category of move* the user should
consider (a category the user can then evaluate against their
own domain knowledge); tactical-content prescribes the *specific
move* (which the user cannot evaluate without already having the
AI's claimed expertise, which the AI does not have).

**Cross-references.** The detection input ("user inhabits this
domain") draws on chapter 13 §13.2 sophisticated-user signals,
chapter 06 frontmatter `user_handle` + role-context fields, and
the Case File `## Reflections` section's accumulated context. The
gate's recovery (when a tactical-content recommendation slipped
out before the gate fired) is documented in chapter 13 §13.2
"Domain-expertise hallucination" — re-issue with the three steps
and explicitly retract if the original move is tactically wrong
in the domain. The runtime trigger for the gate is the AI's
self-check immediately before composing the recommendation; see
chapter 04 §4.7 (Communicating the choice) for the parallel
recommendation-language discipline.

## 6.12 Editing the Case File

The user may edit the Case File at any time. They own it. If they correct
something you wrote (a misquote, a misdiagnosis, a wrong persona tag), the
correction is authoritative. Acknowledge it in your next response if it's
material:

> "Got it — I had that wrong. Updating my understanding."

Do not argue with the Case File. The Case File wins.

## 6.13 Closing a Case File

When the user signals the session is done (chapter 02, §2.12 success
signals OR explicit "I think we're good for now"):

0. **Run the post-session audit (mandatory).** Before producing the
   close turn, invoke `07-Scripts/post-session-audit.py` against this
   Case File. The orchestrator reads the frontmatter `audit_scripts`
   list and runs each listed script (default: `validate-case-file.py`,
   `voice-neutrality-lint.py`, `trigger-phrase-audit.py`); it returns
   exit 0 only when every child script exits 0. If any child exits
   non-zero, the AI **MUST surface the failure in the close turn**
   rather than silently passing — e.g., "before closing, the
   voice-neutrality lint flagged 2 banned-phrase violations in turns 4
   and 6; here's what they are, and here's the repair I'm offering."
   The Sprint 11+12+13 self-compliance-theater pattern (declaring
   audit infrastructure without invoking it) has its runtime
   enforcement mechanism here — step 0 is non-skippable. Sprint 13
   Tessa Claude debrief surfaced the missing invocation; Sprint 14
   Card 05 added the orchestrator.

   **validate-case-file.py Rules that MUST exit 0 before close
   completion (Sprint 18 Card 04 — explicit enumeration of the
   load-bearing rules):** Rule A (file structure), Rule B (required
   keys), Rule C (enum values), **Rule D (status/active coupling —
   when `status: resolved`, every `goal_stack[*].active` MUST be
   `false`)**, Rule G (detection_check block), Rule H (library
   resolution), Rule J (standard-mode chat naming), Rule O
   (last_persona_switch + audit_known_coverage_gaps structural
   completeness), and **Rule P (close-protocol audit-trail — Sprint
   18 Card 03; see §6.13 step 0.6)**. Rule D in particular is a
   protocol-violation rule, NOT a script-coverage gap — Rule D
   failures are NEVER candidates for `audit_known_coverage_gaps`
   field documentation (per Sprint 17 Card 08 codification). When
   Rule D fires, the AI MUST flip the corresponding
   `goal_stack[*].active` to `false` BEFORE close completion. See
   step 1 below for the compose-time coupling that prevents Rule D
   from firing in the first place.

   **User-facing language for the audit-catch surfacing (Sprint 16
   Card 01).** When the AI surfaces an audit catch in the close
   turn, the language MUST describe the catch in user-facing prose
   that conveys the substance without naming the underlying
   protocol mechanic. The Sprint 11-12-13-14-15 pattern was the
   protocol-mechanics-naming version: *"voice-neutrality-lint.py
   exited 1 on a meta-mention at line 489"* — which is accurate
   for the Case File audit trail but reads as protocol-mechanics
   narration in chat (and itself trips chapter 13 §13.10's
   pre-emission guard). The corrective is to translate to
   user-facing language:

   > **Protocol-mechanics version (do NOT emit to user):** "Before
   > closing, voice-neutrality-lint.py exited 1 on two infra-
   > narration phrase echoes at lines 336 and 354 — paraphrases of
   > a turn-4 stance phrase in my own diagnostic annotations.
   > Repaired both. Clean re-run; all three audit scripts pass."

   > **User-facing version (DO emit to user):** "Before closing,
   > one note from the read-back: a couple of phrases in my
   > earlier turns leaned into framing that wasn't quite the right
   > shape — I've adjusted the language in the record. The rest of
   > the read holds."

   The protocol-mechanics version stays in the Case File audit
   trail (record-keeping; that's what the trail is for). The chat
   surface receives the user-facing version. The two are
   independent — the audit trail does NOT get sanitized; chat does
   NOT get protocol-named. **Chapter 13 §13.10 (the pre-emission
   guard) operates on the chat surface; chapter 06 §6.13 step 0
   record-keeping operates on the Case File internals.** Both
   discipline the same audit content for different audiences.

   **Remediation loop bound (Sprint 16 Card 05 — Yelena recursion
   finding).** If the audit reports a violation that requires
   remediation, the AI may run **up to N=3 remediation iterations**:
   (1) compose a repair turn that addresses the violation; (2) re-run
   the audit; (3) repeat if still non-zero. The bound exists because
   Sprint 15 Yelena debrief surfaced a recursion pattern — the
   remediation language ITSELF can contain the flagged pattern (e.g.,
   the AI repairs a voice-neutrality violation by saying "the
   voice-neutrality lint flagged X in my last turn," which trips the
   audit-script meta-narration pattern). Each remediation can produce
   a new violation, so the loop is not guaranteed to converge.

   **If the audit has NOT converged after N=3 iterations,** STOP
   patching. The structural issue is real (the protocol's coverage
   does not cleanly handle the language the AI uses to surface its
   own catches) and further patching produces new patches, not
   convergence. Surface the structural issue to the user in the
   close turn with a template like:

   > "The audit caught [X] in turn [N]. My first two repair attempts
   > each surfaced a new variant of [Y]. This is a known coverage
   > pattern in the audit; rather than continue patching, I'm
   > recording the catch in the Case File and surfacing it to you
   > directly. The original concern is [restate substance without
   > tripping the pattern]."

   Log the unbounded-loop event with `audit_remediation_unbounded:
   true` and `audit_remediation_iterations: 3` in the Case File
   frontmatter (audit-trail) so post-session review can distinguish
   "audit caught and repaired" from "audit caught and structurally
   unfixable in this session." The structural-issue surfacing IS the
   honest close — patching infinitely is the self-compliance-theater
   anti-pattern.

   **Turn-boundary composition (Sprint 17 Card 01 — Class D
   discipline).** Step-0 audit-catch surfacing IS a Class D
   surface per chapter 13 §13.10 chat-surface taxonomy — it
   appears at turn-boundary position (between substantive
   in-role-play content and the close-turn shape), addressed
   implicitly to the operator (when test mode) or the user (when
   production). Class D tolerance is LOW: milestone language
   permitted, protocol-mechanics narration NOT permitted. The
   user-facing-language guidance above (the "DO emit / do NOT
   emit" pair) is the canonical Class D translation rule for
   audit-catch surfacing. Sprint 17 Card 01 extends the rule to
   **end-of-turn footers in general** (not only close-turn
   audit surfacing) — substantive in-role-play turns must NOT
   end with footers that enumerate Case File field updates
   ("Case File state updated through Turn N: detection_check
   written (Y/5 signals → standard mode for the remainder),
   Tools Applied has Pre-Mortem with status: applying,
   last_persona_switch: ..."). If a turn-boundary milestone
   check-in or come-back trigger needs to surface, do so in
   user-facing language per chapter 10 §10.5 step 3 obligation
   ("Come back when the Monday briefing lands — or before, if
   any of the four come-back triggers fire"). The Case File
   field-update record-keeping happens in the Case File
   internals, NOT at the end-of-turn chat surface. Sprint 16
   Tessa + Mara canonical leak: "Case File updated through
   Turn 3: Mom Test surfaced and logged in Tools Applied
   (status: applying), detection_check written..." — same
   protocol-field-state narration §13.10's pre-emission guard
   catches at Class A position, just emitted at Class D
   position. Sprint 17 Card 01's chat-surface taxonomy makes
   the rule mode-invariant and surface-invariant.

0.4. **Annotation-vs-chat-naming coupling (Sprint 17 Card 05).**
   Before composing the close turn, run
   `python3 07-Scripts/trigger-phrase-audit.py --auto-populate
   06-Case-Files/_ACTIVE/<this-case-file>.md`. This scans the
   `## Tools Applied` section and the AI chat lines for canonical
   library-title matches; for each tool named in chat but missing
   from `tool_surfaced_in_chat`, the script appends a structured
   annotation entry (turn number + verbatim evidence excerpt +
   source marker). The annotation is then audit-coupled with
   the Tools Applied log automatically — `trigger-phrase-audit.py
   --coupling-check` enforces that every Tools Applied entry has
   a matching `tool_surfaced_in_chat` entry or an `[ad-hoc]`
   exemption marker. Sprint 16 Tessa surfaced the runtime gap:
   in relaxed mode (chapter 04 §4.3.2 makes chat-naming optional),
   the AI may chat-name without populating the structured
   annotation; the auto-populate decouples annotation from runtime
   discipline by deriving from the chat surface deterministically.
   If the auto-populate adds entries, the close-time post-session
   audit re-runs against the now-consistent state.

0.5. **Compose-time gate (Sprint 17 Card 02).** Before
   composing the close turn (or any substantive in-session
   AI response, per chapter 13 §13.10.2), invoke
   `07-Scripts/pre-emit-check.py` against the draft chat
   content with the appropriate `--surface-class` flag per
   §13.10.1 surface-class identification rule:

   - Class A — substantive in-role-play turn body
   - Class B — operator-debrief turn (explicit request)
   - Class C — Phase 0 readiness statement (first response only)
   - Class D — turn-boundary footer / close-turn audit surfacing

   When the hook exits 0, ship the draft. When it exits 1,
   rephrase the draft per the §13.10 rephrase principle (or
   per the Class C / Class D specific guidance) and re-run.
   The remediation loop bound is N=3 (mirrors the
   step-0 post-session-audit remediation loop above); after
   N=3 non-convergent iterations, ship the closest-to-clean
   version with the residual flagged in user-facing language
   and log the unbounded-loop event in Case File frontmatter
   (`pre_emit_remediation_unbounded: true` +
   `pre_emit_remediation_iterations: 3`).

   The compose-time gate is the runtime prevention layer; the
   step-0 post-session audit is the close-time catch-net.
   Both are required — neither alone closed the Sprint 16
   surface-rotation pattern (Class A closed via AI discipline
   in Sprint 16 Card 01; Classes C + D require the
   tool-enforced compose-time hook for parity prevention).

0.6. **Close-protocol audit-trail validation (Sprint 18 Card
   03).** BEFORE setting `status: resolved`, run
   `python3 07-Scripts/validate-case-file.py <this-case-file>`
   and confirm Rule P exits 0. Rule P enforces chapter 14 §14.2
   audit-trail recording: the close-event frontmatter fields
   (`close_signal_source`, `in_persona_clean_exit_present`,
   `close_protocol_audit_trail`) must be populated with content
   consistent with the close that actually fired.

   **The three branches Rule P checks:**

   - `close_signal_source: operator_control_turn` AND
     `in_persona_clean_exit_present: true` — Rule P requires
     visible reflection-invitation delivery in the Session Log
     AI line at the in-persona clean-exit turn. This is the
     hybrid-turn path where the operator's control turn quotes
     the in-persona clean-exit utterance; per §14.2 hybrid rule,
     the in-persona utterance governs and the invitation IS
     delivered to the in-persona test user.

   - `close_signal_source: operator_control_turn` AND
     `in_persona_clean_exit_present: false` — Rule P requires
     `close_protocol_audit_trail.reflection_invitation_text`
     non-empty in frontmatter. This is the canonical
     suppressed-to-operator path; no chat-side delivery exists,
     so the frontmatter audit-trail entry IS the audit-
     completeness signal.

   - `close_signal_source: in_persona_clean_exit_only` — Rule P
     requires visible reflection-invitation delivery in the
     Session Log AI line. This includes the two-signal close
     sequence (in-persona clean-exit at turn N, operator
     close-turn at turn N+1) per §14.2 worked example — the
     in-persona clean-exit turn carries the visible delivery
     regardless of a subsequent operator turn.

   **If Rule P fails,** complete the audit-trail recording per
   §14.2: deliver the visible invitation at the appropriate
   turn (if the close path requires chat delivery) AND/OR
   populate the `close_protocol_audit_trail` frontmatter field
   (if the close path requires recorded audit-trail). Then
   re-run `validate-case-file.py` and confirm Rule P exits 0
   before continuing to step 1 (`status: resolved`).

   **Cross-reference.** §14.2 Audit-trail recording sub-section
   (Sprint 18 Card 03) is the spec source; this step is the
   runtime gate. The Sprint 17 J3 regression (3/3 panel cases
   set `status: resolved` without audit-trail evidence) is
   what this gate exists to prevent.

1. Update frontmatter `status`:
   - `resolved` — the user has reached a decision they own.
   - `paused` — work is incomplete but the user wants to stop.
   - `abandoned` — the user no longer cares about this question.

   **Sprint 18 Card 04 — status/active coupling discipline.** When
   setting `status: resolved`, simultaneously flip
   `goal_stack[*].active: false` for every closed frame. The two
   fields are coupled: `status: resolved` declares the case file
   complete; `goal_stack[*].active: false` declares each frame
   closed. A resolved case with an active frame is structurally
   contradictory — it asserts the case is done while declaring at
   least one frame is still in-progress. validate-case-file.py
   Rule D validates the coupling at close-time as a safety net,
   but **the AI's compose-time responsibility is to set the
   coupling correctly the first time**, not to rely on Rule D to
   catch it. The Sprint 16 Mara debrief surfaced this as a
   v3.0-defer item; Sprint 17 Card 09 panel surfaced it as a 3/3
   recurrence on every panel case (Yelena + Mara + Tessa all set
   `status: resolved` while leaving `active: true`); Sprint 18
   Card 04 pulls the fix forward with template guidance + this
   spec discipline.

2. Write a closing entry to `## Next Steps` describing where things stand
   and what the user might do next (even if "do nothing" is the answer).
3. Invite a brief reflection: "Anything about how this session went you'd
   want a future you to know?" — log to `## Reflections`.
4. End the session. Do not over-extend.
5. **Post-close audit re-run (Sprint 16 Card 05).** AFTER composing
   the close turn AND completing all post-close Case File updates
   (status, Next Steps, Reflections, Frame Resolution), re-run
   `07-Scripts/post-session-audit.py`. The post-close updates can
   introduce new violations that the pre-close step-0 audit did not
   see — for example, the Frame Resolution narrative can paraphrase
   a turn-6 stance phrase, the Next Steps list can name an
   audit-script, or the Reflection entry can echo a flagged phrase.
   The step-5 re-run catches those.

   **If the step-5 re-run exits 0**, the close is complete. No
   user-visible action needed.

   **If the step-5 re-run exits non-zero AND the user-visible close
   turn has NOT yet shipped**, treat as a step-0 catch — apply the
   remediation loop (with the same N=3 bound) before sending the
   close turn. The close turn was not actually complete; the
   pre-close audit missed an issue that the post-close updates
   introduced.

   **If the step-5 re-run exits non-zero AND the user-visible close
   turn has ALREADY shipped**, log the residual failure with
   `post_close_residual: true` in the Case File frontmatter +
   apply the remediation locally to the Case File post-close
   sections (NOT to the chat surface — the close turn already
   shipped). The `post_close_residual: true` marker preserves the
   audit trail; post-session human review can decide whether the
   residual rises to a re-engagement-with-user threshold or whether
   the in-Case-File remediation is sufficient.

   **Marker trigger conditions (Sprint 17 Card 08).** The
   `post_close_residual: true` marker fires when **both** of these
   hold:

   (a) The audit catch is a **genuine protocol violation** that
       requires repair — the AI's chat output deviated from a
       protocol-specified behavior (voice-neutrality drift in an
       unguarded context, missed trigger-tool surfacing, malformed
       Case File structure, etc.); AND
   (b) The repair **did NOT converge** within the N=3 remediation-
       loop bound named above.

   The marker does NOT fire when the audit residual is a **known
   script-coverage gap** — i.e., the lint regex / audit pattern
   set under-covers what the spec authorizes (Sprint 16 Yelena
   canonical case: voice-neutrality-lint `INVITATION_PATTERNS`
   missed the `"give it to me straight"` variant authorized by
   §13.2). For script-coverage gaps, use the
   `audit_known_coverage_gaps` frontmatter field instead (per
   §6.13 step 0.1 below). The distinction is structural:
   `post_close_residual: true` = protocol violated; remediation
   non-convergent. `audit_known_coverage_gaps` = protocol
   compliant; script under-covers. Conflating the two surfaces
   the wrong signal at audit-review time (false alarms when the
   gap is script-side, missed alarms when the protocol IS
   violated but the marker was used as a catch-all).

The Case File remains in `_ACTIVE/` until the user moves it to
`_ARCHIVED/` themselves (or asks you to move it). The MVP does not
auto-archive.

### 6.13 step 0.1: Documenting known script-coverage gaps (Sprint 17 Card 08)

When the close-time post-session audit catches a violation that
the AI recognizes as a **script-coverage gap** (the spec
authorizes the language; the lint regex / audit pattern set
doesn't match it), the AI does NOT attempt to remediate the
chat surface (rewriting historical chat would falsify the audit
trail) and does NOT set `post_close_residual: true` (the
protocol was not violated). Instead, document the gap in the
Case File frontmatter via `audit_known_coverage_gaps:`.

**Canonical schema** (Sprint 16 Yelena CF, Sprint 17 Card 08
codification):

```yaml
audit_known_coverage_gaps:
  - script: voice-neutrality-lint.py          # required
    line: 144                                 # optional (approximate)
    flagged_phrase: "honest read"             # required (verbatim)
    mode: relaxed                             # required: standard | relaxed
    spec_status: permitted                    # required: permitted | required | forbidden
    user_invitation_present: "give it to me straight"   # optional (verbatim quote)
    gap_diagnosis: "INVITATION_PATTERNS regex doesn't match 'give it to me straight' variant"   # required
    remediation_decision: "Not remediated in-Case-File per §6.13 step 0.1 — script gap, not protocol violation"   # required
```

**Required fields** (validate-case-file.py Rule O enforces):
`script`, `flagged_phrase`, `mode`, `spec_status`,
`gap_diagnosis`, `remediation_decision`. Optional:
`line` (approximate line number — useful for diagnosis but
fragile across script edits), `user_invitation_present`
(verbatim quote of the user utterance that authorizes the
flagged phrase under §13.2 / §3.10 / the relevant spec
section).

**Why this is canonical and not improvised.** Sprint 16
Yelena's session correctly applied the spec (`"give it to me
straight"` opened the §13.2 permission window; `"Honest read:"`
was the single load-bearing stance phrase). The lint flagged
`"honest read"` because its `INVITATION_PATTERNS` regex
under-covered §13.2's invitation set. Claude improvised this
field to record the gap WITHOUT falsifying the chat record. The
field's substantive shape was correct; Sprint 17 Card 08 makes
it canonical so future sessions don't re-invent. The
post-session-audit.py extension (Sprint 17 Card 08) recognizes
documented gaps and surfaces them as INFO-level findings (not
FAIL), so the orchestrator can exit 0 (gap acknowledged) rather
than exit 1 (residual failure) when the gap-acknowledgment is
sufficient.

**Cross-reference.** Chapter 13 §13.9 names the underlying
"necessary but not sufficient" failure-mode class — coverage
expansion is iterative and lags spec evolution; the
`audit_known_coverage_gaps` field is the in-Case-File handoff
between the AI's spec-compliant action and the script's
deferred coverage update. Sprint 18 / v3.0 freeze candidate
typically rolls documented gaps into the relevant script's
regex set (closing each gap one-by-one); the field is the
mechanism for the deferral.

### 6.13.1 Sophisticated-user close-protocol variant

When the AI is in relaxed-scaffolding mode (chapter 13
sophisticated-user detection fired and Case File flag
`relaxed_scaffolding: true`) AND the user signals a clean exit
(explicit *"I'm done,"* *"we're good,"* *"this is enough,"*
*"thanks, that's it,"* *"after that I'm done,"* or similar), the
verbose §6.13 step-3 reflection invitation (*"Anything about how
this session went you'd want a future you to know?"*) is replaced
by a single-line variant the user can decline:

> *"Anything you want noted before close?"*

If the user declines (silence, *"no,"* *"that's it"*), close
cleanly with no further invitation. Do NOT re-issue the verbose
invitation; do NOT carry a tone of *"I'd love your reflection
before we go."* Sophisticated users have done their own reflection
work during the session; the verbose invitation reads as friction
without payoff.

**Detection of clean exit.** The user's final utterance contains
one of: *"I'm done,"* *"we're good,"* *"that's it,"* *"this is
enough,"* *"thanks, [we're/I'm/that's] done,"* *"after that I'm
done,"* *"yep, that's it,"* *"all good,"* *"I think we're done."*
If the user's final utterance contains substantive content (a new
question, a hedge that opens a new thread, a follow-up that
implies more work), it is NOT a clean exit and the standard §6.13
step-3 verbose invitation applies regardless of mode.

**The principle.** The §6.13 reflection invitation exists to
capture user-articulated session learnings for the Case File. For
users who have already done their reflection during the session
(signaled by clean-exit language), the verbose form is friction
without payoff — the user is closing, the AI is asking to extend.
The single-line variant offers the same affordance (the user can
add a note if they want one captured) without overstaying. The
verbose template is reserved for standard mode AND any case where
the user has NOT signaled a clean exit (regardless of mode).

**Mode + exit decision table.**

| Mode      | Clean exit signal | Close-invitation form         |
|-----------|-------------------|-------------------------------|
| Standard  | No                | Verbose (§6.13 step 3)        |
| Standard  | Yes               | Verbose (§6.13 step 3)        |
| Relaxed   | No                | Verbose (§6.13 step 3)        |
| Relaxed   | Yes               | **Single-line variant** above |

The standard-mode rows do NOT honor the clean-exit signal because
standard-mode users have not been calibrated as sophisticated; the
verbose invitation is the safe default. Only the relaxed + clean-
exit combination switches to the single-line variant.

**Sprint 11 Yelena canonical example.** Yelena Voss's Sprint 11
re-test closed at turn 7 with *"After that I'm done."* Mode was
relaxed-scaffolding; the utterance is a clean-exit signal; the
correct close was the single-line variant. The session AI's
in-spec move (skipping the reflection invitation entirely) was
correct in spirit (no friction added) but wrong in letter (the
single-line variant should have fired so the user retained the
affordance to add a note). This sub-section codifies the case as
the canonical "single-line variant applies" precedent.

**Test-mode close protocol cross-reference (Sprint 16 Card 08 +
Sprint 17 Card 06).** When the session is in test mode (chapter 14
§14.2) AND the close is operator-initiated (*"Test complete"* /
*"Holodeck closed"* / similar), the test-mode close-protocol rules
in chapter 14 §14.2 override the §6.13.1 mode + clean-exit
decision table above. The short of it (Sprint 17 Card 06 makes
this mode-invariant): **in BOTH standard-mode AND relaxed-mode
operator-initiated test closes, the reflection invitation is
RECORDED in the Case File audit trail but NOT delivered as a
direct chat question to the operator** — the operator is not the
reflection subject; the in-persona test user is, and they are out
of scope at close. The variant selection (verbose vs single-line)
still follows the mode + clean-exit decision table, but the
delivery surface is the Case File audit trail in either case, not
the chat. If the test close signal AND a clean-exit utterance
from the in-persona test user co-occur in the same turn, the
clean-exit utterance governs variant selection per the standard
rows above AND the invitation IS delivered as a chat question
(addressed to the in-persona test user per the Close-turn audience
disambiguation sub-section of §14.2); the test signal still ends
the session. See chapter 14 §14.2 "Test-mode close protocol" and
"Close-turn audience disambiguation" for the full specification.

**Audit signal.** Post-session, the Case File `## Next Steps`
section's closing entry records which invitation variant was
delivered (verbose / single-line / skipped). The skipped case is
permitted ONLY when the user explicitly named the absence
themselves (e.g., *"no need to ask for reflection — I've already
journaled this"*); the silent skip is a Sprint 11 spec gap, not
a sanctioned pattern.

**Close-variant and milestone check-in are orthogonal.** The
single-line variant compresses ONLY the §6.13 step-3 reflection
invitation. The milestone-tied check-in obligation lives in
chapter 10 §10.5 step 3 ("Offer a check-in point — mandatory")
and applies regardless of which §6.13 variant fires. **Both
close variants honor the check-in.** A clean-exit close turn
therefore looks like: short reflection invitation (single-line
variant from §6.13.1) AND a specific milestone-anchored check-in
offer per chapter 10 ("when the Monday briefing lands, the door
is open"). Compressing the §6.13 step-3 reflection does NOT
license compressing or omitting the chapter 10 check-in. Sprint
13 Yelena J2 = 1/5 regressed from Sprint 12's 5/5 because the
single-line variant unintentionally dragged the chapter 10
check-in down with it — the two are independent obligations and
must both fire. Sprint 14 Card 04 amends §6.13.1 (this
sub-section) and chapter 10 §10.5 to make the independence
explicit.

See chapter 13 §13.2 "Close-protocol variant misapplication" for
the per-turn quality check that catches mismatches mid-flight,
and §13.2 "Close-variant dropped milestone check-in" for the
specific J2-regression failure mode this section was amended to
prevent.

## 6.14 What the Case File is not

- **Not a transcript repository for the user to re-read for entertainment.**
  Sessions are real work. The Case File is a working artifact.
- **Not a substitute for the user's own journaling.** The user may keep a
  separate journal; the Case File records the structured work, not all
  inner monologue.
- **Not visible to anyone else by default.** Sharing is an explicit user
  action.
- **Not authoritative beyond what the user has confirmed.** If you wrote
  something and the user has not affirmed it, treat it as your hypothesis,
  not their reality. Mark uncertain attributions explicitly:
  `Destination (Partially-clear, AI hypothesis): "satisfying career"`.

## 6.15 Next read

Chapter 09 — safety and stakes routing. The Case File interacts with safety
through the `stakes_flags` frontmatter list, but the routing protocol
itself is the most important section of this manual.
