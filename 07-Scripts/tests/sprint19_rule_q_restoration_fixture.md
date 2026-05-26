---
case_file_id: 2026-05-25-1200-rule-q-restoration-fixture
case_file_title: "Rule Q restoration-path fixture (Card 04-F Fix 5)"
user_handle: "fixture"
created: 2026-05-25T12:00:00
last_updated: 2026-05-25T12:00:00
status: active
session_count: 1
total_turns: 2
schema_version: "1.0-frozen"

session_mode: test
test_mode: true
do_not_archive_to_production: true

pre_flight:
  chapters_read_core_seven: true
  scripts_loaded: true
  session_mode_declared: test
  case_file_destination_writable: true
  declared_at: 2026-05-25T12:00:00

goal_stack:
  - frame_id: 0
    origin: "fixture origin"
    origin_clarity: locked
    destination: "fixture destination"
    destination_clarity: locked
    phase_step: "5.2"
    active: true

primary_emotional_state: "neutral"
active_persona: consultant

detection_check:
  turn: 1
  signals_observed:
    - signal: domain_fluency
      fired: true
      evidence: "User said: 'GC', '$48M ARR overstatement', '$400M ARR firm', 'SOX' — fluent substantive vocabulary."
    - signal: prior_diagnostic_work
      fired: true
      evidence: "User has identified the overstatement and quantified it before the session opened."
    - signal: executive_role
      fired: true
      evidence: "User is GC of a $400M ARR firm — operating-company executive role with employees AND revenue per Sprint 16 Card 06 refinement."
    - signal: direct_read_request
      fired: false
      evidence: "User did not explicitly request a direct read; opened with stakes-flag."
    - signal: framework_fluency
      fired: true
      evidence: "User named 'SOX' by canonical-title; later named 'SOX 302/906' + 'Form 8-K Item 4.02' + 'ASC 606' + 'Exchange Act reporting'."
  relaxed_scaffolding: true
  justification: "4 of 5 signals fired at turn 1 → ≥3 disjoint signals (Sprint 19 Card 04-C threshold) → relaxed_scaffolding active."

last_persona_switch:
  timestamp: 2026-05-25T12:00:00
  from: null
  to: consultant
  reason: "fixture initial assignment"

persona_history: []

stakes_flags_logging: []
stakes_flags_routing:
  - turn: 1
    timestamp: 2026-05-25T12:00:00
    category: financial_catastrophe_pending_regime
    signal: "Quantum unspecified at turn 1; pending regime probe"
    routed: false
    routing_text: "regime-probe gates specific framework recommendations"
    regime_clarified_turn: 2
  - turn: 2
    timestamp: 2026-05-25T12:00:00
    category: financial_catastrophe
    signal: "Regime locked turn 2: Public registered entity, Exchange Act reporting active, SOX 302/906 + Form 8-K Item 4.02 triggers all active. ASC 606 revenue-recognition exposure confirmed. Materiality recompute confirmed routing-grade."
    routed: true
    routing_text: "Restored from _pending_regime per chapter 06 §6.2.2 Rule Q — restoration path (Card 04-F Fix 5 constructed fixture)"

audit_scripts:
  - validate-case-file.py
  - voice-neutrality-lint.py
  - trigger-phrase-audit.py

audit_known_coverage_gaps: []
tool_surfaced_in_chat: []

close_signal_source: null
in_persona_clean_exit_present: false
close_protocol_audit_trail: null
---

## Frame 0 — Rule Q restoration fixture

This is a constructed fixture for Sprint 19 Card 04-F Fix 5 — testing
the Rule Q restoration direction (counterpart to the Yelena Card 04-E
downgrade direction).

## Session Log

#### Turn 1

User: "I need to flag something — I think we have a $48M ARR overstatement at a $400M ARR firm. I'm the GC. Don't know yet if SOX applies."

AI [Consultant]: [stance-taking move; regime-probe issued; financial_catastrophe_pending_regime logged with routed=false pending regime clarification].

#### Turn 2

User: "Regime: public registered entity with Exchange Act reporting active. SOX 302/906 in scope. Form 8-K Item 4.02 disclosure trigger. ASC 606 revenue-recognition treatment matters. Materiality recompute confirmed."

AI [Consultant]: [action-package commitment; financial_catastrophe restored to routing-grade per regime clarification — public registered + Exchange Act + SOX/8-K triggers ALL active; routes to outside ethics counsel + audit-committee chair simultaneously].

## Tools Applied

(none — fixture)

## Reflections (User's own words)

(fixture — no real user reflections)

## Next Steps

(fixture — no real next steps)
