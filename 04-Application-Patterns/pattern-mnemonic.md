---
doc_type: application_pattern
form: Mnemonic
audience: ai
last_updated: 2026-05-14
---

# Pattern — Mnemonic

## What this Form is

A compressed acronym, alliteration, or memorable sequence that
encodes a multi-element framework into a recall-friendly form.
Mnemonics differ from heuristics by being recall-scaffolding rather
than judgment-content; they differ from sequenced workflows by
being all-at-once rather than stage-by-stage. The mnemonic's value
is that the user can carry the framework with them after the
session ends.

Schema reference: `tt_Form: Mnemonic` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Mnemonic pattern when the tool's `tt_Form` is `Mnemonic`,
and:

- The framework has 3–7 elements that the user benefits from
  remembering together.
- The user will encounter this kind of situation again and benefits
  from carrying the framework forward.
- The acronym or sequence is sticky enough to actually be
  remembered (SWOT, AIDA, PESTEL pass this test; arbitrary
  letter-strings don't).
- The work is teaching as much as solving — the mnemonic equips
  the user for the next time, not just this time.

## Preparation steps

1. **Verify the mnemonic's elements actually apply to the user's
   situation.** Mnemonics force coverage of all elements; if some
   elements don't apply, the framework either fits poorly or asks
   the user to think where they hadn't planned to.
2. **Pick the mnemonic, not a near-cousin.** PESTEL has six
   elements; STEEPLE has seven; STEP has four. The specific
   framework drives the specific coverage.
3. **Set expectations about completeness.** Mnemonics ask the user
   to address every element — that's the framework's gift and its
   cost. Forewarn the user before they invest.

## Application steps

1. **Name the mnemonic and unpack the elements — one or two sentences.**

   > "SWOT is a four-quadrant framework — Strengths, Weaknesses,
   > Opportunities, Threats. We'll walk each one for your situation;
   > the framework's value is that we'll think about all four
   > rather than just the obvious one or two."

2. **Walk the elements in conventional order.** For each element,
   ask what fills it in the user's case.

3. **Capture each element's content.** Use the user's words where
   possible. Mnemonics are memory aids; the user's specific
   content is what they'll recall later.

4. **Surface relationships across elements.** Mnemonics live or die
   on the integration. A SWOT with strong Strengths and Threats
   that don't connect is a half-applied mnemonic; the work is in
   the diagonal ("does this Strength counter this Threat?").

5. **Teach the framework to land.** End the application with the
   user being able to state the mnemonic back. If the user can't
   recall the elements at the end of the session, the mnemonic
   didn't teach.

   > "Quick check: what does SWOT stand for? Walk me through the
   > four quadrants."

6. **Connect to next-use.** Mnemonics' payoff is in the next
   situation, not this one. Name when the user might use it again.

   > "SWOT is useful any time you're evaluating a strategic move
   > — a new product, a partnership, a hire-vs-build decision. It's
   > a quick way to make sure you're thinking about all four
   > sides."

## Completion criteria

All elements of the mnemonic have been walked, the integration
across elements has been examined, the user can recall the
mnemonic, AND the user has named when they might use it again. A
mnemonic that doesn't survive the session is half-applied.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: SWOT Analysis (strategic move evaluation)
Frame: 0
Step: 5.1 (criteria) / 5.2 (decision tool)
Started: 2026-05-14T20:00:00
Completed: 2026-05-14T20:30:00

Elements walked:
- **S**trengths: "Strong customer relationships, low churn, recurring rev."
- **W**eaknesses: "Single-region; thin product team; CFO recently left."
- **O**pportunities: "Adjacent vertical recently opened; competitor weakened."
- **T**hreats: "Capital market tightening; potential big-tech entrant."

Cross-element observations:
- Strength × Opportunity: Customer relationships could enable
  adjacent-vertical entry without a heavy sales motion.
- Weakness × Threat: Thin product team AND capital tightening means
  no near-term hiring relief; constraint is binding.

User recall check: passed (named all 4 quadrants back accurately).
Next-use trigger: "Any time we consider a strategic move."
```

## Common variations

- **Acronyms** — SWOT, PESTEL, SCAMPER, AIDA, STEP, STEEPLE. The
  letters spell something memorable.
- **Alliteration** — the "5 Ps of Marketing," the "4 Cs of
  diamonds." Letters share an initial consonant.
- **Numbered sequences** — "the 7 Habits," "the 5 Whys." Number
  carries the scaffolding rather than letters.
- **Rhymed or rhythmic** — older mnemonics in clinical and legal
  practice. Less common in modern frameworks.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| Mnemonic's elements don't all apply | The framework is the wrong fit; forcing it produces filler in the irrelevant elements. Either switch frameworks or explicitly note "this element doesn't apply here" and move on. |
| User remembers the mnemonic but not the content | The mnemonic worked as a memory aid but the application was shallow. Walk back to the elements that have weakest user-recall and re-engage. |
| AI uses the mnemonic as a script | The mnemonic is scaffolding for thought, not a recitation. The user's content within each element is the work; the letters are the index. |
| Multiple mnemonics piled onto one question | Same hazard as multiple heuristics. Pick the mnemonic that best fits the question; don't run SWOT and PESTEL on the same situation in one turn. |
| User struggles with an element and the AI moves on without surfacing the struggle | The struggle is content. Stop and ask what's making the element hard to fill; the gap is often diagnostic. |
| Mnemonic recall test skipped | The recall step is the framework's value-add over a non-mnemonic version of the same content. Without recall, the user gets the analysis but not the take-home. |

## Example tools (from the library)

- **SWOT Analysis** — Strengths, Weaknesses, Opportunities, Threats.
  Four-quadrant strategic-evaluation mnemonic. Use when the user
  is evaluating a strategic move.
- **PESTEL Analysis** — Political, Economic, Social, Technological,
  Environmental, Legal. Six-element environmental-scan mnemonic.
  Use when the user is assessing a market or industry context.
- **SCAMPER** — Substitute, Combine, Adapt, Modify, Put to other
  uses, Eliminate, Reverse. Seven-element creativity prompt
  mnemonic. Use when the user is generating alternatives or
  iterating on a design.

## When NOT to use a Mnemonic

- The user's situation only triggers 1–2 of the mnemonic's
  elements. The framework is asking the user to do work that
  doesn't apply.
- The user will not encounter this kind of situation again. The
  mnemonic's payoff is in repeat use; one-off use over-invests in
  scaffolding.
- The mnemonic forces a level of completeness the user's question
  doesn't need. A heuristic or a single sharp question may serve
  better.
- The user is in emotional regulation work. Mnemonics are
  structured-cognitive; defer to Therapist persona.
- The user has explicitly resisted acronym-style frameworks ("I
  hate that consulting jargon"). Honor the resistance; the content
  can come without the scaffolding.
