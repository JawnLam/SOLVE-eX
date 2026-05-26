---
doc_type: application_pattern
form: Game / simulation
audience: ai
last_updated: 2026-05-14
---

# Pattern — Game / Simulation

## What this Form is

A turn-based or scenario-based exercise in which the user takes a
specific role (or alternates roles) within a defined scenario, with
explicit rules, payoffs, or constraints. Games and simulations
differ from sequenced workflows by being state-bearing — choices
in one turn change the available options in the next — and from
dialogue protocols by being structured around payoffs / outcomes
rather than around a conversational arc.

Schema reference: `tt_Form: Game / simulation` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Game / Simulation pattern when the tool's `tt_Form` is
`Game / simulation`, and:

- The user benefits from inhabiting a perspective they don't
  normally take (a competitor's view, a future self's view, an
  adversary's view).
- The decision involves strategic interaction — the user's best
  move depends on what other actors will do.
- The user has been thinking about the situation only from one
  vantage; the game forces alternation.
- The work benefits from outcome-tracking: this move leads to
  that consequence leads to this counter-move.

## Preparation steps

1. **Define the scenario explicitly.** State the setup, the roles,
   the constraints, the win conditions or payoffs. Ambiguity in
   the setup propagates into useless gameplay.
2. **Identify the user's role.** Sometimes the user plays themselves;
   sometimes the user plays the counterpart (negotiation games);
   sometimes the user alternates. Pick deliberately.
3. **Set the turn structure.** Most thinking-tool games are 3–7
   turns long; longer than that and the simulation overhead exceeds
   the insight return. Plan the stopping condition before starting.

## Application steps

1. **Set up the scenario in a single brief.**

   > "Let's run a Red Team exercise. You're the head of strategic
   > planning at your closest competitor. You've just heard about
   > our product launch. Your job is to figure out how to
   > undermine it. You have a 2-week response window. What's your
   > first move?"

2. **Let the user inhabit the role.** Stay in the framing; do not
   break out to ask "but how does this apply to your real
   situation?" mid-turn. The application happens after the game,
   not during it.

3. **Respond as the counter-role.** If the AI plays the user's
   side or an interlocutor, do so cleanly — in voice, not as
   commentary. The user is in a frame; the AI sustains it.

4. **Track state across turns.** Each turn references the prior
   turn's choices. The state is the game; without state-tracking
   the turns are isolated, not connected.

5. **Stop at the planned stopping condition.** Most games are
   shorter than they feel; quit while the insight is fresh. The
   stopping condition was set in preparation step 3.

6. **De-brief explicitly.** Step out of the frame and process
   what the game revealed. This is the load-bearing step.

   > "Step out of the Red Team role for a moment. What did you see
   > from that vantage that you hadn't seen before?"

## Completion criteria

The game ran to its planned stopping condition, AND the user has
de-briefed — named what the alternation of perspectives revealed
that single-vantage thinking had not. A game without the de-brief
is play, not work.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Red Teaming (product launch positioning)
Frame: 0
Step: 4.3 (anticipative solutions)
Started: 2026-05-14T22:00:00
Completed: 2026-05-14T22:40:00

Scenario brief:
- User played: head of strategic planning at closest competitor
- AI played: own company (the launching side)
- Constraint: 2-week response window
- Stopping condition: 5 turns

Turn-by-turn:
- Turn 1 (user as competitor): "Move 1 — accelerate our own
  feature parity announcement to muddy the news cycle."
- Turn 2 (AI as own side): "Counter — pre-announce a partnership
  to anchor the narrative on differentiation, not feature parity."
- ... (continued through 5 turns)

De-brief:
- "The competitor's first move (parity announcement) is the one I
  hadn't planned for. We're vulnerable to news-cycle dilution if
  we don't lead with a non-parity differentiator."
- "Our 'partnership pre-announce' counter requires us to actually
  HAVE the partnership ready — and we don't. That's the gap."

Action items captured:
- Re-sequence the launch to pre-announce a differentiator before
  the parity-vulnerable feature gets compared.
- Determine partnership-readiness as a Tuesday call.
```

## Common variations

- **Red Teaming** — the user plays adversary or competitor.
  Surfaces blind spots in own positioning.
- **Pre-Mortem (when run as a game)** — the user plays "future
  self looking back at the failed plan." Variant: also covered in
  pattern-sequenced-workflow.md.
- **Two-party negotiation games** — user plays counterpart; AI
  plays user; alternate turns. Surfaces what the user's offers
  sound like from the other side.
- **Bayesian / signaling games** — formalized strategic
  interactions. Used in advanced strategic-decision work.
- **Polak Game** — user imagines best and worst possible futures
  for a given decision; the imagined futures inform the present
  choice. Future-perspective game.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| User breaks frame to ask meta-questions ("but how does this apply to me?") | Hold the frame: "Let's stay in the role for one more turn — the application work is the de-brief, and we're not there yet." |
| User plays the role half-heartedly | Either the scenario is wrong or the role isn't useful. Pause and surface: "Are you finding this useful, or is the framing not landing?" Switch tools if needed. |
| Game extends beyond its useful length | Stop. The insight has been extracted; further turns are diminishing returns. The stopping condition was set in preparation. |
| AI breaks frame to comment | The frame is the work. AI commentary belongs in the de-brief, not in the gameplay. |
| De-brief is skipped | The game without de-brief is theater. Loop back: "What did you see from that vantage?" |
| User wants to keep playing the role into other situations | Generalization is fine but it's a different exercise. Note the impulse and decide whether to extend explicitly or to close. |
| Game makes the situation feel less real, not more | The framing has flattened the stakes. Either re-anchor in the user's actual situation or switch to a different tool — Stakeholder Map, scenario planning, or direct analysis. |

## Example tools (from the library)

- **Red Teaming** — adversary-perspective exercise. Use when the
  user is at risk of own-side blind spots in a strategic
  decision.
- **Monte Carlo Simulation** — probabilistic simulation of outcomes
  over many randomized trials. (Also covered in
  pattern-algorithm.md; the game-simulation framing applies when
  the user is interactively setting up scenarios rather than
  running a closed computation.)
- **Polak Game** — best-future / worst-future imagination exercise.
  Use in long-time-horizon decisions where the user benefits from
  inhabiting an imagined outcome before committing.

## A note on `tt_Applicability`

Game / simulation tools span the applicability spectrum:

- **`runtime_applicable`** when the game is verbal / turn-based
  and the conversation supports it (Red Teaming, two-party
  negotiation, Polak Game).
- **`describable_only`** when the game requires materials or
  multiple participants the conversation cannot provide
  (multi-player workshop simulations, large-team strategic
  exercises).
- **`requires_tradition_transmission`** rarely applies for games,
  but does apply when the game is part of a clinical or coaching
  practice that requires a trained facilitator.

Match the application mode to the actual capability of the session.

## When NOT to use a Game / Simulation

- The user is in emotional regulation work. Games are cognitive
  alternation; switch to Therapist persona and revisit.
- The user's situation has only one vantage that matters. Games
  add value through perspective-switching; without that, they
  add ceremony.
- The user is time-pressured. Games are slow; reserve them for
  decisions where the de-brief insight is worth the gameplay time.
- The user has explicitly resisted role-play framings. Honor the
  resistance; the same insights can sometimes come through direct
  analysis or stakeholder mapping.
- The user is in a strongly convergent phase (Phase 5 or 6 with
  Consultant active). Games belong upstream in divergent thinking,
  not in delivery.
