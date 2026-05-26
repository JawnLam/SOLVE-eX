#!/usr/bin/env python3
"""
test-regex-coverage.py — automated coverage test binding the
voice-neutrality-lint.py INVITATION_PATTERNS + INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS
regex sets to their respective canonical specs.

Sprint 17 Card 04 (INVITATION_PATTERNS): closes the "spec authorizes /
script doesn't cover" gap class for §13.2 invitation phrasings.

Sprint 18 Card 02 (INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS): closes the same
gap class for the §13.10 Class A composition-meta banned-pattern family.
The Sprint 17 panel verbatim leak lines below are the canonical
"must-fire" cases; the test asserts each one is caught by at least one
pattern.

Run as:

    python3 07-Scripts/test-regex-coverage.py

Exit codes:
    0  full coverage — every canonical case matches at least one pattern
    1  one or more canonical cases have no matching pattern (gap exists)
    2  invalid input / setup error (voice-neutrality-lint not loadable)

The canonical lists below mirror the §13.2 + §13.10 entries. When the
spec adds a new entry, ADD a corresponding test case here AND add (or
extend) a regex in voice-neutrality-lint.py — the test will fail until
both sides are in parity.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


# §13.2 invitation set — canonical reference.
# Format: (label, sample phrasing, source-section reference)
INVITATIONS = [
    # Content-direct-read invitations (§13.2 table + exception block)
    ("what-do-you-think", "what do you think", "§13.2 exception block"),
    ("what-would-you-do", "what would you do", "§13.2 exception block"),
    ("what-would-you-recommend", "what would you recommend", "§13.2 exception block"),
    ("what-would-you-advise", "what would you advise", "§13.2 exception block"),
    ("what-would-you-suggest", "what would you suggest", "§13.2 exception block"),
    ("what-would-you-say", "what would you say", "§13.2 exception block"),
    ("give-me-your-read", "give me your read", "§13.2 table 'My read' row"),
    ("give-me-the-read", "give me the read", "§13.2 table 'My read' row"),
    ("give-me-your-take", "give me your take", "§13.2 table 'My read' row"),
    ("give-me-the-take", "give me the take", "§13.2 table 'My read' row"),
    ("give-me-your-honest-read", "give me your honest read", "§13.2 table 'Honest read' row"),
    ("give-me-the-bottom-line", "give me the bottom line", "§13.2 table 'My read' row"),
    ("give-me-the-straight-answer", "give me the straight answer", "§13.2 table 'My read' row"),
    ("give-me-your-bottom-line", "give me your bottom line", "§13.2 table 'My read' row"),
    ("tell-me-your-read", "tell me your read", "§13.2 table 'My read' row"),
    ("tell-me-the-read", "tell me the read", "§13.2 table 'My read' row"),
    ("give-it-to-me-straight", "give it to me straight", "§13.2 table 'Honest read' row + line 341 exception"),
    ("tell-it-to-me-straight", "tell it to me straight", "§13.2 table 'Honest read' row variant"),
    ("whats-your-read", "what's your read", "§13.2 exception block"),
    ("what-is-your-read", "what is your read", "§13.2 exception block (Sprint 17 Card 04)"),
    ("whats-the-read", "what's the read", "§13.2 exception block"),
    ("whats-your-take", "what's your take", "§13.2 exception block"),
    ("whats-the-take", "what's the take", "§13.2 exception block"),
    ("whats-your-honest-call", "what's your honest call", "§13.2 table 'Honest read' row"),
    ("whats-the-bottom-line", "what's the bottom line", "§13.2 table 'My read' row"),
    ("whats-your-honest-read", "what's your honest read", "§13.2 table 'Honest read' row"),
    ("whats-your-honest-take", "what's your honest take", "§13.2 table 'Honest read' row"),
    ("honestly-dash-what", "honestly — what should I do", "§13.2 exception block"),
    ("honestly-comma-what", "honestly, what should I do", "§13.2 exception block (Sprint 17 Card 04)"),
    ("what-would-you-actually-recommend", "what would you actually recommend", "§13.2 exception block"),
    ("what-would-you-actually-do", "what would you actually do", "§13.2 exception block"),
    ("what-would-you-actually-say", "what would you actually say", "§13.2 exception block"),
    # Process-direct-read invitations (§13.2 Sprint 15 Card 09 block, §3.10)
    ("am-i-overthinking", "am I overthinking", "§13.2 process-direct-read pattern 1"),
    ("am-i-overthinking-this", "am I overthinking this", "§13.2 process-direct-read pattern 1"),
    ("am-i-being-too-careful", "am I being too careful", "§13.2 process-direct-read pattern 1"),
    ("am-i-being-too-cautious", "am I being too cautious", "§13.2 process-direct-read pattern 1"),
    ("am-i-over-preparing", "am I over-preparing", "§13.2 process-direct-read pattern 1"),
    ("am-i-under-preparing", "am I under-preparing", "§13.2 process-direct-read pattern 1"),
    ("am-i-missing-something", "am I missing something", "§13.2 process-direct-read pattern 2"),
    ("am-i-missing-anything", "am I missing anything", "§13.2 process-direct-read pattern 2"),
    ("am-i-missing-the-point", "am I missing the point", "§13.2 process-direct-read pattern 2"),
    ("is-this-overdone", "is this overdone", "§13.2 process-direct-read pattern 3"),
    ("is-this-too-much", "is this too much", "§13.2 process-direct-read pattern 3"),
    ("is-this-enough", "is this enough", "§13.2 process-direct-read pattern 3"),
    ("is-this-right", "is this right", "§13.2 process-direct-read pattern 3"),
    ("is-this-over-engineered", "is this over-engineered", "§13.2 process-direct-read pattern 3"),
    ("is-my-thinking-off", "is my thinking off", "§13.2 process-direct-read pattern 4"),
    ("is-my-read-off", "is my read off", "§13.2 process-direct-read pattern 4"),
    ("is-my-analysis-off", "is my analysis off", "§13.2 process-direct-read pattern 4"),
    ("is-my-approach-off", "is my approach off", "§13.2 process-direct-read pattern 4"),
    ("is-my-framing-off", "is my framing off", "§13.2 process-direct-read pattern 4"),
]


# Sprint 18 Card 02 — Class A composition-meta canonical leak lines. Each
# entry must be caught by at least one pattern in
# INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS. Source: Sprint 17 panel verbatim
# leak lines (3/3 panel runs emitted Class A composition-meta because
# pre-emit-check.py + voice-neutrality-lint.py did not cover this shape).
# Format: (label, leak line, source-section reference)
COMPOSITION_META_LEAKS = [
    (
        "tessa-t3-im-going-to-write-cf",
        "I'm going to write the Case File now (it's been built up implicitly across these turns and the next response is the action-package commitment moment per protocol). Then I'll deliver the package.",
        "Sprint 17 Tessa turn 3 — Patterns F + G",
    ),
    (
        "mara-t1-let-me-set-up-cf",
        "Let me set up the Case File and get oriented before we move.",
        "Sprint 17 Mara turn 1 — Pattern J",
    ),
    (
        "mara-t6-now-the-actual-response",
        "Now the actual chat response, in Consultant voice with the action package and full scope statement.",
        "Sprint 17 Mara turn 6 — Patterns H + I",
    ),
    # Sprint 18 Card 11 — NEW Class A composition-meta shapes that Card 02
    # Patterns F-K didn't cover. Mara Sprint 18 surfaced 7+ NEW leak shapes
    # in chat-facing turn bodies; Patterns L-Q close the gap.
    (
        "mara-s18-t2-running-diagnostic",
        "Running the diagnostic on Turn 2: she's articulated more shape.",
        "Sprint 18 Mara turn 2 — Pattern L (diagnostic-step narration)",
    ),
    (
        "mara-s18-t3-action-package-trigger-fired",
        "Let me update my task tracking and check the library before composing this turn — the action-package trigger fired but I need to run the Step 8a pre-S2 gate.",
        "Sprint 18 Mara turn 3 — Pattern M (runtime-gate narration)",
    ),
    (
        "mara-s18-t3-now-the-response",
        "Now the response.",
        "Sprint 18 Mara turn 3 — Pattern P (Now-the-response terminator)",
    ),
    (
        "mara-s18-t4-diagnostic-on-turn",
        "Diagnostic on Turn 4: she's posed an explicit process-direct-read invitation.",
        "Sprint 18 Mara turn 4 — Pattern L (diagnostic-step narration)",
    ),
    (
        "mara-s18-t5-persona-stays-in",
        "Persona stays in Guide for the analysis phase; transition to Consultant comes later at action-package delivery.",
        "Sprint 18 Mara turn 5 — Pattern N (persona-state narration)",
    ),
    (
        "mara-s18-t6-re-running-step-gate",
        "Re-running Step 8a pre-S2 runtime gate: three tools named with canonical titles, all resolve to library entries.",
        "Sprint 18 Mara turn 6 — Pattern M (runtime-gate narration)",
    ),
    (
        "mara-s18-t6-output-shape-persona-transition",
        "Output shape: full scope statement with action package. Persona: Guide → Consultant.",
        "Sprint 18 Mara turn 6 — Pattern O + Pattern N (output-shape + persona-transition)",
    ),
    # Sprint 19 Card 04-B — NEW Class A composition-meta shapes from Sprint 19
    # Yelena panel that Sprint 18 Card 11 Patterns L-Q didn't cover. Patterns
    # R-T close the gap. Pattern U ("Switching gears") skipped per operator
    # judgment (too borderline; high false-positive risk).
    (
        "yelena-s19-running-diagnostic-loop",
        "Running the diagnostic loop on a very dense opening.",
        "Sprint 19 Yelena — Pattern R (diagnostic-narration variant)",
    ),
    (
        "yelena-s19-let-me-check-tools-fit",
        "Let me quickly check what library tools fit.",
        "Sprint 19 Yelena — Pattern R (tool-search narration)",
    ),
    (
        "yelena-s19-updating-cf-for-turn",
        "Updating Case File for Turn 3.",
        "Sprint 19 Yelena — Pattern S (Case File state-update narration)",
    ),
    (
        "yelena-s19-now-the-response-colon",
        "Now the response: This turn applies Pre-Mortem and Stakeholder Map.",
        "Sprint 19 Yelena — Pattern T (Now-the-response colon-continuation)",
    ),
]


# Sprint 18 Card 10 — Class C Phase 0 readiness leak canonical lines. Each
# entry must be caught by at least one pattern in pre-emit-check.py's
# CLASS_C_BANNED_PATTERNS. Source: Sprint 18 panel verbatim leak lines (3/3
# panel runs emitted Class C Phase 0 readiness because the original Card 01
# regex covered script-name + path emission but not the sysadmin-log
# readiness-template patterns the template itself produced).
# Format: (label, leak line, source-section reference)
CLASS_C_LEAKS = [
    (
        "yelena-s18-preflight-complete",
        "Pre-flight complete:",
        "Sprint 18 Yelena Phase 0 — sysadmin-log header",
    ),
    (
        "yelena-s18-read-chapters",
        "Read: chapters 00, 01, 02, 03, 06, 09, 13, 14 [in full]",
        "Sprint 18 Yelena Phase 0 — chapter-list enumeration",
    ),
    (
        "tessa-s18-read-chapters",
        "Read: chapters 00, 01, 02, 03, 06, 09, 13 [in full]",
        "Sprint 18 Tessa Phase 0 — chapter-list enumeration",
    ),
    (
        "yelena-s18-session-mode",
        "Session mode: test",
        "Sprint 18 Yelena Phase 0 — mode emission",
    ),
    (
        "yelena-s18-checklist-complete",
        "Session-opening checklist: complete [5 of 5]",
        "Sprint 18 Yelena Phase 0 — checklist-state emission",
    ),
    # Sprint 19 Card 04-A — Class C Phase 0 verbatim leak shapes from Sprint 19
    # panel. Each must be caught by at least one of the 4 new patterns added to
    # pre-emit-check.py CLASS_C_BANNED_PATTERNS in the Sprint 19 Card 04-A
    # supplemental block.
    (
        "yelena-s19-mode-disclosure-prose",
        "Session mode is test per your explicit framing",
        "Sprint 19 Yelena Phase 0 — user-prose-embedded mode disclosure",
    ),
    (
        "yelena-s19-inline-field-run",
        "session_mode: test, test_mode: true, do_not_archive_to_production: true",
        "Sprint 19 Yelena Phase 0 — inline frontmatter field-state run",
    ),
    (
        "tessa-s19-frontmatter-block-names",
        "the pre_flight: and detection_check: blocks will be populated",
        "Sprint 19 Tessa Phase 0 — frontmatter block-name disclosure",
    ),
    (
        "tessa-s19-chapter-section-enum",
        "per chapter 06 §6.1 and chapter 13 §13.2",
        "Sprint 19 Tessa Phase 0 — chapter §-reference enumeration",
    ),
]


def _load_vnl():
    """Import voice-neutrality-lint.py as a module."""
    script_dir = Path(__file__).resolve().parent
    target = script_dir / "voice-neutrality-lint.py"
    if not target.is_file():
        print(f"ERROR: voice-neutrality-lint.py not found at {target}", file=sys.stderr)
        return None
    spec = importlib.util.spec_from_file_location("vnl_for_coverage", target)
    if spec is None or spec.loader is None:
        print("ERROR: could not load voice-neutrality-lint.py module spec", file=sys.stderr)
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"ERROR: voice-neutrality-lint.py failed to import: {e}", file=sys.stderr)
        return None
    return module


def load_invitation_patterns():
    """Import INVITATION_PATTERNS from voice-neutrality-lint.py."""
    module = _load_vnl()
    if module is None:
        return None
    if not hasattr(module, "INVITATION_PATTERNS"):
        print("ERROR: voice-neutrality-lint.py has no INVITATION_PATTERNS attribute", file=sys.stderr)
        return None
    return module.INVITATION_PATTERNS


def load_infrastructure_patterns():
    """Import INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS from voice-neutrality-lint.py."""
    module = _load_vnl()
    if module is None:
        return None
    if not hasattr(module, "INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS"):
        print(
            "ERROR: voice-neutrality-lint.py has no INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS attribute",
            file=sys.stderr,
        )
        return None
    return module.INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS


def load_class_c_patterns():
    """Import CLASS_C_BANNED_PATTERNS from pre-emit-check.py (Sprint 18 Card 10)."""
    script_dir = Path(__file__).resolve().parent
    target = script_dir / "pre-emit-check.py"
    if not target.is_file():
        print(f"ERROR: pre-emit-check.py not found at {target}", file=sys.stderr)
        return None
    spec = importlib.util.spec_from_file_location("pec_for_coverage", target)
    if spec is None or spec.loader is None:
        print("ERROR: could not load pre-emit-check.py module spec", file=sys.stderr)
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"ERROR: pre-emit-check.py failed to import: {e}", file=sys.stderr)
        return None
    if not hasattr(module, "CLASS_C_BANNED_PATTERNS"):
        print(
            "ERROR: pre-emit-check.py has no CLASS_C_BANNED_PATTERNS attribute",
            file=sys.stderr,
        )
        return None
    return module.CLASS_C_BANNED_PATTERNS


def main() -> int:
    # §13.2 invitation coverage (Sprint 17 Card 04)
    inv_patterns = load_invitation_patterns()
    if inv_patterns is None:
        return 2

    inv_gaps = []
    for label, phrase, ref in INVITATIONS:
        if not any(p.search(phrase) for p in inv_patterns):
            inv_gaps.append((label, phrase, ref))

    # §13.10 Class A composition-meta coverage (Sprint 18 Card 02)
    infra_patterns = load_infrastructure_patterns()
    if infra_patterns is None:
        return 2

    leak_gaps = []
    for label, leak_line, ref in COMPOSITION_META_LEAKS:
        if not any(pattern.search(leak_line) for _, pattern in infra_patterns):
            leak_gaps.append((label, leak_line, ref))

    exit_code = 0
    if inv_gaps:
        print(
            f"FAIL: {len(inv_gaps)} of {len(INVITATIONS)} §13.2 invitations are NOT matched by INVITATION_PATTERNS:"
        )
        for label, phrase, ref in inv_gaps:
            print(f"  - [{label}] {phrase!r}  (source: {ref})")
        print(
            "Recovery: extend INVITATION_PATTERNS in voice-neutrality-lint.py "
            "to cover these phrasings, OR remove the entry from this test if "
            "chapter 13 §13.2 has deprecated it."
        )
        exit_code = 1
    else:
        print(
            f"PASS: all {len(INVITATIONS)} §13.2 invitations are matched by INVITATION_PATTERNS "
            "(Sprint 17 Card 04 coverage parity)."
        )

    if leak_gaps:
        print(
            f"FAIL: {len(leak_gaps)} of {len(COMPOSITION_META_LEAKS)} Sprint 17/18/19 composition-meta "
            "leak lines are NOT matched by INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS:"
        )
        for label, leak_line, ref in leak_gaps:
            print(f"  - [{label}] {leak_line!r}  (source: {ref})")
        print(
            "Recovery: extend INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS in voice-neutrality-lint.py "
            "(Patterns F-K, L-Q, R-T and successors) to cover these leak shapes."
        )
        exit_code = 1
    else:
        print(
            f"PASS: all {len(COMPOSITION_META_LEAKS)} Sprint 17/18/19 composition-meta leak lines are "
            "matched by INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS (Sprint 18 Card 02 + Sprint 18 Card 11 + Sprint 19 Card 04-B coverage parity)."
        )

    # §13.10.1 Class C Phase 0 readiness coverage (Sprint 18 Card 10)
    class_c_patterns = load_class_c_patterns()
    if class_c_patterns is None:
        return 2

    class_c_gaps = []
    for label, leak_line, ref in CLASS_C_LEAKS:
        if not any(p.search(leak_line) for p in class_c_patterns):
            class_c_gaps.append((label, leak_line, ref))

    if class_c_gaps:
        print(
            f"FAIL: {len(class_c_gaps)} of {len(CLASS_C_LEAKS)} Sprint 18+19 Class C Phase 0 "
            "leak lines are NOT matched by CLASS_C_BANNED_PATTERNS:"
        )
        for label, leak_line, ref in class_c_gaps:
            print(f"  - [{label}] {leak_line!r}  (source: {ref})")
        print(
            "Recovery: extend CLASS_C_BANNED_PATTERNS in pre-emit-check.py "
            "to cover these readiness-template leak shapes."
        )
        exit_code = 1
    else:
        print(
            f"PASS: all {len(CLASS_C_LEAKS)} Sprint 18+19 Class C Phase 0 leak lines are "
            "matched by CLASS_C_BANNED_PATTERNS (Sprint 18 Card 10 + Sprint 19 Card 04-A coverage parity)."
        )

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
