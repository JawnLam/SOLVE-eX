---
Item_ID: tt-one-way-two-way-doors
Item_Prototype: Thinking_Tool
Title: One-Way / Two-Way Doors (Bezos Memo)
tt_Source: Jeff Bezos, Amazon shareholder letter (2015), articulating Amazon's decision-making philosophy. Reinforced in subsequent letters and Bezos's leadership principles. Widely adopted in technology-company decision frameworks.
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision analysis
tt_Operation: Categorize situation type
tt_Cross_Domains: []
tt_Form:
- Mental model
- Sequenced workflow
tt_Scale:
- Solo
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
- Decision / choice
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Real Options Analysis
- Pre-Mortem
- Cynefin
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Bezos: ''Some decisions are consequential and irreversible — one-way doors. Others are changeable, reversible — two-way doors.'' Two-way doors should be made fast, by individuals or small teams; one-way doors deserve careful, slow analysis with senior input. Common failure: applying heavyweight one-way-door processes to two-way-door decisions, slowing the org. The diagnostic question — ''is this reversible?'' — is the move.'
Needs_Processing: false
AI_Instructions: ''
---

# One-Way / Two-Way Doors (Bezos Memo)

**One-line summary:** Jeff Bezos's decision-classification framework: distinguish between one-way doors (consequential, irreversible — deserve slow, careful analysis) and two-way doors (changeable, reversible — should be made fast by individuals / small teams), then match decision process to door type.

**When to reach for it:** Any meaningful decision in an organization; before convening committees or running long approval processes; coaching teams that over-analyze reversible decisions or under-analyze irreversible ones; designing decision-making protocols at scale; and any context where the cost of slow decision-making is real but the cost of irreversible mistakes is also real.

---

## Purpose Of This Thinking Tool

**One-Way / Two-Way Doors** classifies decisions by reversibility:

1. **One-Way Door** — consequential, hard to reverse. Walking through commits you. Examples: large acquisitions, major hires, public commitments, exiting a market, releasing a product brand.
2. **Two-Way Door** — changeable, easy to reverse. Walking through can be undone. Examples: pricing experiments, feature releases (in agile context), tactical moves, hiring entry-level positions, internal process changes.

Different doors warrant different decision processes:

- **One-way doors:** slow, careful analysis; senior involvement; multiple perspectives; pre-mortem; documented reasoning.
- **Two-way doors:** fast, individual or small-team decisions; bias toward action; experiment-and-learn.

The non-obvious operational insight is that **applying one-way-door process to two-way-door decisions is the dominant organizational failure mode at scale.** As organizations grow, they tend to apply heavyweight processes (committees, multiple approvals, exhaustive analysis) to all decisions for consistency. The result: two-way-door decisions take weeks; the cumulative slowdown drains organizational velocity. Bezos's insight: the door type should determine the process, not the org chart.

A second insight: **reversibility isn't always obvious.** Some decisions look one-way but are actually two-way (most pricing changes, most product features, most hiring). Some look two-way but are actually one-way (firing a senior person, public statements that get archived, partnerships with exclusive clauses). The diagnostic question — "if this fails, can we undo it within reasonable cost?" — is the discipline.

A third insight: **even one-way doors benefit from speed when reversibility is partial.** Bezos's expanded principle: "Most decisions should probably be made with somewhere around 70% of the information you wish you had. If you wait for 90%, in most cases, you're probably being slow." For two-way doors, even less information is fine; for one-way doors, 70% is often appropriate; only the truly irreversible warrant 90%+.

A fourth insight: **the framework empowers delegation.** When a leader explicitly classifies a decision as two-way, juniors are empowered to decide and act. When classified one-way, escalation is appropriate. The labeling system creates organizational clarity about who decides what.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "everything goes to committee" trap.** Heavyweight process applied to two-way doors slows the org without proportionate benefit.
2. **The "fast on irreversible" failure.** Applying lightweight process to one-way doors produces avoidable disasters.
3. **The "founder bottleneck" pattern.** Leaders making all decisions because the team can't distinguish what's safe to delegate. Door classification enables delegation.

For executives, founders, organizational designers, and anyone responsible for decision-making at scale, door classification is foundational discipline.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the decision under consideration.                                       |
|    2 | Ask: if this fails, can we reverse it? At what cost? In what timeframe?         |
|    3 | Classify: one-way (irreversible / very costly to reverse) or two-way (reversible|
|      | at reasonable cost)?                                                              |
|    4 | If two-way: decide quickly. Individual or small team. ~50-70% information.     |
|      | Bias toward action. Plan to monitor and reverse if needed.                       |
|    5 | If one-way: slow down. Senior involvement. Multiple perspectives. Pre-mortem.  |
|      | ~70-90% information. Documented reasoning.                                       |
|    6 | When uncertain, default to "treat as one-way unless proven otherwise" for high|
|      | stakes; default to "treat as two-way" for low stakes.                            |
|    7 | Communicate the classification. The team should know which door this is.       |
|    8 | After the decision, retrospectively check: was the door classified correctly?|
|      | What did we learn?                                                                |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE TWO DOOR TYPES

   ONE-WAY DOOR:
       Walk through; can't easily come back.
       Costly or impossible to reverse.
       Examples:
           Major acquisitions ($M to $B)
           Senior executive hires
           Exiting a market segment
           Public statements / commitments
           Brand re-positioning
           Spinning off a business unit

   TWO-WAY DOOR:
       Walk through; can come back if needed.
       Reversible at reasonable cost.
       Examples:
           Pricing experiments
           Feature releases (especially with feature
           flags)
           Tactical campaign launches
           Junior hiring
           Internal process changes
           Pilot programs

THE PROCESS-MATCHING FRAMEWORK

   ONE-WAY DOOR PROCESS:
       Multiple perspectives sought
       Pre-mortem conducted
       70-90% information gathered
       Senior decision-maker
       Multiple approvals
       Documented reasoning
       Slower (days to weeks)

   TWO-WAY DOOR PROCESS:
       Individual or small team
       50-70% information sufficient
       Junior empowered
       Decision documented but not extensively
       Faster (minutes to days)
       Plan for monitoring and reversal

THE REVERSIBILITY DIAGNOSTIC

   Ask:
       1. If this fails, can we undo it?
       2. What's the cost of undoing?
       3. What's the time to undo?
       4. Are there irreversible side effects (legal,
       reputation, hires, etc.)?

   Door types by reversibility cost:

       Very low cost (<5% of decision value): two-way
       Moderate cost (5-50%): treat as two-way for
       small stakes; analyze for big stakes
       High cost (>50%): one-way
       Truly irreversible: one-way; maximum care

THE WORKED EXAMPLES

   ACQUISITION OF SUBSIDIARY ($100M):
       Reversal cost: divestiture is possible but
       lengthy and money-losing
       Door type: one-way
       Process: extensive diligence; multiple advisors;
       board approval; pre-mortem

   NEW PRICING TIER:
       Reversal cost: change pricing back; some
       customer confusion but recoverable
       Door type: two-way
       Process: PM decides; A/B test; monitor; revert
       if metrics decline

   PUBLIC LAUNCH OF NEW BRAND:
       Reversal cost: brand confusion, media coverage,
       wasted spend; very hard to walk back
       Door type: one-way
       Process: thorough validation; senior alignment;
       launch contingency plan

   FEATURE FLAG ROLLOUT:
       Reversal cost: turn off the flag
       Door type: two-way
       Process: engineer ships; monitor; turn off if
       issues

   HIRING SENIOR EXECUTIVE:
       Reversal cost: high (severance, organizational
       disruption, search costs)
       Door type: one-way
       Process: multiple interviewers; references;
       executive search standards

   HIRING JUNIOR:
       Reversal cost: moderate (probationary period
       limits exposure)
       Door type: two-way (within probation)
       Process: hiring manager + 2-3 interviewers;
       structured but not exhaustive

THE BEZOS-INFORMATION-PRINCIPLE

   Bezos: "Most decisions should probably be made with
   somewhere around 70% of the information you wish
   you had. If you wait for 90%, in most cases, you're
   probably being slow."

   Combined with door framework:
       Two-way: 50-70% info OK
       One-way: 70-90% info preferred
       Irreversible-with-large-stakes: 80-90% info

   The cost of slow decisions is real even on
   one-way doors; care has limits.

THE ESCALATION DISCIPLINE

   Junior empowerment is enabled by door classification:

   "This is a two-way door. You don't need approval.
   Decide; document; monitor; reverse if needed."

   "This is a one-way door. Bring it to me / the
   committee."

   Without classification, juniors either over-escalate
   (slowing everything) or under-escalate (causing
   irreversible mistakes).

   The framework gives juniors clear guidance and gives
   seniors clear scope.

THE COMMON FAILURE MODES

   1. ALL-COMMITTEE DEFAULT
        Treating everything as one-way. Recovery:
        explicit classification; default to two-way
        for routine decisions.

   2. ALL-FAST DEFAULT
        Treating everything as two-way. Recovery:
        identify truly irreversible decisions; slow
        them down.

   3. WRONG CLASSIFICATION
        Calling something two-way that's actually
        one-way (e.g., a "small" public statement
        that gets archived forever). Recovery:
        rigorous reversibility check.

   4. PROCESS WITHOUT EMPOWERMENT
        Classifying decisions but not changing
        practice. Recovery: explicit empowerment of
        juniors for two-way doors.

   5. ALWAYS-90%-INFO PERFECTIONISM
        Waiting for full information even on two-way
        doors. Recovery: 70% rule.

   6. NO RETROSPECTIVE
        Door classification not validated against
        outcomes. Recovery: periodic check on what
        actually was reversible.

   7. TIMING SHIFTS
        Decision two-way at one timeframe, one-way at
        another (e.g., feature flags can be toggled
        for first month, but customer dependence
        builds). Recovery: classify with timeframe
        in mind.

THE OPERATIONAL TEMPLATE

   Decision under consideration: ______________________

   Reversibility check:
       If this fails, can we reverse? Y / N
       Cost of reversal: __________________________
       Time to reverse: ___________________________
       Irreversible side effects: _________________

   Classification: One-way / Two-way

   Process matched:
       Decision-maker: _____________________________
       Information threshold: _____________________
       Pre-mortem? Y / N
       Approvals required: ________________________
       Timeline: __________________________________

   Communication: team knows which door this is? Y / N

   After decision: retrospective on classification?
   Y / N
```

> **Operational notes:** Four disciplines. (1) Classify before deciding. The classification itself is the move. Without it, organizations drift toward over-process or under-process; with it, both excesses are corrected. (2) Match process to door. Heavyweight process for one-way; lightweight for two-way. The cost of slow decisions on two-way doors is real and cumulative; the cost of fast decisions on one-way doors is occasional but severe. Both deserve attention. (3) Empower delegation. The framework's organizational value is enabling junior decisions on two-way doors. Senior leaders should explicitly say "this is two-way, you decide" — and mean it. (4) Validate retrospectively. Door classifications can be wrong; periodic checks of what was actually reversible improve future classifications. Build the calibration loop.
