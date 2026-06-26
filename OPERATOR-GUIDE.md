# SOLVE eX v2.0 — Operator Guide

This guide is for **operators**: people responsible for running, maintaining,
or extending SOLVE eX v2.0. It complements `README.md` (downstream-user
overview) and `INSTALL.md` (setup) by documenting runtime operation, session
modes, validation tooling, and recovery from common failure modes.

For contribution workflow, see `CONTRIBUTING.md`. For release history, see
`CHANGELOG.md`.

---

## 1. How to run a session from start to finish

A SOLVE eX session has five operator-observable phases. The AI handles them
internally; this section names them so operators can recognize what is
happening and audit it.

### 1.1 Pre-flight (operator setup)

Before any session:

- Confirm the corpus is on local disk and readable by the AI environment.
- Confirm `06-Case-Files/_ACTIVE/` is writable by the AI environment, OR
  accept that the session will run in **sandbox mode** (Case File state
  lives as inline markdown blocks in the chat rather than on disk).
- Confirm `07-Scripts/` is accessible and Python 3.10+ with `pyyaml` is
  available, if you want validation scripts to be invocable mid-session
  or post-session.

### 1.2 Phase 0 (AI bootstrap)

The operator triggers Phase 0 by sending the AI:

> Read `AI-BOOTSTRAP.md` and then help me think through something.

The AI MUST:

1. Read in full the **core seven** chapters from `00-Instructions/`:
   `00-START-HERE.md`, `01-the-cognitive-model.md`,
   `02-the-bootstrap-protocol.md`, `03-the-diagnostic-loop.md`,
   `06-the-case-file.md`, `09-safety-and-stakes.md`,
   `13-quality-checks.md`. "Skim" is not a valid mode for the core seven.
2. Verify environment: `06-Case-Files/_ACTIVE/` writable; validation scripts
   loadable. If not, declare sandbox or degraded mode.
3. Declare session mode (see §2 below).
4. Output a single short readiness paragraph as its first response. The
   audit-trail detail (chapters read, scripts loaded, session mode active,
   checklist items) goes in the Case File `pre_flight:` frontmatter block,
   NOT in the chat.

If the AI's first response is anything other than a readiness statement —
a greeting, a question, an artifact, an explanation — Phase 0 was skipped.
**Stop the session and restart.**

### 1.3 In-persona session

The AI runs the diagnostic loop (`00-Instructions/03-the-diagnostic-loop.md`)
across one or more turns, modulating persona per `05-Personas/`. The Case
File is continuously updated as the source of truth for what the user has
said and what has been discovered.

The user describes; the AI diagnoses; the AI surfaces the appropriate
thinking tool from `01-Tools/Tool Entries/`; the user works the tool; the
AI captures the result. Repeat until the user reaches a decision or an
explicit pause point.

### 1.4 Close protocol

When the diagnostic concludes (the user commits to an action package, OR
declares the session paused), the AI:

- Finalizes the Case File (action package, scope statement, any open
  threads).
- Writes any session-mode-specific close-out notes (test-mode audits, etc.).
- Names the next session, if a continuation is planned.

### 1.5 Audit pass (post-session)

After the session, the operator can run validation:

```bash
python3 07-Scripts/validate-case-file.py 06-Case-Files/_ACTIVE/[case-file].md
python3 07-Scripts/voice-neutrality-lint.py 06-Case-Files/_ACTIVE/[case-file].md
python3 07-Scripts/trigger-phrase-audit.py 06-Case-Files/_ACTIVE/[case-file].md
python3 07-Scripts/post-session-audit.py --max-iterations 3 06-Case-Files/_ACTIVE/[case-file].md
```

Exit 0 on all four indicates a clean session per the v3.0 STABLE rule set.
Non-zero exit codes indicate failure modes documented in §4.

---

## 2. Session modes

Declared in Phase 0 per `00-Instructions/14-session-modes.md`.

| Mode                          | When it applies                                                                  | What changes downstream                                                                                                              |
|-------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **production**                | Default — real user, deliverables persist to disk and the user.                  | Standard Case File on disk; full safety routing; standard audit pass.                                                                |
| **test**                      | Acceptance gate / re-test / dry-run / panel runs.                                | Output audited against criteria, not delivered downstream. Test-mode Case Files live in `06-Case-Files/_ACTIVE/test_mode_*.md`.       |
| **sandbox**                   | No writable disk (Claude.ai sandbox, restricted chat, read-only mount).          | Case File state lives as inline markdown blocks in the conversation rather than on disk. All other behavior identical.                |
| **multi-session-resumption**  | Continuing a prior Case File from a previous session.                            | AI reads the prior Case File first; declares which threads are being resumed; preserves existing Case File rather than starting new.  |

**Declaring the wrong mode breaks downstream rules.** A production session
that's actually a panel run will incorrectly persist test deliverables; a
sandbox session declared as production will silently drop Case File writes;
a multi-session-resumption declared as fresh will overwrite prior context.

The mode is operator-observable in the Case File `session_mode:` frontmatter
field. Audit it.

---

## 3. Validation scripts overview

All scripts live in `07-Scripts/` and use Python 3.10+ with `pyyaml` only.

| Script                              | When to run                                              | What it checks                                                                                                          | Exit codes               |
|-------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------|
| `check-phase0-sync.py`              | After any edit to `AI-BOOTSTRAP.md` or `00-Instructions/00-start-here.md` | Root + mirror Phase 0 sections are in sync.                                                                | 0 sync; 1 diverge; 2 setup err |
| `validate-tool.py [file]`           | After authoring or editing a tool entry                  | Tool entry conforms to v1.14.0 schema (file structure, required props, enum values, cross-field consistency, body).      | 0 pass; 1 fail; 2 yaml err; 3 io err |
| `validate-case-file.py [file]`      | Post-session, OR mid-session smoke check                 | Case File conforms to schema rules A–O (and Rule P when applicable).                                                    | 0 pass; non-zero fail (see script docstring for rule-specific codes) |
| `voice-neutrality-lint.py [file]`   | Post-session, OR after AI emits in-session prose         | Case File AI-voice lines do not contain Class A/B/C voice-neutrality violations (chapter 13 §13.2 + §13.10).            | 0 clean; 1 violation found |
| `trigger-phrase-audit.py [file]`    | Post-session                                              | Case File trigger phrases (gate firings, mode declarations, safety routes) are present where chapter 13 requires.        | 0 clean; 1 missing       |
| `pre-emit-check.py --surface-class A\|B\|C\|D` | Mid-session, before the AI emits chat-visible prose | Surface-class-specific banned-pattern lint per chapter 13 §13.10.                                                       | 0 clean; 1 violation     |
| `test-regex-coverage.py`            | After any change to `voice-neutrality-lint.py` regex sets | Lint regex sets fully cover the chapter 13 §13.2 + §13.10 canonical spec entries.                                       | 0 full coverage; 1 gap    |
| `post-session-audit.py --max-iterations N` | Post-session                                              | End-to-end audit chain: runs validate-case-file → voice-lint → trigger-phrase → pre-emit-check iteratively.            | 0 clean (within N iters); 1 fail |
| `case-file-placeholder-lint.py`     | Post-session                                              | Case File does not contain unfilled `<!-- placeholder -->` markers.                                                     | 0 clean; 1 placeholders remain |
| `cross-chapter-dependency-audit.py` | After any edit to `00-Instructions/` chapters             | Cross-chapter `chapter N §M.O` references resolve to existing sections.                                                 | 0 clean; 1 broken refs; 2 setup err |
| `artifact-quality-audit.py`         | Periodic / pre-ship                                       | Aggregate quality scoring across the corpus.                                                                            | (script-specific)        |
| `portability-check.py`              | Pre-ship / after architectural changes                    | No hard-coded paths or environment dependencies in the corpus.                                                          | (script-specific)        |
| `trigger-phrase-audit.py`           | (listed above)                                            |                                                                                                                          |                          |
| `new-case-file.py`                  | At session start (optional)                               | Generates a new Case File from the template.                                                                            | 0 success; 1 io err      |
| `find-tools.py [filters]`           | Mid-session (operator-only)                               | Searches the tool library by facet filters.                                                                             | 0 success                |
| `show-stack.py [case-file]`         | Mid-session (operator-only)                               | Prints the current phase-step stack from a Case File.                                                                   | 0 success                |
| `case-file-summary.py [case-file]`  | Post-session                                              | Generates a human-readable summary of a Case File.                                                                       | 0 success                |
| `search-questions.sh [pattern]`     | Mid-session (operator-only)                               | Searches `03-Question-Banks/` for matching questions.                                                                   | 0 found; 1 no match      |
| `list-tools-by-facet.sh [facet] [value]` | Mid-session (operator-only)                          | Lists tool entries matching a facet value (`tt_Form`, `tt_Operation`, etc.).                                            | 0 success                |

Read each script's docstring header (`head -30 [script.py]`) for full usage,
example invocations, and sprint provenance.

---

## 4. Common failure modes + recovery

Each row names a class of failure that fires during real sessions, the
canonical detection signal, and the recovery procedure.

### 4.1 Rule D status/active mismatch

**Symptom:** `validate-case-file.py` exits 1 with a Rule D violation —
`status:` block declares a phase-step as `active` but the Case File body
indicates a different phase-step is actually being worked.

**Cause:** Case File `status:` block was updated to advance the phase-step
but the prose immediately afterward returned to the prior step (e.g.,
clarification re-opened) without rolling back the `status:` block.

**Recovery:** Roll the `status:` block back to the actual active step, OR
advance the prose to match the declared step. Schema rule D enforces
consistency between the two; arbitrary divergence is invalid. See
`00-Instructions/13-quality-checks.md` for the rule's full specification.

### 4.2 Class C Phase 0 leak

**Symptom:** AI's first response emits sysadmin-style content — explicit
file paths, script-name lists, key:value-formatted system-state fields,
e.g. `Scripts: available [find-tools.py, validate-case-file.py, ...]` or
`Case Files: writable at {HOME}/Dropbox/...`.

**Cause:** AI confused the Phase 0 readiness-statement requirement
(user-facing prose) with the Case File `pre_flight:` audit-trail block
(structured data).

**Recovery:** Stop the session. The first response is non-recoverable —
the leak has already happened and any continuation is downstream-tainted.
Restart with explicit emphasis on the readiness-statement format
(see `00-Instructions/00-start-here.md` §4 and §6). Run
`voice-neutrality-lint.py --mode standard` against the leaked response
text to confirm the pattern that fired, so the regex set can be extended
if the leak shape is new.

### 4.3 §14.2 audit-trail recording

**Symptom:** Session completes cleanly but `trigger-phrase-audit.py` exits
1 with a missing `detection_check:` block, OR `post-session-audit.py`
reports the Phase 0 readiness fired behaviorally but produced no audit
trail.

**Cause:** AI satisfied the runtime gate (e.g., Phase 0 readiness was
declared in chat) but did NOT write the corresponding `detection_check:`
or `pre_flight:` block to the Case File frontmatter as required by
chapter 13 §13.2 + §14.2.

**Recovery:** Add the missing audit-trail block to the Case File
post-session (the gate fired correctly; only its evidence is missing).
Document the recovery in the Case File `post_session_notes:` so the audit
trail explains why the block was added post-hoc rather than at gate-firing
time.

### 4.4 Rule J ↔ §6.4.0 placeholder pattern

**Symptom:** `case-file-placeholder-lint.py` exits 1 reporting unfilled
`<!-- placeholder -->` markers in the Case File, AND/OR
`validate-case-file.py` Rule J fails.

**Cause:** Case File template's placeholder markers (in section 6.4.0 and
elsewhere) were copied into a real Case File but the AI did not replace
them with actual content during the session. This typically happens when
the AI advances quickly through a section without exercising the prompts
that section contains.

**Recovery:** Either fill the placeholders with actual content (if the
section was substantively worked but the content wasn't captured), OR
remove the placeholder markers entirely (if the section was intentionally
skipped per session-mode rules). Do NOT leave placeholders unfilled — the
lint exists because unfilled placeholders silently break downstream tools
that expect filled content.

### 4.5 Detection regex undercount (lookahead-based termination)

**Symptom:** A regex written with character-class exclusion
(`[^-]*?placeholder[^-]*?`) silently undercounts matches because real
content contains internal hyphens (kebab-case identifiers, em-dash + ASCII
hyphen sequences).

**Cause:** The exclusion-class pattern is too restrictive; it skips any
comment whose internal text contains a hyphen.

**Recovery:** Rewrite as lookahead-based termination:
`<!--(?:(?!-->).)*?placeholder(?:(?!-->).)*?-->`. Pre-flight test against a
hyphen-containing case (`<!-- step-by-step placeholder -->`) before
committing. Documented in sister sprint protocol; the same shape recurred
twice in Sprint 11 (voice-neutrality-lint Card 04 + Case File
placeholder-lint Card 06).

### 4.6 Pipe-wrapped exit-code masking in test runners

**Symptom:** A bash test runner reports all tests pass (or all fail)
despite mixed actual outcomes. Symptom is uniform exit codes across
heterogeneous output.

**Cause:** Test script piped through `tail`, `head`, `grep`, or `wc` for
output filtering; `$?` returns the LAST pipeline command's exit code
(always 0 for `tail` / `head` / `wc -l`), masking the test script's actual
exit.

**Recovery:** Two patterns: (a) redirect output and check `$?` immediately:
`script.py file --quiet > /dev/null 2>&1; echo "exit=$?"`; (b) use
`set -o pipefail` at top of test scripts — returns last non-zero exit in
the pipe rather than the literal-last command's exit. Documented as a
Sprint 13 finding (Card 07 voice-neutrality-lint test runner).

---

## 5. Master plan freeze policy

The **master plan** is the canonical specification for SOLVE eX v2.0. It
lives at:

```
{HOME}/Library/CloudStorage/Dropbox/Apps/Hostinger/_Sync Claude Code on Hostinger VPS with DropBox/Plans/solve-ex-v2-master-plan.md
```

The master plan is at **v3.0 STABLE** as of Sprint 19 ship.

### 5.1 What is frozen at v3.0 STABLE

| Element                                      | Status                                                                                  |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| Schema (v1.14.0)                             | FROZEN. Tool entries, Case File fields, frontmatter contracts are stable.               |
| Operating manual chapter structure           | FROZEN. The 14 numbered chapters in `00-Instructions/` are the canonical organization.  |
| Persona contracts (Partner / Counselor / Therapist / Guide / Consultant) | FROZEN. Switching rules + voice characteristics + applicability are stable. |
| Process Framework (6 phases / 21 steps)      | FROZEN. The phase-step taxonomy is the canonical decomposition.                         |
| Validator behavior                           | FROZEN. Scripts in `07-Scripts/` are the canonical enforcement; their exit-code semantics are stable. |
| Application Pattern set (1.0)                | FROZEN at the v3.0 STABLE patterns. New patterns require v3.x bump.                     |
| Class A/B/C/D voice-neutrality taxonomy      | FROZEN (chapter 13 §13.10).                                                             |

### 5.2 What is open for v3.x extension

| Element                                      | Status                                                                                  |
|----------------------------------------------|-----------------------------------------------------------------------------------------|
| Additional tool entries within v1.14.0 schema | OPEN. New tools can be added without a version bump as long as they conform to schema. |
| Additional sample sessions                    | OPEN. New samples in `09-Sample-Sessions/` are additive.                               |
| Additional question banks within existing controlled vocabulary | OPEN. New entries in `03-Question-Banks/` are additive.                           |
| Doc clarifications and typo fixes             | OPEN at any time without version bump.                                                 |
| `tt_Quality_Tier` facet                       | DEFERRED to v3.x. Not present in v1.14.0; do not invent the field on tool entries.     |
| Additional patterns / personas / phases       | REQUIRE v3.x bump + migration crosswalk + migration script.                            |

### 5.3 How to know whether your proposed change is in-scope

1. **Does it change schema?** If yes → v3.x bump required.
2. **Does it change validator behavior or exit codes?** If yes → v3.x bump required.
3. **Does it change persona contracts, phase-step structure, or chapter organization?** If yes → v3.x bump required.
4. **Is it additive content that conforms to existing schema + structure?** If yes → in-scope at v3.0 STABLE; no version bump needed.
5. **Is it a typo, clarification, or doc-only change?** If yes → in-scope at v3.0 STABLE.

For the v3.x bump workflow, see `CONTRIBUTING.md`.

---

## 6. Surface-class taxonomy (operator summary)

The chapter 13 §13.10 voice-neutrality + composition-discipline taxonomy
divides AI output into four surface classes by structural position and
addressee context. Each class has different tolerance for protocol-
mechanic narration. The full normative specification lives in chapter
13 §13.10; this is the operator-facing summary.

| Class       | Surface                                                | Tolerance  | What's banned                                                                                                                       |
|-------------|--------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Class A** | In-persona chat content (the primary chat surface a downstream user reads) | STRICTEST  | Composition-meta narration (Patterns A-T in `voice-neutrality-lint.py` `INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS`). No "let me set up the Case File," no "running the diagnostic loop," no "now the response:" preambles, no "task list is current" prefaces. |
| **Class B** | Operator-debrief content (when the operator has requested mechanics narration explicitly) | MODERATE   | Always-banned phrases ("I'd want," "I feel," "I'd suggest," "I'd say") still apply. Mechanics narration is permitted in B because the operator has requested debriefing. |
| **Class C** | Phase 0 readiness statement (the AI's first response, before any user message) | MODERATE   | Readiness confirmation language permitted ("Pre-flight is ready..."). Explicit script-name enumeration, path-name emission, system-state field-runs, frontmatter-block-name disclosure, and chapter §-reference enumeration are BANNED (Sprint 18 Card 10 + Sprint 19 Card 04-A regex coverage). User-facing prose only. |
| **Class D** | Turn-boundary composition (end-of-turn footers between substantive content and the next user message) | LOW        | Milestone check-in language permitted ("Come back if X happens" — chapter 10 §10.5 step 3 obligation). Protocol-mechanics narration BANNED — no Case File field enumeration, no signals-fired counts, no audit-script name enumeration, no "post-session audit ran: validate-case-file.py passed..." style close-surface leaks. |

**Enforcement.** Each surface class has corresponding regex coverage in
`07-Scripts/voice-neutrality-lint.py` (Class A patterns), and
`07-Scripts/pre-emit-check.py --surface-class A|B|C|D`. Operators
running the post-session audit chain (per §1.5) get class-specific
exit codes. Run `pre-emit-check.py --surface-class C` against the
Phase 0 readiness statement to verify it passes Class C coverage.

---

## 7. Known Limitations (permanent for v3.0 STABLE iteration)

This section names architectural patterns that v3.0 STABLE does NOT
fully close. Each is documented as a permanent limitation rather than
a deferred fix — the v3.0 STABLE freeze means no further protocol
changes in this product iteration. A future product iteration may
revisit these.

### L1. Cognitive-load-correlated compose-time discipline degradation

**Pattern.** Under cognitive load (high-density-sophisticated user
openings, mid-session tool-application complexity, honest-audit-
surfacing turns), the protocol's compose-time behavioral disciplines
may degrade TOGETHER AS A CLASS across multiple surfaces. Sprint 19
Card 04-E re-panel confirmed the mechanism is cross-surface, not
limited to Class A composition-meta.

**Surfaces that exhibit cognitive-load-correlated degradation.**

| Surface                                  | Discipline that degrades                                                       |
|------------------------------------------|--------------------------------------------------------------------------------|
| **Class A** (in-persona chat content)    | Composition-meta narration avoidance (Patterns A-T regex set)                  |
| **Class D** (turn-boundary composition)  | User-facing prose preserved over protocol-mechanic narration                   |
| **Trigger-phrase first-invocation gate** | Within-turn canonical-title surfacing when chapter 04 §4.3.3 trigger fires     |
| **Schema annotation coupling**           | `tool_surfaced_in_chat` Case File annotation when tool surfaces in chat        |
| **Tool-status preface avoidance**        | Substantive turn body content without protocol-state preamble                  |

**Empirical evidence (Sprint 19 panel data, 3 cohorts).**

| Cohort  | Cognitive load                                          | L1 manifestation                                                                     |
|---------|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| Yelena  | HIGH (dense legal-ethics + 5/5 detection + multi-thread) | Multiple surfaces (Class A + Class D + trigger + annotation across Card 04 + 04-E)   |
| Tessa   | MEDIUM (SaaS-ops + 3-4/5 detection mid-session)         | Single-surface manifestations (Class A in Card 04; task-list preface in Card 04-E)   |
| Mara    | LOW (single-frame coaching + 0/5 detection)             | None observed across Sprint 16-19 panels                                             |

**Root cause (architectural).** Script-side regex enumeration
(`voice-neutrality-lint.py` Patterns A-T,
`pre-emit-check.py` Class C/D patterns, `trigger-phrase-audit.py`
within-turn first-invocation gate) is **post-hoc validation** —
catches leaks AFTER composition. The compose-time decision to narrate
vs. just-deliver shifts under cognitive load even when the regex set
would catch the leak if emitted. New shapes WILL emerge under load
that the regex set hasn't seen yet — this is reactive enumeration,
not proactive discipline.

By contrast, **spec-contract enforcement** holds uniformly across
cohorts because it's structural, not behavioral. Card 12 Rule J ↔
§6.4.0 (with falsification-guarded `_check_tool_surfaced_annotation`),
Card 03 Rule P (frontmatter close-event populated before
status:resolved), Card 04 Rule D (status:resolved coupled to
goal_stack[0].active=false at compose-time), and Card 04-D Rule Q
(`_pending_regime` stakes-flag restored or downgraded after regime
clarification) all passed 3/3 panels in Sprint 19. Structural
enforcement is invariant under cognitive load.

**The true architectural fix is twofold:**

1. A **compose-time runtime hook** that hard-blocks on `pre-emit-check`
   exit 1 before the AI emits to chat (removes the "model didn't run
   the script" failure mode).
2. **Conversion of script-side regex enumeration cards to
   spec-contract enforcement** (Card 12 pattern). The cognitive-load
   hotspot scripts would convert to spec contracts that the validator
   checks at compose-time with falsification guards.

**Neither architectural fix is in scope for v2.0 / v3.0 STABLE.**
The compose-time runtime hook requires AI runtime instrumentation
that doesn't exist in the chat-completion API contract. The
spec-contract conversion requires refactoring stable chapters at
v3.0 STABLE — out of scope for a delivery iteration. Both are
candidates for a future product iteration if undertaken.

**Practical implication for operators.** When running high-cognitive-
load sessions (sophisticated users, multi-thread legal/financial
contexts, dense openings, mid-session tool-application complexity):

1. **Expect occasional discipline degradation across multiple
   surfaces** — not just Class A. Class D close-surface leaks,
   trigger-phrase within-turn miss, schema annotation coupling gaps,
   and tool-status preface emissions can all occur on the same
   session.
2. **The audit chain catches what regex covers.** Post-session run
   of `validate-case-file.py + voice-neutrality-lint.py +
   pre-emit-check.py --surface-class A|B|C|D + trigger-phrase-audit.py`
   identifies regex-enumerated leaks. New shapes that the regex set
   hasn't seen may pass audit-clean but still be visible in
   chat-stream review.
3. **Manual chat-stream review is the operator's L1 mitigation.**
   For high-cognitive-load sessions intended for downstream-user
   delivery, review the chat-stream for composition-meta narration,
   protocol-state preamble, script-name enumeration, and missing
   canonical-title surfacings before forwarding.
4. **DO NOT** propose new regex patterns to "close" cognitive-load-
   correlated leaks as they appear (per `CONTRIBUTING.md` §6
   reporting-failures workflow). Each new pattern adds maintenance
   burden + collateral false-positive risk, AND the underlying
   architectural pattern means new shapes emerge faster than regex
   can chase. Sprint 19 Card 04-B Pattern U decision (skip
   "switching gears") and Card 04-F Fix 2 (Pattern D over-fire on
   audit-trail prose, scoped via `AI_PLACEHOLDER_LINE_RE`) are the
   canonical discipline.
5. **DO** propose a v3.x bump (per `CONTRIBUTING.md` §1) if L1
   cross-surface degradation becomes operationally significant
   downstream. Scope: compose-time runtime hook + spec-contract
   conversion of regex-enumeration cards.

**The substantive engine is unaffected.** The protocol's substantive
disciplines — L1 problem identification, L4 close-protocol, persona
transitions, b-vs-c boundary handling, process-direct-read response,
milestone check-in, disclosure-regime probe, financial_catastrophe
routing-grade restoration, single-frame relaxation — all sustained
5-6 consecutive panel sprints at 5/5 across all three cohorts. L1
names a surface-discipline architectural ceiling; the substantive
engine clears it.

---

## Appendix: Quick command reference

```bash
# Pre-flight integrity (post-install)
python3 07-Scripts/check-phase0-sync.py
python3 07-Scripts/test-regex-coverage.py

# Mid-session inspection
python3 07-Scripts/show-stack.py 06-Case-Files/_ACTIVE/[case-file].md
python3 07-Scripts/find-tools.py --form Matrix
07-Scripts/search-questions.sh "ambivalence"

# Post-session audit chain
python3 07-Scripts/post-session-audit.py --max-iterations 3 06-Case-Files/_ACTIVE/[case-file].md

# Pre-ship corpus integrity
python3 07-Scripts/cross-chapter-dependency-audit.py
python3 07-Scripts/portability-check.py
python3 07-Scripts/artifact-quality-audit.py
```

See `07-Scripts/README.md` for any scripts not listed above.

## 8. Engine vs your work — the four content zones (OVE Convention 8)

Your installed SOLVE eX folder has four content zones. Knowing which is which prevents the operator-pulls-and-loses-work failure mode.

### Engine Zone — release-owned; updated by `git pull`

The files that SOLVE eX's release ships:

- Front-door docs: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`
- `00-Instructions/` through `05-Personas/` — engine corpus
- `07-Scripts/`, `08-Schema/` — utility scripts and schema
- `09-Sample-Sessions/`, `10-Reference/` — shipped reference material
- `99-Archive/` — sprint history
- `_types/` — SOLVE-eX's Prototype definitions

**Do not edit Engine Zone files directly.** Updates from `git pull` overwrite them. Customizations belong in `06-Case-Files/` (your case work) or in a fork.

### Operator-Private Zone — gitignored; never tracked

The `.gitignore` excludes:

- Your operator profile (`_USER.md`, if present)
- Active and draft case files (`06-Case-Files/_ACTIVE/`, `06-Case-Files/_DRAFT/`)
- Python and IDE artifacts (`.venv/`, `__pycache__/`, IDE caches)

These never get pushed and never get touched by `git pull`.

### Operator-Extension Zone — your case work; survives `git pull`

This is where your work lives. Cases you run through SOLVE eX become folders under `06-Case-Files/_ACTIVE/`.

`06-Case-Files/_ACTIVE/` and `06-Case-Files/_DRAFT/` are gitignored, so `git pull` never touches them. They're yours.

If you want to track resolved cases (`_RESOLVED/`), `git add -f` per case folder — or maintain a private fork with your case work checked in.

### Shipped Examples Zone — release-owned; updated by `git pull`

- `09-Sample-Sessions/**` — worked-example sessions
- `06-Case-Files/_REFERENCE/**` — reference case files
- `01-Tools/Tool Entries/**` — the canonical 30+ Tool Entries (Thinking Tools library)

**Do not edit Shipped Examples directly.** If you want to riff on a sample session, copy it into your own case-file folder under `_ACTIVE/`.

## 9. Updates and troubleshooting

The canonical update workflow lives in `INSTALL.md § 7`. Common scenarios:

### Clean fast-forward (no local engine modifications)

```bash
cd ~/Operating-Volumes/SOLVE-eX-v<your-major>.<minor>
git fetch origin
git log --oneline HEAD..origin/main          # what's incoming
git pull --ff-only origin main
```

### Fast-forward fails because you have local engine modifications

```bash
git status                                    # see what's modified
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                 # may produce conflicts on engine files you edited
```

If `git stash pop` reports conflicts, the conflict is between *your local edit* of an engine file and *the upstream release's version*. You almost always want the upstream version (engine evolution generally improves what's there):

```bash
git checkout --theirs <conflicting-file>
git add <conflicting-file>
```

### Update lost a file you cared about

`git pull` only updates tracked paths. If a file disappeared, either: (a) the release explicitly removed it (the `CHANGELOG.md` will say so), or (b) it was a gitignored file you forgot was ignored. For (a), the file is recoverable via `git log --all --oneline -- <path>`. For (b), check whether the file matched a `.gitignore` pattern.

### Major.minor folder transition

When the release notes say to rename your folder:

```bash
cd ~/Operating-Volumes/
mv SOLVE-eX-v<old> SOLVE-eX-v<new>
cd SOLVE-eX-v<new>
git status   # should show clean
```

The folder rename doesn't affect git; the rename is for your filesystem clarity.

### Contributing back upstream

To contribute back (open a PR against the upstream SOLVE-eX), re-enable push to *your own fork* (never to upstream):

```bash
# Replace with your fork's URL
git remote set-url --push origin https://github.com/<your-username>/SOLVE-eX.git

# Make a branch, commit, push to your fork, open a PR on GitHub
git checkout -b my-contribution
# ... your changes ...
git commit -m "..."
git push origin my-contribution
```

When you're done contributing, re-disable push to protect your private case work going forward:

```bash
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

## Version

This operator guide ships with SOLVE eX v2.1.2 / master plan v3.0 STABLE.
See `VERSION.md` and `CHANGELOG.md`.
