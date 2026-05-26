---
Item_ID: tt-pasta-threat-modeling
Item_Prototype: Thinking_Tool
Title: PASTA Threat Modeling
tt_Source: "UcedaVelez, T., & Morana, M. M. (2015). Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis. Wiley."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Adversarial / debiasing reasoning
tt_Operation: Sequence multi-party persuasion
tt_Cross_Domains: []
tt_Form:
  - Sequenced workflow
  - Mental model
tt_Scale:
  - Small group
  - Organizational
tt_Duration:
  - Workshop
  - Project
tt_Lineage:
  - Industrial / business
  - Military / strategic
tt_Posture:
  - Expert-required
  - Adversarial-tolerant
tt_State: []
tt_Agent:
  - Human group
tt_About:
  - Risk / uncertainty
  - Group / organization
  - Strategy / competition
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
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-05-12
Date_Modified: 2026-05-12
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Process for Attack Simulation and Threat Analysis — seven-stage risk-centric methodology more business-aligned than STRIDE."
Needs_Processing: false
AI_Instructions: ""
---

# PASTA Threat Modeling

**One-line summary:** Process for Attack Simulation and Threat Analysis — seven-stage risk-centric methodology more business-aligned than STRIDE.

**When to reach for it:** Conducting threat modeling for a business-critical system where business risk alignment is required, and STRIDE's per-component categorical approach is too narrow to capture the full risk picture.

## Purpose

PASTA (Process for Attack Simulation and Threat Analysis) is a seven-stage threat-modeling methodology developed by Tony UcedaVelez and Marco Morana. The stages: (1) Define objectives — what business and security objectives is this analysis serving? (2) Define technical scope — boundaries, dependencies, infrastructure. (3) Application decomposition — components, data flows, trust boundaries. (4) Threat analysis — what threats are present in this environment? (5) Vulnerability analysis — what vulnerabilities exist in the system? (6) Attack modeling — how would an attacker chain vulnerabilities to achieve threat objectives? (7) Risk analysis and management — what is the business risk, and what mitigations are warranted? More risk-business-aligned than STRIDE; suited to enterprise contexts where security must connect to business risk.

## How To Use

(1) Engage business stakeholders to define objectives — what is being protected, what business outcomes matter? (2) Map technical scope — system boundaries, integrations, infrastructure. (3) Decompose the application — components, data flows, trust boundaries; produce architectural diagrams. (4) Analyze threats relevant to the environment — threat actors, motivations, capabilities. (5) Analyze vulnerabilities — known CVEs, configuration weaknesses, design flaws. (6) Model attacks — for each significant threat, construct attack paths combining vulnerabilities to achieve the threat objective. (7) Assess business risk for each attack path and prioritize mitigations. PASTA's strength is the connection of technical findings to business risk; its cost is the time required for a full seven-stage analysis. Often used for high-value systems; STRIDE-style work suffices for less critical components.

## Sources

- UcedaVelez, T., & Morana, M. M. (2015). *Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis*. Wiley.
- OWASP Threat Modeling resources.
- Shostack, A. (2014). *Threat Modeling: Designing for Security*. Wiley.
