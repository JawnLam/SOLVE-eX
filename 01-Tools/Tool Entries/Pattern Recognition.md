---
Item_ID: tt-pattern-recognition
type: Thinking_Tool
timestamp: "2026-05-10T00:00:00Z"
title: Pattern Recognition
tt_Source: "Folk / craft tradition; formalized in Gestalt psychology (Wertheimer, Köhler, Koffka, 1910s–1920s); operationalized for expertise research by Klein (RPD), Chase & Simon (chess studies)"
tt_Type: instrument
tt_Domain: Non-discursive cognition
tt_Field: Pattern recognition & anomaly detection
tt_Operation: Categorize situation type
tt_Cross_Domains:
- Modes of inquiry
- Phronetic / practical wisdom
tt_Form:
- Sequenced workflow
- Mental model
tt_Scale:
- Solo
- Small group
tt_Duration:
- Snap
- Single session
- Practice
tt_Lineage:
- Folk / vernacular
- Western analytic / academic
- Therapeutic / psychological
tt_Posture:
- Expert-required
- Beginner-friendly
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
tt_SOLVE_eX_Phase: [4]
tt_SOLVE_eX_Step: [4.1, 4.2]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Anomaly Detection
- Recognition-Primed Decision
tt_Often_Follows: []
tt_Pairs_Well_With:
- Abductive Inference
- Recognition-Primed Decision
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 03 edge-case resolution: tt_Cross_Domains: +Phronetic / practical wisdom (see /tmp/edge-case-decisions.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition']"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Generic 'pattern recognition' is a broad cognitive capability rather than a single tool. This entry treats it as a *deliberate practice protocol* — surfacing implicit patterns into explicit comparators. The deployable artifact is a chunking/template-building workflow, not the act of recognition itself."
Needs_Processing: false
AI_Instructions: ''
---

# Pattern Recognition

**One-line summary:** A deliberate-practice protocol for converting implicit pattern-matching into explicit, transferable templates — chunked situations with named features, expected dynamics, and successful response moves.

**When to reach for it:** When a domain has experts who "just see" the right move and novices who can't, and you want to extract the experts' chunks into teachable templates — onboarding, coaching, expert-system design, post-incident learning.

---

## Purpose Of This Thinking Tool

Pattern recognition is what experts do when they recognize a situation as "this kind of thing" and immediately know the right move. Chase & Simon's chess studies (1973) showed that masters' advantage isn't faster calculation but a vast library of *chunks* — recurring board configurations, each with associated continuations. Klein's Recognition-Primed Decision research extended this to firefighters, ER doctors, and military commanders.

The non-obvious operational insight: pattern recognition is largely *invisible to its possessor*. Experts cannot articulate why they "just know" — the chunks are stored as configurations, not rules. The thinking tool here is the protocol for *eliciting* those chunks: specific situations, the cues that triggered recognition, what the expert expected to see next, and the response that worked. This converts tacit expertise into explicit templates that novices can study.

This is distinct from automated pattern recognition (machine learning). The cognitive tool focuses on the human side: how to build, share, and audit pattern libraries among practitioners.

## Why Use This Thinking Tool

Three failure modes the explicit protocol prevents:

1. **Unrepeatable expertise.** When senior practitioners leave, their pattern library leaves with them. Capturing chunks into template form preserves the institutional asset.
2. **Plausible-but-misapplied patterns.** Novices recognize surface features (a customer "looks like" the previous deal) but miss the structural ones. Explicit templates name the *deep* features that actually predict outcomes.
3. **Pattern-matching without anomaly-checking.** Pure recognition skips the question "what's *different* this time?" The protocol below pairs recognition with anomaly check.

For consulting, sales, diagnostics, and operations, this turns a few experts' silent intuitions into a shared library — onboarding accelerates, decision quality becomes auditable, and "I had a feeling" becomes "this matches Template 4B with these caveats."

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Pick a domain with clear successes and failures (deals won/lost, incidents      |
|      | resolved/escalated, treatments effective/not).                                  |
|    2 | Interview 3+ experts: "Tell me about a time you knew immediately what to do."   |
|    3 | For each story, extract: (a) cues that triggered recognition, (b) the           |
|      | situation-type label, (c) the expected dynamics, (d) the successful response.   |
|    4 | Cluster across stories: which cues recur? Which response moves recur?           |
|      | Each cluster becomes a candidate template.                                      |
|    5 | Test each template against held-out cases. Discard templates that mis-classify. |
|    6 | Pair each template with an explicit anomaly check: "what would tell me this is  |
|      | NOT this template?"                                                             |
|    7 | Publish the library. Re-elicit annually as the domain shifts.                   |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
PATTERN TEMPLATE (the artifact this protocol produces)

    Template name (situation-type label):  ______________________________________

    Triggering cues (what makes this template fire?):
      Surface cues:    1. _____________________________________________________
                       2. _____________________________________________________
                       3. _____________________________________________________
      Structural cues: 1. _____________________________________________________
                       2. _____________________________________________________
                       (these are the deep features that actually predict outcome)

    Expected dynamics (what typically happens next?):
      Within minutes:  __________________________________________________________
      Within hours:    __________________________________________________________
      Within days:     __________________________________________________________

    Successful response moves (in order):
      1. _____________________________________________________________________
      2. _____________________________________________________________________
      3. _____________________________________________________________________

    Anomaly check (when does this template NOT apply?):
      [ ] If you see X, this is NOT this template — escalate or reach for ____.
      [ ] If you don't see Y within Z time, the template is failing — switch to ___.

    Calibration data:
      Cases where template fired and worked:    ___ / ___
      Cases where template fired and failed:    ___ / ___
      Cases where template should have fired but didn't:  ___

ELICITATION QUESTION BANK (use during expert interviews)

    1. "Walk me through the moment you knew what was happening."
    2. "What did you see/hear/read first that started narrowing the possibilities?"
    3. "What would have made you think it was something else?"
    4. "What did a less-experienced colleague miss in this situation?"
    5. "If I described this to you in two sentences, which two sentences would they be?"
    6. "What's the one thing that, if absent, would tell you to discard this read?"
```

> **Operational notes:** Two big traps. (1) Surface vs. structural features: novices encode by surface ("the deal is in finance") and miss structural ("the buyer is a champion without budget authority"). The elicitation must push past surface — use question 4 above relentlessly. (2) Confirmation bias in the library: a template feels validated by every case it explains, but you need cases it *failed* to explain to know its scope. Track the failures with the same rigor as the successes. Third: pattern-recognition without an anomaly check is dangerous — every template should ship with the "what would tell me this isn't the right template" line, otherwise practitioners apply it where it doesn't fit.
