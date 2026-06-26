---

Item_ID: tt-burden-of-proof-analysis
type: Thinking_Tool
timestamp: "2026-05-11T00:00:00Z"
title: Burden of Proof Analysis
tt_Source: "Common-law and civil-law evidentiary tradition; modern formalizations in evidence textbooks (McCormick on Evidence; Wigmore on Evidence). Standards: preponderance, clear and convincing, beyond reasonable doubt."
tt_Type: instrument
tt_Domain: Discursive-analytical
tt_Field: Legal / juridical reasoning
tt_Operation: Decompose hierarchically
tt_Cross_Domains:
- Modes of inquiry
tt_Form:
- Mental model
- Question bank
- Heuristic
tt_Scale:
- Solo
- Small group
- Civilizational
tt_Duration:
- Single session
tt_Lineage:
- Legal / juridical
- Western analytic / academic
- Religious / monastic
tt_Posture:
- Beginner-friendly
- Expert-required
tt_State: []
tt_Agent:
- Solo human
tt_About:
- Ethics / values
- Power / politics
tt_SOLVE_eX_Phase: [3, 4]
tt_SOLVE_eX_Step: [3.1, 4.3]
tt_Clarifies: ['Path']
tt_Applicability: runtime_applicable
tt_Often_Precedes: []
tt_Often_Follows: []
tt_Pairs_Well_With:
- Bayesian Updating
- Differential Diagnosis
- Falsification
tt_Replaced_By: []
tt_Status: classified
tt_Quality_Tier: B
tt_History:
  - "2026-05-08 — initial classification (Phase 3, schema v1.12.0)"
  - "2026-05-10 — schema v1.13.0: re-anchored to new Domain/Field/Operation via migration script (see migration-crosswalk.md)"
  - "2026-05-10 — Card 04: populated new facets tt_State=[], tt_Agent=['Solo human'], tt_About=['Ethics / values', 'Power / politics']"
  - "2026-05-11 — Zero-Gap Sweep Card 03 facet cleanup: tt_Lineage backfill: added 'Legal / juridical'"
tags:
- '#thinking-tool'
See_Also: []
Date_Added: 2026-05-08
Date_Modified: 2026-05-11
Original_Location: ''
Symlink_Locations: []
File_Attachments: []
Quick_Notes: "Two-part question for any contested claim: who bears the burden of proof, and what's the required standard? Burden of production: who must put forward evidence. Burden of persuasion: who must persuade the fact-finder. Standards (in increasing rigor): preponderance (>50%, civil), clear and convincing (~70-80%, certain civil), beyond reasonable doubt (~95%+, criminal). Operational use beyond law: any contested claim requires the same questions — who must show what, to what standard."
Needs_Processing: false
AI_Instructions: ''

---

# Burden of Proof Analysis

**One-line summary:** A two-part analytical structure for any contested claim — who bears the burden of proof, and what's the required standard — used to focus argument on what actually needs to be shown rather than what would be nice to show.

**When to reach for it:** Legal practice (foundational); any setting with contested claims and decision-making (regulatory, scientific, medical, organizational); decision-making under uncertainty; debate analysis; and as a discipline against shifting-burden arguments.

---

## Purpose Of This Thinking Tool

In any contested claim, two questions structure the argument:

1. **Who bears the burden?** — Who must prove the claim?
2. **What standard applies?** — How much proof is required?

The non-obvious operational insight is that **most weak arguments fail because they implicitly try to shift the burden or relax the standard.** A defendant who argues "the prosecutor hasn't disproved my alibi" has shifted the burden (prosecutor must prove guilt; defendant doesn't need to prove innocence). A claim that "the evidence is consistent with X" applies a vague standard rather than the relevant rigorous one. Naming the burden and standard explicitly disciplines argument.

In law, three standards predominate:

- **Preponderance of the evidence** (>50% probability) — civil cases generally
- **Clear and convincing evidence** (~70-80% probability) — certain civil cases (fraud, paternity, terminated parental rights)
- **Beyond a reasonable doubt** (~95%+ probability) — criminal cases

The standards are matched to the consequences: lower stakes get lower standards; higher stakes (criminal liberty, irreversible deprivation) get higher standards. The choice of standard is itself a normative claim about how to allocate the cost of error.

A second insight: **burden allocation reflects judgment about who can bear the cost of uncertainty.** In criminal law, the prosecution bears the burden because the consequences of wrongful conviction (loss of liberty) are severe and irreversible. In civil law, the burden often goes to whoever has access to the evidence (negligence: plaintiff initially; affirmative defenses: defendant). The allocation isn't arbitrary; it tracks moral and practical considerations.

A third insight: **the framework extends beyond legal context.** Any contested claim raises the same questions:

- Who's making the claim?
- What standard applies (informally) to that claim?
- Has the standard been met?

Scientific claims have their own standards (statistical significance, replication, mechanism); regulatory claims have theirs (precautionary, risk-based); organizational claims have theirs (data-driven, consensus-driven). Naming burden and standard improves clarity.

## Why Use This Thinking Tool

Three failure modes the framework prevents:

1. **The burden-shift fallacy.** "You haven't proven my claim is wrong" implicitly puts the burden on the wrong party. Recognizing burden allocation prevents this rhetorical move.
2. **The standard-vagueness failure.** "There's some evidence for this" is non-specific; "the preponderance standard is met" is. Specificity sharpens argument.
3. **The mismatched-standard error.** Applying a too-rigorous standard (paralyzes decision) or too-lax (produces wrong decisions) both fail. Matching standard to stakes is the calibration.

For lawyers, judges, scientists, regulators, executives, and anyone making contested decisions, burden-of-proof analysis is foundational reasoning structure.

## How To Use This Thinking Tool

```
|======|=================================================================================|
| Step |                                     Action                                      |
|======|=================================================================================|
|    1 | Identify the contested claim. What specifically is being disputed?              |
|    2 | Identify the proponent. Who is asserting the claim?                              |
|    3 | Allocate burden. By default, the proponent bears the burden of production       |
|      | (must put evidence forward) and persuasion (must convince the fact-finder).     |
|    4 | Identify the applicable standard. Match to the stakes: low for routine,         |
|      | moderate for serious civil, high for criminal / irreversible.                    |
|    5 | Audit the evidence against the standard. Does the proponent's evidence meet it?  |
|    6 | If yes: the burden shifts (in some cases) to the opponent for affirmative      |
|      | defenses or counter-claims, with their own standards.                            |
|    7 | If no: the proponent fails to carry the burden; the claim is rejected.         |
|    8 | Watch for burden-shift attempts. Each side may try to put the burden on the    |
|      | other. Hold the burden where it belongs.                                         |
|======|=================================================================================|
```

## The Actual Thinking Tool

```
THE BURDEN-AND-STANDARD TEMPLATE

   Contested claim: ___________________________________________

   Proponent (asserts the claim): ____________________________
   Opponent (resists the claim): _____________________________

   APPLICABLE BURDEN:
       Burden of production (who must put evidence forward):
       ____________________________________________________
       Burden of persuasion (who must persuade fact-finder):
       ____________________________________________________

   APPLICABLE STANDARD:
       [ ] Preponderance (>50%, civil default)
       [ ] Clear and convincing (~70-80%, special civil)
       [ ] Beyond reasonable doubt (~95%+, criminal)
       [ ] Other / domain-specific: ____________________

   Evidence presented by proponent:
       ____________________________________________________

   Does the evidence meet the standard? Y / N / borderline

   If burden shifts (affirmative defense), repeat for opponent.

THE THREE STANDARDS WITH PROBABILITY TRANSLATIONS

   PREPONDERANCE OF THE EVIDENCE (>50%):
       More likely than not. The "tipping point" standard.
       Used in: most civil litigation.
       Translates to: P(claim is true) > 0.5

   CLEAR AND CONVINCING EVIDENCE (~70-80%):
       Highly probable. Substantially more likely than not.
       Used in: fraud claims, certain family-law decisions,
       some administrative actions.
       Translates to: P(claim is true) > ~0.75

   BEYOND A REASONABLE DOUBT (~95%+):
       Near certainty; serious doubt eliminated.
       Used in: criminal liability, certain serious civil
       cases.
       Translates to: P(claim is true) > ~0.95

   These are heuristic translations; legal practice doesn't
   typically state them as numerical probabilities. But the
   ordinal relationship is consistent.

THE BURDEN-SHIFTING CATALOG

   In litigation, burdens shift in patterned ways:

   1. PRODUCTION SHIFT
       Once proponent has produced sufficient evidence to make
       a prima facie case, the opponent must produce
       counter-evidence.
       
       Example: in employment discrimination, plaintiff makes
       prima facie case; burden shifts to employer to articulate
       legitimate non-discriminatory reason.

   2. PERSUASION SHIFT
       Less common; some statutes shift persuasion burden.
       
       Example: certain affirmative defenses (insanity, self-
       defense in some jurisdictions) place persuasion burden
       on defendant.

   3. PRESUMPTION-BASED SHIFT
       Legal presumptions (e.g., presumption of innocence,
       presumption of legitimacy) shift the burden to the party
       opposing the presumption.

   Knowing where burdens currently sit (after various shifts)
   is the foundational tactical question.

THE STANDARD-CALIBRATION PRINCIPLE

   The required standard should track the stakes:

   Higher stakes (irreversible, life-affecting) → higher standard
   Lower stakes (reversible, recoverable) → lower standard

   Different standards reflect different choices about how to
   distribute the cost of error:

   Type I error: false positive (wrongly concluding the claim).
   Type II error: false negative (wrongly rejecting the claim).

   Higher standards reduce Type I errors at cost of more Type II
   errors. Criminal beyond-reasonable-doubt accepts more freed
   guilty (Type II) to reduce wrongful convictions (Type I).
   Civil preponderance balances Type I and Type II nearly equally.

THE OUTSIDE-LAW APPLICATIONS

   SCIENTIFIC CLAIMS:
       Standard: statistical significance + replication +
       mechanism.
       Burden: claimant of the new finding.

   REGULATORY DECISIONS:
       Standards vary: precautionary (high; favor caution) vs.
       risk-based (cost-benefit). Burden often on regulator to
       show necessity.

   MEDICAL DIAGNOSIS:
       Standards vary: high (life-threatening, irreversible
       treatment) vs. moderate (reversible). Burden on physician
       to support diagnosis.

   ORGANIZATIONAL DECISIONS:
       Standard depends on stakes. Burden often on the
       proponent of change.

   In each domain, naming the burden and standard improves
   clarity. Most fuzzy decision-making fails to be explicit
   about either.

THE COMMON FAILURE MODES

   1. BURDEN SHIFT VIA RHETORIC
        "You can't prove me wrong" puts burden on the wrong
        party. Recovery: name where burden actually sits.

   2. STANDARD VAGUENESS
        "There's evidence for this" is unspecific. Recovery:
        name the standard; check whether it's met.

   3. STANDARD MISMATCH
        Applying criminal standard to ordinary decisions
        (paralysis); applying preponderance to criminal
        (wrongful convictions). Recovery: match standard to
        stakes.

   4. PRESUMPTIONS UNRECOGNIZED
        Legal presumptions create implicit burdens. Recovery:
        identify presumptions; note who they favor.

   5. CONCLUSORY CLAIMS
        "X is true" without showing the evidence meets the
        standard. Recovery: explicit evidence-to-standard
        analysis.

THE NON-LEGAL TRANSFER

   For organizational / scientific / regulatory claims:

   1. Name the proponent.
   2. Identify the standard appropriate to the stakes.
   3. Audit evidence against standard.
   4. Don't accept burden-shift attempts.

   This discipline catches most weak arguments — the ones
   that work by shifting burden, vagueness about standards, or
   conclusory assertion.
```

> **Operational notes:** Four disciplines. (1) Name the burden and standard explicitly. Most weak arguments fail by leaving these implicit. Naming them disciplines argument and prevents burden-shift attempts. (2) Match standard to stakes. Higher-stakes / irreversible / life-affecting claims need higher standards; lower-stakes / reversible claims tolerate lower. The mismatch produces decision failure. (3) Watch for burden shifts. Both sides may try to put the burden on the other. Hold the burden where it belongs based on default rules and presumptions. (4) The framework transfers. Scientific, regulatory, medical, and organizational claims face the same structural questions. Naming proponent, standard, and evidence-to-standard meeting catches weak arguments across domains.
