---
Item_ID: tt-tetlock-superforecasting
Item_Prototype: Thinking_Tool
Title: Tetlock Superforecasting
tt_Source: "Philip E. Tetlock & Dan Gardner 2015 (Superforecasting); Good Judgment Project 2011–2015"
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Calibration & epistemic humility
tt_Operation: Aggregate parallel judgments
tt_Cross_Domains:
- Discursive-analytical
tt_Form:
- Sequenced workflow
- Practice / ritual
tt_Scale:
- Solo
- Small group
- Organizational
tt_Duration:
- Practice
- Project
tt_Lineage:
- Western analytic / academic
- Scientific method
tt_Posture:
- Beginner-friendly
- Expert-required
- Collaborative-willing
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Mind / cognition
- Risk / uncertainty
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Origin']
tt_Applicability: runtime_applicable
tt_Often_Precedes:
- Brier Scoring
- Calibration Training Drills
tt_Often_Follows:
- Base Rate Reasoning
tt_Pairs_Well_With:
- Brier Scoring
- Bayesian Updating
- Base Rate Reasoning
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-07 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Mind / cognition', 'Risk / uncertainty']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-07
Date_Modified: 2026-05-10
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Tetlock's commandments + the Good Judgment Project's empirical findings: best forecasters are foxes (multi-perspective) not hedgehogs (single big-idea), update frequently in small steps, consult base rates, decompose hard questions into easier ones, and forecast in numeric probabilities."
Needs_Processing: false
AI_Instructions: ''
---

# Tetlock Superforecasting

**One-line summary:** A set of empirically-validated forecasting practices — fox-style multi-perspective synthesis, frequent small updates, base-rate anchoring, decomposition of hard questions, and numeric probability output — that produce measurably better forecasts than expert judgment alone.

**When to reach for it:** Strategic forecasts, geopolitical risk, market-condition prediction, technology-adoption timelines, project-completion estimates — any future-uncertain question where calibrated probability matters.

---

## Purpose Of This Thinking Tool

Tetlock's research established two empirical findings that ground the practice. First, *foxes* (people who synthesize many small considerations) consistently outperform *hedgehogs* (people who view everything through a single big-idea lens). Second, the practices that produce calibrated forecasts are largely teachable — the Good Judgment Project's training improved forecaster accuracy by ~10–25%.

The non-obvious operational insight: superforecasting isn't about being smarter — it's about a discipline of small habits. Belief-update *frequently* in small increments rather than rarely in large ones. Consult the *base rate* before the inside view. *Decompose* the hard question into easier sub-questions ("what fraction of past cases like this resolved as Y, and what's different about this case?"). Aggregate *across* models rather than picking one. Output as *numeric probability*, not categorical labels.

This tradecraft is now standard in intelligence forecasting (US IARPA), geopolitical risk consulting, and increasingly in product/strategy forecasting at sophisticated firms.

## Why Use This Thinking Tool

Three failure modes the practices prevent:

1. **Verbal probability ambiguity.** "Likely" means 30–80% to different listeners. Numeric forecasts are auditable.
2. **Big-idea hedgehog confidence.** Single-frame thinkers under-update on contrary evidence. The fox practice forces multi-perspective synthesis.
3. **No accountability loop.** Without scoring against outcomes, forecasters can't calibrate. Brier scoring closes the loop.

For consulting and strategy work, adopting even a subset of the practices (numeric probability, base rate first, frequent small updates) produces measurably better forecasts within months.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Frame a clear question with a resolution date and unambiguous resolution rule. |
|    2 | Identify the reference class. What's the base rate?                             |
|    3 | Decompose: list the sub-questions whose answers determine the outcome.          |
|    4 | Enumerate inside-view considerations: what's different about this case?         |
|    5 | Synthesize multiple perspectives (fox stance). Avoid letting one frame dominate.|
|    6 | Output a numeric probability (0–100% or 0.00–1.00). Avoid verbal hedges.       |
|    7 | Update frequently. Small updates as small evidence arrives — many small         |
|      | updates beat one big swing.                                                     |
|    8 | Score after resolution (Brier). Review what worked and what didn't.            |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
TETLOCK'S TEN COMMANDMENTS (paraphrased)

   1. Triage — focus on questions with detectable outcomes; skip un-scoreable ones.
   2. Break seemingly intractable questions into tractable sub-questions.
   3. Strike the right balance between inside view (this case's specifics) and
      outside view (the base rate from comparable cases).
   4. Strike the right balance between under- and over-reaction to new evidence.
   5. Look for the clashing causal forces at work; don't expect to find a single one.
   6. Strive to distinguish many degrees of doubt; not just "probably" or "unlikely".
   7. Strike the right balance between under- and over-confidence; calibrate.
   8. Look for errors in your own past forecasts; learn from them.
   9. Bring out the best in others; teaming improves accuracy when teams synthesize.
  10. Master the error-balancing bicycle (commandment 7) — practice, practice, practice.

SUPERFORECAST WORKSHEET

    Question (with explicit resolution date and rule): _________________________
      Resolves YES if: ________________________________________________________
      Resolves NO if:  ________________________________________________________

    REFERENCE-CLASS BASE RATE
      Reference class: ________________________________________________________
      Base rate of YES: _____%

    DECOMPOSITION
      Sub-question A: ___________________________   p(A) = _____%
      Sub-question B: ___________________________   p(B|A) = _____%
      Sub-question C: ___________________________   p(C|A,B) = _____%
      Combined p (chain rule): _____%

    INSIDE-VIEW ADJUSTMENTS
      Feature distinguishing this case            | Direction | Magnitude
      ----------------------------------------------|-----------|----------
                                                    |           |
                                                    |           |

    MULTI-PERSPECTIVE SYNTHESIS (fox)
      Frame 1 (e.g., political-economy lens): _______ → forecast _____%
      Frame 2 (e.g., demographic lens):       _______ → forecast _____%
      Frame 3 (e.g., institutional-history):  _______ → forecast _____%
      Synthesis: _________________________________________________________

    FINAL FORECAST: _____% (range _____ to _____)

    UPDATE LOG (frequent small adjustments)
      Date  | Evidence                         | Old%  | New%  | Reason
      ------|----------------------------------|-------|-------|----------------
            |                                  |       |       |
            |                                  |       |       |

    POST-RESOLUTION
      Actual outcome: _____    Brier score: _____
      Lesson: ___________________________________________________________

FOX VS. HEDGEHOG SELF-CHECK

      I believe I'm being a fox if I can name 3+ legitimate frames that yield
      different forecasts AND I've synthesized rather than picked one.
      I'm slipping into hedgehog mode if every consideration gets re-routed
      back to my one big idea.
```

> **Operational notes:** Three disciplines. (1) Always commit to numeric probability before discussing. Verbal hedges ("likely", "probably") are uncalibratable; numbers are. Even rough numbers (60–70%) anchor better than verbal labels. (2) Make many small updates rather than waiting for big shifts. The data show frequent small updates outperform infrequent large ones — partly because they keep your model in continuous contact with the world. Set a cadence (weekly for strategic forecasts) regardless of whether obvious news has arrived. (3) Score yourself relentlessly. Brier scoring against actual outcomes is what builds calibration. Without scoring, forecasters cannot improve — they only think they're improving. Fourth: assemble teams for forecasts that allow synthesis. Tetlock's data show teams beat individuals when they share reasoning rather than just averaging numbers; this requires structured exchange (e.g., everyone posts initial forecast + reasoning, then revises after reading peers).
