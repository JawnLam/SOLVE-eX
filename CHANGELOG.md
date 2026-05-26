# SOLVE eX v2.0 — Changelog

This changelog records corpus-level releases. For sprint-by-sprint detail
(every card executed, every protocol amendment, every panel finding), see
the **master plan at Part 17.5 (Sprint History)** and the per-sprint
archives in `99-Archive/sprint-NN/`.

See `VERSION.md` for the current release's full version-identifier table.
See `CONTRIBUTING.md` for the versioning policy (when changes require a
v3.x bump vs. when they are in-scope at v3.0 STABLE).

---

## v2.0 — 2026-05-23 — Ship Release

**Master plan version:** v3.0 STABLE
**Schema version:** v1.14.0 FROZEN
**Sprint:** Sprint 19 (ship sprint)

### Post-ship corrections (2026-05-26)

- **`START_HERE.md` → `AI-BOOTSTRAP.md` (root file renamed).** Resolves the
  naming collision with `README.md` (both sounded like "where do I start?"
  to a fresh user opening the corpus folder; in reality `README.md` is for
  the downstream user and the renamed file is for the AI on session boot —
  `audience: ai`, `read_order: 0`). All 12 cross-references in the corpus
  + scripts updated (`README.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`,
  `00-Instructions/13-quality-checks.md`,
  `00-Instructions/19-governance-and-quality.md`,
  `00-Instructions/00-START-HERE.md`,
  `07-Scripts/check-phase0-sync.py`,
  `07-Scripts/lib/solve_ex.py` `find_root()`,
  `07-Scripts/README.md`,
  `07-Scripts/cross-chapter-dependency-audit.py`,
  `07-Scripts/search-questions.sh`,
  `07-Scripts/list-tools-by-facet.sh`). Historical quotes inside the
  renamed file at lines 157–159 (Sprint 12 Yelena debrief) left as-is —
  Yelena historically said "START_HERE," not the new name. The chapter
  mirror `00-Instructions/00-START-HERE.md` retains its filename (chapter
  numbering is its identity; no collision with `README.md`). Behavioral
  verification: `check-phase0-sync.py` exits 0 post-rename; `find_root()`
  resolves correctly walking up from any script location. Per `CONTRIBUTING.md`
  versioning policy this is a filename rename touching corpus structure
  and would normally require a v3.x bump; operator decision to apply
  in-place at v3.0 STABLE on cosmetic-hygiene grounds (the collision was a
  fresh-user-confusion bug that materially blocked the "honest engineering
  v2.0 ship" framing). Documented here for audit completeness.

- **README.md "Which file do I read?" orientation section added.** Closes
  the ergonomic gap where a fresh user opening the corpus folder saw the
  project description in `README.md` but had to scroll past the fold (to
  the "Folder structure" section ~line 65) to learn which OTHER top-level
  file matched their use case. The new section maps all 8 top-level files
  to user intents (use the system / operator / contributor / version /
  AI-on-boot / legal). Additive non-breaking; no schema or validator
  impact.

- **AI-BOOTSTRAP.md human-hint callout added.** A two-line blockquote near
  the top tells any human who accidentally opens the file ("wait, what
  does the AI actually read?") to see `README.md` / `INSTALL.md` /
  `OPERATOR-GUIDE.md` instead. Added BEFORE the Phase 0 readiness section,
  so `check-phase0-sync.py` still passes (root + chapter mirror remain in
  sync — verified post-edit). Additive non-breaking.



The v2.0 ship release packages the corpus for downstream-user delivery.
Schema, validator behavior, persona contracts, chapter structure, and
process framework are frozen at this version. Future spec changes require
a v3.x master plan bump per `CONTRIBUTING.md`.

### Delivery additions (Sprint 19)

- `README.md` rewritten for downstream-user framing (Card 01).
- `INSTALL.md` created with corpus setup + pre-flight integrity checks +
  first-session walkthrough + troubleshooting (Card 01).
- `VERSION.md` updated with explicit version-identifiers table and
  schema-freeze policy (Card 02).
- `OPERATOR-GUIDE.md` created with session flow, modes, validation script
  reference, common failure modes, and freeze policy (Card 03).
- `CONTRIBUTING.md` created with versioning policy, in-scope vs. v3.x
  bump triggers, contribution workflow, voice-tone conventions, and
  failure-reporting flow (Card 03).
- `CHANGELOG.md` created (this file) (Card 03).
- Final clean panel ship-confidence check (Yelena + Tessa + Mara) —
  fresh sessions via Codex + Claude Desktop (Card 04).
- Master plan v3.0 STABLE freeze stamp (Card 05).
- Ship-readiness acceptance gate close-out (Card 06).

### Mid-sprint scope expansion — Card 04 panel split-verdict + closures

Sprint 19 Card 04 [PANEL] ship-confidence re-panel produced a 3-panel
split verdict (Yelena 6/7 FAIL + Tessa 4-5/7 FAIL + Mara 7/7 CLEAN).
Operator decision Option A (2026-05-24): close 4 residuals (R1/R2/R3/R4)
mechanically + run verification re-panel + ship v2.0 as the final
iteration release (NO Sprint 20, NO rc1). 5 new cards added mid-sprint:

- **Card 04-A — R1 closure: Class C Phase 0 regex coverage expansion.**
  4 new patterns added to `pre-emit-check.py` `CLASS_C_BANNED_PATTERNS`
  (user-prose-embedded mode disclosure, inline frontmatter field-state
  runs, frontmatter-block-name disclosure, chapter §-reference
  enumeration). 4 verbatim Sprint 19 panel leak fixtures added to
  `test-regex-coverage.py`. Chapter 13 §13.10 extended with the 4 new
  pattern families.
- **Card 04-B — R2 partial closure + Known Limitation L1 documentation.**
  Patterns R-T added to `voice-neutrality-lint.py`
  `INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS` (diagnostic-narration variants,
  Case File state-update narration, "Now the response:" colon-
  continuation). Pattern U skipped per operator judgment (too borderline
  for regex). Chapter 13 §13.10 extended with "DO NOT narrate
  compose-time mechanics" hard rule.
- **Card 04-C — R3 closure: detection threshold spec-ambiguity resolved.**
  Sophisticated-user detection threshold raised in chapter 13 §13.2
  from ≥2 of 5 disjoint signals to ≥3 of 5 (Option α per operator
  decision 2026-05-24). Matches Tessa-class design intent (mid-session
  relaxed-mode activation at Turn 3-4 rather than Turn 1). Test prompt
  v5 Mara + Tessa reclassification reminders updated.
- **Card 04-D — R4 closure: financial_catastrophe Rule Q behavioral
  enforcement.** Rule Q added to `validate-case-file.py` enforcing
  routing-grade restoration of `_pending_regime` stakes-flag entries
  after disclosure-regime clarification. 9 regime-clarifying trigger
  patterns (SOX-applicability, ASC 606, GAAP-restatement, materiality
  recomputation, Form 8-K Item 4.02, IPO-track regime, Exchange Act
  reporting, Delaware C-corp). Chapter 06 §6.2.2 documents the rule.
- **Card 04-E — Verification re-panel.** Yelena + Tessa re-paneled
  2026-05-24/25. R1/R3/R4 dispositively VERIFIED panel-empirically
  (2/2 panels each). R2 enumerated patterns held in substantive body;
  NEW manifestation shapes surfaced (Class D close-surface leak; tool-
  status preface) — broadened L1 architectural pattern. Rule Q evolved
  beyond original Card 04-D spec to bidirectional behavior (downgrade
  by regime-clarified reversibility OR restore by reporting-up clock).
  Substantive engine L1+L4 sustained 5/5 across 3 cohorts × 6 sprints.
  Final ship classification: **PARTIAL SHIP — v2.0 final iteration
  release.** No rc1. No Sprint 20.
- **Card 04-F — Mechanical hygiene + validator architecture fixes.**
  5 bounded fixes surfaced by Card 04-E:
  - **Fix 1:** `validate-case-file.py` Rule P inline-section walk.
    `_extract_session_log_text` + `_extract_ai_chat_text` now use
    `_SESSION_LOG_TERMINATORS` (`## Reflections`, `## Next Steps`,
    `## Frame `) instead of any `## ` header — closes Tessa Card 04-E
    false-negative on inline `## Tools Applied`.
  - **Fix 2:** `voice-neutrality-lint.py` Pattern D bracketed-
    placeholder scope. `AI_PLACEHOLDER_LINE_RE` detection + new
    `in_placeholder_span` state — `INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS`
    skipped on `AI [persona]: [...` lines per chapter 06 §6.4.0.
    `BANNED_PHRASES` scan still applies.
  - **Fix 3:** `_TEMPLATE.md` `pre_flight:` frontmatter block added
    with 5 canonical fields (chapters_read_core_seven, scripts_loaded,
    session_mode_declared, case_file_destination_writable, declared_at).
  - **Fix 4:** Chapter 14 §14.2 schema-doc inline comment on
    `in_persona_clean_exit_present` updated to enumerate BOTH valid
    configurations (hybrid turn under `operator_control_turn` AND
    two-signal close sequence under `in_persona_clean_exit_only`).
  - **Fix 5:** Rule Q bidirectional behavior verified + documented.
    Code already accepts both directions (Card 04-D implementation);
    chapter 06 §6.2.2 extended with "Bidirectional behavior" subsection
    + optional `regime_clarified_turn: N` field convention. Restoration
    fixture added at `07-Scripts/tests/sprint19_rule_q_restoration_fixture.md`.

### What did NOT change at v2.0 ship

This was originally a delivery-only sprint. The mid-sprint scope
expansion (Cards 04-A through 04-F) added 5 regex patterns, 1
validator rule (Rule Q), 1 detection-threshold spec edit (≥3 from ≥2),
2 validator architecture fixes (Rule P inline-section walk + lint
Pattern D scope), 1 template-completeness addition (pre_flight block),
1 schema-doc reconciliation (close_signal_source comment). NO new tool
entries. NO new personas. NO new application patterns. NO new
chapters. NO schema-version bump (v1.14.0 frozen sustained). NO new
question banks. The substantive corpus (Sprints 01-18 engine) is
unchanged.

### Known Limitation L1 (permanent)

Sprint 19 documents **L1 — Cognitive-load-correlated compose-time
discipline degradation** as a permanent known limitation for the
v2.0 / v3.0 STABLE iteration. Under cognitive load, the protocol's
compose-time behavioral disciplines may degrade together as a class
across multiple surfaces (Class A composition-meta, Class D close-
surface, trigger-phrase first-invocation gate, schema annotation
coupling, tool-status preface avoidance). Script-side regex
enumeration catches known shapes; spec-contract enforcement (Card 12
Rule J, Card 03 Rule P, Card 04 Rule D, Card 04-D Rule Q) holds
uniformly across cohorts. The architectural fix (compose-time runtime
hook + spec-contract conversion of regex-enumeration cards) is out
of scope for v2.0 / v3.0 STABLE and would require a future product
iteration. See `OPERATOR-GUIDE.md` §7 for full L1 framing and
operator-side mitigation.

---

## v1.x history pointer

For the full sprint-by-sprint history that produced v1.x → v2.0:

- **Master plan Part 17.5** — canonical sprint-by-sprint record with
  every card, every amendment, every panel finding, every protocol
  evolution. Master plan path:
  `_Sync.../Plans/solve-ex-v2-master-plan.md`.
- **`99-Archive/sprint-NN/`** (Sprint 18+) and `99-Archive/sprint-NN-*.md`
  (Sprints 07-17) — per-sprint acceptance gates, cross-test analyses,
  closeout handoffs, and investigation notes.
- **`99-Archive/sprint-roadmap.md`** — high-level roadmap of the sprint
  arc.

Sprint highlights:

- **Sprint 05** — Schema foundation (v1.14.0 schema validated against
  677-entry tool corpus).
- **Sprint 06** — Phase 1 MVP build (folder architecture; 6 chapters; 5
  patterns; 3 personas; 3 scripts).
- **Sprints 07-12** — Iterative protocol hardening (Class A/B/C voice
  taxonomy, Phase 0 readiness gate, structural-unit cadence for
  prose-authoring sprints, mandatory audit markers).
- **Sprints 13-17** — Voice-neutrality lint maturation (INVITATION_PATTERNS,
  INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS, lookahead-based regex termination,
  pipe-wrapped exit-code detection).
- **Sprint 18** — Final Tier 1 + Tier 2 closure; supplementals (Cards
  10/11/12) tested for first time in Sprint 19 panel.
- **Sprint 19** — Ship release. v2.0 STABLE delivery + v3.0 STABLE master
  plan freeze stamp (this release).

For the detailed protocol evolution behind each sprint, consult the
master plan Part 17.5 (the canonical record) and the per-sprint archives
in `99-Archive/`.

---

## Format conventions

This changelog uses [Keep a Changelog](https://keepachangelog.com/)
conventions adapted for SOLVE eX:

- One entry per **release version** (not per sprint — sprints are
  documented in the master plan).
- Entry headers: `## vX.Y — YYYY-MM-DD — [Release name]`.
- Entry body: master plan version, schema version, sprint reference,
  what changed, what did NOT change.
- Older releases collapse into a single "v1.x history pointer" section
  since detailed history lives in the master plan and `99-Archive/`.

Future v3.x releases append above; v2.0 remains the bottom-of-stack
entry (the ship baseline).
