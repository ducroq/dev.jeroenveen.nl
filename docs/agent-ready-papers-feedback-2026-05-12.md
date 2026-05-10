# Feedback for `agent-ready-papers` from a blog-post application

Three proposed PRs distilled from applying the framework at blog-post scale on `dev.jeroenveen.nl` between 2026-05-10 and 2026-05-12. Each PR is independent and self-contained.

This file is **staged here for review**, not yet filed in the `agent-ready-papers` repo. Move / split / discard as appropriate.

---

## PR 1 — Document multi-layer source drift as a verification gate

**Suggested title**: `docs(anti-hallucination): document ANALYSIS-vs-ORIGINAL source-layer drift`

### Motivation

Any project that maintains source artifacts in two layers — a primary-source extraction (e.g., `<source>-ORIGINAL.md`, what the source actually says) and an interpretive summary (e.g., `<source>-ANALYSIS.md`, synthesis and framing) — has a quiet failure mode: the interpretive summary can claim things the original extraction does not, and the original extraction itself can diverge from primary source. Downstream consumers (claim registries, citing articles) pick up the drift without checking back against primary, because the verification chain stops at whichever intermediate artifact happens to be the most convenient.

Concrete instances found while applying the framework to a blog post (2026-05-10), in the HAN Digital Engineers research project:

| Source | Project artifacts claimed | Primary source (verified via WebFetch) | Failure mode |
|---|---|---|---|
| JetBrains 2025 | 61% / 48% trust by experience bracket (in ANALYSIS only; ORIGINAL noted "not captured from landing page") | breakdown not present on landing page | ANALYSIS layer drift |
| Stack Overflow 2025 | 52% → 46% trust trend year-over-year (in ANALYSIS only; ORIGINAL had no time series) | no trust trend on the page; only sentiment trend, a different metric | ANALYSIS layer drift |
| Stack Overflow 2025 | n=65,000 (in **both** ANALYSIS and ORIGINAL extraction) | **n=49,000+** | ORIGINAL extraction error (drift entered at the extraction layer, not added at analysis) |

The HAN claim registry cited some of these numbers as `[VERIFIED] [P0]` even though the ORIGINAL extraction in one case explicitly noted the breakdown was *"not captured from the landing page; refer to full report sections"*. The verification chain stopped at an intermediate layer rather than tracing back to the primary source.

Three closely-related issues to fix:

1. **Intermediate-layer drift** (the core problem) — covers both ANALYSIS-adds-content-not-in-ORIGINAL and ORIGINAL-itself-diverges-from-primary
2. **Sample-size errors propagating silently** — n=65K vs 49K wasn't caught for months because sample sizes feel like stable facts
3. **Cross-claim consistency** — the same HAN registry held three incompatible Stack Overflow trust-trend pairs (52→46, 40→29, and a different experience breakdown) without flagging the contradiction

### Changes

- `templates/anti-hallucination.md`: add "Source-Layer Drift" section before the Worked Example
- `templates/anti-hallucination.md`: add Step 5b (sample-size verification)
- `templates/anti-hallucination.md`: add "Cross-Claim Consistency" section after the per-claim checklist
- `audits/`: a new audit file `2026-05-12-blog-application-source-layer-drift.md` documenting the worked example (or merge into an existing `audits/equation-verification-journey.md`-style narrative)

### Proposed text additions to `templates/anti-hallucination.md`

**Insert before "Worked Example":**

````markdown
## Intermediate-Layer Drift

Some projects keep source artifacts in multiple layers — typically a **primary-source extraction** (e.g., `<source>-ORIGINAL.md`, what the source actually says) and an **interpretive summary** (e.g., `<source>-ANALYSIS.md`, synthesis and framing). The pattern is useful, but every layer between the citing article and the primary source is a place drift can accumulate. Two failure modes:

- **Analysis layer adds content not in the extraction.** The summary asserts a number, breakdown, or framing that does not appear in the primary-source extraction. Downstream consumers cite the analysis layer's number without checking the extraction.
- **Extraction itself diverges from primary.** Even the "ORIGINAL" file can be wrong — a sample size carried over from a previous edition, a number copied from a press release rather than the published page, an OCR error. Both layers in the project agree, but neither matches primary source.

**The check**: when verifying a claim, identify which artifact in the project the cited number comes from, then trace it all the way back to primary source — not just to the most-primary-looking intermediate artifact.

**Worked failure mode (analysis-drift)**: A project's analysis file claimed an experience-by-experience breakdown of trust percentages from a survey. The original extraction said the breakdown was *"not captured from the landing page; refer to full report sections"*. The breakdown propagated into the project's claim registry as `[VERIFIED] [P0]`. Direct primary-source verification (WebFetch on the actual landing page) found that the breakdown is not on the publicly-accessible page at all.

**Worked failure mode (extraction-drift)**: A project's ORIGINAL extraction recorded the survey's sample size as n=65,000. The analysis file repeated it. The article cited it. Primary-source verification (WebFetch on the survey landing page) found the actual figure was 49,000+. The extraction itself was wrong; the verification chain treated the ORIGINAL file as authoritative and never re-checked.

When you cannot trace a number to a primary source, the citation should sit at SUPPORTED tier at most, not ESTABLISHED — even if a downstream artifact says it's verified.
````

**Add to Step 5 ("Is the exact location cited?"):**

```markdown
- [ ] **5b. Is the sample size verified?**
  - Sample sizes propagate through summaries unchecked because they feel like stable facts
  - Re-verify the N alongside the finding, not as a footnote
  - Watch for: an N quoted from a previous-year survey, an early reported number that was later revised, or an N hallucinated entirely
```

**Add as a new section after the Quick Version.** *(Note: this introduces a new tag, `[NEEDS RECONCILIATION]`, that does not exist in the current registry tag set. The maintainer should decide whether to add it formally to the tag legend in the registry template; the alternative is to leave the conflict in a comment on the affected claim rows.)*

```markdown
## Cross-Claim Consistency

When N claims in the same registry cite the same source, do they agree on basic facts? Specifically:
- Sample size (does every claim citing the source state the same N?)
- Year and edition
- Top-line headline numbers

A registry can develop internal contradictions when claims are added by different sessions or different drafts. The fix is a periodic cross-claim consistency pass:

1. Group claims by source
2. For each source group, compare the basic facts
3. Where claims disagree, mark all claims in the group `[NEEDS RECONCILIATION]` (a new tag, see legend) or annotate each affected row with the conflict, until primary source resolves the disagreement

This is a cheap pass that catches drift across registry rows that the per-claim checklist misses.
```

---

## PR 2 — Add non-academic / blog-post use case to framework docs

**Suggested title**: `docs: add non-academic use case (blog post / personal essay) to framework`

### Motivation

The framework was designed around academic papers — formal claim registries, Toulmin/Whetten typing, Gate 1–4 review, peer-review simulation. The full machinery is overkill for blog posts, personal essays, internal memos, or technical articles, but the underlying anti-hallucination move is exactly what such writing needs.

When the framework was applied at blog-post scale on `dev.jeroenveen.nl` (2026-05-10 to 2026-05-12), a clean adaptation pattern emerged. Documenting it would let other practitioners apply the framework to non-academic writing without having to figure out the right-sizing from scratch.

### Changes

- New file: `docs/non-academic-use.md`
- Update to `README.md`: a one-paragraph mention of the non-academic use case, linking to the new doc

### Proposed new file: `docs/non-academic-use.md`

*The full proposed content of the new file is below, in fenced markdown so it can be lifted directly. Everything inside the outer fence is the file's intended contents.*

````markdown
# Non-Academic Use: Blog Posts, Essays, Memos

The framework's anti-hallucination machinery was designed for academic papers. The full machinery (formal claim registry, Toulmin/Whetten typing, Gate 1–4 review, peer-review simulation) is overkill for blog posts, personal essays, internal memos, or technical articles.

The right-sized adaptation:

## Skip
- Formal claim registry (with Toulmin/Whetten typing and P0/P1/P2 priority bands)
- Gate 1–4 review structure
- Peer-review simulation (`templates/review-prompt.md`)
- Equation verification (unless your post is calculation-heavy)

## Keep
- **Step 0** of the anti-hallucination checklist (web search / DOI check)
- **Steps 4–6** of the checklist (scope match, exact location, read the section)
- **Confidence tier → language mapping** as documented in `templates/writing-guide.md` (no parallel mapping needed — the same tiers and language guidance carry over from the academic case)
- **Per-article verification record** as a lightweight version of the claim registry
- **Sources block** in the article footer as the public-facing trace

## Per-article verification record

A structure that worked for the dev.jeroenveen.nl portfolio site (n=1; adapt as your project requires). The point is the discipline of having one verification record per published artifact, not the exact field set:

```
# Verification record — *<article title>*

**Article**: <path to article file>
**Status**: <draft / published>
**Last verified**: <YYYY-MM-DD>
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6)
**Ground truth**: <project ground truth: registry, primary sources, etc.>

## Claim 1 — <article wording>

| Check | Result |
|---|---|
| Source | <citation> |
| URL | <Step 0> |
| Step 4 (scope match) | <pass/fail with note> |
| Step 5 (exact location) | <where in source> |
| Step 6 (read section) | <pass/fail with note> |
| Confidence tier | ESTABLISHED / SUPPORTED / EMERGING / SPECULATIVE |
| Article language | <quote from article + comment on whether the language matches the tier> |

[repeat for each load-bearing claim]

## Sources block

[exact text to render in the article's footer]

## Outstanding tasks

[list of follow-ups]
```

## In-article presentation

Two surfaces of citation, working together:
- **Inline links** on source mentions in the prose (one link per source on first mention)
- **Sources block** at the end of the article body, listing each citation with full URL

This pairs with the verification record (internal, audit-trail) and lets readers chase the sources without academic-style footnotes. Adapt to whatever in-article presentation fits the platform; the verification record is the load-bearing artifact, not the cosmetic surface.

## Retroactive verification

The framework can also be applied to already-published material — see the "Retroactive verification" entry under "When to Run This Checklist" in `templates/anti-hallucination.md`.
````

### Proposed `README.md` addition

In a new "Use Cases" section (e.g., after the existing Status section):

```markdown
## Use Cases

The framework targets academic papers (Toulmin/Whetten typing, formal claim registry, Gate 1–4 review). For blog posts, essays, technical articles, and internal memos, see [docs/non-academic-use.md](docs/non-academic-use.md) for a right-sized adaptation that keeps the anti-hallucination machinery and drops the academic overhead.
```

---

## PR 3 — Polish anti-hallucination checklist for web sources, retroactive use, and framing accuracy

**Suggested title**: `docs(anti-hallucination): add web-source notes, retroactive use case, and framing-accuracy check`

### Motivation

Three smaller polish items discovered during a blog-post application of the framework:

1. The current `templates/anti-hallucination.md` Worked Example uses a journal article with DOI. Many citation sources today are web pages (survey landing pages, model cards, project homepages) that have no DOI but can be verified via WebFetch. The checklist applies cleanly to web sources, but the docs don't say so.
2. The framework's "When to Run This Checklist" guidance covers pre-publication and re-verification of changed claims, but not retroactive application to already-published material. That's a valuable use case worth naming explicitly.
3. The four confidence tiers cover whether a claim is *supported*, but not whether the article's *framing* is accurate to what the source says. One instance found during the application: the claim was technically correct but the framing slightly overstated the source ("EuroLLM covers 35 EU languages" — true number, but only 24 of the 35 are EU official languages).

### Changes

- `templates/anti-hallucination.md`: add "Web Sources" subsection under Step 0
- `templates/anti-hallucination.md`: add "Retroactive verification" item to "When to Run This Checklist"
- `templates/anti-hallucination.md`: add "Framing Accuracy" check as a separate concern from claim verification

### Proposed text additions

**Under Step 0, add:**

```markdown
### Web Sources

For citations to web pages (survey landing pages, model cards, project homepages, blog posts) rather than journal articles:

- Step 0 = "page exists at URL and looks like the cited source"
- Step 6 = "the specific claim appears on that page" (use programmatic fetch / WebFetch / curl)

The distinction matters: a survey landing page might exist (Step 0 passes) but not contain a specific breakdown that's been attributed to it (Step 6 fails). For web sources, always do Step 6 separately, not as a side-effect of Step 0.

Watch for:
- Carry-over numbers from a previous year's edition of the same survey
- Numbers that exist in a downloadable PDF but not on the landing page (verify against the PDF, not the page)
- Year-over-year trends being conflated across editions when only the latest is publicly accessible
```

**Add to "When to Run This Checklist"** (the existing four bullets stay; insert one new bullet):

```markdown
- **Retroactive verification:** Apply to already-published material to catch drift. Steps 0 + 4–6 per claim. Result: a verification record and any minor calibrations needed (republish if minor; flag for revision if a claim doesn't survive verification).
```

**Add as new section after Quick Version:**

```markdown
## Framing Accuracy

The six checks above ask whether the source supports the cited claim. They do not ask whether the article's framing is accurate to what the source actually says.

A common failure mode: the number is correct, but the article's framing slightly overstates, restricts, or generalises the source's actual scope.

**Worked example**: An article writes *"EuroLLM covers 35 EU languages"*. The model card confirms 35 languages and the Apache 2.0 license. But of the 35, only 24 are EU official languages; the other 11 are non-EU (Arabic, Chinese, Hindi, Russian, Turkish, etc.). The number is correct; the framing as "35 EU languages" overstates EU-specificity.

The number is accurate; the framing is not. This isn't a hallucination, but it isn't fully faithful to the source either. The fix is a separate "framing audit" pass:

- Read the article's wording of the claim
- Read the source's exact wording
- Ask: does the article's framing match the source's scope, qualifiers, and population?
- If not, calibrate the framing — usually a small wording change keeps the article's argument intact
```

---

## Where to file

If you want a single repo to land these in, the order I'd suggest:

1. **PR 1 first** (highest leverage, fixes a real category of error that's quietly producing wrong claims)
2. **PR 2 next** (broadens the framework's audience to blog/essay practitioners)
3. **PR 3 last** (polish, smaller surface area)

Each is independent — they can land in any order, or all together. The total surface area is one new file (PR 2's `docs/non-academic-use.md`), three sections added to one existing file (`templates/anti-hallucination.md` across PR 1 and PR 3), and optionally one new audit file (PR 1's worked example).

If you'd rather not file these as PRs and instead capture them in `memory/gotcha-log.md` for later processing, that's also reasonable — they're discoveries from a real application of the framework, which is exactly what the gotcha log is for. Up to you which level of formality.
