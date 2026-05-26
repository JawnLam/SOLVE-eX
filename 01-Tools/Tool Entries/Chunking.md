---
Item_ID: tt-chunking
Item_Prototype: Thinking_Tool
Title: Chunking
tt_Source: "George A. Miller, 'The Magical Number Seven, Plus or Minus Two' (Psychological Review, 1956). Extended by Herbert Simon (1974) and the chunking research of Anders Ericsson on expert performance."
tt_Type: instrument
tt_Domain: Symbolic systems
tt_Field: Memory & knowledge architecture
tt_Operation: Decompose hierarchically
tt_Cross_Domains:
- Discursive-analytical
- Modes of inquiry
tt_Form:
- Heuristic
- Mental model
- Practice / ritual
tt_Scale:
- Solo
tt_Duration:
- Snap
- Practice
tt_Lineage:
- Western analytic / academic
tt_Posture:
- Beginner-friendly
- Solo-quiet
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1, 3.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Method of Loci
- Spaced Repetition
- Deep Work
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
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
Quick_Notes: "Working memory holds ~7 ± 2 items (Miller 1956). 'Chunks' are the units; one chunk can be a single letter or an entire phrase, depending on what the learner has consolidated. Expert chess players see board positions as ~5-9 meaningful patterns where novices see ~5-9 individual pieces — same working-memory capacity, vastly different encoded content. Operationally: structuring information into hierarchical chunks dramatically increases what can be held and processed simultaneously."
Needs_Processing: false
AI_Instructions: ''
---

# Chunking

**One-line summary:** A cognitive technique that groups individual items into meaningful units ("chunks"), exploiting the fact that working memory holds a fixed number of chunks regardless of each chunk's content — so chunking transforms what would be unmanageable detail into tractable structure.

**When to reach for it:** Studying complex material, breaking down skills for learning or teaching, designing presentations and documents for retention, organizing information for working-memory load reduction, and any case where the volume of detail exceeds what can be held mentally at once.

---

## Purpose Of This Thinking Tool

George Miller's 1956 paper *The Magical Number Seven, Plus or Minus Two* established that working memory holds approximately 7 ± 2 items at once. Subsequent research (Cowan 2001) tightened the estimate to 4 ± 1 for unambiguous items, but the structural finding stood: **working memory is severely limited in number of items it can hold, but the size of each item can vary enormously.**

This is the basis for **chunking**: grouping individual elements into meaningful units. The same 7-item working-memory limit can hold 7 letters or 7 words or 7 phrases or 7 entire concepts — depending on what the learner has consolidated into chunks.

Examples:

- A novice chess player sees ~7 individual pieces; an expert sees ~7 meaningful patterns (a kingside attack, a pawn structure, a tactical theme). Same working memory; vastly more represented content.
- A novice phone-number remembers 10 individual digits; with chunking, those become 3 chunks: area code, prefix, line number.
- A novice musician reads notes individually; an expert reads phrases.
- A new code-reader processes line-by-line; an experienced engineer reads functions and patterns.

The non-obvious operational insight is that **expertise is largely chunking expertise.** Experts are not faster thinkers; they have larger chunks. Their working memory holds the same number of items as a novice's, but each item contains more consolidated content. This explains why expertise transfers slowly — the chunks must be built through practice; you cannot give them to someone.

A second insight: **chunking is what allows complex tasks to fit working memory.** When learners say "this is too complex, I can't hold it all in my head," they're describing a chunking problem. Restructuring the material into appropriate chunks — often hierarchically, with sub-chunks — makes it tractable. Teaching is largely chunking design: choosing how to group information so it fits in the learner's current chunks while building new ones.

A third insight: **the right chunk size depends on the learner.** What's a single chunk for an expert is many chunks for a novice. Material organized for one audience often fails for another not because the content is wrong but because the chunk structure doesn't match the audience's existing chunks.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The "more detail = more clarity" trap.** Adding detail often makes material harder, not easier, because it overflows working memory. Chunking-aware design strips to essential chunks at the right level for the audience.
2. **The novice / expert mismatch in teaching.** Experts who have large chunks teach in their chunks (which novices don't have); novices then can't follow. The fix is to redesign material in novice-sized chunks, building toward expert chunks gradually. Curriculum design is essentially chunk-progression design.
3. **The presentation overload failure.** Slides crammed with detail exceed audience working memory. The "rule of 7" (or stricter) for slide content is chunking-aware design: limit each slide to fit working-memory capacity.

For consulting, training, and communication work, chunking is the discipline that converts "too much information" into "the right amount of structure."

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify what's being learned, presented, or processed. Estimate the raw item   |
|      | count.                                                                           |
|    2 | Identify the audience's existing chunks. What do they already know that lets     |
|      | them group items? Their existing chunks determine what counts as one item.       |
|    3 | Design hierarchical chunks. Group items into groups of ~5-7. Group those groups  |
|      | into super-groups, and so on, until top level fits in working memory.            |
|    4 | Use meaningful chunk boundaries. Random groupings are fragile; semantically      |
|      | meaningful groupings consolidate into stable chunks faster.                      |
|    5 | Provide chunk labels. Each chunk should have a clear name / identity that the    |
|      | learner can hold while exploring the chunk's contents.                           |
|    6 | Build chunks through practice. Single exposure rarely consolidates a chunk;      |
|      | repeated meaningful use is what makes it durable.                                |
|    7 | For learning: start with smaller chunks, expand as the learner consolidates.     |
|      | For teaching: structure the path from novice chunks to expert chunks.            |
|    8 | For presentations: respect the rule. ~5-7 items at any level. If you have more,  |
|      | sub-chunk.                                                                       |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE CHUNK-DESIGN HIERARCHY

   Top level (5-7 chunks):
       Chunk A
           A1 (5-7 sub-chunks)
               A1a, A1b, A1c, ...
           A2
           A3
       Chunk B
           B1, B2, B3
       Chunk C
       ...

   At any level, the listener / reader / learner is holding ~5-7
   items in working memory. The hierarchy collapses detail into
   tractable structure.

THE CHUNKING-AWARE COMMUNICATION TEMPLATE

   Material: __________________________________________________________
   Total items: _______________________________________________________
   Audience's existing chunks for this domain: _______________________
                  (level of expertise; relevant prior knowledge)

   Top-level chunks (5-7 max):
       1. _______________________________________________________
       2. _______________________________________________________
       3. _______________________________________________________
       ...

   For each top-level chunk, sub-chunks if needed (5-7 max):
       Sub-chunk 1.1: _______________________________________________
       Sub-chunk 1.2: _______________________________________________
       ...

   Test: at any level, can the audience hold the chunks at THIS
   level in working memory? If no, sub-chunk further.

THE EXAMPLES TABLE (chunking transformations)

   Domain               | Raw items     | Chunked structure
   ---------------------|---------------|--------------------
   Phone number         | 10 digits     | Area / prefix / line (3)
   Resume bullet        | 25 words      | What / how / result (3)
   Code function        | 20 lines      | Init / loop / cleanup (3)
   Presentation         | 50 slides     | 5 sections × ~10 slides
   Curriculum           | 200 concepts  | 5 modules × 5 units × 8 concepts
   Software architecture| 50 components | 5 layers × ~10 components
   Sales process        | 30 steps      | 5 phases × ~6 steps each
   Strategic plan       | 20 initiatives| 5 themes × ~4 initiatives

   The pattern: expand the hierarchy until any single level fits
   in working memory.

THE SKILL-CHUNKING APPLICATION (for learning complex skills)

   When learning a complex skill (programming language, instrument,
   sport, profession):

   1. Identify the smallest meaningful unit of practice (a basic
      pattern, a fundamental move, a syntactic primitive).
   2. Practice each unit until it consolidates into a single chunk
      — meaning you can use it without conscious decomposition.
   3. Combine consolidated chunks into larger patterns; practice
      those.
   4. Continue compositing up the hierarchy.

   Anders Ericsson's expertise research identifies this progression:
   experts have 10,000+ chunks consolidated through deliberate
   practice. The chunks are what their working memory operates on.

   Common error: trying to combine before basic chunks are
   consolidated. The combinatorial chunks won't form because the
   sub-chunks aren't yet automatic.

THE TEACHING-DESIGN APPLICATION

   Curriculum design is chunk-progression design:

   Stage 1: Novice chunks (small, concrete, mostly atomic)
       Example for chess: piece moves, basic captures, check.

   Stage 2: Intermediate chunks (combinations of stage-1 chunks)
       Example: tactical patterns (forks, pins, skewers).

   Stage 3: Advanced chunks (high-level patterns)
       Example: strategic concepts (pawn structures, weak squares).

   Stage 4: Expert chunks (entire positions / contexts)
       Example: typical positions and their strategic plans.

   Skipping stages produces students who memorize without
   understanding. Building all stages takes time but produces
   transferable expertise.

THE WORKING-MEMORY OVERLOAD DIAGNOSIS

   Symptoms of working-memory overload in a learner / audience:
       - Confusion despite individual elements being clear
       - Inability to follow complex examples
       - Forgetting earlier steps when reaching later ones
       - Silence in response to "any questions?" — too overloaded
         to formulate questions

   Response: simplify the chunk structure, not the content. Often
   the same content can be re-organized to fit working memory
   without omitting detail.

THE COMMON FAILURE MODES

   1. EXPERT-SIZED CHUNKS FOR NOVICES
        Material organized in expert chunks fails for novices not
        because content is wrong but because chunk size is wrong.
        Fix: re-organize at smaller granularity.

   2. RANDOM CHUNKING
        Arbitrary groupings (page numbers, alphabetical) don't
        consolidate well. Fix: group semantically.

   3. UNLABELED CHUNKS
        Chunks without clear names don't function as units in
        working memory. Fix: name every chunk.

   4. UNIFORM CHUNK SIZE
        Forcing all chunks to be the same size produces unnatural
        groupings. Fix: let chunks be the size their content suggests,
        within the 5-7 limit.

THE STRATEGIC USE FOR ANALYSTS / CONSULTANTS

   When facing a complex problem:

   1. Inventory the items (data points, factors, considerations).
   2. Find natural groupings — semantic, causal, temporal, spatial.
   3. Build the hierarchy: top level fits in working memory; sub-
      levels also fit.
   4. Present at the appropriate level for the audience. Drill
      down on demand.

   The Minto Pyramid Principle (separate entry) is a chunking
   discipline applied to executive communication; the underlying
   cognitive principle is the same.
```

> **Operational notes:** Four disciplines. (1) Chunk size depends on the audience. The same content can be 50 chunks for a novice and 5 chunks for an expert. Match the chunking to the audience's existing chunks; otherwise material that "should be clear" isn't. (2) Hierarchical chunking is what makes complex content tractable. Single-level chunking (a flat list of 30 items) overwhelms working memory; nested chunking (5 groups of 6, or 6 groups of 5) fits. The hierarchy is the design move. (3) Chunks must be meaningful, not arbitrary. Random groupings are fragile and don't consolidate. Semantic groupings (by topic, by stage, by theme) consolidate faster and more durably. (4) Building expert chunks takes deliberate practice. Cannot be transferred wholesale. The implication for skill-building: expect long timelines for expertise; design the chunk-progression carefully; expect that teaching expert content to novices in expert chunks will fail.
