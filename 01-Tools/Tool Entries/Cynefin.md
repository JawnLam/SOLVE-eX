---
Item_ID: tt-cynefin
Item_Prototype: Thinking_Tool
Title: Cynefin
tt_Source: Dave Snowden, IBM Institute of Knowledge Management (1999), formalized in 'A Leader's Framework for Decision Making' (Snowden & Boone, HBR 2007). Welsh word cynefin (pronounced 'kuh-NEV-in') meaning 'place of multiple belongings.'
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: Cynefin & sense-making
tt_Operation: Categorize situation type
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Mental model
- Sequenced workflow
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Decision / choice
- Mind / cognition
tt_SOLVE_eX_Phase: [5, 6]
tt_SOLVE_eX_Step: [5.1, 6.1]
tt_Clarifies: ['Path', 'Action']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- OODA Loop
- Theory of Constraints
- Pre-Mortem
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice', 'Mind / cognition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Sorts situations into five domains based on cause-effect relationships: Clear (best practice), Complicated (good practice via expertise), Complex (emergent practice via probe-sense-respond), Chaotic (novel practice via act-sense-respond), Confusion/Aporia (sort first). Different domains require different leadership approaches. Misdiagnosing (e.g., applying Clear-domain best practice to a Complex situation) is the central failure mode. Updated 2014 model uses ''Confused'' instead of ''Disorder''.'
Needs_Processing: false
AI_Instructions: ''
---

# Cynefin

**One-line summary:** A sense-making framework — Dave Snowden's — that sorts situations into five domains based on cause-effect relationships (Clear, Complicated, Complex, Chaotic, Confusion), prescribing different decision approaches for each, and identifying the misdiagnosis between domains as the central leadership failure mode.

**When to reach for it:** Strategic decisions where situational diagnosis matters as much as the decision itself; choosing between best-practice playbooks vs. expert analysis vs. emergent experimentation vs. urgent intervention; leadership coaching on situational awareness; complexity management in technology, healthcare, military, and policy domains; and any context where applying the wrong approach to the situation type is a recurring failure mode.

---

## Purpose Of This Thinking Tool

**Cynefin** sorts situations into five domains by cause-effect characteristics:

1. **Clear** (formerly "Simple" / "Obvious") — Cause and effect are obvious; best practice exists. Approach: Sense → Categorize → Respond. Apply known best practice.
2. **Complicated** — Cause and effect are knowable but require analysis or expertise. Approach: Sense → Analyze → Respond. Use experts to find good practice (often multiple acceptable answers).
3. **Complex** — Cause and effect can only be understood in retrospect; the system itself is shifting. Approach: Probe → Sense → Respond. Run small experiments; learn what works; amplify.
4. **Chaotic** — No discernible cause-effect; immediate action required. Approach: Act → Sense → Respond. Stabilize first; understand later.
5. **Confusion** (formerly "Disorder") — Don't yet know which domain. Approach: Sort the situation into a domain first.

The non-obvious operational insight is that **the most common leadership failure is applying the wrong domain's approach.** Best practice (Clear domain) applied to a Complex situation produces brittle, fragile responses. Expert analysis (Complicated domain) applied to a Chaotic situation wastes time during a crisis. Probe-and-learn (Complex) applied to a Clear situation looks like reinventing the wheel. Each domain demands its own approach; the diagnostic question — "which domain are we in?" — is itself the leadership skill.

A second insight: **the boundary between Clear and Chaotic is dangerous.** Snowden draws it as a "cliff": situations that appear Clear (where everyone applies best practice complacently) can collapse into Chaotic when assumptions break (the 2008 financial crisis is the canonical example). The cliff means complacency about Clear-domain situations is risky.

A third insight: **Complex domain is where most contemporary leadership challenges sit.** Markets, organizations, technology adoption, social systems — these are complex (cause-effect understandable only in retrospect; emergent behavior). Tools designed for Complicated domains (analysis, planning, expertise) underperform here.

A fourth insight: **the framework is dynamic.** Situations move between domains. A Complex experiment that succeeds becomes Complicated (now we know how it works) and eventually Clear (now everyone knows). Monitoring movement is part of the practice.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "best practice for everything" trap.** Applying Clear-domain answers to Complex situations. Common in organizations with strong process cultures that miss situational variation.
2. **The "analysis paralysis in chaos" failure.** Trying to analyze a Chaotic situation when stabilizing action is required. Common in slow-moving organizations facing crises.
3. **The "experiment when expertise exists" waste.** Running probe-sense-respond on Complicated situations where experts have known answers. Common in startup cultures that reflexively prefer experimentation.

For leaders, strategists, complexity practitioners, and anyone making decisions across varied situations, Cynefin's diagnostic discipline is foundational.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the situation requiring decision or action.                            |
|    2 | Diagnose the domain. Ask: are cause-effect relationships obvious? Knowable     |
|      | with analysis? Only knowable in retrospect? Not discernible at all? Don't      |
|      | yet know?                                                                          |
|    3 | If diagnosis is "Confusion": invest in sense-making before deciding.            |
|    4 | Match approach to domain.                                                          |
|      | Clear: apply best practice. Complicated: bring in expertise. Complex: probe-   |
|      | sense-respond. Chaotic: act-sense-respond.                                      |
|    5 | Watch for boundary movements. Did a Clear situation just collapse to Chaotic?  |
|      | Has a Complex experiment yielded a Complicated answer?                          |
|    6 | For Complex domain: design small probes; instrument for learning; amplify     |
|      | what works.                                                                       |
|    7 | For Chaotic domain: act decisively for stabilization; reflect afterward.       |
|    8 | Build organizational sense-making capacity. Cynefin diagnosis improves with    |
|      | practice.                                                                          |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FIVE-DOMAIN CYNEFIN MAP

   +-------------+-------------+
   |  COMPLEX    | COMPLICATED |
   |  (emergent) | (knowable)  |
   |             |             |
   |   probe-    |   sense-    |
   |   sense-    |   analyze-  |
   |   respond   |   respond   |
   +-------------+-------------+
   |  CHAOTIC    |   CLEAR     |
   |  (no order) | (obvious)   |
   |             |             |
   |   act-      |   sense-    |
   |   sense-    |   categorize-|
   |   respond   |   respond   |
   +-------------+-------------+
        (Confusion / Aporia center: don't know yet)

   The framework's "cliff" runs between Clear and
   Chaotic — a Clear situation can collapse to Chaotic
   when assumptions break.

THE FIVE DOMAINS — DETAILED

   1. CLEAR (Obvious / Simple):
      Characteristics:
          Cause-effect is obvious to anyone
          Best practice exists
          Standardization works

      Examples:
          Customer service for a known product issue
          Standard manufacturing processes
          Routine medical procedures

      Approach: Sense → Categorize → Respond
      Leadership: command (apply known answer)

   2. COMPLICATED:
      Characteristics:
          Cause-effect is knowable but requires
          analysis / expertise
          Multiple acceptable answers possible
          Experts can sort it out

      Examples:
          Complex engineering problem with known science
          Specialized medical diagnosis
          Standard financial analysis

      Approach: Sense → Analyze → Respond
      Leadership: bring in / consult experts

   3. COMPLEX:
      Characteristics:
          Cause-effect understandable only in retrospect
          System itself shifts; emergent behavior
          Experts disagree; no clear "right answer"

      Examples:
          Market dynamics, customer adoption
          Organizational change initiatives
          Innovation, product-market fit
          Social-policy outcomes

      Approach: Probe → Sense → Respond
      Run small experiments
      Watch what emerges
      Amplify what works; dampen what doesn't
      Leadership: enable; create conditions for
      emergence

   4. CHAOTIC:
      Characteristics:
          No discernible cause-effect (yet)
          Crisis; immediate action needed
          Stabilization is the priority

      Examples:
          Acute crisis (data breach, plane in distress,
          natural disaster onset)
          Complete market collapse
          Existential threat

      Approach: Act → Sense → Respond
      Take decisive action to stabilize
      Then sense what's happening
      Then respond more thoughtfully

      Leadership: command (decisive action)

   5. CONFUSION (Disorder / Aporia):
      Characteristics:
          You don't know which domain you're in
          Multiple voices arguing for different
          domains' approaches

      Approach: Sort the situation into a domain
          before deciding. Often the highest-leverage
          move is investing in sense-making before
          acting.

      Leadership: facilitate sense-making

THE DOMAIN-BOUNDARY DYNAMICS

   Situations move between domains:

   COMPLEX → COMPLICATED:
       Successful experiments yield understanding;
       what was emergent becomes analyzable.

   COMPLICATED → CLEAR:
       Expertise democratizes; what required experts
       becomes best practice.

   CLEAR → CHAOTIC (the cliff):
       Assumptions break; what worked stops working;
       complacency becomes crisis.

   CHAOTIC → COMPLEX:
       Stabilization in chaos shifts the situation
       to where experimental learning is possible.

   The framework is dynamic; periodic re-diagnosis is
   essential.

THE WORKED EXAMPLE — STARTUP DECISIONS

   Question: How should we approach product
   development?

   Diagnosis: Complex
       Customer needs not fully known; market shifting;
       experts disagree; only retrospective
       understanding of why some products succeeded.

   Approach: Probe → Sense → Respond
       Run small experiments (MVPs, pilots)
       Instrument for learning
       Amplify what works (double down on traction)
       Dampen what doesn't (kill or pivot)

   Wrong approach: Complicated thinking
       "Hire an expert consultant; design the perfect
       product." Wastes time and money in a domain
       where the answer can only be found by trying.

   Wrong approach: Chaotic thinking
       "Just do something; we'll figure it out later."
       Without instrumentation, you can't learn from
       the chaos.

   Wrong approach: Clear thinking
       "Apply the best practice from our last
       company." But the situation is complex;
       last-time's-best-practice may not apply.

THE THE ALL-CONTEXTS-ARE-COMPLEX SIMPLIFICATION

   Some practitioners argue most contemporary
   leadership challenges (organizational change, market
   strategy, innovation) are Complex, and that other
   domains are decreasing.

   This is partially true:
       Many situations were Complicated (knowable with
       expertise) but have become Complex (faster
       change, more interaction).
       Many situations remain genuinely Complicated
       (engineering, specialized medicine).
       Some situations are still Clear (routine
       operations).

   The discipline is genuine diagnosis, not defaulting
   to "complex" for everything.

THE COMMON FAILURE MODES

   1. APPLYING WRONG APPROACH
        Best practice on Complex; analysis on Chaotic.
        Recovery: diagnose first.

   2. CLIFF COLLAPSE
        Treating volatile situation as Clear; collapses
        when assumptions break. Recovery: monitor for
        Clear-domain assumptions; have crisis playbook.

   3. UNDIAGNOSED CONFUSION
        Acting before sorting domain. Recovery: invest
        in sense-making.

   4. RIGID DOMAIN ASSIGNMENT
        Diagnosing once; never re-checking. Recovery:
        re-diagnose as situation evolves.

   5. EXPERTISE DEFAULT IN COMPLEX DOMAINS
        Bringing in consultants on Complex situations
        where probing is needed. Recovery: experiment;
        don't analyze.

   6. CRISIS-SEEKING
        Acting Chaotically (decisive) when situation
        is Complex (would benefit from probes).
        Recovery: stabilize, then probe.

   7. EXPERIMENT-DEFAULT
        Running probes when known answer exists
        (Complicated). Recovery: ask experts first.

THE OPERATIONAL TEMPLATE

   Situation: __________________________________________

   Cause-effect characteristics:
       Obvious to anyone? → Clear
       Knowable with analysis? → Complicated
       Only in retrospect? → Complex
       No discernible? → Chaotic
       Don't yet know? → Confusion

   Domain: ____________________________________________

   Matched approach:
       Clear: ___________________________________
       Complicated: _____________________________
       Complex: _________________________________
       Chaotic: _________________________________

   Boundary watch:
       Could this collapse to Chaotic? Y / N
       Has it shifted from another domain recently?

   Re-diagnosis schedule: _____________________________
```

> **Operational notes:** Four disciplines. (1) Diagnose before deciding. The single biggest discipline. Wrong-domain approaches fail predictably; right-domain approaches generally work. The diagnostic question precedes the decision. (2) Match approach to domain. Each domain has its appropriate move; mixing them produces failure modes. Best practice in Complex; experimentation in Clear; analysis in Chaotic — all wrong. (3) Watch boundaries. Situations move between domains. The Clear-to-Chaotic cliff especially: complacency about working systems leaves no playbook for collapse. (4) Build sense-making capacity. Domain diagnosis improves with practice. Organizations that build the capacity at multiple levels (not just the CEO) handle varied situations more robustly.
