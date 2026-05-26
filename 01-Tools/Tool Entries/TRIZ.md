---
Item_ID: tt-triz
Item_Prototype: Thinking_Tool
Title: TRIZ
tt_Source: Genrich Altshuller, Soviet patent engineer (1946 onward); developed via study of 200,000+ patents to identify recurring innovation patterns. TRIZ = 'Theory of Inventive Problem Solving' (Russian acronym). Codified in The Innovation Algorithm (1969) and translated into Western practice from 1990s onward.
tt_Type: instrument
tt_Domain: Non-discursive cognition
tt_Field: Metaphoric / analogical / sympathetic reasoning
tt_Operation: Reframe across lenses
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Question bank
tt_Scale:
- Solo
- Small group
tt_Duration:
- Workshop
tt_Lineage:
- Western analytic / academic
- Industrial / business
- Mathematical / formal
tt_Posture:
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1, 4.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- SCAMPER
- Biomimicry
- Role-Based Analogy
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Altshuller''s analysis: most engineering problems are not unique; they''re variants of recurring contradictions already solved in some other domain. TRIZ catalogs 40 inventive principles (e.g., segmentation, asymmetry, dynamics, prior counter-action) and 39 generic engineering parameters; the contradiction matrix maps ''parameter to improve × parameter that worsens'' to applicable principles. Force the abstract contradiction; find the cross-domain solution.'
Needs_Processing: false
AI_Instructions: ''
---

# TRIZ

**One-line summary:** Genrich Altshuller's "Theory of Inventive Problem Solving" — drawn from analysis of 200,000+ patents — that recasts engineering problems as recurring contradictions and points to one of 40 inventive principles (and a contradiction matrix mapping problem types to principles) for cross-domain solution.

**When to reach for it:** Engineering and product-design problems with apparent trade-offs (improving one parameter worsens another); innovation workshops where conventional approaches have stalled; cross-domain problem-solving (your industry's problem may be solved in another); patent-strategy work; and any context where reframing the abstract contradiction unlocks solutions invisible at the concrete level.

---

## Purpose Of This Thinking Tool

**TRIZ** treats invention as systematic, not creative-flash. The structure:

1. **State the engineering / design contradiction** — improving parameter X worsens parameter Y. (e.g., stronger material = heavier; faster speed = more fuel.)
2. **Translate to abstract form** using TRIZ's 39 generic parameters.
3. **Look up the contradiction matrix** — for "improve X / worsens Y," it suggests applicable principles from the 40 Inventive Principles.
4. **Translate principles back** to your specific domain.
5. **Generate concrete solutions.**

The non-obvious operational insight is that **most "invention" is rediscovery of cross-domain solutions.** Altshuller's analysis showed engineering problems aren't unique to their domain; the same abstract contradictions recur, and other domains have already solved them. TRIZ formalizes the pattern matching across domains.

The 40 Inventive Principles (selected examples):
1. Segmentation (divide an object into independent parts)
2. Taking out (extract the disturbing part / property)
3. Local quality (transition from homogeneous to heterogeneous structure)
4. Asymmetry (replace symmetrical with asymmetrical)
5. Merging (bring identical objects together)
13. The other way round (invert the action used to solve)
15. Dynamics (allow object characteristics to change for optimal performance)
17. Another dimension (move object motion into 2D / 3D)
35. Parameter changes (change the physical state, density, flexibility)
40. Composite materials (replace homogeneous with composite)

A second insight: **the framework's value is forcing abstraction.** Engineers default to concrete problem-statement and search for concrete solutions. TRIZ forces translation up to abstract contradiction, where cross-domain matching becomes possible. The translation is the discipline.

A third insight: **TRIZ has critics and limits.** The framework is engineering-centric; many "principles" are obvious to experienced engineers; the contradiction matrix can produce many candidates without prioritization. Defenders argue: the systematic prompt is the value; even obvious principles get missed without it.

A fourth insight: **the framework extends beyond mechanical engineering.** Software-design contradictions (CAP theorem-style trade-offs), business-model contradictions, organizational contradictions all benefit from TRIZ-style abstraction. The principle catalog adapts to non-engineering domains in modern practice.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "stuck in domain" failure.** Engineers solve problems within their industry's known approaches; TRIZ surfaces other industries' solutions to similar abstract problems.
2. **The "creative blank" stall.** When inspiration fails, TRIZ provides systematic prompts via the principle catalog.
3. **The "trade-off acceptance" trap.** Treating contradictions as immutable trade-offs. TRIZ's premise: the same contradiction has been resolved elsewhere; find the resolution.

For engineers, product designers, innovation consultants, and anyone facing systematic problem-solving with apparent trade-offs, TRIZ is foundational technique.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | State the problem with the contradiction. "We want X but currently can't have   |
|      | X without sacrificing Y."                                                        |
|    2 | Translate parameters to TRIZ's 39 generic engineering parameters.              |
|    3 | Look up the contradiction matrix: "improve P1 / worsens P2" → list of principles|
|      | most often used.                                                                  |
|    4 | For each suggested principle, brainstorm concrete applications in your domain.|
|    5 | Generate multiple candidate solutions (TRIZ produces options, not one answer).|
|    6 | Evaluate candidates: technical feasibility, cost, impact.                       |
|    7 | Prototype the most promising; iterate.                                            |
|    8 | Document the contradiction-and-resolution for future reference.                 |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE TRIZ CONTRADICTION

   Specific:
       "We want a stronger structural beam, but stronger
       means heavier."

   Abstract (using TRIZ's 39 parameters):
       Improve: Strength (parameter 14)
       Worsen: Weight (parameter 1)

   Contradiction matrix lookup:
       For (improve 14, worsen 1): Principles 1, 8, 15, 40
       1: Segmentation
       8: Anti-weight
       15: Dynamics
       40: Composite materials

   Translate back:
       Segmentation: many small beams instead of one
       large.
       Anti-weight: counterweight or buoyancy.
       Dynamics: variable structure, flexes under load.
       Composite materials: layered carbon-fiber.

   Each is a candidate solution. Evaluate per problem
   context.

THE 40 INVENTIVE PRINCIPLES (key set)

   STRUCTURAL:
   1. Segmentation
   2. Taking out
   3. Local quality
   4. Asymmetry
   5. Merging
   6. Universality (one part, many functions)

   FUNCTIONAL:
   13. Inversion (the other way round)
   14. Spheroidality
   15. Dynamics
   17. Another dimension

   TIMING:
   9. Prior counter-action
   10. Prior action
   11. Beforehand cushioning
   12. Equipotentiality

   MATERIAL/PHYSICAL:
   35. Parameter changes
   36. Phase transitions
   37. Thermal expansion
   40. Composite materials

   OPERATIONAL:
   23. Feedback
   25. Self-service
   29. Pneumatics / hydraulics

   The 40 cover most of recurring inventive moves
   across patent literature.

THE WORKED EXAMPLE — REFRIGERATOR

   Problem: improve refrigeration efficiency (less
   energy) without increasing equipment cost.

   Abstract:
       Improve: Energy use (parameter 22)
       Worsen: Cost (parameter 24)

   Matrix suggests principles: 7 (nesting), 13
   (inversion), 19 (periodic action), 35 (parameter
   changes).

   Concrete generation:
       Periodic action: refrigerator cycles cooling
       only when needed (already standard in modern
       fridges)
       Inversion: instead of cooling the air to cool
       contents, isolate contents better (better
       insulation)
       Parameter changes: phase-change materials in
       walls store cold; release as needed

   Each becomes a solution path; engineering team
   evaluates feasibility / cost.

THE COMMON FAILURE MODES

   1. INCOMPLETE PARAMETER TRANSLATION
        Stuck with concrete problem; no abstraction.
        Recovery: force the 39-parameter mapping.

   2. PRINCIPLE LIST WITHOUT TRANSLATION
        "Use principle 15." But how, in your domain?
        Recovery: each principle needs concrete
        translation.

   3. ONE-SOLUTION FIXATION
        Picking one candidate and committing without
        evaluating alternatives. Recovery: TRIZ
        produces multiple candidates; evaluate
        comparatively.

   4. MATRIX-WORSHIP
        Treating the contradiction matrix as
        deterministic. Recovery: it's a heuristic;
        principles outside the suggested set may
        also apply.

   5. ENGINEERING-ONLY APPLICATION
        Limited to mechanical / engineering problems.
        Recovery: software, business, organizational
        adaptations exist.

   6. LACK OF PROTOTYPING
        Generating ideas without testing. Recovery:
        prototype top candidates.

THE OPERATIONAL TEMPLATE

   Problem statement (specific):
       _________________________________________________

   Contradiction:
       Want to improve: _____________________________
       Currently worsens: ____________________________

   TRIZ parameters:
       Improve parameter #: _____ (name: __________)
       Worsen parameter #: _____ (name: __________)

   Contradiction matrix lookup:
       Suggested principles: ________________________

   Concrete solutions per principle:
       Principle X applied: _________________________
       Principle Y applied: _________________________
       Principle Z applied: _________________________

   Top candidate(s) for prototyping:
       _________________________________________________

   Evaluation criteria: _______________________________
```

> **Operational notes:** Four disciplines. (1) Force the abstraction. The translation from concrete problem to TRIZ's abstract parameters is the discipline; without it, you stay in your domain's known solutions. (2) Generate multiple candidates. TRIZ produces options; pick after evaluation, not by first-fit. (3) Translate principles back concretely. "Use segmentation" without specific application is empty. The principle is a prompt; the concrete application is the work. (4) Prototype to validate. The matrix suggests; experimentation confirms. Many TRIZ-generated candidates fail under domain constraints; only prototyping reveals which.
