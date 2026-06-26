---
Item_ID: tt-poker-decision-review
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Poker Decision Review
tt_Source: Professional poker tradition (Doyle Brunson, Phil Galfond, Annie Duke); modern post-session review with hand histories. Adopted in business decision-quality contexts via Annie Duke's Thinking in Bets and the broader decision-science community.
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision analysis
tt_Operation: Run experimental cycle
tt_Cross_Domains: []
tt_Form:
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
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows:
- Thinking in Bets
tt_Pairs_Well_With:
- Thinking in Bets
- Brier Scoring
- After Action Review
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Post-session decision review modeled on poker hand-history analysis. For each significant decision, reconstruct: what info was available; what alternatives existed; what was decided; what was the decision-quality (vs. outcome). Identify mistakes (decisions wrong given info) separately from misfortunes (decisions right; outcomes wrong). Builds calibration over time. Used in poker, investing, software incident response, project management.'
Needs_Processing: false
AI_Instructions: ''
---

# Poker Decision Review

**One-line summary:** A post-session decision-analysis discipline — drawn from professional poker — in which significant decisions are systematically reconstructed (information available, alternatives, choice made, decision quality vs. outcome) to build calibration and identify mistakes separately from misfortunes.

**When to reach for it:** After any session of repeated decision-making (sales calls, hiring rounds, investments, sprints); incident retrospectives where decisions under uncertainty matter; coaching individuals on decision-making improvement; building team decision-calibration; and any context where the volume of decisions justifies systematic post-hoc review for learning.

---

## Purpose Of This Thinking Tool

**Poker decision review** is the practice of post-session analysis of significant decisions. The structure:

1. **Identify significant decisions** from the session. Not every decision warrants review; the consequential ones do.
2. **Reconstruct each:**
   - What information was available at the time?
   - What alternatives existed?
   - Which was chosen?
   - What was the reasoning?
3. **Evaluate decision quality (independent of outcome):** given the information, was the choice correct?
4. **Note the outcome separately.** Did it work?
5. **Categorize:**
   - Good decision + good outcome (skill)
   - Good decision + bad outcome (misfortune)
   - Bad decision + good outcome (luck)
   - Bad decision + bad outcome (mistake)
6. **Extract lessons.** What patterns emerge? Where am I miscalibrated?

The non-obvious operational insight is that **systematic review separates noise from signal in decision performance.** A single decision's outcome is mostly noise (luck-dominated in domains like poker, investing, sales). A pattern across many decisions reveals signal — calibration, recurring mistakes, blind spots.

A second insight: **the practice cures resulting at scale.** Reviewing decisions only when they go wrong reinforces resulting; reviewing decisions systematically (regardless of outcome) trains the mind to evaluate decision quality independently. Over time, decision-makers stop conflating outcome with quality.

A third insight: **the framework requires written decisions.** "What did I decide?" is unreliable from memory weeks later — outcomes color recall. Recording decisions with reasoning at the time of decision is the precondition for honest review.

A fourth insight: **the practice is uncomfortable but durable.** Reviewing your own decisions exposes mistakes that ego prefers to forget. The discipline pays off cumulatively; one session's review is mildly useful, ongoing practice over years is transformative.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "winner's overconfidence" trap.** Successful sessions feel like skill; without review, lucky decisions get treated as good ones.
2. **The "loser's despair" trap.** Bad sessions feel like incompetence; without review, well-made decisions that didn't work get labeled mistakes.
3. **The "no improvement" pattern.** Decision-makers who don't review systematically don't improve systematically; they accumulate experience without learning from it.

For poker players (origin), investors, sales professionals, founders, software engineers (incident review), surgeons, and anyone whose work is decision-rich and outcome-noisy, systematic review is the path to calibration.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |=================================================================================|
|    1 | Identify the session / period to review (a day, a week, a project phase).      |
|    2 | List significant decisions made. Don't review every decision; pick the         |
|      | consequential ones.                                                               |
|    3 | For each, reconstruct: information available, alternatives, choice, reasoning.|
|      | Use written records where possible.                                              |
|    4 | Evaluate decision quality independent of outcome. Was it the right call?       |
|    5 | Note the outcome. Categorize using the 2x2 (skill / misfortune / luck /        |
|      | mistake).                                                                         |
|    6 | Identify patterns across decisions. Recurring mistakes? Calibration drift?     |
|    7 | Extract specific lessons for future similar decisions.                          |
|    8 | Build the practice into routine. Weekly / monthly / per-project review.        |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE REVIEW PROTOCOL

   1. SCOPE
      Identify the session / period.

   2. SELECT
      Identify significant decisions (5-15 typical for
      a session).

   3. RECONSTRUCT (per decision)
      Information available at the time:
          What did I know?
          What did I not know?
          What was my read on the situation?

      Alternatives:
          What were my realistic options?
          What did I consider; what did I not?

      Choice:
          What did I do?

      Reasoning:
          Why? (At the time, not in hindsight.)

   4. EVALUATE DECISION QUALITY
      Given the information at the time:
          Was the choice optimal?
          Was it good but not optimal?
          Was it actively bad?

      Use poker-equity / EV thinking:
          What was the expected value of each option?
          Was my choice the highest-EV?

   5. NOTE OUTCOME (separately)
      What happened?
      Was it the expected probability outcome or
      surprise?

   6. CATEGORIZE
      Decision   Outcome     Category
      ---------  ---------   ------------------
      Good       Good        Skill / expected
      Good       Bad         Misfortune
      Bad        Good        Lucky escape
      Bad        Bad         Mistake

   7. EXTRACT
      Per decision: lesson learned?
      Across decisions: pattern?

   8. CALIBRATE
      Are my probability estimates aligned with
      outcomes over many decisions?

THE WORKED EXAMPLE — POKER (THE SOURCE DOMAIN)

   Decision: facing a bet on the river with bottom pair.

   Reconstruct:
       Info available: opponent's range, betting story,
       my hand strength, pot odds.
       Alternatives: fold, call, raise.
       Chose: call.
       Reasoning: pot odds say I need 35% equity to
       call profitably; my read on opponent's range
       gives me 40%.

   Evaluate decision quality:
       Was 40% equity estimate right?
       Was call the highest-EV option?

   Outcome: opponent had top pair; I lost the call.

   Category: Good decision + bad outcome (misfortune).
   Resulting would say "bad call." Quality review says
   "right call given equity; outcome variance."

   Lesson: my equity estimate was correct; the random
   distribution gave the rare outcome. Don't change
   the decision rule.

   If equity estimate was wrong (e.g., opponent's
   range narrower than thought, true equity was 25%):
   Bad decision + bad outcome = mistake. Lesson:
   recalibrate range reads.

THE WORKED EXAMPLE — BUSINESS

   Decision: hire candidate X for senior engineering
   role.

   Reconstruct:
       Info available: 5 interviews, references, work
       sample, team feedback. Strong on technical;
       moderate on collaboration. References mixed.
       Alternatives: hire X, hire candidate Y (less
       experienced), continue searching.
       Chose: hire X.
       Reasoning: senior engineering need is acute;
       collaboration concerns can be coached;
       references explainable by prior toxic
       environment.

   Evaluate decision quality:
       Were the references' concerns addressable?
       Was urgency real or manufactured?
       Was Y a viable alternative?

   Outcome (6 months later): X is high-performing
   technically; collaboration issues persist;
   eventually departs.

   Category: depends on assessment.
       If collaboration concerns were knowable and
       coachability over-rated: bad decision + bad
       outcome = mistake. Lesson: weight
       collaboration concerns more.
       If concerns were genuinely addressable and X
       hit unforeseen circumstances: good decision +
       bad outcome = misfortune.

   Honest review distinguishes; rationalization
   conflates.

THE WRITTEN-DECISION DISCIPLINE

   For review to work, decisions must be written at
   the time:

   DECISION JOURNAL ENTRY:
       Decision: ____________________
       Information available: _______
       Alternatives considered: _____
       Choice: ______________________
       Reasoning: ___________________
       Probability of success: ___%
       What I'd update on: __________

   Without this, memory shapes recall around outcomes.
   With it, review has honest source material.

THE CALIBRATION ARC

   Across many decisions over time:

       Decisions made: 100
       At "70% confident": 70% materialized → calibrated
       At "70% confident": 90% materialized → underconfident
       At "70% confident": 50% materialized → overconfident

   The patterns reveal:
       Probability calibration (am I generally
       overconfident, underconfident, or aligned?)
       Domain-specific calibration (overconfident on
       technical, underconfident on people?)
       Recurring blind spots

   Calibration improvement is the long-game payoff
   of the practice.

THE COMMON FAILURE MODES

   1. NO WRITTEN DECISIONS
        Memory-based review distorts. Recovery:
        decision journal.

   2. RESULTING-LITE
        Reviewing only "bad outcomes" not "good
        decisions / bad outcomes." Recovery: review all
        significant decisions.

   3. RATIONALIZATION
        Reconstructing reasoning to justify outcomes.
        Recovery: written-at-the-time discipline;
        ego-deflation practices.

   4. NO PATTERN RECOGNITION
        Reviewing single decisions; missing recurring
        patterns. Recovery: periodic synthesis across
        many reviews.

   5. PRACTICE COLLAPSE
        Starts strong, fades over time. Recovery:
        institutional cadence; partner / community.

   6. PERFORMATIVE REVIEW
        Going through motions; not honest. Recovery:
        ego-honest practice; sometimes a coach helps.

   7. NO ACTIONABLE LESSONS
        Insight without action. Recovery: explicit
        commitments to change behavior on similar
        future decisions.

THE OPERATIONAL TEMPLATE

   Session / period: __________________________________

   Significant decisions identified (5-15): ___________

   Per decision review:

       Decision 1: ___________________________________
           Info at time: _____________________________
           Alternatives: _____________________________
           Choice: ___________________________________
           Reasoning: ________________________________
           Decision quality: good / okay / bad
           Outcome: __________________________________
           Category: skill / misfortune / luck / mistake
           Lesson: ___________________________________

       Decision 2: [same structure]
       ...

   Patterns across decisions:
       Recurring mistake: ____________________________
       Calibration drift: ____________________________
       Blind spot: ___________________________________

   Specific commitments for future:
       Will do differently: ___________________________
       Will continue: _________________________________
```

> **Operational notes:** Four disciplines. (1) Separate decision quality from outcome quality religiously. The single most important move. The 2x2 (skill / misfortune / luck / mistake) is the lens. (2) Document decisions at the time. Memory-based review collapses to outcome-influenced rationalization. Decision journals (written reasoning, probability, alternatives) make honest review possible. (3) Review systematically, not just after losses. Reviewing only bad outcomes reinforces resulting; systematic review (every significant decision regardless of outcome) trains decision-quality assessment. (4) Look for patterns. Single-decision lessons are limited; patterns across many decisions reveal calibration drift, recurring blind spots, domain-specific overconfidence. The cumulative practice over years is what produces measurable improvement.
