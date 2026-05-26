---
Item_ID: tt-pre-mortem
Item_Prototype: Thinking_Tool
Title: Pre-Mortem
tt_Source: 'Gary Klein, ''Performing a Project Premortem'' (Harvard Business Review, 2007); developed from naturalistic decision-making research. Related: Daniel Kahneman''s recommendation in Thinking, Fast and Slow.'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Adversarial / debiasing reasoning
tt_Operation: Stress-test a position
tt_Cross_Domains:
- Modes of inquiry
- Inner / psychological work
tt_Form:
- Sequenced workflow
tt_Scale:
- Small group
tt_Duration:
- Single session
- Workshop
tt_Lineage:
- Western analytic / academic
tt_Posture:
- Beginner-friendly
tt_State:
- Heightened-vigilant
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
- Risk / uncertainty
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Red Teaming
- Inversion
- Cognitive Bias Checklists
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=['Heightened-vigilant'], tt_Agent=['Solo human'], tt_About=['Mind / cognition', 'Risk / uncertainty']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: Before launching a project, imagine it has already failed catastrophically. Each team member writes a brief explaining why. The 'prospective hindsight' frame surfaces concerns that current optimism / groupthink suppresses. Klein found prospective hindsight increases the ability to identify causes of future outcomes by 30%. Used in product launches, M&A, strategic initiatives, and any high-stakes decision before commitment.
Needs_Processing: false
AI_Instructions: ''
---

# Pre-Mortem

**One-line summary:** A debiasing technique — Gary Klein's — that asks the team, before launching a project, to imagine it has already failed catastrophically and to write down why; the "prospective hindsight" frame surfaces concerns that current optimism and groupthink suppress.

**When to reach for it:** Before launching any high-stakes initiative (product launch, acquisition, strategic pivot, major hire); during deal due diligence; in agile retrospectives flipped forward; in personal decisions of significant scale; and any context where the cost of unexamined risk is high and the team is currently optimistic.

---

## Purpose Of This Thinking Tool

**Pre-mortem** is a structured exercise to surface risks before commitment. The procedure:

1. **Set the scene.** "Imagine we are 6 months / 1 year / 2 years from now, and the project has failed catastrophically. It's a disaster. We are looking back trying to understand why."
2. **Each team member writes (alone, 5-10 minutes) the story of the failure.** What happened? What were the causes?
3. **Share and aggregate.** Collect everyone's stories.
4. **Identify common themes.** Which failure modes appear across multiple write-ups?
5. **Prioritize and address.** Which can be mitigated now? Which require monitoring? Which kill the project?

The non-obvious operational insight is that **prospective hindsight is psychologically different from prospective analysis.** Asking "what could go wrong?" in present tense triggers either reassurance ("we've thought about that") or vague worry. Asking "imagine it failed; why?" in past tense gives people psychological permission to identify causes. Klein's research found 30% improvement in identifying causes of outcomes when using prospective hindsight vs. forward-looking prediction.

A second insight: **the technique counteracts the optimism that group commitment generates.** Once a team commits to a project, social pressure rewards optimism and punishes "negative" voices. Pre-mortem makes voicing concern the explicit task — what would otherwise be politically costly becomes the assignment.

A third insight: **the individual-write-then-share structure prevents groupthink.** Open brainstorming is dominated by the first speakers; private writing surfaces independent assessments. The aggregation reveals patterns no individual would have produced.

A fourth insight: **the technique works because it gives permission.** Many team members have private concerns they don't voice. Pre-mortem is the safe context to articulate them. Sometimes the most valuable concerns come from the most junior team members who would otherwise stay silent.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "everything's fine" optimism trap.** Committed teams underestimate risks. Pre-mortem counteracts.
2. **The groupthink silence.** Concerned voices stay quiet to avoid being "negative." Pre-mortem makes voicing the assignment.
3. **The unstructured worry list.** Asking "what could go wrong?" produces vague worries; asking "why did it fail?" produces specific failure narratives.

For project leaders, executives, founders, and anyone making high-stakes commitments, pre-mortem is essential debiasing technique.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Schedule the pre-mortem before commitment to the project, not after. Once       |
|      | committed, the exercise is much harder to run honestly.                          |
|    2 | Set the scene precisely. Time horizon (6 months? 2 years?). Failure scope       |
|      | (catastrophic, embarrassing, slow decline).                                      |
|    3 | Have each team member write privately (5-10 minutes). Why did the project      |
|      | fail? What went wrong?                                                           |
|    4 | Collect the write-ups. Share without attribution.                                |
|    5 | Cluster failure modes. Which appear across multiple write-ups?                  |
|    6 | Assess each cluster: probability, impact, mitigability.                         |
|    7 | Decide: which to mitigate before launching? Which to monitor? Which are        |
|      | unmitigable but acceptable? Which are deal-breakers?                             |
|    8 | Document the surfaced risks and mitigation plan; revisit periodically as the   |
|      | project unfolds.                                                                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE PRE-MORTEM PROTOCOL

   1. SCENE-SETTING (2 min)
      Facilitator: "It is now [DATE — 6 months out].
      The [project] has failed. It's a complete disaster.
      Customers are angry, executives are demanding
      answers, the team is demoralized. We're meeting
      now to understand: what went wrong?"

   2. SILENT WRITING (5-10 min)
      Each participant writes the story of the failure.
      What happened? What caused it? What did we miss?
      No discussion yet.

   3. ROUND-ROBIN SHARING (15-20 min)
      Each person reads (or hands in) their failure
      narrative. No critique, no defense — just listen.

   4. CLUSTERING (10-15 min)
      Group identifies common themes. Often 3-5
      clusters emerge.

   5. ASSESSMENT (15-20 min)
      For each cluster:
          Probability: how likely is this failure mode?
          Impact: how bad if it happens?
          Mitigability: what could we do now?

   6. DECISION (10 min)
      Mitigate: assign owners, deadlines
      Monitor: define triggers for action
      Accept: acknowledge the risk
      Deal-breaker: re-examine commitment

THE WHY-IT-WORKS PRINCIPLES

   PROSPECTIVE HINDSIGHT:
       Past-tense framing ("why did it fail?") activates
       different cognition than future-tense ("what
       could go wrong?"). Easier to specify causes than
       worries.

   COMMITMENT REVERSAL:
       Once a team is committed, optimism is socially
       rewarded. Pre-mortem temporarily reverses
       this, making concern the assignment.

   PRIVATE-FIRST:
       Writing alone before sharing avoids first-speaker
       dominance and groupthink. Junior or contrarian
       voices get airspace.

   AGGREGATION:
       Patterns emerging across multiple
       independently-generated narratives are more
       reliable than any individual's prediction.

THE WORKED EXAMPLE — PRODUCT LAUNCH PRE-MORTEM

   Setup: "Six months from now, our product launch
   has failed badly. Sales are 20% of plan, customer
   reviews are negative, the team is demoralized."

   Common themes across 8 team-member write-ups:

   CLUSTER 1: Wrong customer
       3 people: "We targeted enterprise but the
       product is mid-market"
       Mitigation: validate ICP with 5 customer
       interviews before launch

   CLUSTER 2: Insufficient differentiation
       4 people: "Once Competitor X launched their
       similar feature, our differentiation collapsed"
       Mitigation: deepen one feature; cut others

   CLUSTER 3: Channel mismatch
       2 people: "Our channel can't sell this product"
       Mitigation: develop direct-sales path; 30-day
       trial

   CLUSTER 4: Under-resourced support
       3 people: "Customer support overwhelmed; bad
       reviews snowballed"
       Mitigation: pre-fund support; escalation
       playbook

   The surfaced risks and mitigations are visible
   before launch — and frequently they materially
   shift the launch plan.

THE COMMON FAILURE MODES

   1. RUNNING POST-COMMITMENT
        After the team has committed, honesty is
        harder. Recovery: schedule pre-mortems before
        big decisions, not as ceremony after.

   2. PUBLIC BRAINSTORM INSTEAD OF PRIVATE WRITE
        Open discussion gets dominated by first
        speakers. Recovery: enforce silent writing
        first.

   3. NO AGGREGATION
        Stories shared but never clustered. Recovery:
        explicit clustering step.

   4. THEATER WITHOUT ACTION
        Pre-mortem run; risks identified; nothing
        changes. Recovery: explicit decision and
        mitigation assignments.

   5. ATTRIBUTION CHILL
        Identifying who said what makes participants
        cautious. Recovery: anonymize; attribute to
        the team.

   6. WRONG TIME HORIZON
        Failure 5 years out is too abstract; 1 month
        out is too constrained. Match horizon to the
        project nature.

   7. ONLY-INSIDERS
        All participants invested in success.
        Consider including outside-the-team perspectives
        (advisors, adjacent teams).

THE COMPARISON WITH POST-MORTEM

   POST-MORTEM:
       After failure: what went wrong, what can we
       learn?
       Cost: the failure already happened.

   PRE-MORTEM:
       Before launch: what could go wrong, what can we
       mitigate?
       Cost: 1-2 hour exercise.
       Benefit: address risks before they materialize.

   Both valuable; pre-mortem is the cheaper one.

THE OPERATIONAL TEMPLATE

   Project / decision: ________________________________

   Time horizon: ______________________________________

   Failure framing (catastrophic / embarrassing /
   underwhelming): ____________________________________

   Participants: ______________________________________

   Silent write narratives:
       Person 1: _______________________________________
       Person 2: _______________________________________
       ...

   Clusters identified:
       1. ______________________________________________
       2. ______________________________________________
       3. ______________________________________________

   Per cluster: probability / impact / mitigability
       1. _____ / _____ / _____
       2. _____ / _____ / _____
       3. _____ / _____ / _____

   Decisions:
       Mitigate (with owner / deadline): _____________
       Monitor (with trigger): _______________________
       Accept: _______________________________________
       Deal-breaker (re-examine): ____________________
```

> **Operational notes:** Four disciplines. (1) Run pre-commitment, not post. The exercise loses honesty once the team is socially committed. Schedule it as a gate, not as ceremony. (2) Silent writing before discussion. Open brainstorm gets dominated by first speakers; private writing surfaces independent assessments and catches groupthink. (3) Aggregate across narratives. Patterns appearing in multiple independent write-ups are more reliable than any single prediction. The clustering is where the analysis lives. (4) Decide and assign. The exercise without follow-through is theater. Each cluster needs a decision (mitigate / monitor / accept / deal-breaker) and, where mitigated, an owner and deadline.
