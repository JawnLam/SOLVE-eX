---
Item_ID: tt-kepner-tregoe
Item_Prototype: Thinking_Tool
Title: Kepner-Tregoe
tt_Source: "Charles Kepner & Benjamin Tregoe 1965 (The Rational Manager); refined in The New Rational Manager 1981"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Decision analysis
tt_Operation: Score and rank options
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Matrix
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Industrial / business
tt_Posture:
- Beginner-friendly
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Decision / choice
tt_SOLVE_eX_Phase: [5]
tt_SOLVE_eX_Step: [5.1, 5.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Pre-Mortem
- Weighted Decision Matrix
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Decision / choice']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "A four-process system for managers: Situation Appraisal (what's going on?), Problem Analysis (root cause?), Decision Analysis (best choice?), Potential Problem Analysis (what could go wrong?). The Decision Analysis component is the multi-criteria part — distinct from the diagnostic Problem Analysis."
Needs_Processing: false
AI_Instructions: ''
---

# Kepner-Tregoe

**One-line summary:** A four-process management framework — Situation Appraisal, Problem Analysis, Decision Analysis, Potential Problem Analysis — that organizes any complex managerial situation into separate, properly-sequenced reasoning steps with their own templates.

**When to reach for it:** Cross-functional escalations where multiple kinds of work are entangled (something is wrong + a decision is needed + risks are unclear), and a single team needs to disentangle them and address each properly.

---

## Purpose Of This Thinking Tool

Most management situations are not one problem; they're a mix of "what's going on?", "what's causing this?", "what should we do?", and "what could go wrong with the chosen approach?" Untangled, the team flips between these modes, addresses none well, and produces a decision that's actually a vague mixture. Kepner-Tregoe (KT) names the four modes and gives each its own structured process:

1. **Situation Appraisal (SA)** — Inventory concerns, separate them, prioritize, and route each to its appropriate process.
2. **Problem Analysis (PA)** — Diagnose root cause when "something deviates from expected." Compare *is* vs. *is-not* facts to localize the cause.
3. **Decision Analysis (DA)** — Make a choice between alternatives. Separate "must" criteria (hard requirements) from "want" criteria (weighted preferences); evaluate options against both.
4. **Potential Problem Analysis (PPA)** — Pre-mortem the chosen course of action. List potential problems, assess likelihood × impact, and design preventive and contingent actions.

The non-obvious operational insight is the *sequencing*: SA before PA, PA before DA, DA before PPA. Skipping or reordering these is the most common failure mode. Diving into Decision Analysis without a Problem Analysis means the team is choosing between cures for a misdiagnosed condition. Skipping PPA means shipping a chosen plan without explicit risk assessment.

Developed by Charles Kepner and Benjamin Tregoe at RAND in the 1950s, KT became Fortune-500 management training canon (DuPont, GE, Toyota, IBM all adopted it). Today it survives as a structured way to think about complex managerial situations — closer to a methodology than a single tool.

## Why Use This Thinking Tool

Three failure modes KT prevents:

1. **Mode confusion.** "We have a problem and we need to decide what to do" mashes diagnosis and decision. KT separates them, ensuring each gets its proper process.
2. **Hidden mandatory criteria.** DA's must/want distinction prevents the common error of letting a high-scoring option win when it fails a hard requirement.
3. **Risk myopia.** PPA forces explicit attention to what could go wrong with the chosen plan — most teams skip this and ship a plan without contingencies.

For consulting and operations work, KT is a thinking *operating system*: a stable structure that keeps complex meetings on track and ensures the right kind of analysis at each step.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Situation Appraisal: list all concerns. Separate them. Prioritize by urgency,   |
|      | importance, and growth. Route each to PA / DA / PPA.                            |
|    2 | Problem Analysis (only for "something is wrong" concerns):                      |
|      |    State the deviation precisely.                                               |
|      |    Compare IS vs. IS-NOT (what does/doesn't exhibit the problem?).              |
|      |    Identify distinctions (what's different about IS vs. IS-NOT?).               |
|      |    Identify changes (what changed when?).                                       |
|      |    Generate hypotheses; test against the IS/IS-NOT facts; pick best fit.        |
|    3 | Decision Analysis (only after PA, when a choice is needed):                     |
|      |    State the decision objective.                                                |
|      |    Separate Musts (binary, must be met) from Wants (weighted, scored).          |
|      |    Filter options against Musts. Score remaining against Wants.                 |
|      |    Pick highest-Want-score option that passes all Musts.                        |
|    4 | Potential Problem Analysis (after the decision is made):                        |
|      |    List potential problems with the chosen plan.                                |
|      |    Assess likelihood × impact for each.                                         |
|      |    Design preventive actions (reduce likelihood) and contingent actions         |
|      |    (reduce impact if it occurs).                                                |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
SITUATION APPRAISAL TEMPLATE

      Concern             | Type (PA / DA / PPA / Other) | Urgency | Importance | Growth
      --------------------|------------------------------|---------|------------|--------
                          |                              |         |            |
                          |                              |         |            |
      Prioritize:  high U+I+G first.

PROBLEM ANALYSIS — IS / IS-NOT GRID

      Dimension      | IS (where/what/who deviation appears) | IS-NOT (where/what/who similar but not affected)
      ---------------|---------------------------------------|--------------------------------------------------
      What           |                                       |
      Where          |                                       |
      When           |                                       |
      Extent         |                                       |

      Distinctions (IS but not IS-NOT): __________________________________________
      Changes (when did distinctions appear?): __________________________________
      Candidate causes that fit IS but not IS-NOT:
        H1: _______________________________________________________________________
        H2: _______________________________________________________________________

DECISION ANALYSIS — MUSTS AND WANTS

      MUSTS (binary; option fails if not met)
        M1: ______________________________________________________________________
        M2: ______________________________________________________________________

      Option | M1 | M2 | M3 | Pass to Wants?
      -------|----|----|----|----------------
      A      |    |    |    |
      B      |    |    |    |

      WANTS (weighted; only options passing Musts)
        Want         | Weight | Option A score | Option B score | ... 
        -------------|--------|----------------|----------------|------
                     |        |                |                |
        Weighted Σ:                ___              ___           ___

POTENTIAL PROBLEM ANALYSIS

      Potential Problem | Likelihood | Impact | Preventive Action | Contingent Action
      ------------------|------------|--------|--------------------|-------------------
                        |            |        |                    |
                        |            |        |                    |
                        |            |        |                    |

      Trigger that activates contingent action: _________________________________
      Owner of preventive / contingent action:  _________________________________
```

> **Operational notes:** The single highest-leverage move is Situation Appraisal at the front — it dissolves arguments by routing each concern to its proper process. Most cross-functional escalations have a PA, a DA, and a PPA tangled together; SA names them and the meeting becomes tractable. Second: in DA, ruthlessly distinguish Musts from Wants. Stakeholders try to push their preferences into Musts ("we MUST have feature X") to functionally veto options; the discipline asks "if we found the perfect solution that lacks X, would you really kill it?" If yes, it's a Must; if no, it's a Want. Third: PPA is most valuable on irreversible plans — it converts pre-mortem intuitions into an actionable register of preventive/contingent actions with owners. Fourth: KT can feel heavy. Use the full system on high-stakes situations; for routine choices, just one of the four processes (typically DA or PA alone) is enough. The system's value is the named modes and proper sequencing, not the full machinery every time.
