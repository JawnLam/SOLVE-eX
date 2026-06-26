---
Item_ID: tt-c4-architecture-notation
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: C4 Architecture Notation
tt_Source: "Brown, S. (2018). The C4 Model for Software Architecture. Leanpub."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Visual / spatial communication
tt_Operation: Decompose hierarchically
tt_Cross_Domains: []
tt_Form:
  - Visualization technique
  - Mental model
tt_Scale:
  - Solo
  - Small group
tt_Duration:
  - Single session
  - Project
tt_Lineage:
  - Industrial / business
  - Design / craft tradition
tt_Posture:
  - Beginner-friendly
  - Expert-required
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Group / organization
  - Aesthetic / craft
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
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
Quick_Notes: "Simon Brown's four-level visual modeling notation for software architecture — System Context, Containers, Components, Code — each level zooming in so readers can stay at the appropriate level of abstraction."
Needs_Processing: false
AI_Instructions: ""
---

# C4 Architecture Notation

**One-line summary:** Simon Brown's four-level visual modeling notation for software architecture — System Context, Containers, Components, Code — each level zooming in so readers can stay at the appropriate level of abstraction.

**When to reach for it:** Communicating software architecture to stakeholders at different levels of abstraction — executives needing the high-level system context, architects needing container-level views, developers needing component-level detail.

## Purpose

The C4 Model (Simon Brown, 2018) is a hierarchical visual notation for software architecture organized at four levels: (1) System Context — the software in its environment of users, external systems, dependencies; suitable for executives and non-technical stakeholders. (2) Containers — the major deployable units (web apps, databases, message queues, services) and their interactions; suitable for technical leadership. (3) Components — within a single container, the major modules and their interactions; suitable for developers working in that container. (4) Code — UML class diagrams or similar (optional, often skipped) showing implementation detail. Each level zooms in; readers consume the level appropriate to their need. Addresses the common failure mode where one diagram tries to convey everything and conveys nothing.

## How To Use

For the software being documented: produce the four levels in order. Level 1 (System Context): a single page showing the system as a box, surrounded by user types and external systems it integrates with. Annotate the arrows with what is exchanged. Level 2 (Containers): explode the system box into its deployable containers (web app, mobile app, database, API service, queue, etc.). Show inter-container communication with technologies. Level 3 (Components): for each significant container, explode into its major components. Show component responsibilities and interactions. Level 4 (Code): usually omitted — code itself is the documentation at this level. Tools: C4-PlantUML or Structurizr are popular; or plain whiteboard sketches following the conventions. The discipline is the hierarchical zoom; each level should be readable on its own.

## Sources

- Brown, S. (2018). *The C4 Model for Software Architecture*. Leanpub.
- c4model.com — official site with conventions and examples.
- Structurizr documentation.
