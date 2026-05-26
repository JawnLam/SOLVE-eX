---
doc_type: reference
doc_purpose: glossary
audience: ai_and_human
read_order: 0
last_updated: 2026-05-13
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

**Item_Prototype.** Schema discriminator. For tool entries, this is
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
