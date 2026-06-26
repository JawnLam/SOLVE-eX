---

Item_ID: tt-after-action-review
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: After Action Review
tt_Source: U.S. Army Center for Lessons Learned (developed 1970s-80s, formalized in TRADOC Regulation 350-50-2 and FM 6-22). Adopted across business, healthcare (NHS), and emergency services. Documented in books like Hope Is Not a Method (Sullivan & Harper).
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: Metacognition & tool-selection
tt_Operation: Reflect on past action
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
tt_Scale:
- Small group
tt_Duration:
- Single session
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [6]
tt_SOLVE_eX_Step: [6.4]
tt_Clarifies: ['Action']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Double-Loop Learning
- Retrospective Formats
- Pre-Mortem
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Operation remap → 'Reflect on past action' (Op #28)"
  - 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
  - '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'U.S. Army''s structured post-action review. Four questions: (1) What was supposed to happen? (2) What actually happened? (3) Why was there a difference? (4) What can we do better next time? Conducted immediately after action; ranks check rank at the door (the lowest rank can critique the highest); focuses on improvement, not blame. Adopted widely in business and emergency services as the gold-standard learning protocol.'
Needs_Processing: false
AI_Instructions: ''

---

# After Action Review

**One-line summary:** A structured post-action learning protocol — developed by the U.S. Army — that uses four questions (planned vs. actual, why the difference, what to improve) immediately after an action, with rank checked at the door, to extract reusable lessons rather than assign blame.

**When to reach for it:** After military operations (origin); after sprints, releases, incidents, projects in any organization; after sales calls, customer escalations, court cases, surgical procedures, training exercises; and any context where structured learning from completed action is more valuable than scattered post-hoc commentary or blame-focused incident review.

---

## Purpose Of This Thinking Tool

**After Action Review (AAR)** structures team learning after completed action. The four questions:

1. **What was supposed to happen?** What was the plan, the intent, the expected outcome?
2. **What actually happened?** A factual reconstruction, not interpretation.
3. **Why was there a difference?** Causes — system, environment, decisions, execution.
4. **What can we do differently / better next time?** Specific changes for future actions.

The non-obvious operational insight is that **the structure separates fact from interpretation from action.** Most casual post-action discussion mixes these — "what happened" is told as already-interpreted narrative; "why" gets confused with blame; "what to do" gets shaped by political concerns. The four-question structure forces clean separation, producing usable lessons.

The Army's specific disciplines that elevate AAR above ordinary debriefs:

1. **Conducted immediately** — within hours of action, while memories are fresh and accurate.
2. **Rank check at the door** — within the AAR, the lowest rank can critique the highest. Hierarchy resumes after.
3. **Focus on improvement, not blame** — the question is "what can we learn?" not "who screwed up?"
4. **Specific and concrete** — vague "communication was bad" → specific "the radio relay missed checkpoint Charlie at 14:30; cause was frequency confusion; fix is pre-mission frequency drill."
5. **Documented and shared** — lessons enter institutional memory, not individual recall.

A second insight: **the discipline transfers across high-stakes domains.** Military, surgical teams, aviation incident review, sports, emergency services, software incident response — all contexts where the cost of repeating mistakes is high enough to justify the protocol.

A third insight: **AAR is a forcing function for psychological safety.** "Rank check at the door" is institutionally hard; organizations that successfully run AARs have built the cultural permission for honest junior critique of senior decisions. Where this culture doesn't exist, AAR becomes ceremony.

A fourth insight: **the lessons are commodity; the application is the value.** Organizations regularly conduct AARs and document lessons; far fewer reliably apply those lessons to subsequent actions. The application loop — lessons inform planning of the next operation — is what actually generates improvement.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "casual debrief" failure.** Unstructured post-action discussion that fails to extract specific lessons.
2. **The blame-focused incident review.** Asking "who's responsible" produces defensiveness and missing root causes.
3. **The lessons-without-application loop.** Documenting lessons that are never applied to future operations.

For military leaders, surgical teams, software incident responders, sales teams, project managers, and any team whose performance depends on learning from each action, AAR is foundational discipline.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Schedule the AAR immediately after the action — within hours if possible.       |
|    2 | Convene the team that performed the action plus directly relevant observers.    |
|    3 | Set ground rules: rank check at the door; focus on improvement; specific not  |
|      | vague; no blame.                                                                  |
|    4 | Q1: What was supposed to happen? Reconstruct the plan / intent / expected        |
|      | outcome.                                                                          |
|    5 | Q2: What actually happened? Factual reconstruction — what events occurred.    |
|    6 | Q3: Why was there a difference? Causes — environmental, system, decision,      |
|      | execution. Multiple causes typically.                                            |
|    7 | Q4: What do we do differently next time? Specific, actionable lessons.         |
|    8 | Document. Capture lessons in a form that informs future planning.              |
|    9 | Apply. Inject lessons into the next operation's planning. Without application, |
|      | AAR is ceremony.                                                                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FOUR QUESTIONS

   1. WHAT WAS SUPPOSED TO HAPPEN?
      The plan, intent, expected outcome.
      Establishes the standard against which actual is
      measured.

   2. WHAT ACTUALLY HAPPENED?
      Factual reconstruction.
      "At 14:30 we engaged Target X. At 14:32 we
      took fire from sector Y, unanticipated. At 14:35
      we repositioned..."
      Not interpretation; events.

   3. WHY WAS THERE A DIFFERENCE?
      Causes:
          Environmental (changed conditions)
          System (process / tooling / structure)
          Decision (choice points, info available)
          Execution (skill, coordination)
      Often multiple causes interact.

   4. WHAT DO WE DO DIFFERENTLY NEXT TIME?
      Specific, actionable lessons:
          "Before similar ops, conduct frequency drill"
          "Standing comms check every 15 min in similar
          terrain"
          "Brief weather forecast at H-1 hour"
      Vague lessons ("communicate better") don't drive
      change.

THE GROUND RULES (institutional)

   1. RANK CHECK AT THE DOOR
      Within the AAR, junior can critique senior.
      Outside, rank resumes. The institution must
      genuinely back this up; one violation kills it.

   2. NO BLAME
      The question is "what can we learn?" not "who
      screwed up?" Personal accountability is
      separate (HR, command); AAR is for system
      learning.

   3. SPECIFIC AND CONCRETE
      "Communications were bad" → "Radio relay
      missed checkpoint Charlie at 14:30."
      The specific lesson is the actionable one.

   4. EVERY VOICE
      Lowest rank speaks first or is explicitly
      invited; their perspective often contains
      details senior view misses.

   5. TIMELY
      Within hours. Memory degrades fast; rationalization
      builds.

   6. DOCUMENTED
      Lessons captured, indexed, accessible.
      Institutional memory > individual recall.

THE WORKED EXAMPLE — SOFTWARE INCIDENT

   Action: production outage from 14:15 to 17:30.

   Q1 What was supposed to happen?
       Routine database migration during off-peak
       hours; <5 min downtime expected.

   Q2 What actually happened?
       14:15 — migration started
       14:17 — primary DB failover triggered (planned)
       14:18 — replica DB failed to take over (unplanned)
       14:25 — outage detected
       14:30 — incident declared
       15:00 — replica restored from backup
       15:30 — discovered backup was 4 hours old
       17:00 — primary recovered
       17:30 — full service restored
       Total: 3h15m outage; 4 hours data lost

   Q3 Why the difference?
       Environmental: replica had been failing
       silently for 6 hours pre-migration (unmonitored)
       System: backup-staleness alerts disabled in
       last sprint
       Decision: migration started despite warning
       sign in monitoring (one team member noticed,
       didn't escalate)
       Execution: incident response runbook hadn't
       been drilled in 6 months; team improvised

   Q4 What do we do differently?
       1. Pre-migration health-check covering replica
          state (specific checklist before starting)
       2. Re-enable backup-staleness alerts; alert on
          >1h
       3. "Anyone can call abort" rule — explicit
          permission to escalate / halt
       4. Quarterly incident-response drill
       5. Post-incident communication template
          (customer notification was delayed 45 min)

   Each lesson is specific, owned, deadlined.

THE LESSON-APPLICATION LOOP

   AAR's value comes from feeding lessons forward:

   Lessons documented after Action N
       ↓
   Reviewed during planning for Action N+1
       ↓
   Lessons applied; new approaches tested
       ↓
   AAR after Action N+1 covers: did the lessons help?

   Without the loop, lessons accumulate without
   producing change. Many organizations document
   lessons that nobody reads.

   Discipline:
       Pre-action checklist explicitly references
       relevant prior AAR lessons
       Periodic review of accumulated lessons for
       patterns
       Recurrent lessons (same issue across multiple
       actions) get systemic attention

THE COMMON FAILURE MODES

   1. SKIPPING IMMEDIACY
        Conducted weeks later; memories decayed.
        Recovery: schedule within hours / day.

   2. BLAME-FOCUS
        "Who screwed up?" Recovery: institutional
        rule; senior modeling.

   3. VAGUE LESSONS
        "Communicate better" types. Recovery: insist
        on specificity.

   4. RANK PRESSURE
        Junior won't critique senior. Recovery: rank-
        check rule; senior models accepting critique.

   5. DOCUMENTED-NEVER-APPLIED
        Lessons captured; never fed forward. Recovery:
        explicit pre-action review of relevant prior
        lessons.

   6. PERFORMATIVE AAR
        Going through motions; nobody really learning.
        Recovery: leadership models genuine engagement.

   7. SCOPE-CREEP TO FULL POST-MORTEM
        AAR drifts into broader root-cause analysis.
        Recovery: AAR is for action-level learning;
        deeper analysis is separate.

THE OPERATIONAL TEMPLATE

   Action: ____________________________________________
   Date / time: _______________________________________
   AAR conducted at: __________________________________

   Participants: ______________________________________
   Ground rules acknowledged: Y / N

   Q1 Plan / intent: __________________________________
   _____________________________________________________

   Q2 Actual events:
       Time _____ : __________________________________
       Time _____ : __________________________________
       Time _____ : __________________________________

   Q3 Causes of difference:
       Environmental: ________________________________
       System: ______________________________________
       Decision: ____________________________________
       Execution: ___________________________________

   Q4 Lessons / actions for next time:
       1. Specific action: __________ Owner: ____ Due: ____
       2. Specific action: __________ Owner: ____ Due: ____
       3. Specific action: __________ Owner: ____ Due: ____

   Lessons documented in: _____________________________
   Application: incorporated in next planning cycle? Y/N
```

> **Operational notes:** Four disciplines. (1) Run immediately. Memory degrades within days; rationalization builds. AAR within hours captures what days-later AAR misses. (2) Rank check at the door is institutional, not just procedural. The senior leader's first response to junior critique sets the tone. If the senior defends, future AARs are dead. If the senior accepts and acts, the practice strengthens. (3) Lessons must be specific. "Communicate better" is uselessly vague; "Pre-mission frequency drill" is actionable. The discipline of forcing specificity is where the value lives. (4) Application closes the loop. Lessons that don't feed forward into next planning are documentation theater. The institutional discipline of "review prior AAR lessons during pre-action planning" is the test of whether AAR is actually working.
