#!/usr/bin/env python3
"""voice-neutrality-lint.py — scan a markdown file for first-person
expertise-drift phrases banned by chapter 13 §13.2 check (3) AND
infrastructure-announcement leaks (chapter 13 §13.3, Sprint 14 Card 03).

Usage:
    python3 07-Scripts/voice-neutrality-lint.py <path>
    python3 07-Scripts/voice-neutrality-lint.py <path> --threshold 1
    python3 07-Scripts/voice-neutrality-lint.py <path> --mode relaxed
    python3 07-Scripts/voice-neutrality-lint.py <path> --scope chat-only

Exit codes:
    0  no drift detected (or all phrase counts within threshold)
    1  drift detected (one or more banned phrases over threshold,
       OR any infrastructure-announcement leak — those bypass threshold)
    2  invalid input (file not found, unreadable, etc.)

Scope semantics (Sprint 16 Card 02 — chapter 13 §13.3 scope sub-section):
    --scope auto      (default): if the file contains any
        ^AI [persona]: line (canonical Session Log AI-output marker),
        treat it as a Case File and scan ONLY the AI chat-output spans
        between AI [persona]: lines and the next User:/heading/section-
        boundary. Lines outside chat-output spans (Diagnostic blocks,
        Voice-neutrality annotations, quality_check_corrections YAML,
        Tools Applied entries, Next Steps prose, Library status notes,
        audit-history narration, YAML frontmatter, Frame sections) are
        SKIPPED — those sections are exactly the audit / record-keeping
        content that §6.13 step 0 explicitly REQUIRES the AI to write,
        so the lint must not penalize them. If the file has no
        ^AI [persona]: line, scan all eligible lines (chapter-prose
        backward compat preserved).
    --scope all       force-scan all lines regardless of structure
        (legacy behavior; useful for chapter-prose runs).
    --scope chat-only force AI-chat-only scope even on files without a
        ^AI [persona]: line (useful for fragment scans).

Detection rules:
    - Regex match, case-insensitive, word-boundary aware
    - "I thinks" does NOT match "I think"
    - Banned phrases are scanned per-line; one count per match
    - Quoted user content (lines starting with '> ' or 'User:' or
      inside a fenced code block) is EXCLUDED — banned phrases inside
      user-voice content are not drift (the AI quoting the user does
      not violate voice neutrality)
    - Text inside inline backticks (`like this`) is EXCLUDED — this
      is markdown inline code, typically used to cite the banned
      phrase itself as documentation
    - Markdown table rows (lines matching `^\\s*\\|.*\\|`) are EXCLUDED
      when the row defines/documents the banned phrase rather than
      uses it in operational prose

Mode semantics (Sprint 12 Card 06):
    --mode standard  (default): banned phrases are always violations.
        Use for chapter prose AND for standard-mode session transcripts.
    --mode relaxed:  permission-context windows are honored — a user
        utterance containing an explicit invitation ("what do you think,"
        "give me your read," "give it to me straight," "what would you
        actually recommend," etc.) opens a one-paragraph window in the
        AI's immediately-following response. Within the window, ONE
        first-person stance phrase from the permitted set {I think, my
        read, honest read} is allowed; any second instance within the
        same window AND any instance outside any window is a violation.
        The "always banned" phrases (I'd want, I feel, I'd suggest, I'd
        say) violate regardless of mode or window. Use for relaxed-mode
        session transcripts (chapter 13 §13.2 sophisticated-user
        detection fired and Case File flag relaxed_scaffolding: true).
"""
import argparse
import re
import sys
from pathlib import Path

# Phrase metadata: label, detection regex, relaxed-mode permitted?
# Phrases marked relaxed_permitted=True may appear once inside an open
# permission-context window in --mode relaxed; all others always violate.
BANNED_PHRASES = [
    ("I think", r"\bI think\b", True),
    ("I'd want", r"\bI[' ]d want\b", False),
    ("my read", r"\bmy read\b", True),
    ("honest read", r"\bhonest read\b", True),
    ("I feel", r"\bI feel\b", False),
    ("I'd suggest", r"\bI[' ]d suggest\b", False),
    ("I'd say", r"\bI[' ]d say\b", False),
]


INLINE_CODE_RE = re.compile(r"`[^`]*`")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|")
# Match double-quoted strings (straight " and curly ") on a line. The pattern
# uses lookahead-style termination via the negated-character class on the same
# quote char it opened with — `"[^"]*"` for straight quotes and `"[^"]*"` for
# curly quotes. Greedy matching across line boundaries is avoided by working
# line-by-line in scan_file.
DOUBLE_QUOTED_RE = re.compile(r'"[^"]*"|"[^"]*"')

# Sprint 15 Card 08: single-quoted strings, applied ONLY when the line has a
# meta-mention context (see META_MENTION_CONTEXT_RE). Unconditional single-
# quote stripping would eat legitimate apostrophes (contractions like
# "don't", possessives like "Marcus's") — but in audit-narration contexts,
# `'honest read'` (line 489 of Sprint 14 Tessa CF) is a meta-mention of a
# banned phrase, not a use of it. Length-bounded (1–80 chars) to keep
# multi-line apostrophe-traps from over-matching.
SINGLE_QUOTED_RE = re.compile(r"'[^'\n]{1,80}'|'[^'\n]{1,80}'|‘[^’\n]{1,80}’")

# Sprint 15 Card 08: meta-mention context detector. When a line matches one
# of these patterns, the banned-phrase scan treats single-quoted regions on
# the SAME LINE as meta-mentions and skips them. Recognized contexts:
#   - audit / lint narration ("the voice-neutrality lint flagged ...")
#   - phrase-discussion shapes ("the phrase 'X' is", "the violation was")
#   - audit catch + variants ("audit catch", "lint catch")
META_MENTION_CONTEXT_RE = re.compile(
    r"\b("
    r"voice[- ]neutrality\s+lint|"
    r"audit\s+catch|"
    r"lint\s+(?:flagged|caught|fired|surfaced|exited)|"
    r"audit\s+(?:flagged|caught|fired|surfaced|exited)|"
    r"the\s+phrase\b|"
    r"the\s+violation\s+(?:was|is)|"
    r"banned\s+phrase|"
    r"flagged\s+in\s+(?:my|the)\s+(?:last|previous)\s+turn|"
    r"meta[- ]mention|"
    r"quoted\s+occurrence|"
    r"reads\s+stronger\s+than"
    r")\b",
    re.IGNORECASE,
)

# Permission-context invitation patterns (relaxed mode only).
# These match user utterances that explicitly invite the AI's stance.
# Lookahead-based bounds — no character-class exclusion (per
# trelloplan-resume v34 prescription).
#
# Sprint 15 Card 09 extension: process-direct-read invitations
# (chapter 03 §3.10) — user utterances asking the AI to read the
# *process* (am I overthinking, am I missing X, is my analysis off,
# is this overdone). These are direct-read invitations on the
# meta-process layer rather than the content layer. The permission
# window they open is the same: one first-person stance phrase in
# the AI's immediately-following response.
# Content-direct-read invitations (§13.2 exception block + §13.2 table
# "Honest read" / "My read" rows). Open the permission-context window
# in RELAXED MODE only — standard-mode content-direct-read responses do
# not get a stance opener (the "what do you think?" exception applies
# only to sophisticated-user relaxed-scaffolding sessions).
#
# Sprint 17 Card 04 §13.2 audit: regex set extended to close
# "what is your read" + "honestly, what should I do" gaps surfaced
# by exhaustive §13.2-invitation enumeration test.
INVITATION_PATTERNS_CONTENT = [
    re.compile(r"\bwhat do you think\b", re.IGNORECASE),
    re.compile(r"\bwhat would you (do|recommend|advise|suggest|say)\b", re.IGNORECASE),
    re.compile(r"\b(give|tell) me (your|the) (read|take|honest read|bottom line|straight answer)\b", re.IGNORECASE),
    re.compile(r"\b(give|tell) it to me straight\b", re.IGNORECASE),
    re.compile(r"\bwhat(?:'?s|s| is) (your|the) (read|take|honest call|bottom line)\b", re.IGNORECASE),
    re.compile(r"\bhonest(ly)?[\s,—-]+what\b", re.IGNORECASE),
    re.compile(r"\bwhat(?:'?s|s| is) (your )?honest (call|read|take)\b", re.IGNORECASE),
    re.compile(r"\bwhat would you actually (recommend|do|say)\b", re.IGNORECASE),
]

# Process-direct-read invitations (Sprint 15 Card 09 — chapter 03 §3.10
# + Sprint 17 Card 07 mode-parity extension). Open the permission-context
# window in BOTH standard mode AND relaxed mode per Sprint 17 Card 07.
# Sprint 14 Tessa "am I overthinking this?" is the canonical case; Sprint
# 16 Mara "how do I figure out which one is right first?" / "am I
# distracting myself?" are the standard-mode parallel cases that motivate
# the mode-parity extension.
INVITATION_PATTERNS_PROCESS = [
    re.compile(r"\bam I (?:overthinking|over[- ]thinking|under[- ]thinking|"
               r"being too careful|being too cautious|over[- ]preparing|"
               r"under[- ]preparing|over[- ]reading|under[- ]reading|"
               r"distracting (?:myself|me)|"
               r"rationalizing|over[- ]weighting|"
               r"missing (?:something|anything|the point))\b", re.IGNORECASE),
    re.compile(r"\bam I missing (?:something|anything)\b", re.IGNORECASE),
    re.compile(r"\bis this (?:overdone|too much|enough|right|over[- ]engineered|under[- ]done)\b", re.IGNORECASE),
    re.compile(r"\bis my (?:thinking|read|analysis|approach|framing) off\b", re.IGNORECASE),
    # Sprint 17 Card 07: process-direct-read sequencing/prioritization
    # pattern (Sprint 16 Mara canonical: "how do I figure out which one is
    # right first?")
    re.compile(r"\bhow do I figure out which (?:one|of these|approach)?\s*(?:is right|to (?:start|prioritize|do first))?(?:\s*first)?\b", re.IGNORECASE),
]

# Aggregate list — preserves the pre-Sprint-17 external API. Other
# callers (test-regex-coverage.py, downstream tooling) consume this.
INVITATION_PATTERNS = INVITATION_PATTERNS_CONTENT + INVITATION_PATTERNS_PROCESS

# AI speaker line pattern (paragraph start marker for permission window).
AI_LINE_RE = re.compile(r"^AI\s*(?:\[[^\]]+\])?\s*(?:\([^)]+\))?\s*:", re.IGNORECASE)
USER_LINE_RE = re.compile(r"^(User|user)\s*:")

# Sprint 16 Card 02: strict AI chat-output line marker. Used for positive
# scope detection (chat-only mode) — lines matching this pattern OPEN an
# AI chat-output span that stays open until the next User: line, markdown
# heading, or Case File body section marker (SECTION_BOUNDARY_PATTERNS).
# Requires the [persona] bracket per Case File §6.7 Session Log canonical
# format ("AI [Marcus]:", "AI [Consultant]:", "AI [pre-flight]:"). Distinct
# from AI_LINE_RE above (which is intentionally permissive and used for
# relaxed-mode permission-window tracking — that logic needs to track any
# AI utterance shape, not just the canonical bracketed one).
AI_CHAT_LINE_STRICT_RE = re.compile(r"^AI\s*\[[^\]]+\]\s*:", re.IGNORECASE)

# Sprint 19 Card 04-F Fix 2 — placeholder shape per chapter 06 §6.4.0.
# `AI [persona]: [description of what was emitted]` is audit-trail prose,
# not chat surface. INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS should NOT fire
# on placeholder lines — the placeholder describes the response (legitimately
# protocol-mechanic per §6.13 step 0 user-facing-language rule), not the
# response itself. Detection: AI [persona]: line opens with `[`.
AI_PLACEHOLDER_LINE_RE = re.compile(r"^AI\s*\[[^\]]+\]\s*:\s*\[", re.IGNORECASE)

# Sprint 16 Card 02: Case File body section markers. Matching ANY of these
# CLOSES an open AI chat-output span (the line itself is also skipped from
# scanning). Codifies the 7 excluded Case File body section types named by
# the card description plus general structural boundaries (User: turn,
# markdown heading at any level).
#
# Card 02 excluded section types (each named explicitly):
#   1. ^Diagnostic:                            — Diagnostic blocks
#   2. ^- Voice-neutrality:                    — Voice-neutrality annotations
#   3. quality_check_corrections:              — YAML block contents
#   4. ## Tools Applied / ### [Tool Name]      — Tools Applied entries
#   5. ## Next Steps                           — Next Steps section prose
#   6. Library status:                         — Library-status notes
#   7. Audit notes / audit history /           — audit-history narration
#      Post-session audit caught
#
# Plus general boundaries:
#   - User: / user:                            — next user turn (closes span)
#   - ^#{1,6} <text>                           — any markdown heading
#
# §6.13 step 0 EXPLICITLY REQUIRES the AI to record audit catches and
# voice-neutrality observations in these sections — the lint must not
# penalize that record-keeping. The CHAT close-turn surfacing of audit
# catches is a separate concern (handled by Sprint 16 Card 01's runtime
# emission prevention at the response-composition layer).
SECTION_BOUNDARY_PATTERNS = [
    re.compile(r"^\s*User\s*:", re.IGNORECASE),
    re.compile(r"^\s*#{1,6}\s+\S"),
    re.compile(r"^Diagnostic\s*:", re.IGNORECASE),
    re.compile(r"^\s*-\s+Voice[- ]neutrality\s*:", re.IGNORECASE),
    re.compile(r"^quality_check_corrections\s*:"),
    re.compile(r"^###\s+\[[^\]]+\]"),
    re.compile(r"^\s*-\s+Library\s+status\s*:", re.IGNORECASE),
    re.compile(r"^Library\s+status\s*:", re.IGNORECASE),
    re.compile(
        r"^(?:Audit\s+notes|Audit\s+history|Post[- ]session\s+audit\s+caught)",
        re.IGNORECASE,
    ),
]


# Infrastructure-announcement patterns (chapter 13 §13.3, Sprint 14 Card 03).
#
# Catches protocol-mechanics fourth-wall breaks: the AI narrating its own
# infrastructure operations into chat ("Let me open the Case File...",
# "This is the action-package commitment moment..."). Sprint 13 Tessa
# Claude debrief surfaced these as a STRUCTURAL drift class distinct from
# the lexical first-person-stance drift caught by BANNED_PHRASES — these
# phrases are factually neutral but structurally protocol-mechanics-y.
#
# Fires in BOTH modes (relaxed + standard). Protocol mechanics do NOT get
# a relaxed-mode exemption — the §4.3.2 mode rule covers tool-naming
# suppression in relaxed mode, NOT infrastructure-narration suppression.
# Sophisticated users do not benefit from being talked at about protocol
# internals; they benefit from the protocol working invisibly.
#
# Design constraints (v28+v30):
#   - Lookahead-style termination is not needed here because both patterns
#     are single-line keyword pairs (verb + noun-class, or "this is the
#     <noun> ... <event-word>"); the `\b...\b` anchors at both ends
#     provide deterministic bounds and `.*?` is bounded by the line break
#     (scan_file is line-by-line). Lookahead-style termination matters for
#     delimited content where the close-marker contains chars that might
#     legitimately appear inside the match (HTML comments with hyphens —
#     v34 prescription); these patterns don't have that hazard.
#   - Both patterns use `re.IGNORECASE` for case-tolerant matching.
#   - Markdown context exclusions (inline backticks, double-quoted strings,
#     fenced code blocks, user-voice prefixes, table rows) are applied via
#     the existing scan_file pipeline — no separate exclusion needed for
#     infrastructure_announcement matches.
INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS = [
    # Pattern A: "Let me [verb] ... Case File/infrastructure/protocol/action-package/
    #             pre-S2/runtime gate/pre-emission/library entry/audit"
    # OR        "I'll (now) [verb] ..." (same noun list)
    #
    # Sprint 13 Tessa examples this catches:
    #   "Let me get the Case File infrastructure in place..."
    #   "Let me close the Case File while you decide."
    #   "I'll open the Case File for this..."
    # Sprint 14 examples added in Sprint 15 Card 04 expansion:
    #   "I'll run the pre-S2 runtime gate verification..."
    #   "Let me consult the library entry for this..."
    #   "I'll fire the pre-emission check before continuing..."
    (
        "infra: case-file action narration",
        re.compile(
            r"\b(?:let me|i[' ]ll(?:\s+now)?)\s+"
            # Verb list expanded Sprint 15 Card 04 (Sprint 14 verbatim leak verbs):
            r"(?:open|close|update|get|set\s*up|spin\s*up|prepare|"
            r"initialize|seal|finalize|run|fire|trigger|consult|"
            r"look\s*up|verify|check|apply|surface|invoke)\b"
            r".*?"
            # Noun list expanded Sprint 15 Card 04:
            r"\b(?:case\s*file|infrastructure|protocol|action[- ]package|"
            r"pre[- ]?s\d|runtime\s+gate|pre[- ]emission\s+(?:check|guard|gate)|"
            r"library\s+entry|library\s+lookup|"
            r"trigger[- ]phrase\s+audit|voice[- ]neutrality\s+lint|"
            r"validate[- ]case[- ]file|post[- ]session[- ]audit)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern B: "This is the [protocol-noun] (commitment) (moment|step|gate|trigger|threshold)"
    #
    # Sprint 13 Tessa example this catches:
    #   "This is the action-package commitment moment..."
    (
        "infra: protocol-moment narration",
        re.compile(
            r"\bthis is the\s+"
            r"(?:action[- ]package|protocol|step\s*\d+\w?|phase\s*\d+|"
            r"case[- ]file|tool[- ]selection|s\d|library[- ]consultation|"
            r"bootstrap|diagnostic|decision[- ]tree|scope[- ]statement)"
            r"(?:\s+commitment)?\s+"
            r"(?:moment|step|gate|trigger|threshold)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern C (Sprint 15 Card 04): protocol-field state-transition narration.
    # Catches narration of internal protocol-field state changes that should
    # remain author-side bookkeeping, not chat output.
    #
    # Sprint 14 Tessa verbatim:
    #   "relaxed_scaffolding will fire when detection_check writes at turn 4-5"
    #   "detection_check writes at Turn 4 or 5"
    #
    # Does NOT match Yelena-style structured annotations like
    # "Pre-S2 runtime gate: resolved-count=N" (annotation tables that
    # neither anthropomorphize the field nor narrate transitions).
    (
        "infra: protocol-field state narration",
        re.compile(
            r"\b(?:relaxed_scaffolding|detection_check|active_persona|"
            r"signals_observed|goal_stack)\s+"
            r"(?:will\s+fire|writes\s+at|fires\s+at|fires\s+when|"
            r"fired\s+this\s+turn|written\s+this\s+turn|writes\s+this\s+turn|"
            r"updates\s+this\s+turn|updated\s+this\s+turn)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern D (Sprint 15 Card 04): "single load-bearing (line|phrase|stance line)"
    # narration. Catches the specific Tessa Sprint 14 chat artifact where the
    # AI references the relaxed-mode single-stance-phrase rule by its
    # protocol nickname.
    #
    # Sprint 14 Tessa verbatim:
    #   "'Honest read: no' used as the single load-bearing line"
    #
    # Does NOT match legitimate substantive uses of "load-bearing" such as
    # "load-bearing process gap", "load-bearing claim", "load-bearing
    # essence" — those lack the "single" + protocol-line modifier.
    (
        "infra: single-load-bearing line narration",
        re.compile(
            r"\bsingle\s+load[- ]bearing\s+"
            r"(?:line|phrase|stance(?:\s+line)?|invocation|invitation)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern E (Sprint 15 Card 04): audit/lint meta-narration in chat.
    # Catches the AI narrating audit-script behavior by name in chat output.
    # Acceptable in retrospective annotations and case-file docs; NOT in
    # chat output.
    #
    # Sprint 14 Tessa verbatim (in chat at line 489 of the CF):
    #   "the voice-neutrality lint flagged 'honest read' in my last turn"
    #
    # Mode-asymmetry: fires in BOTH relaxed and standard modes — no
    # permission-context window applies to audit-script narration.
    (
        "infra: audit-script meta-narration",
        re.compile(
            r"\b(?:voice[- ]neutrality\s+lint|validate[- ]case[- ]file|"
            r"trigger[- ]phrase\s+audit|post[- ]session[- ]audit|"
            r"artifact[- ]quality\s+audit|portability[- ]check|"
            r"cross[- ]chapter[- ]dependency[- ]audit|case[- ]file[- ]placeholder[- ]lint)"
            r"\b[^\n]{0,80}?"
            r"\b(?:flagged|caught|surfaced|fired|exited|catch|catches)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern F (Sprint 18 Card 02): "I'm/I am going to X [now]" composition-
    # meta narration. Catches Sprint 17 Tessa turn 3 verbatim:
    #   "I'm going to write the Case File now (it's been built up implicitly...)"
    # Scoped to verbs and noun classes that signify protocol-machinery action,
    # not arbitrary speech-act prediction.
    (
        "infra: composition-meta 'I'm going to'",
        re.compile(
            r"\bi(?:'m| am) going to\b"
            r"[^\n]{0,80}?"
            r"\b(?:write|set\s+up|create|initialize|update|open|close|prepare|seal|finalize)\b"
            r"[^\n]{0,80}?"
            r"\b(?:case\s*file|protocol|tool|persona|action[- ]package|framework|infrastructure)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern G (Sprint 18 Card 02): "per protocol" narrative declaration in
    # chat. Catches Sprint 17 Tessa turn 3 verbatim:
    #   "...the next response is the action-package commitment moment per protocol"
    # Scoped to narrative-noun precedent to avoid over-firing on legitimate
    # documentation prose like "AI executes per protocol step 7". The
    # session-log scope filter additionally excludes audit-trail annotation
    # contexts (Tools Applied entries, tool_surfaced_in_chat fields, Diagnostic
    # blocks, audit_known_coverage_gaps entries — all outside AI chat-output
    # spans per Sprint 16 Card 02 scope filter).
    (
        "infra: 'per protocol' narrative declaration",
        re.compile(
            r"\b(?:commitment|moment|step|requirement|response|delivery|stance|"
            r"action|action[- ]package|gate|phase|trigger|threshold|decision|"
            r"stage|invocation|exit)\s+per\s+protocol\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern H (Sprint 18 Card 02): "Now the/my actual chat response..."
    # meta-narration of impending substance. Catches Sprint 17 Mara turn 6
    # verbatim:
    #   "Now the actual chat response, in Consultant voice with the action package..."
    (
        "infra: 'now the actual response' narration",
        re.compile(
            r"\bnow\s+(?:the|my)\s+(?:actual|real)\s+(?:chat|in[- ]chat)\s+response\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern I (Sprint 18 Card 02): "in [Persona] voice" voice-management
    # narration. Catches Sprint 17 Mara turn 6 verbatim:
    #   "Now the actual chat response, in Consultant voice with..."
    # Persona names match the 5-persona library (Consultant, Partner, Counselor,
    # Therapist, Coach). Mode-asymmetry: fires in BOTH relaxed and standard
    # modes — naming the active persona in chat is always a leak regardless of
    # operator-debrief permissions.
    (
        "infra: 'in [Persona] voice' narration",
        re.compile(
            r"\bin\s+(?:Consultant|Partner|Counselor|Therapist|Coach)\s+voice\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern J (Sprint 18 Card 02): "Let me set up [the Case File/framework/
    # protocol/infrastructure]" pre-substance setup narration. Catches Sprint
    # 17 Mara turn 1 verbatim:
    #   "Let me set up the Case File and get oriented before we move."
    # Partial overlap with Pattern A "case-file action narration" verb list
    # (`set up` is in Pattern A's verbs) but Pattern A requires the full
    # let-me-VERB-NOUN shape; Pattern J specializes on the "set up" lexicon
    # which has a distinctive pre-substance-scaffolding signature.
    (
        "infra: 'let me set up' pre-substance narration",
        re.compile(
            r"\blet\s+me\s+set\s+up\b"
            r"[^\n]{0,40}?"
            r"\b(?:the\s+case\s*file|the\s+framework|the\s+protocol|the\s+infrastructure)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern K (Sprint 18 Card 02): "before I/we [deliver|move|continue|...]"
    # pre-substance scaffolding narration. Bounded by the noun the
    # scaffolding postpones (package/response/Case File/action). Catches the
    # composition-meta family shape where the AI announces the deferral
    # rather than just delivering.
    (
        "infra: 'before I/we' scaffolding narration",
        re.compile(
            r"\bbefore\s+(?:I|we)\s+(?:deliver|move|continue|proceed|respond)\b"
            r"[^\n]{0,80}?"
            r"\bthe\s+(?:package|response|case\s*file|action|action[- ]package)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern L (Sprint 18 Card 11): diagnostic-narration in chat. Catches
    # Sprint 18 Mara turn 2 + turn 4 verbatim:
    #   "Running the diagnostic on Turn 2..."
    #   "Diagnostic on Turn 4..."
    # The AI narrating its own diagnostic-step is meta-machinery talk; the
    # diagnostic itself should be invisible in chat, surfacing only via the
    # substantive user-facing content the diagnostic produced.
    (
        "infra: diagnostic-step narration",
        re.compile(
            r"\b(?:Running\s+the\s+diagnostic|Diagnostic)\s+on\s+Turn\s+\d+\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern M (Sprint 18 Card 11): runtime-gate narration in chat. Catches
    # Sprint 18 Mara turn 3 + turn 6 verbatim:
    #   "the action-package trigger fired but I need to run the Step 8a pre-S2 gate"
    #   "Re-running Step 8a pre-S2 runtime gate..."
    # Step-references + gate-state are protocol-machinery; the AI naming
    # them in chat reveals the runtime gate as a visible artifact rather
    # than a silent enforcement mechanism.
    (
        "infra: runtime-gate narration",
        re.compile(
            r"\b(?:Re-?running\s+)?Step\s+\d+[a-z]?\s+"
            r"(?:pre-?S\d+\s+)?(?:runtime\s+)?gate\b",
            re.IGNORECASE,
        ),
    ),
    (
        "infra: 'action-package trigger fired' narration",
        re.compile(
            r"\baction[- ]?package\s+trigger\s+fired\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern N (Sprint 18 Card 11): persona-state narration in chat. Catches
    # Sprint 18 Mara turn 5 + turn 6 verbatim:
    #   "Persona stays in Guide for the analysis phase..."
    #   "Persona: Guide → Consultant."
    # Three sub-shapes: "Persona stays in X" + "Persona: X → Y" + "Persona
    # switch/transition:". The persona-management machinery is internal-log
    # material per chapter 05; surfacing it in chat is composition-meta.
    (
        "infra: 'persona stays in' narration",
        re.compile(
            r"\bPersona\s+stays\s+in\s+"
            r"(?:Consultant|Partner|Counselor|Therapist|Coach|Guide)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "infra: 'Persona: X → Y' transition narration",
        re.compile(
            r"\bPersona\s*:\s*\w+\s*(?:→|->|to)\s+\w+\b",
            re.IGNORECASE,
        ),
    ),
    (
        "infra: 'persona switch/transition' narration",
        re.compile(
            r"\bPersona\s+(?:switch|transition|history)\s*:",
            re.IGNORECASE,
        ),
    ),
    # Pattern O (Sprint 18 Card 11): output-shape narration in chat. Catches
    # Sprint 18 Mara turn 6 verbatim:
    #   "Output shape: full scope statement with action package."
    # Output-shape is the Step 8a decision-tree result label; surfacing it
    # in chat narrates the runtime gate's classification rather than just
    # delivering the classified output.
    (
        "infra: 'Output shape:' narration",
        re.compile(
            r"\bOutput\s+shape\s*:",
            re.IGNORECASE,
        ),
    ),
    # Pattern P (Sprint 18 Card 11): "Now the response" terminator narration.
    # Catches Sprint 18 Mara turn 3 verbatim:
    #   "Now the response."
    # Distinct from Pattern H ("Now the actual/real chat response") which
    # requires the "actual"/"real" modifier. The bare "Now the response"
    # shape is the AI announcing about-to-speak at line-end, which is
    # meta-narration regardless of modifier.
    (
        "infra: 'Now the response' terminator narration",
        re.compile(
            r"(?:^|\.\s+)Now\s+the\s+response\s*\.?(?:\s|$)",
            re.IGNORECASE,
        ),
    ),
    # Pattern Q (Sprint 18 Card 11): task-list state narration. Catches
    # Sprint 18 Mara turn 6 (and similar) verbatim:
    #   "Task list correctly reflects state..."
    #   "Task list is current..."
    #   "Task list already accurate..."
    # Task-tracking is operator-mode machinery; narrating its state in
    # chat is composition-meta. Pattern A already catches "Let me update
    # my task tracking" (let-me + verb + noun); Pattern Q catches the
    # state-assertion shape that Pattern A misses.
    (
        "infra: 'task list is/reflects' state narration",
        re.compile(
            r"\bTask\s+list\s+(?:is|reflects|already|correctly)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern R (Sprint 19 Card 04-B): diagnostic-narration variants. Catches
    # Sprint 19 Yelena verbatim shapes that Pattern L's "Running the diagnostic
    # on Turn N" form did not catch:
    #   "Running the diagnostic loop on a very dense opening"
    #   "Let me quickly check what library tools fit"
    # Variant 1 — "Running the diagnostic loop" (no "on Turn N" suffix; descriptive
    # trailing context instead). Pattern L required "on Turn N" — this variant
    # narrates the diagnostic without the turn anchor.
    (
        "infra: 'Running the diagnostic loop' narration",
        re.compile(
            r"\bRunning\s+the\s+diagnostic\s+loop\b",
            re.IGNORECASE,
        ),
    ),
    # Variant 2 — "Let me [quickly] check what (library) tools fit" — pre-substance
    # tool-search narration. The library lookup is operator-mode machinery; the AI
    # narrating its own library-search-step is composition-meta.
    (
        "infra: 'let me check what tools fit' narration",
        re.compile(
            r"\blet\s+me\s+(?:quickly\s+)?check\s+what\s+(?:library\s+)?tools?\s+(?:fit|apply|are\s+relevant|might\s+apply)\b",
            re.IGNORECASE,
        ),
    ),
    # Pattern S (Sprint 19 Card 04-B): Case File state-update narration (Pattern G
    # extension). Catches Sprint 19 Yelena verbatim:
    #   "Updating Case File for Turn \d+"
    # Pattern G catches "per protocol" narrative declaration; Pattern J catches
    # "Let me set up the Case File" pre-substance narration. Neither catches the
    # mid-session "Updating Case File for Turn N" state-update narration. The
    # state-update is implicit; the AI announcing it in chat narrates infrastructure.
    (
        "infra: 'Updating Case File for Turn' state-update narration",
        re.compile(
            r"\bUpdating\s+(?:the\s+)?Case\s*File\s+(?:for\s+)?(?:Turn\s+\d+|state\b)",
            re.IGNORECASE,
        ),
    ),
    # Pattern T (Sprint 19 Card 04-B): "Now the response:" colon-continuation
    # extension to Pattern P. Pattern P catches the bare "Now the response."
    # terminator (period-anchored); Pattern T catches the colon-continuation shape
    # where "Now the response:" precedes substance description rather than the
    # substance itself. Sprint 19 Yelena verbatim:
    #   "Now the response: This turn applies..."
    # The "Now the response:" prefix announces about-to-speak just as Pattern P
    # does; the colon-continuation pattern just delays the period.
    (
        "infra: 'Now the response:' colon-continuation narration",
        re.compile(
            r"(?:^|\.\s+)Now\s+the\s+response\s*:\s*This\s+turn\s+(?:applies|delivers|uses|invokes|fires|relies\s+on)",
            re.IGNORECASE,
        ),
    ),
    # Pattern U (Sprint 19 Card 04-B): SKIPPED per operator judgment. The
    # "Switching gears — your two questions" shape (Yelena Sprint 19) is
    # conversational English with high false-positive risk on legitimate
    # pivots ("switching gears, let's look at...", "switching gears for a
    # moment..."). The composition-meta signal in this phrase is too weak
    # to enumerate without collateral. If recurring in future panels, the
    # discipline is to address via spec-contract (per Card 04-B handoff
    # L1 known limitation) rather than regex enumeration.
]


def _is_invitation(text: str) -> bool:
    return any(p.search(text) for p in INVITATION_PATTERNS)


def _is_process_direct_read_invitation(text: str) -> bool:
    """Sprint 17 Card 07: distinguish process-direct-read from
    content-direct-read invitations. Process-direct-read invitations
    open the §13.2 permission-context window in BOTH standard mode AND
    relaxed mode. Content-direct-read invitations open the window in
    relaxed mode only (per §13.2 exception block which scopes to
    sophisticated-user relaxed-scaffolding sessions)."""
    return any(p.search(text) for p in INVITATION_PATTERNS_PROCESS)


def is_user_voice_line(line: str, in_code_block: bool) -> bool:
    """Return True if the line is user-voice content (excluded from scan)."""
    if in_code_block:
        return True
    stripped = line.lstrip()
    if stripped.startswith("> "):
        return True
    if stripped.startswith("User:") or stripped.startswith("user:"):
        return True
    return False


def strip_inline_excludes(line: str) -> str:
    """Strip content inside inline backticks AND inside double-quoted strings.

    - Inline backticks (`like this`) cite banned phrases as documentation
      examples in chapter prose; they are not authorial drift.
    - Double-quoted strings ("like this") in chapter prose typically cite
      user-utterance examples (e.g., `signals OR explicit "I think we're
      good for now"`), canonical names, or session-log excerpts. The
      content inside the quote is user voice or named text, not the AI's
      authorial voice. Sprint 13 Card 07 added this exclusion because
      chapter 06 §6.11 had 2 false positives for `"I think we're good for
      now"` examples — both are user-voice content quoted in instruction
      prose, not AI drift.
    - Single-quoted strings (Sprint 15 Card 08) are stripped ONLY when
      the line has a meta-mention context (see META_MENTION_CONTEXT_RE).
      Tessa Sprint 14 close-turn line 489 ("the voice-neutrality lint
      flagged 'honest read'") shipped the self-trap pattern: surfacing
      an audit catch in the close turn caused a second exit-1 on the
      meta-mention. The fix is contextual: in audit-narration contexts,
      single-quoted banned phrases are meta-mentions; in other contexts,
      stripping single-quoted regions unconditionally would eat
      legitimate apostrophes (contractions, possessives).

    Note: this exclusion does NOT extend to session-log AI: lines that
    happen to contain double-quoted strings — those are handled upstream
    by the `User:`-line filter in scan_file (relaxed mode pairs AI lines
    with their preceding user invitation; AI lines are scanned normally).
    The double-quote exclusion only applies to chapter prose, where
    inline `"..."` segments are documentation examples rather than first-
    person AI speech.
    """
    line = INLINE_CODE_RE.sub("", line)
    line = DOUBLE_QUOTED_RE.sub("", line)
    if META_MENTION_CONTEXT_RE.search(line):
        line = SINGLE_QUOTED_RE.sub("", line)
    return line


def is_table_row(line: str) -> bool:
    """Return True if the line is a markdown table row."""
    return bool(TABLE_ROW_RE.match(line))


def detect_session_log_structure(path: Path) -> bool:
    """Return True iff the file contains any ^AI [persona]: chat-output line.

    Used by scan_file to decide whether to apply the Sprint 16 Card 02 scope
    filter (AI-chat-only scanning) under --scope auto. When True, the file
    is treated as a Case File / Session Log and the scope filter applies;
    when False, the file is treated as chapter prose and ALL eligible lines
    are scanned (existing behavior preserved for chapter scans).
    """
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if AI_CHAT_LINE_STRICT_RE.match(line):
                return True
    return False


def scan_file(
    path: Path,
    threshold: int,
    mode: str = "standard",
    scope: str = "auto",
) -> tuple[dict, list]:
    """Scan the file. Return (phrase_counts, violations).

    phrase_counts: dict of phrase -> count (across all eligible lines).
    violations: list of (line_no, phrase, context) for phrases over threshold
                (standard mode) OR for permission-context violations
                (relaxed mode — see Mode semantics in module docstring).

    Sprint 16 Card 02 scope filter: when scope == "auto" and the file
    contains a ^AI [persona]: line, OR when scope == "chat-only", lines
    outside open AI chat-output spans are skipped. See module docstring
    "Scope semantics" for full rules.
    """
    # Sprint 16 Card 02: resolve scope behavior before iterating lines
    if scope == "auto":
        session_log_mode = detect_session_log_structure(path)
    elif scope == "chat-only":
        session_log_mode = True
    elif scope == "all":
        session_log_mode = False
    else:
        raise ValueError(f"unknown scope mode: {scope!r}")
    # When session_log_mode is False, scope filter is inert: span stays
    # True for every line so the existing scan logic runs unchanged.
    in_ai_chat_span = False if session_log_mode else True
    # Sprint 19 Card 04-F Fix 2: track whether the current AI chat span is
    # a placeholder span (per chapter 06 §6.4.0). Placeholder spans skip
    # INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS scan — bracketed-description
    # content describes the response (audit trail), not the response itself.
    in_placeholder_span = False

    counts: dict[str, int] = {label: 0 for label, _, _ in BANNED_PHRASES}
    matches: dict[str, list[tuple[int, str]]] = {label: [] for label, _, _ in BANNED_PHRASES}
    # Infrastructure-announcement bookkeeping (chapter 13 §13.3 / Card 03).
    # Initialized parallel to BANNED_PHRASES so counts/matches reports
    # render uniformly. Violations bypass the per-phrase threshold —
    # any single match is an immediate violation in both modes.
    for infra_label, _ in INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS:
        counts[infra_label] = 0
        matches[infra_label] = []
    infrastructure_violations: list[tuple[int, str, str]] = []
    # Relaxed-mode permission tracking
    window_open = False
    window_used = False  # one permitted stance phrase per window
    relaxed_violations: list[tuple[int, str, str]] = []

    in_code_block = False
    with path.open("r", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line.lstrip().startswith("```"):
                in_code_block = not in_code_block
                continue
            # Sprint 16 Card 02: update AI chat-output span state BEFORE
            # the existing exclusion checks below — an AI [persona]: line
            # opens the span (this line IS in scope and gets scanned);
            # a section-boundary marker closes it (this line is NOT
            # scanned). Continuation lines (no marker match) preserve the
            # current span state, so multi-paragraph AI utterances stay
            # in scope until the next User: / heading / body section.
            if session_log_mode:
                if AI_CHAT_LINE_STRICT_RE.match(line):
                    in_ai_chat_span = True
                    # Sprint 19 Card 04-F Fix 2: detect placeholder shape
                    # (AI [persona]: [description]) and mark the span so
                    # infrastructure-pattern scan is skipped for all lines
                    # in this AI chat span.
                    in_placeholder_span = bool(AI_PLACEHOLDER_LINE_RE.match(line))
                elif any(p.match(line) for p in SECTION_BOUNDARY_PATTERNS):
                    in_ai_chat_span = False
                    in_placeholder_span = False
            # Detect speaker boundaries for permission-window tracking.
            # Sprint 17 Card 07: window tracking applies in BOTH modes —
            # in standard mode the window only opens on process-direct-read
            # invitations (per §13.2 + chapter 03 §3.10 mode-parity).
            stripped = line.lstrip()
            is_user = bool(USER_LINE_RE.match(stripped))
            is_ai = bool(AI_LINE_RE.match(stripped))
            if is_user:
                # New user turn — close any open window
                window_open = False
                window_used = False
                # Check for invitation. In relaxed mode, ANY invitation
                # opens the window. In standard mode, only process-
                # direct-read invitations open the window (Sprint 17
                # Card 07).
                if mode == "relaxed":
                    pending_invitation = _is_invitation(stripped)
                else:
                    pending_invitation = _is_process_direct_read_invitation(stripped)
            elif is_ai:
                # Open a window iff a pending invitation preceded this AI line
                if 'pending_invitation' in locals() and pending_invitation:
                    window_open = True
                    window_used = False
                    pending_invitation = False
                else:
                    window_open = False
                    window_used = False
            elif not stripped:
                # Blank line — closes any open paragraph window
                window_open = False
                window_used = False

            if is_user_voice_line(line, in_code_block):
                continue
            if is_table_row(line):
                continue
            # Sprint 16 Card 02: scope filter — when session_log_mode is on,
            # skip any line outside an open AI chat-output span. This is the
            # central enforcement point that prevents the lint from over-
            # firing on Case File body content (Diagnostic blocks, Voice-
            # neutrality annotations, Tools Applied entries, Next Steps,
            # Library status notes, audit-history narration, YAML
            # frontmatter, Frame-section bullet annotations) — all of which
            # §6.13 step 0 explicitly REQUIRES the AI to record.
            if not in_ai_chat_span:
                continue
            scan_line = strip_inline_excludes(line)
            # Infrastructure-announcement scan (chapter 13 §13.3 / Card 03).
            # Always violates in both modes — no relaxed exemption, no
            # threshold gating. Runs BEFORE the lexical BANNED_PHRASES
            # loop because the two scans are orthogonal (no double-
            # counting risk — distinct labels).
            #
            # Sprint 19 Card 04-F Fix 2: skip the infrastructure scan on
            # placeholder-shape AI lines (per chapter 06 §6.4.0). The
            # bracketed description IS audit-trail prose about the
            # response, not the response itself — Pattern D and adjacent
            # protocol-mechanic patterns would false-fire on legitimate
            # audit-trail content. BANNED_PHRASES still scan (voice-
            # projection words like "I feel" / "honestly" remain
            # violations even in audit-trail descriptions because they
            # imply the AI actually emitted them).
            if not in_placeholder_span:
                for infra_label, infra_pattern in INFRASTRUCTURE_ANNOUNCEMENT_PATTERNS:
                    if infra_pattern.search(scan_line):
                        counts[infra_label] += 1
                        matches[infra_label].append((line_no, line.rstrip()))
                        infrastructure_violations.append(
                            (line_no, infra_label, line.rstrip())
                        )
            for label, pattern, relaxed_permitted in BANNED_PHRASES:
                if re.search(pattern, scan_line, flags=re.IGNORECASE):
                    if mode == "relaxed":
                        # Always-banned phrases ignore the window
                        if not relaxed_permitted:
                            counts[label] += 1
                            matches[label].append((line_no, line.rstrip()))
                            relaxed_violations.append((line_no, label, line.rstrip()))
                            continue
                        # Permitted phrase: allowed once inside an open window
                        if window_open and not window_used:
                            # Consume the window permission silently
                            window_used = True
                            continue
                        # Either no window or second instance — violation
                        counts[label] += 1
                        matches[label].append((line_no, line.rstrip()))
                        relaxed_violations.append((line_no, label, line.rstrip()))
                    else:
                        # Standard mode (Sprint 17 Card 07): the
                        # permission window opens only on process-
                        # direct-read invitations. When open, a single
                        # permitted-phrase instance is silently consumed
                        # in the response opener; second instances and
                        # phrases outside the window count as violations.
                        # Always-banned phrases ignore the window
                        # (mirroring relaxed-mode behavior).
                        if not relaxed_permitted:
                            counts[label] += 1
                            matches[label].append((line_no, line.rstrip()))
                            continue
                        if window_open and not window_used:
                            window_used = True
                            continue
                        counts[label] += 1
                        matches[label].append((line_no, line.rstrip()))

    if mode == "relaxed":
        # In relaxed mode, every recorded BANNED_PHRASES violation is
        # already filtered through the permission-window logic. Append
        # infrastructure violations — those bypass the window entirely.
        return counts, list(relaxed_violations) + infrastructure_violations

    # Standard mode: apply threshold to BANNED_PHRASES counts only.
    # Infrastructure-announcement violations bypass the threshold and are
    # appended directly (any single match is a violation).
    violations = []
    for label, _, _ in BANNED_PHRASES:
        count = counts.get(label, 0)
        if count > threshold:
            for line_no, ctx in matches[label]:
                violations.append((line_no, label, ctx))
    violations.extend(infrastructure_violations)
    return counts, violations


def format_report(path: Path, counts: dict, violations: list, threshold: int) -> str:
    lines = [f"voice-neutrality-lint.py — {path}"]
    lines.append(f"threshold: > {threshold} occurrences flagged")
    lines.append("")
    lines.append("Phrase counts:")
    total = 0
    for label, count in counts.items():
        marker = "  FLAG" if count > threshold else "  ok  "
        lines.append(f"{marker}  {label:20s} = {count}")
        total += count
    lines.append("")
    lines.append(f"Total banned-phrase occurrences: {total}")
    lines.append(f"Violations (over threshold): {len(violations)}")
    if violations:
        lines.append("")
        lines.append("Flagged lines:")
        for line_no, label, ctx in violations:
            lines.append(f"  line {line_no:4d}  [{label}]  {ctx[:120]}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Sprint 15 Card 04 self-test fixtures
#
# Positive cases (≥5): infrastructure-announcement patterns that MUST flag.
# Each line is sourced verbatim from Sprint 14 Tessa CF (sales-hire-decision)
# or composed in the same shape as the card's verbatim leak examples.
#
# Negative cases (≥3): similar lexicon used in legitimate substantive prose
# (Yelena-CF style) that MUST NOT flag. These guard against false positives
# from the new Card 04 patterns.
# ---------------------------------------------------------------------------
SELF_TEST_POSITIVE_CASES = [
    # Sprint 14 Tessa CF verbatim — protocol-field state narration
    ("Tessa L356", "- Sophistication signals (running): 3/5 → relaxed_scaffolding will fire when detection_check writes at turn 4-5.", "infra: protocol-field state narration"),
    # Sprint 14 Tessa CF verbatim — single-load-bearing line narration
    ("Tessa L458", "- Voice-neutrality: relaxed mode permits ONE first-person stance phrase per invitation; \"Honest read: no\" used as the single load-bearing line.", "infra: single-load-bearing line narration"),
    # Sprint 14 Tessa CF verbatim — audit-script meta-narration in chat
    ("Tessa L489", "One audit catch before closing: the voice-neutrality lint flagged 'honest read' in my last turn — the phrase reads stronger than 'am I overthinking this' invited.", "infra: audit-script meta-narration"),
    # Card-spec verbatim example (Pattern A expansion: 'I'll run ... pre-S2 runtime gate')
    ("Card-spec verb expansion", "I'll run the pre-S2 runtime gate verification before continuing the diagnostic.", "infra: case-file action narration"),
    # Card-spec verbatim example (Pattern A expansion: 'Let me consult ... library entry')
    ("Card-spec library entry", "Let me consult the library entry for Conviction-vs-Argument before the next move.", "infra: case-file action narration"),
    # Pattern C variant — detection_check state-transition
    ("Pattern C variant", "The detection_check writes at turn 5 and the relaxed_scaffolding will fire then.", "infra: protocol-field state narration"),
]

SELF_TEST_NEGATIVE_CASES = [
    # Yelena CF substantive use of "load-bearing"
    ("Yelena 'load-bearing process gap'", "- This is the load-bearing process gap underlying the four-path comparison."),
    # Yelena CF substantive use of "load-bearing"
    ("Yelena 'load-bearing claim'", "The cross-quarter consistency is the load-bearing claim — show the recurrence."),
    # Yelena-style structured annotation (Pre-S2 runtime gate as table-row label, not chat narration)
    ("Yelena structured annotation", "  - Pre-S2 runtime gate: resolved-count=3 (Conviction vs Argument, Pre-Mortem as Foresight, Stakeholder Power-Interest Grid)"),
    # Yelena single-frame relaxation in annotation form (not state-transition narration)
    ("Yelena single-frame annotation", "  - S2 (diagnostic depth): yes (single-frame relaxation applies — internally coherent at one frame)"),
    # User-voice quote referencing protocol terms (excluded by user-voice filter)
    ("User-voice quote", "> User: \"What does the detection_check do exactly?\""),
    # Sprint 15 Card 08: single-quoted banned phrase in "the phrase X"
    # meta-mention context — must not count toward banned-phrase total.
    # The Tessa L489-verbatim line ALSO trips Card 04's infra: audit-script
    # meta-narration pattern (correctly — that's a separate infra violation
    # the Card 04 fix added), so the verbatim L489 is not a clean negative
    # case for Card 08 in isolation. This paraphrased variant exercises the
    # meta-mention skip without tripping Card 04's audit-script pattern.
    ("C08 paraphrased meta-mention", "I caught my own use of 'honest read' in the previous response — the phrase reads stronger than the invitation warranted."),
    # Card 08 negative: 'honest read' inside contraction-heavy prose without
    # audit context — must NOT skip (single-quote stripping is context-gated).
    ("C08 contractions (no meta-mention)", "Marcus's pacing isn't off; he's been showing what he doesn't yet name."),
    # Card 08 negative: discussing the phrase 'honest read' with explicit
    # "the phrase" context — meta-mention recognized; the banned phrase quote
    # is skipped. Combined with no other infra patterns, this should not flag.
    ("C08 'the phrase' meta-context", "Documentation note: the phrase 'honest read' should appear in retrospective annotations only, not in the close turn."),
]


# ---------------------------------------------------------------------------
# Sprint 16 Card 02 scope-filter test fixtures
#
# Positive cases (≥5): AI chat-output (^AI [persona]: lines or their
# continuations) containing banned phrases or infrastructure-announcement
# patterns — these MUST still flag under the scope filter.
#
# Negative cases (≥5): Case File body sections (Diagnostic blocks,
# Voice-neutrality annotations, quality_check_corrections YAML, Tools
# Applied entries, Next Steps prose, Library status notes, audit-history
# narration) containing banned phrases or infra patterns — these MUST NOT
# flag because §6.13 step 0 explicitly requires the AI to record them.
# Each negative case includes at least one ^AI [persona]: line so
# Session Log mode is detected and scope filter activates.
# ---------------------------------------------------------------------------
SCOPE_POSITIVE_CASES = [
    # P1: always-banned phrase in single-paragraph AI chat
    (
        "P1 chat I'd want (always-banned)",
        "AI [Marcus]: I'd want to think about it more before deciding.\n",
        "I'd want",
    ),
    # P2: always-banned phrase in close-turn AI chat
    (
        "P2 chat I feel (always-banned)",
        "AI [Consultant]: I feel like the second path is the move here.\n",
        "I feel",
    ),
    # P3: infra: case-file action narration in AI chat
    (
        "P3 chat infra case-file action",
        "AI [Yelena]: Let me open the Case File and update the schema before we continue.\n",
        "infra: case-file action narration",
    ),
    # P4: multi-paragraph AI chat — banned phrase in continuation paragraph
    (
        "P4 chat continuation 'I'd suggest'",
        (
            "AI [Partner]: That cash math is load-bearing. Two constraints visible now.\n"
            "\n"
            "I'd suggest sequencing the engine fix before the hire onboarding.\n"
        ),
        "I'd suggest",
    ),
    # P5: infra: protocol-field state narration in AI chat
    (
        "P5 chat infra protocol-field",
        (
            "AI [Consultant]: Acknowledging the regime lock.\n"
            "\n"
            "The detection_check writes at turn 5 and the relaxed_scaffolding will fire then.\n"
        ),
        "infra: protocol-field state narration",
    ),
]

SCOPE_NEGATIVE_CASES = [
    # N1: Diagnostic block bullet annotation (the Tessa L356 false-positive shape)
    (
        "N1 Diagnostic block protocol-field",
        (
            "AI [Partner]: Substantive chat response here.\n"
            "\n"
            "Diagnostic:\n"
            "- Sophistication signals (running): 3/5 → relaxed_scaffolding will fire when detection_check writes at turn 4-5.\n"
        ),
    ),
    # N2: Voice-neutrality annotation (the Tessa L458 false-positive shape)
    (
        "N2 Voice-neutrality annotation",
        (
            "AI [Consultant]: Substantive turn-6 response.\n"
            "\n"
            "- Voice-neutrality: relaxed mode permits ONE first-person stance phrase per invitation; \"Honest read: no\" used as the single load-bearing line.\n"
        ),
    ),
    # N3: quality_check_corrections YAML block — banned phrase verbatim cited
    (
        "N3 quality_check_corrections YAML",
        (
            "AI [Marcus]: Substantive chat.\n"
            "\n"
            "quality_check_corrections:\n"
            "  - turn: 6\n"
            "    catch: \"Used 'Honest read: no' to open the response — I'd want to revisit this.\"\n"
        ),
    ),
    # N4: ## Tools Applied → ### [Tool Name] entry with banned phrases inside
    (
        "N4 Tools Applied entry",
        (
            "AI [Consultant]: Substantive chat content.\n"
            "\n"
            "## Tools Applied\n"
            "\n"
            "### [Pre-Mortem as Foresight]\n"
            "- I feel this applies because the failure mode is asymmetric.\n"
            "- I'd suggest framing the pre-mortem around the 90-day hire window.\n"
        ),
    ),
    # N5: ## Next Steps prose with banned phrases
    (
        "N5 Next Steps prose",
        (
            "AI [Consultant]: Substantive turn-7 close.\n"
            "\n"
            "## Next Steps\n"
            "- I'd suggest the Monday morning conflict-counsel call.\n"
            "- I feel the timeline is tight but workable.\n"
        ),
    ),
    # N6: Library status note (bullet form)
    (
        "N6 Library status note",
        (
            "AI [Marcus]: Substantive chat.\n"
            "\n"
            "- Library status: 3 candidate tools surfaced. I'd want to consult the library entry for Pre-Mortem before next turn.\n"
        ),
    ),
    # N7: Audit-history narration paragraph
    (
        "N7 Audit-history narration",
        (
            "AI [Consultant]: Substantive chat.\n"
            "\n"
            "Audit notes: voice-neutrality lint exited 1 on turn 6 close — 'honest read' caught out of permission window. I'd suggest the substitute phrasing per §13.2 table.\n"
        ),
    ),
    # N8: Frame section bullet annotation BEFORE Session Log (frontmatter-style content)
    (
        "N8 Frame section bullet annotation",
        (
            "# Case File: Sample\n"
            "\n"
            "## Frame 0\n"
            "\n"
            "- Goal Statement: I'd want clarity on the 30-day decision before committing — verbatim user paraphrase.\n"
            "- Persona: consultant\n"
            "\n"
            "## Session Log\n"
            "\n"
            "AI [Consultant]: Substantive chat begins here.\n"
        ),
    ),
]


def _run_scope_tests() -> int:
    """Run Sprint 16 Card 02 scope-filter test fixtures.

    Each positive case must flag at least one violation (banned phrase
    over threshold or any infra pattern). Each negative case must flag
    zero violations. Both run under --scope auto with Session Log
    structure detected (each fixture includes at least one ^AI
    [persona]: line). Returns 0 if all pass, 1 otherwise.
    """
    import tempfile

    all_pass = True
    # Scope positive cases use threshold=0 so single occurrences of always-
    # banned phrases flag (the test asks "did the scope filter let in-scope
    # content through to scanning?" — single-occurrence is the canonical
    # signal). Infra patterns flag at any threshold (any match is a
    # violation), so threshold value is moot for those.
    print(f"\n=== Scope-filter positive cases (must FLAG) — {len(SCOPE_POSITIVE_CASES)} cases ===")
    for label, text, expected_marker in SCOPE_POSITIVE_CASES:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(text)
            tmpf = Path(f.name)
        try:
            counts, violations = scan_file(tmpf, threshold=0, mode="standard", scope="auto")
            hit_labels = {v[1] for v in violations}
            status = "PASS" if expected_marker in hit_labels else "FAIL"
            if expected_marker not in hit_labels:
                all_pass = False
            print(f"[{status}] {label} -- expected '{expected_marker}', hits={sorted(hit_labels)}")
        finally:
            tmpf.unlink()

    # Scope negative cases use threshold=0 too — if scope filter is working,
    # zero phrases get counted (because all body content is skipped), so
    # threshold=0 still produces no violations. If scope filter is broken,
    # phrases get counted and threshold=0 would expose ANY false-positive.
    print(f"\n=== Scope-filter negative cases (must NOT flag) — {len(SCOPE_NEGATIVE_CASES)} cases ===")
    for label, text in SCOPE_NEGATIVE_CASES:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(text)
            tmpf = Path(f.name)
        try:
            counts, violations = scan_file(tmpf, threshold=0, mode="standard", scope="auto")
            status = "PASS" if not violations else "FAIL"
            if violations:
                all_pass = False
                print(f"[{status}] {label} -- expected no flags, got {len(violations)}: {[v[1] for v in violations]}")
            else:
                print(f"[{status}] {label} -- no flags (correct)")
        finally:
            tmpf.unlink()

    return 0 if all_pass else 1


def run_self_test() -> int:
    """Verify Sprint 15 Card 04 pattern coverage AND Sprint 16 Card 02
    scope filter against authored test cases.

    Each positive case must flag at least one infrastructure-announcement
    violation matching the expected pattern label. Each negative case must
    flag zero violations. Returns 0 if all cases pass, 1 otherwise.
    """
    import tempfile

    all_pass = True
    print(f"=== Positive cases (must FLAG) — {len(SELF_TEST_POSITIVE_CASES)} cases ===")
    for label, text, expected_pattern in SELF_TEST_POSITIVE_CASES:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(text + "\n")
            tmpf = Path(f.name)
        try:
            counts, violations = scan_file(tmpf, threshold=1, mode="standard")
            hit_labels = {v[1] for v in violations}
            status = "PASS" if expected_pattern in hit_labels else "FAIL"
            if expected_pattern not in hit_labels:
                all_pass = False
            print(f"[{status}] {label} -- expected pattern '{expected_pattern}', hits={sorted(hit_labels)}")
        finally:
            tmpf.unlink()

    print(f"\n=== Negative cases (must NOT flag) — {len(SELF_TEST_NEGATIVE_CASES)} cases ===")
    for label, text in SELF_TEST_NEGATIVE_CASES:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(text + "\n")
            tmpf = Path(f.name)
        try:
            counts, violations = scan_file(tmpf, threshold=1, mode="standard")
            status = "PASS" if not violations else "FAIL"
            if violations:
                all_pass = False
                print(f"[{status}] {label} -- expected no flags, got {len(violations)}: {[v[1] for v in violations]}")
            else:
                print(f"[{status}] {label} -- no flags (correct)")
        finally:
            tmpf.unlink()

    scope_result = _run_scope_tests()
    if scope_result != 0:
        all_pass = False
    return 0 if all_pass else 1


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "--self-test":
        return run_self_test()

    parser = argparse.ArgumentParser(
        description="Scan a markdown file for first-person expertise drift."
    )
    parser.add_argument("path", help="Path to markdown file or transcript")
    parser.add_argument(
        "--threshold",
        type=int,
        default=1,
        help="Banned-phrase count above this threshold is a violation (default: 1)",
    )
    parser.add_argument(
        "--mode",
        choices=("standard", "relaxed"),
        default="standard",
        help=(
            "standard (default): every banned phrase is a violation. "
            "relaxed: permission-context windows honor one stance phrase "
            "per AI paragraph following an explicit user invitation."
        ),
    )
    parser.add_argument(
        "--scope",
        choices=("auto", "all", "chat-only"),
        default="auto",
        help=(
            "auto (default): auto-detect Case File structure (any "
            "^AI [persona]: line) and scope scan to AI chat-output spans "
            "only; chapter prose with no AI [persona]: lines is scanned "
            "in full (backward compat). all: scan every eligible line "
            "regardless of structure. chat-only: force AI-chat-only scope "
            "even on files without an AI [persona]: line."
        ),
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress report; exit code only",
    )
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"error: {path} not found", file=sys.stderr)
        return 2
    if not path.is_file():
        print(f"error: {path} is not a file", file=sys.stderr)
        return 2

    counts, violations = scan_file(path, args.threshold, args.mode, args.scope)
    if not args.quiet:
        print(format_report(path, counts, violations, args.threshold))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
