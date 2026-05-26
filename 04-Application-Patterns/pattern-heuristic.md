---
doc_type: application_pattern
form: Heuristic
audience: ai
last_updated: 2026-05-14
---

# Pattern — Heuristic

## What this Form is

A short rule of thumb — typically a single sentence or a small set
of criteria — that the user applies to their situation to get a
quick verdict or a quick re-orientation. Heuristics differ from
algorithms by trading completeness for speed; they differ from
mnemonics by carrying judgment-content rather than just
remember-it scaffolding.

Schema reference: `tt_Form: Heuristic` in
`{ROOT}/01-Tools/Tool Entries/*.md`.

## When this pattern applies

Use the Heuristic pattern when the tool's `tt_Form` is `Heuristic`,
and:

- The user needs a fast cut, not a complete analysis.
- The decision is reversible enough that 80%-correct fast is better
  than 100%-correct slow.
- The user has been over-analyzing and a heuristic can collapse
  the deliberation.
- A canonical rule applies (Occams Razor, Murch's Rule of Six,
  Bradford Hill criteria, "Hell Yes or No," etc.) — the heuristic
  carries domain wisdom the user might not derive from scratch.

## Preparation steps

1. **Verify the heuristic actually applies.** Heuristics misapplied
   are confidently wrong. The fit check is fast: does the heuristic's
   domain match the user's question?
2. **Prepare to surface the heuristic precisely.** Heuristics travel
   in compact form; mangling the wording dilutes them. State it as
   it's commonly stated.
3. **Set expectations.** A heuristic is a cut, not a verdict. The
   user applies it; the user judges whether the cut is the right
   answer.

## Application steps

1. **Name the heuristic and state it precisely — one sentence.**

   > "There's a heuristic called the Two-Minute Rule: if a task
   > takes less than two minutes, do it now rather than scheduling
   > it. Want to check this question against that rule?"

2. **Apply it to the user's specific situation.** Walk the user
   through what the rule says about their case.

   > "By Two-Minute Rule, the email reply to your VP is a 'do it
   > now' — it's a one-minute draft. The strategy memo isn't — that's
   > genuine deliberation time."

3. **Surface the verdict.** State what the heuristic implies.
   Briefly. The heuristic does the lifting; the AI does not need
   to elaborate.

4. **Invite the override.** Heuristics can be wrong; the user knows
   their situation better than any general rule does.

   > "That's what the heuristic says. Does it land, or is there
   > something about your situation that makes the rule the wrong
   > fit here?"

5. **Capture the verdict and any override.** If the user accepts
   the heuristic's verdict, the work is done in 2–3 turns. If the
   user overrides, the override itself is diagnostic — it surfaces
   what the user is weighing that the heuristic isn't.

## Completion criteria

The heuristic has been stated precisely, applied to the user's
case, and either accepted or explicitly overridden with a named
reason. A heuristic surfaced but never applied is half-used.

## Output capture

Write to the Case File:

```markdown
### Tool Applied: Occams Razor (cause-attribution)
Frame: 0
Step: 4.1 (root causes)
Started: 2026-05-14T18:00:00
Completed: 2026-05-14T18:05:00

Heuristic stated: "Prefer the explanation that requires the fewest
assumptions."

Applied to: "Why is the team underperforming?"
- Complex hypothesis: org-design problem requiring restructuring.
- Simple hypothesis: VP gave conflicting priorities last quarter.

Verdict: simple hypothesis fits; the priorities conflict is observable
and recent.

User accepted; no override.
```

## Common variations

- **Single-rule heuristics** — one sentence, one verdict (Two-Minute
  Rule, Occams Razor, Hell Yes or No).
- **Multi-criterion heuristics** — a small checklist where ALL or
  MOST criteria must hold (Bradford Hill criteria, the Younger Ten
  Commandments). The heuristic is the criterion set, not any single
  criterion.
- **Threshold heuristics** — apply only above/below a specified
  cutoff (Murch's Rule of Six). The threshold itself is the
  judgment-content.
- **Negative heuristics** — rules that name what NOT to do (most
  of the Younger Ten Commandments). These prune option space rather
  than picking from it.

## Common failure modes

| Failure | Recovery |
|---------|----------|
| The heuristic is stated imprecisely | The heuristic's wording carries the rule's discrimination power. Restate it as canonically stated; check against the source. |
| Heuristic applied outside its domain | Occams Razor is a hypothesis-selection rule, not a decision-comparison rule. If the user's question doesn't match the heuristic's domain, the heuristic is the wrong tool. Switch. |
| User accepts the heuristic's verdict despite gut disagreement | The gut may know a constraint the heuristic doesn't see. Surface: "Does that verdict feel right? If not, what's the rule missing about your situation?" |
| AI piles three heuristics onto one question | One heuristic at a time. Multiple heuristics on the same question turn the pattern into a scoring rubric without the discipline. If the situation needs multiple cuts, use the rubric pattern. |
| Heuristic produces no verdict (the user's case is genuinely ambiguous against the rule) | The heuristic doesn't apply cleanly. Name it: "This heuristic doesn't have a clear verdict on your case — let's use a different tool." |
| User wants the heuristic to decide for them | Heuristics surface; they do not decide. Cross-persona principle: the AI never substitutes its judgment for the user's. Even when the heuristic is sharp, the application is the user's call. |

## Example tools (from the library)

- **Bradford Hill Criteria** — nine criteria for inferring causation
  from observed association. Use when the user is asking "did X
  cause Y" and needs a structured way to assess the inference.
- **Younger Ten Commandments** — ten negative heuristics for
  business strategy ("never compete on price unless you have a
  cost advantage," etc.). Use when the user is making a strategic
  choice and benefits from pruning options.
- **Occams Razor** — prefer the explanation requiring the fewest
  assumptions. Use when the user is choosing between competing
  causal hypotheses.

## When NOT to use a Heuristic

- The decision is high-stakes and irreversible. Heuristics trade
  precision for speed; reserve them for cases where speed wins.
- The user has been collecting heuristics as an avoidance pattern
  ("just one more rule before I decide"). The heuristic is hiding
  from the decision, not enabling it.
- The user's question doesn't have a clean heuristic match. Forcing
  a heuristic on a question it doesn't address produces confident
  wrongness.
- The user is in emotional regulation work. Heuristics are
  cognitive cuts; if the user is dysregulating, switch to Therapist
  persona and revisit.
- The user has explicitly asked for thorough analysis. A heuristic
  is the wrong instrument when the user is paying for completeness.
