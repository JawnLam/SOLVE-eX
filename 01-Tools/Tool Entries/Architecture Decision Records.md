---
Item_ID: tt-architecture-decision-records
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: Architecture Decision Records (ADRs)
tt_Source: "Nygard, M. (2011). 'Documenting Architecture Decisions.' Cognitect blog."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Engineering / design reasoning
tt_Operation: Frame the problem
tt_Cross_Domains: []
tt_Form:
  - Narrative template
  - Sequenced workflow
tt_Scale:
  - Solo
  - Small group
  - Organizational
tt_Duration:
  - Single session
tt_Lineage:
  - Industrial / business
  - Design / craft tradition
tt_Posture:
  - Beginner-friendly
  - Collaborative-willing
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Decision / choice
  - Time / future
  - Group / organization
tt_SOLVE_eX_Phase: [3]
tt_SOLVE_eX_Step: [3.1]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With: []
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-12 — initial classification (Sprint 03 — Deep-Gap Backfill Card 09)"
tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Lightweight markdown documents capturing significant architecture decisions — Title, Status, Context, Decision, Consequences — numbered sequentially and checked into the code repository."
Needs_Processing: false
AI_Instructions: ""
---

# Architecture Decision Records (ADRs)

**One-line summary:** Lightweight markdown documents capturing significant architecture decisions — Title, Status, Context, Decision, Consequences — numbered sequentially and checked into the code repository.

**When to reach for it:** Making a significant architecture decision in a software engineering project where the reasoning will need to be discoverable later — by future-self, by new team members, by reviewers of design choices.

## Purpose

Architecture Decision Records (ADRs), originated by Michael Nygard at ThoughtWorks (2011), are lightweight markdown documents that capture significant architecture decisions in code repositories. Standard structure: Title (numbered, e.g., 'ADR-007: Use PostgreSQL for the user database'); Status (proposed/accepted/deprecated/superseded); Context (the situation and forces); Decision (what was decided); Consequences (positive, negative, neutral). One ADR per decision, numbered sequentially, checked into the repository alongside code. The cognitive payload: the reasoning behind architectural choices is preserved at the point of decision, retrievable later when context has faded. Distinct from full architecture documents; ADRs are decision-grained and time-stamped.

## How To Use

When making a significant architecture decision: create a new markdown file numbered sequentially (ADR-001, ADR-002, etc.) in a dedicated `/decisions/` or `/adr/` directory of the repo. Title: brief and specific. Status: start as 'proposed'; move to 'accepted' when the decision is committed; mark 'superseded by ADR-NNN' if later replaced. Context: what is the situation requiring a decision? What forces are at play? What constraints exist? Decision: state the decision in active voice — 'We will use X.' Consequences: positive (what does this enable?), negative (what trade-offs?), neutral (what follows?). Keep it short — 1-2 pages typical. The ADR is for the future-reader, including future-self.

## Sources

- Nygard, M. (2011). 'Documenting Architecture Decisions.' Cognitect blog.
- Keeling, M. (2017). *Design It! From Programmer to Software Architect*. Pragmatic Bookshelf.
- GitHub: joelparkerhenderson/architecture-decision-record.
