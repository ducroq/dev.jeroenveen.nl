# Verification record: *Verification is a workflow problem, not a model problem.*

**Article**: `src/pages/writing/verification-is-a-workflow-problem.astro` (status: published 2026-06-01; LinkedIn cross-post 2026-06-02)
**Article slug**: `verification-is-a-workflow-problem`
**Last verified**: 2026-06-02
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md), adapted for a mixed-surface piece (own-work observation + framework characterisation + intentionally anonymised numeric claims).

**Built retroactively** (2026-06-02, two days after article publish; surfaced by `/curate` check during session wrap-up). The article shipped without this record being created — a workflow gap, not a calibration decision. The retroactive record below maps confidence tiers to the language as it was published. If any claim's tier comes out below what the published language asserts, the gap is logged in the **Remaining gaps** section for revisit.

The article has only one explicit external link (the agent-ready-papers GitHub URL). No traditional Sources block at the end. The verifiable surface is therefore:
- The framework characterisation (paragraph 8): tested against the agent-ready-papers repo content.
- The model-level technique characterisations (paragraphs 6–7): RAG, citation checkers, grounded generation, judge models — tested against `docs/glossary.md` definitions and standard LLM-engineering usage.
- The fresh-session-reviewer pattern (paragraph 2): tested against agent-ready-papers DR-011 / Step 7 (Pass 1 small + Pass 2 large, same-family, fresh session).
- The anonymised numeric and category-swap claims (paragraphs 4–5): tested only against Jeroen's research-session notes, which are not public by design.

Confidence tiers map to article language per `docs/writing-guide.md` §7.

---

## Claim 1: The 5.48 GB / million-token context figure (paragraph 4)

**Article wording**:
> A trade-press article had stated that a recent open-weight model needed only 5.48 GB of GPU memory to hold a million-token context, framed as a hardware-does-not-matter-anymore argument. The figure was credited to an unnamed analyst using unspecified modeling benchmarks. The drafting context took the number as authoritative.

| Check | Result |
|---|---|
| Source type | Trade-press article identified during the €5k research session; intentionally not named in the article. |
| Primary reference | Jeroen's research-session notes (private; from the hardware-purchase research exercise the article is built on). |
| Step 0 (does the article identify the source?) | No, by design. The article's argument is that the *pattern* of unsourceable numbers reaches RAG-and-citation-checker-protected workflows; naming the trade-press piece would shift the article from "pattern observation" to "calling out a specific publisher," which is not the intent. |
| Step 4 (scope match) | The article does not claim the 5.48 GB figure is correct or incorrect — it claims (a) the figure was published, (b) it was credited to an unnamed analyst, (c) the drafting context accepted it as authoritative, (d) other sources gave higher figures. All four are statements *about the research session*, not about GPU economics. |
| Step 5 (exact location) | The trade-press URL + the four counter-source URLs live in Jeroen's research-session notes. |
| Step 6 (have I read the relevant section?) | I (the verifier) have not. Jeroen ran the session and the meta-claim is grounded in his direct reading. |
| Confidence tier | **ESTABLISHED** for the meta-claim ("such a figure was published unsourced and accepted in the drafting context"), contingent on Jeroen's notes containing the URLs. **N/A** for the figure's correctness — the article does not assert that. |
| Article language | "had stated", "was credited to", "took the number as authoritative" — all attributional, no claim that 5.48 GB is right or wrong. Matches the tier. |

**Open**: If a reader challenges with "name the trade-press article so I can check," the honest reply is that the article anonymises by design (the pattern matters; the publisher does not). If pressed harder, the URLs are recoverable from Jeroen's notes.

---

## Claim 2: "Four independent technical sources gave figures from 9.6 GB up" (paragraph 4)

**Article wording**:
> Four independent technical sources, when checked, gave figures from 9.6 GB up. The vendor's own model card gave only a relative figure.

| Check | Result |
|---|---|
| Source type | Counter-figures gathered during the same research session. |
| Primary reference | Jeroen's research-session notes (private). |
| Step 4 (scope match) | The claim is "four independent sources gave figures ≥9.6 GB" — a count and a lower bound. The article does not assert that 9.6 GB is *correct*, only that the bottom of the verifiable range is well above the trade-press figure. |
| Step 5 (exact location) | URLs to the four sources + the vendor model card URL live in the research notes. |
| Step 6 (have I read the relevant section?) | I have not. Same situation as Claim 1. |
| Confidence tier | **ESTABLISHED** for the meta-claim (four sources were checked, lower bound was 9.6 GB), contingent on the notes. The claim is structural ("the spread between published-and-quoted vs published-and-sourceable was large") rather than a GPU-memory benchmark assertion. |
| Article language | "when checked, gave figures from 9.6 GB up" — bounded, no over-claim. "The vendor's own model card gave only a relative figure" — attributional. Matches the tier. |

**Open**: Same as Claim 1. The article is making a meta-point about source-tier asymmetry, not a GPU-benchmark claim. A reader who wants to re-run the comparison can be pointed to the notes.

---

## Claim 3: The category swap — code-completion tools vs autonomous coding agents (paragraph 5)

**Article wording**:
> An argument about demand for AI tools that assist with code by completing lines and suggesting edits was using usage data from a different product class: AI tools that run as long-running autonomous agents executing multi-step plans. The two shared the "self-hosted AI agent" framing but did materially different jobs.

| Check | Result |
|---|---|
| Source type | Specific instance from the research session; both product classes intentionally not named. |
| Primary reference | Research-session notes (private). |
| Step 4 (scope match) | The claim is that two different product classes were conflated under shared "self-hosted AI agent" surface framing. The category distinction (code-completion vs autonomous-agent) is real and well-known in the LLM-tooling space. |
| Step 5 (exact location) | The specific platforms + the citation chain live in the notes. |
| Step 6 (have I read the relevant section?) | I have not. |
| Confidence tier | **ESTABLISHED** for the meta-claim (the conflation occurred and was caught by an outside reviewer), contingent on notes. **SUPPORTED** for the structural claim (these two product classes are distinct enough that conflating them is a real error). |
| Article language | Descriptive, no naming. Matches the tier. |

---

## Claim 4: Fifteen issues with near-zero overlap between two fresh-session reviewers (paragraph 2)

**Article wording**:
> Two fresh-session reviewers found fifteen issues in it, with near-zero overlap between them. One was a small same-family model running a mechanical checklist. One was a large same-family model in a fresh session running an argument-shape critique.

| Check | Result |
|---|---|
| Source type | Own-work observation from the research session. |
| Primary reference | Research-session notes. |
| Step 4 (scope match) | The "fifteen issues" count and "near-zero overlap" characterisation are specific and falsifiable from the notes. |
| Step 6 (does the structural pattern match DR-011?) | ✓ Yes. The "small same-family running a mechanical checklist + large same-family running an argument-shape critique" is literally Pass 1 + Pass 2 from `agent-ready-papers/templates/anti-hallucination.md` Step 7. The article's observation is the field-test of DR-011 at blog scale. |
| Confidence tier | **ESTABLISHED** for the count and overlap claim, contingent on notes. **ESTABLISHED** for the structural-pattern match to DR-011 (the template explicitly predicts disjoint coverage). |
| Article language | "fifteen issues", "near-zero overlap" — specific. The matching predictions from DR-011 (Passes 1 and 2 catch essentially disjoint issues) hold. Matches the tier. |

**Note**: This is one of the strongest claims in the article *and* one of the most verifiable from a paper-trail perspective — the issue list exists in the notes. If the article is ever challenged on the "near-zero overlap" claim, the notes are the artefact to point to.

---

## Claim 5: Characterisation of RAG, citation checkers, grounded generation, judge models (paragraphs 6–7)

**Article wording (paragraph 6)**:
> Most advice on catching GenAI mistakes points at the model. Retrieval-augmented generation, citation checkers, grounded generation, judge models. […] Neither error here lives in the model's output. Both live in the drafting context, which the model cannot see from inside.

**Article wording (paragraph 7)**:
> RAG retrieves what you ask for. The drafter had access to the trade-press article and to vendor documentation; what was missing was a prompt to compare them against each other. Citation checkers confirm that referenced sources exist. The 5.48 number had a citation, vaguely, with no name and no methodology. That is exactly the pattern model-level checkers cannot flag. Grounded generation pins outputs to a corpus. It does not check whether the corpus supports the kind of claim the output makes.

| Check | Result |
|---|---|
| Are these terms in standard use? | ✓ All four are standard LLM-engineering vocabulary. |
| Primary references | `docs/glossary.md` (Grounding entry — explicit "Retrieval / factual" sense matches "grounded generation"); `agent-ready-papers/README.md` (RefChecker, scite.ai as citation checkers; RAG / grounded generation as model-level partial solutions); standard LLM-tooling literature. |
| Step 4 (scope match — does each characterisation describe what the technique does?) | RAG "retrieves what you ask for" ✓ (correct: retrieval is query-driven, not comparative). Citation checkers "confirm referenced sources exist" ✓ (correct: existence-check, not claim-match). Grounded generation "pins outputs to a corpus, does not check whether the corpus supports the kind of claim" ✓ (correct: it constrains generation to the corpus but does not evaluate whether the corpus is on-topic for the claim being made). |
| Step 6 (do the characterisations match the glossary?) | The Grounding entry explicitly says: *"grounding-the-technique is upstream of validation, not a substitute for it. A well-grounded model can still produce output that follows from the retrieved sources but is wrong about the world the sources describe, or right about the world but wrong for the engineer's context."* The article's characterisation is the same point applied to a specific failure mode (corpus-supports vs claim-shape). |
| Confidence tier | **ESTABLISHED** for each technique's characterisation; **SUPPORTED** for the inference that *therefore* model-level checkers cannot catch the two specific errors. |
| Article language | "retrieves what you ask for", "confirm that referenced sources exist", "pins outputs to a corpus. It does not check…" — all descriptive of mechanism, not evaluative judgments. Matches the tier. |

**Open**: Judge models are named in paragraph 6 but not given a dedicated characterisation in paragraph 7. The omission is fine for blog scale (the listed three already establish the model-level pattern), but if the article were repositioned as a methodological piece, the judge-model case would need its own sentence. Logged as a remaining gap below.

---

## Claim 6: Agent-ready-papers framework characterisation (paragraph 8)

**Article wording**:
> The framework I have been building is agent-ready-papers (https://github.com/ducroq/agent-ready-papers). The name is paper-specific; the discipline is not. Typed claim registry. Source-tier metadata on every load-bearing claim. Anti-hallucination checklist applied before commit. Multi-pass review with reviewer-bias escapes at two different scales. The paper-specific bits, page budgets, LaTeX, journal style guides, are about twenty percent of it. The other eighty percent is "GenAI failure modes need verification infrastructure because the failures are not noise, they are structural."

| Check | Result |
|---|---|
| Step 0 (does the linked repo exist?) | ✓ `https://github.com/ducroq/agent-ready-papers` resolves; local clone at `C:/local_dev/agent-ready-papers/`. Current release `v1.3.0` (per repo README). |
| Step 4 (does the framework contain a "typed claim registry"?) | ✓ `templates/claim-registry.md`. |
| Step 4 (source-tier metadata on every load-bearing claim?) | ✓ Confidence-tier system (ESTABLISHED / SUPPORTED / EMERGING / SPECULATIVE / PROVOCATION variants) in `templates/claim-registry.md` and applied in this very file. |
| Step 4 (anti-hallucination checklist applied before commit?) | ✓ `templates/anti-hallucination.md`, the file this verification record is built from. |
| Step 4 (multi-pass review with reviewer-bias escapes at two different scales?) | ✓ `templates/anti-hallucination.md` Step 7 + DR-011: Pass 1 (intra-family small, fresh session) + Pass 2 (intra-family large, fresh session) + Pass 3 (cross-vendor, opt-in). The article's "two different scales" maps to Passes 1 and 2. |
| Step 4 (the 20%-paper-specific / 80%-general split — is this a defensible characterisation?) | The repo README explicitly frames the work as verification infrastructure with academic-writing as the worked instantiation, not the limit of generality. The 20/80 split is the author's own estimate of which parts of the templates are LaTeX-/journal-/page-budget-bound vs which are domain-general. As a rough estimate it is defensible; as a hard ratio it is illustrative, not measured. |
| Confidence tier | **ESTABLISHED** for the four enumerated framework components (each maps directly to a file in the repo). **EMERGING** for the 20/80 split as a numeric claim (the split itself is the author's estimate, not a measured ratio). |
| Article language | "Typed claim registry. Source-tier metadata… Anti-hallucination checklist… Multi-pass review…" — all directly verifiable. "are about twenty percent of it" — "about" appropriately hedges the estimate. Matches the tier. |

---

## Claim 7: The three-property workflow that caught the errors (paragraph 8)

**Article wording**:
> What did catch the errors was a workflow with three properties: a registry that named which claims supported which conclusions and required source-tier metadata on each, a fresh-session reviewer with no investment in the conclusion, and a multi-pass structure that escapes the bias of the drafting context at two different scales. The registry is the verification artefact. The reviewer is the verifier. The multi-pass structure is the redundancy. None of this lives inside the model.

| Check | Result |
|---|---|
| Step 4 (does the agent-ready-papers framework instantiate all three properties?) | ✓ Registry (`templates/claim-registry.md` with source-tier per claim); fresh-session reviewer pattern (DR-011 / Step 7 Pass 1 and Pass 2 prescribe fresh sessions); multi-pass structure at two scales (Pass 1 small + Pass 2 large). |
| Step 6 (does the article's claim "none of this lives inside the model" hold?) | ✓ Structurally. The registry is a file in the project. The reviewer is a separate model instance with no shared context. The multi-pass structure is a workflow discipline. None requires modification of the underlying model. |
| Confidence tier | **ESTABLISHED**. |
| Article language | Procedural and structural. Matches the tier. |

---

## Sources block

Not recommended for inclusion in the article body. The piece has one inline link (agent-ready-papers GitHub) which is sufficient. The anonymised sources (trade-press article, vendor model card, four counter-sources) are anonymised by design; surfacing them in a Sources block would defeat the article's intent. The framework / glossary / DR-011 references are internal infrastructure rather than citation-worthy literature.

---

## Cross-model review log

The article *describes* a cross-model review pattern in its central anecdote. Whether the article *itself* received a cross-model review pass before publish is a separate question. From the commit log:

| Commit | What |
|---|---|
| `7f2d62d` | Draft created |
| `90ae428` | Article + diagram landed |
| `ce738f3..7884058..efe3591..d0f3c9b` | Four content edits (opening tightened, category-swap rewritten as concrete-function, "context" threaded through, agent-ready-papers paragraph reframed to own the name mismatch) |
| `2878a61` | Per-page OG image + canonical URL + Twitter card (publish prep) |
| `3fc6ee6` | Draft deleted (article shipped) |

The four-edit sequence between draft-landing and publish-prep is consistent with iterative refinement informed by review (own re-read or cross-model), but I cannot confirm from the commit log alone whether a Pass 1 / Pass 2 cross-model pass was actually run, and there is no preserved review-pass log for this article. Logged as a remaining gap below.

---

## Remaining gaps

The retroactive nature of this record means three things are weaker than they would be if built before publish:

1. **No preserved cross-model review log.** Other articles (`the-model-is-not-the-grader`, the unpulled `who-runs-the-drc`) have detailed Pass 1 / Pass 2 logs with explicit findings tables. This article does not. The commit-log signal is suggestive but not authoritative. **Action:** if cross-model review was run, the findings are gone; if it was not run, this is the cleanest concrete instance of the workflow-step gap that motivated the larger curate flag.
2. **Judge models named but not characterised.** Paragraph 6 lists "judge models" as a fourth model-level technique; paragraphs 6–7 characterise the other three (RAG, citation checkers, grounded generation) but not judge models. Acceptable at blog scale, but the structural argument is slightly weaker than it would be if all four were addressed symmetrically.
3. **The 20%/80% split is illustrative, not measured.** The framework characterisation is otherwise verifiable line-by-line against the repo, but the percentage is the author's estimate. Article language ("about twenty percent") hedges appropriately; a more precise reader will recognise the hedge as a directional claim, not a measured ratio.

---

## Meta-note

This verification record was built **after publish** (2026-06-02), as a consequence of the workflow gap surfaced during session wrap-up. The record itself is one of the better demonstrations of the article's own thesis: a fresh-session reviewer (this verification pass) caught something the drafting context did not (the missing verification record + the asymmetric judge-models treatment). Worth flagging in the next session that the article's workflow argument and the workflow that produced it have a mismatch that is honest to close.
