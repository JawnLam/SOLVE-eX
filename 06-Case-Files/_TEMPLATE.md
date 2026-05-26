---
case_file_id: YYYY-MM-DD-HHMM-user-slug
case_file_title: "Short title of the question being worked"
user_handle: "user"
created: YYYY-MM-DDTHH:MM:SS
last_updated: YYYY-MM-DDTHH:MM:SS
status: active        # active | paused | resolved | abandoned
session_count: 1
total_turns: 0
schema_version: "1.0-frozen"  # Sprint 18 Card 08 — v2.0 freeze. Adding new frontmatter fields requires schema-version bump + migration script per 00-Instructions/19-governance-and-quality.md.

session_mode: production              # production | test | sandbox | multi_session_resumption — see chapter 14
test_mode: false                      # set true only when session_mode == test (chapter 14 §14.2)
do_not_archive_to_production: false   # set true only when session_mode == test (prevents migration to production _ARCHIVED/)

# Sprint 19 Card 04-F Fix 3: Phase 0 readiness audit trail.
# Chapter 00 §4 (START_HERE Phase 0) + chapter 02 §2.6 require the AI
# to record pre-flight readiness state in this Case File frontmatter
# block. Per chapter 13 §13.10 Class C: pre-flight detail goes in
# THIS frontmatter block, NOT in the chat-visible readiness statement
# (which is user-facing prose only). Sprint 19 Cards 04-A + 04-B add
# CLASS_C_BANNED_PATTERNS that hard-fire on chat-surface leaks of
# the audit-trail fields below.
pre_flight:
  chapters_read_core_seven: true       # 00, 01, 02, 03, 06, 09, 13 (the "core seven" from chapter 00 §1)
  scripts_loaded: true                 # 07-Scripts/ validation tools available (or `false` for degraded mode)
  session_mode_declared: production    # production | test | sandbox | multi_session_resumption — mirrors `session_mode` above
  case_file_destination_writable: true # 06-Case-Files/_ACTIVE/ writable (or `false` for sandbox mode)
  declared_at: YYYY-MM-DDTHH:MM:SS     # ISO-8601 timestamp of readiness-statement turn

# goal_stack: per-frame state for the session. When setting
# `status: resolved` at session close, you MUST also flip
# `active: false` on the closed frame(s). validate-case-file.py
# Rule D fails the Case File when status=resolved coexists with
# any frame having active=true. The coupling is the AI's
# compose-time responsibility (chapter 06 §6.13 step 1);
# Rule D is the safety net, not the primary discipline.
# Sprint 17 retrospective: Rule D fired on all 3 panel cases
# (Yelena + Mara + Tessa) because the compose-time flip was
# skipped. Sprint 18 Card 04 closes the discipline gap.
goal_stack:
  - frame_id: 0
    origin: "[fill in: where the user currently is]"
    origin_clarity: unclear   # unclear | partially_clear | clear_but_unstable | locked
    destination: "[fill in: where the user wants to be]"
    destination_clarity: unclear
    phase_step: "1.1"
    active: true              # auto-flip to false when parent status: resolved (validate-case-file.py Rule D safety net)
    # parent_frame: N      # only for sub-frames

primary_emotional_state: "[fill in: short description of emotional baseline]"
active_persona: partner   # partner | counselor | therapist | guide | consultant

# Sprint 16 Card 09: last_persona_switch is now a structured object,
# not a bare timestamp. The four fields capture WHEN the switch
# happened, WHICH personas were involved (so the switch is auditable
# without scanning history), and WHY (so the trigger is preserved
# for post-session review). Persona-switch reasoning is load-bearing
# evidence for chapter 05 no-linger compliance and chapter 09 stakes
# routing — bare timestamps were lossy.
last_persona_switch:
  timestamp: YYYY-MM-DDTHH:MM:SS
  from: partner       # partner | counselor | therapist | guide | consultant | null (initial)
  to: consultant
  reason: "[short string — e.g., 'forward-motion signal at turn 5 (chapter 03 step 8 trigger)']"

# Sprint 16 Card 09: persona_history is the across-session trajectory.
# Each entry records a single switch in chronological order — the
# first entry is the initial assignment (from: null, to: <initial>),
# subsequent entries record each switch. Combined with
# last_persona_switch above, this lets post-session review trace
# the full persona arc without re-reading the Session Log.
# Each entry: { turn: <int>, from: <persona|null>, to: <persona>, trigger: <string>, timestamp: <iso8601> }.
persona_history: []
#   - turn: 1
#     from: null
#     to: partner
#     trigger: "initial assignment from chapter 02 opening"
#     timestamp: 2026-05-19T17:00:00
#   - turn: 4
#     from: partner
#     to: counselor
#     trigger: "stakes signal escalation (chapter 09 §9.2)"
#     timestamp: 2026-05-19T17:42:00

# Sprint 16 Card 09: stakes_flags is split into two parallel arrays
# distinguishing the runtime consumer.
#   - stakes_flags_logging: drives chapter 02 §2.1.5 framing only.
#     Logging-grade stakes are recorded but do NOT trigger §9.2
#     safety routing (e.g., financial_material_commitment without
#     reversibility-blocking properties).
#   - stakes_flags_routing: drives chapter 09 §9.2 safety routing.
#     Routing-grade stakes MUST trigger the safety routing path
#     (e.g., legal_jeopardy, financial_catastrophe, physical_harm,
#     irreversibility).
# Tessa Sprint 15 financial_material_commitment was logging-grade
# only; Yelena Sprint 15 legal_jeopardy + financial_catastrophe
# were routing-grade. Both arrays preserved if applicable; either
# may be empty.
stakes_flags_logging: []
stakes_flags_routing: []

# Post-session audit invocation list (chapter 06 §6.13 — Sprint 14 Card 05).
# Each entry is a script filename in 07-Scripts/. The AI MUST invoke
# 07-Scripts/post-session-audit.py against this Case File BEFORE
# producing the close turn; non-zero exit from any listed script must be
# surfaced in the close turn rather than silently passed.
audit_scripts:
  - validate-case-file.py
  - voice-neutrality-lint.py
  - trigger-phrase-audit.py

# Known script-coverage gaps (Sprint 17 Card 08 codification — replaces
# Sprint 16 Yelena's improvised version). Use this field when the
# close-time post-session audit catches a violation that is a SCRIPT
# COVERAGE GAP (lint regex / audit pattern set doesn't match what the
# spec authorizes), NOT a protocol violation. Distinct from
# `post_close_residual: true` (which marks genuine non-convergent
# protocol violations per §6.13 step 0 trigger conditions).
#
# Required fields per entry: script, flagged_phrase, mode, spec_status,
# gap_diagnosis, remediation_decision. Optional: line, user_invitation_present.
# Schema documented in 00-Instructions/06-the-case-file.md §6.13 step 0.1.
# validate-case-file.py Rule O extension validates required-field presence.
# post-session-audit.py recognizes documented gaps as INFO findings
# (overall exit 0 if gap-acknowledgment is sufficient).
audit_known_coverage_gaps: []
#   - script: voice-neutrality-lint.py
#     line: 144
#     flagged_phrase: "honest read"
#     mode: relaxed
#     spec_status: permitted   # permitted | required | forbidden
#     user_invitation_present: "give it to me straight"
#     gap_diagnosis: "INVITATION_PATTERNS regex doesn't match the 'give it to me straight' variant"
#     remediation_decision: "Not remediated in-Case-File per §6.13 step 0.1 — script gap, not protocol violation"

# Tool-surface annotations (Sprint 15 Card 07 — structural-vs-text-presence
# coverage gap closure).
# When the Session Log uses placeholder text for an AI turn (e.g.,
# "AI [Consultant]: [full verbatim response delivered in chat — see turn-N
# chat output]"), the trigger-phrase-audit.py text-presence scan cannot
# confirm tool surface from the placeholder alone. List each turn where a
# mandatory-trigger tool surfaced in the (out-of-band) chat output; the
# audit script accepts the annotation as an alternative verification path.
# Remove this stub or set to [] if no triggers fired / no placeholder turns
# used. Each entry: { turn: <int>, tool: <canonical_title_or_id>, evidence: <string> }.
#
# Sprint 17 Card 05: populated automatically by
# `python3 07-Scripts/trigger-phrase-audit.py --auto-populate <path>`
# before composing the close turn (chapter 06 §6.13 step 0.4). The
# auto-populate scans `## Tools Applied` H3 entries + AI chat lines for
# canonical-title matches and appends entries derived from the chat
# surface. Manual edits are permitted but should be flagged in the
# close-turn audit-trail (mark `source: manual` to distinguish from
# auto-populated entries). The coupling-check (Sprint 17 Card 05) gates
# the close audit on every Tools Applied entry having a matching
# tool_surfaced_in_chat entry OR an `[ad-hoc]` exemption marker.
tool_surfaced_in_chat: []
#   - turn: 3
#     tool: "conviction-vs-argument"
#     evidence: "canonical phrase 'the Conviction-vs-Argument three-layer pass' used explicitly with all three layers applied in chat output"

# Sprint 18 Card 03: close-protocol audit-trail recording (validate-case-file.py Rule P).
# Populated at close (status: resolved) per chapter 14 §14.2 Audit-trail recording
# sub-section + chapter 06 §6.13 step 0.6. Absent / null until close fires.
#
# close_signal_source — required when status=resolved. Enum:
#   - operator_control_turn       (operator sends "Test complete" or similar)
#   - in_persona_clean_exit_only  (in-persona test user signals clean exit)
#   - hybrid_turn                 (operator turn contains BOTH a close signal AND a quoted in-persona clean-exit utterance)
# in_persona_clean_exit_present — bool. Relevant only when close_signal_source=operator_control_turn:
#   - true   = hybrid two-signal sequence; in-persona clean-exit utterance arrived in a prior in-persona turn
#   - false  = canonical suppressed-to-operator path; no in-persona delivery available
# close_protocol_audit_trail — structured frontmatter capturing the audit-trail entry.
#   Required when close_signal_source=operator_control_turn AND in_persona_clean_exit_present=false
#   (suppressed-to-operator path — the audit-trail IS the only completeness signal).
#   Optional but recommended otherwise (the visible Session Log AI line is the primary record;
#   the frontmatter field is the structured re-encoding for tooling ingest).
close_signal_source: null
in_persona_clean_exit_present: false
close_protocol_audit_trail: null
# Example populated form (operator-only close, no in-persona — suppressed-to-operator):
# close_signal_source: operator_control_turn
# in_persona_clean_exit_present: false
# close_protocol_audit_trail:
#   reflection_invitation_text: "Anything about how this session went you'd want a future you to know?"
#   milestone_check_in_text: "Come back if X happens — or before, if any of the four come-back triggers fire"
#   recorded_at: 2026-05-22T12:34:56
#
# Example populated form (two-signal close sequence — in-persona then operator):
# close_signal_source: in_persona_clean_exit_only
# in_persona_clean_exit_present: true
# close_protocol_audit_trail:
#   reflection_invitation_text: "Anything you want noted before close?"
#   reflection_invitation_turn: 5
#   operator_close_acknowledgment_turn: 6
#   recorded_at: 2026-05-22T17:00:00
---

# Case File: [title]

## Frame 0 — [short title]

### Frame opened: YYYY-MM-DDTHH:MM:SS

### Origin (clarity state: unclear)

<!-- Origin narrative placeholder — replace with where the user currently is; populated and updated through Phase 1 work -->

### Destination (clarity state: unclear)

<!-- Destination narrative placeholder — replace with where the user wants to be; populated and updated through Phase 2 work -->

### Reasons to Resolve (Step 2.1)

<!-- Step 2.1 placeholder — replace with reasons-to-resolve content -->

### Goal Statement (Step 2.2)

<!-- Step 2.2 placeholder — replace with goal-statement content -->

### Requirements (Step 2.3)

<!-- Step 2.3 placeholder — replace with requirements content -->

### Current Facts (Step 3.1)

<!-- Step 3.1 placeholder — replace with current-facts content -->

### Past Facts (Step 3.2)

<!-- Step 3.2 placeholder — replace with past-facts content -->

### Systems Facts (Step 3.3)

<!-- Step 3.3 placeholder — replace with systems-facts content -->

### Future Facts (Step 3.4)

<!-- Step 3.4 placeholder — replace with future-facts content -->

### Root Causes (Step 4.1)

<!-- Step 4.1 placeholder — replace with root-causes content -->

### Ideas (Step 4.2)

<!-- Step 4.2 placeholder — replace with ideas content -->

### Anticipative Solutions (Step 4.3)

<!-- Step 4.3 placeholder — replace with anticipative-solutions content -->

### Refined Options (Step 4.4)

<!-- Step 4.4 placeholder — replace with refined-options content -->

### Evaluation Criteria (Step 5.1)

<!-- Step 5.1 placeholder — replace with evaluation-criteria content -->

### Decision Tool Used (Step 5.2)

<!-- Step 5.2 placeholder — replace with decision-tool content -->

### Validation (Step 5.3)

<!-- Step 5.3 placeholder — replace with validation content -->

### Design and Test (Step 6.1)

<!-- Step 6.1 placeholder — replace with design-and-test content -->

### Action Plan (Step 6.2)

<!-- Step 6.2 placeholder — replace with action-plan content -->

### Execution Notes (Step 6.3)

<!-- Step 6.3 placeholder — replace with execution-notes content -->

### Follow-up Review (Step 6.4)

<!-- Step 6.4 placeholder — replace with follow-up-review content -->

### Resolution / Pause / Abandon / Failure

<!-- Frame-closure placeholder — populated at frame closure -->

## Session Log

### Session 1 — YYYY-MM-DD

*Per-turn record. Append a `#### Turn N` block for each turn.*

#### Turn 1

User: "Verbatim user message (truncated to ~500 chars if longer)."

Diagnostic:
- Frame: 0
- Phase-step: 1.1
- Origin: unclear
- Destination: unclear
- Persona: partner
- Stakes flags: none
- Strategy: listen / mirror / probe

AI [Partner]: "Verbatim AI response."

<!-- Turn 2 placeholder — replace with turn content; append additional Turn N placeholder blocks as the session progresses -->

## Tools Applied

*Per-tool record. Append a block for each tool surfaced and applied.*

### [Tool Name]

Tool ID: tt-tool-slug
Frame: 0
Step: X.Y
Surfaced: YYYY-MM-DDTHH:MM:SS
Applied: YYYY-MM-DDTHH:MM:SS
Completed: YYYY-MM-DDTHH:MM:SS
Status: surfaced | applying | completed | abandoned

Input fed to tool:
<!-- Tool input placeholder — replace with what was given to the tool from prior work -->

Output:
<!-- Tool output placeholder — replace with what the tool produced -->

User's reaction:
<!-- Tool user-reaction placeholder — replace with user's response to the tool's output -->

## Reflections (User's own words)

*Free-text reflections from the user across the session(s).*

## Next Steps

*Notes for resumption or for after the session closes — what to do, what to think about, what to come back to.*
