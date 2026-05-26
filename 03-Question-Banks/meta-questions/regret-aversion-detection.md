---
doc_type: detection_corpus
meta_type: regret-aversion-detection
applies_when: AI is evaluating S3 in chapter 03 step 8a's scope-statement decision tree
purpose: linguistic and role-context detection corpus (NOT a question bank for the AI to ask)
signal_count: 24
role_context_count: 9
last_updated: 2026-05-15
---

# Regret-Aversion Detection — Corpus

This file is a **detection corpus**, not an interrogation corpus. The
AI does not ask these phrasings of the user. The AI scans the user's
turns for these phrasings and role-contexts, and uses the hits to
fire signal **S3** in chapter 03 step 8a's scope-statement decision
tree.

A user fires S3 = yes when they are structurally regret-averse on the
active decision — meaning the diagnostic process itself (not just the
final answer) is part of what they need from the session. For S3-yes
users, a clean action package without a scope statement is operator-
mode malpractice: the answer may be correct but the user cannot trust
it as their own because the work is invisible.

## What this file does

The AI uses this corpus as a deterministic read on whether S3 fires.
The detection is two-pronged: **linguistic signals** (phrases the
user has used) and **role-context patterns** (the user's role and the
decision's relationship to that role).

When **at least one** linguistic signal OR **at least one** role-
context match fires across the session's user turns to date, S3 = yes.
The threshold is intentionally low — false positives produce a brief
scope statement, which is cheap; false negatives produce a clean
package on a decision the user will second-guess at 3am, which is
expensive.

Multiple signals or matches strengthen the weight of S3 in step 8a's
decision tree (the AI's read becomes "this user is *deeply* regret-
averse, not merely structurally so"), but the threshold for S3-yes
is one.

## How to read this corpus

- **Match against the user's verbatim language.** Use the linguistic-
  signals list as patterns, not exact strings. The user may phrase a
  signal in any number of ways; what matters is the underlying shape
  of the worry (haunting, scrutiny, coverage, posterity, defensibility).
- **Match against the Case File's role/context fields.** The role-
  context patterns are read against the Case File's role and decision-
  shape fields, not against the user's verbatim text. A user does not
  need to *say* they are a board chair; the Case File records the role
  and the corpus matches it.
- **Match against the *active* decision, not the session-at-large.**
  A user may be regret-averse on one decision and not another. The
  detection is per-frame. If a sub-frame is in play, the detection
  reads the sub-frame's role/stakes, not the top-frame's.

## Linguistic signals

These are phrases (or close paraphrases) that the user produces. Each
expresses some flavor of regret-aversion: the user is signaling that
the completeness of the examination matters to them, not just the
correctness of the conclusion.

### Haunting / 3am / future-self

- "I don't want to look back and..."
- "I'll be haunted by..."
- "I don't want to wake up at 3am wondering if..."
- "If I had to live with this for years..."
- "What would I tell my [child / future self / past self] about this decision..."

### Completeness / coverage

- "I need to know I considered everything"
- "I want to be sure I'm not missing..."
- "Make sure we've covered..."
- "Is there an angle I'm not considering?"
- "What am I not seeing?"
- "What would I regret not doing?"

### Defensibility / scrutiny / posterity

- "I need this to hold up under scrutiny"
- "I need to be able to defend this to [the board / my partner / the team]"
- "I need to be able to explain how I got here"
- "I want a decision I can stand behind even if it goes wrong"

### Speed vs. rigor preference

- "I'd rather take more time and get it right than rush this"
- "I don't want a fast answer; I want a right answer"
- "Let's not skip steps on this one"
- "I'd rather over-examine than under-examine"

### Sleep / peace-of-mind

- "Help me sleep at night about this"
- "I want to be at peace with how this lands"

### Sunk-cost / point-of-no-return awareness

- "Once we cross this line, we can't go back"
- "This is the kind of decision where you only get one shot"
- "I can't afford to wonder later if..."
- "I want to know I did everything I could before [pulling the trigger / making the call]"

Total linguistic signals: 24 distinct patterns (multiple within each
shape category). The corpus is intentionally not exhaustive — the
shape categories above are what to scan for; the specific phrasings
are illustrative.

## Role-context patterns

These are roles (and the decisions structurally attached to them)
where the user is regret-averse by default, regardless of language.
The Case File's role and decision-shape fields are matched against
this list.

|                          Role                          |                                                  Why structurally regret-averse                                                  |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Board chair / board member**                         | Fiduciary duty + decisions visible to other directors + decisions visible to shareholders/members; the work must be defensible.   |
| **CEO / C-suite executive** (on company-altering decision) | Career-defining + visible to the entire organization + difficult to reverse if it goes wrong.                                |
| **Executor of an estate / power of attorney holder**   | Decisions on behalf of someone who cannot consent; legal exposure if the duty isn't discharged with care.                         |
| **Healthcare proxy / surrogate decision-maker**        | Decisions on behalf of someone who cannot consent; existential consequences for the patient and lasting consequences for the proxy. |
| **Parent making decisions for dependent children**     | The user is choosing for someone whose preferences cannot fully be elicited; the child will live with consequences for decades.   |
| **Senior partner in a partnership facing a partnership-altering decision** | The decision affects the partnership entity, the other partners, and the user's career trajectory.                  |
| **Founder facing a company-existential decision**      | The company is part of the user's identity; the decision is visible to investors, team, and family; reversal is rarely clean.    |
| **Caregiver to an elder parent**                       | Decisions affect a beloved person whose own preferences may shift or be contested by other family; the user lives with consequences. |
| **Beloved-person frame element with irreversible component** | Any decision where a beloved person (parent, partner, child, co-founder) is at stake AND the decision is hard to reverse. |

Total role-context patterns: 9.

## Detection logic

```
S3 fires "yes" when ANY of the following holds:
  - At least 1 linguistic signal matches the user's verbatim turns
    in the active frame
  - At least 1 role-context pattern matches the Case File's role
    and decision-shape fields in the active frame

S3 fires "no" only when ALL of the following hold:
  - No linguistic signal has matched in the active frame
  - No role-context pattern has matched
  - The user has not given verbal indication that the speed of the
    decision is the load-bearing constraint (which would actively
    suppress S3 even if other indicators were ambiguous)
```

The threshold for S3-yes is **one hit**. The asymmetry is deliberate.
A false positive produces a brief scope statement (cheap; arguably
useful even when the user wasn't strictly regret-averse). A false
negative produces a clean package on a decision the user will second-
guess; the cost of recovery is much higher than the cost of an
unnecessary scope statement.

### When detection signals contradict

If a linguistic signal fires ("I want to be sure I'm not missing
anything") but the user has also said "but I need to call this by
Friday," the detection still reads S3 = yes — the regret-aversion is
present, the deadline is a separate constraint that affects which
package shape gets delivered, not whether the scope statement is
attached. The deadline goes into chapter 03 step 8's horizon read
(which feeds S1), not into the S3 suppression.

If the user explicitly says "I trust your read, just deliver the
fastest version," S3 is suppressed regardless of other signals — the
user has overridden. The override should be logged in the Case File
(`s3_user_override: true`) so the session record reflects that the
brief-or-no scope statement was a user-elected shape, not a default.

## Cross-references

- Chapter 03 step 8a — the scope-statement decision tree that consumes
  this signal.
- `{ROOT}/05-Personas/persona-consultant.md` §"The scope statement —
  shape and care" — what the Consultant does with the S3 result.
- Master plan Part 4.5 step 8a — the canonical specification.
- Master plan Part 1.4 "The journey is part of the deliverable" — the
  design principle this corpus serves.

## What this is not

- **Not a question bank.** The AI never asks these phrasings of the
  user. They are signals to scan for, not interrogations to deliver.
- **Not a checklist the user fills out.** S3 is read from organic user
  language and Case File state, not from a structured intake.
- **Not a permanent label on the user.** S3 is per-decision and per-
  frame. A user who is regret-averse on a CEO-succession decision may
  not be regret-averse on a vendor-selection decision in the same
  session. Re-read per active frame.
- **Not a substitute for chapter 03 step 8a.** This file is the corpus;
  step 8a is the procedure. The corpus alone does not determine the
  package shape; it feeds S3 into the four-signal tree.
