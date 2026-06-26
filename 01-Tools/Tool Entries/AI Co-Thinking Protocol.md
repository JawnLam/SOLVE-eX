---
Item_ID: tt-ai-co-thinking-protocol
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: AI Co-Thinking Protocol
tt_Source: "Ethan Mollick, *Co-Intelligence: Living and Working with AI* (2024); related: Reid Hoffman, *Impromptu: Amplifying Our Humanity Through AI* (2023); empirical work on LLM-augmented reasoning (Wharton studies on GPT-4 + consultants, Microsoft's Copilot productivity data). Earlier theoretical predecessor: J.C.R. Licklider's *Man-Computer Symbiosis* (1960)."
tt_Type: instrument
tt_Domain: Phronetic / practical wisdom
tt_Field: Metacognition & tool-selection
tt_Operation: Reflect on past action
tt_Cross_Domains:
  - Symbolic systems
tt_Form:
  - Sequenced workflow
  - Dialogue protocol
tt_Scale:
  - Solo
  - Dyadic
tt_Duration:
  - Single session
  - Practice
tt_Lineage:
  - Modern productivity / self-help
  - Industrial / business
tt_Posture:
  - Collaborative-willing
  - Expert-required
tt_State: []
tt_Agent:
  - Human-AI partnership
tt_About:
  - Mind / cognition
  - Decision / choice
tt_SOLVE_eX_Phase: [6]
tt_SOLVE_eX_Step: [6.4]
tt_Clarifies: ['Action']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
  - Feynman Technique
  - After Action Review
  - Critical Question Mapping
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-11 — initial classification (Zero-Gap Sweep Card 09; closes Field anchor for Metacognition/tool-selection's AI-partnership case, PRIMARY ANCHOR for tt_Agent 'Human-AI partnership' — the last empty Agent value)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-11
Date_Modified: 2026-05-11
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "A structured discipline for using LLMs (Claude, GPT-4, Gemini) as cognitive partners — not as oracles, not as search engines, not as labor-replacement. The protocol distinguishes four modes of use (research, draft, critic, simulator) and applies different prompting and oversight discipline to each. Mollick's research suggests AI co-thinking adds 30-40% to expert task performance when used disciplinedly; misuse produces regressions in critical thinking."
Needs_Processing: false
AI_Instructions: ""
---

# AI Co-Thinking Protocol

**One-line summary:** A four-mode discipline (Research / Draft / Critic / Simulator) for using LLMs as cognitive partners — with different prompting, oversight, and verification rules per mode — distinguishing productive co-thinking from over-reliance, hallucination acceptance, or critical-thinking erosion.

**When to reach for it:** Knowledge work (research, writing, analysis, coding) where LLMs are now operationally available; teams developing AI-augmented workflows; individual practice during the current transitional period when usage habits are forming; teaching contexts where AI use is happening informally and benefits from structure.

---

## Purpose Of This Thinking Tool

Ethan Mollick's central operational claim: **LLMs work best when treated as cognitive partners, not as oracles or as replacements.** Three failure modes have emerged:

- **Oracle use** — treating LLM output as authoritative, accepting confident hallucinations as fact.
- **Search-replacement use** — using LLMs for fact-retrieval where they underperform actual search and produce confabulations.
- **Labor-replacement use** — generating output without engaging the cognitive work the output is supposed to embody, producing degraded final products and atrophied skills.

The protocol distinguishes four productive modes:

1. **Research mode.** Use the LLM to scaffold understanding of an unfamiliar domain. Ask for concept-maps, key debates, terminology, common confusions. Verify factual claims separately. Output: your own understanding, not the LLM's summary.

2. **Draft mode.** Use the LLM to produce a first-draft of a known artifact (memo, code, analysis). You edit aggressively. The draft is anchor-and-friction for your own thinking; the final artifact is yours. Risk: shipping the draft as the final.

3. **Critic mode.** Provide the LLM with your work and ask for critique — what's weak, what's missing, where's the steel-man counterargument. The LLM's critique is uneven but cheap, and surfaces blind spots. You decide what to act on.

4. **Simulator mode.** Use the LLM to role-play counterparties, stakeholders, or future versions of yourself. Useful for negotiation prep, difficult-conversation rehearsal, decision war-gaming. The LLM's simulation is imperfect but better than imagining alone.

The non-obvious operational insight: **the discipline is in mode-awareness.** Most failed AI-co-thinking sessions fail because the user is mode-confused — treating Draft output as Research authority, or Research scaffolding as final Draft. Each mode has different verification, edit, and trust rules.

A second insight: **AI co-thinking has both expertise-amplifying and skill-atrophying potential.** Used as Critic by an expert, it sharpens. Used as Draft-with-no-edits by a novice, it short-circuits the skill-building loop. Heavy users in the wrong mode show measurable critical-thinking degradation over time.

## Why Use This Thinking Tool

Three failure modes the protocol prevents:

1. **Hallucination acceptance.** Trusting confident LLM output without verification.
2. **Skill erosion.** Letting the AI do the cognitive work that builds your skill, then losing the skill.
3. **Mode-confused use.** Different modes have different rules; conflating them produces consistent low-quality output.

The framework's empirical case is still developing (early studies show productivity gains, but downstream effects on expertise and judgment are not yet measured). The discipline matters because the technology is changing faster than the use-norms are forming.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|  1   | Before starting an AI-augmented task: identify the mode. Research / Draft /    |
|      | Critic / Simulator.                                                              |
|  2   | RESEARCH: Ask scaffolding questions. Verify factual claims separately. Your    |
|      | output is your own understanding, not the LLM's summary.                        |
|  3   | DRAFT: Generate first draft; edit aggressively. Output is yours, not the LLM's.|
|      | Hard rule: never ship without your edit pass.                                  |
|  4   | CRITIC: Provide your work; ask for steel-man critique, missing arguments,     |
|      | weak points. Treat output as material to consider, not prescription.            |
|  5   | SIMULATOR: Set up the role-play with explicit framing of who the LLM is        |
|      | playing. Use for negotiation prep, conversation rehearsal, scenario testing.   |
|  6   | After the session: notice which cognitive work you did vs. which the AI did. |
|      | Cognitive work you didn't do is skill not built.                                |
|  7   | Verification discipline by mode:                                               |
|      |   Research → independent verification of factual claims                        |
|      |   Draft → editorial pass + factual verification                                 |
|      |   Critic → assessment of critique quality (not all critiques valid)            |
|      |   Simulator → recognition that simulation ≠ reality                            |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
AI Co-Thinking Session Sheet

TASK:                  ___________________________________
MODE:                  [ ] Research [ ] Draft [ ] Critic [ ] Simulator

MODE-SPECIFIC SETUP:

  If RESEARCH:
    Domain I want to scaffold understanding in: ___________
    Key questions (3-5): ___________________________________
    Verification plan: ____________________________________

  If DRAFT:
    Artifact type: __________________________________
    Constraints (length, audience, format): ___________
    Edit-pass commitment: I will not ship without ___ rounds of editing.

  If CRITIC:
    The work I'm submitting for critique: ___________
    What kinds of critique I want (steel-man / missing / weak / structure):
    _________________________________________________

  If SIMULATOR:
    Who is the LLM playing? _________________________
    Context / setup for the role-play: ______________
    Goal of the rehearsal: __________________________

SESSION LOG (key prompts and responses):
   _________________________________________________

COGNITIVE WORK AUDIT (post-session):
   What did the AI do? _______________________________
   What did I do? ____________________________________
   Skill I exercised: ________________________________
   Skill I would have exercised without AI but didn't:
   ____________________________________________________

VERIFICATION DONE:
   [ ] Factual claims verified
   [ ] Critique quality assessed
   [ ] Edit pass complete
   [ ] Simulation limits acknowledged

NEXT ITERATION OR FOLLOW-UP:
   _________________________________________________
```

> **Operational notes:** (1) **Mode-clarity before prompting.** A 30-second mode-decision often saves a 30-minute session that produced mixed-mode confusion. (2) **Verification is not optional, especially for factual claims.** LLMs hallucinate with high confidence; the verification step is the cost of doing business. (3) **The skill-erosion risk is real and individual-specific.** People who use AI in Draft mode without editing measurably degrade in writing skill over months. Critic mode is generally safer because it requires you to do the work first. (4) **Privacy and confidentiality.** Treat the LLM as a public conversation unless you're using verified-private deployments. (5) **Model and capability change quickly.** Re-assess your workflows every 6 months; what wasn't possible last quarter may be now.

## Related Tools and Frameworks

- **Feynman Technique** — pairs as the no-AI baseline for understanding-checking; pre/post AI Co-Thinking comparison reveals what the AI is doing for you vs. what you're doing yourself.
- **After Action Review** — pairs as the structured-reflection cousin for post-session audit.
- **Critical Question Mapping** — useful as the question-scaffolding tool in Research mode.

## Sources

- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio.
- Hoffman, R., with GPT-4 (2023). *Impromptu: Amplifying Our Humanity Through AI*. Dallepedia.
- Licklider, J. C. R. (1960). Man-Computer Symbiosis. *IRE Transactions on Human Factors in Electronics*.
- Dell'Acqua, F., et al. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. Harvard Business School Working Paper.
- Microsoft Work Trend Index reports (ongoing) on Copilot productivity data.
