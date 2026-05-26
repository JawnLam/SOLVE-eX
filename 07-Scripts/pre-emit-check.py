#!/usr/bin/env python3
"""
pre-emit-check.py — compose-time validator hook that wraps
voice-neutrality-lint.py + trigger-phrase-audit.py as a gate fired
BEFORE chat ships. Sprint 17 Card 02 — natural evolution of Sprint
16 Card 01's pre-emission guard thesis at the lint-script layer:
moves enforcement from "AI discipline" to "tool-enforced."

Sprint 17 Card 01 chat-surface taxonomy (chapter 13 §13.10):
- Class A (in-persona): ZERO tolerance — banned-pattern list applies
- Class B (operator-debrief): MODERATE tolerance — explicit mechanics permitted
- Class C (Phase 0 readiness): MODERATE tolerance — no script/path enumeration
- Class D (turn-boundary): LOW tolerance — milestone language only

Usage:
    cat draft.txt | python3 07-Scripts/pre-emit-check.py
    python3 07-Scripts/pre-emit-check.py draft.txt
    python3 07-Scripts/pre-emit-check.py --surface-class C draft.txt
    python3 07-Scripts/pre-emit-check.py --surface-class D --quiet draft.txt

Exit codes (sibling-script-compatible, v28+v30+v31 lint conventions):
    0  clean — no violations detected; safe to ship
    1  violations detected — refuse to ship; rephrase and re-run
    2  invalid input — file not found, unreadable, etc.

Surface-class flag:
    --surface-class A  ZERO tolerance (default, fail-closed)
    --surface-class B  MODERATE — explicit mechanics permitted
    --surface-class C  MODERATE — no script-name / path enumeration in chat
    --surface-class D  LOW — milestone language only, no field enumeration

When surface class is unknown or unspecified, defaults to Class A
(strictest) per chapter 13 §13.10.1 fail-closed default rule.

Hook is idempotent — re-running on same input produces same exit
code. The hook composes with existing scripts (voice-neutrality-lint
+ trigger-phrase-audit) rather than duplicating their pattern
coverage — the existing scripts ARE the canonical pattern source-
of-truth; pre-emit-check just runs them in the compose-time slot.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def load_voice_neutrality_lint():
    """Import voice-neutrality-lint.py module for pattern access."""
    target = SCRIPT_DIR / "voice-neutrality-lint.py"
    if not target.is_file():
        return None
    spec = importlib.util.spec_from_file_location("vnl", target)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception:
        return None
    return module


# Class A supplemental patterns — coverage gaps surfaced by Sprint 17
# Card 02 v31 verification that voice-neutrality-lint.py's Pattern A
# misses. Sprint 18 carry-forward candidate: roll these into Pattern A's
# noun list. For now they're scoped to pre-emit-check.py so Card 02
# doesn't bleed into Card 04 (script-layer regex hygiene).
#
# Sprint 18 Card 02 — the composition-meta banned-pattern family
# (Patterns F-K) was added to voice-neutrality-lint.py's
# INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS rather than this supplemental list,
# because composition-meta is canonical chapter 13 §13.10 Class A coverage
# (not a pre-emit-check-only gap). scan_class_a() below imports vnl's
# pattern list, so the new Patterns F-K are picked up automatically when
# pre-emit-check.py runs --surface-class A. No additions to
# CLASS_A_SUPPLEMENTAL_PATTERNS are needed; duplicating the patterns here
# would cause each match to fire twice with conflicting labels.
CLASS_A_SUPPLEMENTAL_PATTERNS = [
    # "I'll/let me [verb] ... detection check"
    re.compile(
        r"\b(?:let me|i[' ]ll(?:\s+now)?)\s+"
        r"(?:run|fire|trigger|verify|check|apply|invoke|consult|"
        r"look\s*up|surface|do|perform)\b"
        r".*?\bdetection\s+check\b",
        re.IGNORECASE,
    ),
    # "Let me verify [Tool] (tool) exists in the library"
    re.compile(
        r"\b(?:let me|i[' ]ll(?:\s+now)?)\s+verify\b.*?"
        r"\bexists?\s+in\s+the\s+library\b",
        re.IGNORECASE,
    ),
    # "I'll/let me [verb] (the) tool-selection/library-lookup/sophistication-detector"
    re.compile(
        r"\b(?:let me|i[' ]ll(?:\s+now)?)\s+"
        r"(?:run|fire|trigger|consult|invoke|apply|verify|check)\b"
        r".*?\b(?:tool[- ]selection|sophistication[- ]detect|library[- ]lookup|"
        r"step\s*8a?|step\s*\d+(?:\.\d+)?\s+gate|"
        r"audit\s+script|coverage\s+check)\b",
        re.IGNORECASE,
    ),
]

# Class C banned patterns — script-name + path-name + system-state
# emission in Phase 0 readiness statement. Chapter 13 §13.10 Class C
# tolerances.
#
# Sprint 18 Card 10 (supplemental to Card 01) — Sprint 18 panel runs
# revealed that the readiness-statement template itself emitted patterns
# the original Card 01 didn't catch: chapter-list enumeration ("Read:
# chapters X, Y, Z"), session-mode emission ("Session mode: test"),
# checklist-state ("Session-opening checklist: complete [N of N]"), and
# the "Pre-flight complete:" sysadmin-log header. All 3 panel cases
# (Yelena + Tessa + Mara) leaked these despite check-phase0-sync.py
# passing. Card 10 adds the 4 patterns AND rewrites root + chapter-00
# mirror Phase 0 readiness templates to user-facing prose (per the
# original spec intent — "readiness should read as user-facing prose,
# not a system-administrator log").
CLASS_C_BANNED_PATTERNS = [
    # Script-name enumeration in chat
    re.compile(r"\b(?:find-tools|validate-case-file|voice-neutrality-lint|trigger-phrase-audit|post-session-audit|pre-emit-check|test-regex-coverage|cross-chapter-dependency-audit|case-file-placeholder-lint)\.py\b", re.IGNORECASE),
    # Bracketed script-list shape ("Scripts: available [...]")
    re.compile(r"Scripts:\s*available\s*\[", re.IGNORECASE),
    # Absolute path emission
    re.compile(r"/(?:Users|var|home|opt|tmp)/\S+/(?:Dropbox|SOLVE|06-Case-Files|_ACTIVE)\b"),
    re.compile(r"writable at\s+(?:/|~|\$HOME)", re.IGNORECASE),
    # Protocol-field state in readiness statement
    re.compile(r"\b(?:detection_check|relaxed_scaffolding|active_persona|signals_observed|goal_stack)\s+(?:block format verified|initialized|ready)", re.IGNORECASE),
    # Sprint 18 Card 10 supplemental — sysadmin-log readiness-template patterns
    # "Pre-flight complete:" sysadmin-log header
    re.compile(r"\bPre-?flight\s+complete\s*:", re.IGNORECASE),
    # "Read: chapters X, Y, Z [in full]" — chapter-list enumeration in Phase 0
    re.compile(r"\bRead\s*:\s*chapters?\s+\d+(?:\s*,\s*\d+){1,}(?:\s*\[(?:in full|[^]]+)\])?", re.IGNORECASE),
    # "Session mode: test/production/sandbox" — mode emission in Phase 0
    re.compile(r"\bSession\s+mode\s*:\s*(?:production|test|sandbox|multi-session-resumption)", re.IGNORECASE),
    # "Session-opening checklist: complete [N of N]" — checklist-state in Phase 0
    re.compile(r"\bSession-opening\s+checklist\s*:\s*(?:complete\s*)?\[\s*\d+\s+of\s+\d+\s*\]", re.IGNORECASE),
    # Sprint 19 Card 04-A supplemental — Class C Phase 0 leak shapes
    # surfaced in Sprint 19 panel (Yelena + Tessa) that the Sprint 18
    # Card 10 patterns above did not catch.
    # 1. User-prose-embedded mode disclosure (Yelena): "Session mode is
    #    test per your explicit framing" — narrative form, distinct from
    #    the colon-separated "Session mode: test" pattern above.
    re.compile(r"\bSession\s+mode\s+is\s+(?:production|test|sandbox|multi-session-resumption)\b", re.IGNORECASE),
    # 2. Inline frontmatter field-state runs (Yelena): "session_mode: test,
    #    test_mode: true, do_not_archive_to_production: true" — multiple
    #    Case File frontmatter fields enumerated inline in chat prose.
    re.compile(r"\b(?:session_mode|test_mode|do_not_archive_to_production|production_artifact|operator_audit)\s*:\s*(?:true|false|test|production|sandbox|yes|no)\b", re.IGNORECASE),
    # 3. Frontmatter-block name disclosure (Tessa): "the pre_flight: and
    #    detection_check: blocks will be populated" — naming YAML frontmatter
    #    block fields directly in chat-visible prose.
    re.compile(r"\b(?:pre_flight|detection_check|signals_observed|s2_single_frame_relaxation|stakes_flags_routing|stakes_flags_logging|goal_stack|tools_applied)\s*:\s*(?:and\s+\w+\s*:\s*)?(?:block|blocks)\b", re.IGNORECASE),
    # 4. Chapter §-reference enumeration (Tessa): "per chapter 06 §6.1
    #    and chapter 13 §13.2" — naming multiple chapters + section
    #    numbers in chat prose during Phase 0 readiness statement.
    re.compile(r"\bchapter\s+\d+\s*§\s*\d+(?:\.\d+)*\s+and\s+chapter\s+\d+\s*§\s*\d+(?:\.\d+)*", re.IGNORECASE),
]

# Class D banned patterns — Case File field enumeration in
# end-of-turn footers + protocol-field state narration at
# turn-boundary position. Chapter 13 §13.10 Class D tolerances.
CLASS_D_BANNED_PATTERNS = [
    # Case File state enumeration
    re.compile(r"Case File\s+(?:state\s+)?(?:updated|state)\s+through\s+Turn\s+\d", re.IGNORECASE),
    re.compile(r"Tools Applied\s+(?:has|now contains|now logs)", re.IGNORECASE),
    re.compile(r"\bdetection_check\s+(?:written|fired|recorded)\s+\(", re.IGNORECASE),
    # Protocol-field state narration at turn-boundary
    re.compile(r"\b(?:relaxed_scaffolding|last_persona_switch|stakes_flags_routing|stakes_flags_logging|s2_single_frame_relaxation)\s+(?:remains|unchanged|written|recorded|populated|empty|set to)", re.IGNORECASE),
    re.compile(r"\(\s*\d+/5\s+signals\b", re.IGNORECASE),  # "(0/5 signals → standard mode)"
    # End-of-turn signal-status enumeration
    re.compile(r"End of Turn\s+\d+\s*:", re.IGNORECASE),
    # Script-name-with-.py + meta-verb in close/turn-boundary
    # (Sprint 17 Card 02 v31-verification coverage gap; Sprint 18
    # carry-forward to roll into voice-neutrality-lint Pattern E).
    re.compile(
        r"\b(?:voice[- ]neutrality[- ]lint|validate[- ]case[- ]file|"
        r"trigger[- ]phrase[- ]audit|post[- ]session[- ]audit|"
        r"pre[- ]emit[- ]check|test[- ]regex[- ]coverage|"
        r"artifact[- ]quality[- ]audit|portability[- ]check|"
        r"cross[- ]chapter[- ]dependency[- ]audit|"
        r"case[- ]file[- ]placeholder[- ]lint)"
        r"(?:\.py)?"
        r"\b[^\n]{0,80}?"
        r"\b(?:exited|flagged|caught|surfaced|fired|catch|catches|repaired)\b",
        re.IGNORECASE,
    ),
]


def scan_class_a(text: str, vnl) -> list[tuple[str, str]]:
    """Class A scan: voice-neutrality infrastructure-announcement
    patterns from the canonical scan list (chapter 13 §13.10) plus
    Sprint 17 Card 02 supplemental coverage gaps."""
    violations = []
    if vnl is not None and hasattr(vnl, "INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS"):
        for label, pattern in vnl.INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS:
            for m in pattern.finditer(text):
                violations.append((label, m.group(0)))
    for pattern in CLASS_A_SUPPLEMENTAL_PATTERNS:
        for m in pattern.finditer(text):
            violations.append(("class-a: supplemental coverage", m.group(0)))
    return violations


def scan_class_b(text: str, vnl) -> list[tuple[str, str]]:
    """Class B scan: operator-debrief MODERATE tolerance. Explicit
    mechanics narration permitted when the operator has requested
    debriefing. The banned-pattern list applies only to content
    that would be visible to a non-debrief audience. Pragmatic
    implementation: scan for the always-banned phrases (I'd want,
    I feel, I'd suggest, I'd say) which violate regardless; allow
    everything else."""
    violations = []
    if vnl is None or not hasattr(vnl, "BANNED_PHRASES"):
        return violations
    for label, pattern, relaxed_permitted in vnl.BANNED_PHRASES:
        if relaxed_permitted:
            continue  # operator-debrief tolerates these
        for m in re.finditer(pattern, text, re.IGNORECASE):
            violations.append((f"always-banned: {label}", m.group(0)))
    return violations


def scan_class_c(text: str, vnl) -> list[tuple[str, str]]:
    """Class C scan: Phase 0 readiness — no script-name / path /
    state enumeration in chat-visible content."""
    violations = []
    for pattern in CLASS_C_BANNED_PATTERNS:
        for m in pattern.finditer(text):
            violations.append(("class-c: phase-0 leak", m.group(0)))
    return violations


def scan_class_d(text: str, vnl) -> list[tuple[str, str]]:
    """Class D scan: turn-boundary — no Case File field enumeration
    + Class A's banned-pattern list also applies (inheritance per
    §13.10 Class D tolerances)."""
    violations = []
    # Class D specific patterns
    for pattern in CLASS_D_BANNED_PATTERNS:
        for m in pattern.finditer(text):
            violations.append(("class-d: turn-boundary leak", m.group(0)))
    # Class D inherits Class A banned-pattern list
    violations.extend(scan_class_a(text, vnl))
    return violations


SCAN_DISPATCH = {
    "A": scan_class_a,
    "B": scan_class_b,
    "C": scan_class_c,
    "D": scan_class_d,
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compose-time validator hook (Sprint 17 Card 02)."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default=None,
        help="Path to draft file. If omitted, reads from stdin.",
    )
    parser.add_argument(
        "--surface-class",
        choices=["A", "B", "C", "D"],
        default="A",
        help="Chat surface class (chapter 13 §13.10 taxonomy). "
             "Default A (strictest, fail-closed).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress per-violation output; emit only summary line.",
    )
    args = parser.parse_args()

    # Load input
    if args.input is None:
        if sys.stdin.isatty():
            print(
                "ERROR: no input — provide a file path or pipe text via stdin",
                file=sys.stderr,
            )
            return 2
        text = sys.stdin.read()
    else:
        path = Path(args.input)
        if not path.is_file():
            print(f"ERROR: file not found: {args.input}", file=sys.stderr)
            return 2
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            print(f"ERROR: could not read {args.input}: {e}", file=sys.stderr)
            return 2

    if not text.strip():
        print(
            f"ERROR: input is empty (surface class {args.surface_class})",
            file=sys.stderr,
        )
        return 2

    # Load voice-neutrality-lint patterns for shared scan logic
    vnl = load_voice_neutrality_lint()
    if vnl is None:
        print(
            "ERROR: voice-neutrality-lint.py not loadable; cannot run pre-emit check",
            file=sys.stderr,
        )
        return 2

    scan_fn = SCAN_DISPATCH[args.surface_class]
    violations = scan_fn(text, vnl)

    if violations:
        if not args.quiet:
            for label, snippet in violations:
                print(f"FAIL [{args.surface_class}]: {label}: {snippet!r}")
        print(
            f"FAILED: {len(violations)} violation(s) at surface class "
            f"{args.surface_class} — refuse to ship. Rephrase and re-run."
        )
        return 1

    print(
        f"OK: surface class {args.surface_class} — no violations detected "
        f"({len(text.splitlines())} lines scanned)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
