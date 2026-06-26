---
Item_ID: tt-stride-threat-modeling
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: STRIDE Threat Modeling
tt_Source: "Shostack, A. (2014). Threat Modeling: Designing for Security. Wiley."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Adversarial / debiasing reasoning
tt_Operation: Decompose hierarchically
tt_Cross_Domains: []
tt_Form:
  - Checklist
  - Mnemonic
tt_Scale:
  - Solo
  - Small group
tt_Duration:
  - Single session
  - Workshop
tt_Lineage:
  - Industrial / business
  - Military / strategic
tt_Posture:
  - Expert-required
  - Adversarial-tolerant
tt_State: []
tt_Agent:
  - Solo human
  - Human group
tt_About:
  - Risk / uncertainty
  - Group / organization
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
Quick_Notes: "Microsoft-originated threat-modeling framework — six threat categories enumerated against any system component: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege."
Needs_Processing: false
AI_Instructions: ""
---

# STRIDE Threat Modeling

**One-line summary:** Microsoft-originated threat-modeling framework — six threat categories enumerated against any system component: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

**When to reach for it:** Conducting security review of a software system or component where systematic threat enumeration is required and ad-hoc threat-imagination would miss critical categories.

## Purpose

STRIDE is a threat-modeling framework developed at Microsoft for enumerating security threats against system components. The mnemonic: (S)poofing — pretending to be someone else (impersonation, identity theft); (T)ampering — modifying data in transit or at rest; (R)epudiation — denying having performed an action (logs absent or tampered); (I)nformation disclosure — unauthorized data exposure; (D)enial of service — making the system unavailable; (E)levation of privilege — gaining higher-than-authorized permissions. Each category is checked against each component of the system. STRIDE is per-component categorical; complements other threat-modeling methods (PASTA is risk-centric process; attack trees are scenario-driven).

## How To Use

For the system being analyzed: produce a data-flow diagram showing components, data stores, processes, and trust boundaries. For each component (process, data store, data flow): walk through the STRIDE letters. Can this component be spoofed (S)? Can the data here be tampered with (T)? Are actions here repudiable (R)? Is information here at risk of disclosure (I)? Can this component be denied to legitimate users (D)? Can authorization here be elevated improperly (E)? Document each identified threat with severity and mitigation. The mnemonic ensures comprehensive coverage; the per-component walkthrough produces a threat list that can be prioritized and addressed. Often used as the entry-level threat modeling method; more sophisticated methods (PASTA, attack trees) build on STRIDE output.

## Sources

- Howard, M., & LeBlanc, D. (2003). *Writing Secure Code* (2nd ed.). Microsoft Press.
- Shostack, A. (2014). *Threat Modeling: Designing for Security*. Wiley.
- Hernan, S., et al. (2006). 'Threat Modeling: Uncover Security Design Flaws Using the STRIDE Approach.' *MSDN Magazine*.
