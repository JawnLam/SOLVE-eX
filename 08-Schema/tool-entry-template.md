---
Item_ID: tt-replace-me
Item_Prototype: Thinking_Tool
Title: Replace Me With Tool Title
tt_Source: "Author, A. (YYYY). *Work Title*. Publisher."
tt_Type: instrument                # instrument | stance
tt_Domain: Discursive-analytical   # one of 12 register-clean Domains; see facet-enums.md
tt_Field: ""                       # open-but-curated; see Thinking Tools Index
tt_Operation: Frame the problem    # one of 36 canonical Operations; do NOT invent a 37th
tt_Cross_Domains: []               # multi-value, optional
tt_Form:                           # multi-value; empty if tt_Type=stance
  - Sequenced workflow
tt_Scale:                          # multi-value
  - Solo
  - Small group
tt_Duration:                       # multi-value
  - Single session
tt_Lineage:                        # multi-value
  - Western analytic / academic
tt_Posture:                        # multi-value
  - Collaborative-willing
tt_State: []                       # multi-value, optional
tt_Agent:                          # multi-value, optional
  - Solo human
tt_About:                          # multi-value, optional
  - Decision / choice
tt_SOLVE_eX_Phase:                 # multi-value; required v1.14.0
  - 1
tt_SOLVE_eX_Step:                  # multi-value; required v1.14.0
  - "1.1"
tt_Clarifies:                      # multi-value; required v1.14.0
  - Origin
tt_Applicability: runtime_applicable   # required v1.14.0; runtime_applicable | describable_only | requires_tradition_transmission
tt_Often_Precedes: []              # tool names; optional
tt_Often_Follows: []               # tool names; optional
tt_Pairs_Well_With: []             # tool names; optional
tt_Replaced_By: []                 # tool names; populate only if deprecating
tt_Status: in-progress             # proposed | in-progress | classified | deprecated
tt_History:
  - "YYYY-MM-DD — initial classification (Sprint NN — Reason)"
Tags:
  - "#thinking-tool"
See_Also: []
Date_Added: 2026-MM-DD
Date_Modified: 2026-MM-DD
Original_Location: ""
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "One-paragraph human-readable summary of the tool's purpose and shape."
Needs_Processing: false
AI_Instructions: ""
---

# {Replace Me With Tool Title}

**One-line summary:** A single declarative sentence stating what the tool does
and what it is for. No fluff. This line is what surfaces in `find-tools.py`
results.

**When to reach for it:** Two to four sentences describing the situations this
tool fits. Mention preconditions, user state, type of decision, or phase-step
where the tool earns its keep.

## Purpose

A paragraph explaining what cognitive work this tool performs. What does it
clarify, decompose, generate, evaluate, or stabilize? Why was the tool
invented? What does it *not* do?

## How To Use

Numbered steps. Each step is a concrete action the user (or AI guiding the
user) takes. If the tool is a `Sequenced workflow`, the steps are the
workflow. If it is a `Matrix`, the steps walk the matrix's cells. If it is a
`Mental model`, the steps are: present the model, apply it to the user's
case, surface what the model reveals.

1. Step one.
2. Step two.
3. Step three.

## Worked Example (optional)

A short anonymized example of the tool applied to a generic but realistic
situation. Useful for tools whose mechanics are hard to grasp without seeing
them in action.

## Common Failure Modes

- Failure mode 1: what goes wrong, how to detect, how to recover.
- Failure mode 2: as above.

## Sources

- Citation 1 (full).
- Citation 2 (full).

## See Also

- `Adjacent Tool Name` — short note on relationship.

<!-- SECTION: VALIDATION_FOOTER -->
Validate this entry: `python3 {ROOT}/07-Scripts/validate-tool.py "{ROOT}/01-Tools/Tool Entries/{Tool Title}.md"`
<!-- /SECTION -->
