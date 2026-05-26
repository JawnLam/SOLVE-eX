---
doc_type: schema_reference
audience: ai_and_human
read_order: 2
last_updated: 2026-05-14
generated_from: Master_Schema.yaml
schema_version: "1.15.0"
---

# Facet Enums — Human-Readable Reference

This is the canonical list of legal values for every `tt_*` enum-controlled
facet. **Tool entries must use these exact strings.** Out-of-vocabulary (OOV)
values fail validation in `07-Scripts/validate-tool.py`.

Source: `Master_Schema.yaml` (v1.15.0). Regenerate this file when the schema
bumps.

---

## tt_Type (single-value)

| Value | Meaning |
|-------|---------|
| `instrument` | Fillable, deployable tool with a template / protocol / rubric |
| `stance` | A mode you enter, not an instrument you wield |

---

## tt_Domain (single-value, 12 values)

12 register-clean Domains — each answers "What cognitive register does this
tool operate in?" (Path-B single-axis taxonomy, v1.13.0).

| Value |
|-------|
| `Discursive-analytical` |
| `Modes of inquiry` |
| `Non-discursive cognition` |
| `Embodied / somatic` |
| `Inner / psychological work` |
| `Symbolic systems` |
| `Contemplative` |
| `Generative / improvisational` |
| `Speculative / imaginative` |
| `Emotional cognition` |
| `Aesthetic` |
| `Phronetic / practical wisdom` |

`tt_Cross_Domains` (multi-value, optional) draws from the same enum.

---

## tt_Form (multi-value, 16 values)

How the tool is enacted — the application pattern that governs it. Empty if
`tt_Type = stance` (stances have no Form).

| Value |
|-------|
| `Matrix` |
| `Checklist` |
| `Dialogue protocol` |
| `Scoring rubric` |
| `Mental model` |
| `Visualization technique` |
| `Sequenced workflow` |
| `Question bank` |
| `Canvas` |
| `Decision tree` |
| `Narrative template` |
| `Heuristic` |
| `Algorithm` |
| `Mnemonic` |
| `Game / simulation` |
| `Practice / ritual` |

---

## tt_Scale (multi-value, 7 values)

| Value | Meaning |
|-------|---------|
| `Solo` | One person, thinking alone |
| `Dyadic` | Two people |
| `Small group` | 3–10 |
| `Large group` | 10–100 |
| `Organizational` | 100+ within an organization |
| `Inter-organizational` | Across organizations |
| `Civilizational` | Cross-society or cross-era |

---

## tt_Duration (multi-value, 5 values)

| Value | Meaning |
|-------|---------|
| `Snap` | Sub-minute (gut check, intuitive judgment) |
| `Single session` | 5 min – 2 hr |
| `Workshop` | Half-day to multi-day |
| `Project` | Weeks to months |
| `Practice` | Lifelong / ongoing discipline |

---

## tt_Lineage (multi-value, 15 values)

Intellectual / cultural tradition that produced or carries the tool.

| Value |
|-------|
| `Western analytic / academic` |
| `Eastern philosophical` |
| `Indigenous / oral traditions` |
| `Industrial / business` |
| `Military / strategic` |
| `Therapeutic / psychological` |
| `Design / craft tradition` |
| `Ancient Greek / Roman` |
| `Religious / monastic` |
| `Scientific method` |
| `Mathematical / formal` |
| `Folk / vernacular` |
| `Modern productivity / self-help` |
| `Legal / juridical` |
| `Medical / clinical` |

---

## tt_Posture (multi-value, 9 values)

Engagement stance the tool requires of the practitioner.

| Value |
|-------|
| `Collaborative-willing` |
| `Adversarial-tolerant` |
| `Solo-quiet` |
| `Somatically-regulated` |
| `Time-pressured-OK` |
| `Trust-required` |
| `Low-stakes-only` |
| `Beginner-friendly` |
| `Expert-required` |

---

## tt_State (multi-value, 7 values, OPTIONAL)

Psychological/phenomenological state the tool asks the practitioner to enter
or sustain. Distinct from posture (a stance the practitioner takes) and from
agent (who is doing the thinking).

| Value |
|-------|
| `Liminal` |
| `Flow` |
| `Playful` |
| `Numinous` |
| `Contemplative-quiet` |
| `Speculative-imaginative` |
| `Heightened-vigilant` |

---

## tt_Agent (multi-value, 6 values, OPTIONAL)

Type of cognitive agent doing the work. Distinct from `tt_Scale` (how many).

| Value |
|-------|
| `Solo human` |
| `Human group` |
| `Crowd / market` |
| `Human-AI partnership` |
| `Cross-species` |
| `Cross-cultural` |

---

## tt_About (multi-value, 14 values, OPEN-EXTENSIBLE)

Broad subject-of-thought categories. Open-extensible **only at the ≥10-tool
applicability threshold**; do not silently add singletons.

| Value |
|-------|
| `Self / identity` |
| `Other / relationship` |
| `Group / organization` |
| `Power / politics` |
| `Ethics / values` |
| `Strategy / competition` |
| `Decision / choice` |
| `Risk / uncertainty` |
| `Time / future` |
| `Place / ecosystem` |
| `Body / embodiment` |
| `Mind / cognition` |
| `Sacred / transcendent` |
| `Aesthetic / craft` |

---

## tt_SOLVE_eX_Phase (multi-value, 7 values)

| Value | Phase |
|-------|-------|
| `1` | State / Origin clarification |
| `2` | Objective / Destination clarification |
| `3` | Learn / fact-gathering |
| `4` | Vision / divergent path generation |
| `5` | Evaluate / convergent option assessment |
| `6` | eXecute / action and follow-through |
| `any` | Cross-phase utility |

---

## tt_SOLVE_eX_Step (multi-value, 22 values)

Granular step-level affinity. All 21 SOLVE eX steps plus `any` for
cross-step utility.

| Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6 | Cross |
|---------|---------|---------|---------|---------|---------|-------|
| `1.1` | `2.1` | `3.1` | `4.1` | `5.1` | `6.1` | `any` |
| `1.2` | `2.2` | `3.2` | `4.2` | `5.2` | `6.2` |       |
| `1.3` | `2.3` | `3.3` | `4.3` | `5.3` | `6.3` |       |
|       |       | `3.4` | `4.4` |       | `6.4` |       |

---

## tt_Clarifies (multi-value, 5 values)

Which segment of the user's decision journey the tool clarifies. First-cut
filter in the Tool Selector.

| Value | Meaning |
|-------|---------|
| `Origin` | Tool clarifies the user's current state |
| `Destination` | Tool clarifies the user's target state |
| `Path` | Tool charts routes between Origin and Destination |
| `Action` | Tool supports executing and following up on chosen path |
| `None` | Tool is structural or about the meta-process |

---

## tt_Applicability (single-value, 3 values)

Whether the v2.0 AI can guide enactment in-session.

| Value | Meaning |
|-------|---------|
| `runtime_applicable` | AI can guide the user through the tool in chat |
| `describable_only` | AI can describe the tool but cannot guide in-session |
| `requires_tradition_transmission` | Tool requires teacher / lineage transmission |

---

## tt_Status (single-value, 4 values)

| Value | Meaning |
|-------|---------|
| `proposed` | Name only; no entry yet |
| `in-progress` | Entry being drafted |
| `classified` | Entry exists with full content |
| `deprecated` | Replaced by another tool or no longer recommended |

---

## tt_Quality_Tier (single-value, 4 values) — added v1.15.0

Curated quality assessment, independent of `tt_Status`. A tool can be
`A`-tier and `experimental`, or `D`-tier and `active`. The tiering is
*curated quality*; the status is *lifecycle*.

| Value | Meaning |
|-------|---------|
| `A` | High-quality, well-vetted, frequently load-bearing in real sessions |
| `B` | Solid; appropriate fit for most use cases |
| `C` | Workable; included for completeness; check fit carefully |
| `D` | Marginal; included for breadth; consider alternatives first |

Tier-aware ranking is implemented in `find-tools.py`: by default,
results are ranked `A > B > C > D` when other facets are equal. Pass
`--no-tier-sort` to disable, or `--tier A` to filter to a specific tier.

---

## Operations (open-but-curated, 36 canonical values)

`tt_Operation` is a free-string field per `Master_Schema.yaml`, but the
canonical inventory locked in Sprint 05's Saturation Sweep + Buddhist-contemplative
corpus test contains 36 values. New entries should re-use existing operations
where possible; new operations are added only when the cognitive move is
genuinely distinct and applies to ≥10 tools.

Canonical inventory lives in `{ROOT}/01-Tools/Index of Thinking Tools.md`.
A representative subset:

`Frame the problem` · `Decompose hierarchically` · `Map causes and effects` ·
`Score and rank options` · `Surface assumptions` · `Test against criteria` ·
`Generate alternatives` · `Compare side-by-side` · `Cultivate emotion` · …

When in doubt, **use an existing Operation rather than invent a new one**.
Operation drift was the silent failure mode of Sprint 01 (cleanup of 13
entries required at Card 14 verification).
