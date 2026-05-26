#!/usr/bin/env python3
"""post-session-audit.py — orchestrate per-Case-File audit scripts.

Reads the Case File's `audit_scripts` frontmatter field (list of script
filenames in 07-Scripts/) and invokes each against the Case File. Emits
a consolidated pass/fail report. Exits 0 only when all child scripts
exit 0.

Sprint 13 Tessa Claude debrief flagged self-compliance-theater: the
Case File declared which audits would run but nothing executed them.
This script is the runtime hook chapter 06 §6.13 now requires the AI to
invoke before producing the close turn.

Usage:
  python3 07-Scripts/post-session-audit.py <case-file-path>
  python3 07-Scripts/post-session-audit.py <case-file-path> --quiet
  python3 07-Scripts/post-session-audit.py <case-file-path> --log

Exit codes:
  0 = all child scripts exited 0
  1 = at least one child script exited non-zero (any audit failure)
  2 = invalid Case File (no audit_scripts field, frontmatter parse
      failure, file not found, audit_scripts entry is not a string)

Output:
  - stdout: consolidated summary (script-name, exit-code, brief tail)
  - --log:  writes the same summary to
            <case-file-dir>/<case-file-id>--audit.log

Design constraints (v28+v30 — Sprint 14 Card 05):

  1. Aggregation: defaultdict(list) keyed by script-name for results
     (supports future repeat-invocation patterns; single-pass here).
  2. Exit-code semantics: 0/1/2 per usage above. Child exit codes are
     preserved per-script in the report and aggregated into a single
     overall exit code.
  3. Output: stdout always (unless --quiet); log file optional via
     --log flag. Log path is derived from case_file_id so multiple
     CFs in the same directory don't collide.
  4. Idempotent: rerunning produces the same output. The report
     contains no per-run timestamps — only the script name, exit
     code, and tail of script output. This makes diff-based change
     detection across reruns meaningful.
  5. Mode-aware: when invoking voice-neutrality-lint.py, reads the
     CF's `detection_check.relaxed_scaffolding` flag and passes
     --mode relaxed or --mode standard accordingly. Mode-aware
     scripts are tracked in the MODE_AWARE_SCRIPTS set.

Cross-references:
  - chapter 06 §6.13 close protocol (the invocation requirement)
  - chapter 13 §13.2 "close turn produced without invoking audit
    scripts" (the failure-mode entry)
  - 06-Case-Files/_TEMPLATE.md (the audit_scripts default list)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent

# Scripts that accept a --mode {standard|relaxed} argument and whose
# behavior depends on the CF's relaxed_scaffolding flag. Add new
# mode-aware scripts here as they ship.
MODE_AWARE_SCRIPTS = {"voice-neutrality-lint.py"}

# Subprocess timeout per child script (seconds). Long enough for
# corpus-scale walks on Dropbox CloudStorage paths; short enough that
# a runaway script doesn't hang the close turn indefinitely.
CHILD_TIMEOUT_SECONDS = 120


def parse_frontmatter(text: str) -> tuple[dict | None, str | None]:
    """Return (fm_dict, error_message). On error, fm_dict is None."""
    if not text.startswith("---\n"):
        return None, "no frontmatter (file does not start with '---')"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unterminated frontmatter (no closing '---')"
    try:
        fm = yaml.safe_load(text[4:end])
    except yaml.YAMLError as e:
        return None, f"YAML parse failure: {e}"
    if not isinstance(fm, dict):
        return None, "frontmatter is not a YAML mapping"
    return fm, None


def find_relaxed_scaffolding(fm: dict, body: str) -> bool:
    """Return True iff detection_check.relaxed_scaffolding is True.

    Looks in frontmatter first, then in fenced ```yaml blocks in body.
    Mirrors validate-case-file.py find_detection_check_in_body
    discipline; bare top-level detection_check: blocks are out of scope
    here (frontmatter / fenced are the canonical Case File renderings).
    """
    dc = fm.get("detection_check")
    if isinstance(dc, dict) and dc.get("relaxed_scaffolding") is True:
        return True
    for block in re.findall(r"```ya?ml\s*\n(.*?)\n```", body, re.DOTALL):
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            dc2 = data.get("detection_check")
            if isinstance(dc2, dict) and dc2.get("relaxed_scaffolding") is True:
                return True
    return False


def build_invocation(
    script_name: str, case_file_path: Path, relaxed: bool
) -> list[str]:
    """Build the subprocess argv for a given audit script."""
    script_path = SCRIPTS_DIR / script_name
    argv = ["python3", str(script_path), str(case_file_path)]
    if script_name in MODE_AWARE_SCRIPTS:
        argv.extend(["--mode", "relaxed" if relaxed else "standard"])
    return argv


def _summarize_tail(stdout: str, stderr: str) -> str:
    """Return a short tail string summarizing the script's output."""
    combined = (stdout + "\n" + stderr).strip()
    tail_lines = [ln for ln in combined.split("\n") if ln.strip()]
    # Prefer lines that name a result; fall back to the last non-empty line.
    for marker in ("FAILED", "FAIL", "OK", "WARN", "error"):
        matched = [ln for ln in tail_lines if marker in ln]
        if matched:
            return matched[-1][:200]
    return (tail_lines[-1] if tail_lines else "(no output)")[:200]


def _gap_acknowledges_violation(
    script_name: str,
    child_stdout: str,
    known_gaps: list,
) -> tuple[bool, list[str]]:
    """Sprint 17 Card 08: check whether an audit_known_coverage_gaps
    entry acknowledges this child script's exit 1. Returns
    (acknowledged, matched_phrases) — acknowledged is True if every
    flagged-phrase quoted in the child's stdout matches some documented
    gap for this script; matched_phrases lists the matched flagged
    phrases for logging.

    Pragmatic heuristic: scan child_stdout for any documented
    flagged_phrase. If at least one match found AND the child reports
    failures only on documented phrases (best-effort check), accept as
    acknowledged. Otherwise treat as real failure.
    """
    if not isinstance(known_gaps, list) or not known_gaps:
        return False, []
    matched: list[str] = []
    for entry in known_gaps:
        if not isinstance(entry, dict):
            continue
        if (entry.get("script") or "").strip() != script_name:
            continue
        flagged = (entry.get("flagged_phrase") or "").strip()
        if not flagged:
            continue
        if flagged.lower() in child_stdout.lower():
            matched.append(flagged)
    return (len(matched) > 0), matched


def run_audit(
    case_file_path: Path,
) -> tuple[int, list[tuple[str, int, str]]]:
    """Run all audit_scripts listed in the CF's frontmatter.

    Returns (overall_exit, results) where:
      overall_exit = 0 (all child scripts exited 0 OR all non-zero
                       child exits were acknowledged by
                       audit_known_coverage_gaps per Sprint 17 Card 08)
                   | 1 (any child non-zero without gap acknowledgment)
                   | 2 (invalid CF / missing audit_scripts)
      results = list of (script_name, exit_code, tail_summary) tuples,
                ordered the same as the audit_scripts list. Tail
                summary includes a "(GAP ACK)" suffix when the child's
                non-zero exit was acknowledged by a documented gap.
    """
    try:
        text = case_file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        print(f"ERROR: could not read {case_file_path}: {e}", file=sys.stderr)
        return 2, []
    fm, err = parse_frontmatter(text)
    if fm is None:
        print(f"ERROR: {case_file_path.name}: {err}", file=sys.stderr)
        return 2, []
    audit_scripts = fm.get("audit_scripts")
    if not isinstance(audit_scripts, list) or not audit_scripts:
        print(
            f"ERROR: {case_file_path.name}: missing or empty "
            f"'audit_scripts' frontmatter field. Add per chapter 06 "
            f"§6.13 / Case File template default list.",
            file=sys.stderr,
        )
        return 2, []
    end = text.find("\n---\n", 4)
    body = text[end + 5:] if end != -1 else ""
    relaxed = find_relaxed_scaffolding(fm, body)
    known_gaps = fm.get("audit_known_coverage_gaps") or []

    results: list[tuple[str, int, str]] = []
    aggregated: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)
    overall = 0
    for entry in audit_scripts:
        if not isinstance(entry, str):
            tag = repr(entry)
            results.append((tag, 2, "invalid entry (not a string)"))
            aggregated[tag].append((2, "non-string entry"))
            overall = 1
            continue
        script_name = entry
        argv = build_invocation(script_name, case_file_path, relaxed)
        try:
            proc = subprocess.run(
                argv,
                capture_output=True,
                text=True,
                timeout=CHILD_TIMEOUT_SECONDS,
            )
        except FileNotFoundError:
            results.append((script_name, 2, "script not found in 07-Scripts/"))
            aggregated[script_name].append((2, "script not found"))
            overall = 1
            continue
        except subprocess.TimeoutExpired:
            results.append(
                (script_name, 2, f"timed out after {CHILD_TIMEOUT_SECONDS}s")
            )
            aggregated[script_name].append((2, "timeout"))
            overall = 1
            continue
        tail = _summarize_tail(proc.stdout, proc.stderr)
        # Sprint 17 Card 08: gap acknowledgment downgrade.
        if proc.returncode != 0 and known_gaps:
            acknowledged, matched = _gap_acknowledges_violation(
                script_name, proc.stdout + "\n" + proc.stderr, known_gaps
            )
            if acknowledged:
                tail = f"{tail} (GAP ACK: {', '.join(repr(m) for m in matched)})"
                results.append((script_name, proc.returncode, tail))
                aggregated[script_name].append((proc.returncode, tail))
                # Do NOT escalate overall to 1 — the gap acknowledgment
                # downgrades the child exit-non-zero from FAIL to INFO.
                continue
        results.append((script_name, proc.returncode, tail))
        aggregated[script_name].append((proc.returncode, tail))
        if proc.returncode != 0:
            overall = 1
    return overall, results


def format_report(
    case_file_path: Path, overall: int, results: list[tuple[str, int, str]]
) -> str:
    lines = [f"post-session-audit.py — {case_file_path.name}"]
    lines.append(f"overall: {'PASS' if overall == 0 else 'FAIL'}")
    lines.append("")
    for name, code, tail in results:
        marker = "  ok  " if code == 0 else "  FAIL"
        lines.append(f"{marker}  {name:35s} exit={code}  {tail}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Orchestrate per-Case-File audit scripts."
    )
    parser.add_argument(
        "path", type=Path, help="Path to a Case File .md file"
    )
    parser.add_argument(
        "--log",
        action="store_true",
        help=(
            "Write audit log to "
            "<case-file-dir>/<case-file-id>--audit.log "
            "(idempotent — overwrites on each run)"
        ),
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress stdout report (exit code only)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=3,
        metavar="N",
        help=(
            "Maximum number of audit-iteration markers to honor before "
            "triggering bound-mode behavior (Sprint 16 Card 05 remediation "
            "loop bound). Default 3. The flag is informational to callers "
            "(the audit itself does not run remediation loops — that is "
            "the AI's responsibility); --bound-mode determines exit-code "
            "semantics when the AI has hit the bound. To indicate that "
            "this run is the post-bound check, callers should also set "
            "AUDIT_LOOP_HIT_BOUND=1 in the environment."
        ),
    )
    parser.add_argument(
        "--bound-mode",
        choices=("strict", "lenient"),
        default="lenient",
        help=(
            "Behavior when the audit-iteration bound has been hit (signaled "
            "via AUDIT_LOOP_HIT_BOUND=1 environment variable) AND the audit "
            "still exits non-zero (Sprint 16 Card 05). strict: exit 2 (treat "
            "unbounded loop as invalid input — refuse to close). lenient: "
            "exit 1 (treat as normal audit failure) PLUS emit a "
            "BOUND-LOOP-UNCONVERGED diagnostic so the AI knows to surface "
            "the structural issue per §6.13 step 0 remediation-bound rule."
        ),
    )
    args = parser.parse_args()

    path: Path = args.path
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    overall, results = run_audit(path)
    if overall == 2:
        return 2
    report = format_report(path, overall, results)
    # Sprint 16 Card 05: bound-mode handling. The script signals
    # the AI that a remediation-bound has been hit so the AI can
    # follow the §6.13 step 0 structural-issue surfacing path
    # instead of continuing to patch.
    import os as _os
    bound_hit = _os.environ.get("AUDIT_LOOP_HIT_BOUND") == "1"
    if bound_hit and overall != 0:
        report = (
            report
            + f"\n\nBOUND-LOOP-UNCONVERGED: --max-iterations={args.max_iterations} "
            f"reached and audit still exits {overall}. Per Sprint 16 Card 05, "
            f"surface the structural issue to the user via the §6.13 step 0 "
            f"template rather than continuing to patch. Log "
            f"audit_remediation_unbounded=true + audit_remediation_iterations="
            f"{args.max_iterations} in the Case File frontmatter."
        )
    if not args.quiet:
        print(report)
    if args.log:
        try:
            fm, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
            cf_id = (fm or {}).get("case_file_id") or path.stem
        except Exception:
            cf_id = path.stem
        log_path = path.parent / f"{cf_id}--audit.log"
        try:
            log_path.write_text(report + "\n", encoding="utf-8")
        except OSError as e:
            print(f"WARN: could not write audit log {log_path}: {e}", file=sys.stderr)
    if bound_hit and overall != 0 and args.bound_mode == "strict":
        return 2
    return overall


if __name__ == "__main__":
    sys.exit(main())
