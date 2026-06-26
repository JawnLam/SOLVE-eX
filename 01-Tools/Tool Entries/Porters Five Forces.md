---
Item_ID: tt-porters-five-forces
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Porter's Five Forces
tt_Source: 'Michael Porter, Competitive Strategy: Techniques for Analyzing Industries and Competitors (1980); Harvard Business School. Refined in subsequent works including How Competitive Forces Shape Strategy (HBR 1979).'
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Strategic & game-theoretic reasoning
tt_Operation: Map relational topology
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Sequenced workflow
- Canvas
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
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Strategy / competition
tt_SOLVE_eX_Phase: [1, 3]
tt_SOLVE_eX_Step: [1.2, 3.2, 3.3]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- SWOT Analysis
tt_Often_Follows: []
tt_Pairs_Well_With:
- SWOT Analysis
- Wardley Maps
- Jobs-to-Be-Done
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Strategy / competition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Five forces shape an industry''s profitability: rivalry among existing competitors, threat of new entrants, threat of substitutes, bargaining power of suppliers, bargaining power of buyers. Useful for industry analysis, market entry, and identifying where competitive pressure originates. Common misuse: applied as static checklist; actually meant as dynamic structural analysis. Critique: focuses on industry-level forces; misses ecosystem and platform dynamics in modern markets.'
Needs_Processing: false
AI_Instructions: ''
---

# Porter's Five Forces

**One-line summary:** A structural framework for analyzing industry competitive intensity by examining five forces — rivalry, new entrants, substitutes, supplier power, buyer power — that together determine an industry's profit potential and where competitive pressure originates.

**When to reach for it:** Industry analysis (deciding whether a market is structurally attractive); market-entry decisions; competitive strategy (identifying which forces to neutralize, deflect, or exploit); investor diligence on industry economics; and any context where understanding the structural sources of competition matters more than understanding individual competitors.

---

## Purpose Of This Thinking Tool

**Porter's Five Forces** analyzes industry competitive intensity through five structural forces:

1. **Rivalry among existing competitors** — how intense is direct competition? (number of firms, growth rate, exit barriers, differentiation)
2. **Threat of new entrants** — how easily can new players enter? (capital requirements, switching costs, regulation, scale economies)
3. **Threat of substitutes** — what alternatives could replace the industry's offering? (price-performance of substitutes, switching costs)
4. **Bargaining power of suppliers** — how much can suppliers extract? (supplier concentration, switching costs, criticality)
5. **Bargaining power of buyers** — how much can buyers extract? (buyer concentration, price sensitivity, switching costs)

The non-obvious operational insight is that **industry profitability is determined by structure, not just by competition.** A "good" industry can have weak competitive rivalry but powerful suppliers extracting all the value; a "bad" industry can have intense rivalry that nonetheless leaves room for differentiated profit. The five forces collectively determine where value can be captured.

A second insight: **the framework is dynamic, not static.** Each force shifts over time. A new substitute (e.g., streaming for cable TV) can transform an industry from attractive to unattractive in a decade. Strategic action can shift forces (e.g., a firm building switching costs reduces buyer power).

A third insight: **strategic position involves choosing where to compete based on force structure.** A startup considering market entry should ask: are entry barriers I'd face high (bad to enter) or low (easy to enter — but then easy for next entrants too, suggesting the industry will commoditize)? Established firms ask: which forces threaten our profitability and how can we neutralize them?

A fourth insight: **modern critique exists.** The framework was developed for traditional industries; ecosystem dynamics (Apple's developer network), platform economics (Amazon's two-sided market), and complementary products (gas stations + cars) aren't well-captured. Use Porter as foundation; supplement with platform / ecosystem frameworks for modern contexts.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "competitor focus only" failure.** Treating competition as just rivalry between known firms misses suppliers, buyers, substitutes, and new entrants — often the larger threats.
2. **The "industry attractiveness ≠ company profitability" confusion.** Some firms profit in unattractive industries via differentiation; some struggle in attractive ones. Five Forces gives the industry frame; firm strategy is separate.
3. **The static-snapshot trap.** Using the framework once and assuming the analysis holds. Forces evolve; periodic re-analysis is essential.

For strategists, investors, market entrants, and anyone analyzing industry economics, Porter's framework is foundational.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the industry boundary precisely. Too broad and the analysis is vague;    |
|      | too narrow and it misses substitutes.                                            |
|    2 | Analyze rivalry. Number of competitors, growth, differentiation, exit barriers, |
|      | switching costs. High intensity → low profitability.                             |
|    3 | Analyze new-entrant threat. Capital, scale economies, network effects,           |
|      | switching costs, regulation, brand. High barriers → established firms protected. |
|    4 | Analyze substitute threat. What else could meet the same need? How does         |
|      | price/performance compare?                                                        |
|    5 | Analyze supplier power. Supplier concentration, switching costs, criticality of |
|      | input. High supplier power → margins extracted upstream.                         |
|    6 | Analyze buyer power. Buyer concentration, price sensitivity, alternatives,     |
|      | switching costs. High buyer power → margins extracted downstream.                |
|    7 | Synthesize. Which forces are strong? Where is value being captured? What's the |
|      | overall profit potential?                                                         |
|    8 | Translate to strategy. Which forces to neutralize? Which to exploit? Where to  |
|      | invest in structural advantages?                                                 |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FIVE-FORCES DIAGRAM

                +---------------------+
                |   New Entrants      |
                |  (threat of entry)  |
                +----------+----------+
                           |
                           v
       +-------+    +------+------+    +-------+
       |       |    |             |    |       |
       | Sup-  |--->|   Industry  |<---| Buyer |
       | plier |    |    Rivalry  |    | Power |
       | Power |    |             |    |       |
       +-------+    +------+------+    +-------+
                           ^
                           |
                +----------+----------+
                |    Substitutes     |
                |  (threat of replacement)|
                +---------------------+

THE FIVE FORCES — DRIVERS

   1. RIVALRY DRIVERS:
      - Number and balance of competitors
      - Industry growth rate (slow growth → fierce share fights)
      - Differentiation (low → price competition)
      - Switching costs (low → easier customer poaching)
      - Exit barriers (high → too many firms stay in)
      - Fixed cost structure (high → utilization races)

   2. NEW-ENTRANT BARRIERS:
      - Capital requirements
      - Economies of scale
      - Network effects
      - Switching costs / lock-in
      - Brand / reputation
      - Regulation, licenses
      - Distribution access
      - Proprietary tech / IP

   3. SUBSTITUTE THREAT:
      - Substitute price-performance ratio
      - Switching costs to substitute
      - Customer propensity to switch
      - Indirect substitutes (e.g., video calls vs. travel)

   4. SUPPLIER POWER:
      - Supplier concentration
      - Lack of substitutes for input
      - Forward-integration threat
      - Switching costs to alternative suppliers
      - Criticality of input to product

   5. BUYER POWER:
      - Buyer concentration
      - Price sensitivity
      - Backward-integration threat
      - Switching costs
      - Alternatives available
      - Information transparency

THE WORKED EXAMPLE — AIRLINE INDUSTRY

   RIVALRY: Very High
       Many competitors; thin differentiation; price-led
       competition; high fixed costs; slow growth.

   NEW ENTRANTS: Moderate
       High capital costs; regulation; gate access; but
       low-cost carriers have repeatedly entered.

   SUBSTITUTES: High
       Trains (in some markets); video conferencing;
       autonomous vehicles future threat.

   SUPPLIER POWER: High
       Aircraft makers (Boeing, Airbus duopoly); jet
       fuel; airports (limited gates); pilot unions.

   BUYER POWER: High (consumer side); Moderate (corporate)
       Price-comparison sites; many alternatives;
       commoditized service.

   Synthesis: industry has structurally weak profit
   potential. Hence airlines' historical struggle.

THE STRATEGIC RESPONSE PATTERNS

   Once you've analyzed forces, strategy involves:

   NEUTRALIZE STRONG FORCES:
       Build switching costs to reduce buyer power
       Develop proprietary supplier alternatives to
       reduce supplier power
       Differentiate to escape rivalry intensity

   EXPLOIT WEAK FORCES:
       If entry barriers are weak, enter quickly and
       build before others
       If substitutes are weak, develop the category

   SHIFT FORCES THROUGH STRATEGIC ACTION:
       Patents shift entry barriers
       Vertical integration shifts supplier/buyer power
       Standardization shifts substitute dynamics

THE COMMON FAILURE MODES

   1. INDUSTRY-DEFINITION ERROR
        Boundary too broad ("hospitality") or too narrow
        ("luxury hotels in Boston"). Recovery: define
        at the level where firms genuinely compete and
        substitute against each other.

   2. STATIC ANALYSIS
        Snapshot treated as permanent. Recovery:
        re-analyze periodically; forces evolve.

   3. CHECKLIST APPLICATION
        Filling boxes without integrating. Recovery:
        synthesize across forces; find the dominant
        ones.

   4. IGNORING ECOSYSTEM
        Modern industries have platform / network
        dynamics. Recovery: supplement Porter with
        ecosystem frameworks (e.g., Wardley Maps,
        platform analysis).

   5. CONFUSING INDUSTRY ATTRACTIVENESS WITH FIRM
      PROFITABILITY
        Profitable firms exist in unattractive
        industries; struggling firms exist in
        attractive ones. Recovery: separate industry
        analysis from firm strategy.

THE OPERATIONAL TEMPLATE

   Industry: __________________________________________
   Boundary clarity check: ____________________________

   Force 1 — Rivalry: Low / Moderate / High
       Drivers: __________________________________
   Force 2 — New Entrants: Low / Moderate / High
       Drivers: __________________________________
   Force 3 — Substitutes: Low / Moderate / High
       Drivers: __________________________________
   Force 4 — Supplier Power: Low / Moderate / High
       Drivers: __________________________________
   Force 5 — Buyer Power: Low / Moderate / High
       Drivers: __________________________________

   Dominant force(s): _________________________________
   Industry attractiveness assessment: ________________

   Strategic implications:
       Forces to neutralize: __________________________
       Forces to exploit: _____________________________
       Forces to monitor for shifts: __________________
```

> **Operational notes:** Four disciplines. (1) Define the industry precisely. The boundary determines which firms are "rivals" vs. "substitutes," which buyers count, etc. Wrong boundary produces wrong analysis. (2) Analyze drivers, not just outcomes. "High rivalry" without identifying why is uninformative. The drivers point to what could change. (3) Update the analysis. Industry forces evolve. The framework should be re-run on a cadence (annual? quarterly in volatile sectors?), not treated as a one-shot. (4) Supplement for modern markets. Platform, ecosystem, and complementor dynamics aren't well-captured by classic Five Forces. Use Porter as foundation, then add the missing dimensions for contexts where they matter.
