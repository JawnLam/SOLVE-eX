---
doc_type: process_framework
doc_purpose: steps_spec
audience: ai_and_human
read_order: 2
last_updated: 2026-05-13
---

# The Twenty-One SOLVE eX Steps

The six phases decompose into 21 steps. Step affinity is the finest-grained
routing facet for the Tool Selector: tools are tagged with
`tt_SOLVE_eX_Step` and the Selector ranks by step match.

Note: the field is named "twenty-one" because v1.0 has 21 steps. The
master plan's filename `02-the-nineteen-steps.md` was a v0 artifact; the
canonical name is `02-the-twenty-one-steps.md` per the 21-step count.

| # | Phase | Step | Title | What the work produces |
|---|-------|------|-------|------------------------|
|  1 | 1 | 1.1 | Describe the situation | A coherent narrative of the current state |
|  2 | 1 | 1.2 | Write the problem statement | One-sentence compression of the problem |
|  3 | 1 | 1.3 | Frame the situation | An explicit framing ("one way to look at this is…") |
|  4 | 2 | 2.1 | Articulate reasons to resolve | Why this matters to the user |
|  5 | 2 | 2.2 | Write the goal statement | A coherent statement of the desired outcome |
|  6 | 2 | 2.3 | Establish requirements | Non-negotiable criteria for any acceptable outcome |
|  7 | 3 | 3.1 | Find current facts and data | Snapshot of the present state |
|  8 | 3 | 3.2 | Find past facts and data | Historical context |
|  9 | 3 | 3.3 | Find systems facts and data | How the system around the decision works |
| 10 | 3 | 3.4 | Find future facts and data | Trends, projections, scenarios |
| 11 | 4 | 4.1 | Analyze root causes | The gap-explaining causes |
| 12 | 4 | 4.2 | Expansive idea formation | A broad inventory of options |
| 13 | 4 | 4.3 | Anticipative solution crafting | Solutions that account for second-order effects |
| 14 | 4 | 4.4 | Idea refinement | Sharpened, combined, or hybrid options |
| 15 | 5 | 5.1 | Define evaluation criteria | The criteria the user will judge options against |
| 16 | 5 | 5.2 | Select decision tools | The chosen evaluation method (matrix, tree, etc.) |
| 17 | 5 | 5.3 | Validate decision impact | Gut-check, second-order, reversibility check |
| 18 | 6 | 6.1 | Design and test solution | Pilot, prototype, or low-cost experiment |
| 19 | 6 | 6.2 | Create action plan | Concrete time-bound plan |
| 20 | 6 | 6.3 | Implement action plan | Execution |
| 21 | 6 | 6.4 | Conduct follow-up and feedback | Post-action review |

## Step naming conventions

- Step numbers are quoted as strings in YAML frontmatter (`"1.1"`, not
  `1.1`) — see `{ROOT}/08-Schema/validation-rules.md` §I.
- Step titles use sentence case in this document, lowercase-with-hyphens
  in question-bank filenames (e.g., `phase-1-1-describe-situation.md`).

## Step diagnostic signals

The diagnostic-loop chapter (`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`
§3.2) maps user-language signals to step hypotheses. The signal table is
authoritative for in-session diagnosis. The step table above is the
reference for what each step *produces* — i.e., the artifact that should
appear in the Case File when the step is complete.

## Step completion criteria

A step is "complete" when:

1. The step's produced artifact exists in the Case File (e.g., Step 1.2
   has a one-sentence problem statement in `### Goal Statement` or
   `### Problem Statement`).
2. The user has affirmed the artifact (not just provided raw material for
   it).
3. The artifact has survived at least one stress-test question (where
   "stress-test" means: "Does this still feel right when I ask it back to
   you a different way?").

Step completion does **not** require all sub-points to be exhausted. Many
steps complete in 2–4 turns of focused work; some take many sessions.

## Step skip patterns

| When the user has… | …you may skip directly to… |
|-------------------|--------------------------|
| A locked Origin and locked Destination at session start | Step 3.1 (Phase 3) or Step 5.1 (Phase 5) depending on whether facts or options are the bottleneck |
| A locked Origin but Unclear Destination | Step 2.1 |
| A locked Destination but Unclear Origin | Step 1.1 |
| Both endpoints Unclear | Step 1.1 (default starting move) |
| A specific tool they want to apply | The relevant step for that tool's `tt_SOLVE_eX_Step`; the tool's application is the step's work |

Skips are not violations of the framework. The framework is scaffold; the
diagnostic decides which scaffold-rungs are load-bearing in this session.

## Step revisits

Any step can be revisited. Common revisit patterns:

- **Step 1.2 revisited after Phase 5.** The user's evaluation surfaced a
  consideration the problem statement did not capture. Update Step 1.2;
  re-check Step 2.2 for goal-statement consistency.
- **Step 2.2 revisited after Step 5.3.** Gut-check failed; the goal
  statement was probably wrong.
- **Step 3.1 revisited after Step 4.2.** A divergent option requires
  facts you hadn't gathered.
- **Step 4.1 revisited after Step 6.4.** Implementation feedback revealed
  the root cause was different than diagnosed.

Revisits are not "going backwards." They are how decision-making actually
works.

## Step-to-tool affinity summary

A representative sampling of which tools cluster around which steps. Use
the library's `tt_SOLVE_eX_Step` facet for the authoritative mapping.

| Step | Representative tools |
|------|---------------------|
| 1.1 | Context Clarity Navigator, Situation Analysis, A3 Background section |
| 1.2 | 5W1H, Toyota A3 Problem Statement, Issue Tree |
| 1.3 | Reframing prompts, Inversion, Six Thinking Hats |
| 2.1 | Reasons to Change inventory, Motivational Interviewing pros |
| 2.2 | Goal Statement template, SMART/SMARTER, Ikigai, Eulogy Exercise |
| 2.3 | Requirements Matrix, MoSCoW, Must-Have / Nice-to-Have |
| 3.1 | SWOT, PESTEL, Stakeholder Map |
| 3.2 | Historical Trend Analysis, Cohort Analysis |
| 3.3 | Causal Loop Diagram, Systems Map, Iceberg Model |
| 3.4 | Scenario Planning, Three Horizons (future), Premortem (future) |
| 4.1 | Five Whys, Fishbone, Root Cause Analysis |
| 4.2 | SCAMPER, TRIZ, Lateral Thinking, Brainstorming |
| 4.3 | Anticipative scenario crafting, Backcasting |
| 4.4 | Idea Combination, Hybrid Refinement |
| 5.1 | Criteria Generation, Values-First Filter |
| 5.2 | Eisenhower Matrix, Weighted Decision Matrix, Decision Tree, Expected Value |
| 5.3 | Gut Check, Pre-Mortem, Reversibility Test, Second-Order Effects |
| 6.1 | Pilot Design, Lean Experiment, MVP Definition |
| 6.2 | If-Then Implementation Intentions, Time-Boxed Plan, OKR draft |
| 6.3 | Daily Operations practices, Habit Stacking, Accountability Structures |
| 6.4 | After-Action Review, Retrospective, Lessons Learned |

The library has many more tools per step; the table above is illustrative.
