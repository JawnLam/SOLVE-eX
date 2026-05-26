---
Item_ID: tt-network-centrality-analysis
Item_Prototype: Thinking_Tool
Title: Network Centrality Analysis
tt_Source: "Linton Freeman, 'Centrality in Social Networks: Conceptual Clarification' (Social Networks, 1979); broader social-network-analysis tradition (Wasserman & Faust 1994; Borgatti, Mehra, Brass, Labianca 2009 — Network Analysis in the Social Sciences)."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Systems / cybernetic thinking
tt_Operation: Map relational topology
tt_Cross_Domains: []
tt_Form:
- Algorithm
- Visualization technique
- Mental model
tt_Scale:
- Small group
- Organizational
- Inter-organizational
- Civilizational
tt_Duration:
- Workshop
- Project
tt_Lineage:
- Western analytic / academic
- Mathematical / formal
tt_Posture:
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Coalition Mapping
- Influence Sociogram
tt_Often_Follows:
- Stakeholder Power-Interest Grid
tt_Pairs_Well_With:
- Influence Sociogram
- Coalition Mapping
- Clustering Percolation Analysis
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
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
Quick_Notes: "Four canonical centrality measures (Freeman 1979): degree (number of connections), betweenness (lying on paths between others), closeness (average distance to all others), eigenvector / PageRank (connections to important others). Each captures a different kind of 'importance.' For organizational network analysis (ONA), degree finds connectors, betweenness finds bridges, closeness finds reach, eigenvector finds prestige. Picking the wrong centrality measure for the wrong question is the dominant failure mode."
Needs_Processing: false
AI_Instructions: ''
---

# Network Centrality Analysis

**One-line summary:** A family of mathematical measures (degree, betweenness, closeness, eigenvector) that identify which nodes occupy structurally important positions in a network — used to find connectors, bridges, prestige holders, and information bottlenecks.

**When to reach for it:** Organizational network analysis (who actually connects the company?), change-management diagnosis (whose buy-in is structurally load-bearing?), influence mapping in stakeholder analysis, knowledge-flow audits, and any case where formal org charts under-describe how information and influence actually move.

---

## Purpose Of This Thinking Tool

Linton Freeman's 1979 paper *Centrality in Social Networks: Conceptual Clarification* formalized four distinct measures of "importance" in a network, each capturing a different structural role:

- **Degree centrality** — how many direct connections a node has. Identifies *connectors* (people with many ties).
- **Betweenness centrality** — how often a node lies on the shortest path between other pairs of nodes. Identifies *bridges* and *gatekeepers* (people through whom information must pass).
- **Closeness centrality** — average distance from a node to all other nodes. Identifies *reach* (people who can spread information broadly with few hops).
- **Eigenvector centrality / PageRank** — how connected a node is to other well-connected nodes. Identifies *prestige* (people whose connections are themselves important).

The non-obvious operational insight is that **these four measures often disagree about who is important.** A high-degree node (lots of connections) may have low betweenness (their connections are all in one cluster, so they bridge nothing). A high-betweenness node may have low degree (they have few connections, but each is crucial). A high-eigenvector node may have low degree (they are connected only to the right people). The four measures answer four different questions about network structure, and which one matters depends on what you're trying to do.

For **organizational network analysis (ONA)**, the practical mapping:

|         Question           |       Use this measure          |          What it finds          |
|----------------------------|---------------------------------|---------------------------------|
| Who are the connectors?    | Degree                          | People with many ties           |
| Who controls information?  | Betweenness                     | Bridge nodes / gatekeepers      |
| Who reaches everyone fast? | Closeness                       | Broad-reach people              |
| Who has prestige?          | Eigenvector / PageRank          | Connected to other importants   |

The dominant failure mode is **using the wrong centrality measure for the question being asked**. Asking "who are the influencers?" and reaching for degree centrality (most-connected) when the question really is about prestige (who matters in the eyes of others) produces actionable-looking but misleading answers.

A second insight: **bridge nodes (high betweenness) are operationally the most fragile and most powerful.** They control information flow, which gives them disproportionate informal power; if they leave, the network can fragment. ONA practitioners track bridge nodes carefully because they are simultaneously high-leverage (engage them, the information flows) and high-risk (lose them, the network breaks).

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The org-chart trap.** Formal hierarchies show reporting lines but not influence. Asking "who do we need on board for this change?" by reading the org chart misses the informal connectors and bridges who are often more structurally important. ONA reveals them.
2. **The "everyone is equally important" failure.** Stakeholder analysis that treats nodes as equivalent loses the structural signal — some nodes have order-of-magnitude more influence than others by virtue of position alone. Centrality quantifies this.
3. **The single-measure trap.** Practitioners who use only one centrality measure (typically degree, because it's intuitive) miss the structural roles the other three measures capture. A robust ONA reports all four and reads them in combination.

For consulting and change management, ONA is the discipline that converts "we need to talk to the right people" from vague aspiration into a defensible map. It is also a discipline that frequently surprises sponsors — the people who appear important on the org chart and the people who appear important in the network are often different people, and the second list is more predictive of change-program success.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the network: who are the nodes (people, teams, organizations)? What is    |
|      | the tie type (collaboration, communication, information-sharing, advice-seeking)? |
|    2 | Collect the network data: typically a survey ("who do you go to for advice on X?" |
|      | or "who do you collaborate with weekly?"), email metadata, or observed behavior. |
|    3 | Build the adjacency matrix or edge list. Many tools accept this directly         |
|      | (NodeXL, Gephi, igraph in R/Python, NetworkX, Polinode for ONA).                |
|    4 | Compute all four centrality measures. Don't pick one in advance.                |
|    5 | Visualize the network with node size proportional to one centrality measure;    |
|      | swap measures to see how rankings shift.                                         |
|    6 | Interpret per question: connectors (degree), bridges (betweenness), reachers    |
|      | (closeness), prestige (eigenvector). Different questions, different measures.    |
|    7 | Stress-test: remove the top 3 betweenness nodes from the network; does it       |
|      | fragment? If yes, those are critical-path nodes — high-leverage AND high-risk.  |
|    8 | Report findings honestly, including where centrality contradicts the formal org |
|      | chart. Be careful with social cost of naming structural-but-low-status people.  |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FOUR CENTRALITY MEASURES (use in combination)

   1. DEGREE CENTRALITY
        Count of direct connections.
        High-degree node: well-connected, many ties, often a "connector."
        Question answered: Who has the most direct ties?
        Use case: identifying social hubs, finding active community members.

   2. BETWEENNESS CENTRALITY
        How often the node lies on shortest paths between other nodes.
        High-betweenness node: a bridge or gatekeeper.
        Question answered: Through whom does information flow?
        Use case: change management (engage bridges first), risk
                   assessment (bridges are fragility points).

   3. CLOSENESS CENTRALITY
        Average graph distance from this node to all others.
        High-closeness node: can reach the network quickly.
        Question answered: Who can broadcast information fastest?
        Use case: identifying nodes for rapid information dissemination.

   4. EIGENVECTOR CENTRALITY / PAGERANK
        Connected to other well-connected nodes.
        High-eigenvector node: prestigious; "important by association."
        Question answered: Who is structurally prestigious?
        Use case: identifying thought leaders, influencers, status-driven
                   adoption patterns.

THE QUESTION-MEASURE MAPPING TABLE

   |  Question                        | Use measure(s)              |
   |----------------------------------|-----------------------------|
   | Who are the active connectors?   | Degree                      |
   | Who are the bridges?             | Betweenness                 |
   | Who can reach everyone fast?     | Closeness                   |
   | Who has prestige?                | Eigenvector / PageRank      |
   | Who is structurally critical?    | Betweenness + degree        |
   | Who would leave the biggest gap  | Betweenness + degree +      |
   |   if they left?                  |   eigenvector               |

THE FOUR-QUADRANT INTERPRETATION GUIDE (for 2-measure combinations)

                            HIGH BETWEENNESS
                                  │
                                  │
       isolated bridge             │           critical-path connector
       (rare, fragile)             │           (high leverage, high risk)
   LOW DEGREE ──────────────────────────────── HIGH DEGREE
       peripheral                  │           hub (in-cluster only)
       (low importance)            │           (loud but not bridging)
                                  │
                                  │
                            LOW BETWEENNESS

   The most operationally interesting nodes are upper-right
   (high degree + high betweenness) — connectors who also bridge.
   The most fragile are upper-left — single bridges with few alternatives.

THE NETWORK-COLLECTION PROTOCOL

   Question framing matters:
       "Who do you go to for advice on X?" — advice network
       "Who do you collaborate with at least weekly?" — collaboration network
       "Whose decisions affect your work?" — influence network
       Different networks reveal different roles.

   Roster vs. name-generator:
       Roster (give a list, ask which you interact with): fast, may miss
              external ties.
       Name-generator (ask "who do you...", they fill in names): more
              complete but harder to clean.

   Response rate:
       Below ~70% participation, network metrics get unreliable.
       Plan for follow-ups; partial networks lie about structure.

   Anonymization:
       ONA results name people, which has political consequences.
       Often the right move is to share aggregated structural insights
       publicly and individual centrality scores privately with
       leadership.

THE STRESS-TEST DIAGNOSTIC (find the fragility)

   For each of the top 5 betweenness nodes:
       Hypothetically remove them.
       Does the network fragment? (Look for disconnected components.)
       Does the diameter (longest shortest path) increase substantially?

   Nodes whose removal fragments the network are critical bridges.
   They are high-leverage for change initiatives AND high-risk for
   business continuity. Often deserve focused engagement (mentoring,
   redundancy, retention) regardless of formal level.

WHEN ONA SURPRISES THE ORG CHART (what to do)

   Common surprises:
       - A mid-level person has the highest betweenness in the company
       - A senior leader has low centrality on every measure
       - A team that "doesn't matter" structurally connects two key
         business units
       - A "key influencer" identified by HR has low eigenvector
         centrality (no one important defers to them)

   These results often challenge organizational self-image. Two responses:
       1. Take the data seriously. The structural reality is what it is.
       2. Be careful with the social cost. ONA can reveal that a senior
          leader is structurally unimportant; making that public can
          damage the leader and the org. Calibrate disclosure.

CENTRALIZATION (the meta-statistic)

   Beyond individual node centrality, networks themselves vary in how
   centralized they are.

   High-centralization network: few nodes carry most of the structural
   weight. Vulnerable but efficient.

   Low-centralization network: weight is distributed broadly. Resilient
   but slower for top-down information diffusion.

   For change management: high-centralization networks are easier to
   change top-down (find the central nodes, engage them). Low-
   centralization networks require broader engagement; no shortcut.
```

> **Operational notes:** Four disciplines. (1) Pick the centrality measure based on the question, not the convenience of the measure. Degree is easiest to compute but rarely the right answer for "who matters?" Betweenness for bridges, closeness for reach, eigenvector for prestige — match the measure to the question. (2) Bridges (high betweenness) are simultaneously high-leverage and high-risk. Engage them for change; protect them for continuity. They are often the most operationally important nodes in a network and the most often missed by org-chart-only thinking. (3) Network data collection has political consequences. ONA reveals structural realities the formal organization may not want to confront. Calibrate disclosure carefully — aggregated insights are often the right unit for public reporting; individual centrality scores are often best shared privately. (4) The four measures often disagree, and the disagreement is itself informative. Always compute all four and look at where they converge and where they diverge. Convergence indicates clearly important nodes; divergence reveals that the node plays a specific structural role (bridge but not hub, prestige but not connected, etc.).
