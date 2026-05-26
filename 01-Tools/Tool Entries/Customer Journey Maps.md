---
Item_ID: tt-customer-journey-maps
Item_Prototype: Thinking_Tool
Title: Customer Journey Maps
tt_Source: User experience and service-design tradition; popularized by Marc Stickdorn and Jakob Schneider's This Is Service Design Thinking (2010); adopted widely in IDEO, Adaptive Path, frog design. Modern toolkits via Nielsen Norman Group.
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: User-centered design
tt_Operation: Map relational topology
tt_Cross_Domains:
- Symbolic systems
tt_Form:
- Canvas
- Sequenced workflow
tt_Scale:
- Small group
tt_Duration:
- Workshop
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
- Human group
tt_About:
- Other / relationship
- Aesthetic / craft
tt_SOLVE_eX_Phase: [5, 6]
tt_SOLVE_eX_Step: [5.1, 6.1]
tt_Clarifies: ['Path', 'Action']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Service Blueprints
tt_Often_Follows:
- Personas
tt_Pairs_Well_With:
- Personas
- Empathy Maps
- Service Blueprints
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: A
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human', 'Human group'], tt_About=['Other / relationship', 'Aesthetic / craft']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: Map a customer's experience over time across touchpoints with a product / service. Capture stages, actions, thoughts, emotions, pain points, opportunities. Reveals friction invisible to internal teams; surfaces moments that matter (peak / end / surprise). Used in service design, UX, and customer-experience strategy.
Needs_Processing: false
AI_Instructions: ''
---

# Customer Journey Maps

**One-line summary:** A visualization technique that traces a customer's experience over time across all touchpoints with a product or service — capturing actions, thoughts, emotions, pain points, and opportunities — surfacing friction and moments-that-matter that internal-process views miss.

**When to reach for it:** Customer-experience improvement initiatives; service-design projects; product redesign with focus on experience flow; cross-functional alignment around customer view; understanding why metrics-good services produce experience-bad results; and any context where the question shifts from "what does our system do?" to "what does the customer experience?"

---

## Purpose Of This Thinking Tool

**Customer journey maps** trace experience across time. The structure:

1. **Stages** (columns): Awareness → Consideration → Purchase → Onboarding → Use → Loyalty / Churn (or domain-specific stages).
2. **Per stage, capture:**
   - **Actions** — what the customer is doing
   - **Touchpoints** — channels / interactions with you
   - **Thoughts** — what's going through their mind
   - **Emotions** — how they feel (often a curve from highs to lows)
   - **Pain points** — friction, frustration
   - **Opportunities** — places to improve
3. **Annotate** with internal data (analytics, support tickets, NPS) that informs each stage.

The non-obvious operational insight is that **internal-process views and customer-experience views diverge.** A company's internal map shows efficient process flow; the customer's experience map shows friction at handoffs, waits, and confusion that the process view doesn't capture. Mapping the customer view is a structural corrective.

A second insight: **the emotion curve often surprises.** Plotting emotional state across stages reveals that customer satisfaction isn't monotonic — peaks and dips appear in surprising places (often onboarding has dips even when sales experience is great). The dips often have outsized effect on retention.

A third insight: **the framework integrates with peak-end rule from behavioral psychology.** Customers' overall judgment of an experience is dominated by peak emotional moments and the end. Designing for peaks (delight moments) and ends (clean closure) often matters more than uniform improvement.

A fourth insight: **journey maps are facilitation tools, not just analytical artifacts.** Cross-functional teams building one together produce shared understanding that handed-off documentation can't match.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "internal-process blindness" failure.** Optimizing internal processes without seeing how they feel from the outside.
2. **The "ignore the dips" trap.** Average satisfaction can mask catastrophic individual moments that drive churn.
3. **The "every touchpoint equally important" assumption.** Peak-end rule says some moments dominate; journey maps surface them.

For UX designers, service designers, customer-experience strategists, marketing leaders, and anyone responsible for end-to-end customer experience, journey maps are foundational.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Choose a persona / customer segment to map. Different segments have different    |
|      | journeys.                                                                         |
|    2 | Define stages from the customer's perspective. Awareness through to              |
|      | post-purchase.                                                                    |
|    3 | For each stage, list customer actions, touchpoints, thoughts, emotions, pain   |
|      | points, opportunities.                                                           |
|    4 | Source from real customers — interviews, surveys, support data — not just      |
|      | internal assumptions.                                                             |
|    5 | Plot the emotion curve across stages. Identify peaks and dips.                  |
|    6 | Identify moments that matter — peaks, dips, ends.                                |
|    7 | Brainstorm interventions for high-leverage moments.                             |
|    8 | Validate the map with customers; iterate.                                       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE JOURNEY MAP STRUCTURE

   Stages:    Awareness   Consideration   Purchase   Onboarding   Use       Loyalty
   ─────────  ─────────   ─────────────   ────────   ──────────   ───────   ───────
   Actions    [...]       [...]           [...]      [...]        [...]     [...]
   Touchpoints [...]       [...]           [...]      [...]        [...]     [...]
   Thoughts   [...]       [...]           [...]      [...]        [...]     [...]
   Emotions   :)          :)              :|         :(           :)        :)
   Pain pts   [...]       [...]           [...]      [...]        [...]     [...]
   Opps       [...]       [...]           [...]      [...]        [...]     [...]

   Emotion curve plotted across the row reveals
   peaks and dips.

THE STAGE TEMPLATE

   AWARENESS:
       Customer realizes need; encounters category /
       brand.
       Actions: searching, asking, browsing.
       Channels: search, social, word-of-mouth, ads.

   CONSIDERATION:
       Comparing options; researching.
       Actions: reviews, comparisons, demos.
       Channels: review sites, sales calls, content.

   PURCHASE:
       Decision and transaction.
       Actions: configuring, paying, signing.
       Channels: site, app, store, email.

   ONBOARDING:
       First experience using.
       Actions: setup, learning, first-success
       moments.
       Channels: in-product, tutorials, support.

   USE:
       Ongoing usage.
       Actions: daily / weekly use, problem-solving.
       Channels: product, support, community.

   LOYALTY / CHURN:
       Long-term relationship.
       Actions: renewal, recommendation, leaving.
       Channels: support, success teams, exit surveys.

THE EMOTION CURVE INSIGHT

   Plot emotional state across stages:

   :) :) :) :( :| :) :) :( :)
   ▲              ▼  ▲        peak/dip
   |             |  |
   sales       activation  long-term

   Common patterns:
       Sales high (excitement) → Onboarding dip
       (friction) → Activation peak (success!) → Long
       term plateau

   Dips at activation are common churn drivers; peaks
   at sales are common over-confidence drivers.

THE PEAK-END RULE APPLICATION

   Daniel Kahneman's research:
       Customer's memory of experience is dominated by
       peak emotional moment + end.
       Average experience matters less than these
       two.

   Implications:
       Engineer specific peaks (delight moments)
       Engineer the end carefully (clean closure;
       follow-up; recap)
       Average improvement matters less than these
       two

   Many companies optimize average; should optimize
   peak-and-end.

THE WORKED EXAMPLE — SAAS ONBOARDING

   Persona: small-business owner trying our project
   management tool.

   Stages and emotion:
       Awareness (positive — saw it on Twitter)
       Consideration (positive — read good reviews)
       Sign-up (positive — frictionless)
       First-login (negative — overwhelming UI)
       Set-up (negative — doesn't understand jargon)
       First successful use (positive — satisfaction)
       Daily use (neutral — normal)
       Bug encounter (negative — slow support)
       Renewal time (uncertain)

   Peaks: first successful use.
   Dips: first-login + first bug.
   End matters: how does the renewal experience feel?

   Interventions:
       First-login: simplified default workspace;
       getting-started checklist
       First-bug: faster support; in-product help; bug
       acknowledgment
       Renewal: human contact 30 days before;
       celebrate success metrics

THE COMMON FAILURE MODES

   1. INTERNAL ASSUMPTIONS, NOT CUSTOMER DATA
        Map built from team's view; doesn't match
        actual experience. Recovery: customer
        interviews; survey data.

   2. UNIFORM ATTENTION
        All stages treated equally; missing peak-end.
        Recovery: identify peaks, dips, ends; focus
        intervention.

   3. NO EMOTION CURVE
        Map captures actions but not feelings.
        Recovery: explicit emotion plot.

   4. SINGLE-PERSONA MAP
        One map for many segments. Recovery: segment-
        specific maps.

   5. STATIC MAP
        Built once, never updated. Recovery: living
        document; refresh annually or after major
        changes.

   6. NO ACTION
        Map produced; nothing changes. Recovery:
        explicit interventions per high-leverage
        moment.

THE OPERATIONAL TEMPLATE

   Persona / segment: _________________________________

   Stages (customer perspective):
       Stage 1: ______________________________________
       Stage 2: ______________________________________
       Stage 3: ______________________________________
       ...

   Per stage:
       Actions: ______________________________________
       Touchpoints: __________________________________
       Thoughts: _____________________________________
       Emotion: _____________________________________
       Pain points: __________________________________
       Opportunities: ________________________________

   Emotion curve:
       ___________________________________________
       ___________________________________________
       
   Peaks identified: _________________________________
   Dips identified: __________________________________
   End matters: _____________________________________

   Interventions for peak-end / dips:
       1. _____________________________________________
       2. _____________________________________________
       3. _____________________________________________
```

> **Operational notes:** Four disciplines. (1) Source from real customers, not internal assumptions. The whole point of the journey map is to surface what internal teams don't see; if it's built only from internal views, it inherits the blindness. (2) Plot the emotion curve. Action-only maps miss the experience signal. Emotion reveals where the journey breaks down even when functional process flows. (3) Apply peak-end rule. Average satisfaction matters less than peak emotional moments and ends. Optimization effort should concentrate on these. (4) Segment by persona. One journey map for many customer types collapses meaningful differences. Build per persona; reconcile common moments.
