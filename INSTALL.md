# SOLVE eX v2.0 — Install Guide

This is the step-by-step setup for a fresh installation. Once setup is
complete, a downstream user only ever needs `README.md` + `AI-BOOTSTRAP.md` —
the AI handles everything else at runtime.

## 1. Get the corpus

Copy the entire `SOLVE eX v2.0/` folder to local disk in a location your AI
assistant can read. Common choices:

- Cloud-synced folder (Dropbox, iCloud, OneDrive) — convenient if you want the
  same corpus available across devices and AI environments.
- Project folder inside a code editor (VS Code, JetBrains) — convenient if you
  plan to run sessions via Claude Code or a similar in-editor agent.
- Plain local folder — works for any AI environment that supports
  file-attachment uploads.

The folder is fully self-contained. No `git clone` is required; no network
fetch happens at runtime; no path is hard-coded into the corpus. Move it
anywhere readable.

## 2. Verify Python and dependencies

The runtime use of SOLVE eX (an AI reading the corpus and conducting a
session) requires **no Python at all**. Python is needed only for the
**optional** utility scripts in `07-Scripts/` (validation, audit, session
management).

If you want the scripts to be available:

```bash
python3 --version          # must be 3.10 or newer
python3 -c "import yaml"   # must succeed (no output = success)
```

If `import yaml` fails:

```bash
pip3 install pyyaml
```

That is the only third-party Python dependency in the corpus. The scripts use
nothing else beyond the Python standard library.

## 3. Run pre-flight integrity checks

These confirm the corpus reached you intact. Run from the corpus root.

**Phase 0 sync check** — verifies the root `AI-BOOTSTRAP.md` Phase 0 section
matches the canonical mirror in `00-Instructions/00-start-here.md`. Exit 0 =
in sync.

```bash
python3 07-Scripts/check-phase0-sync.py
```

**Tool-entry schema validation** — spot-check one or more tool entries
against the v1.14.0 schema. Exit 0 = pass.

```bash
python3 07-Scripts/validate-tool.py "01-Tools/Tool Entries/Eisenhower Matrix.md"
```

**Regex coverage test** — verifies the voice-neutrality lint regex sets
fully cover their canonical spec entries (chapter 13 §13.2 invitation
patterns + §13.10 Class A composition-meta patterns). Exit 0 = full coverage.

```bash
python3 07-Scripts/test-regex-coverage.py
```

If any of the three return a non-zero exit code, the corpus has drifted
from a known-good state. Inspect the script output to identify the gap. Do
not proceed to a real session against a drifted corpus — open
`CONTRIBUTING.md` for the repair workflow, or re-copy the corpus from a
known-good source.

Additional scripts in `07-Scripts/` (`validate-case-file.py`,
`cross-chapter-dependency-audit.py`, `voice-neutrality-lint.py`,
`case-file-placeholder-lint.py`, `trigger-phrase-audit.py`,
`artifact-quality-audit.py`, `post-session-audit.py`, `portability-check.py`)
are documented in `07-Scripts/README.md` and `OPERATOR-GUIDE.md`. They are
not required for first-session use.

## 4. First session walkthrough

1. **Confirm Case File destination is writable.** Verify
   `06-Case-Files/_ACTIVE/` exists and your AI environment can write to it.
   If not (read-only mount, sandbox chat, restricted AI environment), no
   action needed — the AI will detect this in Phase 0 and declare **sandbox
   mode** (Case File state lives as inline markdown blocks in the conversation
   rather than on disk).

2. **Open the corpus in your AI environment.** Point Claude Code / Claude
   Desktop / ChatGPT-with-files / your IDE-integrated agent at the folder.

3. **Trigger the AI bootstrap.** Send the AI a single message:

   > Read `AI-BOOTSTRAP.md` and then help me think through something.

   The AI will execute Phase 0 pre-flight — reading the core seven chapters
   from `00-Instructions/`, verifying environment access to scripts and Case
   Files, and declaring its session mode (production / test / sandbox /
   multi-session-resumption per chapter 14).

4. **Wait for the readiness statement.** The AI's first response should be a
   short user-facing paragraph confirming readiness (e.g., "Pre-flight is
   ready. The core chapters have been internalized; Case File storage is
   available and the validation scripts are loaded. Ready for your first
   message."). The audit-trail detail (which chapters were read, which
   scripts are loaded, session mode) goes into the Case File `pre_flight:`
   frontmatter block — not the chat.

   If the AI responds with anything other than a readiness statement on
   turn 1 — a greeting, a question, an artifact, an explanation — it has
   skipped Phase 0. Stop and restart the session.

5. **Describe what is on your mind.** From here, the AI guides you through
   the SOLVE eX diagnostic loop. You do not need to know which phase or
   step you are in; the AI tracks it in the Case File.

## 5. Troubleshooting

| Symptom                                                | Likely cause / resolution                                                                                                            |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `python3: command not found`                           | Python not installed. Install Python 3.10+ via your OS package manager or python.org.                                                |
| `ModuleNotFoundError: No module named 'yaml'`          | `pip3 install pyyaml`.                                                                                                               |
| `check-phase0-sync.py` exits 1 (sections diverge)      | Root `AI-BOOTSTRAP.md` and the chapter-00 mirror have drifted. The chapter-00 copy wins; re-copy from a known-good source.             |
| `validate-tool.py` exits 1 on every tool               | Schema file `08-Schema/` is missing or corrupted. Re-copy `08-Schema/` from a known-good source.                                     |
| `test-regex-coverage.py` exits 1                       | `voice-neutrality-lint.py` has fallen out of parity with the spec. See `CONTRIBUTING.md` for the repair workflow.                    |
| AI never produces a readiness statement                | AI may not have read `AI-BOOTSTRAP.md`. Re-send the bootstrap message explicitly: "Read `AI-BOOTSTRAP.md` in full before responding."    |
| AI produces a readiness statement but then loses state | Case File was not initialized. Check that `06-Case-Files/_ACTIVE/` is writable, OR confirm the AI declared sandbox mode in Phase 0.  |
| AI declares sandbox mode unexpectedly                  | `06-Case-Files/_ACTIVE/` is not writable from the AI's environment. Either fix the permissions or accept sandbox mode for the session.|

For deeper operational and maintenance guidance, see `OPERATOR-GUIDE.md`.
For contribution workflow (adding tools, extending chapters, fixing regex
drift), see `CONTRIBUTING.md`.

## Version

This install guide ships with SOLVE eX v2.0.0. See `VERSION.md` for full
release metadata.
