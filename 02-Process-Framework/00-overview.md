---
doc_type: process_framework
doc_purpose: overview
audience: ai_and_human
read_order: 0
last_updated: 2026-05-13
---

# Process Framework — Overview

This folder specifies the SOLVE eX methodology: the six phases, the
twenty-one steps, the endpoint clarity model, the recursive goal-stack,
and the frame lifecycle.

The folder is **reference** for the AI Operating Manual chapters in
`{ROOT}/00-Instructions/`. The Manual chapters tell the AI what to *do*;
this folder explains the model the Manual operates on.

## Files in this folder

| File | Purpose |
|------|---------|
| `00-overview.md` | This file. Map and short summaries. |
| `01-the-six-phases.md` | The six phases of SOLVE eX. What each phase is for. |
| `02-the-twenty-one-steps.md` | The 21 steps that decompose the phases. |
| `03-endpoint-clarity-states.md` | The four clarity states and the clarity matrix. |
| `04-recursion-semantics.md` | How frames stack; how recursion works. |
| `05-push-pop-rules.md` | When to push a frame, pop a frame, jump back to an earlier step. |
| `06-frame-lifecycle.md` | Created → active → resolved → popped. Pause and abandon paths. |
| `source-material/` | Original SOLVE eX source documents (Phase 0–3 .txt files, JSON canon, Thinking Tools 01–26.txt, S.O.L.V.E. eX overview .txt). |

## The shortest possible summary

A SOLVE eX session is a journey from where the user is (Origin) to where
they want to be (Destination), with a path between. The journey runs
through six phases (State, Objective, Learn, Vision, Evaluate, eXecute),
which decompose into 21 steps. Both endpoints have four possible clarity
states; you continuously assess both. When clarification stalls, you push
a sub-frame whose Destination is "make the parent's endpoint clear." This
recursion is fractal — SOLVE eX cycles run within SOLVE eX cycles.

The full operational details live in the files above. The Manual chapter
that operationalizes all of this is
`{ROOT}/00-Instructions/03-the-diagnostic-loop.md`.

## What this folder is NOT

- Not the implementation. The Manual chapters are the implementation.
- Not a user manual. The user does not read this folder. The system reads
  it on session start and refers to it when needed.
- Not a static specification. Schema evolves; the steps and phases here
  are v1.0 of the v2.0 build. Major changes require a version bump and
  a migration crosswalk in `{ROOT}/99-Archive/`.

## Source material

The original SOLVE eX methodology lives in `source-material/`:

- `Phase 0 - Using SOLVE eX.txt` — pre-process orientation
- `Phase 1 - Define the Current State.txt` — Phase 1 working documents
- `Phase 2 - Define the Goal State.txt` — Phase 2 working documents
- `Phase 3 - Fact Finding And Data Collecting.txt` — Phase 3 working documents
- `S.O.L.V.E. eX. Problem Solving Process.json` — canonical JSON description
- `S.O.L.V.E. eX.txt` — overview document
- `S.O.L.V.E. eX - v2.txt` — v2 revision
- `Thinking Tools 01-26.txt` — original 26-tool seed library

These are preserved for reference and to ground the framework in its
methodology pedigree. They are NOT the operational documents — the
operational documents are in this folder's `01-` through `06-` files
and in `{ROOT}/00-Instructions/`.
