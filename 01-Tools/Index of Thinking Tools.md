# Index of Thinking Tools

> **Status:** v1.6 — 2026-05-15 *(schema v1.15.0 — SOLVE eX v2.0 Calibration Sprint Sophisticated-User Mode complete; +1 new entry (Conviction vs Argument); 678 entries populated; pairwise occupancy 63.7%; all 112 Fields and 36 Operations populated)*
> **Purpose:** A "Library of Congress" of thinking tools. The 26 SOLVE eX tools were the seed; the library now contains 678 classified cognitive instruments organized into 12 register-clean Domains, 112 Fields, 36 Operations, and 13 cross-cutting facets (9 pre-v1.14 + 4 added in v1.14 for SOLVE eX v2.0 Co-pilot routing) — every Field and every Operation populated by ≥1 entry, pairwise occupancy at 63.7% across 55 facet-pairs.

## Changelog

- **v1.6 (2026-05-15):** SOLVE eX v2.0 Calibration Sprint Sophisticated-User Mode (Sprint 10) — added **Conviction vs Argument** (`tt-conviction-vs-argument`) as a new tool entry. Original to SOLVE eX, surfaced via the Sprint 09 panel-test self-debrief on the Dr. Renata Mendes-Olufemi case (regional VP healthcare ops; rural hospital closure decision). The tool codifies the conviction-vs-argument distinction for decisions involving asymmetric quantifiability — when one side of a tradeoff is precisely measurable and the other is statistically distributed, the personal data point on the distributed side is calibration-correction rather than bias to suppress. Facet placement: `tt_Domain: Modes of inquiry`, `tt_Field: Decision under uncertainty`, `tt_Operation: Surface assumptions` (canonical match; the tool's core move is surfacing the implicit assumption that personal data = bias), `tt_Form: [Mental model]`, `tt_SOLVE_eX_Phase: [4, 5]`, `tt_SOLVE_eX_Step: [4.1, 5.1]`, `tt_Clarifies: [Origin]`, `tt_Applicability: runtime_applicable`, `tt_Quality_Tier: B` (promotable to A after corpus-usage evidence), `tt_Pairs_Well_With: [Pre-Mortem, Stakeholder Power-Interest Grid]`. Library count goes 677 → **678**. Validation: `validate-tool.py` passes with 0 errors and 0 warnings. Sprint outputs: master plan Part 17.10 (Sprint 10 scope codification, v2.4 revision); chapter 13 amendment (sophisticated-user detection self-check + voice-neutrality two-question revision); chapter 03 step 8a amendment (relaxed-scaffolding scope-statement variant + derived-content-recommendation cross-reference + direct-read principle); chapter 04 §4.3.2 (tool-naming adaptation for relaxed-scaffolding mode + `tools_applied_this_session` counter); chapter 10 Rule 0a (high-leverage single question permission); persona-consultant §"The derived-content-recommendation move" (operator-mode repertoire entry); sample-11 sophisticated-user (NEW canonical reference session); D-tier population sweep (Sprint 08 deferred). Sprint 10 acceptance gate: panel re-test on two fresh cases (one sophisticated-user → detection fires; one user-needs-scaffolding → detection does NOT fire; ambiguous boundary case for calibration verification). No schema regressions.

- **v1.5 (2026-05-13):** SOLVE eX v2.0 Schema Foundation complete (Sprint 05). Master_Schema bumped v1.13.0 → **v1.14.0** with four new facets added to support the v2.0 AI-orchestrated decision-making companion's Tool Selector: (1) `tt_SOLVE_eX_Phase` (multi-value enum [1, 2, 3, 4, 5, 6, any]) — which SOLVE eX 6-phase(s) the tool is useful for, primary Phase-Step affinity routing facet; (2) `tt_SOLVE_eX_Step` (multi-value enum [1.1 through 6.4, any]) — granular 19-step affinity, more precise than Phase; (3) `tt_Clarifies` (multi-value enum [Origin, Destination, Path, Action, None]) — first-cut filter for the Tool Selector, restricting tool suggestions to the segment of the user's decision journey currently needing clarification (when Destination is Unclear, the Selector restricts to `tt_Clarifies: Destination` tools); (4) `tt_Applicability` (single-value enum [runtime_applicable, describable_only, requires_tradition_transmission]) — capability gate for the v2.0 Co-pilot: whether it can guide the user through the tool in-session, only describe it, or whether the tool requires teacher/lineage transmission. All 4 facets registered in the `Thinking_Tool` prototype's `specific_keys`. Schema regressions: **zero** — no existing facets, enums, or prototypes were modified. **All 677 entries populated** with all 4 new facets via heuristic-based bulk classifier (`/tmp/sprint05_audit.py` + `/tmp/sprint05_write_batch.py`) driven by an assignment rubric (Card 02) defining decision rules per facet plus 20 worked examples spanning all 12 Domains. Final audit: zero YAML parse errors, zero OOV violations, zero missing new facets across all 677 entries. Bucket distribution across Cards 04-10: Card 04 (Phase 1 / Origin) 122 entries · Card 05 (Phase 2 / Destination) 25 entries · Card 06 (Phase 3 / Learn) 205 entries · Card 07 (Phase 4 / Vision) 118 entries · Card 08 (Phase 5 / Evaluate) 141 entries · Card 09 (Phase 6 / Execute) 8 entries · Card 10 (cross-phase utilities + stance tools + Contemplative tradition-locked practices) 58 entries. Sprint did not add or remove any tool entries; corpus count remains at 677. Library is now v2.0-ready: the schema supports the Co-pilot's runtime routing decisions (Phase-Step affinity + first-cut Clarifies filter + capability gate). Sprint outputs: `/tmp/sprint05-assignment-rubric.md` (Card 02 rubric + 20 worked examples), `/tmp/sprint05-final-audit.md` (Card 11 6-gate audit report), `/tmp/sprint05-batch-04-updates.md` through `/tmp/sprint05-batch-10-updates.md` (per-batch write logs). **One outstanding housekeeping item** flagged for v1.15 or a future sprint: the v1.13.0 facets `tt_State` / `tt_Agent` / `tt_About` were never registered in `Thinking_Tool.specific_keys` (only added to `properties:`); Sprint 05 only added the 4 new v1.14 facets to specific_keys, preserving the existing inconsistency. Recommend correction in a follow-up schema housekeeping pass.

- **v1.4 (2026-05-12):** Reverse-Audit complete (Sprint 04 — Thinking Tools Reverse-Audit Against External Collections). Corpus grew 483 → **675** (+192 new entries) via reverse-audit of 21 external authoritative collections in 3 tiers. **Schema saturation milestone: every one of the 112 canonical Fields and all 36 canonical Operations now has ≥1 corpus entry** (was 76 Fields / 20 Operations pre-sprint). Methodology was inverse to Sprints 01/03: instead of starting from the schema and looking for empty cells, Sprint 04 enumerated named tools in authoritative external collections (Tier 1: Munger / FS / Decision Book / Wikipedia / Cambridge Handbook; Tier 2: TRIZ + OR + Causal Inference + DOE + System Dynamics + Game Theory + Information Theory + FCA + Lean+Six Sigma; Tier 3: PKM + Foresight + IFS + ACT-DBT + Negotiation + Book of Why + Model Thinker). Coverage achieved: Tier 1 ~92% (target ≥90%), Tier 2 ~95% (target ≥75%), Tier 3 ~95% (target ≥60%). Major class-coverage additions: full Combinatorial / Morphological / FCA family (Morphological Analysis, FCA, t-way Combinatorial Testing, Theoretical Saturation, Constant Comparative — the class Sprint 04 was launched to address); full TRIZ toolkit decomposed into 12 distinct entries (40 Principles, ARIZ, IFR, S-curve, Trends of Engineering Evolution, Su-Field, 9-Windows, STC, Function Analysis, Trimming, Resource Analysis, Separation Principles, Contradiction Matrix); Senge's 9 system archetypes (8 missing pre-sprint); causal inference identification strategies (do-calculus, backdoor, frontdoor, RDD, DiD, propensity score, mediation, synthetic control, g-methods, SCM); DBT skills decomposed (TIPP, DEAR MAN, GIVE, FAST, Wise Mind, Radical Acceptance); IFS toolkit decomposed (6Fs, Parts Mapping, Self-Energy); MI techniques decomposed (OARS, DARN-CAT, Change Talk Elicitation); pedagogical methods (Montessori, ZPD, Bloom Taxonomy + Mastery, PBL, Flipped, Socratic, Harkness, IBL, Direct Instruction); legal-interpretation schools (Originalism, Textualism, Purposivism, Living Constitution, Legal Realism); hermeneutic methods (Gadamer, Schleiermacher, Ricoeur, Midrash, Medieval Fourfold); Lean/TPS specifics (DMAIC, PDCA, VSM, Kanban, Kaizen, Hoshin, Jidoka, Poka-Yoke, Toyota Kata); Voss negotiation micro-skills (Tactical Empathy, Mirroring+Labeling, Calibrated Questions, Accusations Audit); decision/strategy canon (Pareto, Power-Law Reasoning, First-Principles, Second-Order, Circle of Competence, Opportunity Cost, Sunk Cost, Map-Territory, Five Whys, Occam's Razor, Hanlon's Razor, Probabilistic Thinking, Skin in the Game, Lindy, Network Effects, BCG, Ansoff, 7S, AIDA, Marketing 4Ps, Johari Window, Csikszentmihalyi Flow, Drama Triangle, Six Thinking Hats, World Café, Mind/Concept Mapping, Means-Ends, Affinity Diagram); information theory (Shannon Entropy, Mutual Information, KL Divergence, Max Entropy, MDL); network science (Community Detection, Preferential Attachment, Small-World, Bayesian Persuasion); GTD family (GTD, Weekly Review, Two-Minute Rule, Smart Notes Workflow, Evergreen Notes); foresight family (Scenario Planning, Wind Tunneling, STEEP/PESTEL, Hype Cycle); plus Statistical Process Control, ESS / Evolutionary Game Theory, Shapley Value, Subgame Perfect Equilibrium, Backward Induction, Mixed-Strategy, Mechanism Design, Signaling Games, Repeated Games / Folk Theorem, Tit-for-Tat, Bayesian Games, Tradeoff Analysis, Reference Class Forecasting, Outside View, Steelmanning, Ecosystem Thinking, Evolutionary Reasoning, Red Queen, Hick's Law, Diminishing Returns, Maslow's Hierarchy, Iceberg Model, Hysteresis, Activation Energy, Forcing Function, Marginal Analysis, Comparative Advantage, PMI, COM-B, Behavior Change Wheel, Transtheoretical Stages of Change, OKRs, Pomodoro, Convexity-Concavity, Compounding, Regression to the Mean, Tipping Point. **Schema regressions: zero.** Every Sprint 04 candidate mapped to canonical v1.13.0 Fields/Operations/Lineages — Sprint 04's clean schema-saturation result strongly validates the v1.13.0 schema design as structurally complete for the named-thinking-tool space. Pairwise occupancy improved 60.6% → **63.7%** (+3.1 pp; 226 facet-pair cells closed). Cumulative across Sprints 01+03+04: 48.6% → 63.7% (+15.1 pp; 1,078 cells closed; corpus 294 → 675). Sprint outputs: `pairwise-matrix.md` (regenerated), `pairwise-outliers.md` (cumulative S01+S03+S04 narrative), `external-audit-register.md` (per-source diff + coverage %), `sprint04-schema-proposal.md` (zero changes), `/tmp/sprint04-audit-summary.md`. **Anti-V'Ger checkpoint:** Sprint 04 was the last planned saturation sprint barring discovery of a new audit methodology. Schema is structurally saturated; external-collection coverage exceeds target on every tier; corpus contains the methodology used to evaluate its own saturation (Theoretical Saturation, Constant Comparative Method, Pairwise t-way Testing, Morphological Analysis, FCA) — recursive completion.

- **v1.3 (2026-05-12):** Deep-Gap Backfill complete (Sprint 03 — Thinking Tools Deep-Gap Backfill). Corpus grew 374 → **483** (+109 new entries) targeting Sprint 01's Category C "coherent and reachable" gaps. Coverage expansion across: 10 Indigenous traditions (Hawaiian Hoʻoponopono + Lōkahi, Quechua Ayni + Pacha + Quipu + Ukhu, Inuit IQ + Inuksuk, Mesoamerican Tonalamatl + Flower-and-Song + Maya math, Maori Whakapapa + Mauri, Aboriginal Yarning, Lakota Medicine Wheel, Polynesian Etak, Cherokee Harmony, Sámi Joik); Hindu/Vedantic/Tantric sub-traditions (Sankhya, Mimamsa, Kashmir Shaivism, Sri Vidya Tantra, Advaita Vedanta, Patanjali Pratyahara, Bhakti, Bhagavad Gita Saamya); Buddhist sub-traditions (Goenka, Pure Land Nembutsu, Soto Shikantaza, Rinzai Hakuin curriculum, Korean Seon Hwadu, Tibetan Vajrayana Chöd + Phowa + Trekchö + Tögal, Shingon Three Mysteries, Theravada Abhidhamma + Visuddhimagga + Pa Auk, Vietnamese Bell Practice, Naikan); Islamic legal-philosophical methods (Qiyas, Ijtihad, Istihsan, Maslaha, Maqasid, Avicenna); African philosophy (Oruka Sage, Sankofa, Ubuntu); Confucian self-cultivation (Mengzi Four Sprouts, Xunzi Ritual, Toegye Ten Diagrams); Daoist (Wu Wei decision practice, Ba Duan Jin); Kalam Atomism + Hermetic As-Above-So-Below; medical specialty pockets (SPIKES, REMAP, NURSE, Dignity Therapy, WHO Surgical Checklist, ABCDEF Bundle, M&M, MSE, Biopsychosocial, 4P, HEEADSSS, CGA, Beers, Bradford Hill, Screening Test); legal specialty (Voir Dire, Younger's Commandments, Daubert, Deposition Sequencing, Scrutiny Tiers, Settlement Trees, Mediation Styles); engineering specialty (Chaos Engineering, STRIDE, PASTA, Blameless Postmortem, ADRs, C4 Notation, FMEA, HAZOP); craft/trade (Mise en Place, Mother Sauces, Taste-as-Data, Grain Reading, Weather Reading, Phenological Reading, Hive Reading); performing arts (Stanislavski, Meisner Repetition, LMA, Viewpoints, Murch's Rule of Six, Jazz Chord-Substitution, Raga Grammar, Schenkerian Analysis). Pairwise occupancy improved 55.9% → **60.6%** (+4.7 pp; 335 facet-pair cells closed). Cumulative across Sprints 01+03: 48.6% → 60.6% (+12.0 pp; 852 cells closed; corpus 294 → 483). Schema unchanged through both sprints: zero new facet values, zero new Fields, zero new Operations. Sprint outputs: `pairwise-matrix.md` (regenerated), `pairwise-outliers.md` (cumulative S01+S03 narrative), `sprint03-audit-summary.md`. Library now substantially saturated; remaining 2,816 empty cells are predominantly Category A incoherent or Category B searched-and-unfound.
- **v1.2 (2026-05-12):** Pairwise-Gap Audit complete (Sprint 01 — Thinking Tools Pairwise-Gap Audit). Corpus grew 294 → 374 (+80 new entries across Medical/Clinical, Legal/Juridical, Jewish/Talmudic, Industrial/Lean, Crowd/Market, Military/Strategic, Therapeutic, Embodied/Somatic, Christian-contemplative, Generative/Improvisational, Futures methods, Aesthetic non-Western, Indigenous, Buddhist variants, Sufi/Islamic, Confucian, Hindu/Vedantic, Daoist, and African traditions). Pairwise occupancy improved from 48.6% → 55.9% (+7.3 pp; 517 facet-pair cells closed). Schema unchanged: zero new facet values, zero new Fields, zero new Operations — 100% of new entries used canonical v1.13.0 enums. Sprint outputs: `pairwise-matrix.md`, `coherent-gaps.md`, `search-batches.md`, `pairwise-outliers.md`. Sprint executed sequentially across 10 cards. Heavy under-representation of non-Western Lineages (Western-academic was 65% of corpus pre-sprint) addressed via Card 07's dedicated non-Western traditions batch — though further opportunities remain (documented in `pairwise-outliers.md`).
- **v1.1 (2026-05-11):** Zero-Gap Sweep complete (Sprint 01 — Thinking Tools Zero-Gap Sweep). 54 originally-empty slots (1 Domain + 33 Fields + 14 Operations + 2 Lineages + 1 State + 3 Agents) all populated by ≥1 entry. Corpus grew 259 → 294 (+35 new entries; +1 re-classification — Awe Walks moved from Contemplative/Awe-numinous to Emotional cognition/Gratitude-awe-reverence cultivation). Card 03 facet cleanup remapped 9 entries' tt_Operation values to v1.13.0 canonical Operations per the §2BB Phase 3 remap note (Apophatic Reasoning + Negative Capability + Strategic Silence → #20; Collective Idea Explorer + Sleep-On-It + Wallas → #23; Impact-Focused Problem Approach → #26; AAR → #28; Counterfactual Reasoning → #30; NVC → #32; Eulogy Exercise + Ikigai Diagram → #33; 7 Proof/Logic tools → #34; Casuistry → #35) and backfilled tt_Lineage / tt_Agent / tt_State for ~20 entries. Audit verdict: Empty: 0 across all 12 layers (Domain, Field, Operation, Type, Form, Scale, Duration, Lineage, Posture, State, Agent, About). Zero outliers — see `zero-gap-outliers.md` for the audit record. Gap-coverage matrix saved at `zero-gap-matrix.md`. Sprint executed sequentially across 11 cards (no Agent Teams) per user request.
- **v1.0.1 (2026-05-10):** Terminology clarification — Operation reframed from "hierarchy Level 3" to "mandatory single-valued facet." From v0.3 onward the Index called Domain → Field → Operation → Tool a "4-level hierarchy," but structurally that framing fails the parent-child test for Field → Operation (the same Operation appears across many Fields — that cross-cutting is what makes the Operation layer valuable for query). Corrected framing: **2-level hierarchy (Domain → Field) + 10 facets**, where Operation is the mandatory single-valued facet (along with Type). No schema change — `tt_Operation` was always a flat property at the same YAML depth as the other facets; only the doc language was sloppy. Updated §1A vocabulary table, §1B organizing-logic diagram, §2BB header, plus Saturation Sweep clarification note + Decisions To-Do D32. See D32 for full rationale.
- **v1.0 (2026-05-10):** Saturated. Schema v1.13.0 migration complete (see `Saturation Sweep.md` + `migration-crosswalk.md`). Path B selected at the Domain layer (single-axis register only): 16 mixed-axis Domains → 12 register-clean Domains (Discursive-analytical, Modes of inquiry, Non-discursive cognition, Embodied / somatic, Inner / psychological work, Symbolic systems, Contemplative, Generative / improvisational, Speculative / imaginative, Emotional cognition, Aesthetic *(NEW)*, Phronetic / practical wisdom *(NEW)*). Five v1.12.0 Domains dissolved (Disciplinary traditions, Collective / networked, Substrate processes, Moral / value, Spatial / temporal / ecological, Cross-substrate, Liminal / threshold, Negative cognition / clearing) — their Fields redistributed by register character. Fields expanded ~93 → 112; Operations expanded 18 → 36 (17 retained + 1 compound split + 18 new register-appropriate moves). Three new cross-cutting facets added: `tt_State` (7 values), `tt_Agent` (6 values), `tt_About` (14 values, open-extensible). `tt_Lineage` expanded 13 → 15 (added Legal / juridical, Medical / clinical). All 250 entries re-anchored to canonical Field, Domain derived from Field; per-tool Op #15 split decisions encoded in `migration-crosswalk.md` §3a; 8 edge-case overrides in `/tmp/edge-case-decisions.md`. Full prototype-compliance audit passes on first run (zero out-of-vocabulary values, zero (Field, Domain) mismatches, zero Cross_Domain self-references, all stances have empty Form, all entries declare v1.13.0 history entry). 76 of 112 canonical Fields populated; 36 stubs await Phase 3 expansion. Three flagged stubs populated in this sprint by Cards 11/12/13: Wabi-sabi / imperfection aesthetics, Awe / numinous cognition, Strategic patience & timing-judgment.
- **v0.9 (2026-05-08):** Post-sprint cleanup — Sprint 01's runner introduced 207 unauthorized values across 5 controlled-vocabulary properties (`tt_Form`, `tt_Scale`, `tt_Duration`, `tt_Lineage`, `tt_Posture`), violating the prototype's `options_ref` contracts. The schema's CASE SENSITIVITY RULES and the Decision Log's value-level definitions explicitly forbid silent additions ("New Form additions need explicit decision-log entries"). Audit found and corrected: `tt_Form: Template / canvas` → `Canvas` (12), `Workshop protocol` → `Sequenced workflow` (5); `tt_Scale: Workshop` → `Small group` (30, category confusion — Workshop is a Duration); `tt_Duration: Ongoing practice` → `Practice` (29), `Multi-day` → `Workshop` (13); `tt_Lineage: Strategic management` → `Industrial / business` (33), plus several mode-mappings to Eastern philosophical / Religious / monastic; `tt_Posture: Practitioner-accessible` → `Beginner-friendly` (64). Total: 70 files updated, 208 individual fixes. Also corrected 5 stance-type miscodings (Beginner's Mind, Negative Capability, Strategic Silence, Apophatic Reasoning, Unlearning) — set `tt_Type: stance` and blanked `tt_Form: []` per Decision Log spec. Renamed 5 files to restore stripped apostrophes (Beginner's Mind, Galton's Ox, Gendlin's Focusing, Ostrom's Design Principles, Worden's Tasks of Mourning); Worklist filename pointers updated. Library now passes full prototype-compliance audit: zero out-of-vocabulary values, zero stance-type miscodings, zero Roman numerals, all 250 entries declare `type: Thinking_Tool`.
- **v0.8 (2026-05-08):** Phase 3 build-out complete — 220 new entries classified across all 11 working Domains (Foundational cognitive operations, Modes of inquiry, Non-discursive cognition, Inner / psychological work, Symbolic systems, Collective / networked cognition, Substrate processes, Moral / value cognition, Disciplinary traditions, Negative cognition / clearing, Play/humor/improvisation). Library now contains **250 total classified entries** spanning 11 active Domains and ~50 Fields. All entries use the canonical 18 `tt_Operation` values from v0.7's section 2BB inventory. Sprint 01 (Thinking Tools Phase 3 Build-Out) complete.
- **v0.7 (2026-05-07):** Schema v1.12.0 — fixed semantic drift in `tt_Operation`. Values had been written as tool-specific one-line summaries (one Operation per Tool, zero discriminatory value). The Operation layer's purpose is cross-cutting query — "show me every 'Score and rank options' tool across all Domains and Fields" — which collapses if Operations are unique per tool. Defined a starter inventory of 18 shared Operations and rewrote all 30 entries to use them. Average density: 1.67 Tools per Operation. New section 2BB documents the inventory. Reverses earlier D9 ("Operations stay emergent") — Operations now have a canonical, curated inventory.
- **v0.6 (2026-05-07):** Schema v1.11.0 — dropped Roman numeral codes (I–XVI) from `tt_Domain` in favor of descriptive names stored directly. Removed redundant `tt_Domain_Name` property; `tt_Cross_Domains` lists now also use descriptive names. Section 2A retitled (no "Code" column); section 2B subsection headers stripped of "Under [Roman] —" prefix; cross-cutting Field annotations stripped of Roman-numeral spans. All 30 entries migrated. Reasoning: the indirection added friction and string-sort weirdness without value; the rest of the canonical schema stores human-readable values directly.
- **v0.5 (2026-05-07):** Adopted canonical `Master_Schema.yaml` v1.10.0 — added the `tt_` namespace and `Thinking_Tool` prototype. All 30 existing entries (26 SOLVE eX seed + 4 Phase 3 Power-Politics tools) migrated: bare property names (`domain`, `field`, etc.) rewritten to `tt_*` form per CASE SENSITIVITY RULES; `Item_ID`, `type`, `Date_Added`, `Date_Modified`, `Tags`, `See_Also` added per UNIVERSAL DECLARATION RULE. Bases file updated to query `note.tt_*`. Schema authority moved out-of-project to the canonical infrastructure folder.
- **v0.4 (2026-05-07):** Source `.txt` files merged into entry `.md` files; `Tool Entries/` flattened to 26 single-file entries (no number prefix, no "Thinking Tool" prefix). Tooling switch from Dataview to **Obsidian Bases** finalized (sections 3, 4 swept). Master `Thinking Tools.base` file created with 6 starter views (By Domain, By Field, By Posture, Scale × Duration, By Lineage, Cards). D3/D6/D7 reclassifications applied during consolidation: "Group facilitation" Field split into 5 granular Fields; #11 → Collective decision-making; #17 → Group ideation; #26 Domain VI → IX (Field "Systems mapping" relocates). Two Field renames per D4 (Strategic foresight, Devil's advocacy).
- **v0.3 (2026-05-07):** Reinstated level 2 (renamed "Area" → **Field**). Renamed level 3 ("Job" → **Operation**). All 26 tool entries updated with both fields. Field inventory in section 2B retitled. Added 6 new Fields surfaced by the SOLVE eX classification (Futures thinking / forecasting, Question generation, Feedback systems design, Systems mapping, plus Multi-perspective analysis and Trade-off / multi-criteria decision promoted from cross-cutting).
- **v0.2 (2026-05-07):** Resolved terminology (super-cluster → **Domain**). Added **Type** field (instrument vs. stance). Committed to **Obsidian + Bases**. Phase 0 complete; Phase 1 done — 26 SOLVE eX tools classified.
- **v0.1 (2026-05-07):** Initial structure — taxonomy overview, faceted system, phased build-out plan.

---

## 1. Taxonomy Overview

### 1A. Vocabulary (locked v1.0 — schema v1.13.0; framing clarified 2026-05-10)

**2-level hierarchy (Domain → Field) + 10 facets.** The hierarchy gives parent-child containment (every Field anchors to exactly one Domain, per Saturation Sweep D2). The 10 facets are independent dimensions that each describe a Tool from a different angle. **Operation is structurally a facet** (it cross-cuts Fields — the same Operation appears in many Fields), but it is the *mandatory, single-valued* facet, which gives it a special role and is why earlier drafts (v0.3–v1.0) called it "Level 3."

|              Position              |           Term          |                              Example                               |                                                                                                                       Notes                                                                                                                        |
|------------------------------------|-------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hierarchy L1 (broadest)            | **Domain**              | "Discursive-analytical"                                            | 12 values. Answers *"What cognitive register does this tool operate in?"* (single-axis since v1.13).                                                                                                                                               |
| Hierarchy L2                       | **Field**               | "Decision analysis"                                                | Subdivision of a Domain. 112 Fields locked; each anchors to exactly one Domain (D2 — single-anchor rule). Cross-Domain spanning at tool level only.                                                                                                |
| Leaf                               | **Tool**                | "AHP (Analytic Hierarchy Process)"                                 | The specific instrument or stance. Described by `(Domain, Field)` + a vector of facet values.                                                                                                                                                      |
| Facet — *mandatory, single-valued* | **Operation**           | "Score and rank options"                                           | The cognitive *move* a tool performs (verb-phrase). 36 canonical Operations. **Cross-cuts Fields** — multiple Tools share an Operation, and the same Operation appears in many Fields. That cross-cutting is what gives the layer its query value. |
| Facet — *mandatory, single-valued* | **Type**                | "instrument" / "stance"                                            | Whether the entry is a fillable instrument or a mode you enter. 2 values.                                                                                                                                                                          |
| Facet — multi-value                | **Form**                | "Matrix" / "Dialogue protocol"                                     | Shape of the tool (only meaningful for instruments). 16 values.                                                                                                                                                                                    |
| Facet — multi-value                | **Scale**               | "Solo" / "Small group" / "Organizational"                          | Group size at which it operates. 7-step ladder.                                                                                                                                                                                                    |
| Facet — multi-value                | **Duration**            | "Snap" / "Workshop" / "Practice"                                   | Time signature. 5 values.                                                                                                                                                                                                                          |
| Facet — multi-value                | **Lineage**             | "Western analytic" / "Eastern philosophical"                       | Source tradition. 15 values (added Legal / juridical, Medical / clinical in v1.13).                                                                                                                                                                |
| Facet — multi-value                | **Posture**             | "Solo-quiet" / "Adversarial-tolerant"                              | Disposition the practitioner must bring. 9 values.                                                                                                                                                                                                 |
| Facet — multi-value                | **State** *(NEW v1.13)* | "Liminal" / "Flow" / "Numinous"                                    | Psychological / phenomenological state the tool asks the practitioner to enter or sustain. 7 values. *Distinct from Posture: Posture is what you bring; State is what you become.*                                                                 |
| Facet — multi-value                | **Agent** *(NEW v1.13)* | "Solo human" / "Human-AI partnership" / "Cross-cultural"           | Type of cognitive agent doing the work. 6 values. *Distinct from Scale: Scale is how many; Agent is what kind.*                                                                                                                                    |
| Facet — multi-value                | **About** *(NEW v1.13)* | "Decision / choice" / "Power / politics" / "Sacred / transcendent" | Subject matter the tool operates on. 14 values, open-extensible at ≥10-tool-applicability threshold. Required to be ≥1 value on every entry.                                                                                                       |

> **Why hierarchy + facets, not 4-level hierarchy:** the parent-child test (does a value have exactly one parent at the layer above?) passes for Domain → Field (yes — single-anchor rule) and fails for Field → Operation (no — Operations cross-cut Fields, which is the whole point of the Operation layer). Calling Operation "Level 3" was a legacy framing from v0.3 that's structurally inaccurate. The schema's YAML has always treated `tt_Operation` as a flat property alongside the other facets; only the documentation language was sloppy. Clarified 2026-05-10. See `Saturation Sweep.md` Operation-as-facet note + Decisions To-Do D32.

> **Why this set of names:** Domain → Field maps onto standard academic taxonomy (Discipline → Field) while keeping single-axis register precision. "Field" reads as "subject area" / "research area" / "field of study" — universal scholarly vocabulary. "Operation" is teleological (verb), where Field is categorical (noun); together with the other facets they give each Tool a richly described position in the conceptual space.

### 1B. Organizing logic — Hierarchy + facets (committed in v0.2; refined in v1.13; framing clarified 2026-05-10)

```
Domain (12, register only)
 └── Field (112, single-anchor to Domain)
      └── Tool ────► Facets (all describe the Tool, none are sub-levels of Field):
                     ├── Operation (36, mandatory single-valued)
                     ├── Type (2, mandatory single-valued)
                     ├── Form (16, multi-value)
                     ├── Scale (7, multi-value)
                     ├── Duration (5, multi-value)
                     ├── Lineage (15, multi-value)
                     ├── Posture (9, multi-value)
                     ├── State (7, multi-value — NEW v1.13)
                     ├── Agent (6, multi-value — NEW v1.13)
                     ├── About (14, multi-value, open-extensible — NEW v1.13)
                     └── Combinations: { Cross-Domains, Often-Precedes, Often-Follows, Pairs-Well-With, Replaced-By }
```

- The **2-level hierarchy** (Domain → Field) gives the obvious browse path.
- The **10 facets** give cross-cutting query power (via Bases). Operation is *mandatory single-valued* like Type; the other 8 are multi-value (Form/Scale/Duration/Lineage/Posture/State/Agent/About).
- "Cross-Domains" lets a tool link to additional Domains beyond its canonical placement (the v0.x "cross-cutting Fields" subsection is eliminated — all spanning happens at tool level via Cross-Domains).
- Per Saturation Sweep D2: each Field anchors to exactly one Domain. There is no parent-child relationship between Field and any facet (including Operation) — facets are independent axes that intersect at the Tool.

---

## 2. Faceted Classification System — Canonical Vocabularies

### 2A. Primary — **Domain** (level 1)

The 12 Domains. Each answers exactly one question: *"What cognitive register does this tool operate in?"* — where a register is a mode in which mind operates, characterized by the attention it requires, the operations available within it, and the kind of knowing it produces. Saturated and locked 2026-05-09 (see `Saturation Sweep.md` §Domain layer + Decision Log D18–D20). Entries store the descriptive name in `tt_Domain` directly.

|            Domain            |                                            Register character                                            |                                 Representative Fields                                  |                         Example tools                         |
|------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Discursive-analytical        | Step-by-step verbal/logical reasoning; attention narrow and sequential; produces propositional knowledge | Decision analysis, Causal & diagnostic reasoning, Strategic & game-theoretic reasoning | AHP, Pre-Mortem, Bayesian Updating, Wardley Mapping           |
| Modes of inquiry             | Disciplined investigation; attention selective and questioning; produces evidence-grounded understanding | Empirical / scientific method, Calibration & epistemic humility, Dialogue practice     | Tetlock Superforecasting, Mill's Methods, NVC                 |
| Non-discursive cognition     | Knowing-without-words; attention diffuse and feature-detecting; produces tacit / felt knowledge          | Intuitive judgment, Metaphoric reasoning, Pattern recognition                          | Heads-or-Tails Gut-Check, TRIZ, Biomimicry                    |
| Embodied / somatic           | Body-located knowing; attention sensed in tissue and physiology; produces somatic insight and regulation | Felt-sense / focusing, Kinesthetic / somatic knowing, State management                 | Gendlin's Focusing, Feldenkrais, Breath Regulation            |
| Inner / psychological work   | Self-as-object inquiry; attention turned inward; produces self-knowledge, healing, integration           | Psychotherapeutic restructuring, Identity work, Values clarification                   | CBT, IFS, Designing Your Life, Ikigai                         |
| Symbolic systems             | Signs and structures used to think; attention manipulates representations; produces communicable meaning | Logical / formal reasoning, Memory architecture, Narrative architecture                | Propositional Logic, Method of Loci, Hero's Journey           |
| Contemplative                | Quieted, receptive attention; not-grasping; produces apophatic, mystical, or unitive knowing             | Concentration & insight practice, Apophatic / clearing practice, Theological reasoning | Vipassana, Centering Prayer, Negative Capability              |
| Generative / improvisational | Real-time creative production; attention loose and playful; produces novel combinations and divergence   | Divergent thinking / brainstorming, Improvisation, SCAMPER & recombination             | Sleep-On-It, Oblique Strategies, Wallas Four Stages           |
| Speculative / imaginative    | World-projection; attention holds suspended-disbelief and counterfactuals; produces alternative-futures  | Strategic foresight, Counterfactual reasoning, Backcasting & mental simulation         | Horizon Explorer, Counterfactual Reasoning, Moral Imagination |
| Emotional cognition          | Affect-as-information; attention to felt response; produces emotional discernment and regulation         | Affect labeling, NVC family, RAIN technique                                            | *(corpus not yet populated — Phase 3 expansion)*              |
| Aesthetic                    | Quality-of-form perception; attention to elegance, fit, beauty; produces craft judgment and design taste | Connoisseurship, Pattern-language aesthetics, Musical reasoning                        | Alexander Pattern Languages, Wayfinding, Motivic Development  |
| Phronetic / practical wisdom | Judgment-in-context; attention to particular case and timing; produces situated, ethical action          | Habit & behavior design, Casuistry, Cynefin & sense-making, Negotiation                | BATNA-ZOPA, Atomic Habits, After Action Review, Cynefin       |

**What the new structure resolves:** v1.12.0 mixed axes (register / tradition / state / agent / output). v1.13.0 commits to *register only* at the Domain layer; tradition moves to `tt_Lineage`, state to new `tt_State`, agent to new `tt_Agent`, output stays at `tt_Operation`. See `Saturation Sweep.md` §Step 0 + Decision Log D18 for the Path B selection rationale.

**Saturation:** All 12 Domains passed mutual-exclusivity, joint-exhaustiveness, and population-stress tests; the saturated structure also passed an external-corpus test against 7 published lists (Tetlock, Kahneman, Cynefin, Polanyi, Bloom, Buddhist contemplative tradition, Indigenous practices) with 52/52 placement and zero torture-fits.

### 2B. Primary — **Field** (level 2)

Canonical list of 112 Fields, organized under their 12 canonical Domains. Each Field anchors to exactly one Domain (per Saturation Sweep D2 — single-anchor rule). Cross-Domain spanning is handled at the tool level via `tt_Cross_Domains`. The cross-cutting Fields subsection from v0.x is eliminated; what were "cross-cutting" Fields have been absorbed into their best-fit canonical Domain. Saturated 2026-05-09; per-Domain Field counts within the 3–15 sanity range.

> **Population state (2026-05-10):** Of 112 canonical Fields, 76 are populated by ≥1 entry; 36 are stubs awaiting Phase 3 expansion. Three stubs are flagged in the Sweep as priority for this sprint — Wabi-sabi / imperfection aesthetics, Awe / numinous cognition, Strategic patience & timing-judgment — each being populated to ≥3 tools by Cards 11/12/13. Counts in parens below show current tool population.

#### Discursive-analytical (13 Fields)
- **Causal & diagnostic reasoning** *(merges OLD Causal + Diagnostic/abductive)* — 4 tools: Causal Chain Breaker, Abductive Inference, Causal DAGs, Instrumental Variables
- **Combinatorial / enumerative reasoning** — 2 tools: Combinatorial Enumeration, Layered Actions Breakdown
- **Quantitative & probabilistic reasoning** — 5 tools: Fermi Estimation, Bayesian Updating, Base Rate Reasoning, Expected Value Decision Trees, Sensitivity Analysis
- **Argument structuring** *(merges OLD Argument mapping + MECE / issue trees)* — 6 tools: IBIS, Minto Pyramid Principle, Issue Tree / Hypothesis Pyramid, Toulmin Model, So-What Laddering, Dialectical Maps
- **Decision analysis** *(merges OLD Decision-quality + Trade-off / multi-criteria + Collective decision-making)* — 13 tools: AHP, Ease-Impact Assessment Matrix, Weighted Decision Matrix, Eisenhower Matrix, Kepner-Tregoe, Thinking in Bets, One-Way / Two-Way Doors, Antifragility, Real Options Analysis, Taleb's Barbell, Tail-Risk Hedging, Poker Decision Review, Effort Justification Meter
- **Strategic & game-theoretic reasoning** *(merges OLD Strategic positioning + Game theory + Coordination + Mechanism + Principal-agent + Military strategic)* — 19 tools: Wardley Maps, Porter's Five Forces, SWOT Analysis, Blue Ocean / Strategy Canvas, Jobs-to-Be-Done, Nash Equilibrium, Game Theory Primer, Schelling-Point Reasoning, OODA Loop, Clausewitz Center of Gravity, Sun Tzu Asymmetric Logic, Ostrom's Design Principles, Tragedy of the Commons, Prediction Markets, Auction Design, Agency Theory Analysis, Moral Hazard Analysis, Galton's Ox, Gamification Frameworks
- **Systems / cybernetic thinking** *(merges OLD Systems mapping + Feedback systems + Dynamic systems + Network/graph + Constraint/bottleneck)* — 9 tools: Causal Loop Diagrams, Stock-and-Flow Models, Theory of Constraints, Critical Chain / Critical Path, Feedback Delay Analysis, Holistic Systems Mapper, Dynamic Feedback Mapper, Network Centrality Analysis, Clustering / Percolation Analysis
- **Adversarial / debiasing reasoning** *(merges OLD Devil's advocacy + Debiasing & adversarial stress-testing)* — 5 tools: Pre-Mortem, Inversion, Red Teaming, Constructive Contrarian Guide, Cognitive Bias Checklists
- **Power, politics & influence mapping** — 4 tools: Stakeholder Power-Interest Grid, Force Field Analysis, Coalition Mapping, Influence Sociogram
- **Engineering / design reasoning** — 6 tools: Blueprint Optimization Framework, FOCUS Ideation, Constraint Satisfaction, Design of Experiments, Factor of Safety, Priority-Based Requirements Matrix
- **Legal / juridical reasoning** *(merges OLD Legal + Civic/political/constitutional)* — 5 tools: Legal Precedent Reasoning, Statutory Interpretation, Constitutional Interpretation, Burden of Proof Analysis, Democratic Deliberation
- **Financial / accounting reasoning** — 3 tools: Capital Allocation, Cash vs Accrual Reasoning, Balance-Sheet Thinking
- **Ethical reasoning** *(formal moral philosophy; case-based casuistry lives in Phronetic)* — 6 tools: Deontology, Consequentialism, Virtue Ethics, Contractualism, Veil of Ignorance, Stakeholder Ethics Matrix

#### Modes of inquiry (13 Fields)
- **Empirical / scientific method** *(includes Falsification design + Operationalization)* — 8 tools: Scientific Method (RCTs / A-B Testing), Popper Falsifiability, Mill's Methods, Experimental Innovation Cycle, Pre-Registered Predictions, Construct Validity Frameworks, KPI Design, Goodhart-Aware Metric Selection
- **Question generation** — 1 tool: Critical Question Mapping
- **Historical inquiry** — 2 tools: Historical Periodization, Path Dependence Analysis
- **Forensic / investigative inquiry** — 1 tool: Forensic Chain of Custody
- **Hermeneutic / interpretive inquiry** — 1 tool: Hermeneutic Interpretation
- **Ethnographic inquiry** *(includes cognitive ethology via tt_Agent: cross-species)* — 1 tool: Ethnographic Thick Description
- **Phenomenological inquiry** — 1 tool: Phenomenological Analysis
- **Calibration & epistemic humility** *(includes Source / evidence triangulation; absorbs Trust calibration)* — 5 tools: Tetlock Superforecasting, Brier Scoring, Calibration Training Drills, Unlearning / Bayesian Dis-updating, Trust Equation (Maister)
- **Cross-cultural inquiry** *(absorbs Cross-cultural translation + Cultural evolution/memetic)* — 3 tools: Erin Meyer Culture Map, Hofstede Dimensions, Memetics
- **Problem framing** — 1 tool: Impact-Focused Problem Approach
- **Multi-perspective analysis** — 2 tools: Holistic Perspective Harmonizer, Holistic Perspective Toolkit
- **Dialogue practice** *(absorbs NVC family + Bohm dialogue)* — 4 tools: Collaborative Conversation Navigator, Difficult Conversations, Nonviolent Communication / NVC, Vulnerability Laddering
- **Ecological / place-based inquiry** *(absorbs OLD Place-based + Bioregional)* — *(stub; awaiting Phase 3)*

#### Non-discursive cognition (5 Fields)
- **Tacit knowing & explicit-tacit conversion** *(Polanyi, Nonaka SECI)* — *(stub; Phase 3)*
- **Intuitive judgment / felt-sense pattern recognition** — 1 tool: Heads-or-Tails Gut-Check
- **Implicit learning / master-apprentice transmission** — *(stub; Phase 3)*
- **Metaphoric / analogical / sympathetic reasoning** *(Lakoff + sympathetic-magic absorbed)* — 4 tools: TRIZ, SCAMPER, Biomimicry / Cross-Domain Transfer, Role-Based Analogy
- **Pattern recognition & anomaly detection** *(intuitive variety; formal-method tools cross-mark to Discursive-analytical)* — 2 tools: Pattern Recognition, Anomaly Detection

#### Embodied / somatic (6 Fields)
- **Felt-sense / focusing** *(Gendlin)* — 1 tool: Gendlin's Focusing
- **Kinesthetic / somatic knowing** — 1 tool: Feldenkrais Method
- **Polyvagal / nervous-system practices** — *(stub; Phase 3 — overlaps with Trauma-informed cognition)*
- **Authentic Movement / movement-as-inquiry** — *(stub; Phase 3)*
- **State / physiological-cognitive management** — 3 tools: Breath Regulation, HRV-Based State Management, Glucose-Aware Cognition
- **Sleep & cognition optimization** — *(stub; Phase 3 — Sleep-On-It Protocols lives in Generative)*

#### Inner / psychological work (10 Fields)
- **Psychotherapeutic restructuring** *(CBT, IFS, schema)* — 4 tools: Cognitive Behavioral Therapy (CBT), Internal Family Systems (IFS), Schema Therapy, Psychodynamic Analysis
- **Trauma-informed cognition** — 2 tools: Polyvagal Theory, Somatic Experiencing
- **Existential / meaning-making** — 2 tools: Frankl's Logotherapy, Yalom's Existential Therapy
- **Grief & loss processing** — 2 tools: Worden's Tasks of Mourning, Continuing-Bonds Model
- **Identity / self-narrative work** — 1 tool: Narrative Therapy
- **Defense-mechanism / shadow recognition** — 2 tools: Shadow Work, Hillman's Archetypal Psychology
- **Self-knowledge / temperament mapping** — 3 tools: Big Five Inventory, CliftonStrengths, Trigger Inventories
- **Oneiric / dream-work** *(moved from Non-discursive in v1.13)* — 3 tools: Jungian Dream-Work, Lucid Dreaming, Hypnagogia Practice
- **Values clarification & life design** *(moved from Moral/value)* — 5 tools: Designing Your Life, Ikigai Diagram, Eulogy Exercise, Prioritized Purpose Planner, Collective Objective Builder
- **Failure / repair / forgiveness work** — *(stub; Phase 3)*

#### Symbolic systems (13 Fields)
- **Discourse / frame analysis** — 3 tools: Frame Analysis, Context Clarity Navigator, Perspective Pivot Workshop
- **Linguistic / language-shapes-thought analysis** — 2 tools: Sapir-Whorf Hypothesis, Lakoff's Conceptual Metaphor
- **Semiotic / sign-system analysis** — 2 tools: Saussurean Semiotics, Peircean Semiotics
- **Rhetorical analysis & construction** — 1 tool: Aristotelian Rhetoric
- **Translation / code-switching** — 1 tool: Code-Switching
- **Audience analysis** — 2 tools: Geoffrey Moore Chasm Segmentation, Persona-Shifting
- **Narrative architecture** *(absorbs the "Narrative cognition" gap)* — 4 tools: Hero's Journey, SCQA, StoryBrand, Problem-Solution-Result
- **Visual / spatial communication** — 3 tools: Sketchnoting, Back of the Napkin, Tufte Data-Display Principles
- **Logical / formal reasoning** *(moved from Foundational → Symbolic systems in v1.13)* — 3 tools: Propositional Logic, Predicate Logic, Modal Logic
- **Mathematical / proof reasoning** — 4 tools: Proof by Induction, Proof by Contradiction, Direct Proof, Proof by Construction
- **Programming / algorithmic thinking** — 4 tools: Abstraction, Recursion, Type-Thinking, Complexity Analysis
- **Divinatory / oracular systems** *(Tarot, I Ching, runes)* — *(stub; Phase 3)*
- **Memory & knowledge architecture** *(merges Mnemonic + External brain / Zettelkasten)* — 6 tools: Zettelkasten, Building A Second Brain, PARA, Method of Loci, Spaced Repetition, Chunking

#### Contemplative (11 Fields)
- **Apophatic / clearing practice** *(merges Apophatic + Negative capability + Unlearning + Silence)* — 3 tools: Apophatic Reasoning, Negative Capability, Strategic Silence / Pause
- **Concentration & insight practice** *(Vipassana + Shamatha + Centering prayer)* — 3 tools: Buddhist Meditation, Christian Contemplation, Secular Meditation
- **Koan / paradox practice** — *(stub; Phase 3)*
- **Beginner's mind & wonder** *(merges Beginner's mind/shoshin + Curiosity)* — 1 tool: Beginner's Mind
- **Discernment practice** *(Ignatian)* — *(stub; Phase 3)*
- **Awe / numinous cognition** — *(stub; awaiting Card 12)*
- **Ritual cognition** — *(stub; Phase 3)*
- **Initiation / rite-of-passage** — *(stub; Phase 3)*
- **Hope / faith / surrender practices** — *(stub; Phase 3)*
- **Theological / sacred reasoning** *(moved from Moral/value)* — 2 tools: Apophatic Theology, Cataphatic Theology
- **Attention / focus management** *(moved from Substrate processes)* — 3 tools: Deep Work, Flow Engineering, Attention Restoration

#### Generative / improvisational (7 Fields)
- **Play / ludic exploration** — *(stub; Phase 3)*
- **Humor / wit construction** — *(stub; Phase 3)*
- **Improvisation / "yes-and"** — *(stub; Phase 3)*
- **Divergent thinking / brainstorming** *(merges Brainstorming + Idea generation + Group ideation)* — 3 tools: Collective Idea Explorer, Sleep-On-It Protocols, Wallas's Four Stages of Creativity
- **Lateral thinking** *(de Bono)* — *(stub; Phase 3)*
- **Analogical reasoning for ideation** *(Gentner, Holyoak)* — *(stub; Phase 3)*
- **SCAMPER & creative-recombination methods** — 3 tools: Design-Constraint Method, Haiku-Style Constraint Exercises, Oblique Strategies (Eno)

#### Speculative / imaginative (8 Fields)
- **World-building** *(sci-fi, design fiction)* — *(stub; Phase 3)*
- **Thought-experiment construction** — *(stub; Phase 3)*
- **Counterfactual reasoning** *(moved from Foundational → Speculative in v1.13)* — 1 tool: Counterfactual Reasoning
- **Strategic foresight** *(merges Scenarios + Delphi + Three Horizons + Futures wheels)* — 2 tools: Horizon Explorer, Delphi Forecasts and Predictions
- **Pre-mortem & failure imagination** — *(see Pre-Mortem in Adversarial / debiasing; this Field reserves Pre-mortem-as-foresight-tool; Phase 3)*
- **Backcasting & mental simulation** *(merges Backcasting + Mental simulation)* — 4 tools: Natural Step Backcasting, Reverse-Engineered Milestones, Imagine A Day In This Future, Recognition-Primed Decision (Klein RPD)
- **Moral imagination** *(moved from Moral/value)* — 1 tool: Moral Imagination
- **Ancestral / multigenerational thinking** *(Long Now, 7-gen)* — *(stub; Phase 3)*

#### Emotional cognition (7 Fields)
- **Appraisal-theoretic emotional cognition** — *(stub; Phase 3)*
- **Affect labeling & granularity** — *(stub; Phase 3)*
- **Gratitude / awe / reverence cultivation** — *(stub; Phase 3)*
- **Disgust / aversion / threat-detection** — *(stub; Phase 3)*
- **Compassion / loving-kindness practice** — *(stub; Phase 3)*
- **Nonviolent Communication (NVC) family** — *(NVC the tool currently lives in Modes of inquiry/Dialogue practice — see edge-case decisions; this Field reserves for affect-side NVC variants; Phase 3)*
- **RAIN technique & affect-regulation practices** — *(stub; Phase 3)*

#### Aesthetic (7 Fields)
- **Connoisseurship & taste cultivation** — 1 tool: Connoisseurship Training
- **Design critique & design review** — *(stub; Phase 3)*
- **Formal aesthetics** *(Kant, Hume)* — *(stub; Phase 3)*
- **Pattern-language aesthetics** *(Christopher Alexander)* — 3 tools: Alexander Pattern Languages, Proxemics, Wayfinding
- **Wabi-sabi / imperfection aesthetics** — *(stub; awaiting Card 11)*
- **Musical / temporal-aesthetic reasoning** *(moved from Disciplinary traditions)* — 3 tools: Motivic Development, Musical Form, Tension/Release
- **Code review for elegance & quality** — *(stub; Phase 3)*

#### Phronetic / practical wisdom (12 Fields)
- **Reflective practice & experiential learning** *(Schön + AAR + Action learning)* — *(see After Action Review in Metacognition; this Field reserves for Schön-canonical reflective practice; Phase 3)*
- **Casuistry / case-based moral reasoning** — 1 tool: Casuistry
- **Cynefin & sense-making** — 1 tool: Cynefin
- **Conflict resolution** — 2 tools: Crucial Conversations, Conversation Convergence Process
- **Consensus building** — 1 tool: Critical Consensus Constructor
- **Negotiation** *(BATNA, interest-based)* — 3 tools: BATNA-ZOPA, Interest-Based Bargaining, Mutual Gains Framework
- **Clinical reasoning** *(moved from Disciplinary traditions; clinical judgment is phronetic in character)* — 3 tools: Differential Diagnosis, Evidence Pyramids, Clinical Heuristics
- **Metacognition & tool-selection** *(merges Tool selection + Tool composition + Metacognition/double-loop)* — 6 tools: After Action Review, Double-Loop Learning, Cynefin-Based Tool Selection, Decision-Context Matching, Tool Sequencing Playbooks, Retrospective Formats
- **User-centered design** — 4 tools: Customer Journey Maps, Empathy Maps, Personas, Service Blueprints
- **Habit & behavior design** *(moved from Substrate processes)* — 5 tools: Atomic Habits Framework, BJ Fogg Behavior Model, Implementation Intentions, Time-Blocking, Energy Mapping
- **Deliberate practice design** — 3 tools: Ericsson Deliberate Practice, Deconstruction-Drilling, Feynman Technique
- **Strategic patience & timing-judgment** *(newly added in v1.13)* — *(stub; awaiting Card 13)*

**Dissolved Domains** *(v1.12.0 → v1.13.0)*: Disciplinary traditions, Collective / networked cognition, Substrate processes, Moral / value cognition, Spatial / temporal / ecological, Cross-substrate cognition, Liminal / threshold cognition, Negative cognition / clearing. Each dissolved Domain's Fields were redistributed to one of the 12 canonical Domains based on register character. The v0.x "Cross-cutting Fields" subsection is eliminated; cross-Domain spanning at the tool level is handled by `tt_Cross_Domains`. Full crosswalk: `migration-crosswalk.md`.

**Renamed Domains in v1.13**: Foundational cognitive operations → Discursive-analytical (renamed for register clarity); Play, humor, improvisation → Generative / improvisational; Speculative / fictional cognition → Speculative / imaginative; Negative cognition / clearing absorbed into Contemplative.

**New Domains in v1.13**: Aesthetic *(NEW)* — anchors Connoisseurship, Pattern-language, Musical reasoning, Wabi-sabi, plus design-aesthetic Fields; Phronetic / practical wisdom *(NEW)* — anchors Casuistry, Cynefin, Negotiation, Habit design, Conflict resolution, Clinical reasoning, Metacognition, User-centered design, Deliberate practice, Strategic patience.

### 2BB. Primary — **Operation** *(mandatory single-valued facet; not a hierarchy level — see §1A clarification)*

The cognitive *move* a tool performs — its action-shape, abstracted to a verb-phrase. **Multiple Tools share an Operation**; that's what makes the layer useful for cross-cutting query ("show me every 'Score and rank options' tool across all Domains and Fields"). Saturated 2026-05-09 at 36 canonical Operations: 17 retained from v1.12.0, 1 compound (#15 "Stress-test and refine an idea") split into two, plus 18 new register-appropriate moves added to cover contemplative, embodied, emotional, and phronetic registers the v1.12.0 inventory under-covered. The Gate 3 external-corpus test (Buddhist contemplative tradition) surfaced the final gap — Operation #36 *Cultivate emotion* — for Metta/Tonglen-class practices.

Open-but-curated: extend by proposing new Operations, but bias toward reusing existing ones before adding new. **Current corpus uses 20 of 36 Operations**; the other 16 are reserved for Phase 3 expansion tools (mostly contemplative, embodied, and phronetic registers).

| #  |                              Operation                               |                                 What it does                                 |                                             Current corpus (tool count + samples)                                             |
|----|----------------------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|  1 | **Locate intervention leverage**                                     | Find the high-leverage point in a structure                                  | 6 tools — Causal Chain Breaker, OODA Loop, Clausewitz Center of Gravity                                                       |
|  2 | **Decompose hierarchically**                                         | Recursive breakdown into nested sub-parts                                    | 28 tools — Abstraction, Layered Actions Breakdown, Atomic Habits Framework, Burden of Proof Analysis                          |
|  3 | **Score and rank options**                                           | Apply numeric/categorical scores; prioritize                                 | 21 tools — AHP, Bayesian Updating, Stakeholder Power-Interest Grid, Weighted Decision Matrix                                  |
|  4 | **Reframe across lenses**                                            | View the same situation through multiple perspectives                        | 47 tools — Apophatic Reasoning, Aristotelian Rhetoric, Beginner's Mind, Frame Analysis, Perspective Pivot Workshop            |
|  5 | **Apply question bank**                                              | Work through a structured set of trigger questions                           | 20 tools — Critical Question Mapping, Cognitive Bias Checklists, Big Five Inventory, Alexander Pattern Languages              |
|  6 | **Run dialogue protocol**                                            | Execute a turn-based conversational structure                                | 5 tools — Collaborative Conversation Navigator, NVC, Conversation Convergence Process, Difficult Conversations                |
|  7 | **Build consensus**                                                  | Assemble agreement among willing parties                                     | 2 tools — Critical Consensus Constructor, Collective Objective Builder                                                        |
|  8 | **Aggregate parallel judgments**                                     | Anonymous/independent synthesis of separate views                            | 6 tools — Delphi, Collective Idea Explorer, Galton's Ox, Prediction Markets                                                   |
|  9 | **Probe via contrarian role**                                        | Formal devil's-advocacy / structured opposition                              | 2 tools — Constructive Contrarian Guide, Red Teaming                                                                          |
| 10 | **Account opposing forces**                                          | List and weight tensions/drivers/restraints                                  | 1 tool — Force Field Analysis                                                                                                 |
| 11 | **Map relational topology**                                          | Visualize relationships among elements as a graph                            | 23 tools — Causal Loop Diagrams, Causal DAGs, Holistic Systems Mapper, Sketchnoting                                           |
| 12 | **Run experimental cycle**                                           | Hypothesis → test → analyze → iterate                                      | 15 tools — Experimental Innovation Cycle, AAR, Building A Second Brain, Ericsson Deliberate Practice                          |
| 13 | **Project alternative futures**                                      | Envision multiple end-states                                                 | 5 tools — Horizon Explorer, Counterfactual Reasoning, Natural Step Backcasting, Imagine A Day In This Future                  |
| 14 | **Surface intuitive preference**                                     | Bypass deliberation to access gut response                                   | 17 tools — Heads-or-Tails Gut-Check, Gendlin's Focusing, Buddhist Meditation, Breath Regulation                               |
| 15 | **Stress-test a position** *(split from former #15)*                 | Probe a position for weaknesses, failure modes, gaming risks                 | 5 tools — Pre-Mortem, Construct Validity Frameworks, Design of Experiments, Factor of Safety, Goodhart-Aware Metric Selection |
| 16 | **Refine a draft / artifact** *(split from former #15)*              | Iterate to improve a work product under constraints/feedback                 | 7 tools — Blueprint Optimization Framework, Constraint Satisfaction, Feynman Technique, KPI Design                            |
| 17 | **Categorize situation type**                                        | Classify what kind of situation this is                                      | 24 tools — Cynefin, Anomaly Detection, Antifragility, Path Dependence Analysis                                                |
| 18 | **Sequence multi-party persuasion**                                  | Coalition-assembly steps; whip operations                                    | 8 tools — Coalition Mapping, BATNA-ZOPA, Game Theory Primer, Auction Design                                                   |
| 19 | **Structure problem space across aspects**                           | Orthogonal-dimension canvas (FOCUS, SWOT, etc.)                              | 7 tools — FOCUS Ideation, Hero's Journey, Musical Form, Problem-Solution-Result                                               |
| 20 | **Clear / negate / empty** *(NEW in v1.13 — apophatic move)*         | Practice un-knowing; clear concepts to make room for fresh seeing            | *(0 corpus tools; Phase 3 — Unlearning may move here on review)*                                                              |
| 21 | **Witness without intervention** *(NEW in v1.13)*                    | Open observation without manipulating; mindful allowing                      | *(0 corpus tools; Phase 3 — Vipassana, Open Awareness, RAIN candidates)*                                                      |
| 22 | **Concentrate attention** *(NEW in v1.13)*                           | Single-point focus; distinct from open witness                               | *(0 corpus tools; Phase 3 — Shamatha, Centering Prayer candidates)*                                                           |
| 23 | **Generate divergent options** *(NEW in v1.13)*                      | Brainstorming-class divergent ideation                                       | *(0 corpus tools; Phase 3 — current brainstorming tools currently use Decompose/Categorize)*                                  |
| 24 | **Improvise responsively** *(NEW in v1.13)*                          | Real-time generative, distinct from deliberative                             | *(0 corpus tools; Phase 3 — jazz improv, theatrical "yes-and")*                                                               |
| 25 | **Sense the body** *(NEW in v1.13)*                                  | Somatic awareness as primary cognitive move                                  | *(0 corpus tools; Phase 3 — Body Scan, Felt-sense practices)*                                                                 |
| 26 | **Frame the problem** *(NEW in v1.13)*                               | Choose initial frame, distinct from Categorize-situation                     | *(0 corpus tools; Phase 3 — Impact-Focused Problem currently uses Decompose)*                                                 |
| 27 | **Surface assumptions** *(NEW in v1.13)*                             | Make implicit explicit                                                       | *(0 corpus tools; Phase 3 — Pre-mortem assumptions audit, Five Whys assumption probe)*                                        |
| 28 | **Reflect on past action** *(NEW in v1.13)*                          | AAR, Schön reflection-on-action                                              | *(0 corpus tools; Phase 3 — current AAR uses Run experimental cycle)*                                                         |
| 29 | **Calibrate confidence** *(NEW in v1.13)*                            | Brier scoring, prediction journaling, posterior revision                     | 1 tool — Unlearning / Bayesian Dis-updating *(remapped by Card 03 from former #15)*                                           |
| 30 | **Imagine counterfactually** *(NEW in v1.13)*                        | Backward-looking, distinct from forward-projection                           | *(0 corpus tools; Phase 3 — Counterfactual Reasoning currently uses Project alternative futures)*                             |
| 31 | **Label affect** *(NEW in v1.13)*                                    | Affect-labeling family — names emotions to regulate                          | *(0 corpus tools; Phase 3 — RAIN, name-it-to-tame-it)*                                                                        |
| 32 | **Listen empathically** *(NEW in v1.13)*                             | NVC, Bohm dialogue, deep listening practice                                  | *(0 corpus tools; Phase 3 — current NVC uses Run dialogue protocol)*                                                          |
| 33 | **Articulate values** *(NEW in v1.13)*                               | Values clarification                                                         | *(0 corpus tools; Phase 3 — Eulogy Exercise, Ikigai currently use Reframe across lenses)*                                     |
| 34 | **Derive via formal rules** *(NEW in v1.13)*                         | Logic, proof, computation as deductive cognitive move                        | *(0 corpus tools; Phase 3 — current Proof tools use Decompose; Logic tools use Reframe)*                                      |
| 35 | **Compare against paradigm case** *(NEW in v1.13)*                   | Casuistry, case-based reasoning                                              | *(0 corpus tools; Phase 3 — current Casuistry uses Categorize-situation)*                                                     |
| 36 | **Cultivate emotion** *(NEW in v1.13 — added in Gate 3 corpus test)* | Active generation of a felt state (Metta, Tonglen, Bodhicitta, Awe practice) | *(0 corpus tools; Phase 3 — see Cards 11/12)*                                                                                 |

> **Operation vs. tool description.** An Operation is the *kind of cognitive move* multiple tools make; a tool description is the *specific way that tool makes the move*. "Score and rank options" is an Operation; "plot stakeholders on a Power × Interest 2×2 and triage by quadrant" is a description of Mendelow specifically. The distinction matters because the Operation layer's job is enabling cross-cutting query — "show me every score-and-rank tool regardless of Domain" — which collapses if every tool has a unique Operation string.

> **Phase 3 remapping note:** Several currently-classified tools use a v1.12.0-era Operation that has a more precise v1.13.0 equivalent now available (e.g., AAR currently at *Run experimental cycle* — better fit *Reflect on past action*; Casuistry at *Categorize situation type* — better fit *Compare against paradigm case*; Counterfactual Reasoning at *Project alternative futures* — better fit *Imagine counterfactually*; Proof tools at *Decompose hierarchically* — better fit *Derive via formal rules*). Card 03 deferred per-tool Operation remappings beyond the Op #15 split; the next migration sweep can revisit using the 18 new Operations as canonical targets. The current state is internally consistent — every Operation value is canonical v1.13.0 — but the assignments could be tightened.

### 2C. Primary — **Type** (cross-cutting, NEW in v0.2)

|      Type      |                                                                               Meaning                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **instrument** | Fillable, deployable tool — has a template, protocol, workflow, or scoring schema. Most entries.                                                                     |
| **stance**     | A mode you enter, not an instrument you wield (negative capability, beginner's mind, ritual cognition). Marked separately so users don't expect a fillable template. |

### 2D. Primary — **Form** (cross-cutting, instruments only)

The shape an instrument takes. 16 form values.

|             Form            |                                What it looks like                               |
|-----------------------------|---------------------------------------------------------------------------------|
| **Matrix**                  | 2D scoring or classification grid (e.g., #19 Ease-Impact)                       |
| **Checklist**               | Yes/no or rating items (e.g., #11 Effort Justification)                         |
| **Dialogue protocol**       | Turn-based conversation script (e.g., #02 Conversation Convergence)             |
| **Scoring rubric**          | Multi-criteria scoring with aggregation (e.g., AHP)                             |
| **Mental model**            | Conceptual lens, no template (e.g., reversibility, optionality)                 |
| **Visualization technique** | Diagram/map/canvas (e.g., causal loop diagram, journey map)                     |
| **Sequenced workflow**      | Ordered steps to execute (e.g., #09 Layered Actions, FOCUS)                     |
| **Question bank**           | Set of prompts (e.g., #16 Holistic Perspective, #22 Critical Question Mapping)  |
| **Canvas**                  | Large templated area filled in (e.g., Business Model Canvas)                    |
| **Decision tree**           | Branching logic                                                                 |
| **Narrative template**      | Story shape (e.g., StoryBrand, hero's journey)                                  |
| **Heuristic**               | Rule of thumb (e.g., Occam's razor, "if in doubt, leave it out")                |
| **Algorithm**               | Formal step-by-step procedure                                                   |
| **Mnemonic**                | Memory device (e.g., SCAMPER, FOCUS itself)                                     |
| **Game / simulation**       | Playable scenario (war games, business simulations)                             |
| **Practice / ritual**       | Repeated action sequence (meditation, journaling, retrospectives)               |

> **Note:** Stance entries leave Form blank — the "stance" Type *is* the marker.

### 2E. Primary — **Scale** (cross-cutting)

|          Scale           |                      Meaning                      |
|--------------------------|---------------------------------------------------|
| **Solo**                 | 1 person                                          |
| **Dyadic**               | 2 people                                          |
| **Small group**          | 3–10                                              |
| **Large group**          | 10+                                               |
| **Organizational**       | Within a single org                               |
| **Inter-organizational** | Across orgs (negotiation, alliance, market)       |
| **Civilizational**       | Society-scale (constitutional, multigenerational) |

### 2F. Primary — **Duration** (cross-cutting)

|      Duration      |                  Meaning                   |
|--------------------|--------------------------------------------|
| **Snap**           | Sub-minute (gut check, intuitive judgment) |
| **Single session** | 5 min – 2 hr                               |
| **Workshop**       | Half-day to multi-day                      |
| **Project**        | Weeks to months                            |
| **Practice**       | Lifelong / ongoing discipline              |

### 2G. Secondary — **Lineage / source**

15 values *(expanded from 13 in v1.13 — added Legal / juridical, Medical / clinical to absorb demoted Disciplinary-tradition values).*

|             Lineage              |                                         Examples                                         |
|----------------------------------|------------------------------------------------------------------------------------------|
| Western analytic / academic      | Issue trees, MECE, formal logic                                                          |
| Eastern philosophical            | Buddhist, Daoist, Hindu — koan work, tonglen, mindfulness                                |
| Indigenous / oral traditions     | Seven-generations, council process, talking-stick                                        |
| Industrial / business            | Lean, Six Sigma, Toyota, BCG, McKinsey                                                   |
| Military / strategic             | OODA, Clausewitz, Sun Tzu, red team                                                      |
| Therapeutic / psychological      | CBT, IFS, schema, NVC                                                                    |
| Design / craft tradition         | Bauhaus, Alexander, IDEO, Ranganathan                                                    |
| Ancient Greek / Roman            | Stoicism, Socratic method, rhetoric                                                      |
| Religious / monastic             | Lectio divina, examen, casuistry                                                         |
| Scientific method                | Popper falsification, RCTs, peer review                                                  |
| Mathematical / formal            | Proof techniques, set theory                                                             |
| Folk / vernacular                | Heuristics passed down without formal authorship                                         |
| Modern productivity / self-help  | GTD, Atomic Habits, Designing Your Life                                                  |
| Legal / juridical *(NEW v1.13)*  | Anglo-American common law, civil law, statutory interpretation, constitutional reasoning |
| Medical / clinical *(NEW v1.13)* | Hippocratic, evidence-based medicine, differential diagnosis, clinical heuristics        |

### 2H. Secondary — **Posture / precondition**

|        Posture        |                           When required                            |
|-----------------------|--------------------------------------------------------------------|
| Collaborative-willing | Tool needs participants in good faith (most facilitation tools)    |
| Adversarial-tolerant  | Tool works even with conflicting interests (negotiation, red team) |
| Solo-quiet            | Tool requires uninterrupted self-reflection                        |
| Somatically-regulated | Body-state needs to be calm (contemplative, trauma work)           |
| Time-pressured-OK     | Tool works under urgency (OODA, snap heuristics)                   |
| Trust-required        | Tool only works among trusted parties (high-stakes 1:1, NVC)       |
| Low-stakes-only       | Tool fails when consequences are severe (some idea generation)     |
| Beginner-friendly     | No prior context required                                          |
| Expert-required       | Needs significant prior knowledge or training                      |

### 2I. Cross-cutting — **State** *(NEW v1.13)*

Psychological / phenomenological state the tool asks the practitioner to enter or sustain. **Distinct from Posture:** Posture is what you bring; State is what you become. Multi-value allowed. Empty list for most analytical tools — populated only when a named state is required for the tool to function. 7 values.

|          State          |                                 Character                                 |
|-------------------------|---------------------------------------------------------------------------|
| Liminal                 | Between-states; transitional thresholds (ritual, rite of passage)         |
| Flow                    | Csíkszentmihályi absorbed-engaged state (improvisation, deep practice)    |
| Playful                 | Light, generative, low-inhibition (ludic exploration, brainstorming)      |
| Numinous                | Awe-struck; mysterium tremendum (awe practices, gratitude cultivation)    |
| Contemplative-quiet     | Settled, non-grasping, open (meditation, apophatic clearing)              |
| Speculative-imaginative | Suspending disbelief; holding multiple worlds (foresight, world-building) |
| Heightened-vigilant     | Adversarial alertness; survival-mode (red team, pre-mortem)               |

### 2J. Cross-cutting — **Agent** *(NEW v1.13)*

Type of cognitive agent doing the work. **Distinct from Scale:** Scale is how many; Agent is what kind. Multi-value when multiple agent types collaborate. 6 values.

|        Agent         |                                Character                                 |
|----------------------|--------------------------------------------------------------------------|
| Solo human           | Single individual thinking alone (default for most tools)                |
| Human group          | Multiple humans co-thinking (facilitation, dialogue, consensus)          |
| Crowd / market       | Aggregated independent humans (prediction markets, Delphi, Galton's Ox)  |
| Human-AI partnership | Co-thinking with AI system (AI peer review, co-writing)                  |
| Cross-species        | Incorporating non-human cognition (cognitive ethology, biophilic design) |
| Cross-cultural       | Bridging cultural cognitive systems (Hofstede, Meyer Culture Map)        |

### 2K. Cross-cutting — **About** *(NEW v1.13)*

Subject matter the tool operates on — the *object of thought*. **Open-extensible** at ≥10-tool-applicability threshold; do not silently add singletons. **Required ≥1 value on every entry.** Multi-value common. 14 canonical values.

|         About          |                                       Character                                        |
|------------------------|----------------------------------------------------------------------------------------|
| Self / identity        | Individual-as-object (Big Five, IFS, Eulogy Exercise)                                  |
| Other / relationship   | Dyadic and interpersonal (NVC, Trust Equation)                                         |
| Group / organization   | Collective dynamics (Stakeholder mapping, Service Blueprints)                          |
| Power / politics       | Influence distribution and structures (Force Field, Coalition Mapping)                 |
| Ethics / values        | Moral / value reasoning (Deontology, Veil of Ignorance, Casuistry)                     |
| Strategy / competition | Competitive positioning, game-theoretic dynamics (Porter, Wardley, Nash)               |
| Decision / choice      | Choice under uncertainty (AHP, Pre-Mortem, Bezos Memo)                                 |
| Risk / uncertainty     | Probabilistic reasoning, hedging (Bayesian Updating, Antifragility, Real Options)      |
| Time / future          | Forecasting, ancestral, multigenerational (Horizon Explorer, Backcasting)              |
| Place / ecosystem      | Place-based, bioregional, ecological inquiry (Phase 3 — currently stub)                |
| Body / embodiment      | Somatic, physiological (Gendlin, Feldenkrais, Breath Regulation)                       |
| Mind / cognition       | Mental phenomena as object (Bias checklists, Pattern Recognition, Memory architecture) |
| Sacred / transcendent  | Contemplative / theological / numinous (Meditation, Apophatic Theology)                |
| Aesthetic / craft      | Quality-of-form perception (Alexander, Tufte, Code review)                             |

### 2L. Secondary — **Combinations**

For each tool, capture:
- **often_precedes:** [other tools]
- **often_follows:** [other tools]
- **pairs_well_with:** [other tools]
- **replaced_by:** [other tools] in [context]

This is where "playbooks" emerge. Build it out in **Phase 4** (per recommendation #3) once you have ~100+ entries classified.

---

## 3. Sample entry schema (Obsidian + Bases, v1.0 — Master_Schema.yaml v1.13.0)

Entries use the `Thinking_Tool` prototype (Master_Schema.yaml v1.13.0+). The `tt_` namespace anchors the classification facets; `Universal_Core` provides identity (`Item_ID`, `type`, `Title`) and admin fields. `tt_Domain` is single-valued (one canonical register); `tt_Cross_Domains` lists additional register spans. 9 cross-cutting facets in v1.13: Type, Form, Scale, Duration, Lineage, Posture, **State**, **Agent**, **About** *(last three added in v1.13)*.

```yaml
---
Item_ID: tt-causal-chain-breaker
type: Thinking_Tool
title: Causal Chain Breaker
tt_Source: "SOLVE eX #01"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Causal & diagnostic reasoning
tt_Operation: Locate intervention leverage
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Matrix
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
tt_Lineage:
- Western analytic / academic
tt_Posture:
- Collaborative-willing
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_Often_Precedes:
- "#14"
tt_Often_Follows:
- "#20"
- "#24"
tt_Pairs_Well_With:
- "#14"
tt_Replaced_By: []
tt_Status: classified
tt_History:
  - "2026-05-07 — initial classification (v0.2 schema)"
  - "2026-05-07 — added Field, renamed Job → Operation (v0.3 schema)"
  - "2026-05-07 — consolidated source into entry; flat naming (v0.4)"
  - "2026-05-07 — migrated to canonical Master_Schema.yaml v1.10.0; tt_ namespace + Thinking_Tool prototype (v0.5)"
  - "2026-05-07 — schema v1.11.0: dropped tt_Domain_Name; tt_Domain and tt_Cross_Domains store descriptive names (Roman numerals removed)"
  - "2026-05-10 — schema v1.13.0: re-anchored Domain (Foundational → Discursive-analytical) and Field (Causal reasoning → Causal & diagnostic reasoning); Operation tightened to canonical 'Locate intervention leverage'; new facets tt_State, tt_Agent, tt_About populated"
tags:
- "#thinking-tool"
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Quick_Notes: "Useful when root cause is outside your control. Asks: where in the chain do I have leverage?"
Needs_Processing: false
---
```

**Canonical schema authority:** `~/Obsidian/V'Ger/_Infrastructure For All Vaults/Master_Schema.yaml` (v1.13.0). **Prototype template:** `_types/Thinking_Tool.md`. **Decision history:** `V'Ger/_Infrastructure For All Vaults/! Infrastructure Decision Log.md` → entries dated 2026-05-07 (v1.10) and 2026-05-09 (v1.13). **Migration record:** `migration-crosswalk.md` + `v1_13_audit_log.md`.

Each tool has its own file in `Tool Entries/`. Bases views against these files give faceted retrieval. Queries live in the master `Thinking Tools.base` file at the root of this folder; views include By Domain, By Field, By Posture, Scale × Duration, By Lineage, and Cards. Frontmatter properties are accessed as `note.<property>`; built-in file metadata as `file.<property>`; computed values via `formula.<name>`. Filters compose with recursive `and` / `or` / `not`.

---

## 4. Phased build-out plan

### Phase 0 — Lock the facet vocabularies ✅ COMPLETE (v0.3)
- ✅ 16 Domains defined
- ✅ ~100 Fields inventoried (renamed from "Areas," then expanded in v0.3)
- ✅ Type field added (instrument vs. stance)
- ✅ 16 Form values defined
- ✅ Scale (7), Duration (5), Lineage (13), Posture (9) defined
- ✅ Terminology resolved: **Domain → Field → Operation → Tool**
- ✅ Tooling committed: Obsidian + Bases

### Phase 1 — Catalogue the seed entries ✅ COMPLETE (v0.3)
- ✅ All 26 SOLVE eX tools classified — see `Tool Entries/`
- ✅ Each tool has Domain, Field, Operation populated
- ✅ Validation surfaced schema drift in v1.12.0; saturation sweep (v1.13.0) addressed it

### Phase 1.5 — Saturation sweep ✅ COMPLETE (v1.0 / schema v1.13.0)
- ✅ Domain ontology locked: Path B (single-axis register only), 12 Domains
- ✅ 112 Fields locked, each anchored to exactly one Domain
- ✅ 36 Operations locked
- ✅ 3 new cross-cutting facets added: `tt_State`, `tt_Agent`, `tt_About`
- ✅ `tt_Lineage` expanded to 15 values
- ✅ External corpus test passed: 7 published lists, 52/52 placement, 0 torture-fits
- ✅ All 250 entries re-anchored; prototype-compliance audit passes (zero violations across 16 rules)

### Phase 2 — Tooling ✅ COMPLETE (v0.4)
- **Obsidian + Bases** — plain-text durability, version control, no vendor lock-in
- Vault root: this folder (`Thinking Tools/`)
- Master Bases file: `Thinking Tools.base` (root of folder) — 6 views: By Domain, By Field, By Posture, Scale × Duration, By Lineage, Cards (Bases views to be validated against v1.13.0 facet structure in Card 14)

### Phase 3 — Expand entries (active)
- 76 of 112 canonical Fields populated; 36 stubs await expansion
- Three stub Fields populated in v1.0 sprint: Wabi-sabi, Awe / numinous, Strategic patience (≥3 tools each via Cards 11/12/13)
- Remaining stub Fields prioritized by Domain coverage gap (Emotional cognition Domain is fully stub; Speculative / imaginative and Generative / improvisational each have ≥3 stub Fields)
- Sources: existing books (Decisive, Thinking in Systems, Designing Your Life, etc.), academic reviews, anthropological catalogues
- Don't try to be exhaustive; build out as needs surface

### Phase 4 — Build playbooks (last)
- Once ~100+ entries classified, document chains and sequences via the Combinations field
- E.g., "Engagement kickoff" = #20 → #08 → #21 → #12 → #25
- Highest-value layer of the library — patterns of *how tools combine*, not just what they are

---

## 5. Outstanding decisions / parking lot

### Resolved
- [x] ~~Final terminology: super-cluster vs. realm vs. territory~~ → **Domain** (v0.2)
- [x] ~~Final terminology: domain vs. area vs. kind~~ → **Field** (v0.3)
- [x] ~~"Job" replacement~~ → **Operation** (v0.3)
- [x] ~~Hierarchy vs. faceted vs. hybrid~~ → **Hybrid** (v0.2)
- [x] ~~How to handle "stances" that aren't tools~~ → Separate **Type** field (v0.2)
- [x] ~~Tooling commit~~ → **Obsidian + Bases** (v0.2)
- [x] ~~Areas (level 2) — keep or drop?~~ → **Keep, renamed Field** (v0.3)

### Open (with current recommendations)
- [ ] How granular for Domain IX (disciplinary traditions) — recommendation: **one level deep only** ("Legal" not "Contract law / Tort law"). Sub-discipline lives in `notes` or `tags`, not the hierarchy.
- [ ] "Difficulty" / "expertise required" field beyond posture — recommendation: **defer**; posture covers most.
- [ ] Tools that are themselves *libraries* (the 26 SOLVE eX is one; SCAMPER is another) — recommendation: **parent + children**, with each child entry linking back via a `parent` field.
- [ ] Versioning when a tool is refined — recommendation: **append-only `history` field**, edit in place. Don't fork.
- [ ] Cross-references with non-tool resources (papers, books, videos) — recommendation: **`sources` field on each tool**, no parallel library.

---

---

# APPENDIX: Source Conversation (Raw Material)

> Below is the working conversation from which this taxonomy was built. It's rough material — not yet organized, but useful as the trail of thought that led to the structure above.

## Round 1 — The seed material: 26 SOLVE eX thinking tools

The folder contained 26 numbered text files, all dated December 5, 2023:

| #  |                          Name                         |
|----|-------------------------------------------------------|
| 01 | Causal Chain Breaker (a.k.a. Domino Sequence Breaker) |
| 02 | Conversation Convergence Process                      |
| 03 | Critical Consensus Constructor                        |
| 04 | Delphi Forecasts and Predictions                      |
| 05 | Dynamic Feedback Mapper                               |
| 06 | Constructive Contrarian Guide                         |
| 07 | Collaborative Conversation Navigator                  |
| 08 | Holistic Perspective Harmonizer                       |
| 09 | Layered Actions Breakdown                             |
| 10 | Horizon Explorer                                      |
| 11 | Effort Justification Meter                            |
| 12 | Collective Objective Builder                          |
| 13 | Priority-Based Requirements Matrix                    |
| 14 | Impact-Focused Problem Approach                       |
| 15 | Heads-or-Tails Gut-Check                              |
| 16 | Holistic Perspective Toolkit                          |
| 17 | Collective Idea Explorer                              |
| 18 | Blueprint Optimization Framework                      |
| 19 | Ease-Impact Assessment Matrix                         |
| 20 | Context Clarity Navigator                             |
| 21 | Prioritized Purpose Planner                           |
| 22 | Critical Question Mapping                             |
| 23 | Experimental Innovation Cycle                         |
| 24 | Perspective Pivot Workshop                            |
| 25 | FOCUS Ideation                                        |
| 26 | Holistic Systems Mapper                               |

## Round 2 — Initial grouping by job (8 jobs)

After studying all 26 tools, they were grouped by what cognitive *job* each performs:

**1. Frame the problem (make sure you're solving the right thing)**
- 01 Causal Chain Breaker — trace the chain back; intervene where you actually have leverage
- 14 Impact-Focused Problem Approach — decompose, attack highest-impact piece first
- 20 Context Clarity Navigator — force precision: problem (statement) vs. issue (question) vs. opportunity ("what if…")
- 24 Perspective Pivot Workshop — reframe across 9 dimensions
- 26 Holistic Systems Mapper — position central process within layers (immediate / related / external / feedback)

**2. See it from every angle**
- 08 Holistic Perspective Harmonizer — owner / empathy / external / contrary / unbiased viewpoints
- 16 Holistic Perspective Toolkit — deep 5W1H question bank
- 22 Critical Question Mapping — brainstorm questions (not answers); categorize, prioritize

**3. Set goals & purpose**
- 12 Collective Objective Builder — align individual motivations with team goal via "How can…" / "How to…"
- 13 Priority-Based Requirements Matrix — classify every element 0–3 (Not Required → Mandatory)
- 21 Prioritized Purpose Planner — list every reason as "To + action verb"; prioritize; expand top purpose

**4. Group dynamics & dialogue**
- 02 Conversation Convergence Process — A states → B paraphrases → B clarifies → switch → chart
- 03 Critical Consensus Constructor — build commitment to "best possible" decision (not unanimous)
- 06 Constructive Contrarian Guide — formal devil's advocate role
- 07 Collaborative Conversation Navigator — true dialogue (understanding > persuasion)

**5. Generate ideas**
- 17 Collective Idea Explorer — individual ideation → anonymous redistribution → enhancement → categorization
- 25 FOCUS Ideation — Foundation / Objective / Constraints / Understanding / Strategy

**6. Prioritize & decide**
- 11 Effort Justification Meter — 10-question rubric scored 1–10 → continue / halt / postpone
- 15 Heads-or-Tails Gut-Check — flip a coin; reaction reveals true preference
- 19 Ease-Impact Assessment Matrix — 3×3 grid; score 1–9; chase the "9s"

**7. Look ahead**
- 04 Delphi Forecasts and Predictions — multi-round anonymous expert questionnaires
- 10 Horizon Explorer — possible / probable / preferred futures

**8. Move from idea to execution**
- 05 Dynamic Feedback Mapper — design feedback systems
- 09 Layered Actions Breakdown — recursive "How?" (3–5 levels deep)
- 18 Blueprint Optimization Framework — idea → pros/cons → modify → cross-pollinate → roadmap
- 23 Experimental Innovation Cycle — vision → hypothesis → experiment → insight → integrate

**Patterns noticed:**
- Three tools converge on "are we solving the right thing?" — 20, 24, 16/22
- Dialogue tools (02, 03, 06, 07) form a ladder: dialogue → conflict resolution → consensus, with 06 as stress-test
- Goal-setting split across 12, 13, 21 (why / who's-bought-in / what's-mandatory)
- 15 (coin flip) is the only deliberately non-rational tool
- Most consultant-relevant cluster: 01, 14, 21, 12, 03, 25, 18, 23 — near-complete engagement workflow

## Round 3 — 14 jobs the original 26 don't really cover

The set's shape: collaborative, qualitative, workshop-oriented, consensus-leaning. Assumes a facilitator with willing participants in non-zero-sum context. Missing:

1. **Quantitative & probabilistic reasoning** — Fermi, Bayes, EV, base rates, sensitivity analysis
2. **Debiasing & adversarial stress-testing** — pre-mortem, inversion, red teaming, bias checklists
3. **Power, politics & influence mapping** — Mendelow, force field analysis (Lewin), influence maps, coalition mapping
4. **Strategic positioning** — Porter, SWOT, Wardley, JTBD, Blue Ocean
5. **MECE / issue trees** — McKinsey hypothesis pyramids, Minto, so-what laddering
6. **Trade-off & multi-criteria decision** — weighted matrix, Pugh, AHP, Kepner-Tregoe
7. **Analogical & lateral thinking** — TRIZ, SCAMPER, biomimicry, cross-domain transfer
8. **Dynamic systems modeling** — causal loop diagrams, stock-and-flow, feedback delays
9. **User-centered design** — JTBD, journey maps, personas, empathy maps
10. **Negotiation** — BATNA/ZOPA, interest-based bargaining
11. **Sense-making in different conditions** — Cynefin, OODA
12. **Constraint / bottleneck thinking** — Theory of Constraints (Goldratt), critical chain
13. **Metacognition & double-loop learning** — AAR, Argyris, retrospectives
14. **Ethics & values reasoning** — stakeholder ethics, veil of ignorance, deontology/consequentialism/virtue

Highest-leverage gaps for management consulting work: power/politics mapping, pre-mortem/inversion, quantitative reasoning, MECE issue trees.

## Round 4 — 28 more jobs across 10 meta-clusters (A–J)

**A. Epistemic / knowledge:** Calibration, Falsification design, Argument mapping, Operationalization
**B. Decision-quality:** Reversibility classification, Process-vs-outcome separation, Optionality preservation, Black-swan reasoning
**C. Personal / self-management:** Values clarification & life design, Self-knowledge / temperament, Time & energy allocation, Habit & behavior design
**D. Communication:** Audience analysis, Narrative architecture, Visual/spatial communication
**E. Relational / conflict:** High-stakes 1:1 conversation, Trust calibration, Cross-cultural translation
**F. Incentive / mechanism:** Mechanism / incentive design, Principal-agent diagnosis
**G. Creativity:** Constraint-driven creativity, Incubation protocols
**H. Imagination / visioning:** Mental simulation, Backcasting
**I. Learning & knowledge-management:** Deliberate practice design, External brain architecture
**J. Meta-tool:** Tool selection, Tool composition / chaining

## Round 5 — 9 super-clusters with ~50 sibling domains

**I. Foundational cognitive operations:** Logical / formal reasoning, Causal reasoning, Diagnostic / abductive, Pattern recognition & anomaly detection, Counterfactual / modal, Combinatorial / enumerative

**II. Modes of inquiry:** Empirical / scientific method, Historical, Forensic / investigative, Hermeneutic / interpretive, Ethnographic / participant-observation, Phenomenological

**III. Non-discursive cognition:** Embodied / kinesthetic / somatic, Aesthetic / sensory / connoisseurship, Intuitive / felt-sense, Contemplative / meditative, Oneiric / dream-work, Numinous / mystical

**IV. Inner / psychological work:** Psychotherapeutic, Trauma-informed, Existential / meaning-making, Grief & loss, Identity / self-narrative, Defense-mechanism / shadow

**V. Symbolic systems:** Linguistic, Semiotic, Rhetorical, Discourse / frame analysis, Translation / code-switching

**VI. Collective & networked cognition:** Crowd / market wisdom, Network / graph thinking, Game-theoretic strategic interaction, Coordination / Schelling-point, Cultural evolution / memetics, Commons / collective-action

**VII. Substrate processes:** Memory / mnemonic, Attention / focus, Habit & automaticity, Sleep & cognition, State management

**VIII. Moral / value cognition:** Ethical reasoning, Casuistry, Moral imagination, Civic / political, Theological / sacred

**IX. Disciplinary traditions:** Legal, Medical / clinical, Military / strategic, Financial / accounting, Engineering / design, Architectural / spatial, Mathematical / proof, Programming / algorithmic, Musical / temporal-aesthetic

**X. Negative cognition / clearing:** Beginner's mind / shoshin, Negative capability, Apophatic reasoning, Unlearning / deprogramming, Silence / pause

## Round 6 — Final super-clusters added (XI–XVI) + classification system

**XI. Emotional cognition:** Appraisal-theoretic, Gratitude / awe / reverence, Disgust / aversion, Compassion / loving-kindness

**XII. Play, humor, improvisation:** Ludic, Humor / wit, Improvisation / "yes-and"

**XIII. Speculative / fictional:** World-building, Thought-experiment construction, Alternate-history reasoning

**XIV. Liminal / threshold:** Ritual cognition, Initiation / rite-of-passage, Failure / repair / forgiveness, Hope / faith / surrender

**XV. Spatial / temporal / ecological:** Place-based / topophilic, Bioregional / ecological, Ancestral / multigenerational, Chronesthesia / time-sense

**XVI. Cross-substrate cognition:** Cognitive ethology, Neurodivergent cognitive modes, Human-AI partnership, Magical / sympathetic / metaphoric

**Plus:** Curiosity / wonder cultivation as standalone job

**Boundary observations:**
- The category "thinking tool" stretches at the edges — some entries are *modes you inhabit* (ritual, hope-as-stance, beginner's mind) rather than *instruments you wield*. Need a category for these alongside fillable templates. (Resolved v0.2: Type field with instrument/stance values.)
- Disciplinary cluster (IX) could fan out indefinitely. Filter: does the discipline have *transferable* cognitive structure, or is its toolkit purely intra-domain?
- ~95 sibling-level domains across all rounds is roughly the right order of magnitude for a Library of Congress.

## Round 7 — Faceted classification system (the basis of section 2 above)

Faceted classification (Ranganathan style) was chosen over single hierarchical (Dewey) because tools fit multiple categories. The 5 primary facets + 3 secondary metadata fields are detailed in section 2 of this document. (After v0.3: 6 primary facets — Domain, Field, Type, Form, Scale, Duration; 3 secondary — Lineage, Posture, Combinations. Plus level-3 Operation as entry-level metadata.)

The 4 practical recommendations (now Phase 0–4 in section 4):
1. Start with facets, not entries — lock down the values for each facet first
2. Use a tool with proper structured metadata — Notion, Airtable, or Obsidian + Bases
3. Build the "playbook" (combinations) layer last — patterns won't be visible until ~100+ entries
4. Reserve one facet value for "cognitive stance" that doesn't fit the tool metaphor — ritual, contemplative practice, hope-as-posture

## Round 8 (v0.2) — Implementation pass

Resolved decisions:
- Renamed "super-cluster" → **Domain**; dropped second-level "Area" (jobs were level 2)
- Added **Type** field (instrument / stance) as a separate primary facet, removed "Stance / posture" from Form
- Committed to **Obsidian + Bases**
- Recommendation #4 forcing-function executed: classified all 26 SOLVE eX tools → see `Tool Entries/`

## Round 9 (v0.3) — Terminology lock + level reinstated

Resolved decisions:
- Reinstated level 2 (renamed **Field**, mapping to academic "field of study" usage)
- Renamed level 3 from **Job** to **Operation** (cognitive operation = teleologically precise; complements spatial-categorical Field)
- Added 6 new Fields surfaced by classifying the SOLVE eX 26 (Futures thinking, Question generation, Feedback systems design, Systems mapping, Adversarial stress-testing, plus Multi-perspective analysis and Trade-off / multi-criteria decision promoted from cross-cutting)
- All 26 tool entry files updated to v0.3 schema (added `field`, renamed `job` → `operation`)

Why "Field" was chosen over "Function," "Subdomain," "Area":
- "Function" creates redundancy with Operation (both teleological) and conflicts with technical meanings (math, CS, biology, sociology)
- "Subdomain" felt too rigid / mathematical
- "Area" was workable but generic
- "Field" maps to universal academic usage (field of study, research field, problem field) — comfortable for any academic reader
