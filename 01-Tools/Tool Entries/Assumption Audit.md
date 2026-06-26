---
Item_ID: tt-assumption-audit
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Assumption Audit
tt_Source: "Synthesis: Chris Argyris's *Ladder of Inference* (1990) — the canonical Western analytic frame for assumption-surfacing; Sakichi Toyoda's *Five Whys* (Toyota Production System, 1930s) — the manufacturing-rooted iterative version; Peter Senge, *The Fifth Discipline* (1990) for the Ladder's modern systematization."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Adversarial / debiasing reasoning
tt_Operation: Surface assumptions
tt_Cross_Domains:
  - Modes of inquiry
tt_Form:
  - Question bank
  - Sequenced workflow
tt_Scale:
  - Solo
  - Small group
tt_Duration:
  - Single session
tt_Lineage:
  - Industrial / business
  - Western analytic / academic
tt_Posture:
  - Collaborative-willing
  - Beginner-friendly
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Mind / cognition
  - Decision / choice
  - Strategy / competition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
  - Pre-Mortem
  - Critical Question Mapping
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Pre-Mortem
  - Lazarus Appraisal Framework
  - Cognitive Bias Checklists
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-11 — initial classification (Zero-Gap Sweep Card 10; closes Operation #27 'Surface assumptions' — the canonical anchor)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-11
Date_Modified: 2026-05-11
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Combines the Ladder of Inference (Argyris) and Five Whys (Toyota) into an assumption-surfacing protocol. Ladder maps how data → assumption → conclusion → action, letting you trace backward from a problematic action to the assumption driving it. Five Whys forces iterative depth: each 'why' surfaces a level deeper. The two together produce a saturating audit of the assumption-stack behind any position."
Needs_Processing: false
AI_Instructions: ""
---

# Assumption Audit

**One-line summary:** A two-method assumption-surfacing protocol — Ladder of Inference (Argyris) maps the path from data to action; Five Whys (Toyota) iteratively probes the *why* behind each level — combining to surface the full assumption-stack behind any position or decision.

**When to reach for it:** Decisions that "feel" right or wrong without articulated reasoning; strategic moves where the implicit assumptions need to be made explicit before commitment; team conflicts where parties seem to disagree about facts but actually disagree about underlying assumptions; pre-mortem prep where assumption-discovery is the goal.

---

## Purpose Of This Thinking Tool

Chris Argyris's *Ladder of Inference* (1990) models how humans go from data → action in a series of jumps:

1. **Observable data** (what actually happened)
2. **Selected data** (which subset we paid attention to)
3. **Added meaning** (what we made of the selected data)
4. **Assumptions** (the unstated commitments shaping the meaning)
5. **Conclusions** (the inferences drawn from the assumptions)
6. **Beliefs** (the conclusions integrated into worldview)
7. **Actions** (taken from the beliefs)

Each step is a jump. Most decision-making operates at the action layer with the lower layers invisible. The ladder makes them inspectable.

Sakichi Toyoda's *Five Whys* (1930s, Toyota Production System) is a complementary iterative move: when you have a problem (or a position), ask "why?" — then ask "why?" of the answer, repeating typically five times. Each iteration goes deeper toward root cause / root assumption.

The non-obvious operational claim: **most assumption-driven errors come from the middle layers (3-5).** People rarely err at the data-observation layer or the action layer; they err in the selected-meaning-assumption stack. The audit's value is forcing visibility on those layers.

The Two-Method synthesis:

1. **Identify the action / position / conclusion.** "We should hire X." / "This strategy will work." / "He's not a fit."
2. **Apply the Ladder going down.** What conclusion? What beliefs underwrite it? What assumptions underwrite the beliefs? What meaning was added to what data? What data was selected? What data was ignored?
3. **At each layer, apply Five Whys.** Why this assumption? Why? Why? — until you reach an assumption you cannot easily justify further.
4. **Test the assumptions.** Is each load-bearing assumption defensible? Is each one falsifiable? Is each one in fact true?
5. **Surface alternatives.** What other assumptions could fit the same data? What different conclusions would follow?

A second insight: **the assumptions you can't justify further are the ones worth examining.** Argyris called these "espoused theories" vs. "theories in use" — the gap between what we say we believe and what our actions reveal we believe. The audit closes that gap.

## Why Use This Thinking Tool

Three failure modes the protocol prevents:

1. **Acting on invisible assumptions.** Most decision-errors are not data-errors; they are assumption-errors. Visibility is the first move.
2. **Stuck-disagreement.** Parties agreeing on data, disagreeing on action, never realizing they disagree at the assumption layer. The audit surfaces this.
3. **Surface-only critique.** Critiques that target the action without engaging the underlying assumption-stack. Easy to dismiss; doesn't change the decision.

The Ladder is well-established in organizational learning (Senge, Argyris, MIT Center for Organizational Learning). Five Whys is foundational in lean manufacturing and root-cause analysis.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|  1   | State the action / position / conclusion you're auditing.                       |
|  2   | Climb down the Ladder. From the action, identify: belief → conclusion →         |
|      | assumption → added meaning → selected data → observable data.                   |
|  3   | At each layer, apply Five Whys. Why this belief? Why? Until you reach          |
|      | bedrock — an assumption you cannot further justify.                              |
|  4   | List the load-bearing assumptions. These are the ones that, if false, would    |
|      | collapse the action.                                                              |
|  5   | Test each: Is it true? Defensible? Falsifiable? What evidence supports it?     |
|      | What evidence contradicts it?                                                    |
|  6   | Generate alternatives. What other assumption could fit the same data?           |
|      | What different action would follow from a different assumption?                  |
|  7   | Decide. The action may survive the audit (good — it's now examined). Or it     |
|      | may need revision (also good — you caught it before acting).                    |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
Assumption Audit Worksheet

ACTION / POSITION / CONCLUSION BEING AUDITED:
   _____________________________________________________

LADDER OF INFERENCE (climb down from action to data):

   Action:           ___________________________________
   Belief:           ___________________________________
   Conclusion:       ___________________________________
   Assumption(s):    ___________________________________
   Added meaning:    ___________________________________
   Selected data:    ___________________________________
   Observable data:  ___________________________________

   Data IGNORED (not selected — also informative):
   _____________________________________________________

FIVE WHYS at the load-bearing assumption layer:

   Assumption: _____________________________________
   Why?  → _________________________________________
   Why?  → _________________________________________
   Why?  → _________________________________________
   Why?  → _________________________________________
   Why?  → _________________________________________

   Bedrock assumption (the one you can't justify further):
   _____________________________________________________

LOAD-BEARING ASSUMPTION TESTS:

   Assumption 1: _____________________________________
     Defensible?         [ ] yes [ ] no [ ] uncertain
     Falsifiable?        [ ] yes [ ] no
     Evidence FOR:       _____________________________
     Evidence AGAINST:   _____________________________

   Assumption 2: _____________________________________
     [same structure]

ALTERNATIVE FRAMINGS:

   If assumption X were false instead, the action would be:
   _____________________________________________________

   If different data were selected, the action would be:
   _____________________________________________________

DECISION:
   [ ] Action survives audit (examined and defensible)
   [ ] Action needs revision: _____________________________
   [ ] Need more information before deciding
```

> **Operational notes:** (1) **The hardest layer to see is "selected data."** What you didn't pay attention to is invisible by definition; deliberately asking "what data did I leave out?" requires effort. (2) **Five Whys is often more like Three Whys** in practice. The point is iterative depth, not a literal count. Stop when you reach an assumption you cannot further justify. (3) **Group audits surface cross-party assumption-differences.** Two people doing this exercise on the same action often discover they share the data but differ at the assumption layer — productive ground for dialogue. (4) **Don't audit every action.** The protocol is for non-trivial decisions or strategic commitments; trivial decisions don't earn the audit cost.

## Related Tools and Frameworks

- **Pre-Mortem** — pairs as the failure-imagination cousin; assumption audit is the assumption-surfacing companion.
- **Critical Question Mapping** — adjacent question-generation toolkit.
- **Lazarus Appraisal Framework** — affective cousin; surfaces appraisals (a sub-type of assumption) driving emotion.
- **Cognitive Bias Checklists** — adjacent debiasing tool; this audit is the structural-assumption sibling.

## Sources

- Argyris, C. (1990). *Overcoming Organizational Defenses*. Allyn & Bacon.
- Senge, P. (1990). *The Fifth Discipline: The Art and Practice of the Learning Organization*. Doubleday.
- Toyoda, S. (Toyota Production System, 1930s). Five Whys methodology.
- Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production*. Productivity Press.
- Ross, R. (1994). The Ladder of Inference. In Senge et al., *The Fifth Discipline Fieldbook*.
