---
doc_type: instruction
doc_purpose: cross-chapter-dependency-index
audience: ai
read_order: 0.5
last_updated: 2026-05-18
---

# Cross-Chapter Operational Dependencies

This index lists every cross-chapter `§`-reference in the
`00-Instructions/` corpus. References are tagged:

- **OP (operational)** — reading the source section requires having read the
  target section. If the target chapter is not in your **core seven** pre-flight
  reads (chapters 00, 01, 02, 03, 06, 09, 13), you must load it on-demand
  before executing the source section.
- **DOC (documentation)** — a "see also" pointer. Read on-demand only when
  you need to consult the target for additional detail.

Generated initially from a one-pass audit of cross-chapter
`chapter N §M.O` references using
`07-Scripts/cross-chapter-dependency-audit.py`. Maintained by hand thereafter:
when a new chapter §-reference is added, add an entry here in the appropriate
group; when a section is renumbered or deleted, update the matching entries.
The audit script ensures all references still resolve; this index records
which ones gate behavior.

If a cross-reference exists in the corpus but is NOT listed here, treat it as
DOC. The default is the looser semantics; OP must be explicit.

---

## Source chapter 00 (START-HERE / pre-flight)

- §1 mandatory reads [OP] → chapter 13 §13.2 (`detection_check` block format —
  required to satisfy the §5 session-opening checklist item 5)

## Source chapter 02 (bootstrap protocol)

- §2.3 / mode rule [OP] → chapter 04 §4.3.2 (mode rules govern tool-naming and
  pedagogy after `relaxed_scaffolding: true` fires — the bootstrap cites mode
  rules but mode rules live in ch.4)
- §2.6 / Initialize Case File [OP] → chapter 06 (the Case File schema, write
  rules, and section structure live in chapter 06; chapter 06 §6.6
  resumption protocol is OP for returning users)
- §2.10 / first turn safety pass [OP] → chapter 09 (stakes routing categories)

## Source chapter 03 (diagnostic loop)

- §3.1 / clarity states [OP] → chapter 01 §1.2 (four clarity states are the
  Phase-Step diagnostic primitives)
- §3.1 step 8 / tool-naming branch [OP] → chapter 04 §4.3 (corpus-gap protocol
  + `[ad-hoc]` marker convention) and chapter 04 §4.3.2 (mode rules govern
  what the tool branch does)
- §3.1 step 8a / single-frame relaxation [DOC] → master plan Part 4.5 (Sprint
  10 Tessa codification; not a chapter cross-reference)

## Source chapter 04 (tool selection)

- §4.2.X / two-tool composition [DOC] → chapter 05 §5.6 (composition rules
  live in ch.5)
- §4.3 / Case File bookkeeping [OP] → chapter 06 §6.3 (foreground vs.
  background determines what counts as a named tool)
- §4.3 / per-turn trigger-phrase scan [OP] → chapter 13 §13.2 (the quality
  check that fires when a trigger phrase is detected; multiple references)

## Source chapter 05 (tool application patterns)

- §5.2 / affinity-ranker procedural requirement [OP] → chapter 04 §4.2.1
- §5.2.X / communicating choice [DOC] → chapter 04 §4.7
- §5.2.1 / tools-named baseline [DOC] → chapter 04 §4.3.1

## Source chapter 06 (Case File)

- §6.1 / first substantive user message [OP] → chapter 02 §2.6 (initialize on
  first substantive message)
- §6.1 / failure modes [OP] → chapter 13 §13.2 (per-turn check that catches
  Case-File-related quality failures)
- §6.7 / session close [DOC] → chapter 02 §2.12 (success path of the
  bootstrap closes via the §2.12 protocol)
- §6.11 / domain-expertise gate (clinical detection) [OP] → chapter 13 §13.2
  (the domain-detection rule cites the §13.2 sophisticated-user signal stack)
- §6.13 / close-protocol variant [OP] → chapter 04 §4.7 (communicating-the-
  choice protocol) and chapter 13 §13.2 (variant-misapplication failure mode)

## Source chapter 07 (persona modulation)

- §7.3 / friendship-as-frame trigger [OP] → chapter 04 §4.3.3 (tool-surfacing
  protocol that fires when persona switches to Friend)

## Source chapter 08 (question banks)

- §8.2 / compression default [DOC] → chapter 10 §10.2 (Rule 0 governs
  compression decisions across all retrieval-based responses)
- §8.X / parallel principles [DOC] → chapter 04 §4.3

## Source chapter 09 (safety and stakes)

- §9.X / specific guards [DOC] → chapter 06 §6.11 (domain-expertise guards)
- §9.X / Case File defaults [DOC] → chapter 06 §6.8 (local-only storage default)

## Source chapter 10 (session management)

- §10.2 / Therapist-locked branch [DOC] → chapter 11 §11.4 (distinguishing
  meta from on-topic during therapist mode)
- §10.3 / diagnostic-to-delivery transition [OP] → chapter 03 §3.1 step 8
  (action-package commitment trigger)

## Source chapter 11 (meta-conversation)

- §11.2 / action-package commitment trigger [OP] → chapter 03 §3.1 step 8

## Source chapter 12 (edge cases)

- §12.X / user objects to chosen tool [OP] → chapter 03 §3.1 step 8 (re-read
  the step 8 logic when the chosen tool gets pushback)

## Source chapter 13 (quality checks)

This chapter is the fan-in target: most chapters cite §13.2. Outbound
references:

- §13.2 / various failure modes [DOC] → chapter 12 §12.10, §12.11, §12.17
  (recovery patterns for specific failure modes)
- §13.2 / tool-library surfacing [DOC] → chapter 04 §4.3 (and several
  §4.3.3 entries for trigger-phrase patterns)
- §13.2 / journey-shape check [OP] → chapter 02 §2.1.5 (stakes-scaled shape
  statement)
- §13.2 / compression Rule 0 [DOC] → chapter 10 §10.2, §10.5
- §13.2 / sophisticated-user close-protocol [OP] → chapter 06 §6.13.1 (the
  decision table Sprint 11 Yelena introduced; Sprint 13 Card 09 deliverable)
- §13.2 / question-bank-empty branch [DOC] → chapter 08 §8.5
- §13.2 / friendship-as-frame trigger [DOC] → chapter 04 §4.3.3, chapter 07
  §7.3 (cross-references to the Sprint 11 Conviction-vs-Argument pattern)
- §13.2 / clinical domain-expertise gate [OP] → chapter 06 §6.11.1 (the gate
  spec) and chapter 04 §4.7 (communicating the recommendation)
- §13.2 / Case File foreground-vs-background [DOC] → chapter 06 §6.3 (Yelena
  test reference)
- §13.X / pre-close residual check [DOC] → chapter 06 §6.13

---

## How to use this index

1. **At pre-flight (Phase 0):** the core seven (00, 01, 02, 03, 06, 09, 13) are
   read in full. This index helps you predict when an on-demand chapter (04, 05,
   07, 08, 10, 11, 12, 14) will need to be loaded — scan for any OP entry
   targeting an on-demand chapter and pre-load it if you expect the source
   section to fire this session.

2. **During execution:** when you encounter a cross-chapter `§`-reference inline
   in a section you're executing, check this index:
   - If marked OP and the target chapter is not yet in working memory, **stop**
     and read the target before proceeding.
   - If marked DOC, you may read on-demand or defer.

3. **When the audit catches a broken reference:** run
   `python3 07-Scripts/cross-chapter-dependency-audit.py`. If it reports a
   broken reference, fix the source citation (the section it cited has been
   renumbered or removed) before continuing. Update this index entry to match.

4. **When adding a new cross-reference to a chapter:** add an entry here under
   the source-chapter group, with the appropriate OP/DOC tag.
