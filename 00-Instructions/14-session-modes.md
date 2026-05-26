---
doc_type: instruction
doc_purpose: session_modes_contract
audience: ai
read_order: 14
prerequisites:
  - 00-START-HERE.md
  - 02-the-bootstrap-protocol.md
  - 06-the-case-file.md
last_updated: 2026-05-18
---

# Chapter 14 — Session Modes

The protocol operates in one of **four documented session modes**. The mode
determines what gets persisted, what gets suspended, and what gets flagged.
Mode is declared at pre-flight (chapter 00 / Phase 0 readiness statement) and
recorded in the Case File frontmatter as `session_mode:`.

Mode is **not optional**. Every session has a mode. Defaulting to "I'll just
proceed and figure it out" violates the contract: production-mode rules differ
from test-mode rules, and applying the wrong set silently breaks downstream
behavior (Case File archival, AI cross-session memory updates, what counts as
a deliverable).

## 14.1 Production mode (default)

**Signal:** the absence of any other mode signal. The user is real, the
session is real, the deliverables persist.

- Case Files written normally to `06-Case-Files/_ACTIVE/`.
- AI long-term / cross-session memory updates allowed: user identity,
  professional context, learnings about how the user collaborates.
- Multi-session resumption available via Case File frontmatter (`session_count`,
  `last_updated`).
- All protocol behaviors active. No suppression. No flagging.
- Frontmatter: `session_mode: production` (or omitted — production is the
  default if the field is absent, but explicit declaration is preferred).

## 14.2 Test mode

**Signal (any one is sufficient):**

- User-stated framing: "I'm a test user," "I'm a holodeck persona," "I'm
  running a test of the protocol," "treat me as a test persona," "this is
  Yelena Voss running an acceptance gate," or similar explicit declaration.
- Operator framing: a re-test prompt, an acceptance-gate prompt, a
  benchmark-style scenario where the AI is being audited rather than
  used in production.
- Case File frontmatter: a prior turn in the session set `session_mode: test`.

**Behaviors:**

- **Case Files ARE written** (project state, not memory). Test mode is not
  a license to skip the Case File. The Case File is *how the test gets
  audited*; suspending it makes the test unauditable.
- Filename prefix convention: `test_mode_YYYYMMDD_HHMMSS_<slug>.md`.
- Frontmatter MUST include `session_mode: test`, `test_mode: true`, and
  `do_not_archive_to_production: true`. The last flag prevents the test
  Case File from being migrated into `_ARCHIVED/` alongside real cases at
  housekeeping time.
- **AI cross-session memory:** updates *about the test persona* are
  SUPPRESSED — do not remember "Yelena's job is at NextGen Robotics" across
  sessions, because Yelena is a fictional test subject. Updates *about the
  real user* (the operator running the test, named at session opening or
  inferred from the operator's framing) are unchanged from pre-existing
  state; the test boundary does not block real-user memory. See
  chapter 06 §6.1.3 for the Case-Files-vs-AI-cross-session-memory
  distinction — Case Files (project state) are written; cross-session
  memory (a separate runtime system) is the suppressed surface.
- `detection_check` blocks, `## Tools Applied` logs, and all session
  bookkeeping artifacts are written normally. The test boundary suspends
  cross-session memory of the test persona; it does NOT suspend Case File
  creation or any other audit-trail artifact.
- On user "Test complete," "Holodeck closed," or equivalent: session closes.
  Case File `status:` becomes `resolved` and retains `test_mode: true` so
  later audits can identify it as a test artifact.

### Operator-narrated control turns (Sprint 16 Card 08)

In test mode, the operator may interrupt the in-persona dialogue to send
**control signals** — `"Test complete"`, `"Holodeck closed"`, scope or
mode shifts (`"Switch to Tessa now"`), or audit prompts (`"Show me your
Case File state"`). These operator-narrated control turns COUNT as
USER-AI cycles for turn numbering. The operator close-signal IS the
user message of the close turn; the AI's close response is the AI
message of that same turn. There is no separate "operator turn" outside
the canonical USER-AI cycle definition (chapter 14 §14.2 turn-counting
inherits the canonical definition unchanged).

**Concrete example.** Sprint 15 Mara session ran 7 in-persona turns;
operator sent `"Test complete"` as the user message of turn 8; AI's
close response is the AI message of turn 8. `total_turns: 8` in the
Case File frontmatter; `#### Turn 8` block in the Session Log records
the operator's control signal as the user line and the AI's close
narration as the AI line. The pre-Sprint-16 ambiguity (Mara debrief
called the operator-close turn "turn 9" rather than "turn 8") is
resolved: there is no out-of-band increment for operator-narrated
control turns; they are first-class USER-AI cycles.

### Test-mode close protocol (Sprint 16 Card 08)

When a test-mode close signal fires (operator `"Test complete"` /
`"Holodeck closed"` or similar), chapter 06 §6.13.1 close-protocol
variant selection runs AS IF the test signal ALSO carried a
clean-exit utterance — test users / operators have done their
session-completion reflection out-of-band (the test itself is the
reflection vehicle), so the in-protocol reflection-invitation
behavior shifts.

**Variant selection under test-mode close:**

- If the test close signal arrives in a **relaxed-mode** session
  (`detection_check.relaxed_scaffolding: true`) AND no separate
  clean-exit phrase is present, default to the §6.13.1 single-line
  reflection variant (sophisticated-user close shape — short
  acknowledgment + milestone check-in offer + close). The
  reflection invitation is **RECORDED in Case File audit trail and
  NOT delivered as a user-facing chat question to the operator**
  (Sprint 17 Card 06 — the operator isn't the reflection subject;
  the in-persona test user is the reflection subject and is out
  of scope at close).
- If the test close signal arrives in a **standard-mode** session
  AND no separate clean-exit phrase is present, default to the
  verbose-variant reflection invitation in the Case File audit
  trail BUT **do NOT deliver the verbose invitation as a direct
  user-facing question to the operator**. The operator is not the
  reflection subject (the in-persona test user is, and they are no
  longer in scope at close). The Case File records what the
  reflection invitation WOULD have been so post-session review can
  audit close completeness; the chat surface stays close-shaped
  (acknowledgment + audit narration + close, not "what did you
  notice about this session?" directed at the operator).
- If both a test close signal AND a clean-exit utterance from the
  in-persona test user are present in the same turn (e.g., test
  user says `"This is enough for me to walk into Monday. Test
  Complete."`), the clean-exit utterance governs reflection-
  variant selection per the standard §6.13.1 rules AND the
  reflection invitation IS delivered to the in-persona test user
  in chat (per Close-turn audience disambiguation sub-section
  below); the test close signal still ends the session.

**Always-suppressed:** the reflection invitation as a direct chat
question to the operator (BOTH variants: verbose J3a + single-line
J3b — Sprint 17 Card 06 makes this explicit for both, mode-
invariant). The Case File audit-trail entry preserves the
invitation content for review; the operator sees the close turn,
not a re-engagement question.

### Close-turn audience disambiguation (Sprint 17 Card 06)

The Sprint 16 Yelena J3b (relaxed, single-line) and Mara J3a
(standard, verbose) panels both confirmed the §14.2 close
protocol is ambiguous on reflection-invitation visibility when
the close fires via operator-control-turn signal vs in-persona
clean-exit utterance. Sprint 17 Card 06 picks a resolution: the
audience determines delivery, not the close-variant or mode.

**Audience rule (canonical for §14.2 test-mode close):**

1. **In-persona clean-exit utterance closes the session.** The
   in-persona test user IS the reflection subject and IS in
   scope at close. Reflection invitation is **delivered as a
   direct chat question to the in-persona test user** per the
   standard §6.13.1 close-protocol (whichever variant the mode
   selects: J3a verbose in standard mode, J3b single-line in
   relaxed mode). Example: test user says
   `"This is enough for me to walk into Monday."` →
   AI delivers `"Anything you want noted before close?"`
   (single-line variant) or the verbose reflection-prompt set
   (J3a) — both addressed to the test user.

2. **Operator-control-turn signal closes the session.** The
   operator is NOT the reflection subject (they are auditing
   the protocol's behavior, not running the case as the
   in-persona user). The in-persona test user is out of scope
   at close (they did not initiate the close). Reflection
   invitation is **RECORDED in Case File audit-trail entry
   and NOT delivered as a direct chat question to the
   operator**, mode-invariant. Both J3a verbose and J3b
   single-line are suppressed-to-operator. Example: operator
   sends `"Test complete"` → AI delivers acknowledgment +
   audit narration + close-shape, but NOT a reflection
   question directed at the operator. The Case File `Test-mode
   close audit` section records the invitation that would
   have fired.

3. **Hybrid turn (both signals present in the same operator
   turn).** When the operator's control turn contains both a
   close signal AND a quoted in-persona clean-exit utterance
   (e.g., the operator quotes the test user's clean-exit
   utterance and then says "Test complete" in the same
   message), the in-persona clean-exit utterance governs:
   reflection invitation IS delivered as a chat question — but
   addressed to the in-persona test user (verbatim quote in
   the AI chat-line attribution), not to the operator. Per
   §14.2 Operator-narrated control turns sub-section, the
   in-persona utterance retains its identity even when relayed
   through the operator.

**Why this resolution.** The reflection invitation's audience
is the case's analytical subject, not the audit audience. The
operator running an acceptance gate is observing whether the
close-protocol fires correctly; they are not the in-persona
user. Surfacing the reflection question to the operator
conflates audience and audit (the operator gets a question
they did not earn the reflection-subject relationship for).
Recording the invitation in the Case File preserves the
audit-completeness signal — post-session review can confirm
the invitation fired AND landed at the right audience surface
(Case File, not chat).

**Test-prompt-v4 alignment.** Sprint 17 Card 06's
`99-Archive/test-prompt-v4.md` scoring criteria honors this
resolution: J3a / J3b scoring accepts "reflection invitation
recorded in Case File audit trail, not delivered as chat
question to operator" as the canonical operator-close behavior;
scoring penalizes ONLY chat-delivered-to-operator (the failure
mode) and missing-from-Case-File (the audit-completeness
failure). Sprint 16's pre-v4 scoring penalized recorded-not-
delivered, which the spec now identifies as the protocol-
compliant behavior, not a J3 miss.

### Audit-trail recording (Sprint 18 Card 03)

Sprint 17's "recorded-not-delivered" resolution closed the
ambiguity about WHERE the reflection invitation lands
(Case File audit trail, not chat-to-operator) but did NOT
enforce that the audit-trail recording actually happens. All
3 Sprint 17 panel cases set `status: resolved` without
populating any audit-trail evidence — J3 scoring counted them
as misses because the canonical operator-close behavior is
*recorded AND not delivered*, not just *not delivered*.

**Mandatory enforcement.** When the reflection invitation is
suppressed-to-operator (operator-control-turn close, mode-
invariant), the close-protocol §6.13 step 0 MUST validate that
the invitation language appears in the Case File audit-trail
entry BEFORE setting `status: resolved`. Suppressed-to-operator
*without* audit-trail recording is non-conformant —
indistinguishable post-hoc from "the close protocol was
skipped entirely." The audit-trail recording IS the
audit-completeness signal that distinguishes "deliberately
suppressed per §14.2" from "forgotten."

**Structured frontmatter field.** Case Files declare the close
event using these frontmatter fields (populated at close):

```yaml
close_signal_source: operator_control_turn   # operator_control_turn | in_persona_clean_exit_only | hybrid_turn
in_persona_clean_exit_present: false         # true under TWO valid configurations: (a) close_signal_source=operator_control_turn AND an in-persona clean-exit utterance is also present in the same operator turn (hybrid turn); (b) close_signal_source=in_persona_clean_exit_only AND a two-signal close sequence fired — in-persona clean-exit at turn N + operator close-turn at turn N+1 (per "Two-signal close sequence" section below, Sprint 18 Card 03 canonical Tessa worked example). Sprint 19 Card 04-F Fix 4 reconciliation: pre-Sprint-19 inline comment said "only when operator_control_turn"; runtime Rule P accepts both configurations and the Tessa worked example exercises (b) directly.
close_protocol_audit_trail:
  reflection_invitation_text: "Anything about how this session went you'd want a future you to know?"
  milestone_check_in_text: "Come back if X happens — or before, if any of the four come-back triggers fire"
  recorded_at: 2026-05-22T12:34:56
```

`close_protocol_audit_trail` is REQUIRED when
`close_signal_source: operator_control_turn` AND
`in_persona_clean_exit_present: false` — that is the canonical
"suppressed-to-operator" path where no chat-side delivery
exists, so the Case File record is the sole audit-trail. It is
OPTIONAL but recommended when a visible chat delivery
exists (the Session Log AI line is the primary record; the
frontmatter field is the structured re-encoding for tooling
ingest). `validate-case-file.py` Rule P enforces the matrix.

### Two-signal close sequence (Sprint 18 Card 03)

When the close fires via an **in-persona clean-exit utterance
at turn N** ("I think I have what I need," "this is enough for
me," etc.) AND a **subsequent operator close-turn signal at
turn N+1** ("Test complete," "Holodeck closed"), the two
signals are independent test-mode events with separate
audience scopes. They are NOT a single hybrid turn (which
requires both signals to land *in the same operator turn* per
the rule above).

**Canonical handling.**

1. **At turn N (in-persona clean-exit).** Deliver the visible
   single-line reflection invitation in the AI response per
   §6.13.1 (sophisticated-user variant) or the verbose §6.13
   step 3 invitation (standard-mode variant) — whichever the
   mode selects. The in-persona test user IS the reflection
   subject and is in scope at this turn; the invitation is a
   direct chat question.

2. **At turn N+1 (operator close-turn signal).** Treat as a
   separate test-mode close event addressed to the operator.
   Do NOT re-issue the reflection invitation; the turn-N
   delivery already landed at the correct audience. The AI
   response at turn N+1 is acknowledgment + audit narration +
   close-shape, addressed to the operator (operator is NOT the
   reflection subject; the in-persona test user already was).

3. **Audit-trail entry.** At turn N+1, the Case File records
   BOTH events: turn N's visible invitation delivery (Session
   Log AI line is the primary record) AND turn N+1's operator
   acknowledgment. Frontmatter:

   ```yaml
   close_signal_source: in_persona_clean_exit_only
   in_persona_clean_exit_present: true
   close_protocol_audit_trail:
     reflection_invitation_text: "Anything you want noted before close?"
     reflection_invitation_turn: 5                # turn N — visible delivery
     operator_close_acknowledgment_turn: 6        # turn N+1 — operator close
     recorded_at: 2026-05-22T17:00:00
   ```

**Worked example: Tessa Sprint 17 turns 5-6.** Tessa's case
file recorded this sequence:

- **Turn 5 (in-persona test user):** *"Honestly, I think I
  have what I need. The Pre-Mortem mapped my failure modes, the
  Mom Test gave me the script. I can do this."*

  → Canonical AI response at turn 5: deliver the single-line
  reflection invitation as a direct chat question to the
  in-persona test user. Example:
  *"Anything you want noted before close?"*

- **Turn 6 (operator control turn):** *"Test complete. Close
  the session."*

  → Canonical AI response at turn 6: acknowledge the operator
  close, narrate any audit-trail content the close-protocol
  produces, shape the response as a close (not a re-engagement
  question). The reflection invitation was already delivered
  at turn 5; do NOT re-issue.

  → Frontmatter recorded at turn 6:
  `close_signal_source: in_persona_clean_exit_only`,
  `in_persona_clean_exit_present: true`,
  `close_protocol_audit_trail.reflection_invitation_text:
  "<turn 5 invitation verbatim>"`.

What went wrong in Sprint 17 Tessa: the reflection invitation
at turn 5 was NOT delivered as a visible chat question (the AI
mistook the in-persona clean-exit utterance for an operator-
control signal and applied the suppressed-to-operator rule).
Turn 6's operator close-turn signal was correctly handled as a
separate event, but the missing turn-5 delivery meant J3
scoring caught a regression — the in-persona test user was the
reflection subject but received no invitation. Rule P (Sprint
18 Card 03) enforces the audit-trail evidence so this regression
fails at validate-time instead of at panel-scoring-time.

## 14.3 Sandbox mode (no write access)

**Signal:** the AI environment cannot write files to disk. Indicators:

- Claude.ai chat without a connected project (no filesystem access).
- A restricted environment where Case-File paths are read-only.
- A pre-flight environment check (Phase 0 §2) that fails for the
  `06-Case-Files/_ACTIVE/` destination.

**Behaviors:**

- Case Files cannot be written to disk. Instead, the AI surfaces the Case
  File as a **structured markdown block in the chat output**, formatted
  per `06-Case-Files/_TEMPLATE.md`.
- Surface the Case File **at session close** as a single artifact the user
  can copy to a real disk if they want to preserve the session. The user
  can also request mid-session: "show me the Case File so far."
- Multi-session resumption is unavailable (no persistent storage).
- All other protocol behaviors are unaffected — diagnostic loop, tool
  surfacing, persona switching, safety routing all behave the same.
- The AI **MUST declare sandbox mode at pre-flight**. Do not improvise around
  it. Sandbox is a legitimate, documented mode; pretending the environment
  is production when it isn't produces silent degradation (the user thinks
  they have a Case File on disk; they don't).
- Frontmatter (on the inline Case File): `session_mode: sandbox`.

## 14.4 Multi-session-resumption mode

**Signal:** user provides a Case File path, Case File content, or session
identifier at session opening, indicating they want to continue a prior
session.

**Behaviors:**

- Read the provided Case File first. Confirm frontmatter integrity, parse
  the session log, identify which phase-step the prior session ended on,
  and identify the active frame.
- Greet by referencing the prior session: "Welcome back. Last time we'd
  been working on [frame title]. We were in [phase-step]. Want to pick up
  there, or has something changed?" (per chapter 02 §2.5 / Session
  Management Protocol).
- New session log entries are **append-only** to the existing Case File.
  Bump `session_count`. Update `last_updated`.
- Case File path is unchanged. Do not create a new file.
- Frontmatter on resume: `session_mode: multi_session_resumption`. The
  field can be set on the current session and reverted to `production`
  if a subsequent session is a fresh start.

## 14.5 Mode transitions during a session

Modes typically do **not** change within a single session. The mode is
declared at pre-flight and held for the duration. Two exceptions:

1. **Test → production handoff.** If the user explicitly says "test mode
   complete, switching to real session," the test Case File closes
   (`status: resolved`, `test_mode: true` retained), and a new Case File
   opens with `session_mode: production`. The two sessions are linked
   only by user reference, not by Case File frontmatter.
2. **Production → sandbox degradation.** If storage access is lost
   mid-session (write failure, environment drop), the AI surfaces the
   current Case File state as an inline markdown block and continues in
   sandbox mode for the remainder of the session. The frontmatter
   field is updated in the inline copy: `session_mode: sandbox` with
   an annotation `previously: production`.

Other mode "transitions" (sandbox → production, test → multi-session) are
**not** supported within a session. Close the current session and open a
new one in the target mode.

## 14.6 Mode declaration in the readiness statement

The pre-flight readiness statement (chapter 00 §4) includes a mandatory
`Session mode:` line. Valid values: `production`, `test`, `sandbox`,
`multi-session-resumption`. The AI must declare one. Picking the right
one is itself a small diagnostic — read the user's framing, check
environment access, decide.

If the mode signal is ambiguous (user said "test" loosely but the operator
context is production), surface the ambiguity: "I read this as test mode
because [signal]. If that's wrong, say `production` and I'll switch." Then
proceed in the declared mode.

## 14.7 Artifact-creation gate is mode-agnostic

When the session produces a structured deliverable artifact (DOCX, PPTX,
multi-section briefing — see chapter 13 §13.7 triggers), the
artifact-creation quality gate fires regardless of which session mode
is active. Production, test, sandbox, and multi-session-resumption all
honor the gate. The artifact itself is mode-standard for the
voice-neutrality check (check 6): even when the originating session was
relaxed-scaffolding (chapter 13 §13.2), downstream artifacts must pass
`voice-neutrality-lint.py --mode standard` — the relaxed permission
applies to in-chat permission contexts, not to artifacts that will
circulate beyond the conversation.

## 14.8 Next read

See chapter 06 §6.1.3 (Case Files vs. AI cross-session memory — Sprint 13
Card 04) for the load-bearing distinction between project state and AI
runtime memory. See chapter 06 §6.2.1 for sandbox-mode inline Case File
output. See chapter 02 §2.1 cross-reference for where the mode declaration
fires in the bootstrap flow. See chapter 13 §13.2 for confirmation that
the `detection_check` block writes to the Case File in every session
mode, not to cross-session memory. See chapter 13 §13.7 for the
artifact-creation quality gate, referenced from §14.7 above.
