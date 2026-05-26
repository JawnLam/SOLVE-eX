---
Item_ID: tt-recognition-primed-decision
Item_Prototype: Thinking_Tool
Title: Recognition-Primed Decision (Klein RPD)
tt_Source: 'Gary Klein, Sources of Power: How People Make Decisions (1998); developed via studies of firefighters, ICU nurses, military commanders. Naturalistic decision-making (NDM) tradition; alternative to rational-choice models.'
tt_Type: instrument
tt_Domain: Speculative / imaginative
tt_Field: Backcasting & mental simulation
tt_Operation: Categorize situation type
tt_Cross_Domains:
- Discursive-analytical
- Inner / psychological work
tt_Form:
- Mental model
- Sequenced workflow
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Practice
tt_Lineage:
- Western analytic / academic
- Mathematical / formal
tt_Posture:
- Beginner-friendly
- Expert-required
tt_State:
- Speculative-imaginative
tt_Agent:
- Solo human
tt_About:
- Time / future
- Decision / choice
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Imagine A Day In This Future
- Cynefin
- Differential Diagnosis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=['Speculative-imaginative'], tt_Agent=['Solo human'], tt_About=['Time / future', 'Decision / choice']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'How experts actually decide under time pressure: pattern-match to a known situation type; mentally simulate the typical response; if simulation looks good, act; if not, modify or try another. Klein''s research on firefighters: 80%+ of decisions made via RPD; only edge cases involve comparative analysis. Implications: train experts via diverse case exposure (build pattern library); preserve mental simulation step (don''t act on first match).'
Needs_Processing: false
AI_Instructions: ''
---

# Recognition-Primed Decision (Klein RPD)

**One-line summary:** Gary Klein's model of expert decision-making under time pressure: experts pattern-match the current situation to a known type, mentally simulate the typical response, and act if the simulation looks good — only modifying or comparing alternatives when the simulation reveals problems.

**When to reach for it:** Time-pressured decisions where deliberate analysis isn't feasible (firefighting, emergency medicine, military command, sports, software incident response); training experts (RPD-based training builds pattern libraries); coaching novices toward expertise; understanding why experts seem to "just know" what to do; and any context where pattern recognition + simulation outperforms slower comparative analysis.

---

## Purpose Of This Thinking Tool

**Recognition-Primed Decision (RPD)** describes how experts decide under time pressure. The structure:

1. **Recognize the situation** — pattern-match current circumstances to a known type from prior experience.
2. **Identify the typical response** — what generally works in this type of situation.
3. **Mentally simulate** — imagine carrying out the response. Does it work?
4. **Act if the simulation succeeds.** If not, modify the response or try another pattern.
5. **Do all this in seconds** — experts compress what would take novices much longer.

Klein's research found that 80%+ of expert decisions follow this pattern — not the rational-choice model of "list options, weigh trade-offs, pick best." Only edge cases or genuinely novel situations trigger comparative analysis.

The non-obvious operational insight is that **expertise isn't about better analysis; it's about better pattern recognition.** Experts don't think faster than novices through the same options; they recognize the situation faster and skip directly to the appropriate action. The slow reasoning happens during training (when patterns are learned), not at decision time.

A second insight: **the mental simulation step is essential and skippable.** Skilled experts mentally simulate the response before acting; less-skilled "experts" sometimes skip this and act on first pattern match. The simulation catches mismatches between the pattern and the specific situation. Skipping it produces the failure mode of "fighting the last war" — applying patterns that don't fit.

A third insight: **RPD validates intuition while bounding it.** Expert intuition isn't magic; it's compressed pattern-recognition. This validates trusting expert judgment under time pressure. But intuition is wrong when the pattern library is wrong (lack of experience in the specific domain) or when the situation is genuinely novel. Bounded intuition is the calibrated stance.

A fourth insight: **the framework has training implications.** Building expertise = building a pattern library. Diverse case exposure (varied situations, with feedback on outcomes) builds the recognition base. Single-track experience builds shallow expertise that fails outside the narrow track.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "rational analysis under time pressure" fallacy.** Comparative analysis takes too long for fast-moving situations; RPD describes what actually works.
2. **The "trust intuition unconditionally" trap.** Intuition without simulation produces overconfidence; RPD's mental-simulation step bounds it.
3. **The "novice training" mismatch.** Training that emphasizes analysis over pattern-recognition fails to build expertise. RPD prescribes case-exposure-based training.

For commanders, emergency responders, surgeons, software incident responders, executives in crisis, athletes, and anyone making time-pressured expert decisions, RPD is foundational descriptive and prescriptive model.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | When facing a time-pressured decision, recognize first. Pattern-match the      |
|      | situation to types you've seen before.                                            |
|    2 | Identify the typical response associated with this pattern.                     |
|    3 | Mentally simulate the response. Walk through how it would unfold.              |
|    4 | If simulation succeeds, act.                                                      |
|    5 | If simulation reveals problems, modify the response. Or try another pattern.   |
|    6 | If situation is genuinely novel (no good pattern match), then engage           |
|      | comparative analysis.                                                            |
|    7 | After acting, reflect. Did the pattern fit? Did the response work? Update      |
|      | pattern library.                                                                  |
|    8 | Build expertise via diverse case exposure with feedback. Each case adds to     |
|      | pattern library.                                                                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE RPD PROCESS

   Situation encountered
       ↓
   Pattern recognition: "this is like X"
       ↓
   Typical response retrieved from memory
       ↓
   Mental simulation: "what happens if I do this?"
       ↓
   ┌─ Simulation succeeds → Act
   │
   └─ Simulation fails → Modify response or recognize
                          differently → re-simulate

   The whole loop: often <30 seconds for experts.

THE THREE-VARIANT TYPOLOGY (Klein)

   VARIANT 1: SIMPLE MATCH
       Pattern recognition is clear; typical response
       fits; act.
       (Most common; fastest.)

   VARIANT 2: DIAGNOSIS
       Pattern unclear; gather more info; recognize;
       respond.
       (Slower; in ambiguous situations.)

   VARIANT 3: EVALUATING COURSE OF ACTION
       Pattern recognized but typical response may not
       fit; mental simulation reveals problems;
       modify.
       (Slowest; in nuanced situations.)

   Variant 1 dominates for routine expert work;
   Variants 2-3 for edge cases.

THE MENTAL-SIMULATION DISCIPLINE

   The simulation step is what separates skilled from
   unskilled expertise:

   SKILLED EXPERT:
       Recognizes pattern → mentally walks through
       response → catches "this doesn't quite fit"
       before acting → modifies or pursues different
       pattern.

   UNSKILLED "EXPERT":
       Recognizes pattern → acts immediately on
       typical response → discovers mismatch in
       reality → recovers (or doesn't).

   The mental simulation is fast (seconds) but
   high-leverage. Don't skip it.

THE KEY EXAMPLE (KLEIN'S FIREGROUND COMMANDER)

   Klein's classic case:

   Fireground commander arrives at house fire.
   Expected pattern: typical kitchen fire; vent and
   ventilate.

   Observation: silent room; unusual heat
   distribution; floor unusually hot.

   The pattern doesn't quite match. Mental simulation
   of "vent and ventilate" produces unease.

   Commander orders evacuation; minutes later, the
   floor collapses (basement fire below — pattern was
   wrong).

   This is RPD with mental simulation: pattern
   recognition is the start; the simulation catches
   misfit; the action is corrected.

   Without mental simulation: act on first match;
   floor collapse with crew on it.

THE TRAINING IMPLICATIONS

   Building expertise via RPD:

   1. DIVERSE CASE EXPOSURE
      Many situations of varying types build pattern
      library.
      Single-track experience builds shallow expertise.

   2. FEEDBACK ON OUTCOMES
      Pattern + outcome feedback consolidates
      memory.
      Without feedback, patterns don't strengthen.

   3. DELIBERATE EDGE CASES
      Train on the unusual; routines pattern-match
      easily; edges are where pattern-matching fails.

   4. POST-ACTION REVIEW
      Discuss what was recognized, simulated, acted
      on. Strengthens the cognitive process.

   5. SIMULATIONS / DRILLS
      Realistic scenarios build pattern library
      without the cost of real failures.

THE NOVICE-EXPERT TRANSITION

   Novice decisions:
       Conscious analysis of options
       Slow
       Often correct in stable situations
       Often wrong in novel ones (no pattern library)

   Intermediate:
       Mix of analysis and pattern-matching
       Some confidence; some hesitation
       Common pitfall: false-confident pattern match
       in novel situations

   Expert:
       Fast pattern recognition + mental simulation
       Variant 1 dominates routine work
       Variants 2-3 for edge cases
       Bounded by quality and breadth of pattern
       library

   Building expertise: deliberate practice in diverse
   cases.

THE COMMON FAILURE MODES

   1. SKIPPING MENTAL SIMULATION
        Acting on first pattern match. Recovery: build
        habit of imagining the action.

   2. PATTERN-LIBRARY GAPS
        No relevant pattern; defaulting to closest
        match anyway. Recovery: recognize novelty;
        engage comparative analysis.

   3. FIGHTING THE LAST WAR
        Applying old pattern to genuinely changed
        situation. Recovery: question whether pattern
        still applies; check key features.

   4. UNDERTRAINED EXPERTISE
        Confidence without breadth. Recovery: diverse
        case exposure with feedback.

   5. RATIONAL-MODEL TRAINING
        Training that emphasizes options analysis;
        doesn't build pattern library. Recovery: case-
        based training.

   6. NO DEBRIEFING
        Decisions made; no reflection. Recovery:
        AAR-style review of pattern match, simulation,
        action.

THE OPERATIONAL TEMPLATE

   Time-pressured decision: ___________________________

   Pattern recognition:
       This situation looks like: ____________________
       Key features matching: ________________________
       Confidence in pattern match: ___________________

   Typical response for this pattern:
       _________________________________________________

   Mental simulation:
       Step 1 of response: ___________________________
       Step 2: _______________________________________
       Outcome predicted: ____________________________
       Anything off? _________________________________

   Decision:
       Act on response: Y / N
       If N, modification: ___________________________
       Or different pattern: _________________________

   After action:
       Did it work? __________________________________
       Was the pattern correct? ______________________
       Update to pattern library: ____________________
```

> **Operational notes:** Four disciplines. (1) Recognize first, then simulate, then act. The sequence matters. Skipping the simulation produces "fighting the last war" failures; skipping recognition produces slow novice analysis. (2) Build pattern library via diverse case exposure. Expertise isn't generic; it's pattern-specific. The library determines what you can recognize. Single-track experience builds shallow expertise. (3) Bound trust in intuition. RPD validates expert intuition under time pressure but doesn't make it infallible. The pattern library may have gaps; the situation may be novel. The mental simulation catches some misfits; awareness of pattern-library limits catches others. (4) Train via cases with feedback. Rational-analysis training doesn't build pattern recognition; case-based training with outcome feedback does. The training method matches the cognitive model.
