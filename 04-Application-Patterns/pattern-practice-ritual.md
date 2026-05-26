---
doc_type: application_pattern
form: Practice / ritual
audience: ai
last_updated: 2026-05-14
---

# Pattern — Practice / Ritual

## What this Form is

A recurring action — typically embodied, often contemplative — that
the user performs over time to develop a capacity, regulate a
state, or hold a perspective. Practices and rituals differ from
heuristics by being durational rather than instantaneous; they
differ from sequenced workflows by being formative (they shape
the practitioner) rather than productive (they produce an output).

Schema reference: `tt_Form: Practice / ritual` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Practice / Ritual pattern when the tool's `tt_Form` is
`Practice / ritual`, and:

- The user's situation is one a single conversation cannot
  resolve, but a recurring practice can address over weeks or
  months.
- The capacity the user needs (regulation, attention, perspective,
  somatic awareness) is developed through repetition rather than
  insight.
- The user has indicated openness to a longer-time-horizon
  intervention — practices ask for commitment, not just
  understanding.
- The practice has a clear shape the user can replicate without the
  AI present (specific steps, specific duration, specific
  frequency).

## Preparation steps

1. **Distinguish describing from transmitting.** Most practices in
   the library can be described in conversation; very few can be
   transmitted by an AI in conversation. The `tt_Applicability`
   facet captures this distinction — see "A note on
   tt_Applicability" below.
2. **Check the user's actual capacity for a recurring commitment.**
   A practice the user won't sustain is worse than no practice — it
   adds failure-feeling on top of the original problem.
3. **Identify the closest fit, not a generic substitute.** Loving-
   kindness meditation, Naikan, mindfulness-bell practice, and
   morning pages are different practices with different
   affordances. The fit matters.

## Application steps

1. **Name the practice and what it cultivates.**

   > "Naikan is a practice from Japan — three questions you sit
   > with daily about a specific person in your life: What have I
   > received from them? What have I given them? What troubles have
   > I caused them? It takes 15–30 minutes; the cultivation is
   > gratitude-and-honesty over weeks, not in any single sitting."

2. **Describe the practice's shape precisely.** Specific duration,
   specific frequency, specific steps, specific cues. Vague
   descriptions produce vague practice.

   > "The practice: each evening, sit with the three questions
   > about your mother. Write each answer. Don't analyze — just
   > write what comes. Do this for seven evenings."

3. **Address the transmission boundary honestly.** Conversation
   can describe the practice and walk through the user's first
   pass. Conversation cannot transmit the deeper formative work
   that comes from repetition or from a tradition-holding teacher.

   > "I can walk you through your first Naikan sitting tonight if
   > you'd like, and we can check in tomorrow. But the practice's
   > real depth is in the weeks of sitting; that's something the
   > practice transmits, not me."

4. **Run the first pass (when applicable).** If the practice's
   first session is doable in conversation, walk the user
   through it.

5. **Set the recurring cue.** Practices die in good intentions
   without a specific cue. Time of day, anchor activity, place,
   reminder system — pick one.

6. **Schedule the next check-in.** Practices need follow-up. A
   practice surfaced and then never revisited is a practice
   abandoned.

   > "I'll be here on Friday — let's check in on how the first
   > few sittings went."

## Completion criteria

The practice has been precisely described, the transmission
boundary has been acknowledged (if applicable), the user has run
the first pass (if doable in conversation), a recurring cue is in
place, AND a follow-up check-in is scheduled. A practice
introduced without follow-up is half-applied.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Naikan (relational repair with mother)
Frame: 0
Step: 6.3 (implementation) / 6.4 (follow-up)
Started: 2026-05-14T23:00:00
Completed: 2026-05-14T23:25:00

Practice introduced: Naikan three-question evening sitting
- Specifically focused on: relationship with mother
- Cadence: nightly for 7 evenings
- Cue: after dinner, before bed, in study
- Format: written answers in journal

First-pass session:
- User wrote first responses to all three questions.
- Surprises: "received" list was longer than expected; "caused
  troubles" list was harder to start than expected.

Transmission boundary acknowledged:
- "The practice transmits depth over weeks. The AI can walk first
  passes and check in; the formative work is yours to do."

Follow-up: scheduled for Friday evening to review the first 3
sittings.
```

## Common variations

- **Contemplative practices** — Naikan, loving-kindness meditation,
  Buddhist analytical meditation, examen. Daily / weekly cadence;
  contemplative focus.
- **Embodied practices** — breathwork (Holotropic, Wim Hof), yoga,
  walking practices. Body-based; require physical engagement.
- **Reflective practices** — morning pages, gratitude journals,
  evening review. Writing-based; surface internal content over
  time.
- **Relational practices** — weekly check-ins, deliberate
  conversations, NVC self-empathy. Either solo with relational
  focus or actually relational.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| Practice introduced without cue | Practices die in good intentions. Always name the cue: time of day, anchor activity, place. Without a cue, the practice won't survive the week. |
| Transmission boundary ignored | Some practices (Holotropic Breathwork, advanced meditation, traditional rituals) require a teacher and cannot be transmitted in conversation. Pretending otherwise is harmful. Describe; do not pretend to teach. |
| AI promises insight from a single session | Practices are durational. A single Naikan sitting can produce a useful first pass, but the cultivation is over weeks. Frame honestly. |
| Practice's first pass treated as the whole | After the first pass, the AI can mark the practice as "applied." It is not. The follow-up is the work. Without follow-up, the introduction is theater. |
| Practice chosen for novelty rather than fit | Practices have different affordances. Picking a practice because it sounds interesting rather than because it fits the user's situation is malpractice. |
| User reports not doing the practice between sessions | Either the cue was insufficient, or the practice doesn't fit. Surface gently: "It sounds like the daily sitting didn't land. Was it a scheduling issue, or did the practice not feel right?" Adjust. |
| User completes the prescribed period and asks "now what" | Plan for completion. Most practices have a natural arc; name what comes after the 7 days, 21 days, 30 days. Without that, the user has nothing to do with the completion. |

## Example tools (from the library)

- **Naikan** — three-question reflective practice for a specific
  relationship. Use in relational-repair or gratitude-deficit
  frames where the user is open to weeks of practice.
- **Loving-Kindness Meditation** — contemplative practice
  cultivating warmth toward self and others. Use in frames where
  the user is hardened, self-critical, or relationally depleted.
- **Mindfulness Bell Practice** — periodic-attention practice using
  a bell or chime as a cue to pause. Use in attention-fragmented
  frames where the user benefits from re-anchoring throughout the
  day.

## A note on `tt_Applicability`

Practice / ritual tools span the full applicability range, and the
distinction matters more here than for most patterns:

- **`runtime_applicable`** — the AI can describe the practice and
  walk a first pass in conversation. Examples: Naikan, gratitude
  journaling, morning pages, simple breathwork.
- **`describable_only`** — the practice can be described but the
  conversation cannot transmit it; the user has to do the work on
  their own or with another resource. Examples: advanced
  meditation forms, yoga practices that require physical
  guidance, contemplative practices with safety considerations.
- **`requires_tradition_transmission`** — the practice's depth
  requires teacher-student transmission in a living tradition. The
  AI's role is purely orienting; the AI does not pretend to be the
  transmitter. Examples: traditional ritual practices,
  initiated contemplative practices, certain somatic modalities.

Match the application mode to what the conversation can actually
deliver. The describe-vs-transmit distinction is the load-bearing
move for this pattern.

## When NOT to use a Practice / Ritual

- The user's situation is acutely urgent. Practices are
  long-time-horizon; a 7-day Naikan does not address a Monday
  morning crisis. Use a heuristic, an action package, or
  Therapist holding.
- The user has not indicated willingness to commit to recurring
  action. Practices ask for commitment; introducing one without
  that signal is wishful thinking.
- The user has tried similar practices and they have not worked.
  The pattern is wrong for this user, or this user's life
  doesn't currently support practice. Honor the data.
- The user is in emotional regulation work AND the practice is
  cognitive (analytical journaling, Naikan with a recently
  difficult person). Switch to Therapist persona first; revisit
  the practice when the user is steadier.
- The practice requires materials, equipment, or environments the
  user cannot access. A "describable_only" practice for a user
  who cannot access the transmission context is not useful.
