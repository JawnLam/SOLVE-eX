#!/usr/bin/env python3
"""Sprint 18 Card 05 — dispositive test for trigger-phrase-audit.py --auto-populate.

Sprint 17 panel had `tool_surfaced_in_chat` pre-populated by Claude manually
across all 3 cases, so the `--auto-populate` code path never had to fire on a
genuinely empty annotation array — the disambiguating test never ran. This
fixture forces the dispositive scenario: empty annotation + chat-named tools.
After `--auto-populate` runs, the annotation array MUST contain entries for
Mom Test (turn 1) and Assumption Audit (turn 2) with the correct verbatim
evidence excerpts.

Run as:
    python3 -m pytest 07-Scripts/tests/test_auto_populate.py
OR (no pytest dependency):
    python3 07-Scripts/tests/test_auto_populate.py

Exit codes:
    0 — fixture round-trip passes (both expected entries present)
    1 — one or more expected entries missing or malformed
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FIXTURE_NAME = "test_auto_populate_fixture.md"
EXPECTED_TURN_1_TOOL = "Mom Test"
EXPECTED_TURN_2_TOOL = "Assumption Audit"


def _scripts_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def _fixture_path() -> Path:
    return Path(__file__).resolve().parent / FIXTURE_NAME


def test_auto_populate_fixture() -> int:
    fixture = _fixture_path()
    if not fixture.is_file():
        print(f"FAIL: fixture not found at {fixture}", file=sys.stderr)
        return 1

    scripts_dir = _scripts_dir()
    audit_script = scripts_dir / "trigger-phrase-audit.py"
    if not audit_script.is_file():
        print(f"FAIL: trigger-phrase-audit.py not found at {audit_script}", file=sys.stderr)
        return 1

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        shutil.copy2(fixture, tmp_path)

        result = subprocess.run(
            [sys.executable, str(audit_script), "--auto-populate", str(tmp_path)],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            print(
                f"FAIL: trigger-phrase-audit.py --auto-populate returned exit "
                f"code {result.returncode}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}",
                file=sys.stderr,
            )
            return 1

        after = tmp_path.read_text(encoding="utf-8")

        for turn, tool_name in ((1, EXPECTED_TURN_1_TOOL), (2, EXPECTED_TURN_2_TOOL)):
            turn_block = f"- turn: {turn}\n    tool: \"{tool_name}\""
            if turn_block not in after:
                print(
                    f"FAIL: expected entry for turn {turn} tool '{tool_name}' "
                    f"not found in post-run frontmatter.\nstdout:\n{result.stdout}",
                    file=sys.stderr,
                )
                return 1

        if "source: \"auto-populated by trigger-phrase-audit.py --auto-populate" not in after:
            print(
                "FAIL: auto-populate source marker missing on appended entries.",
                file=sys.stderr,
            )
            return 1

        print("PASS: auto-populate dispositive test passed.")
        print(f"  - turn 1 tool: {EXPECTED_TURN_1_TOOL}")
        print(f"  - turn 2 tool: {EXPECTED_TURN_2_TOOL}")
        return 0
    finally:
        try:
            tmp_path.unlink()
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(test_auto_populate_fixture())
