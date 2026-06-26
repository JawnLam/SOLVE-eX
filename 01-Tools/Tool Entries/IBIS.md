---
Item_ID: tt-ibis
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: IBIS (Issue-Based Information System)
tt_Source: "Horst Rittel & Werner Kunz 1970 (early IBIS); refined by Conklin & Begeman (gIBIS) 1980s; Compendium tool 2000s"
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Argument structuring
tt_Operation: Decompose hierarchically
tt_Cross_Domains: []
tt_Form:
- Visualization technique
- Sequenced workflow
tt_Scale:
- Small group
- Organizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Western analytic / academic
- Design / craft tradition
tt_Posture:
- Collaborative-willing
- Adversarial-tolerant
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Toulmin Model
- Dialectical Maps
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Three node types: Issues (questions), Positions (proposed answers), Arguments (pro/con). Originally designed for wicked problems (Rittel) where the right framing is itself contested. The strongest design move: every node is *named* and *connected*, making implicit dialogue structure visible."
Needs_Processing: false
AI_Instructions: ''
---

# IBIS (Issue-Based Information System)

**One-line summary:** A graphical argumentation method built from three node types — Issues (questions), Positions (proposed answers), and Arguments (pro/con) — used to map deliberation on contested or wicked problems.

**When to reach for it:** Group decisions on wicked problems, design rationale capture, post-meeting record of why a decision was made, structured policy debate, and any deliberation that needs to leave an auditable trail.

---

## Purpose Of This Thinking Tool

IBIS was created by Horst Rittel (Berkeley designer / planner) for *wicked problems* — problems where stakeholders disagree on the framing itself, where there's no stable problem statement to optimize against. The method's three node types impose a useful structure on otherwise free-flowing deliberation:

- **Issue** — a question or contested decision (drawn as `?`)
- **Position** — a proposed answer to an issue (drawn as `•`)
- **Argument** — a consideration that supports (`pro`) or undermines (`con`) a position

Issues spawn Positions; Positions are linked to supporting and opposing Arguments; Arguments themselves can spawn sub-Issues when contested. The graph is the deliberation's bones.

The non-obvious operational insight: capturing the *issue* explicitly is what most meetings skip. Discussions hop directly to positions ("we should do X") or arguments ("but doing X is risky") without naming the underlying question. IBIS forces issue-articulation as the first move, which often re-frames the discussion productively.

Compendium (open-source IBIS tool) and modern tools like Kialo continue this lineage. The method also influenced design rationale capture in software engineering (gIBIS, Conklin's "Dialogue Mapping").

## Why Use This Thinking Tool

Three failure modes IBIS prevents:

1. **Position-without-issue.** Discussions hop straight to advocacy. The issue node forces the question to be named first.
2. **Lost rationale.** Six months after a decision, no one remembers why it was made. The IBIS graph is the durable record.
3. **Wicked-problem confusion.** When the framing is contested, normal decision tools fail. IBIS surfaces the framing as an explicit issue with competing positions.

For consulting, design, and policy work, IBIS is the artifact that survives the meeting — auditable, referenceable, expandable. It's especially powerful for cross-functional decisions where stakeholders need to see how their concerns were addressed.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Name the root issue — the central question being deliberated.                   |
|    2 | List positions that have been proposed or could be proposed.                    |
|    3 | For each position, list arguments that support it (pro) and undermine it (con). |
|    4 | If an argument generates a new sub-question, attach a sub-issue to it.          |
|    5 | Continue until the graph is reasonably complete; aim for breadth, not depth     |
|      | of detail (let detail emerge).                                                  |
|    6 | Identify positions whose pro/con balance is informative; eliminate clearly      |
|      | dominated positions.                                                            |
|    7 | If the issue has multiple legitimate positions surviving review, either pick   |
|      | one with explicit acknowledgement of trade-offs, or escalate to a higher-level  |
|      | issue.                                                                          |
|    8 | Save the graph. It IS the decision rationale.                                  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
IBIS NOTATION

    ?  ISSUE         (a question)
    •  POSITION      (a proposed answer)
    +  PRO ARGUMENT  (supports a position)
    −  CON ARGUMENT  (undermines a position)

EXAMPLE STRUCTURE (ASCII-rendered)

    ? Should we centralize procurement?
    │
    ├── • Yes, fully centralize
    │   ├── + Volume discounts (saving ~12%)
    │   ├── + Easier vendor management
    │   ├── − Slower local-team execution
    │   ├── − Loss of local supplier relationships
    │   │   └── ? How much value do those relationships provide?
    │   │       ├── • High in some markets, low in others
    │   │       ├── • Mostly relational, low transactional value
    │   └── + Standardized contracts
    │
    ├── • No, keep distributed
    │   ├── + Local responsiveness
    │   ├── − Foregoes volume discounts
    │   └── − Inconsistent contract terms across geos
    │
    └── • Hybrid: centralize indirect, distribute direct
        ├── + Captures most volume discount
        ├── + Preserves operational responsiveness
        ├── − Adds complexity in the boundary cases
        └── ? Where is the boundary drawn?
            └── (further sub-issue)

WORKSHEET

    Root Issue:  ___________________________________________________

    Position A: __________________________________________________
      Pro arguments: a1 ________________ a2 ________________
      Con arguments: c1 ________________ c2 ________________
      Sub-issues raised: ?si1 _______________________

    Position B: __________________________________________________
      Pro arguments: ____________________________________________
      Con arguments: ____________________________________________

    Position C (synthesis or alternative):
      _____________________________________________________________

    DECISION
      Selected position: _____________________________________________
      Trade-offs explicitly accepted: _________________________________
      Live unresolved sub-issues: _____________________________________
      Date / authors: _________________________________________________

DIALOGUE MAPPING TIPS (Conklin)

    • Always start with an issue; never with a position
    • One node per idea — granular, not paragraph-sized
    • When two positions seem irreconcilable, look for a missing sub-issue
    • A "pro" for one position is not necessarily a "con" for another
    • The map is the meeting record; share it after, with revisions tracked

WHEN A POSITION IS DOMINATED

    Position D dominates Position E if:
      • Every pro for E is matched by an equal-or-better pro for D
      • E has at least one con not present for D
    Eliminate dominated positions to focus on real trade-offs.
```

> **Operational notes:** Three disciplines. (1) Capture the issue first, always. The instinct in meetings is to advocate (position) or counter-advocate (argument); the issue gets assumed. Naming it explicitly often re-frames the discussion productively — sometimes the team realizes it was answering the wrong question. (2) Granularity matters. Each node should hold one idea — a sentence, not a paragraph. Coarse nodes blur arguments together; the discipline is single-thought-per-node. (3) Treat the graph as the durable artifact. Many teams use IBIS in the meeting and lose the graph afterward; the value compounds when the graph survives — six months later when "why did we decide X?" comes up, the graph answers in full detail. Use a tool (Compendium, Kialo, or a structured wiki) that preserves it. Fourth: IBIS is most valuable for *wicked* problems (no agreement on framing) and *design* decisions (where the decision is whose preferences to weight). For tame problems with clear optimization criteria, simpler decision matrices serve.
