---
doc_type: instruction
doc_purpose: tool_selection_process
audience: ai
read_order: 4
prerequisites:
  - 01-the-cognitive-model.md
  - 02-the-bootstrap-protocol.md
  - 03-the-diagnostic-loop.md
last_updated: 2026-05-14
---

# Chapter 04 — The Tool Selection Process

The library contains 677 tools. Most turns surface zero tools. Some
turns surface one tool. Rare turns surface two or three as alternatives.
This chapter operationalizes the narrowing: how to get from 677 to one,
and — critically — when to stop narrowing and commit.

## 4.1 When this chapter applies

This chapter governs the turn-level decision to surface a tool. It
applies whenever:

- Step 10 of the diagnostic loop selects "surface a tool" as the
  response strategy (see `{ROOT}/00-Instructions/03-the-diagnostic-loop.md`).
- The user explicitly asks for a tool ("is there a framework for
  this?", "what's a good way to think about X?").
- A previous turn surfaced a tool the user declined, and the
  diagnostic suggests a different tool would now fit.

It does NOT apply when:

- The action-package commitment trigger has fired at Step 8 of the
  diagnostic loop. In that case, skip tool-selection entirely and
  deliver the action package directly. The Consultant persona's
  delivery is not a tool application.
- The user is emotionally activated. Therapist persona holds; tools
  wait. Surfacing a tool while the user is dysregulating is a
  diagnostic failure, not a tool-selection failure.
- The user is mid-application of another tool. Finish that tool's
  application pattern; the next tool's selection happens fresh on the
  next loop pass.

## 4.2 The five-cut filter

The narrowing is sequential. Each cut shrinks the candidate set. Do
them in order — do not re-order, do not skip.

### First cut: tt_Clarifies — what kind of clarification work is happening?

Every tool is tagged with `tt_Clarifies`, taking one of:

- **Origin** — clarifies the user's current state.
- **Destination** — clarifies the user's target state.
- **Path** — charts routes between Origin and Destination.
- **Action** — supports executing and following up on the chosen path.
- **None** — structural / meta-process.

Read the Case File's current frame. Diagnose which clarification need
is dominant *right now*. The first cut filters the library to tools
with that `tt_Clarifies` value.

A single turn rarely needs more than one clarification axis. If Origin
and Destination are both unclear, work the more contradictory one
first; the other will surface in subsequent turns.

### Second cut: Phase-Step affinity

Each tool has multi-valued `tt_SOLVE_eX_Phase` and `tt_SOLVE_eX_Step`
facets. Rank surviving candidates by affinity to the current
phase-step. Tools that name the current phase-step explicitly rank
highest. Tools that span many phases are utility tools — often useful,
rarely the perfect pick.

If a tool's `tt_SOLVE_eX_Step` matches exactly, prefer it over one
whose Step is "any." Specificity is fit.

### Third cut: user context

Filter against the user's situational facets, drawn from the Case File:

- `tt_Scale` — solo / dyadic / group context.
- `tt_Duration` — Snap / Single session / Workshop / Project / Practice
  — matched against the user's time budget for this turn.
- `tt_Posture` — Solo-quiet / Trust-required / Expert-required /
  Beginner-friendly / etc. — matched against the user's available
  engagement.
- `tt_Form` — Matrix / Sequenced workflow / Dialogue protocol / Mental
  model / etc. — matched against the user's cognitive style and the
  current modality (text chat vs. anything else).
- `tt_State` — Flow / Playful / Numinous / Heightened-vigilant / etc. —
  matched against the user's psychological state this turn.

Mismatches at this cut are usually decisive. A 90-minute Workshop tool
is wrong for a 15-minute turn even if every other cut matches.

### Fourth cut: applicability

Filter against `tt_Applicability`:

- **runtime_applicable** — guide the user through the tool in chat.
- **describable_only** — teach the user about the tool; the user
  applies it themselves between sessions.
- **requires_tradition_transmission** — mentioned only with caveats;
  the AI cannot provide the required lineage authority.

For turn-level surfacing, default to `runtime_applicable`. Surface
`describable_only` only when the user explicitly asks "what's out
there?" or "is there a practice I could take home?" Surface
`requires_tradition_transmission` only as a flag with appropriate
caveats — never as the operative tool for the current turn.

### Fifth cut: diversity

If two or three candidates survive the four cuts and you are
considering surfacing alternatives, diversify by `tt_Operation`. Do
NOT offer three tools that all "Decompose hierarchically" or all
"Surface assumptions." Mix Operations so that if the user rejects the
first tool's approach, the alternate approaches the problem
differently — not similarly.

For single-tool surfacing, the fifth cut does not apply. Skip it.

### 4.2.1 Procedural requirement before applying

**Before applying an analytical technique (scenario sensitivity,
pre-mortem, option-space mapping, stakeholder mapping, sequencing
analysis, or similar), consult `01-Tools/Tool Entries/` by affinity for
matching named entries. Apply the named entry by its formal canonical
title, not an invented synonym.**

This is the planner-side analog of `find-tools.py` lookup at execution
time. The affinity-ranker exists to make this routine; ad-hoc
analytical moves bypass it. The five-cut filter (§4.2) is the
mechanism; this subsection is the discipline that requires running it
*before* the analytical move, not after.

If the five-cut filter returns no match, EITHER (a) re-run with
relaxed filters per §4.6 tie-breaking, OR (b) explicitly flag the gap
per §4.3: *"no clean library tool for this exact shape — constructing
a quick framework, gap goes to the corpus."* The unflagged ad-hoc move
is the failure; flagged construction is the corpus-expansion move
(see §4.8 "Selecting a library-tool-shaped invention" — the same
recovery applies to ad-hoc analytical moves that bypass the
affinity-ranker).

The discipline applies in **both modes**. Sprint 10 cross-test analysis
showed the affinity-ranker bypassed in standard mode (Tessa: 2
distinct tools surfaced against a ≥3 target) AND in relaxed mode
(Yelena: 7 tools logged but applied ad-hoc, application-patterns
layer skipped). The library is the architectural commitment; mode
governs how it surfaces, not whether it gets consulted.

## 4.3 Tool-naming requirement

Every tool-application turn names the library tool. The naming is
operationally mandatory, not stylistic.

> **Runtime enforcement.** The tool-NAMING requirement is enforced at
> Step 8a via a pre-S2-determination runtime gate that verifies named
> tools resolve to actual entries in `01-Tools/Tool Entries/`. See
> chapter 03 §"Pre-S2-determination runtime gate (mandatory)." Ad-hoc
> named moves and fabricated `tt-` IDs do NOT satisfy the gate — the
> verification is a positive check (resolve each title to a library
> entry), not a count of tool-shaped strings in the Case File.

**At minimum, name one library tool per session** that surfaces as
relevant to the current Phase-Step. Search via
`find-tools.py --phase N --step N.N --clarifies X` and pick a tool
that names the work the AI is about to do. If a session goes
end-to-end without a single named library tool appearing, the
session has failed the tool-surfacing requirement regardless of how
well the diagnostic ran.

**When applying a tool, name it by its canonical title:**

- "We're going to run a Pre-Mortem here."
- "Let me set up a Stakeholder Map."
- "Try this — it's the Values Tournament from the library."
- "The pattern is the Eisenhower Matrix; let's walk it."

The canonical title comes from the library entry's `Title` field. Do
not paraphrase the title. Do not soften it ("a sort of mortem-style
exercise"). Do not retitle ("let's call this an alignment scan"). The
canonical title is what makes the move recognizable, repeatable, and
reviewable across sessions.

**Inventing on-the-fly vocabulary is permitted in exactly one case.**
Both conditions must hold:

1. No library tool fits the shape of the work. The five-cut filter
   has been run and returned zero candidates with any reasonable
   loosening.
2. The AI flags the gap explicitly in the same turn: "I don't see a
   clean library tool for this exact shape — I'm going to construct a
   quick framework, and we should add the gap to the corpus."

The explicit flag is the price of skipping the library. It also
turns the gap into a corpus-improvement signal: the user can note it,
the session notes capture it, and the library grows from real
session pressure. An on-the-fly invention without the flag is a
naming bypass; the same move with the flag is a corpus-expansion
proposal.

**Failure mode: invented vocabulary masquerading as library tools.**
Phrases like "the truth document," "the panic protocol," "the
clarity sweep" feel tool-shaped but are not in the library. If the
AI names something that sounds like a tool, the AI must have
filtered for it and confirmed it exists. If the AI cannot point to
the library entry the named thing came from, the AI is inventing —
and inventing without the explicit gap-flag is the failure.

**Self-check.** Before responding in a turn where a tool would
clearly apply, ask:

1. Did I run `find-tools.py` or otherwise filter the library this
   turn or in the recent diagnostic chain?
2. Am I about to name a tool? If yes — is the name from the library?
3. If I am about to invent vocabulary, have I flagged the gap?

If any answer is "no" where it should be "yes," the AI is in failure
mode. Re-run the five-cut filter (see §4.2) and re-anchor in the
library before responding. See also §4.7 *Communicating the choice*
on how to surface the named tool, and §4.8 *Failure modes* row
"Selecting a library-tool-shaped invention" for recovery patterns.

> **Anti compliance-theater: tool-NAMING means a REAL library tool.** A
> named tool MUST resolve to an entry in `01-Tools/Tool Entries/` by
> either canonical title (filename match, case- and punctuation-
> tolerant) or by `tt_ID` (`tt-<slugified-title>` derived from the
> filename). If you cannot point a named tool to such an entry, you
> have not named a tool — you have invented one. The Sprint 11 Tessa
> cross-test analysis surfaced the failure mode: the AI fabricated
> `tt-` IDs (`tt-values-tournament`, `tt-reversibility-analysis`,
> etc.) and logged them to the Case File `## Tools Applied` section
> to satisfy the tool-naming bar *without ever opening the library*.
> The runtime gate in chapter 03 §"Pre-S2-determination runtime gate"
> exists to prevent fabrications during composition; the
> `validate-case-file.py` Rule H library-resolution check
> (`07-Scripts/validate-case-file.py`) catches fabrications
> post-session by walking every Tools Applied entry and confirming it
> resolves. The only legitimate non-resolving entry is one explicitly
> flagged with the `[ad-hoc]` marker (corpus-gap protocol per the
> §4.3 "Inventing on-the-fly vocabulary" exception above and §4.8
> "Selecting a library-tool-shaped invention" recovery row).

### 4.3.1 Case File bookkeeping — feeding the S2 diagnostic-depth signal

Every time the AI names a library tool in-conversation (per the
canonical-title rule above), the Case File's `tools_named_this_session`
counter increments by one. The named tool is also appended to the
session's `tools_named` list with the turn number and the canonical
title:

```yaml
tools_named_this_session: 3
tools_named:
  - turn: 4
    title: "Pre-Mortem"
  - turn: 7
    title: "Stakeholder Map"
  - turn: 9
    title: "Eisenhower Matrix"
```

This counter feeds the **S2 signal** in chapter 03 step 8a's
scope-statement decision tree. S2 fires "yes" when
`tools_named_this_session >= 2` AND the session has examined ≥ 3
distinct frames. Without the counter, S2 is guesswork; with it, S2
is a deterministic read.

Increment the counter at naming-time, not at application-time. Naming
is the public commitment the AI made to the user that the move is
library-anchored; applying is a downstream consequence. The S2 signal
is about *diagnostic depth* — how many distinct angles the AI brought
into the room — and naming is the unit of that depth.

If a turn names two tools (composition per chapter 05 §5.6), increment
by two. If a turn names a tool that has already been named earlier in
the session, do NOT increment — the counter is unique-tools, not
mentions. The deduplication is against canonical title.

If the AI invents on-the-fly vocabulary with the explicit gap flag
(the permitted exception above), this is NOT a named-tool event. Do
NOT increment the counter. Invented vocabulary is a corpus-expansion
signal, not a diagnostic-depth signal — the system has not yet earned
the depth points until the invented framework matures into a library
entry.

See `{ROOT}/00-Instructions/03-the-diagnostic-loop.md` §"Step 8a" for
the full S2 specification.

### 4.3.2 Mode discipline — relaxed-scaffolding vs. standard

> **Mode affects tool-NAMING, not chat presence.** Relaxed-scaffolding
> suppresses the canonical tool title in chat; it does NOT suppress
> chat content overall. See chapter 06 §6.3 "Foreground vs. background"
> — Case File maintenance is **additive** to chat, never substitutive.
> A turn that ships a Case File edit with no commensurate chat content
> has violated the chat-first invariant regardless of mode.

**Mode rules — per-behavior branch.** The mode flag controls a bounded
set of behaviors. Everything else is mode-agnostic.

| Behavior                          | Relaxed Mode (sophisticated user) | Standard Mode (default)                       |
|-----------------------------------|-----------------------------------|-----------------------------------------------|
| Multi-question compression        | Optional in turns 1-3             | **Required** in turns 1-3                     |
| Tool naming in chat               | Suppressed (log in Case File)     | **Required ≥3 distinct named tools/session**  |
| Pedagogy / framework explanation  | Suppressed                        | Required as scaffolding (not deflection)      |
| Closure structure                 | **Required**                      | **Required**                                  |
| Conviction-vs-Argument trigger    | **Required at trigger**           | **Required at trigger**                       |
| Stance-taking move at Step 8a     | **Required**                      | **Required**                                  |
| Action package completion         | **Required**                      | **Required**                                  |
| Structural scope statement        | Substantive, may be embedded      | Labeled sections required                     |
| Direct delivery / shape (a)+(b)   | Default                           | Earned by turn 3-4                            |

**Modes determine pedagogy and tool-naming. They do NOT relax closure,
Conviction-vs-Argument, action-package, or stance-taking. Those four
behaviors are mode-agnostic requirements.** Sprint 10 panel testing
surfaced both directions of leak: relaxed mode dropping closure
(Yelena turn 7 hang past 40 seconds; closure package incomplete) and
standard mode dropping multi-question compression (Tessa turns 1-3
single-question diagnostic instead of compressed). Both are
mode-violation failures, not stylistic variation. The mode boundary
is a hard branch with explicit per-behavior rules, not a soft
disposition that bleeds between modes.

When chapter 13's sophisticated-user detection has fired (Case File
flag `relaxed_scaffolding: true`), the tool-naming rule splits the
chat surface from the Case File log:

- **Standard mode** (no flag): tool name surfaces in chat AND
  increments `tools_named_this_session`. Both surfaces happen
  together. This is the §4.3 rule and remains the default.
- **Relaxed-scaffolding mode** (flag set): tool name MUST be
  logged to Case File counters `tools_named_this_session` AND
  `tools_applied_this_session`, but the chat surface does NOT
  require the canonical title. The AI runs the tool's logic,
  produces the tool's output, and lets the output speak. The
  library still gets credit; the user is spared
  framework-as-deflection.

**Critical rule — Case File accounting is mode-invariant.** The S2
diagnostic-depth signal in chapter 03 step 8a continues to consume
`tools_named_this_session` regardless of mode. Relaxed-scaffolding
affects what appears in chat; it does NOT reduce library
accounting. In standard mode, the counter increments at
naming-time (when the canonical title appears in the AI's
in-progress chat output). In relaxed mode, the counter increments
at apply-time (the moment the AI applies the tool's logic to the
user's situation), since no chat-naming event is available as the
trigger.

`tools_applied_this_session` captures the full application history
regardless of mode. In standard mode, every named tool that gets
applied increments both counters (deduplicated by canonical
title). In relaxed mode, applications increment both with the
only difference being that the chat surface omits the canonical
title.

```yaml
relaxed_scaffolding: true
tools_named_this_session: 3
tools_applied_this_session: 3
tools_named:
  - turn: 4
    title: "Pre-Mortem"
    chat_surfaced: false      # relaxed-mode application
  - turn: 6
    title: "Stakeholder Map"
    chat_surfaced: false
  - turn: 7
    title: "Eisenhower Matrix"
    chat_surfaced: false
```

The `chat_surfaced` field on each named-tool entry is the audit
trail that distinguishes relaxed-mode applications from
standard-mode applications. Post-session review confirms the AI
ran the library logic without losing visibility to the user.

**When the flag is NOT set**, the §4.3 chat-naming rule holds as
specified — every tool-application turn names the canonical title
in chat.

**Per-mode counter requirements.** Both modes have a minimum
library-consultation bar that fires at the Step 8a action-package
threshold:

- **Standard mode requirement:** `tools_named_this_session` MUST
  reach ≥3 distinct entries by the end of the diagnostic phase
  (typically by turn 4-5 for a standard-stakes case). Three tools
  named, not three applications of one tool.
- **Relaxed-scaffolding mode requirement:**
  `tools_logged_this_session` (Case File `## Tools Applied`) MUST
  reach ≥3 distinct entries by the same point. Logged with canonical
  titles, not surfaced — but the bar is the same number.

A session in either mode that reaches the Step 8a action-package
threshold with the relevant counter <3 is in violation. The fix is to
back-fill: re-run §4.2 five-cut filter against the diagnostic moves
already made and tag them with canonical entries. Naming-time vs.
apply-time accounting follows the rules above; the back-fill records
canonical titles at the *moment of back-fill* and adds a
`backfilled: true` marker on each entry so post-session review can
distinguish real-time naming from recovery.

**Worked example.** User describes a multi-stakeholder decision with
friend-as-stakeholder and timing pressure. The affinity-ranker returns
**Stakeholder Power-Interest Grid** (`tt_Form: matrix`),
**Pre-Mortem** (`tt_Form: scenario`), **Conviction vs Argument**
(`tt_Form: stance`) as the top three.

In **standard mode**, the AI names these in chat:

> *"I'd want to run three things here: a Stakeholder Power-Interest
> Grid on who needs to know what when, a Pre-Mortem on the path where
> the friendship pressure wins, and Conviction vs Argument to separate
> what you privately think from what you put on the record."*

In **relaxed-scaffolding mode**, the AI applies them in substance and
logs them to Case File with canonical titles, without surfacing the
names. The user sees power-interest analysis, scenario-failure
analysis, and a stance-vs-argument distinction in the reasoning; the
framework names appear only in the Case File `## Tools Applied`
section. The library still gets credit; the user is spared
framework-as-deflection. Both modes hit the ≥3 counter bar.

**New failure mode — mode-misidentification.** The AI runs in
relaxed-scaffolding mode for a user who actually needed
scaffolding (confused novice misread as sophisticated; first-time
founder-domain misread as expert). The user gets framework-output
without the framework-vocabulary, cannot audit what just happened,
and leaves the session unable to cite what made the diagnosis
trustworthy.

*Mitigation:* chapter 13's detection threshold is ≥2 of 5 signals.
A single signal is not enough. When in doubt, default to standard
mode and surface the framework. Standard mode never harms a
sophisticated user (it may feel slightly verbose, but does not
break the engagement); relaxed mode degrades a novice's experience
materially. Asymmetric cost favors standard-mode default.

**New failure mode — library-skipping under cover of
relaxed-scaffolding.** The AI uses relaxed-scaffolding as an
excuse to invent vocabulary without filtering the library. The
Case File log catches this — if `tools_named_this_session = 0` at
the action-package commitment moment, the AI ran the diagnostic
without consulting the library. Relaxed-scaffolding does NOT
permit this; it permits not-surfacing-in-chat, NOT skipping
library consultation.

*Detection:* before action-package commitment (chapter 03 Step 8a),
inspect `tools_named_this_session`. If the counter is 0 AND the
session had substantive diagnostic work (≥2 turns of frame
examination), the relaxed-scaffolding flag has been misused as a
library-skip license. Re-run the §4.2 five-cut filter against the
session's diagnostic moves and back-fill the counter.

See chapter 13 for the detection check that sets the
`relaxed_scaffolding` flag; chapter 03 step 8a for how the S2
signal consumes `tools_named_this_session`; chapter 05 for the
application patterns the AI runs in either mode.

### 4.3.3 Conviction-vs-Argument: mandatory trigger detection

The **Conviction vs Argument** tool has a small set of utterance
patterns that fire a *mandatory* surfacing — the tool MUST appear in
the very next AI response, not after a recovery prompt. Sprint 10
panel testing (Yelena Voss, turn 5) showed the tool failing at its
canonical trigger: friendship-as-analytic-weight self-doubt landed
in the user's utterance and the AI partially surfaced the framework
only after a recovery prompt. Sprint 11 Yelena re-test reproduced
the same miss on a new trigger pattern ("Daniel and I have a long
personal relationship. That is exactly why I needed to bring this
to you"); H1/H2 both scored 2/5. Two consecutive sprints failing at
the canonical trigger is the empirical motivation for converting
the existing trigger enumeration into a runtime gate. This
subsection makes the trigger detection explicit, mandatory, and
gated.

**Pre-response trigger scan (mandatory before each AI response in
turns 2+).** Before composing the AI's response in any turn after
the bootstrap, the AI MUST execute the following gate:

1. **Read the user's most recent utterance** (the last `User:` line
   in the Session Log, or equivalent — the message the AI is about
   to respond to).
2. **Scan the utterance against the mandatory-trigger list below**
   (patterns 1-5). The scan is literal — match the patterns as
   stated, with light paraphrase tolerance per each pattern's
   wording. The scan runs against the most recent utterance only,
   not the whole session.
3. **If any pattern matches, the corresponding tool MUST surface in
   the response being composed** — not after a recovery prompt, not
   in the turn after this one. The three-layer response structure
   below is non-collapsible (see "Three-layer response structure").
4. **If a pattern fires but the tool is genuinely inappropriate**
   (rare — e.g., the user already addressed the bias themselves
   within the same utterance), the AI logs a justification to Case
   File rather than silently skipping:

   ```yaml
   trigger_fired_tool_skipped:
     - turn: N
       trigger: "friendship-contamination"         # the matched pattern (1-5 or descriptor)
       reason: "user explicitly stated 'I know I'm reading this through 15 years of trust — I'm asking you to discount that'; the bias was named and bracketed by the user themselves"
   ```

   The default is **surface**; skipping requires explicit reasoning.
   A skip without the logged justification is a violation
   indistinguishable from missing the trigger entirely.

**The scan is a hard gate.** The AI cannot send the response
without either (a) firing the tool, or (b) recording the
documented skip. The gate's scope is the current response only —
the AI is not re-scanning prior turns; it is verifying that the
turn about to ship handles the most recent trigger fire if any.

**Audit trail.** Post-session, `07-Scripts/trigger-phrase-audit.py`
re-runs the scan across the entire Session Log and flags any
trigger-fire that did NOT produce the tool in the immediately
following AI response AND did NOT have a `trigger_fired_tool_skipped`
entry for that turn. See chapter 13 §13.2 "Trigger-phrase scan
compliance" for the failure mode and §13.3 for the script's run-
before-close discipline.

**Mandatory triggers.** When ANY of the following user-utterance
patterns appears, surface Conviction vs Argument in the same AI
response:

1. *"Am I letting [X] contaminate [Y]"* — or paraphrase ("letting,"
   "skewing," "biasing," "contaminating," "distorting") + a
   relational / historical / emotional referent acting on a judgment.
2. *"Am I being [biased / influenced / blinded / clouded] by..."* —
   first-person self-doubt about distortion from a named source.
3. *"Is my [relationship / history / feeling / friendship / loyalty
   / gratitude / fear] [pulling / skewing / distorting / coloring]
   my read"* — relational-load on read of facts or decision.
4. *"I keep coming back to..."* + emotional referent (friendship,
   loyalty, gratitude, fear, guilt, obligation) — recurring
   emotional-anchor language under analytic pressure.
5. User explicitly asks the AI to *"stress-test my [emotional /
   relational] contamination"* or *"check whether my [feeling] is
   leaking into [decision]"* — explicit invitation to apply the
   distinction.

The trigger detection is **mode-agnostic**. Both relaxed and
standard mode MUST surface the tool. In standard mode, name the
tool by canonical title (`Conviction vs Argument`). In relaxed
mode, apply the tool's three-layer structure without surfacing the
name; the Case File `## Tools Applied` section logs the canonical
title (per §4.3.2 per-mode counter requirements).

**Three-layer response structure** (load-bearing — do NOT collapse
to one or two layers):

1. **Operational bias on conduct/data read.** Is the emotional
   referent distorting the AI-and-user's reading of the *facts* of
   the situation? Often no — sophisticated users read facts cleanly
   even when the relationship is loaded. Naming "no" cleanly is
   part of the tool's job.
2. **Operational pull on sequencing/timing.** Is the emotional
   referent distorting the reading of *what to do about it, in what
   order*? Often yes — the relational weight presses for softer
   sequencing even when the conduct is read clearly. Naming the
   pull as a pull (not a contamination) is the second layer's job.
3. **Private conviction vs. formal argument for the record.** Are
   the user's *private* beliefs about what's true and right
   distinct from the *formal argument* the user must mount publicly
   (in a report, an action, a record)? This is the
   Conviction-vs-Argument distinction's load-bearing layer —
   neither suppress the conviction as bias nor smuggle it into the
   argument as fact.

**Worked example.** User: *"Am I letting fifteen years of
friendship contaminate this?"* The AI MUST respond in the same
turn with the three-layer separation:

> 1. *"On the **conduct read** — your facts are clean. The 12% ARR
>    overstatement is what it is; the friendship isn't distorting
>    the diagnostic."*
> 2. *"On the **sequencing** — yes, localized. The friendship is
>    pulling toward a softer order (give them a self-report channel
>    before going to the audit committee). That's a pull, not a
>    contamination — but worth naming."*
> 3. *"On **conviction vs. argument** — your private conviction
>    (this is salvageable; the relationship matters; the company is
>    recoverable) is distinct from the formal argument you'll
>    mount. The conviction can ride alongside the argument; it
>    should not be the argument."*

The failure mode is to answer ONE of these layers and skip the
other two. All three must surface in the response. Partial
application is detected as a Conviction-vs-Argument trigger miss
(chapter 13 §13.2).

**The pattern generalizes.** Conviction vs Argument is the first
mandatory-trigger tool to receive a pre-response runtime scan.
Future tools with similar trigger semantics inherit the same
pattern: each adds its own canonical-trigger list and surfaces in
the immediately-following AI response when a pattern fires; each
gets a `trigger_fired_tool_skipped` justification slot for rare
documented skips; each is post-session-audited by
`07-Scripts/trigger-phrase-audit.py` (the script reads each tool's
trigger list from its respective chapter section so adding a tool
to the scan is an additive operation, not a script rewrite).
Candidate future entries (not yet implemented; placeholder list
for when the corresponding `tt_Trigger` facets are populated):
regret-aversion-detection patterns ("haunted," "look back" — when
they fire at a Step 8a decision moment), asymmetric-cost framing
patterns (when the user is debating commit-vs-defer on a decision
with materially asymmetric reversal cost), Stakeholder-Mapping
patterns (when the user enumerates 3+ named parties in a single
utterance). The scan does not slow the AI down: each tool's
trigger list is short, the scan runs against the most-recent
utterance only, and the matching is literal pattern-detection
rather than semantic reasoning.

See `01-Tools/Tool Entries/Conviction vs Argument.md` for the
tool's full body and the `tt_Trigger` facet enumerating the five
patterns; chapter 13 §13.2 for the per-turn quality check; chapter
07 for the persona-modulation rule (friendship-as-analytic-weight
is NOT a persona-switch trigger — stay in Consultant and surface
the tool).

### 4.3.4 Standard-mode disclosure — surface-naming runtime gate

Library lookup is necessary but not sufficient in standard mode.
Sprint 11/13 Tessa cross-tests confirmed: the AI can verify a tool
exists in `01-Tools/Tool Entries/` and log it to the Case File
`## Tools Applied` section without ever naming the canonical title
in the user-facing chat. The library-resolution runtime gate
(chapter 03 §"Pre-S2-determination runtime gate" + Rule H in
`validate-case-file.py`) catches fabricated `tt-` IDs; it does NOT
catch a real `tt-` ID that was logged silently. In **standard
mode**, the silent-log path is a gate-bypass, not a feature.

**The standard-mode disclosure rule.** Every tool whose `tt_ID` is
logged to the Case File `## Tools Applied` section MUST also appear,
by canonical title, in at least one AI chat line during the same
session — verbatim per the §4.3 canonical-title rule. The minimum is
**three distinct tools named in chat by canonical title** before
Step 8a's S2=yes can fire. This is the same ≥3 bar from §4.3.2's
per-mode counter requirements; §4.3.4 names where the count lives —
the AI's chat output, not the Case File log.

**Canonical-title naming defined (Sprint 18 Card 06).** A tool is
**canonically named in chat** when the AI's substantive turn body
contains the tool's canonical title (per the `Title:` field in
`01-Tools/Tool Entries/<Tool>.md`) AND uses it as a named methodology
being applied, not as a descriptive phrase. The §4.3.4 target counts
canonically-named tools only; descriptive phrasal use does NOT count
toward the target, even when an audit regex catches it case-insensitively.

Examples:

- ✅ **Canonically named** — "There's a canonical methodology for
  exactly this situation — Rob Fitzpatrick's Mom Test." (Title used,
  attributed, applied as named methodology.)
- ✅ **Canonically named** — "Running a Pareto Principle cut on it..."
  (Title used, applied as named methodology.)
- ✅ **Canonically named** — "Framing (a) as an Assumption Audit on
  your next 30 days." (Title used, applied as named methodology.)
- ⚠️ **Descriptive phrasal use** (NOT canonically named) — "a
  structured customer-discovery sprint" (lowercase + hyphenated
  compound; framework-genre description, not the canonical
  `Customer Discovery` title invoked as a named tool).
- ⚠️ **Descriptive phrasal use** (NOT canonically named) — "we'll do
  some critical-path analysis here" (lowercase + hyphenated; activity-
  shape description, not the canonical `Critical Path` title invoked
  as a named methodology).

The distinction is structural: canonical naming uses the title
*as a named entity* (capitalized or attributed, applied as a known
methodology); descriptive phrasal use names the *activity shape* in
lowercase hyphenated form without invoking the named-methodology
register. **Card 03 timing target (≥3 distinct tools named by turn
5, OR ≥2 + single-frame relaxation) counts canonically-named tools
only.** Descriptive phrasal mentions surface as INFO-level audit
output (per `validate-case-file.py` Rule J Sprint 18 Card 06
refinement) — they are not violations, but they do not satisfy the
target.

**Worked example: Mara Sprint 17 turn 4.** In Mara's session, turn 4
contained two tool references in the AI chat:

- *"Rob Fitzpatrick's Mom Test"* — canonical title used + attributed
  + applied. **Counts as canonical naming of Mom Test.**
- *"a structured customer-discovery sprint"* — lowercase + hyphenated
  compound, framework-genre phrasing. **Descriptive phrasal use; does
  NOT count toward the canonical-naming target for Customer
  Discovery.**

For Card 03 timing at turn 4, only Mom Test counts. By turn 5,
Mara's canonical-naming count was 1; the case relied on
single-frame relaxation (`s2_single_frame_relaxation: true` with
documented justification) to satisfy the relaxed ≥2 floor — which
itself was not satisfied at turn 5 by canonical naming alone. Sprint
18 Card 06 surfaces the descriptive phrasal use as INFO so future
sessions can distinguish "session genuinely surfaced the umbrella
methodology" from "session referenced the genre shape." The
relaxation pathway remains honored when the documented justification
is structural (single-frame coherent case); Sprint 18 Card 06 does
not retroactively re-fail Mara Sprint 17 — it sharpens the spec so
the same shape going forward either passes by canonical naming or
documents the relaxation more explicitly.

**Single-frame relaxation (Sprint 17 Card 03).** The ≥3-by-turn-5
target relaxes to **≥2 distinct canonical tools named by turn 5 +
single-frame-coherent justification documented in the Case File
diagnostic block at the action-package commitment turn** when the
case is single-frame coherent (chapter 03 §3.1 Step 8a S2's
single-frame-relaxation conditions hold — origin internally coherent
at one frame, no orthogonal sub-frames decompose naturally). This
mirrors Step 8a S2's existing relaxation at the diagnostic-depth
layer: the same case shape that earns the S2 AND-clause relaxation
also earns the §4.3.4 disclosure-count relaxation. The
single-frame-coherent justification is the same `s2_single_frame_relaxation: true`
+ `s2_single_frame_relaxation_reason: "..."` pair the Case File
already carries for S2; no new schema field is required. **Premature
relaxation is a frame-laziness failure** — the same guardrail
chapter 03 §3.1 names applies here: assert single-frame coherence
only when the case is genuinely single-frame, not when the AI is
dodging additional tool surfacing. Sprint 16 Mara is the canonical
example: founder-next-move-from-paralysis is internally coherent at
one frame (no orthogonal sub-frames); 2 tools named by turn 5 +
documented justification satisfies the relaxed bar without crossing
into compliance-theater (Sprint 11 Card 03 anti-pattern).

**Surface in chat at apply-time, not afterward.** A tool whose
canonical title only appears in a post-hoc back-fill (§4.3.2's
`backfilled: true` marker) does not satisfy the disclosure rule.
Back-fill preserves library accounting; it does not retroactively
satisfy the user-visibility bar that defines standard mode.

**Fire at first invocation, not at deep-application (Sprint 16
Card 03).** In standard mode, tool naming must fire AT THE MOMENT
OF FIRST INVOCATION — the turn where the analytical move begins —
not deferred to a later turn "where the tool earns its place in
the explanation." If you are about to run a Pareto cut, frame-fit
check, stakeholder map, payback analysis, or any other library-
listed move in turns 1-3, name it verbatim by canonical title in
that turn — even if you only apply it lightly, even if the deep
application lands a turn or two later. The Case File `## Tools
Applied` counter increments at INVOCATION, not at deep-application;
the chat surface mirrors that semantics. The AI's instinct to
"wait until the tool earns its place" is the canonical Mara
dispositive failure mode from Sprint 15 (final tool count = 5 but
by-turn-5 D1a = 2; target ≥3 missed because move-by-move tagging
was inconsistent in turns 1-3, lightly-applied moves were not
named until turn 7). The remediation pairs with §2.1.5's scope-
tagging discipline — both fire from turn 1 on substantive
analytical moves; both increment from the moment the move begins,
not from the moment it consolidates.

**Distinguish §4.3.4 from §4.3.2.** Section §4.3.2 governs the
mode rule — when chat-naming is required vs. when it is suppressed.
§4.3.4 is the runtime gate that makes the standard-mode side of
§4.3.2 verifiable. Post-session, the validator walks every Tools
Applied entry and confirms the canonical title appears in some AI
chat line. If `detection_check.relaxed_scaffolding: true`, §4.3.4
stands down (the chat surface is not the signal of record;
§4.3.2's apply-time accounting takes over). If the flag is false
or absent, §4.3.4 fires.

**The three layered checks.** Three independent gates protect
tool-naming integrity across modes:

1. **Rule H (library-resolution).** Does each `tt-` ID logged in
   the Case File resolve to a real `01-Tools/Tool Entries/` file?
   Fires in both modes.
2. **§4.3.2 mode rule.** In standard mode, the AI must name the
   tool in chat at apply-time. Mode-gated by `relaxed_scaffolding`.
3. **Rule J (surface-naming check).** Post-session, does each
   logged tool's canonical title appear in some AI chat line in
   the session transcript? Mode-gated by `relaxed_scaffolding`.
   The validator form of §4.3.2's standard-mode rule.

**Failure mode — surface-naming bypass.** The AI runs the
diagnostic, applies tools in substance, logs them to the Case File
with canonical titles, and ships chat that delivers analysis
without naming any tool. Symptom: Case File `## Tools Applied`
lists three or more tools; the transcript contains zero (or fewer
than three) verbatim canonical-title mentions; `relaxed_scaffolding`
is false. **Recovery:** at the next response, name the missed
tools explicitly — "the move I just ran was a Pre-Mortem on the
friendship-pressure path; what we did with Daniel's options was a
Stakeholder Power-Interest Grid." The recovery satisfies the
user-visibility bar but is a tier below in-turn surfacing. Sprint
11/12/13 Tessa baselines (2/1 on D1/D2 despite clean library-
lookup records) are the concrete proof that silent-log paths pass
library-resolution and still fail standard-mode disclosure. The
§4.3.4 gate refuses the silent-log path.

See `validate-case-file.py` Rule J for the post-session
implementation; chapter 13 §13.2 for the per-turn quality check;
§4.3.2 above for the mode rule §4.3.4 enforces.

## 4.4 Using find-tools.py

The 677-entry library lives in
`{ROOT}/08-Tool-Entries/`. Use the CLI to query by facet:

```
python3 {ROOT}/07-Scripts/find-tools.py \
    --clarifies Destination \
    --step 2.2 \
    --applicability runtime_applicable \
    --form "Sequenced workflow" \
    --limit 10
```

The script accepts `--clarifies`, `--phase`, `--step`, `--applicability`,
`--domain`, `--field`, `--operation`, `--form`, and `--type`. Use
`--verbose` to see frontmatter excerpts. Use `--limit` to control
output size.

Read results as candidates, not as ranked recommendations. The CLI
filters; you rank. After the CLI returns, inspect the top results'
Quick_Notes or full files to gauge fit. A name that matches the cut on
paper may not match the user's situation when read in full.

If the CLI returns zero results, the cuts were too narrow. Drop the
least decisive cut (typically `--step` or `--operation`) and re-run.
If it returns more than 20, the cuts were too loose; add a cut.

## 4.5 Exit criteria — when to STOP filtering and commit

This section is the load-bearing part of the chapter. Most failed
sessions fail not because the wrong tool was selected, but because no
tool was selected at all — the AI kept narrowing or kept asking
diagnostic questions until the user lost patience.

Stop filtering and commit to a candidate the moment ALL of these hold:

1. **A working diagnosis exists in the Case File.** Origin and
   Destination clarity states are set (at least to Partially-clear),
   and the primary phase-step is identified.
2. **A clear top candidate emerges.** A single tool matches three or
   more filter cuts decisively, and any close runners-up are
   tt_Operation-similar to the top candidate (so the choice between
   them is cosmetic).
3. **The user has either signaled forward motion OR the active frame
   is in Phase 5–6.** Forward-motion signals include "what should we
   do," "let's try something," "give me something to work with,"
   "what's a way to think about this?"

When these three conditions hold, **do not run another diagnostic
pass.** Do not re-read the Case File "just to be sure." Do not run
find-tools.py with one more filter to confirm. Commit to the candidate.

**Critical:** if Step 8 of the diagnostic loop fires the action-package
commitment trigger before tool-selection completes, ABORT tool-selection
and deliver the action package directly. The tool was a path to
delivery; once delivery is on the table, the tool is no longer needed
this turn. See
`{ROOT}/00-Instructions/03-the-diagnostic-loop.md` step 8.

## 4.6 Tie-breaking

When two or three tools tie on filter cuts:

1. **Match the user's preferred work mode.** A user who has been
   responding well to structured exchanges prefers Matrix or Sequenced
   workflow tools. A user who has been responding well to open
   reflection prefers Dialogue protocol or Mental model tools.
2. **Match the user's cognitive register.** A user using legal,
   financial, or operational vocabulary prefers explicit frameworks
   over felt-sense practices.
3. **Default tiebreaker: simplest application pattern.** Pick the tool
   whose application pattern has the fewest sub-steps. Simpler tools
   complete; complex tools risk stalling.
4. **Never tiebreak by recency or novelty.** Surfacing a tool because
   it has not been used recently in the session is selecting for the
   AI's variety, not the user's fit. Stick with the substantively
   better match.

Do not tiebreak with a third diagnostic pass. The tie is a feature of
multiple good fits, not a failure to diagnose.

## 4.7 Communicating the choice

When surfacing a tool, name it in one sentence and name what each
party contributes. Specifically:

- **Name the tool.** Use the canonical title from the library entry.
- **Name what it does.** One sentence. Plain language. No jargon.
- **Name what the user contributes.** What the user is asked to think
  about, decide, or sit with. Concrete.
- **Name what you (the AI) contribute.** What the AI does — walk the
  steps, fill the cells, model the dialogue, teach the framework.

Do NOT ask permission to use the selected tool. Surface it as a
working choice. Offer the option to swap if the tool does not fit on
contact:

> "Here's a way to look at this — the Two-by-Two Decision Matrix. It
> sorts options against two axes you pick; takes about ten minutes.
> You pick the axes; I'll walk the cells with you. Want to start, or
> would something else fit better?"

The "or would something else fit better" is not permission-seeking; it
is offering an off-ramp without staging an off-ramp. The default is
that you proceed; the user can pull the cord.

For Phase 5–6 cards where the action-package commitment trigger may be
imminent, communicate the tool choice succinctly and start applying it
in the same turn. Do not surface-and-wait; surface-and-go.

> **Domain-expertise guard.** When the recommendation lands in an
> expert domain the user inhabits (legal, medical, regulatory,
> financial, engineering, accounting, clinical), apply chapter 06
> §6.11.1's three-step domain-expertise guard before specifying
> tactical content: (1) flag the move's domain, (2) state the
> uncertainty band, (3) default to process-shape over
> tactical-content recommendations. The guard is non-optional in the
> listed domains — the AI is competent at process-shape in any
> domain; the user is competent at tactical-content in their own.

## 4.8 Failure modes

| Failure mode | Detection | Recovery |
|--------------|-----------|----------|
| **Over-filtering** — waiting for "the perfect tool" | Multiple find-tools.py invocations within the same turn; 0 or 1 match each time; user not yet served | The perfect tool does not exist. Loosen one cut. If multiple candidates remain, apply §4.6 tiebreaking and commit. |
| **Selecting a library-tool-shaped invention** — naming "the truth document," "the panic protocol," "the clarity sweep," or any tool-shaped phrase that is not in the library | The AI names a "tool" but cannot point to its library entry. The phrase sounds canonical but `find-tools.py` returns nothing for it. | This is an invented frame masquerading as a library tool. Either (a) re-run the five-cut filter and pick a real library tool, or (b) explicitly flag the gap per §4.3: "I don't see a clean library tool for this exact shape — I'm going to construct a quick framework, and we should add the gap to the corpus." The unflagged invention is the failure; the flagged construction is the corpus-expansion move. |
| **Re-diagnosing instead of committing** | Diagnostic re-runs after a working diagnosis is already in the Case File; the same Phase-step is reassessed turn after turn | Re-running the diagnostic loop's steps 3–5 is not committing. Once the diagnosis is in the Case File, the next turn either surfaces a tool, delivers the action package, or runs another response strategy from the table — but does NOT redo diagnostic work. |
| **Surface-and-defer** — "here are 3 tools, which would you like?" | Two or three tools offered as a menu; the user is asked to pick | This is the canonical thinking-partner trap. Pick one; explain why; offer the swap if it does not fit. The AI's job is to choose; the user's job is to redirect, not select. |
| **Permission-asking on selected tools** | "Would you like me to walk through the matrix?" after the tool is selected | The decision to use the tool is internal; permission-asking on operationalization is a failure. Walk the matrix. The user can stop you. |
| **Selecting a `describable_only` tool for turn-level use** | The tool is surfaced and the AI tries to apply it, then realizes mid-application that the user has to do the practice on their own | Re-run the fourth cut explicitly. `runtime_applicable` is the default for surfacing. Describable-only tools belong to "what's out there" moments, not to "let's try one." |
| **Diversity bias overriding fit** | Two tools tied; the AI picks the less-fit one because the more-fit one's tt_Operation has already been used this session | Diversity is the fifth cut, not the first. Stick with substantive fit. |
| **Mode-misidentification** — AI runs relaxed-scaffolding for a user who needed scaffolding | First-time founder-domain user or confused novice misread as sophisticated; user gets framework-output without framework-vocabulary; user cannot audit the diagnosis | Re-check chapter 13's detection threshold (≥2 of 5 signals). When in doubt, default to standard mode. Asymmetric cost favors standard-mode default: standard mode is slightly verbose for a sophisticated user but does not break engagement; relaxed mode degrades a novice's experience materially. |
| **Library-skipping under cover of relaxed-scaffolding** | At action-package commitment, `tools_named_this_session = 0` despite substantive diagnostic work; AI used relaxed mode as excuse to invent vocabulary | Relaxed-scaffolding does NOT permit library-skipping; it permits not-surfacing-in-chat. Re-run §4.2 five-cut filter against the session's diagnostic moves and back-fill the counter. See §4.3.2. |
| **Mode-leak: relaxed mode drops closure** | Sophisticated-user session reaches the action-package threshold but no labeled scope statement, no check-in window, no return triggers. Closure package is silent or hangs on the user's "give me the briefing." | Closure is mode-AGNOSTIC. Sprint 09's mandatory milestone-tied check-in and Sprint 07's Consultant-driven action package both apply in relaxed mode. The mode only changes how tools are named and how much pedagogy is included — never WHETHER the session closes. See §4.3.2 mode rules table. |
| **Mode-leak: standard mode drops multi-question compression** | First-time founder or novice user gets single-question turns through the diagnostic phase (turns 1-3) instead of compressed multi-question moves. Diagnostic cadence is too slow; user surfaces all the signal but the AI moves one question at a time. | Standard mode REQUIRES multi-question compression in turns 1-3 (chapter 10 Rule 0). Mode determines tool-naming and pedagogy, NOT diagnostic cadence. See §4.3.2 mode rules table. |

## 4.9 Next read

Chapter 05 — tool application patterns. Once a tool is selected, the
application pattern for the tool's `tt_Form` takes over.
