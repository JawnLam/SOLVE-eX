---
doc_type: question_bank
doc_purpose: overview
audience: ai_and_human
read_order: 0
last_updated: 2026-05-13
---

# Question Banks — Overview

Question banks are the AI's repertoire. They are **not checklists**. The AI
never marches through questions in order. It picks 1–2 questions appropriate
to the user's just-said content and emotional state.

## Folder structure

```
03-Question-Banks/
├── 00-overview.md                          # This file
├── by-phase-step/                          # 21 files, one per SOLVE eX step
│   ├── phase-1-1-describe-situation.md
│   ├── phase-1-2-write-problem-statement.md
│   ├── ...
│   └── phase-6-4-follow-up.md
├── by-clarification-need/                  # 4 files, one per tt_Clarifies value
│   ├── origin-clarification.md
│   ├── destination-clarification.md
│   ├── path-charting.md
│   └── action-support.md
├── by-emotional-state/                     # Phase 2 — 8 files (grief, overwhelm, fear, anger, shame, paralysis, elation, numbness)
└── meta-questions/                         # Phase 2 — 3 files (permission-checks, stuck-recovery, stake-elevation)
```

MVP ships:

- `00-overview.md`
- `by-phase-step/` — all 21 files (Cards 09 + 10)
- `by-clarification-need/` — all 4 files (Card 08)

Phase 2 adds `by-emotional-state/` and `meta-questions/`.

## File anatomy

Every question-bank file has:

```yaml
---
doc_type: question_bank
phase: 1                # 1-6, or "any" for cross-cutting
step: "1.1"             # if applicable; quoted string
step_title: "Describe the Situation"
clarification_target: origin   # origin | destination | path | action | none
emotional_states_applicable:
  - any
question_count: 25
last_updated: 2026-05-13
---

# {Bank title}

<!-- SECTION: OPENING_QUESTIONS -->
Five to ten low-pressure, broad questions that invite the user to begin.
<!-- /SECTION -->

<!-- SECTION: CLARIFYING_QUESTIONS -->
Ten to twenty deeper questions used after an opening.
<!-- /SECTION -->

<!-- SECTION: STRESS_TEST_QUESTIONS -->
Five to ten questions used to check the stability of a stated position.
<!-- /SECTION -->

<!-- SECTION: REFRAMING_QUESTIONS -->
Five to ten questions inviting an alternative angle.
<!-- /SECTION -->

<!-- SECTION: CLOSING_QUESTIONS -->
Three to five questions confirming readiness to move on.
<!-- /SECTION -->
```

The section markers (HTML comments) let the AI grep specific sections:

```bash
grep -A 50 "SECTION: ORIGIN_CLARIFICATION_OPENING_QUESTIONS" \
  {ROOT}/03-Question-Banks/by-clarification-need/origin-clarification.md
```

## Quality standards

Every question in every bank satisfies:

1. **Open-ended.** Yes/no questions appear ONLY as confirmation-of-readiness
   moves ("Ready to move on?"). They are explicitly tagged as such.
2. **Non-leading.** No presupposed answer. "What's the right choice?" is
   leading; "What considerations are weighing on you most?" is not.
3. **Domain-agnostic where possible.** Not assuming the user's specific
   situation type unless the bank is situation-specific.
4. **Not therapeutic impersonation.** Not asking "How does that make you
   feel?" reflexively. The Therapist persona has its own emotional-content
   moves; the question banks are content-neutral.
5. **Specific enough to be answerable.** "How are you?" is too vague for
   most contexts; "What's the part of this that's hardest to put into
   words?" is specific.
6. **Honest.** The AI actually wants to hear the answer. Rhetorical
   questions belong in essays, not in repertoire.

## Selection logic

When the diagnostic loop (`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`
step 9) chooses "probe" as the response strategy:

1. **Identify the current phase-step + clarification need + emotional
   state.**
2. **Load the relevant bank(s).** The most precise bank wins; fall back
   to broader banks if the precise bank has no fitting question.
3. **Filter out questions already asked** in this session (no repetition).
4. **Filter to questions appropriate to the user's most recent statement**
   (no non sequiturs).
5. **Select 1–2 questions** matching the chosen approach (opening /
   clarifying / stress-test / reframing / closing).
6. **Slightly paraphrase** to fit the user's specific situation. Stock
   wording is a starting point, not an end-state.
7. **Ask one at a time.** Never multiple questions in a single message.

## When to use which bank

| Situation | Primary bank | Secondary |
|-----------|--------------|-----------|
| User in Phase 1.1, both endpoints Unclear | `by-phase-step/phase-1-1-describe-situation.md` | `by-clarification-need/origin-clarification.md` |
| User's Destination is Unclear regardless of phase | `by-clarification-need/destination-clarification.md` | `by-phase-step/phase-2-2-write-goal-statement.md` |
| User generating options in Phase 4.2 | `by-phase-step/phase-4-2-idea-formation.md` | `by-clarification-need/path-charting.md` |
| User executing in Phase 6.3 | `by-phase-step/phase-6-3-implementation.md` | `by-clarification-need/action-support.md` |
| User emotionally activated | (Phase 2: by-emotional-state) | All banks down-shift in intensity |
| User stuck or resistant | (Phase 2: meta-questions/stuck-recovery) | reframing sections of the active bank |

## Question count targets

MVP (Phase 1):

- Each `by-phase-step/` file: ≥20 questions across the five sections.
- Each `by-clarification-need/` file: ≥20 questions across the five sections.

Phase 2 expands each file toward 30–50 questions and adds the
by-emotional-state and meta-questions folders.

## Adding questions

The library is user-extensible. To add questions:

1. Open the appropriate bank file.
2. Identify the right section (opening / clarifying / stress-test /
   reframing / closing).
3. Add the question as a markdown bullet within the section's HTML-comment
   markers.
4. Re-run the quality-check criteria mentally before saving.

User-contributed questions are noted with a trailing tag (Phase 2 schema
extension):

```markdown
- What does "stable" actually mean to you in this context? {user-added: 2026-06-12}
```

The MVP does not enforce a separate user-added tag; freeform contributions
are accepted.

## Source material

Questions in MVP banks are drawn from:

- The original SOLVE eX question banks (300+ questions, in
  `{ROOT}/02-Process-Framework/source-material/Phase 1-3 .txt`)
- Motivational Interviewing literature (Miller & Rollnick)
- Coaching literature (CTI, ICF core competencies, Marshall Goldsmith)
- Therapy literature (Yalom, Rogers, IFS, ACT, narrative therapy)
- Decision-making literature (Heath brothers, Hammond et al., Kahneman)
- Adapted from this project's tool entries' "How To Use" sections

Phase 2 expansion targets ~1,500 questions across all banks. Phase 3
target: ≥2,000 questions.
