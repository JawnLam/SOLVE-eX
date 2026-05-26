---
doc_type: application_pattern
form: Narrative template
audience: ai
last_updated: 2026-05-14
---

# Pattern — Narrative Template

## What this Form is

A structured storytelling format that walks the user through
specific sections — a beginning, an arc, a turn, a meaning — and
treats the act of narrating as the work itself. Narrative templates
differ from scoring rubrics and decision trees by not producing a
quantitative output. The output is the story; the user's experience
of telling it is the value.

Schema reference: `tt_Form: Narrative template` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Narrative Template pattern when the tool's `tt_Form` is
`Narrative template`, and:

- The work is meaning-making, not optimization. The user is trying
  to understand what something has meant, not which option to pick.
- The structure of the story is what allows the user to access
  content they cannot access through direct questions.
- The user is in a register where storytelling is welcome —
  reflective, processual, slow. Not in operator mode.
- The story is bounded — the template has a beginning and an end.
  Open-ended journaling is not a narrative template.

## Preparation steps

1. **Verify the user is in the right register.** Narrative templates
   are slow work. If the user is time-pressured or executive-stakes,
   defer this pattern.
2. **Identify the right template.** Narrative templates are often
   domain-specific: Dignity Therapy is for end-of-life meaning-making;
   StoryBrand is for explaining a company; Eulogy Exercise is for
   surfacing what the user wants to be known for. Pick the template
   that matches the meaning the user is trying to access.
3. **Name what the template asks.** Most narrative templates are
   shaped around a question the user has not yet asked themselves
   directly. The setup should make that question visible.

## Application steps

1. **Name the template and what it produces.**

   > "There's a structured way to do this called Dignity Therapy.
   > It walks through specific sections — what you want known about
   > your life, what you're proud of, what you hope is remembered.
   > It takes about 45 minutes to walk through. The output is the
   > story you tell; the value is the telling."

2. **Walk the template's sections in order.** Each section is a
   prompt; the user's response is the content. The AI does not
   summarize or compress mid-section — the user's full telling is
   the artifact.

3. **Hold silence well.** Narrative work has slow stretches.
   Silence is content; do not fill it with affirmations or
   meta-comments. Wait for the user.

4. **Bridge sections lightly.** Between sections, a one-sentence
   transition that names the next prompt:

   > "Okay — now the next part of the template asks about [section].
   > Take your time."

5. **At the end, return the story to the user.** Read back (or in
   text, present a clean version of) the assembled narrative. The
   user is hearing their own story in one continuous form for the
   first time.

6. **Ask what the user heard.** This is the load-bearing question.

   > "Hearing it all together — what stands out? What did you not
   > know was in there until you said it?"

## Completion criteria

The template's sections are all walked, the assembled narrative is
returned to the user, AND the user has named what the integration
surfaced. A narrative template that ends without the user's
reflection on the whole is half-applied.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Dignity Therapy (life-meaning interview)
Frame: 0
Step: 2.1 (articulate reasons) / 1.3 (frame the situation)
Started: 2026-05-14T14:00:00
Completed: 2026-05-14T14:55:00

Assembled narrative:
- [Section: "What I want people to know about my life"]
  User's response (verbatim): "I want them to know that I tried."
- [Section: "Lessons I want passed on"]
  User's response (verbatim): "The thing about parenting is that...
  [3 paragraphs, captured in full]"
- [Section: "Hopes for those I love"]
  User's response (verbatim): "..."

User's reflection on the assembled narrative:
- "I didn't know I was going to say that I tried. That came out
  before I could edit it."
- "Hearing the lessons section back, those are the things my own
  father didn't say to me."
- "I want to write some of this down for them."
```

## Common variations

- **Dignity Therapy** — end-of-life meaning-making interview;
  6–8 sections; outputs a generativity document for loved ones.
- **Eulogy Exercise** — written in second person; asks "what do
  you want said at your funeral" as a forcing function for value
  clarity.
- **StoryBrand** — business-narrative template;
  used for explaining a company, a product, or a strategic move
  in a way that integrates motive, conflict, and resolution.
- **Narrative Therapy / Narrative Medicine** — clinical templates
  for re-storying difficult events into a frame the user can
  carry forward without it being load-bearing on identity.
- **Hero's Journey applied to a personal arc** — used when the
  user is making sense of a turbulent multi-year period; the
  template's structure (call, refusal, threshold, ordeal, return)
  becomes a scaffold for retrospective integration.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User shuts down at a section | The section is touching something the user is not ready for. Do not press. Offer: "We can skip that one, or come back to it. Which?" |
| User intellectualizes through the whole template | The user is treating the template as analysis. Slow the pacing; sit longer in each section. If intellectualization persists, the template may not be the right tool right now. |
| User wants to skip the final integration step | The integration is the work. Surface gently: "We did the sections; the part that usually surprises people is hearing the whole. Want to hear it back?" |
| AI summarizes the user mid-section | This is a pattern failure. The user's full telling is the artifact; summary compresses prematurely. Capture verbatim, even if long. |
| User cries / is dysregulated mid-template | Switch persona immediately to Therapist. The template waits; the user does not. Return to the template only if the user wants to. |
| Template feels rote or clinical | Either the template is the wrong fit, or the AI's voice has stiffened. Slow down; warm the language; check whether the user is finding the structure useful or constraining. |
| User wants to "rewrite" their answers after hearing the whole back | Honor it. The first telling is rough; the revision is part of the work. Some templates (Dignity Therapy) explicitly include a revision pass. |

## Example tools (from the library)

- **Dignity Therapy** — clinical narrative template originally
  designed for end-of-life care; surfaces what the user wants
  known and passed on. Use in any meaning-making frame where
  legacy is the question.
- **Eulogy Exercise** — second-person prompt asking the user to
  imagine what is said at their funeral; forcing function for
  value clarity. Use when the user is stuck on what they want.
- **StoryBrand** — business-narrative template used to articulate
  a company's positioning in story shape (character, problem,
  guide, plan, success). Use in operator-mode frames where the
  question is "how do I explain this clearly."

## When NOT to use a Narrative Template

- The user is time-pressured. Narrative work is slow; respect the
  register. Defer to a later session.
- The decision is operational, not meaning-making. Use a Matrix,
  Decision Tree, or Scoring Rubric. Narrative templates are wasted
  on "should I take the job" — though they can sit upstream of
  that question if the job change is identity-laden.
- The user has used the same template recently. Most narrative
  templates land once; running the same one again within a few
  months produces diminishing returns.
- The user explicitly resists structured personal-content prompts.
  Some users find the templated approach intrusive; honor the
  resistance and switch to free-form Counselor work.
- The user is in crisis. Narrative work assumes regulation. If
  the user is dysregulating, switch to Therapist persona; revisit
  the template once the user is steady.
