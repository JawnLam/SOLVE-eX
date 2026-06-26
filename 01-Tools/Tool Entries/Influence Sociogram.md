---
Item_ID: tt-influence-sociogram
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Influence Sociogram
tt_Source: Moreno 1934
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Power, politics & influence mapping
tt_Operation: Map relational topology
tt_Cross_Domains:
- Inner / psychological work
tt_Form:
- Visualization technique
tt_Scale:
- Solo
- Small group
tt_Duration:
- Single session
tt_Lineage:
- Therapeutic / psychological
- Industrial / business
tt_Posture:
- Solo-quiet
- Trust-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Power / politics
- Group / organization
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Coalition Mapping
tt_Often_Follows:
- Stakeholder Power-Interest Grid
tt_Pairs_Well_With:
- Stakeholder Power-Interest Grid
- Coalition Mapping
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
- 2026-05-07 — initial classification (Phase 3, v0.4 schema)
- '2026-05-07 — schema v1.11.0: dropped tt_Domain_Name; tt_Domain and tt_Cross_Domains store descriptive names (Roman numerals removed)'
- '2026-05-07 — schema v1.12.0: tt_Operation rewritten as shared value ''Map relational topology'' (was tool-specific summary)'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Power / politics', 'Group / organization']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: '2026-05-07'
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: Jacob Moreno introduced sociometry in Who Shall Survive? (1934). The technique migrated from group therapy and education into organizational network analysis (Krackhardt, Cross). Posture is solo-quiet because the map will surface uncomfortable truths about who actually moves whom; trust-required because sharing the map widely can damage relationships.
Needs_Processing: false
AI_Instructions: ''
---

# Influence Sociogram

**One-line summary:** Plot people as nodes, draw arrows for who influences whom, and read the topology — hubs, brokers, isolates — to find the real paths to outcomes.

**When to reach for it:** The org chart says one thing but decisions move differently. You need to know who actually carries weight, who connects subgroups, who's quietly central, and which formal authority figures are bypassed in practice.

---

## Purpose Of This Thinking Tool

The org chart shows reporting lines. The sociogram shows influence lines — and they often disagree. A sociogram makes the *informal organization* visible: the people whose opinions move others' positions, the bridges between otherwise-disconnected subgroups, the peripheral actors who are heard inside their cluster but invisible outside it.

The tool produces three classes of insight:

1. **Hubs** — nodes with many incoming or outgoing influence edges. High-leverage targets for any persuasion strategy. Often differ from formal authority.
2. **Brokers** — nodes that bridge otherwise-separated clusters. Disproportionately powerful because information and persuasion flow through them. Removing or alienating a broker fragments the network.
3. **Isolates** — nodes with few connections. Either irrelevant to the question, or under-engaged given their formal role. Both readings matter.

A bonus reading: **non-obvious paths.** If you can't influence A directly, the sociogram shows whose influence on A you might enlist. This is the political analog of shortest-path routing.

## Why Use This Thinking Tool

In any sufficiently mature organization, decisions of consequence are pre-made informally before they're ratified formally. A leader who only engages the formal decision-maker arrives after the influence has already crystallized. The sociogram forces the question: *who shaped this person's view before I got there, and who else is shaping it now?*

It also corrects the bias toward seniority. In most knowledge orgs, technical or domain credibility produces influence asymmetric to title. The mid-level engineer whose code review everyone trusts moves more decisions than the VP they nominally report to. The sociogram makes that visible without anyone having to say so out loud.

For consulting work, the tool is most useful in the first 4–6 weeks of an engagement. Build it from observation and interviews, not from the org chart. By the end of week 6, your sociogram should disagree with the org chart in at least three places — if it doesn't, you haven't been listening hard enough.

## How To Use This Thinking Tool

```
|======|==================================================================================|
| Step |                                     Action                                       |
|======|==================================================================================|
|    1 | Define the question. Influence is question-specific — A's influence on technical |
|      | decisions ≠ A's influence on hiring. State the slice.                            |
|    2 | List all candidate nodes (people or roles). Don't filter by formal seniority.    |
|    3 | For each pair, ask: does X meaningfully shape Y's view on this question?         |
|      | Direction matters. A → B means A influences B.                                   |
|    4 | Score edge strength: weak (1) / moderate (2) / strong (3). Use line thickness    |
|      | when drawing.                                                                    |
|    5 | Lay out the graph spatially — group nodes that influence each other, separate    |
|      | clusters that don't.                                                             |
|    6 | Identify hubs (high in/out degree), brokers (between clusters), isolates.        |
|    7 | For your goal: trace the non-obvious paths to the people you need to influence.  |
|======|==================================================================================|
```

## The Actual Thinking Tool

```
                            (The map itself is the artifact)

                             [ Person A ]──→[ Person B ]
                                   │              ▲
                                   │              │
                                   ▼              │
                             [ Person C ]←──[ Person D ]
                                   │              ▲
                                   │              │
                                   ▼              │
                             [ Person E ]    [ Person F ]
                                                  │
                                                  ▼
                                             [ Person G ]

|====================|========================================================|
|        Role        |                       Definition                       |
|====================|========================================================|
| Hub                | Many influence edges in or out. High persuasion        |
|                    | leverage; central to any campaign.                     |
| Broker             | Connects otherwise-separated clusters. Information     |
|                    | and persuasion flow through them. Disproportionate     |
|                    | power; lose them and the network fragments.            |
| Isolate            | Few connections. Either peripheral to this question    |
|                    | or under-engaged given their formal role.              |
| Sink               | Influences received but rarely transmits. May be       |
|                    | high-status but politically passive.                   |
| Source             | Transmits but isn't influenced. Independent thinker;   |
|                    | hard to move via lateral persuasion.                   |
|====================|========================================================|

|========================|====================|========================|==========|
| Influence path target  | Direct (Y/N)?      | Path through whom?     | Strength |
|========================|====================|========================|==========|
|                        |                    |                        |          |
|========================|====================|========================|==========|
```

> **Confidentiality:** A sociogram is the most politically sensitive artifact in this entire library. It names asymmetries that the named people may not want named. Keep it solo or share only inside a tight trust circle. Never email it. Never put it on a shared drive. If you wouldn't say the line out loud, don't draw the edge on a wall.

> **Refresh cadence:** Influence networks shift on a quarterly timescale. A 6-month-old sociogram is unreliable; an 18-month-old one is misleading. Rebuild it whenever leadership changes or after any major organizational event.
