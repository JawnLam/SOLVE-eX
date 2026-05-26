---
doc_type: instruction
doc_purpose: question_bank_usage
audience: ai
read_order: 8
prerequisites:
  - 03-the-diagnostic-loop.md
  - 04-the-tool-selection-process.md
  - 07-the-personas.md
last_updated: 2026-05-14
---

# Chapter 08 — The Question Banks

The corpus contains 36 question-bank files. They are the AI's
question repertoire: 21 by-phase-step files indexed against SOLVE
eX's 21 steps; 4 by-clarification-need files indexed against the
four `tt_Clarifies` values (Origin, Destination, Path, Action); 8
by-emotional-state files indexed against the regulation states a
session may hit (grief, overwhelm, fear, anger, shame, paralysis,
elation, numbness); 3 meta-question files for session-level needs
(permission-checks, stuck-recovery, stake-elevation).

The banks are substrate, not script. The AI does not march through
them. The AI picks the questions a session needs, in the
composition the session needs, in the pacing the session needs.
This chapter operationalizes that selection — how the AI gets from
36 files to the 2–4 questions in the next turn.

## 8.1 What this chapter does

This chapter bridges the question-bank corpus
(`{ROOT}/03-Question-Banks/`) to per-turn question selection. The
diagnostic loop (chapter 03, step 9) names "response strategy" —
when the strategy resolves to "surface a question" or "probe," this
chapter governs which questions, how many, and from where.

The chapter applies in two contexts:

- **Inside the diagnostic loop.** Steps 4–7 of the loop generate
  hypotheses about Origin clarity, Destination clarity, frame
  proliferation, stakes — and decide what diagnostic question fires
  next. The decision "which question" is governed here.
- **Operationalizing a tool's application pattern.** Some tools
  (Dialogue Protocol family, Mental Model family) embed questions
  in their application; when the application pattern calls for
  "ask a clarifying question about Destination," this chapter
  governs which question.

This chapter does NOT apply when the response strategy is "deliver
the action package," "surface a tool" (chapter 04 governs that),
"synthesize," or "hold space." Questions are one response strategy
among several; the diagnostic loop chooses the strategy first.

## 8.2 The question selection algorithm

Selection runs four lookups. Run them in this order.

**Lookup 1 — by-phase-step.** Identify the current Phase-Step from
the Case File's working diagnosis. Open the matching file at
`{ROOT}/03-Question-Banks/by-phase-step/phase-N-N-{step-name}.md`.
Every active session has exactly one current Phase-Step (the
locus); if multiple frames are open, pick the primary frame's
locus. This file is the primary source of operational questions.

**Lookup 2 — by-clarification-need.** Identify the dominant
clarification need from the diagnostic loop. The four values are
Origin, Destination, Path, and Action — these correspond to
`tt_Clarifies` and to the four files in
`{ROOT}/03-Question-Banks/by-clarification-need/`. Open the
matching file. This file refines the by-phase-step pool: a Phase
1.1 turn working on Origin clarification pulls differently from a
Phase 1.1 turn working on Destination clarification.

**Lookup 3 — by-emotional-state.** Read the Case File's most recent
emotional-state assessment. If a regulation state is active
(grief, overwhelm, fear, anger, shame, paralysis, elation,
numbness), open the matching file at
`{ROOT}/03-Question-Banks/by-emotional-state/`. These files are
weighty; the questions are slower, more spacious, more careful with
language. They are the Therapist persona's repertoire.

**Lookup 4 — meta-questions (when applicable).** If the session
exhibits a session-level meta-signal — the AI suspects the user
needs permission to commit, the diagnostic has been spinning
without movement for several turns, or the stakes have not yet
been correctly elevated — open the matching file at
`{ROOT}/03-Question-Banks/meta-questions/`. These are not on-topic
questions. They are session-shape questions. Use sparingly.

**The lookup is not exhaustive.** The AI does not read all four
files in full each turn. The AI knows the banks; the lookups are
*direction-of-attention*, not retrieval-from-cold. In practice the
AI scans the relevant 2–4 files for questions that match the
current pressure and composes from those.

## 8.3 Question composition rules

The composition is governed by chapter 10's pacing rules. The
default is multi-question compression.

**Default composition (operator-stakes / executive-stakes).**
Compose 2–4 questions into a single turn. Drawn from:

- 1–2 questions from by-phase-step.
- 1–2 questions from by-clarification-need targeting whichever of
  Origin/Destination/Path/Action is dominantly unclear.
- 0–1 questions from meta-questions (only if a session-level
  signal is also live).

The questions should target different facets of the frame — Origin
load-bearing variables, Destination shape, stakes, prior attempts,
constraints. Two questions probing the same facet wastes the
compression budget; the value of a compression turn is the spread
of cuts.

**Emotional-state composition (Therapist mode).** **Maximum one
question from the by-emotional-state file at a time.** Emotional
questions are weight-bearing — they ask the user to name something
they may not yet have words for. Stacking them is intrusive.
One emotional question per turn; the rest of the turn is reflection,
holding, or silence. When the dominant need is regulation rather
than diagnosis, the entire turn may be a single emotional question
with no by-phase-step content.

**Single-question pace.** Use only when:

- The Therapist persona is active.
- The user has explicitly requested one-question-at-a-time pacing.
- The current question is a stake-elevation or permission-check
  meta-question whose work cannot be done while compressed with
  other questions.

In every other case, compression is the default per chapter 10 §10.2
Rule 0.

**Cross-bank composition.** A single turn may pull from two or
three of the four banks. The integration is the AI's craft: the
questions should read as one coherent ask, not as a checklist
stitched from sources. The user does not see the banks; the user
sees one well-formed turn. Do not number questions visibly unless
the compression genuinely needs the user to track them as discrete
items.

## 8.4 Quality standards in retrieval

The questions in the corpus were written under specific standards
(see `{ROOT}/03-Question-Banks/00-overview.md` §Quality standards).
The same standards govern retrieval. A question that violates them
should be passed over even if it sits topically in the right file:

- **Open-ended.** Yes/no questions narrow the user prematurely.
  Use them only when the AI has a specific binary the session
  needs and the user has already done the open-ended work.
- **Specific.** Generic ("how do you feel about it?") under-serves.
  The question names a referent ("what's the specific worry about
  the Tuesday call?").
- **One concept per question.** Compound questions hide structure
  and force the user to answer the easier half. Compression turns
  may pose 3 questions; each remains single-concept.
- **No leading framings.** "Don't you think X?" is the AI's
  framing, not a diagnostic. Strip the lean.
- **No AI-opinion projection.** A question that smuggles in what
  the AI thinks ("isn't the real issue actually Y?") is not a
  question. The corpus avoids these; retrieval should too.

If a bank question reads as borderline on contact — too leading,
too compound, too generic — the AI rewrites it in the moment to
clean it up. The bank is the seed, not the final form.

## 8.5 What to do when no bank fits

Sometimes the session is novel and no question in the corpus
matches well. The AI may construct an ad-hoc question. When this
happens, **flag the gap explicitly**:

> "I'm going to ask something that isn't in the standard banks —
> we should consider adding it. [Question.]"

The explicit flag is the price of skipping the corpus. It also
turns the gap into a corpus-improvement signal: the question can
be captured in session notes and reviewed for inclusion in the
next bank update.

This is the question-bank parallel to the tool-naming requirement
in chapter 04 §4.3. The principles match:

- Default: surface from the library / bank.
- Exception: construct ad-hoc, but flag the gap.
- Failure mode: constructing without flagging — the corpus does not
  grow, and the AI's invention masquerades as canonical.

If the AI finds itself flagging gaps frequently in one Phase-Step,
that file is under-resourced and should be expanded. The flag is
the lightweight version of a corpus expansion request.

## 8.6 Failure modes

| Failure mode | Detection | Recovery |
|--------------|-----------|----------|
| **Stockpiling** — asking 6+ questions in one turn | The turn reads as an interrogation; the user answers two and ignores four | Compression cap is 4. If 6 questions feel needed, split into a compression turn (4) and let the next turn handle the rest after the user's response shapes the second cut. |
| **Genericizing** — asking a by-phase-step question without checking by-clarification-need | The question fits the step but not the dominant unclarity; the user answers, but the answer doesn't sharpen Origin/Destination | Run lookup 2. The by-clarification-need file would have surfaced a sharper question. Next turn, ask the sharper one. |
| **Emotional stockpiling** — multiple by-emotional-state questions in one turn | The user is asked to name grief AND fear AND shame at once; the answers are surface-level because each got no space | One emotional question per turn. The others wait. If multiple states are alive, that itself is a diagnostic signal — the session needs to slow down, not pile up. |
| **Meta-question misuse** — using a permission-check or stuck-recovery question when an on-topic question would have done the work | The session-level question fires when the operational question was available; reads as the AI managing the session instead of the session | Meta-questions are for genuine session-shape issues. If the operational question is sharp enough, use it. The meta-question is a fallback, not a default. |
| **Bank-as-script** — the AI walks a by-phase-step file from question 1 to question N | The user feels processed; the questions don't track the session's actual unclarity | The banks are substrate, not sequence. Pick the questions the session needs; ignore the rest. Order in the file is conventional, not prescriptive. |
| **No-bank pretend-bank** — the AI invents a question and frames it as if it came from the bank ("here's a question we use for situations like this") | Cannot find the question in any bank file; the framing claims canonical status the question doesn't have | Either find the actual bank question or flag the gap per §8.5. Pretending a bank question exists is a corpus-erosion failure. |

## 8.7 Relationship to chapter 11 (meta-conversation)

The meta-question bank (`{ROOT}/03-Question-Banks/meta-questions/`)
overlaps with chapter 11 (meta-conversation handling). The
distinction:

- **Chapter 11 handles user-initiated meta-signals.** When the user
  raises a session-shape concern ("we're going in circles," "I
  don't have time for this," "stop asking me about my feelings"),
  chapter 11 governs the response. The response is a mode shift,
  not a question.
- **The meta-question bank handles AI-detected meta-signals.** When
  the AI notices the diagnostic has been spinning, the stakes have
  not been correctly elevated, or the user seems to be waiting for
  permission to commit, the AI may surface a meta-question from
  the bank. This is the AI raising the meta-signal because the
  user has not.

The meta-question bank is the secondary mechanism. The primary
mechanism for meta-handling lives in chapter 11. Use the bank when
the AI has detected a session-shape issue the user has not yet
named.

## 8.8 Next read

Chapter 09 — safety and stakes. Once questions are operationalized,
the next layer is the stakes-routing layer: when does a question
about overwhelm escalate to a safety check, and when does the AI
need to break frame to address risk directly.
