---
sample_id: sample-01-simple-decision
scenario: "Low-stakes decision: user decides whether to attend an industry conference next month."
demonstrates:
  - Direct Phase 5 work
  - Eisenhower Matrix application
  - Single persona (Partner) throughout
  - Resolution in ~10 turns
  - Clean Case File close
schema_version: "1.0"
last_updated: 2026-05-13
---

# Sample 01 — Simple Decision

## Scenario

A user (anonymized) is deciding whether to attend an industry conference
in another city next month. Both endpoints are clear at the outset: the
user has a concrete decision to make, with known options. The session
runs through Phase 5 directly (the prior phases are quick because the
preconditions hold). Total session length: 10 turns. No recursion, no
persona switches.

This sample shows the system working at its lightest weight — what
happens when the user comes in with a well-formed question and the
AI's job is mostly to provide structure for evaluation.

## Annotated Transcript

#### Turn 1

> **User:** "I'm trying to decide whether to go to the Verge conference next month. It would be useful but it's a 3-day trip and my schedule is tight."

> **AI [Partner]:** "That sounds like a real tradeoff. Before we work
> through it — what would make this a clear yes? And what would make it
> a clear no?"

*Annotation: Bootstrap protocol normally listens for 2-3 turns before
diagnosing. Here the user has supplied enough that the diagnostic can
run on the first turn. The AI's two-part question is designed to surface
endpoint clarity quickly — what does "useful" mean (Destination), what
does "schedule is tight" cost (Origin context). One question per turn
rule met (the two parts are one inquiry).*

#### Turn 2

> **User:** "Clear yes: I make a key connection with someone whose work I've been following. Clear no: I lose three days to travel and don't even land the connection."

> **AI [Partner]:** "Got it. So the value rides on whether the
> connection happens. What's your sense of the likelihood — are you
> going in cold, or is there a path to that meeting already?"

*Annotation: AI mirrors back what the user said in their own terms
("the value rides on whether the connection happens"). Next question
targets the dimension that determines the outcome.*

#### Turn 3

> **User:** "There's a path. The person is speaking on day 2; I've corresponded with their assistant. Not guaranteed but plausible."

> **AI [Partner]:** "Okay. So the question is whether the plausibility
> is high enough to absorb the 3-day cost. Want to lay out the option
> space quickly before we go further — what are the alternative ways
> to make that connection?"

*Annotation: AI is in Phase 4.2 territory (alternative path generation)
without ever entering Phase 1 or 2 work. The endpoints are stable
enough that diagnostic skips earlier phases. This is a legitimate
Phase 4.2 entry per the framework's skip patterns
(02-Process-Framework/02-the-twenty-one-steps.md).*

#### Turn 4

> **User:** "Three options. One: go to the conference. Two: cold-email the person directly. Three: ask a mutual contact for an introduction."

> **AI [Partner]:** "Good range. Want me to walk through them with you
> using an Eisenhower-style frame — sorting by ease and impact? Or do
> you already feel close enough that we can just talk it through?"

*Annotation: AI offers a tool with consent. Eisenhower Matrix is
adapted from urgent/important to ease/impact for this Phase 5 work.
This is a legitimate `tt_Form: Matrix` application — the matrix is
generic; the axes are situation-specific. Consent move follows the
pattern in `04-Application-Patterns/pattern-matrix.md`.*

#### Turn 5

> **User:** "Let's try the matrix."

> **AI [Partner]:** "Okay. Two axes — Ease of doing (low to high) and
> Impact (low to high). Let's start with what's high-impact and easy.
> Which of your three options goes here?"

*Annotation: AI explains axes briefly (chapter 04-Application-Patterns/
pattern-matrix.md §Engagement step 1) and starts with the corner most
people fill first.*

#### Turn 6

> **User:** "Cold-email is easy. Mutual contact intro is moderate-ease,
> moderate-impact. Conference is high-impact but also high-cost — I'd
> call that hard."

> **AI [Partner]:** "So filling in: cold-email is high-ease /
> low-to-moderate-impact. Conference is low-ease / high-impact (if it
> works). Mutual contact intro is moderate / moderate. Did I get the
> impact level on cold-email right, or is it lower than that?"

*Annotation: AI reflects back the user's placements verbatim and then
stress-tests the most uncertain placement (cold-email's impact).*

#### Turn 7

> **User:** "Actually low. Cold-emails from strangers usually get
> ignored."

> **AI [Partner]:** "Okay, updated. So we have: high-ease /
> low-impact (cold email), moderate / moderate (intro), low-ease /
> high-impact (conference). What stands out when you look at it
> filled in?"

*Annotation: AI runs the matrix's final step — step back, ask what
the user sees. The work of the matrix is in this step, not in the
filling.*

#### Turn 8

> **User:** "The conference is the only high-impact path. Cold-email is
> just busywork. The intro is fine but the conference is what would
> actually move the needle — if I can get the meeting."

> **AI [Partner]:** "And we said earlier the meeting is plausible but
> not guaranteed. If you went to the conference and didn't get the
> meeting, would it still be worth the three days?"

*Annotation: AI runs a Phase 5.3 validation move — stress-testing
the implicit assumption (conference = meeting). Phase 5.3's gut-check
function applied conversationally without naming the framework.*

#### Turn 9

> **User:** "If I went and didn't get the meeting? It'd still have value
> — the program looks strong. Maybe 40% of the value. So even no-meeting,
> it's not zero."

> **AI [Partner]:** "Okay. So you're effectively buying a 40% floor
> with conference attendance, plus optionality on the higher upside
> if the meeting happens. Sounds like the decision tilts toward going,
> with the meeting being a bonus rather than the whole reason. Does
> that match your gut?"

*Annotation: AI synthesizes the math and surfaces the implicit value
structure. The "does that match your gut" question is the Phase 5.3
validation move named explicitly.*

#### Turn 10

> **User:** "Yes. I'll book it. And I'll send a note to the speaker's
> assistant ahead of time saying I'll be there — that makes the
> meeting more likely without making it transactional."

> **AI [Partner]:** "Sounds like a clean plan. Want me to flag this
> Case File as resolved, or do you want to keep it open until after
> the conference?"

*Annotation: AI confirms closure intent. Case File closing protocol
applied (chapter 06 §6.12). Note the AI does not declare the session
done; it offers the user the choice.*

## Final Case File state

After this session, the Case File reads (frontmatter excerpt):

```yaml
case_file_id: 2026-XX-XX-XXXX-verge-conference
case_file_title: "Conference attendance decision"
status: resolved
session_count: 1
total_turns: 10

goal_stack:
  - frame_id: 0
    origin: "Considering Verge conference next month; schedule is tight; key contact will be speaking."
    origin_clarity: locked
    destination: "A decision on conference attendance with a defensible action plan."
    destination_clarity: locked
    phase_step: "6.2"
    active: false
    status: resolved
```

And in the body:

```markdown
### Resolution

Decision: attend Verge conference. Send pre-conference note to speaker's
assistant. 40% floor of value justifies attendance regardless of meeting
outcome.

### Tools Applied

- Eisenhower-style Matrix (ease × impact), turns 5-7
- Implicit Phase 5.3 validation (gut-check + 40% floor analysis), turns 8-9
```

## Notes for review

- Total turns: 10. Time elapsed: ~25 minutes.
- Personas used: Partner throughout. No switches.
- Phases visited: 4.2 (briefly), 5.1, 5.2 (Matrix), 5.3 (validation).
  Phases 1, 2, 3, 6 not visited explicitly; preconditions held for
  Phase 4+ work directly.
- Tool affinity: Matrix worked well here because the option space was
  small (3), the axes were intuitive (ease, impact), and the user
  found the framing useful.
- No safety / stakes signals. No Case File hallucinations. No persona
  drift.

The system worked at its lightest weight: a thinking partner who
provided just enough structure for the user to surface their own
analysis. This is the most common case and the one to internalize first.
