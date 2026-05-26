---

Item_ID: tt-galtons-ox
Item_Prototype: Thinking_Tool
Title: Galton's Ox
tt_Source: Francis Galton, 'Vox Populi' (Nature, 1907) — the original ox-weight observation. James Surowiecki, The Wisdom of Crowds (2004) — modern synthesis. Scott Page, The Difference (2007) — diversity-prediction theorem.
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Strategic & game-theoretic reasoning
tt_Operation: Aggregate parallel judgments
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Algorithm
- Heuristic
tt_Scale:
- Small group
- Large group
- Organizational
tt_Duration:
- Snap
- Single session
tt_Lineage:
- Western analytic / academic
- Industrial / business
tt_Posture:
- Beginner-friendly
- Collaborative-willing
tt_State: []
tt_Agent:
- Crowd / market
- Solo human
tt_About:
- Strategy / competition
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Prediction Markets
- Tetlock Superforecasting
- Anonymous Voting
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Agent backfill: added 'Crowd / market'"
  - 2026-05-08 — initial classification (Phase 3, schema v1.12.0)
  - 2026-05-08 — filename + Title + Item_ID updated to restore apostrophe punctuation
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Strategy / competition']"
Tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: 'Galton observed (1906 country fair) that the median of 787 estimates of an ox''s slaughtered weight (1198 lb) was within 1% of the actual (1207 lb). The mechanism: independent errors cancel; the wisdom is in the aggregation, not the individuals. Conditions for the effect: independence (no anchoring on others), diversity (different perspectives / information), aggregation method (median / mean), and decentralization (no one has full information). Surowiecki''s four conditions remain the operational checklist.'
Needs_Processing: false
AI_Instructions: ''

---

# Galton's Ox

**One-line summary:** When independent estimates from a diverse crowd are aggregated (typically by median or mean), the aggregate is often more accurate than any individual estimate — because uncorrelated errors cancel, leaving the underlying signal.

**When to reach for it:** Estimating quantities (effort, cost, duration, market size), forecasting events with uncertain outcomes, calibrating expert opinions against a broader sample, and any case where independent judgment from many people can be collected and aggregated cheaply.

---

## Purpose Of This Thinking Tool

In 1906, Francis Galton attended an English country fair where 787 attendees paid sixpence to guess the weight of an ox after slaughter. The actual dressed weight was 1,198 lbs. Galton, a statistician and (notoriously) a believer in the inferiority of the masses, expected the average guess to be wildly off. The median guess was 1,197 lbs — off by less than 1%. Even the mean was within 1% of the truth. Galton reported the result in *Nature* (1907) as "Vox Populi" and spent the rest of the paper trying to explain why his expectations had been wrong.

The mechanism is statistical. Each individual guess contains the underlying signal (some sense of how much an ox weighs) plus error (idiosyncratic personal bias, lack of information, distraction). If errors are uncorrelated across individuals, they cancel out in aggregation; the signal remains. With enough independent estimates, the aggregate converges toward the truth.

James Surowiecki's *The Wisdom of Crowds* (2004) named four conditions under which the effect holds:

1. **Diversity** — participants have different information, backgrounds, perspectives
2. **Independence** — participants form their estimates without seeing others' answers
3. **Decentralization** — participants draw on local knowledge; no central coordination
4. **Aggregation** — there must be a mechanism to combine estimates into a single answer

The non-obvious operational insight: **the wisdom is in the aggregation, not in the individuals.** Most participants individually are wrong. The crowd is right because the mechanism by which it aggregates causes errors to cancel. Removing the aggregation (asking only the most confident participant, or letting participants discuss before answering) destroys the effect.

A second insight from Scott Page's *Diversity Prediction Theorem* (2007) is mathematical:

> Crowd error = Average individual error − Diversity of estimates

This means: **adding diversity to a crowd reduces the crowd's collective error even if it doesn't improve any individual's accuracy.** Diversity isn't a soft virtue here; it's an algebraic component of the error formula. A crowd of skilled-but-similar experts can be less accurate than a diverse crowd of less-skilled individuals, because the diversity term is large.

The single most common failure mode is **dependence contamination** — participants seeing each other's answers, group discussion before anonymous estimates, or social-status pressure that makes some answers heard louder than others. All of these collapse the variance among estimates, which kills the aggregation effect.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The expert-deference trap.** Single-expert estimates (the most senior engineer's effort estimate, the head of sales' revenue forecast) are systematically miscalibrated — overconfident, anchored, slow to update. A simple wisdom-of-crowds protocol (collect independent estimates from 5-10 informed participants, take the median) typically beats the single expert.
2. **The "we discussed it and agreed on 12 weeks" failure.** Groups that discuss before estimating produce less accurate aggregates than groups that estimate independently and then aggregate. Discussion creates dependence; the wisdom-of-crowds effect requires independence.
3. **The narrow-crowd failure.** A "crowd" of ten people who all work in the same department, share the same training, and read the same trade publications is not a crowd in the relevant sense — they share too much information for their errors to cancel. Diversity is a structural requirement, not a stylistic preference.

For consulting and operational forecasting (project effort, market sizing, headcount needs), the discipline is small but powerful: collect independent written estimates from a diverse group, take the median, and treat that as the working estimate. Improvements over single-expert or post-discussion-consensus estimates are typically 10-30% in error reduction.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Define the question precisely. Quantitative is best (a number, a date, a         |
|      | probability). Vague questions don't aggregate well.                              |
|    2 | Identify a diverse pool of informed participants — at least 5, ideally 15+.      |
|      | Diversity matters more than individual expertise.                                |
|    3 | Collect estimates INDEPENDENTLY. Each participant submits without seeing other   |
|      | participants' answers. Written submissions, anonymous polls, or sealed envelopes |
|      | all work; group discussion does not.                                             |
|    4 | Aggregate. Take the median (more robust to outliers than mean). For quantitative |
|      | questions, also report the spread (interquartile range) as a confidence signal.  |
|    5 | If the spread is wide, the aggregate is less reliable — investigate why people   |
|      | disagree before treating the median as decisive.                                 |
|    6 | If aggregating probability estimates, the geometric mean of odds is sometimes    |
|      | better-calibrated than arithmetic mean of probabilities (especially for low-     |
|      | probability events). For most operational use, plain median is fine.             |
|    7 | After resolution, score the crowd's aggregate against truth. Calibration         |
|      | improves over repeated rounds.                                                   |
|    8 | Periodically refresh the participant pool. Static crowds become correlated as    |
|      | members influence each other through informal channels.                          |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE FOUR CONDITIONS (Surowiecki) — must hold for the effect to work

   1. DIVERSITY OF INFORMATION
       Participants must have different perspectives, backgrounds,
       information sources, biases. A homogeneous crowd's errors don't
       cancel — they reinforce.

   2. INDEPENDENCE
       Participants form estimates without seeing each other's answers.
       No discussion, no anchoring, no social-pressure conformity.

   3. DECENTRALIZATION
       Each participant draws on their own local knowledge. No central
       expert dictating to others.

   4. AGGREGATION
       There must be a mechanism to combine estimates into one answer.
       (Median, mean, weighted average, voting, market price.)

   Failure of ANY one condition can break the effect.

THE PAGE DIVERSITY-PREDICTION THEOREM

   Crowd error = Average individual error − Diversity of estimates

   Implications:
       - Adding diversity reduces crowd error even if no individual
         gets more accurate.
       - A crowd of less-accurate-but-diverse people can outperform
         a crowd of more-accurate-but-similar people.
       - Selecting only the "best" experts can be counterproductive
         if it reduces diversity faster than it increases skill.

THE MEDIAN-VS-MEAN CHOICE

   MEDIAN:
       Robust to outliers and contaminated data.
       Default for most quantitative aggregation.
       Use when distribution is unknown or skewed.

   MEAN:
       More efficient when distribution is symmetric / Gaussian.
       Sensitive to outliers — one ridiculous estimate can shift it.
       Use only when participants are vetted and outliers are absent.

   GEOMETRIC MEAN (of odds, for probabilities):
       Better-calibrated for low-probability events.
       Convert probabilities p to odds (p/(1-p)), take geometric mean,
       convert back. Useful for forecasting tournaments.

   For most operational use, median is the safe default.

THE INDEPENDENCE-PROTECTION CHECKLIST

   [ ] Estimates collected privately (written / anonymous / sealed)
   [ ] No group discussion before estimates submitted
   [ ] No public visibility of others' estimates during collection
   [ ] No status-weighted discussion that would anchor lower-status
       participants on higher-status ones' answers
   [ ] If collecting iteratively (Delphi method), each round's estimates
       are anonymous

   Diagnostic question: would this protocol prevent participant A from
   knowing what participant B estimated? If not, you have dependence
   contamination.

THE DELPHI VARIANT (when you want to update toward consensus)

   Round 1: Independent estimates collected and aggregated.
   Round 2: Aggregate from Round 1 published; participants resubmit
            (still independently, without seeing individual answers).
   Round 3: Repeat until convergence or termination criterion.

   Delphi preserves much of the wisdom-of-crowds effect while allowing
   gradual convergence toward an agreed estimate. Used in expert
   forecasting (medicine, defense, policy).

THE OPERATIONAL ESTIMATION TEMPLATE (for project effort, etc.)

   Question:        ________________________________________________
   Participants:    ________________________________________________
                    (need 5+, ideally 10-15, with diverse perspectives)
   Method:          Independent written estimates; collect via form
                    or sealed submissions
   Aggregation:     Median (default)
   Spread:          Report IQR as confidence indicator

   Estimates collected (sorted):
       ___, ___, ___, ___, ___, ___, ___, ___, ___, ___

   Median:           ___
   Q1:               ___
   Q3:               ___
   IQR:              ___

   Working estimate: median, with IQR as uncertainty range.

   If IQR is large relative to the median (>50%), the spread is
   itself a finding: the team disagrees, and the disagreement should
   be investigated before treating the median as a decision input.

WHEN THE EFFECT BREAKS (do not use)

   - Highly technical questions with one objectively right answer that
     participants without specific expertise cannot estimate. (Crowds
     can't accurately estimate the molecular weight of a protein.)
   - Questions where participants have no information at all (pure
     guessing without partial knowledge produces noise, not signal).
   - Adversarial settings where participants have incentives to lie
     or strategically misreport.
   - Cascading-information environments where early answers are
     visible (markets handle this with market-makers; informal polls
     don't).

   Use a wisdom-of-crowds protocol when participants have *partial,
   diverse* information and submit *independently*.
```

> **Operational notes:** Four disciplines. (1) Independence is the hardest condition to maintain in practice. The temptation is always to "discuss it" before submitting — and that destroys the effect. Build the discipline of "submit first, discuss after"; the discussion is more valuable when it can compare to the aggregate. (2) Diversity is structural, not stylistic. A crowd of ten engineers from the same company is not diverse; their errors will be correlated. Composition matters as much as count. (3) Use the median, not the mean, for almost all operational use. The robustness to outliers is worth the small efficiency loss. (4) The aggregate's spread is itself a signal. A median of 12 weeks with an IQR of 6 weeks is a different finding than a median of 12 weeks with an IQR of 1 week — the first signals real disagreement worth investigating, the second signals genuine consensus. Always report both the central estimate and the spread.
