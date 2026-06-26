---
Item_ID: tt-blameless-postmortem
type: Thinking_Tool
timestamp: "2026-05-12T00:00:00Z"
title: Google SRE Blameless Postmortem
tt_Source: "Beyer, B., et al. (2016). Site Reliability Engineering: How Google Runs Production Systems. O'Reilly."
tt_Type: instrument
tt_Domain: Modes of inquiry
tt_Field: Reflective practice & experiential learning
tt_Operation: Reflect on past action
tt_Cross_Domains: []
tt_Form:
  - Sequenced workflow
  - Dialogue protocol
tt_Scale:
  - Small group
  - Organizational
tt_Duration:
  - Single session
  - Workshop
tt_Lineage:
  - Industrial / business
tt_Posture:
  - Trust-required
  - Collaborative-willing
tt_State: []
tt_Agent:
  - Human group
tt_About:
  - Group / organization
  - Risk / uncertainty
tt_SOLVE_eX_Phase: [6]
tt_SOLVE_eX_Step: [6.4]
tt_Clarifies: ['Action']
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
Quick_Notes: "Google SRE practice for post-incident analysis — strict no-blame framing focuses on systems, assumes good faith with available information, and surfaces root causes (often multiple, systemic)."
Needs_Processing: false
AI_Instructions: ""
---

# Google SRE Blameless Postmortem

**One-line summary:** Google SRE practice for post-incident analysis — strict no-blame framing focuses on systems, assumes good faith with available information, and surfaces root causes (often multiple, systemic).

**When to reach for it:** Conducting post-incident analysis in a software engineering or operations context where the alternative — blame-based review — would suppress information needed to actually understand what happened.

## Purpose

The Blameless Postmortem, codified at Google in the SRE practice and earlier articulated by John Allspaw at Etsy, is a post-incident analysis method built on strict no-blame framing. Core commitments: focus on systems and processes, not individuals; assume all participants acted in good faith with the information they had; surface root causes (which are usually multiple and often systemic); output a written postmortem document with action items. The cognitive payload: by removing the threat of personal blame, the practice surfaces information that blame-based reviews suppress — what people actually thought, what alerts didn't fire, what assumptions failed. The result is better understanding and more effective prevention than blame-based methods produce.

## How To Use

Schedule the postmortem soon after the incident (1-3 days) but not so soon that responders are exhausted. Designate a facilitator who explicitly enforces blameless framing. Reconstruct the timeline: what happened, when, who took what action with what information available at the time. Use 'just culture' framings: 'Given what was known at the time, this was a reasonable decision.' Identify contributing factors across multiple dimensions: technical (system behavior, monitoring), procedural (runbooks, on-call processes), organizational (staffing, training, communication). Generate action items with owners and due dates. Write up: published widely within the organization; the discipline of transparent publication is part of the practice. Track action items to completion.

## Sources

- Beyer, B., et al. (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O'Reilly.
- Allspaw, J. (2012). 'Blameless PostMortems and a Just Culture.' Etsy Engineering blog.
- Dekker, S. (2007). *Just Culture: Balancing Safety and Accountability*. Ashgate.
