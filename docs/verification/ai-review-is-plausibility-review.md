# Verification record: *AI review measures plausibility.*

**Article:** `drafts/ai-review-is-plausibility-review.md` (status: DRAFT awaiting promotion to `src/pages/writing/ai-review-is-plausibility-review.astro`)
**Article slug:** `ai-review-is-plausibility-review`
**Last verified:** 2026-06-05 (pass 1, pre-publish)
**Method:** Anti-hallucination checklist (Step 0 + Steps 4 to 6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md), calibrated to blog-scale per `feedback_polish_loop_calibration.md`. This is the moderate-formality version: every load-bearing statistic, named tool, and coined attribution gets a primary-source trace, but the record skips the elaborate build-history and source-artefact-survey of the maximal version (`verification-is-a-workflow-problem.md`).

**Source artefacts.** The empirical case in the article (68-equation document, two assessment passes returning zero errors, one reproduction pass returning three) is the driven-pendulum retrofit. Primary sources:

- `C:/local_dev/agent-ready-papers/audits/driven-pendulum-retrofit.md` §9.1: the canonical audit document with the case, the three specific errors, and the prompt-mode contrast.
- `C:/local_dev/augmented-engineering/site/src/pages/patterns/reproduce-dont-assess.astro`: the AE pattern page that summarises the case as the empirical anchor for the pattern.
- `C:/local_dev/agent-ready-papers/decisions/DR-009_calculation-verification.md`: the decision record behind the equation-checker template.
- `C:/local_dev/agent-ready-papers/templates/equation-checker.md`: the calculation-verification template named in the article body.
- `C:/local_dev/agent-ready-papers/templates/anti-hallucination.md`: the template named in the article body as the citation-equivalent of the equation-checker.

Confidence tiers map to article language per `docs/writing-guide.md` §7.

---

## Claim 1: Two assessment-mode reviews returned zero errors; one reproduction-mode review returned three (paragraphs 1, 3-5)

**Article wording (compact across the opening):**
> In a 68-equation theory document, two AI reviews in assessment mode caught zero errors. A third pass with the same model family but a reproduction instruction caught three.

| Check | Result |
|---|---|
| Step 0 (does the case appear in a verifiable primary source?) | Yes. `audits/driven-pendulum-retrofit.md` §9.1 documents the case with the same structure: two assessment-mode LLM passes (one Gemini, one Claude) returning zero errors, one reproduction-mode pass (Claude with structured "substitute, compute, compare" prompt) catching three. |
| Step 4 (scope match) | Article does not claim the result generalises beyond the case. The closing kit-paragraph and citation/code-review generalisations are explicitly marked as mechanism-shaped extensions, not as additional empirical replications. |
| Step 5 (exact location) | `audits/driven-pendulum-retrofit.md` §9.1, with the three errors enumerated in §9.1.1-9.1.3. Cross-referenced by the AE pattern page (`patterns/reproduce-dont-assess.astro`) as the empirical anchor. |
| Step 6 (have I read the relevant section?) | Yes, pass 1. Glossary entry at `docs/glossary.md` was updated 2026-05-18 with the same case-summary; the LLM-reproduction framing in this article matches the audit doc and the pattern page, not the (now-outdated) "manual reproduction" phrasing in earlier internal notes. |
| Confidence tier | **ESTABLISHED**. Own work, two aligned primary sources (audit doc + AE pattern page). |

---

## Claim 2: The three specific errors (paragraph 6)

**Article wording:**
> The first was a label mismatch. A table headed "5 degrees" contained values that had been computed at 1 degree. Coupling estimates in the relevant chapter were therefore five times more optimistic than the design called for. The second was a formula error in a dwell-time calculation: a missing variable and a spurious factor of two made the tabulated values roughly seven times too small. The third was an internal inconsistency. An hourly correction stated as 36 s/hr did not survive the arithmetic. 3.3 ms per swing, times 3,600 swings per hour, lands near 12 s/hr, not 36.

| Check | Result |
|---|---|
| Step 0 / 5 (does each error appear in a primary source?) | Yes. All three errors are listed in `audits/driven-pendulum-retrofit.md` §9.1 with the same magnitudes (5x label mismatch, 7x dwell-time error, 36-vs-12 arithmetic). The AE pattern page summarises them with the same numbers. |
| Step 4 (scope match) | Article's numeric specifics match the audit doc. The arithmetic in the body ("3.3 ms per swing, times 3,600 swings per hour, lands near 12 s/hr, not 36") is reproducible in the article surface itself. |
| Step 6 (have I read the relevant section?) | Yes, pass 1. |
| Confidence tier | **ESTABLISHED**. |

---

## Claim 3: The equation-checker template and DR-009 (paragraph 8)

**Article wording:**
> The pattern lives in agent-ready-papers as the equation-checker template, and the decision record behind it is DR-009 (calculation-verification). The 68-equation case is the empirical anchor for both.

| Check | Result |
|---|---|
| Step 0 (do the named artefacts exist?) | Yes. `agent-ready-papers/templates/equation-checker.md` exists. `agent-ready-papers/decisions/DR-009_calculation-verification.md` exists (confirmed via the `DR-009_calculation-verification.md` entry in the decisions/ directory listing). |
| Step 4 (scope match) | Article claims (a) the template exists in the framework, (b) DR-009 is its decision record, (c) the 68-equation case is the empirical anchor for both. (a) and (b) are file-existence claims. (c) is anchored in the audit doc which is the case's canonical record and which DR-009 cites as the empirical motivation. |
| Step 5 (exact location) | `templates/equation-checker.md`; `decisions/DR-009_calculation-verification.md`. |
| Step 6 (have I read the relevant section?) | Pass 1 covered file existence. **Open IOU**: pre-publish, read the DR-009 body to confirm the template-purpose phrasing in the article ("substitute, compute, compare") matches the DR's canonical language. Risk if skipped: paraphrase drift if DR-009 frames the move differently. |
| Confidence tier | **ESTABLISHED**. DR body read 2026-06-05 (IOU 1 cashed); article phrasing matches DR canonical language including the "equation-checker template" name, the Driven Pendulum evidence base, and the "prompt matters more than the model" key insight. |

---

## Claim 4: The anti-hallucination checklist as the citation-equivalent of the equation-checker (paragraph 9)

**Article wording:**
> The anti-hallucination checklist in the same framework is the citation-equivalent of the equation-checker. It forces a check that the source exists and says what the prose says it says, rather than a judgment about whether the citation reads plausible.

| Check | Result |
|---|---|
| Step 0 (does the template exist?) | Yes. `agent-ready-papers/templates/anti-hallucination.md` exists; the writing-guide already references it. |
| Step 4 (scope match) | Article claims the checklist (a) exists in the framework, (b) operates on citations as the equation-checker operates on equations, (c) forces a source-exists-and-says-what-prose-says check rather than a plausibility judgment. |
| Step 5 / 6 (read the relevant section) | **Open IOU**: pre-publish, read the anti-hallucination checklist body to confirm the article's characterisation of its mechanism matches the template's actual instructions. The "Step 6" of the checklist itself ("read the relevant section of the primary source and confirm it says what you claim it says") is the analogue the article points at. Confirm phrasing fidelity. |
| Confidence tier | **ESTABLISHED**. Body read 2026-06-05 (IOU 2 cashed); article's mechanism characterisation (source exists, source says what prose claims it says) matches the template's Steps 1 + 6 and the hallucination-pattern table's "plausible fabrication" entry. |

---

## Claim 5: Multi-pass review escapes drafting-context bias at two scales (paragraph 12, kit-list)

**Article wording (after fix):**
> The other parts of the kit fill in failures that neither of those catches alone.

(Multi-pass review and the claim-registry are referenced obliquely as "the other parts of the kit" rather than named individually. After the 2026-06-05 review-battery fixes, the kit-list was tightened from four named tools to two illustrative ones.)

| Check | Result |
|---|---|
| Step 0 (do the unnamed tools exist?) | Yes. Multi-pass review is documented in `agent-ready-papers/decisions/DR-011_multi-model-review-pattern.md`. The typed claim registry is documented across the framework's README, templates, and DRs. |
| Step 4 (scope match) | Article does not make specific claims about the unnamed tools; it asserts only that they exist as "other parts of the kit". Verification scope is limited to existence. |
| Confidence tier | **ESTABLISHED** for existence; no specific characterisation to verify. |

---

## Claim 6: agent-ready-papers as the framework and inline link (paragraph 8)

**Article wording:**
> The pattern lives in agent-ready-papers as the equation-checker template...

Inline link: `https://github.com/ducroq/agent-ready-papers`.

| Check | Result |
|---|---|
| Step 0 (does the link resolve?) | The same URL was used in `verification-is-a-workflow-problem.astro` (line 116) which is currently published and live. Treat as ESTABLISHED unless the repo has been renamed or made private since 2026-06-01. **Open IOU**: pre-publish, fetch the URL to confirm public accessibility. |
| Confidence tier | **PENDING repo public flip**. Repo currently private (verified via `gh api` 2026-06-05). Inline link 404s for public readers. Will become **ESTABLISHED** once Jeroen flips the repo to public; see IOU 3 in the cashing log below. Pre-promotion gate: re-run `gh api repos/ducroq/agent-ready-papers --jq .visibility` and confirm `public`. |

---

## Claim 7: AE pattern "Reproduce-Don't-Assess" link (paragraph 13)

**Article wording:**
> The pattern that names the equation-specific move is on the augmented engineering site

Inline link: `https://augmented-engineering.eu/patterns/reproduce-dont-assess`.

| Check | Result |
|---|---|
| Step 0 (does the page exist and contain the pattern?) | Local source file confirmed: `C:/local_dev/augmented-engineering/site/src/pages/patterns/reproduce-dont-assess.astro`. **Open IOU**: pre-publish, confirm the page is deployed at the public URL. |
| Confidence tier | **ESTABLISHED** locally. **SUPPORTED** for the public URL: WebFetch returned `ECONNREFUSED` 2026-06-05 (could be transient network issue, not necessarily a real outage); needs browser confirmation by Jeroen pre-promotion. See IOU 4. |

---

## Pre-publish IOUs (cashed 2026-06-05)

1. **DR-009 body read. CASHED ✓.** Read `agent-ready-papers/decisions/DR-009_calculation-verification.md`. DR-009 explicitly names "equation-checker template" (line 49) and lists the Driven Pendulum project as the Evidence Base (line 55: "3/3 errors caught by reproduction, 0/3 by plausibility review"). Key insight in DR-009 (line 42): "For arithmetic verification, the prompt matters more than the model." This matches the article's "Same model. Different mode. Different result." crystallisation. **Claim 3 promoted from SUPPORTED to ESTABLISHED.**

2. **Anti-hallucination checklist body read. CASHED ✓.** Read `agent-ready-papers/templates/anti-hallucination.md`. Step 1 confirms canonical citation (source exists). Step 6 ("Have I read the relevant section?") explicitly asks "Does the source actually say what we claim it says?". The hallucination-pattern table contrasts plausibility-shaped failures (e.g., "Plausible fabrication: Real author + real journal + fake paper") with DOI-check verification. Mechanism characterisation in the article body matches the template. **Claim 4 promoted from SUPPORTED to ESTABLISHED.** *Adjacent finding worth carrying forward:* the template's Step 7 (Multi-Pass Review Across Model Families) is the same three-pass structure now woven with the trust + context-orchestration frame in `drafts/cross-model-review.md`.

3. **agent-ready-papers public URL fetch. FAILED → ACTION PENDING.** `gh api repos/ducroq/agent-ready-papers` returns `visibility: private`. The inline link `https://github.com/ducroq/agent-ready-papers` in paragraph 8 of the article body will return 404 for public readers. This is also the case for the same link in the already-published `verification-is-a-workflow-problem.astro` line 116 (which has been shipping a broken primary-source link since 2026-06-01). **Resolution path (decided 2026-06-05):** Jeroen will flip the repo to public on GitHub before promoting this article. Once that lands, both articles' inline links resolve automatically and no body changes are required. *Pre-promotion gate:* re-run `gh api repos/ducroq/agent-ready-papers --jq .visibility` and confirm `public` before promoting to `src/pages/writing/`.

4. **AE pattern public URL fetch. UNRESOLVED via WebFetch.** WebFetch returned `ECONNREFUSED` on `https://augmented-engineering.eu/patterns/reproduce-dont-assess`. Could be a transient WebFetch network issue rather than a real outage. Local source file at `C:/local_dev/augmented-engineering/site/src/pages/patterns/reproduce-dont-assess.astro` confirmed to exist. **Pre-promotion gate:** Jeroen confirms the URL loads in a browser before promoting.

5. **agent-ready-papers/audits/ public-link check. CONTINGENT on IOU 3 cashing.** `gh api repos/ducroq/agent-ready-papers/contents/audits` confirms `driven-pendulum-retrofit.md` exists in the audits directory (alongside `equation-verification-journey.md`, `feedback-from-*.md`, `proposition-retrofit.md`, etc.). The directory will be publicly browsable as soon as the repo flips to public (IOU 3). Once that lands, add a deep-link to `audits/driven-pendulum-retrofit.md` as a third entry in the Sources block (see updated Sources block proposal below).

## Sources block to embed in the published `.astro`

After IOU 3 (repo public flip) lands, embed:

```html
<aside class="article-sources">
  <span class="article-label">Sources</span>
  <ul>
    <li><a href="https://github.com/ducroq/agent-ready-papers" target="_blank" rel="noopener">agent-ready-papers</a> (framework, templates, decision records)</li>
    <li><a href="https://github.com/ducroq/agent-ready-papers/blob/main/audits/driven-pendulum-retrofit.md" target="_blank" rel="noopener">Driven pendulum retrofit audit, §9.1</a> (the 68-equation case and the three errors)</li>
    <li><a href="https://augmented-engineering.eu/patterns/reproduce-dont-assess" target="_blank" rel="noopener">Reproduce, don't assess</a> (AE pattern page with the empirical case)</li>
  </ul>
</aside>
```

If for any reason IOU 3 does not resolve before promotion, drop the first two `<li>` entries and keep only the AE pattern page link. The framework name in the body prose still functions without the inline link; readers can search for it if and when the repo becomes public.

## Notes

- Verification record built per the moderate-formality calibration. The maximal version (per `verification-is-a-workflow-problem.md`) is overkill for an article whose load-bearing claims are author-side observations on author-side artifacts, all already documented in the framework's own audit trail.
- This record does not separately verify the citation/code-review generalisations in paragraphs 9 and 10. Those are mechanism-shaped extensions, not empirical claims with primary sources to trace.
- Cold re-read pass and final cross-model review pass are tracked separately and gate the promotion to `src/pages/writing/`.
