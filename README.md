# SOLVE eX v2.1

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v2.1-blue.svg)](VERSION.md)
[![Schema](https://img.shields.io/badge/schema-v1.14.0%20FROZEN-success.svg)](08-Schema/)
[![Master Plan](https://img.shields.io/badge/master%20plan-v3.0%20STABLE-informational.svg)](VERSION.md)

SOLVE eX is an **[operating volume](https://github.com/JawnLam/Operating-Volume-Engineering)** for AI-orchestrated decision-making and problem-solving. Point any capable AI assistant at this folder, tell it to read `AI-BOOTSTRAP.md`, and it will walk you through structured thinking on whatever is in front of you. No accounts, no servers, no subscriptions — everything runs locally against the model you already use.

> **What's an operating volume?** A self-contained markdown corpus an AI loads to orchestrate a particular kind of long-running, stateful work — the slot in the AI lexicon between a Custom GPT / Project and an AI harness. Substrate-agnostic (Claude, GPT, Gemini, etc.), stateful (files on disk are the memory), forkable. See **[Operating-Volume-Engineering](https://github.com/JawnLam/Operating-Volume-Engineering)** for the discipline and a worked-example design walkthrough. SOLVE eX is one of three operating volumes by the same author, alongside **[LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)** and **Operating-Volume-Engineering** itself.

---

## What this is

SOLVE eX is a methodology library plus an AI operating manual. The corpus contains 14 instruction chapters, 677 thinking-tool entries (schema v1.14.0 FROZEN), a 21-step process framework, question banks, five operational personas, sample sessions, and validation scripts. The instructions are written for the AI; you do not need to learn the system.

When you point an AI at the folder and ask for help thinking through something, it diagnoses where you are in your decision-making, surfaces the right thinking tool at the right moment, captures what you discover in a Case File, and walks you out the other side with clarity and an actionable plan.

The system is objective and rigorous. It does not project personality. It is a competent partner in thinking — nothing more, nothing less.

## Examples of what it can help with

- **Decisions under uncertainty** — picking between roles, partners, products, paths when the data is incomplete and the stakes are real.
- **Problem decomposition** — turning a vague "something is wrong" into a structured map of root causes, leverage points, and tractable next steps.
- **Structured thinking under time pressure** — fast reasoning when the deadline doesn't care about your decision quality.
- **Stakeholder dynamics** — mapping interests, power, leverage, and likely responses before a hard conversation or negotiation.
- **Reframing stuck situations** — surfacing the assumptions and frames that are quietly limiting the option set.
- **Risk and reversibility** — distinguishing one-way doors from two-way doors before you walk through.
- **High-stakes life decisions** — career pivots, relationships, geography, money — with appropriate safety routing when stakes warrant a licensed professional.
- **Strategy under adversarial conditions** — competitive moves, asymmetric situations, and games where the other player is also thinking.

## Quick start

You just cloned (or downloaded) this repository. Here is how to use it.

### 1. Open the folder in your AI environment

The corpus is plain markdown plus a few Python utility scripts. Any environment where your AI assistant can read local files works:

- **Claude Code** (CLI) — `cd` into the folder and start a session
- **Claude Desktop** — drag the folder into a project
- **ChatGPT / Gemini / other web UIs** — upload the folder or its files
- **VS Code / Cursor / similar IDEs** — open the folder; use the AI side-panel

### 2. Tell the AI to bootstrap

In your first message, say:

> **"Read `AI-BOOTSTRAP.md` and then help me think through something."**

The AI completes Phase 0 pre-flight (core chapter reads, environment checks, session-mode declaration) and responds with a short readiness statement. This takes about 30 seconds.

### 3. Describe what is on your mind

Plain language. As specific or vague as you like. The AI takes it from there — diagnosing, picking a thinking tool, asking the questions that move you forward, and recording what surfaces in a Case File.

You do not need to learn the system. `AI-BOOTSTRAP.md` instructs the AI; the AI meets you where you are.

For environment setup details and integrity verification, see [`INSTALL.md`](INSTALL.md).

## System requirements

- **AI assistant** — any model capable of reading markdown and parsing YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above).
- **OS** — Mac, Windows, or Linux.
- **Python** — 3.10 or newer, required only for the optional utility scripts in `07-Scripts/` (validation, audit, session management).
- **Python dependencies** — `pyyaml` only. No other third-party packages are used by any script in the corpus.
- **Network** — none required. The corpus is self-contained; nothing is fetched at runtime.
- **Disk** — read access to the folder; write access to `06-Case-Files/_ACTIVE/` if persistent session storage is desired (otherwise the AI declares sandbox mode and keeps Case File state inline).

## Which file do I read?

There are eight top-level files in this folder. Each has a distinct audience and purpose — read the one that matches what you're trying to do:

- **You want to use the system**: read this `README.md`, then [`INSTALL.md`](INSTALL.md) if you're setting up fresh. Once set up, point any AI at the folder and say "read `AI-BOOTSTRAP.md` and help me think through something."
- **You're an operator running sessions** for yourself or others: read [`OPERATOR-GUIDE.md`](OPERATOR-GUIDE.md) — it covers runtime operation, validation scripts, common failure modes, and the v3.0 STABLE freeze policy.
- **You're extending or modifying the protocol**: read [`CONTRIBUTING.md`](CONTRIBUTING.md) — it describes what's in-scope at v3.0 STABLE vs. what requires a v3.x master plan version bump.
- **You need version info**: [`VERSION.md`](VERSION.md) (current release identifiers and schema-freeze policy) and [`CHANGELOG.md`](CHANGELOG.md) (history of releases).
- **You're the AI on session boot**: [`AI-BOOTSTRAP.md`](AI-BOOTSTRAP.md) (frontmatter `audience: ai`, `read_order: 0`) — this is the pre-flight reading list.
- **Legal / usage terms**: [`LICENSE.md`](LICENSE.md) — CC-BY 4.0.

## Folder structure

| Folder              | Contents                                                 |
|---------------------|----------------------------------------------------------|
| `00-Instructions/`  | Operating manual — 14 numbered chapters + dependency index |
| `01-Tools/`         | 677 thinking-tool entries (v1.14.0 schema)               |
| `02-Process-Framework/` | SOLVE eX methodology spec — 6 phases / 21 steps      |
| `03-Question-Banks/`| Question repertoire (by phase-step + by clarification need) |
| `04-Application-Patterns/` | How to apply tools conversationally               |
| `05-Personas/`      | Five operational personas + switching rules              |
| `06-Case-Files/`    | Session storage — `_TEMPLATE.md` only in this public release |
| `07-Scripts/`       | Utility scripts (Python 3.10+, pyyaml only)              |
| `08-Schema/`        | Schema definitions and validation rules                  |
| `09-Sample-Sessions/`| Annotated demonstration transcripts                     |
| `10-Reference/`     | Glossary, FAQ, supplementary material                    |

Top-level files: `AI-BOOTSTRAP.md` (AI bootstrap entry point), `VERSION.md` (release metadata), `LICENSE.md` (CC-BY 4.0), `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`.

## Where to go for what

| If you want to…                                          | Read…                                                  |
|----------------------------------------------------------|--------------------------------------------------------|
| Have the AI run a session for you                        | Nothing — just tell the AI to read `AI-BOOTSTRAP.md`     |
| Understand the cognitive model behind the system         | `00-Instructions/01-the-cognitive-model.md`            |
| Understand how the AI opens a session                    | `00-Instructions/02-the-bootstrap-protocol.md`         |
| Understand the diagnostic loop                           | `00-Instructions/03-the-diagnostic-loop.md`            |
| Understand how the AI picks a tool                       | `00-Instructions/04-the-tool-selection-process.md`     |
| Understand the Case File (session storage)               | `00-Instructions/06-the-case-file.md`                  |
| Understand safety routing                                | `00-Instructions/09-safety-and-stakes.md`              |
| Understand session modes (production / test / sandbox)   | `00-Instructions/14-session-modes.md`                  |
| Browse the thinking-tool library                         | `01-Tools/Tool Entries/` (one markdown file per tool)  |
| See the 21-step process framework                        | `02-Process-Framework/`                                |
| Try a sample session                                     | `09-Sample-Sessions/`                                  |
| Look up glossary or FAQ                                  | `10-Reference/`                                        |
| Run integrity checks on the corpus                       | `07-Scripts/` (see `INSTALL.md` for pre-flight script invocation) |
| Operate, maintain, or extend the system                  | `OPERATOR-GUIDE.md`                                    |
| Contribute changes                                       | `CONTRIBUTING.md`                                      |
| See what changed between releases                        | `CHANGELOG.md`                                         |

## Maintenance and versioning

- **Software / corpus release** — see [`VERSION.md`](VERSION.md) and [`CHANGELOG.md`](CHANGELOG.md). Tagged at v2.0 (ship release) and v2.1.0 (minor release — ADAPT Loop Integration).
- **Master plan version** — v3.0 STABLE. The master plan specification (the document governing schema, chapter structure, persona contracts, and validator behavior) is frozen at v3.0. Schema (v1.14.0) and validator behavior are locked at this version.
- **Future protocol changes** — once v3.0 STABLE is stamped, further changes require an explicit v3.x bump and a documented migration path. Patch-level fixes (typos, doc clarifications, additional sample sessions, additional tool entries within the existing schema) do not require a version bump.
- **Schema compatibility** — schema v1.14.0 is locked. If you have written tool entries against this schema, future v3.x bumps will provide a migration crosswalk and a migration script in `07-Scripts/`.

## What this is not

- Not a substitute for professional services. The AI is a thinking-tools companion. For mental health crises, legal jeopardy, medical emergencies, financial catastrophes, and other high-stakes situations, the AI routes you to appropriate professionals per `00-Instructions/09-safety-and-stakes.md`.
- Not a marketing pitch. The system either helps or it does not.
- Not a static document. Schema, manual chapters, question banks, patterns, and personas evolve through versioned releases.
- Not opinionated about what you should decide. The AI guides; you decide.

## License

SOLVE eX v2.0 is released under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share, adapt, and build upon this material for any purpose — including commercially — provided you give appropriate attribution.

See [`LICENSE.md`](LICENSE.md) for the full license text. Attribution format:

> Built on **SOLVE eX v2.0** by Jawn Lam — https://github.com/JawnLam/SOLVE-eX
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Version

See [`VERSION.md`](VERSION.md) for current release metadata, included components, and compatibility matrix. This is the **v2.0 ship release** with master plan v3.0 STABLE and schema v1.14.0 FROZEN.
