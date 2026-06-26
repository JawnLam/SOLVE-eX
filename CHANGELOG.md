# SOLVE eX v2.x — Changelog

This changelog records corpus-level releases. For sprint-by-sprint detail
(every card executed, every protocol amendment, every panel finding), see
the **master plan at Part 17.5 (Sprint History)** and the per-sprint
archives in `99-Archive/sprint-NN/`.

See `VERSION.md` for the current release's full version-identifier table.
See `CONTRIBUTING.md` for the versioning policy (when changes require a
v3.x bump vs. when they are in-scope at v3.0 STABLE).

---

## [2.2.0] — 2026-06-26

Google OKF v0.1 conformance (coordinated with vault Master_Schema v1.23.0 + OVE v2.4.0). Universal Core renamed to OKF field names (Item_Prototype→type, Title→title, Tags→tags; added timestamp from Date_Modified, optional description/resource). Convention-6 folder _Prototypes/ → _types/. Date_Modified kept, time-synced with timestamp. Hugo excluded.

## v2.1.3 — 2026-06-07 — UPDATE-PROMPT.md (OVE Convention 7's fourth artifact)

**Master plan version:** v3.0 STABLE (unchanged)
**Schema version:** v1.14.0 FROZEN (unchanged)
**License:** CC-BY 4.0 (unchanged)

Patch release adding `UPDATE-PROMPT.md` at the SOLVE-eX root — the fourth required artifact under OVE Convention 7 (added in OVE v1.2.1).

### Added — `UPDATE-PROMPT.md`

Copy-pasteable AI prompt that asks any AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code) to walk the operator through updating SOLVE-eX to the latest release. The prompt instructs the AI to:

1. Read `INSTALL.md § "Updating"` and `OPERATOR-GUIDE.md § "Updates and troubleshooting"` so it knows SOLVE-eX's update protocol.
2. Run `git fetch origin` and report incoming commits + the new CHANGELOG entry.
3. Check `git status` and propose a stash strategy if local engine modifications exist.
4. Walk through `git pull --ff-only origin main` step by step, stopping to confirm before running.
5. Surface migration recipes (e.g., master-plan-version bumps that require re-running validation scripts), major.minor folder renames, breaking-change notes from the new CHANGELOG entry.
6. Verify the operator's active case files (`06-Case-Files/_ACTIVE/`) and operator-private content (`06-Case-Files/_DRAFT/`, `_USER.md`) are intact and untouched after the pull.

The prompt enforces discipline:

- Do not modify Operator-Extension or Operator-Private Zone content.
- Do not run destructive commands without explicit operator confirmation.
- Stop and ask if anything is unclear or unexpected.

### Why two update paths

OVE Convention 7 supports both a **manual path** (operator reads `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates`, runs git commands themselves) and an **AI-assisted path** (operator opens `UPDATE-PROMPT.md`, copies the prompt, pastes to an AI, approves each step). Manual path is recommended for major-version transitions and any release with a non-trivial migration recipe (a SOLVE-eX v3.0 would qualify); AI-assisted path is recommended for routine releases (patches and small minors).

### No behavioral, schema, or content changes

- Process framework unchanged
- Tool Entries unchanged (30+ canonical Tools still operative)
- Master Plan version unchanged at v3.0 STABLE
- Schema version unchanged at v1.14.0 FROZEN

Patch release. Purely additive.

Coordinated multi-OV release with OVE v1.2.1 (codifies the artifact + adds validator C10), LFW v1.7.2, LLL v1.3.1.

---

## v2.1.2 — 2026-06-06 — Conventions 7+8 adoption (install/update + zone boundary)

**Master plan version:** v3.0 STABLE (unchanged)
**Schema version:** v1.14.0 FROZEN (unchanged)
**License:** CC-BY 4.0 (unchanged)

Adopts OVE Conventions 7 (install-and-update pattern) and 8 (engine vs operator-content boundary). Documents the install/update workflow and the four-zone content boundary in front-door docs.

### Added — OVE Convention 7 (install-and-update pattern)

`INSTALL.md` rewritten with:

- **§ 1** — canonical git-clone-with-push-disabled install snippet. Concrete URL: `https://github.com/JawnLam/SOLVE-eX.git`. Folder convention: `SOLVE-eX-v<major>.<minor>`.
- **§ 1a** — alternative no-git install (download ZIP, manual copy).
- **§ 7 — Updating** — `git fetch` + `git log --oneline HEAD..origin/main` + `git pull --ff-only`, with stash-pop fallback for when local engine edits would conflict.
- Major.minor folder transition snippet (`mv SOLVE-eX-v2.1 SOLVE-eX-v2.2`).

`OPERATOR-GUIDE.md` gains:

- **§ 9 — Updates and troubleshooting** — clean fast-forward, stash-pop conflict resolution (`git checkout --theirs`), recovery for lost files, major.minor folder transitions, contributing back upstream (re-enable push to your fork; never to upstream).

### Added — OVE Convention 8 (engine vs operator-content boundary)

`CONTRIBUTING.md` gains:

- **§ 7 — Content zones** — declares the four zones with concrete path patterns:
  - **Engine Zone** — front-door docs, `00-Instructions/` through `05-Personas/`, `07-Scripts/`, `08-Schema/`, `09-Sample-Sessions/`, `10-Reference/`, `99-Archive/`, `_types/`, `.gitignore`
  - **Operator-Private Zone** — `_USER.md`, `06-Case-Files/_ACTIVE/`, `06-Case-Files/_DRAFT/`, Python/IDE caches
  - **Operator-Extension Zone** — `06-Case-Files/_ACTIVE/<your-case>/` and `06-Case-Files/_RESOLVED/<your-case>/`; custom tools in `01-Tools/Tool Entries/` (requires fork)
  - **Shipped Examples Zone** — `09-Sample-Sessions/`, `06-Case-Files/_REFERENCE/`, `01-Tools/Tool Entries/` (the canonical 30+ Tool Entries)

`OPERATOR-GUIDE.md` gains:

- **§ 8 — Engine vs your work** — plain-English explanation of the four-zone boundary, with concrete file/folder examples per zone.

### No behavioral, schema, or content changes

- Process framework unchanged
- Tool Entries unchanged (30+ canonical Tools still operative)
- Master Plan version unchanged at v3.0 STABLE
- Schema version unchanged at v1.14.0 FROZEN
- No new sprints, protocols, or content extensions

This is a patch release whose only contribution is install/update pattern + zone-boundary documentation through OVE Conventions 7+8 conformance.

This release is part of an OVE-coordinated multi-OV cycle: OVE v1.2.0 codifies Conventions 7 and 8; LFW v1.7.1, LLL v1.3.0, and this release retrofit them across the OV ecosystem.

---

## v2.1.1 — 2026-06-06 — Convention 6 adoption (portability)

**Master plan version:** v3.0 STABLE (unchanged)
**Schema version:** v1.14.0 FROZEN (unchanged)
**License:** CC-BY 4.0 (unchanged)

Adopts Operating-Volume-Engineering Convention 6 (every OV ships its own `_types/` folder for portability). Anyone cloning this repo without the operator's vault Infrastructure now gets the Prototype definition out of the box.

### Added — `_types/` folder with `Thinking_Tool.md`

A new top-level `_types/` folder contains one Markdown file: `Thinking_Tool.md`, a verbatim mirror of the vault's `_Infrastructure For All Vaults/_types/Thinking_Tool.md`. This is the canonical definition of the `Thinking_Tool` Prototype that every Tool Entry in `01-Tools/Tool Entries/` instantiates.

SOLVE eX uses only one Prototype — `Thinking_Tool` (from the vault's `tt_` namespace) — so `_types/` contains exactly one file. The remaining content (Process Framework, Question Banks, Application Patterns, Personas, Case Files, Reference, etc.) is structured prose, not Prototype-bearing notes.

### No content, schema, or behavioral changes

- Process framework unchanged
- Tool Entries unchanged
- Master Plan version unchanged at v3.0 STABLE
- Schema version unchanged at v1.14.0 FROZEN
- No new sprints, protocols, or content extensions

This is a patch release whose only contribution is portability through Convention 6 conformance.

---

## v2.1.0 — 2026-05-29 — ADAPT Loop Integration (Sprint 02)

**Master plan version:** v3.0 STABLE (unchanged)
**Schema version:** v1.14.0 FROZEN (unchanged)
**Sprint:** Sprint 02 of the public-release iteration — first content extension under the v3.0 STABLE freeze
**License:** CC-BY 4.0 (unchanged)

First substantive content extension under the v3.0 STABLE freeze. Demonstrates that the `CONTRIBUTING.md` "additive non-breaking extensions accepted" path works as designed. Integrates **The ADAPT Loop** — the operator's dissertation-derived framework on senior-executive political capital, agenda formation, decision-matrix discipline, and multi-cycle compounding (Lam 2020, Pepperdine Ed.D.) — into the SOLVE eX tool library.

### Additive content (Sprint 02)

- **12 new atomic tool entries** at `01-Tools/Tool Entries/` (8 mandatory + 4 optional):
  - `Actor-Agenda Decomposition` (was: Agenda Funnel) — the structural ladder Actor → Agenda → Interest → Objective → Goal → Target.
  - `Required-Resource Check` (was: Capability Gate) — pre-action gate; surfaces the implicit resource-controlled assumption.
  - `Decision Matrix Construction` — PP × AA × Benefit × Cost matrix; includes multi-PP hierarchy sub-discipline.
  - `Bet vs Workhorse Discrimination` — option-classification lens for matrix output.
  - `Perception and Actual Effect Gap Audit` (was: Perception Gap Audit) — three-utilities (Expected / Actual / Perceived) post-action diagnostic.
  - `Disciplined Hold` — stance entered when the capability gate returns No.
  - `9-Resource Portfolio Diagnostic` (NEW from dissertation) — Money / Hard Assets / Credibility / Attributes / Legitimacy / Information / Access / Title / Tribe taxonomy.
  - `Nested Sub-Cycle Discipline` (NEW from dissertation) — cycle-stack discipline for sub-cycle procurement work.
  - `Mid-Cycle Interest Pivot` (optional, NEW) — abductive reformulation when mid-execution reveals a different interest serves the agenda.
  - `Cross-Actor Matrix Reading` (optional) — perspective-shift lens that runs the ADAPT funnel on overlay actors.
  - `Iterated Loop Compounding` (optional) — stance for cycle-over-cycle compounding via the recursive prescription.
  - `Calibration Gap Read` (optional, NEW) — interprets outcome-magnitude surprises as third-party overlay-matrix output, not noise.
- **1 new glossary section** at `10-Reference/glossary.md` — "ADAPT Loop — 19 Theoretical Categories (Lam 2020)" — adds 19 alphabetical categories + 3 framing wrappers (Agenda / Objective / Intention) + 9 Resource sub-types (Money through Tribe). Each entry: dissertation page citation + 1-3 sentence definition + backticked cross-link to operationalizing tool entry. SOLVE eX system-vocabulary cross-links wired into Goal, Outcome, Tribe, and Resources entries.
- **1 new application pattern** at `04-Application-Patterns/pattern-adapt-loop-multi-cycle-strategic-action.md` — the corpus's first **integrative-session-design** application pattern (distinct from the existing form-mapping patterns which describe how one `tt_Form` value is enacted; this one describes which tools to apply in what combinations under the ADAPT framework specifically). Sections: Framework overview (positioned as lens, NOT prescription, per Lam 2020 Ch 6 tacit-vs-explicit framing); the four field-manual views as alternative entry points; five multi-cycle architectural patterns with case-study extracts; when-to-invoke / when-NOT-to-invoke; tool composition; glossary cross-reference.
- **1 new reference PDF** at `10-Reference/ADAPT-Loop-Field-Manual.pdf` — 42-page operator-facing field manual (443 KB). Includes the master diagram, four progressively-zoomed views (Whole loop / Forming the aim / Decide / Act-Perceive-Track), three fictional case studies (Cresterly analytics group / Cathna Series A under pressure / Talvyn CTO offer), how-to-use-in-practice chapter, and 41-entry glossary.

### Sources and citation discipline

- **Field manual** — placed in corpus at the path above.
- **Dissertation** — Lam, J. (2020). *The Accumulation, Utilization, and Protection of Political Capital by Senior Executives of For-Profit Organizations.* Doctoral dissertation, Pepperdine University. **NOT placed in corpus** per Pepperdine IRB obligations to the five case-study participants (Ch 3 Policies & Procedures, dissertation pp. 67-70). Cited inline in every tool entry, glossary entry, and the application pattern by category-and-page reference. Readers wanting the academic version may contact the operator directly.
- **Dual-citation channels** — every tool entry's body cites BOTH dissertation page numbers (for conceptual claims) AND field-manual page numbers (for operator-facing worked examples). All 12 entries pass dual-citation verification.

### Validation

- All 12 ADAPT tool entries pass `07-Scripts/validate-tool.py` (exit 0; schema v1.14.0 compliant).
- All 12 ADAPT tool entries pass `07-Scripts/voice-neutrality-lint.py` (exit 0).
- Extended `10-Reference/glossary.md` passes `07-Scripts/voice-neutrality-lint.py` (exit 0).
- New application pattern at `04-Application-Patterns/` passes `07-Scripts/voice-neutrality-lint.py` (exit 0).
- All 41 `tt_Pairs_Well_With` cross-references across the 12 new tool entries resolve to existing tool filenames (verified via Python set-membership against `01-Tools/Tool Entries/` directory).
- All 12 tool-entry backticked cross-references in the new glossary section resolve to existing tool entries.

### Significance

This is the proof-of-life for v3.0 STABLE's additive-extension policy. Sprint 02 shipped substantively new content (1 application pattern + 12 tool entries + 1 glossary section + 1 reference PDF) without invoking any v3.x bump trigger — validating the entire freeze-with-extensibility design that Sprint 19's `CONTRIBUTING.md` proposed. External contributors considering ADAPT-like additions can look at Sprint 02 as the canonical worked example. **Schema regressions: zero.** Cross-references resolve: 100%. Voice neutrality: 100%.

### Sprint 02 archive

`99-Archive/sprint-02-adapt-integration/sprint-02-acceptance-gate.md` (operator-private; not in public repo per CC-BY 4.0 attribution-only requirement).

---

## v2.0 — 2026-05-26 — Public Release (GitHub Publish)

**Master plan version:** v3.0 STABLE (unchanged)
**Schema version:** v1.14.0 FROZEN (unchanged)
**Sprint:** Sprint 01 of the public-release iteration (NOT Sprint 20 of the prior internal-development iteration — that iteration closed at v2.0 SHIPPED with v3.0 STABLE master plan freeze at Sprint 19, 2026-05-25)
**Public URL:** [https://github.com/JawnLam/SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

The corpus is now publicly available. This is publish hygiene, not protocol amendment — v3.0 STABLE is NOT broken by this release.

### Publish-hygiene changes (Sprint 01)

- **Path scrubbing.** All `/Users/jawnlam/` absolute paths in 4 corpus files (`AI-BOOTSTRAP.md`, `OPERATOR-GUIDE.md`, `00-Instructions/00-START-HERE.md`, `00-Instructions/13-quality-checks.md`) replaced with `{HOME}/` placeholders. Operator-private filesystem layout no longer leaks into corpus content. `99-Archive/` historical "Jawn Lam" attribution preserved (intentional honest historical record per operator decision).
- **`.gitignore` created.** Excludes `06-Case-Files/_ACTIVE/` (operator-private session content), `99-Archive/` (operator-private development history), `.DS_Store` (Mac filesystem metadata), `**/_writetest*` (Phase 0 environment-check probes), editor artifacts (`.vscode/`, `.idea/`, `*.swp`), Python bytecode (`__pycache__/`, `*.pyc`), and OS metadata (`Thumbs.db`, `.directory`).
- **License swap.** Custom operator-private `LICENSE.md` replaced with **Creative Commons Attribution 4.0 International** (CC-BY 4.0). Maximum-adoption permissive license; attribution to John Lam ([JawnLam/SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)) required.
- **`.DS_Store` files removed.** 7 instances across root + 5 chapter folders + `07-Scripts/lib/` deleted from local filesystem; `**/.DS_Store` pattern in `.gitignore` prevents recurrence.
- **README rewrite for public-arrival context.** Added 4 GitHub-style badges (license, version, schema, master plan), an "Examples of what it can help with" section (8 use cases), expanded Quick Start for fresh-clone arrivals, explicit CC-BY 4.0 license callout with attribution template, inline cross-reference links throughout. Preserved verbatim: "Which file do I read?", folder structure table, "Where to go for what" table, maintenance/versioning, "What this is not." All 20 cross-references verified post-rewrite.
- **Email-pattern review.** 4 Tool Entries flagged by prior audit (NURSE Statements, Stuart Brown Play Frame, REMAP Goals of Care, Sun Tzu Asymmetric Logic) verified clean: ZERO `@`-matches in flagged files OR across all 682 Tool Entries.
- **Git provenance.** First commit `b872461` on `main` branch with annotated `v2.0` tag. Author: John Lam <jawnlam@gmail.com>. 837 tracked files, 144,816 insertions.
- **GitHub Topics set** (12 for discoverability): `ai`, `decision-making`, `problem-solving`, `methodology`, `thinking-tools`, `claude`, `anthropic`, `framework`, `structured-thinking`, `consulting`, `ai-orchestration`, `decision-framework`.

### Known cosmetic issue

GitHub's license auto-detect (Licensee gem) returned `NOASSERTION` for the CC-BY 4.0 `LICENSE.md`. The canonical legal text IS in the file body, but a 19-line SOLVE-eX-specific preamble (title, TL;DR, attribution, canonical link) prevents the strict pattern match. Substance is preserved (license is legally CC-BY 4.0); only the auto-rendered sidebar badge is affected. Future small sprint can remediate by moving the preamble to a separate `ATTRIBUTION.md` and starting LICENSE.md at the canonical text on line 1.

### Sprint 01 archive

`99-Archive/sprint-01-public-release/sprint-01-publish-readiness-gate.md` (operator-private; not in public repo per Decision 2).

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
