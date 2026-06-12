# Verification record: *Claim verification is now a product. For reading, not writing.*

**Article**: `drafts/claim-verification-is-now-a-product.md` (status: **draft, not yet published**)
**Article slug**: `claim-verification-is-now-a-product`
**Last verified**: 2026-06-12
**Method**: Anti-hallucination checklist (Step 0 + Steps 4-6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md).
**Ground truth**: Direct WebFetch of Elsevier primary pages (2026-06-12, this session) + agent-ready-papers internal logs (`CHANGELOG.md` v2.2.4 candidate, `audits/dsp-workshop-pilot/`). The agent-ready-papers literature entry L48 (`literature/sources/elsevier-researcher-future-2025.md`, same date) records the same survey verification; this record re-states it independently rather than citing the registry as authority, per writing-guide Section 7 ("trace each number to primary source, not to a downstream registry that says it's already verified").

---

## Claim 1: Survey numbers (84% / 22% / 3,200 / 113 countries)

**Article wording (paragraph 1)**:
> Elsevier surveyed 3,200 researchers across 113 countries and published two numbers that belong side by side: 84% have used AI tools. 22% believe those tools are trustworthy.

| Check | Result |
|---|---|
| Source | Elsevier. (2025). *Researcher of the Future*, Confidence in Research series. |
| URL (Step 0) | https://www.elsevier.com/insights/confidence-in-research/researcher-of-the-future |
| Step 4 (scope match) | Survey covers researcher AI adoption, trust, training, governance, research integrity. Match. |
| Step 5 (exact location) | Full report PDF (26 pp., https://assets.ctfassets.net/o78em1y1w4i4/137SmnpRSP2mSuhDxtFdls/72a1777e8a72f3c60748956037f76433/Researcher-Of-The-Future.pdf): methodology box p.4; 84% in Figure 1 p.12; 22% in Figure 2 p.13. |
| Step 6 (read section) | **Done at primary source (PDF) 2026-06-12.** Figure 1 (p.12): 84% have used an AI tool (58% for work + 26% non-work only; 16% never; question: "Have you used an AI (including generative AI) tool or an AI feature on an existing tool you use?"; base n=3,234). Figure 2 (p.13) + body text verbatim: "22% of respondents believe AI tools are currently trustworthy, compared to 39% who say they are unreliable." Methodology (p.4): online survey by email invitation, August-September 2025; 3,234 active researchers and leaders across academia, R&D-led corporations and research institutions, 113 countries; responses geographically weighted (regional bases: NA 480, SA 141, Europe 848, APAC 1,534, MEA 128). |
| Confidence tier | **ESTABLISHED**: both numbers verified at the full report PDF, exact figures and question wording identified, sample and fieldwork dates confirmed. |
| Article language | "surveyed... and published two numbers" - attributed statement of what Elsevier reports. Appropriate. The article never generalises the numbers beyond the survey. |

**Caveats carried into the article**:
- Industry self-published survey, not peer-reviewed. Elsevier has a commercial stake: the same numbers underwrite LeapSpace marketing. The article handles this by attributing every figure to Elsevier and by *using* the conflict structurally (the survey is the product's pitch).
- The 22% wording is about belief that AI tools are trustworthy, not about willingness to use them. Article preserves this ("believe those tools are trustworthy").
- Conflation risk: distinct from Elsevier's *Insights 2024: Attitudes toward AI* (3,000 researchers + clinicians, 123 countries, different figures). This article uses only Researcher-of-the-Future numbers.
- "sixty-two-point spread": 84 - 22 = 62. Arithmetic, not a quoted statistic.

**Spectrum nuance (prepared answer for comments)**: the 22% comes from a bipolar spectrum item (Trustworthy vs Unreliable) with the midpoint not charted. 22% trustworthy side, 39% unreliable side, roughly 39% neutral. So "only 22% call them trustworthy" is exact; "78% distrust them" would be wrong and the article never says it. The article's "sixty-two-point spread" subtracts two same-base percentages (84 use, 22 trust-side); honest as stated.

**Sample composition note**: n=3,234 includes research *leaders* (heads of department, research services directors) alongside active researchers. The article's "3,200 researchers" matches Elsevier's own landing-page self-description ("3,200 researchers across 113 countries") and is acceptable; if a pedantic reader pushes, the precise framing is "3,234 active researchers and leaders".

**Resolved 2026-06-12**: PDF pulled and read; fieldwork dates and sampling frame confirmed (see Step 6). Landing page and PDF agree. Local copy archived at `C:/local_dev/agent-ready-papers/audits/elsevier-researcher-of-the-future-2025.pdf` (gitignored).

---

## Claim 2: LeapSpace launch and features

**Article wording (paragraph 2)**:
> Last November they launched LeapSpace, an AI research workspace, and its flagship features are verification features. Trust Cards show how each AI-generated statement aligns with the source it cites. Claim Radar shows how a claim holds up across the wider literature: how much published evidence supports it, how much contradicts it.

| Check | Result |
|---|---|
| Source | Elsevier launch press release (November 2025) + LeapSpace product page. |
| URLs (Step 0) | https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery ; https://www.elsevier.com/products/leapspace/introducing-research-grade-ai |
| Step 6 (read section) | Done 2026-06-12. Product page verbatim: Trust Cards display *"how a claim aligns with its cited source"*; Claim Radar shows *"how it holds up across the broader body of research"*. Press coverage of the September 2025 announcement describes Claim Radar as surfacing *"how much evidence supports or contradicts"* a claim. Launch announcement November 2025; paid availability Q1 2026; thousands of users reported by 2026. |
| Confidence tier | **ESTABLISHED** for the launch event and feature descriptions (vendor's own pages, descriptions paraphrased closely). |
| Article language | Descriptive present tense for what the features *show*; the article does not claim the features *work as advertised* (see Claim 6 paragraph, which explicitly questions that). |

**Note**: "Last November" is correct relative to a 2026 publish date. If publication slips past 2026, re-date.

---

## Claim 3: Corpus size (sixteen million articles and books)

**Article wording (paragraph 6)**:
> Trust Cards work because Elsevier holds sixteen million full-text articles and books, plus licensing deals with other publishers, to check claims against.

| Check | Result |
|---|---|
| Source | Elsevier launch press release: content base of *"16+ million peer-reviewed articles and books"* plus licensed content (agreements named with Emerald Publishing, IOP Publishing, NEJM Group, Oxford University Press, Sage). |
| Confidence tier | **SUPPORTED as attributed vendor claim**. The article presents it inside an explanation of Elsevier's own business logic, not as an independently audited count. |
| Article language | "Elsevier holds sixteen million..." - acceptable; the sentence's function is the moat argument, which survives even if the count is marketing-rounded. |

---

## Claim 4: "The world's largest scientific publisher"

**Article wording (paragraph 3)**: "The world's largest scientific publisher just bet a flagship product on that view."

| Check | Result |
|---|---|
| Status | Widely used characterisation of Elsevier (by article output and revenue among scientific publishers). Not verified against a ranking source this session. |
| Confidence tier | **SUPPORTED** (common-knowledge characterisation). |
| Action | Acceptable as is. If the cross-model review pass flags it, soften to "the largest scientific publisher" without "world's", or to "Elsevier, the biggest player in scientific publishing". Do not add a citation; a ranking footnote would be heavier than the sentence deserves. |

---

## Claim 5: dsp-workshop equation-check numbers (390 checks / 20 chapters / 19 hard errors)

**Article wording (paragraph 9)**:
> This week I ran an automated equation check across a signal-processing teaching site I maintain: 390 checks over 20 chapters turned up 19 hard numerical errors, including a performance-budget table whose cycle counts contradicted their own total.

| Check | Result |
|---|---|
| Source | Internal: agent-ready-papers `CHANGELOG.md` v2.2.4 candidate entry ("390 checks -> 19 hard errors" across "all 20 equation/number-bearing chapters"; the self-contradictory cycle-count budget table is the named pilot finding) + `audits/dsp-workshop-pilot/full-sweep.md`. Sweep ran 2026-06-11/12. |
| Whose story | Jeroen's own project and own published prose. Writing-guide Section 5: OK to use. |
| Confidence tier | **ESTABLISHED** (internal logs, exact numbers). |
| Article language | "turned up" - appropriate. "Every error sat in prose I had written and published": consistent with the logs (hand-authored .qmd content). |

**Note**: the article says "This week". Correct for a publish date in the week of 2026-06-08. If publish slips, change to "Recently".

---

## Claim 6: The negative claim (no writing-side equivalent)

**Article wording (paragraphs 4, 7, 10)**: "Every one of those verification features runs while you read. None of them run while you write." / "...leaves the practice half where it has always been: with the author." / "The writing half stays open."

| Check | Result |
|---|---|
| Scope | The LeapSpace product page and press releases contain no manuscript-side verification features (checked 2026-06-12: the Reading Assistant interrogates existing articles; no mention of verifying user manuscripts, confidence calibration of user prose, or authoring-time citation checks). The article's claim is scoped to this product and to the absence of *claim-level verification at authoring time as a product*; it does not claim no writing tools exist (grammar checkers, plagiarism scanners, and reference managers exist but do none of the three things the article names: citation-existence checks, confidence-language calibration, numerical reproduction). |
| Confidence tier | **SUPPORTED** for LeapSpace specifically (checked); **EMERGING** as a market-wide absolute. The article avoids the market-wide absolute: "nobody ships one as a flagship" is the strongest formulation used, and it is about flagship products, not all tooling. |
| Risk | A reader may name a startup doing authoring-time claim checks (e.g. citation-screening tools in the Scite family). Scite's citation-context classification is reading-side (how a paper is cited), not authoring-side claim verification, but be ready for the comment. If the cross-model review pass surfaces a genuine counter-example, weaken "nobody ships one" to "no publisher ships one". |

---

## Claim 7: Grounding-chain caveat

**Article wording (paragraph 8)**:
> A Trust Card is the system's own judgment of how well its statement aligns with the source it retrieved. The generator and the judge sit on the same chain, reading from the same corpus.

| Check | Result |
|---|---|
| Basis | Inference from the product's own description (the card is generated by the system that generated the claim, against the corpus it retrieved from), not from an independent audit of LeapSpace internals. Elsevier's own framing supports the human-in-the-loop reading: the product page emphasises *"supporting continuous human validation and critical thinking"*, i.e. the card supports checking rather than replacing it. |
| Confidence tier | **SUPPORTED** (structural inference from vendor's own description; consistent with vendor's own positioning). |
| Article language | "is the system's own judgment" - descriptive of the architecture as documented. The paragraph credits the design as honest before raising the limit, which keeps it from reading as vendor-bashing. |

---

## Sources block (for the .astro version)

```
Sources

Elsevier. (2025). Researcher of the Future: a Confidence in
  Research report.
  https://www.elsevier.com/insights/confidence-in-research/researcher-of-the-future
Elsevier. (2025, November). Elsevier launches LeapSpace.
  Press release.
  https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery
Elsevier. (2026). LeapSpace: the research-grade AI workspace.
  https://www.elsevier.com/products/leapspace/introducing-research-grade-ai
```

---

## Outstanding tasks before publish

1. ~~Pull the Researcher of the Future PDF/databook~~ **Done 2026-06-12.** Fieldwork Aug-Sep 2025, n=3,234 incl. leaders, geographically weighted; 84% and 22% verified at Figures 1-2 (pp. 12-13). Claim 1 upgraded SUPPORTED to ESTABLISHED.
2. Cold re-read after overnight rest (workflow step 2).
3. Cross-model review pass (different model or fresh session, agent-ready-papers `templates/review-prompt.md` Variant B). Filter output against writing-guide Section 6 voice rules.
4. Pre-push gate: `gh api repos/ducroq/agent-ready-papers --jq .visibility` must return `public` (article inline-links the repo).
5. Em-dash audit on the final .astro body (drafted clean, but re-check after any edits).

---

## Method note

Blog-scale calibration: Step 0 + Steps 4-6 per pinned statistic, no Toulmin typing, no gates. All Elsevier-side claims were verified by direct fetch of Elsevier's own pages on 2026-06-12 in the drafting session; nothing was taken from the LinkedIn promo post or third-party coverage except the September-2025 announcement timeline (Research Information, used only in this record for context, not load-bearing in the article).
