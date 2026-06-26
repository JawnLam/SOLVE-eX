---
doc_type: reference
doc_purpose: glossary
audience: ai_and_human
read_order: 0
last_updated: 2026-05-29
---

# Glossary

Definitions for terms used throughout the SOLVE eX v2.0 system.

---

**Action plan.** A concrete, time-bound sequence of steps the user
commits to executing as the outcome of Phase 6.2. Distinct from the
chosen path (which is the strategic direction) — the action plan
operationalizes the path.

**Active frame.** The frame at the top of the goal-stack. Only one
frame is active at a time. Tracked in Case File frontmatter as
`active: true`.

**Application pattern.** The shape of how a tool is applied
conversationally — matrix-filling, sequenced-workflow-walking,
dialogue-protocol-running, etc. One pattern per `tt_Form` value (plus
one for `tt_Type: stance`). See `{ROOT}/04-Application-Patterns/`.

**Bootstrap protocol.** The deterministic script for the AI's first
response and first 2–3 turns of any session. See chapter 02.

**Case File.** The durable per-session artifact. Markdown file with
YAML frontmatter plus structured body sections. Source of truth for
everything the user has said and everything the system has decided in
the session. See chapter 06.

**Clarification need / `tt_Clarifies`.** Which segment of the user's
decision journey a tool clarifies: Origin, Destination, Path, Action,
or None. First-cut filter in the Tool Selector.

**Clarity state.** One of four states an endpoint (Origin or
Destination) can be in: Unclear, Partially-clear, Clear-but-unstable,
Locked. Re-assessed every turn.

**Consultant (persona).** Operational mode for decisive, time-pressured
moments. Direct, structured. Phase 2 persona; MVP approximates with
crisper Partner.

**Counselor (persona).** Operational mode for values tension and hard
tradeoffs. Probing, slow, asks more than tells.

**Destination.** "Where the user wants to be." The target endpoint of a
frame. Distinct from Origin (where the user is) and from Path (how to
get from one to the other).

**Diagnostic loop.** The per-turn procedure run by the AI. Ten steps;
produces an updated Case File state, a response strategy, and a
response in the active persona's voice. See chapter 03.

**Frame.** A discrete question with its own Origin, Destination, and
phase-step. Sessions may have multiple frames in a recursive
goal-stack. See `02-Process-Framework/04-recursion-semantics.md`.

**Frame lifecycle.** The states a frame moves through: Created →
Active (3 sub-states) → Resolved / Paused / Abandoned / Failed →
Popped. See `02-Process-Framework/06-frame-lifecycle.md`.

**Goal-stack.** The ordered list of frames a session has touched.
Only the top frame is active. Stored in Case File frontmatter as
`goal_stack`.

**Guide (persona).** Operational mode for orienting the user in
unfamiliar territory. Patient, instructional. Phase 2 persona; MVP
approximates with explicitly-instructional Partner.

**Hallucination prevention.** Rules that prevent the AI from inventing
user details. The Case File is source of truth; ask if unsure rather
than fabricate. See chapter 06 §6.10 and chapter 09 §9.5.

**Item_ID.** Unique identifier for a tool entry, formatted as
`tt-{kebab-title}`. Required schema property.

**type.** Schema discriminator. For tool entries, this is
always `Thinking_Tool`. Required schema property.

**Jump.** A motion that returns the active frame to an earlier
phase-step (without popping the frame). Triggered by new information
that invalidates a prior step's artifact. See `05-push-pop-rules.md`.

**Master_Schema.yaml.** The single source of truth for the data model
governing tool entries. Lives in `{ROOT}/08-Schema/`. Downstream from
the Obsidian Vault infrastructure of the same name.

**Operating Manual.** The thirteen chapters in `{ROOT}/00-Instructions/`.
MVP ships six of thirteen (00, 01, 02, 03, 06, 09); Phase 2 adds the
remaining seven.

**OOV (out-of-vocabulary).** A value used in a schema-controlled facet
that is not on the canonical enum list. OOV values fail validation in
`validate-tool.py`. The most common bug class in tool authoring.

**Origin.** "Where the user is." The starting endpoint of a frame.
Distinct from Destination (where they want to be).

**Partner (persona).** Default operational mode. Collaborative,
exploratory, moderate pace. The persona most of any session is in.

**Path.** The route between Origin and Destination within a frame. The
work of Phases 3–5 charts the path; the work of Phase 6 executes it.

**Persona.** One of five operational modes the AI inhabits at a time:
Partner, Counselor, Therapist, Guide, Consultant. Operational roles,
not character or personality. See chapter 05.

**Phase.** One of six SOLVE eX phases: State, Objective, Learn, Vision,
Evaluate, eXecute. Phases break into 21 steps. See
`02-Process-Framework/01-the-six-phases.md`.

**Phase-step.** A specific step within a phase (e.g., 2.2 = "Write the
Goal Statement"). 21 steps in total. The granular routing facet for
tools (`tt_SOLVE_eX_Step`).

**Pop.** A motion that closes the current sub-frame and returns the
parent frame to active. Triggered when the sub-frame's Destination is
Locked or when the user explicitly asks to return.

**Pre-Mortem.** A specific tool: imagine the plan failed, identify
causes, rank by likelihood, design safeguards. Used in Phase 5.3
validation work.

**Push.** A motion that opens a sub-frame, making the current frame
paused. Triggered when a prerequisite question must be answered before
the current question can resolve.

**Quick_Notes.** Optional human-readable one-paragraph summary in a
tool entry's frontmatter. Surfaces in `find-tools.py --verbose`.

**Resumption protocol.** The Case File's procedure for resuming a
session days or weeks later. The AI reads the Case File, runs the
resumption check ("Last time we'd been working on X; want to pick up
there or has something changed?"), waits for the user's direction. See
chapter 06 §6.5.

**Schema version.** The version of `Master_Schema.yaml`. MVP ships
schema v1.14.0 (locked Sprint 05). Case Files carry their own
`schema_version` field.

**Section markers.** HTML comment markers in markdown files that the
AI can grep to retrieve specific blocks without reading whole files.
Example: `<!-- SECTION: ORIGIN_CLARIFICATION_OPENING_QUESTIONS -->`.

**SOLVE eX.** The methodology (six phases / twenty-one steps) and the
v2.0 implementation built around it. Original SOLVE eX source docs
live in `{ROOT}/02-Process-Framework/source-material/`.

**Stakes flags.** Per-session list of safety-relevant events. Recorded
in Case File frontmatter as `stakes_flags`. See chapter 09.

**Stakes routing.** The chapter 09 protocol for stopping process work
and routing the user to appropriate professional services when a
high-stakes signal fires.

**Step.** A specific procedural unit within a Phase. The SOLVE eX
methodology has 21 steps across 6 phases.

**Stress-test.** A move that probes whether an endpoint's clarity is
stable. Examples: restating the endpoint from a different angle, posing
an obvious counter-argument, projecting forward 6 months. Moves an
endpoint from Clear-but-unstable to Locked.

**Therapist (persona).** Operational mode for emotionally activated
users. Mirroring, validating, very slow. Companion mode for non-
clinical distress; chapter 09 takes over for clinical-grade
situations.

**Tool (thinking tool).** An entry in `{ROOT}/01-Tools/Tool Entries/`.
A discrete cognitive instrument with structured `tt_*` metadata.
v1.14.0 schema. 677 entries.

**Tool entry.** A single tool's documentation file. YAML frontmatter
plus markdown body (Purpose, How To Use, Sources, etc.).

**Tool Library.** The full set of 677 tool entries. Lives in
`{ROOT}/01-Tools/Tool Entries/`.

**Tool Selector.** The algorithm that selects tools given Case File
state. Operates on `tt_Clarifies` → `tt_SOLVE_eX_Phase/Step` → user
context → applicability → diversity. See chapter 01 §1.6.

**tt_ namespace.** The schema prefix for Thinking Tool properties.
`tt_*` properties are governed by `Master_Schema.yaml` and validated
by `validate-tool.py`.

**Validation rules.** The rules enforced by `validate-tool.py`. See
`{ROOT}/08-Schema/validation-rules.md`.

**`{ROOT}`.** Placeholder for the absolute path to the SOLVE eX folder.
The AI substitutes this at session start with the actual path. Used in
all instructional references to enable path-independence.

---

## ADAPT Loop — 19 Theoretical Categories (Lam 2020)

The academic vocabulary underlying the ADAPT-Loop tool family
(`Actor-Agenda Decomposition`, `Required-Resource Check`, `Decision
Matrix Construction`, `Bet vs Workhorse Discrimination`, `Perception
and Actual Effect Gap Audit`, `Disciplined Hold`, `9-Resource Portfolio
Diagnostic`, `Nested Sub-Cycle Discipline`, `Mid-Cycle Interest
Pivot`, `Cross-Actor Matrix Reading`, `Iterated Loop Compounding`,
`Calibration Gap Read`), the `pattern-adapt-loop-multi-cycle-strategic-action`
application pattern, and the operator-facing field manual at
`{ROOT}/10-Reference/ADAPT-Loop-Field-Manual.pdf`. Each category has a
formal definition in the dissertation (Lam, J. (2020). *The Accumulation,
Utilization, and Protection of Political Capital by Senior Executives of
For-Profit Organizations.* Doctoral dissertation, Pepperdine University).
Page citations below are dissertation pages.

---

### 19 Theoretical Categories (alphabetical)

**Action (ADAPT).** Political activity or influence tactic performed
to create effect on the target's decision matrix. The bridge from
planning zone to consequence zone — the irreversible step. (Lam 2020
p. 155.) Operationalized in `Required-Resource Check` (pre-flight) and
the ADAPT application pattern (post-flight).

**Actor (ADAPT).** A person or group capable of decisions. The
initiator of an interaction cycle by spending a resource to perform an
action. The unit of analysis in the framework. (Lam 2020 p. 150.)
Operationalized in `Actor-Agenda Decomposition` as the funnel's top
layer.

**Actual effect (ADAPT).** The real alteration of the target's
decision matrix produced by the action — often opaque to the actor and
frequently differing from the intended effect. (Lam 2020 p. 156.)
Operationalized in `Perception and Actual Effect Gap Audit` as the
post-action diagnostic that distinguishes actual from perceived
utility.

**Adverse alternative(s) / AA (ADAPT).** The actor-opposed option(s)
in the decision matrix; the fallback if the preferred position fails.
Multiple AA's possible; each scored on benefit, cost, utility. The
matrix's discipline is in the AA, not the PP. (Lam 2020 p. 153.)
Operationalized in `Decision Matrix Construction`.

**Benefits (ADAPT).** Favorable conditions in the decision matrix
apportioned by option. The B in B(PP) and B(AA). (Lam 2020 p. 153.)
Operationalized in `Decision Matrix Construction`.

**Component (ADAPT).** Intersection unit of the decision matrix —
e.g., "Benefit of Preferred Position" = one of four-plus components.
Also: constituent parts of an action (a memo, a meeting, a phone call)
— what the action actually consists of. (Lam 2020 p. 153.)
Operationalized in `Decision Matrix Construction`.

**Considerations (ADAPT).** The two appraisal axes of the decision
matrix: aggregate benefits and aggregate costs. (Lam 2020 p. 153.)
Operationalized in `Decision Matrix Construction`.

**Costs (ADAPT).** Requisite expenditures in the decision matrix
apportioned by option. The C in C(PP) and C(AA). (Lam 2020 p. 153.)
Operationalized in `Decision Matrix Construction`.

**Decision matrix (ADAPT).** Set of options (two-plus) × two
considerations (benefits + costs) = at least four components. Every
move has two possible futures — preferred position and adverse
alternative. The right reading is to compare the U(PP) / U(AA) pair
across options, not pick highest U(PP) alone. (Lam 2020 pp. 152-153.)
Operationalized in `Decision Matrix Construction`.

**Detection (ADAPT).** The actor's observation / evaluation
discovering (a) who owns / controls the resource of interest and (b)
the composition of that person's decision matrix. The "reading the
room" phase that precedes intent formation. (Lam 2020 p. 151.)
Operationalized in `Cross-Actor Matrix Reading`.

**Goal (ADAPT).** The specific measurable result that satisfies an
objective. Where an objective can be described, a goal can be
measured. ("Be one of the seven named members in the charter when it
is published next month.") (Lam 2020 p. 156.) Cross-references the
SOLVE eX system vocabulary at Phase 2 Goal Statement (step 2.2 — see
`02-Process-Framework/02-the-twenty-one-steps.md`); the ADAPT Goal is
the political-action analog of the SOLVE eX Phase 2 Goal Statement.
Operationalized in `Actor-Agenda Decomposition`.

**Interest (ADAPT).** What an agenda produces at the moment —
situational, changeable, lower-stakes than agenda. Losing an interest
is recoverable; threatening an agenda is not. (Lam 2020 p. 154.)
Operationalized in `Actor-Agenda Decomposition`.

**Options (ADAPT).** The available moves the actor can score in the
decision matrix; actor-centric labeling as preferred positions or
adverse alternatives. (Lam 2020 p. 153.) Operationalized in `Decision
Matrix Construction`.

**Outcome (ADAPT).** The settled result of a cycle: future state from
target's selection, including resource payout to actor and utility
delivered to target. Feeds the resource loop and the learning loop
into the next cycle. (Lam 2020 p. 156.) Cross-references SOLVE eX
Phase 6 outcome-assessment vocabulary (Phase 6.3 — "did the action
land as intended" review; see `02-Process-Framework/01-the-six-phases.md`);
the ADAPT Outcome is the iterated-cycle structural unit that the SOLVE
eX Phase 6 assessment audits per-frame. Operationalized in
`Iterated Loop Compounding`.

**Perception (ADAPT).** What the actor believes they got, filtered
through hope, defensiveness, ego, prior belief. Distinct from actual
utility; the gap between them is the framework's quiet but central
error term. (Lam 2020 p. 156.) Operationalized in `Perception and
Actual Effect Gap Audit`.

**Preferred position(s) / PP (ADAPT).** Actor-favored option(s) in
the decision matrix. Multiple PP's possible with hierarchy (e.g., P1
"voluntary departure" preferred over P2 "fire-with-cause"). Scored on
benefit, cost, utility. (Lam 2020 p. 153.) Operationalized in
`Decision Matrix Construction`.

**Resources (ADAPT).** Means to perform action. Nine-type taxonomy:
Money, Hard Assets, Credibility, Attributes, Legitimacy, Information,
Access, Title, Tribe (see sub-entries below). Distinguish
intrinsic-value resources from politically-useful resources — those
that compound. (Lam 2020 pp. 154-156.) Operationalized in
`9-Resource Portfolio Diagnostic`; adjacent to `Real Options Analysis`
(formalizes option-value of unspent resources across cycles) and
`Theory of Constraints` (identifies which resource is the binding
constraint on the current cycle's throughput).

**Target (ADAPT).** The thing or person the actor must move to
achieve the goal. Closes the interaction cycle by selecting an option
after appraising net utility. Skipping target identification is one
of the most common failure modes the framework exposes. (Lam 2020
p. 151.) Operationalized in `Actor-Agenda Decomposition`.

**Utility (ADAPT).** Net difference benefits − costs per option.
Three kinds of utility — Expected (matrix prediction), Actual (real
value delivered), Perceived (what the actor believes they got) — are
easily confused and rarely equal. Distinguishing them is the
framework's single most important discipline. (Lam 2020 p. 153.)
Operationalized in `Perception and Actual Effect Gap Audit` and
`Decision Matrix Construction`.

---

### 3 Framing Wrappers

The dissertation's three framing wrappers organize the planning
funnel. They are categorically distinct from the 19 categories above
but cross-link the same ADAPT vocabulary.

**Agenda (ADAPT).** The actor's long-running ambition — a collection
of multiple interests organizing everything else. Rarely stated
openly, often misidentified by observers. Cycles run sequentially or
in parallel under one agenda. The most stable layer of the planning
funnel — get the agenda wrong and every prediction below it will
drift. (Lam 2020 p. 154.) Operationalized in `Actor-Agenda
Decomposition`.

**Objective (ADAPT).** A concrete aim that serves the interest. The
first thing on the funnel that can be written down without ambiguity.
("Win the seat on the steering committee" is an objective; "have more
influence" is not.) The transition from interest to objective is often
where actors lose their way. (Lam 2020 p. 154.) Operationalized in
`Actor-Agenda Decomposition`.

**Intention (ADAPT).** The actor's formulated impact on the target's
perception of the decision matrix. The bridge between objective and
action. What the actor proposes to make the target see differently.
(Lam 2020 p. 154.) Operationalized in `Actor-Agenda Decomposition`.

---

### 9 Resource Sub-Types

Sub-entries under the ADAPT Resources category. Each is one of the
nine types `9-Resource Portfolio Diagnostic` audits across.

**Resources sub-type 1: Money (ADAPT).** Capital available for direct
exchange; the most fungible resource and the most commonly
over-weighted in resource self-assessment.

**Resources sub-type 2: Hard Assets (ADAPT).** Physical goods or
property under the actor's control; less fungible than money but more
stable.

**Resources sub-type 3: Credibility (ADAPT).** The actor's track
record of delivering what they commit to. A politically-useful
resource because it compounds across cycles.

**Resources sub-type 4: Attributes (ADAPT).** Personal capacities
(intelligence, judgment, social skill, charisma) that travel with the
actor and produce ongoing convertibility.

**Resources sub-type 5: Legitimacy (ADAPT).** Standing to act on
behalf of an interest — formal authority, role-based permission,
sanctioned representation.

**Resources sub-type 6: Information (ADAPT).** Knowledge of facts,
relationships, agendas, decision-matrix compositions that the actor
controls or can access asymmetrically.

**Resources sub-type 7: Access (ADAPT).** Ability to reach decision
makers directly — meeting time, communication channels, calendar
priority — independent of formal title.

**Resources sub-type 8: Title (ADAPT).** Formal role, position, rank
in the organizational hierarchy. Produces legitimacy and access but
is bounded by tenure.

**Resources sub-type 9: Tribe (ADAPT).** The coalition of others who
will reliably support the actor. A politically-useful resource because
it amplifies all other resources and is the hardest to deplete.
Cross-references SOLVE eX Phase 4 stakeholder vocabulary (Phase 4.2 —
divergent stakeholder mapping; see `02-Process-Framework/01-the-six-phases.md`);
the ADAPT Tribe is the durable-coalition reading of the same surround
that the SOLVE eX Phase 4 stakeholder pass enumerates.

---

**Recursive prescription (Lam 2020 p. 226).** *Control the resources
that facilitate the ability and opportunity to control more
resources.* Not all resources hold equal value — politically useful
resources are those that compound. The 9-type lens recovers
Credibility, Attributes, Information, Access, Tribe — the resources
that most users under-weight by defaulting to Money + Title reasoning.
