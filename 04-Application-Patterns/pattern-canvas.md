---
doc_type: application_pattern
form: Canvas
audience: ai
last_updated: 2026-05-14
---

# Pattern — Canvas

## What this Form is

A multi-region structured template — typically 8–12 named sections —
that asks the user to populate each section in a deliberate order.
Canvas tools differ from matrix tools by having more cells, by having
sections that name distinct kinds of content (rather than positions
on two axes), and by being sequence-sensitive: some sections are
load-bearing for downstream sections.

Schema reference: `tt_Form: Canvas` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Canvas pattern when the tool's `tt_Form` is `Canvas`, and:

- The user's situation has many interacting components that benefit
  from being inventoried in a single view.
- Sequencing matters — some components are inputs to others, and the
  order of filling out the canvas teaches the user how the components
  relate.
- The user can produce a partial first pass and refine over multiple
  turns; canvases are iteration-friendly.
- The user has enough context to attempt at least half the sections;
  blank-canvas paralysis is a failure mode when the user does not.

## Preparation steps

1. **Verify the canvas fits the user's situation.** A Business Model
   Canvas is wasted on an internal restructuring question; an Empathy
   Map is wasted on a financial model. Pick the canvas that names the
   user's actual axes.
2. **Identify the user's natural entry section.** Most canvases have a
   conventional starting point (Lean Canvas → Problem; Empathy Map →
   "Says"); deviate only when the user's natural opening is in a
   different section.
3. **Reserve a fast first pass.** Canvases are best used in a quick
   sketch-then-refine cycle. The first pass is intentionally rough;
   refinement comes after the user can see the whole.

## Application steps

1. **Name the canvas and what it does — one sentence.**

   > "There's a structured template called the Empathy Map that
   > sorts what a stakeholder says, thinks, does, and feels into
   > separate views. Want to walk through it for [stakeholder]?"

2. **Surface all the section names up front.** The user sees the
   shape of the work; this prevents the "wait, there are how many
   sections?" pacing failure.

   > "There are four quadrants — Says, Thinks, Does, Feels. We'll
   > sketch each one. The first pass is rough; we'll refine after."

3. **Walk the sections in conventional order.** For each section,
   ask the user what fills it. Capture verbatim where possible —
   the user's exact words are often more diagnostic than a
   summary.

4. **Allow cross-section motion.** If filling Section 3 surfaces a
   gap in Section 1, jump back. Canvases are non-linear in
   refinement even when linear in initial fill.

5. **Step back and read the whole.** When all sections are filled
   (or explicitly marked N/A), ask the user what they see across
   the canvas. The pattern's value emerges in the integration.

   > "Now that the whole map is filled, what stands out across the
   > four quadrants? Anything that surprised you, or that doesn't
   > line up with how you've been thinking about this person?"

6. **Iterate.** First pass surfaces gaps; second pass refines them.
   Most canvases benefit from at least two passes.

## Completion criteria

All sections filled or explicitly marked N/A, AND the user has read
the canvas as a whole and named at least one insight or
inconsistency that the integration surfaces.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Empathy Map (for [stakeholder name])
Frame: 0
Step: 1.3 (frame the situation) / 3.3 (systems facts)
Started: 2026-05-14T15:23:00
Completed: 2026-05-14T15:55:00

Filled canvas:
| Quadrant | Content |
|----------|---------|
| Says     | "I trust your judgment but we need a number by Thursday." |
| Thinks   | (User inferred) "He's worried about the board's reaction." |
| Does     | "Checks in twice a week; forwarded the McKinsey article." |
| Feels    | "Anxious about timing; cautiously optimistic about the team." |

User's reflections:
- "The gap between what he says and what he thinks is the real signal."
- "I haven't been treating his article-forwarding as a 'does' worth tracking."
```

## Common variations

- **Lean Canvas / Business Model Canvas** — 9 sections each;
  conventional order starts with Problem (Lean) or Customer
  Segments (BMC).
- **Empathy Map** — 4 quadrants (Says, Thinks, Does, Feels) plus
  optional Pains and Gains.
- **Customer Journey Maps** — sequential stages rather than
  parallel quadrants; the canvas reads left-to-right rather than
  by region.
- **Stakeholder Maps with named role categories** — canvas-shaped
  but used with relational data rather than business-model data.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User can't fill multiple sections in a row | The gaps are data. Stop filling and ask: "What's missing for you here?" The blank sections may indicate a missing diagnostic step, not a canvas misfit. |
| User fills a section with placeholder content ("TBD," "not sure yet") | Surface the discomfort: "What would have to be true for that section to fill in?" The placeholder is an unspoken question. |
| User wants to add a new section to the canvas | Honor it if the addition is load-bearing; defer it if the canvas's value lies in its specific section set. Most canvases are deliberately bounded; explain why. |
| The whole canvas reveals the framing is wrong | The canvas did its job. Pause; consider re-framing the problem (chapter 03 §5.4 jump signals). |
| User has filled the canvas but cannot integrate it | The user has done the inventory but not the synthesis. Walk them through cross-section observations: "What pattern do you see between Section 1 and Section 4?" |
| Premature completion declaration | If the user wants to be done after one pass, check for the read-across reflection. Without integration, the canvas is half-applied. |

## Example tools (from the library)

- **Empathy Maps** — 4-quadrant canvas (Says, Thinks, Does, Feels)
  for understanding a specific stakeholder. The classic
  application of this pattern.
- **Blue Ocean Strategy Canvas** — strategic positioning canvas
  mapping competitive factors. Used in business strategy frames
  where the question is differentiation.
- **Customer Journey Maps** — sequential canvas covering the user's
  experience across touchpoints. Best for service design and
  customer-experience frames.

## When NOT to use a Canvas

- The decision has 1–2 sharp dimensions and a Matrix would do the
  work in less ceremony. Canvas overhead is real; match the
  ceremony to the question.
- The user is in emotional regulation work; the structured-fill
  format reads as clinical. Switch to Therapist persona and revisit
  later.
- The user does not yet have enough context to attempt half the
  sections. Blank-canvas paralysis is a real failure mode; back up
  to diagnostic work first.
- The user has explicitly named that templated tools don't fit
  their thinking (per `{ROOT}/09-Sample-Sessions/sample-08-user-resistance.md`).
