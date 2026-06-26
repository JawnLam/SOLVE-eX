---
Item_ID: tt-spaced-repetition
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Spaced Repetition
tt_Source: Hermann Ebbinghaus's forgetting curve research (1885); Sebastian Leitner's flashcard system (1972); Piotr Wozniak's SuperMemo algorithms (1985 onward); Anki (free, open-source, 2006). Backed by extensive cognitive-psychology research.
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: Memory & knowledge architecture
tt_Operation: Run experimental cycle
tt_Cross_Domains:
- Modes of inquiry
- Inner / psychological work
tt_Form:
- Sequenced workflow
tt_Scale:
- Solo
tt_Duration:
- Practice
tt_Lineage:
- Western analytic / academic
- Mathematical / formal
tt_Posture:
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Building A Second Brain
- Zettelkasten
- Feynman Technique
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
- 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
- '2026-05-08 — post-sprint cleanup: brought facet values into compliance with schema v1.12.0 controlled inventories (Form/Scale/Duration/Lineage/Posture); corrected stance-type miscodings where applicable'
- "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
- "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Schedule reviews of information at increasing intervals (1 day, 3 days, 1 week, 2 weeks, 1 month) — based on the forgetting curve. Counters memory decay efficiently. Anki and similar apps automate scheduling per item based on recall difficulty. Used in language learning, medical school, factual mastery in any domain. Bears compound returns: small daily investment preserves large knowledge bases.'
Needs_Processing: false
AI_Instructions: ''
---

# Spaced Repetition

**One-line summary:** A memory technique — grounded in Hermann Ebbinghaus's forgetting-curve research — that schedules reviews at increasing intervals (matched to predicted forgetting), efficiently maintaining factual knowledge with small daily investment via tools like Anki.

**When to reach for it:** Language learning (vocabulary, kanji); medical / professional licensing exams (huge factual loads); domain mastery in any factual field; long-term retention of ideas you don't want to lose; building durable knowledge that stays accessible without re-learning; and any context where the forgetting curve is the enemy and small consistent investment can defeat it.

---

## Purpose Of This Thinking Tool

**Spaced repetition** schedules information reviews based on the forgetting curve. The structure:

1. **Encode** — create a flashcard, question-answer pair, or other recall prompt for what you want to remember.
2. **Review at increasing intervals** — first review after 1 day; if recalled, next after 3 days; then 1 week, 2 weeks, 1 month, etc.
3. **Adjust based on recall** — if you fail to recall, reset to short interval. If you recall easily, lengthen further.
4. **Compound** — over months and years, large knowledge bases get maintained with minutes per day.

The non-obvious operational insight is that **memory decays predictably; spacing reviews to match the decay curve is far more efficient than re-reading.** Ebbinghaus showed that without reinforcement, memory drops sharply within days. Standard re-reading at fixed intervals (e.g., daily review) wastes effort on already-strong memories. Spaced repetition reviews each item just before it would be forgotten — efficient and durable.

The practical implementation:

- **Anki** (free, open-source) is the dominant tool. It uses an algorithm derived from SM-2 (SuperMemo) to schedule each card individually based on recall ratings.
- **Cards** typically have a question on the front, answer on the back. You see the front, attempt recall, then check the back. You rate the recall quality (Again / Hard / Good / Easy); the algorithm schedules the next review accordingly.
- **Daily practice** is the discipline. Even 15 minutes/day maintains thousands of cards.

A second insight: **the technique compounds dramatically.** A daily 15-minute practice maintains 5,000-10,000 cards over years. The cumulative effect: massive durable knowledge for small ongoing investment. Comparable to a financial annuity — small payments over time produce large balance.

A third insight: **the framework requires good cards.** Bad cards (vague questions, multiple-information cards, poorly-formed prompts) make practice frustrating and unhelpful. The "20 rules of formulating knowledge in learning" by Wozniak provides guidance: keep things simple, atomic, specific, contextualize.

A fourth insight: **the framework excels for facts; less well for skills.** Spaced repetition maintains memory for factual knowledge — vocabulary, formulas, names, dates, definitions. It's less directly applicable to procedural skills (riding a bike, writing well) which require deliberate practice instead. Use the right tool for the type of learning.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "study hard then forget" cycle.** Cramming produces short-term recall and fast forgetting; spaced repetition produces durable knowledge.
2. **The "re-reading inefficiency" trap.** Repeated reading wastes effort on strong memories; scheduling matched to decay is far more efficient.
3. **The "knowledge attrition" problem.** Things learned but not maintained slip away; spaced repetition keeps them accessible long-term.

For language learners, medical students, scholars, professionals in factual fields, and anyone whose work depends on durable factual mastery, spaced repetition is foundational technique.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Choose a tool (Anki recommended).                                                |
|    2 | Identify what you want to remember durably. Specific factual / definitional   |
|      | content.                                                                          |
|    3 | Create cards. Each card: one question, one answer, atomic.                      |
|    4 | Review daily. The algorithm schedules; you just do today's queue.              |
|    5 | Rate recall honestly (Again / Hard / Good / Easy).                              |
|    6 | Add new cards as you encounter new material. Don't add too many at once       |
|      | (~10-20/day is sustainable).                                                     |
|    7 | Refine cards that aren't working. Bad cards → frustration; reformulate.        |
|    8 | Continue indefinitely. The compound benefits are over years, not weeks.         |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FORGETTING CURVE

   Without reinforcement:
       Day 0: 100% recall
       Day 1: ~70%
       Day 3: ~50%
       Day 7: ~30%
       Day 30: ~10%

   With spaced reviews matched to the curve:
       Each successful review pushes the next to longer
       intervals.
       Memory remains accessible with minimal review.

THE SCHEDULING ALGORITHM (simplified)

   For a card:
       New card → Review tomorrow
       Tomorrow:
           Recalled easily → Review in 3 days
           Recalled with difficulty → Review in 1 day
           Failed → Reset to today; review again
       3 days later (if successful):
           Recalled easily → Review in 7 days
           ...
       Each successful review approximately doubles
       the interval (with adjustments).
       Each failure resets to a short interval.

   Anki's SM-2 algorithm refines this with per-card
   ease factors learned from your history.

THE CARD-DESIGN DISCIPLINE

   Wozniak's principles for good cards:

   1. ATOMIC
      One fact per card. "What is X?" not "What is X
      and how does it work?"

   2. SPECIFIC
      Avoid generic prompts. "What's the capital of
      France?" beats "What is Paris's role?"

   3. UNAMBIGUOUS
      Question has one clear answer.

   4. CONTEXTUALIZED
      Provide enough context that the question is
      meaningful.

   5. PERSONAL
      Relate to your experience or domain when
      possible.

   6. ACTIVE
      Force recall, not recognition. Open-ended
      better than multiple-choice.

   7. CLOZE-DELETION FOR FACTS-IN-CONTEXT
      "{{c1::Paris}} is the capital of France."

   Bad cards are frustrating and unhelpful;
   reformulating is part of the practice.

THE WORKED EXAMPLE — LANGUAGE LEARNING

   Goal: 2000-word vocabulary in Spanish.

   Setup:
       Anki with Spanish-English cards.
       Add 20 new cards/day.
       Review daily.

   Year 1:
       Day 1: 20 new + 0 review = 20 cards
       Day 30: 20 new + ~80 review = 100 cards
       Day 365: 0 new (or fewer; vocabulary acquired)
       + ~200 review at various intervals
       
   Time investment: ~15-20 min/day.
   Result: 2000 vocabulary words durably retained.

   Without spaced repetition: cramming produces
   short-term recall; words slip away over weeks.

THE COMPOUND-RETURN PATTERN

   Spaced repetition's value compounds over time:

   Year 1: build base of 1000-2000 cards
   Year 2: add to base; maintain via daily review
   Year 5: 10,000+ cards maintained durably

   Daily investment: 15-30 min/day.
   Result: massive durable knowledge.

   Comparable to financial compound interest: small
   regular contributions produce large eventual
   balance.

THE PROCEDURAL-VS-FACTUAL DISTINCTION

   Spaced repetition excels for:
       Vocabulary
       Definitions
       Formulas
       Names
       Dates
       Specific factual associations

   Spaced repetition is weak for:
       Procedural skill (writing, sport, music
       performance)
       Conceptual understanding (read about it
       differently)
       Creative judgment
       Tacit knowledge

   Use spaced repetition for facts; use deliberate
   practice for skills. Different tools for different
   learning types.

THE COMMON FAILURE MODES

   1. NO DAILY PRACTICE
        Skipping days; backlog grows; abandoning.
        Recovery: daily ritual; small daily amount.

   2. BAD CARDS
        Vague, ambiguous, multi-fact cards. Recovery:
        reformulate; apply Wozniak principles.

   3. ADDING TOO MANY
        Adding 50/day; can't sustain. Recovery: 10-20
        max; quality over quantity.

   4. DISHONEST RATINGS
        Marking "Easy" to avoid review; defeats the
        algorithm. Recovery: honest self-assessment.

   5. WRONG-DOMAIN APPLICATION
        Using for procedural skill or tacit knowledge.
        Recovery: deliberate practice instead.

   6. PERFECTIONIST CARD-MAKING
        Spending hours per card; never reviewing.
        Recovery: rough cards; refine on review if
        problematic.

   7. ABANDONMENT
        Stopping after weeks; cards decay. Recovery:
        commit to long-term; the compound benefits
        are over years.

THE OPERATIONAL TEMPLATE

   Goal: ______________________________________________
   Domain: ____________________________________________

   Tool: ______________________________________________

   Card-creation discipline:
       New cards/day target: _____________________
       Card formation principles: ________________

   Daily review:
       Time slot: ______________________________
       Duration: ______________________________
       Honesty: rating reflects actual recall

   Maintenance:
       Refine bad cards as encountered
       Don't add too aggressively
       Long-term commitment

   Progress check at 6 months: _________________
   Progress check at 12 months: ________________
```

> **Operational notes:** Four disciplines. (1) Daily practice. The technique requires consistency; skipping days creates backlog and abandonment. Small daily amount (15 min) is sustainable indefinitely; large irregular bursts aren't. (2) Card design matters. Bad cards make practice frustrating and unhelpful. Atomic, specific, unambiguous; reformulate when cards aren't working. (3) Honest self-rating. The algorithm depends on accurate recall ratings. Marking "Easy" to avoid future review defeats the system. (4) Match to learning type. Spaced repetition excels for factual knowledge; for procedural skills and tacit knowledge, deliberate practice is the right tool. Use the right framework for the type of learning.
