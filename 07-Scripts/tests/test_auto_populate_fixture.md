---
case_file_id: 2026-05-22-card05-auto-populate-fixture
case_file_title: "Card 05 auto-populate dispositive test fixture"
user_handle: "test"
created: 2026-05-22T12:00:00
last_updated: 2026-05-22T13:00:00
status: active
session_count: 1
total_turns: 4
schema_version: "1.0"
session_mode: test
test_mode: true
do_not_archive_to_production: true
goal_stack:
  - frame_id: 0
    origin: "x"
    origin_clarity: clear_but_unstable
    destination: "y"
    destination_clarity: clear_but_unstable
    phase_step: "1.1"
    active: true
primary_emotional_state: "neutral"
active_persona: consultant
last_persona_switch:
  timestamp: 2026-05-22T12:00:00
  from: null
  to: consultant
  reason: "initial"
persona_history:
  - turn: 1
    from: null
    to: consultant
    trigger: "initial"
    timestamp: 2026-05-22T12:00:00
stakes_flags_logging: []
stakes_flags_routing: []
audit_scripts:
  - trigger-phrase-audit.py
audit_known_coverage_gaps: []
# Sprint 18 Card 05 fixture: tool_surfaced_in_chat intentionally EMPTY.
# AI lines name "Mom Test" and "Assumption Audit"; auto-populate should
# append entries for both with turn numbers + verbatim evidence.
tool_surfaced_in_chat: []
detection_check:
  turn: 4
  signals_observed:
    - domain_fluency: true
    - prior_diagnostic_work: false
    - executive_role: true
    - direct_read_request: false
    - framework_fluency: false
  relaxed_scaffolding: false
  justification: "test fixture for Sprint 18 Card 05 auto-populate dispositive validation"
---

# Case File: auto-populate fixture

## Frame 0 — auto-populate dispositive

### Frame opened: 2026-05-22T12:00:00

## Session Log

### Session 1 — 2026-05-22

#### Turn 1

User: "How do I validate this customer assumption?"

AI [Consultant]: "Let me apply the Mom Test to surface the assumption-as-fact pattern in your pitch."

#### Turn 2

User: "And the business model?"

AI [Consultant]: "I'll run the Assumption Audit on the unit economics — that catches the same shape at the model level."

## Tools Applied

### Mom Test

Tool ID: tt-mom-test
Frame: 0
Step: 4.1
Surfaced: 2026-05-22T12:15:00
Applied: 2026-05-22T12:25:00
Completed: 2026-05-22T12:35:00
Status: completed

Input fed to tool:
Customer assumption to validate.

Output:
Surfaced 2 assumption-as-fact patterns.

User's reaction:
Acknowledged.

### Assumption Audit

Tool ID: tt-assumption-audit
Frame: 0
Step: 4.1
Surfaced: 2026-05-22T12:40:00
Applied: 2026-05-22T12:50:00
Completed: 2026-05-22T13:00:00
Status: completed

Input fed to tool:
Unit-economics inputs.

Output:
Identified 3 model assumptions to test.

User's reaction:
Acknowledged.

## Reflections (User's own words)

None.

## Next Steps

None.
