---
Item_ID: tt-wardley-maps
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Wardley Maps
tt_Source: Simon Wardley, originally developed at Canonical and Fotango (early 2000s); formalized in his 'Wardley Mapping' book and freely shared via Medium articles. Influenced by Sun Tzu's Art of War and Boyd's OODA loop.
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Strategic & game-theoretic reasoning
tt_Operation: Map relational topology
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Canvas
- Sequenced workflow
tt_Scale:
- Solo
- Small group
tt_Duration:
- Workshop
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
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
tt_Often_Precedes: []
tt_Often_Follows:
- Jobs-to-Be-Done
tt_Pairs_Well_With:
- Porter's Five Forces
- Jobs-to-Be-Done
- OODA Loop
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
Quick_Notes: 'Strategic visualization where Y-axis = visibility-to-user (anchor at top: user need; below it the value-chain components); X-axis = evolutionary stage (genesis → custom-built → product/rental → commodity/utility). Components flow right over time as they evolve. Maps reveal what to build, buy, outsource, or compete on; where to invest; and which market dynamics dominate. Uniquely captures evolution + competitive position together.'
Needs_Processing: false
AI_Instructions: ''
---

# Wardley Maps

**One-line summary:** A strategic visualization technique that plots a value-chain (anchored to user needs) against an evolutionary axis — from genesis to commodity — making visible what to build, buy, outsource, and compete on, and how the landscape will shift as components evolve.

**When to reach for it:** Strategic planning beyond traditional industry analysis (especially in tech, where evolution is rapid); identifying when to in-house a capability vs. consume it as utility; spotting where competitive advantage is currently possible vs. about to commoditize; understanding ecosystem and platform dynamics; and any context where understanding the *evolution* of components changes the strategic answer.

---

## Purpose Of This Thinking Tool

**Wardley Maps** plot value-chain components on two axes:

- **Y-axis: visibility to user** — at the top, the user and their need; below, components that satisfy the need (each more invisible to the user as you go down).
- **X-axis: evolutionary stage** — Genesis (novel, custom) → Custom-Built → Product / Rental → Commodity / Utility.

Each component is placed at its current location on both axes. The map reveals:

1. **The value chain** — what depends on what.
2. **Evolutionary position** — which components are novel vs. mature.
3. **Movement direction** — components naturally evolve rightward over time (genesis → commodity).
4. **Strategic implications** — what to build (genesis novelty), what to buy as product, what to outsource as utility.

The non-obvious operational insight is that **strategy depends on evolutionary stage, and that's invisible in most strategy frameworks.** Porter's Five Forces tells you industry structure; SWOT tells you firm capabilities. Wardley Maps add the dimension of *how each component is evolving* — and the strategic move differs at each stage. A genesis-stage component should be experimented with; a product-stage component should be bought; a commodity should be consumed as utility.

A second insight: **evolution is generally inevitable but rate varies.** Components flow right (toward commodity) over time. Network effects, regulation, and certain barriers can slow this; nothing reliably reverses it. Strategy that fights inevitable evolution loses.

A third insight: **the map enables predicting the future, not just reading the present.** When you see a component at "product" stage, anticipate that within years it will become commodity. Plan for it: how does the value chain change when this component becomes utility? Often whole industries restructure around the shift.

A fourth insight: **mapping is collaborative and iterative.** Done well, Wardley mapping is a workshop activity that surfaces shared understanding (or disagreement) about the landscape. Multiple maps may be needed for different perspectives (customer, competitor, regulator).

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "static snapshot" strategic blindness.** Most frameworks describe the present without addressing how it evolves. Wardley Maps add evolution.
2. **The "build everything" or "buy everything" reflex.** Without the framework, build/buy decisions follow ideology. Wardley puts each component in its appropriate stage.
3. **The "competitor-blind to substrate" trap.** Firms that compete fiercely at one layer often miss that the substrate (the layer below) has commoditized — undercutting their differentiation. Maps make the substrate visible.

For technology strategists, platform builders, large-scale architects, and anyone whose strategy depends on understanding how components evolve, Wardley Maps add a dimension other frameworks miss.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the user(s) and their needs at the top of the map.                    |
|    2 | Identify the value chain — components that, together, satisfy the need.        |
|      | Place each below the user, with dependencies as connecting lines.              |
|    3 | For each component, assess evolutionary stage. Genesis (novel)? Custom-built? |
|      | Product / Rental? Commodity / Utility?                                          |
|    4 | Place components on the X-axis according to their stage.                       |
|    5 | Identify movement. Which components are evolving rightward fast? Which are     |
|      | stuck? Which are at risk of commoditization?                                  |
|    6 | Read strategic implications. What should be built, bought, or consumed as     |
|      | utility? Where is differentiation possible?                                    |
|    7 | Anticipate the next 1-3 years. Which components will commoditize? How does    |
|      | the chain restructure?                                                         |
|    8 | Iterate the map with team / stakeholders. Disagreements about placement reveal |
|      | strategic uncertainties worth resolving.                                        |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE WARDLEY MAP STRUCTURE

   Y-axis (top → bottom): Visibility to user
       Top: User + need
       Below: Components that satisfy the need
       Bottom: Most invisible substrate

   X-axis (left → right): Evolutionary stage
       Genesis: novel, custom, uncertain
       Custom-Built: bespoke for one application
       Product / Rental: productized, multiple buyers
       Commodity / Utility: standardized, often metered

       (Some Wardley work uses 4 stages: I, II, III, IV)

   Components are placed by both axes simultaneously.
   Lines connect them by dependency.

   Visible:
                      USER (top)
                       |
                  Capability A (genesis)
                  /          \
            Component B    Component C
            (product)      (commodity)
                |
            Component D (utility)

THE EVOLUTIONARY-STAGE CHARACTERISTICS

   GENESIS (novel):
       Novel, uncertain, exploration mode
       Few users; bespoke; experimentation
       Strategic move: explore; small bets
       Don't industrialize prematurely

   CUSTOM-BUILT:
       Bespoke for a specific application
       Custom code, custom configurations
       Strategic move: refine into product if scaling
       
   PRODUCT / RENTAL:
       Productized for multiple users
       Variable customization
       Strategic move: buy / partner; differentiate
       on usage, not building

   COMMODITY / UTILITY:
       Standardized, often metered
       Cloud, electricity, common APIs
       Strategic move: consume as utility; don't build

THE EVOLUTIONARY-FORCES PATTERNS

   Forces driving rightward movement:
       Repeated demand
       Standardization pressure
       Economies of scale
       Industrialization

   Forces slowing rightward movement (rare reversals):
       Patents
       Network effects entrenching a player
       Regulation
       High switching costs

   Default expectation: rightward, irreversibly.

THE STRATEGIC-MOVE PATTERNS

   By component stage:

   GENESIS components:
       INNOVATE — explore; small bets
       Experimental teams; high tolerance for failure
       Don't outsource (vendors don't have it)

   CUSTOM-BUILT components:
       BUILD — bespoke implementations
       Lean teams; iterative
       Sometimes start to refine into product

   PRODUCT components:
       BUY — purchase from a vendor or use standard
       offering
       Don't reinvent
       Differentiate on application, not the product

   COMMODITY components:
       USE AS UTILITY — consume metered service
       Cloud infrastructure, payment processing,
       authentication
       Free up your engineers for genesis / custom

   The framework names what to do at each stage.

THE WORKED EXAMPLE — TECH STARTUP

   USER: Customer wanting AI-powered customer support

   Value chain (top to bottom):
       User → Web app
       Web app → Application logic (custom)
       App logic → AI inference (LLM API)
       LLM API → Underlying compute
       Compute → Cloud infrastructure

   Map placement:
       Web app (UI/UX): product stage
       App logic: custom (this is where differentiation
       lives)
       LLM API: rapidly evolving from product to
       commodity
       Compute (GPU / TPU): commodity (utility)
       Cloud infra: commodity (utility)

   Strategic implications:
       Don't build LLM from scratch — consume API
       Don't build cloud infra — use AWS/GCP
       Differentiate on app logic — this is custom-built
       Anticipate: LLM APIs will commoditize further;
       differentiation will move up the stack to
       app-layer

   Without the map, the firm might over-invest in
   building infrastructure or under-invest in
   differentiated app logic.

THE COMPLEMENTARY MOVES

   Wardley framework includes named strategic plays:

   "ECOSYSTEM" — encourage others to build on your
   commodity / utility (your platform); their innovation
   is your data.

   "PIONEERS-SETTLERS-TOWN PLANNERS" — different team
   types for different stages. Pioneers explore genesis;
   Settlers refine custom into product; Town Planners
   industrialize commodities.

   "ATTACK / DEFEND / EXPLOIT" — moves on the map as
   competitive responses.

   The full Wardley repertoire is rich; the basic
   mapping is the entry point.

THE COMMON FAILURE MODES

   1. WRONG USER / NEED ANCHOR
        Top of map is wrong; the value chain doesn't
        actually serve this user. Recovery: revisit
        anchor.

   2. WRONG EVOLUTIONARY-STAGE PLACEMENT
        Components placed at wrong X-axis position.
        Recovery: validate against actual market
        observation; check for vendors offering as
        product, utility offerings, etc.

   3. STATIC MAP
        Map drawn once and not revisited; evolution
        ignored. Recovery: re-map periodically; track
        movement.

   4. SOLO MAPPING
        One person's mental model; misses team
        knowledge. Recovery: collaborative mapping.

   5. INSUFFICIENT DEPTH
        Stops too high in the value chain. Recovery:
        keep going down; substrate often holds
        strategic surprises.

   6. NO ACTION FROM MAP
        Pretty diagram; no strategic decisions.
        Recovery: explicit "build / buy / consume"
        decisions per component, with timeline.

THE OPERATIONAL TEMPLATE

   User (top of map): _________________________________

   Need being satisfied: ______________________________

   Value chain (top to bottom):
       Component 1: _______________ Stage: ___________
       Component 2: _______________ Stage: ___________
       Component 3: _______________ Stage: ___________
       ...

   Movement direction (which components evolving fastest):
       _________________________________________________

   Strategic implications:
       Build (genesis / custom): _____________________
       Buy (product): ________________________________
       Consume as utility (commodity): _______________
       Anticipate commoditizing in 1-3 years: ________

   Workshop with team: agreement on placements? Y / N
   Disagreements reveal: ______________________________
```

> **Operational notes:** Four disciplines. (1) Anchor to user + need. The value chain serves the user; the map without anchor floats. The user-need at top disciplines what counts as a component. (2) Take evolution seriously. Components flow right; this is the main insight other frameworks miss. Strategic decisions that fight evolution generally lose; decisions aligned with evolutionary direction win. (3) Map collaboratively. One person's mental model misses team knowledge and won't generate the consensus needed for action. Disagreements during mapping are themselves strategic insights. (4) Refresh periodically. Today's product is tomorrow's commodity. The map should be re-drawn on a cadence appropriate to your industry's pace — annually for slower industries, quarterly or even more often for fast-moving ones.
