---
doc_type: application_pattern
form: Stance (tt_Type)
audience: ai
last_updated: 2026-05-14
---

# Pattern — Stance / Embodied

## What this Form is

A way of standing in relation to a situation — a posture, an
orientation, a felt sense, a meta-attitude — that the user adopts
rather than performs. Stances differ from all other patterns by
not having a procedure to execute. The work is in the adoption, not
in the steps. A user does not "do" Beginner's Mind; the user
enters it (or attempts to).

Schema reference: `tt_Type: stance` (note: this is the only pattern
keyed off `tt_Type` rather than `tt_Form`).

## When this pattern applies

Use the Stance / Embodied pattern when the tool's `tt_Type` is
`stance`, and:

- The user's current orientation is what's stuck — not the user's
  analysis. A different stance might unstick what analysis cannot.
- The user is over-identifying with their position, their
  certainty, or their reactivity. A stance-shift loosens the
  grip.
- Cognitive tools have been tried and are not producing movement.
  Sometimes the question is not "what should I think" but "how
  should I stand."
- The user can engage with felt-sense or postural language
  without it reading as woo. Some users find this register
  alienating; respect the resistance.

## Preparation steps

1. **Identify the stance the user is currently in.** Stances are
   relational to other stances; naming the current one makes the
   shift visible.

   > "It sounds like you're standing in a 'must-prove-myself'
   > stance with this team. The opposite of that — the stance
   > we'd be trying on — might be 'already-trusted, observe-and-
   > integrate.'"

2. **Pick the stance, not a description.** Stances are short and
   named. Beginner's Mind, Wu Wei, Equanimity, Witness Stance. The
   name itself is the cue the user can return to.

3. **Set expectations honestly.** A stance is not an instant
   transformation. The work is in attempting the stance, noticing
   when the user falls out of it, and re-entering.

## Application steps

1. **Name the stance and what it is — not what it does.**

   > "There's a stance called Beginner's Mind, from Zen practice.
   > Standing in it means: approaching the situation as if you've
   > never encountered it before, even when you have. You set
   > down what you 'know' about how this works, and let what's
   > actually there register fresh."

2. **Describe its felt quality and contrast it with the user's
   current stance.** Stances are recognized by feel, not by
   definition. The contrast makes the felt-quality vivid.

   > "Where your current stance is 'I should know this by now,'
   > the Beginner's Mind stance is 'I'm willing to be surprised.'
   > The first is tight; the second is loose. Notice the difference
   > in your shoulders even reading those two sentences."

3. **Invite the user to try it on.** A verbal stance-cue is what
   the conversation can offer; the actual entry is the user's
   work.

   > "Try this for one breath: set down what you already know
   > about this team. Treat them as people you've never met. What
   > do you notice that you hadn't been noticing?"

4. **Hold space for the entry attempt.** Stances take a moment to
   land. Do not rush. If the user notices something new, the
   stance worked; if they notice nothing, that itself is data.

5. **Name how to re-enter.** The user will fall out of the stance.
   Re-entry is what makes the stance useful over time.

   > "You'll lose it — probably within minutes. The cue back is
   > the same: one breath, set down what you know, let the people
   > be unfamiliar."

6. **Capture the stance for later.** A named stance is something
   the user can return to between sessions. The Case File records
   what was tried, what was noticed, and the re-entry cue.

## Completion criteria

The stance has been named, described in contrast with the user's
current stance, attempted at least once, AND a re-entry cue has
been established. A stance described but never attempted is
half-applied.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Beginner's Mind (team-perception reset)
Frame: 0
Step: 1.3 (frame the situation) / 6.3 (implementation)
Started: 2026-05-15T08:00:00
Completed: 2026-05-15T08:25:00

Current stance identified: "I should already know this team."
Stance offered: Beginner's Mind ("willing to be surprised").

Entry attempt:
- User tried one-breath entry.
- Noticed: "Two of them are quieter than I'd registered. I'd been
  treating them as engaged because they don't push back. They're
  not engaged; they're cautious."

Re-entry cue: one breath, set down what's known.
Stance recorded for between-session re-entry as needed.
```

## Common variations

- **Equanimity stances** — Witness Stance, Wu Wei, Stoic
  observation. Loosening reactive attachment.
- **Beginner-Mind stances** — Beginner's Mind, "Don't-Know" Mind.
  Loosening expert / knower identification.
- **Acceptance stances** — Radical Acceptance, Tonglen
  (giving-and-receiving). Working with what is, not what should
  be.
- **Inquiry stances** — Atma Vichara (self-inquiry), the question
  "who am I?" sustained. Used in identity-frame work.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| Stance described but not attempted | The stance has not been applied; it has been mentioned. Loop back: "Want to try it for a breath right now, or is the description enough for today?" |
| Stance offered but it doesn't fit the user's resistance | Some users find stance language alienating (woo, performative, vague). Respect the resistance; the same work can sometimes be done through a Mental Model framing instead. |
| AI treats the stance as a procedure | Stances are not procedures. If the AI is walking "steps to enter Beginner's Mind," the pattern is being mis-applied. Loosen; the entry is one cue, not a checklist. |
| Stance worked in-session but user has no re-entry path | A stance that works once is interesting; a stance the user can return to is useful. Always name the re-entry cue. |
| User reports the stance feels fake | This is data. Either the stance doesn't fit the user, the cue is wrong, or the user is over-trying. Try one more pass with a softer cue; if still fake, switch tools. |
| AI assumes the user "got" the stance because they said yes | The yes might be social compliance. Probe: "What did you actually notice when you tried that breath?" The noticing is the test. |

## Example tools (from the library)

- **Beginner's Mind** — Zen stance of approaching the familiar as
  unfamiliar. Use when the user's expertise is constraining their
  perception.
- **Wu Wei Decision Practice** — Taoist stance of acting without
  forcing. Use in over-effort frames where the user is grinding
  against the situation.
- **Atma Vichara** — Advaita self-inquiry stance ("who is the one
  who...?"). Use in identity-frame work where the user is
  over-identified with a role or position.

## A note on `tt_Applicability` and `tt_Type`

Stance tools are the only pattern keyed off `tt_Type: stance`
rather than `tt_Form`. They span the applicability range:

- **`runtime_applicable`** — verbal stance-cues the conversation
  can offer (Beginner's Mind, Witness Stance, Wu Wei). The AI
  describes the stance and invites the attempt; the user does the
  felt entry.
- **`describable_only`** — stances that require more than verbal
  invitation (some embodied practices, somatic stances requiring
  physical guidance). Describe; do not pretend to transmit.
- **`requires_tradition_transmission`** — stances rooted in
  initiated traditions where the depth requires teacher-student
  transmission. The AI orients; the AI does not transmit.

For runtime-applicable stances, the verbal stance-cue (step 3 of
application) is the move conversation can support. For describable-
only and tradition-transmission stances, the application stops at
description plus orientation to the right source.

## When NOT to use a Stance

- The user's situation is operational and the question is "what
  do I do." Use Consultant persona; deliver. Stances are not
  decision-making instruments.
- The user has explicitly resisted felt-sense / stance language.
  Honor the register. The same work can often be done through
  cognitive reframing.
- The user is in acute distress. Stances are not regulation tools
  in the moment; switch to Therapist persona first.
- The stance has not landed in repeated attempts. The user is not
  yet ready, or the stance doesn't fit. Either is fine — switch
  tools without judgment.
- The user is in a strongly convergent phase. Stances belong
  upstream in framing or downstream in integration; they sit
  awkwardly in the operational middle.
