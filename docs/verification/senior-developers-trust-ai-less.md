# Verification record — *Senior developers trust AI less than juniors.*

**Article**: `src/pages/writing/senior-developers-trust-ai-less.astro` (status: draft, awaiting publish)
**Article slug**: `senior-developers-trust-ai-less`
**Last verified**: 2026-05-10
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md).
**Ground truth**: HAN Digital Engineers research project (`OneDrive - HAN/Research/Digital engineers/propositions/CLAIM-REGISTRY.md`, v0.15, 258 claims, 82% verified). Primary-source extractions in `OneDrive - HAN/Research/Digital engineers/sources/`.

This record is the audit trail for every load-bearing statistic in the article. It exists so that any reader who asks *"where does that number come from?"* can be pointed at a specific source, with verification status, sample size, and the confidence tier under which the article uses the claim.

---

## Confidence tiers used in this record

Per agent-ready-papers convention, a claim's tier maps to the language used in the article:

| Tier | Language | Use when |
|---|---|---|
| ESTABLISHED | "demonstrates", "shows", "confirms" | Verified at primary source, exact numbers, sample identified |
| SUPPORTED | "found", "indicates", "evidence suggests" | Verified via registry chain or analysis layer; primary-source extraction may be partial |
| EMERGING | "may", "preliminary evidence" | Plausible but disputed or partially extracted |
| SPECULATIVE | "warrants investigation", "remains unclear" | Source identified but key details unverified |

---

## Claim 1 — JetBrains 2025: senior 61% / junior 48% low trust

**Article wording (paragraph 2)**:
> JetBrains' 2025 Developer Ecosystem survey of 24,500 software developers found that those with ten or more years of experience report low trust in AI output 61% of the time. Those with zero to two years of experience report low trust 48% of the time.

| Check | Result |
|---|---|
| Registry ID | P2-H1b `[VERIFIED]` `[P0]` |
| Source | JetBrains. (2025). *The State of Developer Ecosystem 2025.* |
| URL (Step 0) | https://www.jetbrains.com/lp/devecosystem-2025/ → redirects to https://devecosystem-2025.jetbrains.com/ |
| Sample size | **24,534 confirmed at primary source** (verbatim: *"24,534 people across the globe"*, *"24,534 developers after data cleaning"*). Article uses "24,500" — acceptable rounding. The HAN ANALYSIS file's "26,000+" figure is wrong. |
| Step 4 (scope match) | ✓ Survey covers AI adoption, trust, and use, organised in a dedicated AI section |
| Step 5 (exact location) | The 61% / 48% experience breakdown is **not on the landing page** as accessed 2026-05-10. The landing page directs readers to detailed section pages and the full report PDF for AI-trust statistics. |
| Step 6 (read section) | **Could not verify directly.** Attempted `https://devecosystem-2025.jetbrains.com/ai/` — returned HTTP 404. The full report or the AI section page would need to be located via a link on the landing page that this WebFetch tool did not surface. |
| Confidence tier | **SUPPORTED** — registry verified at P0, sample size confirmed at primary source, experience breakdown not directly verified at primary source by this session |
| Article language | "found" — appropriate for SUPPORTED tier |

**Outstanding work**: If a pedantic reader pushes back on the 61% / 48% breakdown, locate the JetBrains 2025 AI report section page or the full PDF, find the exact section, and either confirm the numbers or update the verification record. Note: the HAN Digital Engineers research project treats P2-H1b as `[VERIFIED]` `[P0]` (their highest tier), so the registry's verification chain stands behind the claim. The dependency is on the registry author's source check.

---

## Claim 2 — Stack Overflow 2025

**Article wording (paragraph 2, current draft)**:
> Stack Overflow's 2025 Developer Survey, separately, with 65,000 respondents, found that overall trust in AI output has been declining year over year, from 52% in 2023 to 46% in 2025. The decline is not driven by people who never tried it. It is driven by people who used it most.

| Check | Result |
|---|---|
| Source | Stack Overflow. (2025). *2025 Developer Survey.* |
| URL (Step 0) | https://survey.stackoverflow.co/2025 |
| Step 6 (read primary source) | **Done 2026-05-10 via WebFetch.** See findings below. |
| Confidence tier (current draft) | **REJECTED** — multiple specific factual errors |

**Primary-source findings (2026-05-10)**:

| Article claim | Primary source says | Verdict |
|---|---|---|
| "65,000 respondents" | "Stack Overflow received over 49,000+ responses from 177 countries" | **Wrong number.** Article's 65,000 likely from earlier-year survey or hallucinated. |
| "trust… declining year over year, from 52% in 2023 to 46% in 2025" | No year-over-year trust trend stated on accessed page. The page DOES state: *"Positive sentiment for AI tools has decreased in 2025: 70%+ in 2023 and 2024 to just 60% this year"* — but sentiment ≠ trust. | **Unsupported as written.** The 52% / 46% pair from the HAN analysis file does not appear in primary source. |
| "decline is not driven by people who never tried it. It is driven by people who used it most" | Not supported by primary source as accessed. | **Unsupported.** |
| Implicit support for "seniors trust less" | *"Experienced developers are the most cautious, with the lowest 'highly trust' rate (2.6%) and the highest 'highly distrust' rate (20%)"* | **Qualitatively supported.** Different framing than JetBrains' 61%/48% but same direction. |

**What the primary source DOES support (verbatim quotes available for the article)**:
- *"More developers actively distrust the accuracy of AI tools (46%) than trust it (33%)"*
- *"The biggest single frustration, cited by 66% of developers, is dealing with 'AI solutions that are almost right, but not quite'"*
- *"Experienced developers are the most cautious, with the lowest 'highly trust' rate (2.6%) and the highest 'highly distrust' rate (20%)"*
- *"Positive sentiment for AI tools has decreased in 2025: 70%+ in 2023 and 2024 to just 60% this year"* (sentiment, not trust)
- *"84% of respondents are using or planning to use AI tools"*

**Recommended rewrite of the Stack Overflow paragraph**:

The current paragraph cannot survive verification as written. Three rewrite options, ordered by how much narrative weight they keep:

> **Option A (closest to current draft, fixed numbers):**
> Stack Overflow's 2025 Developer Survey, separately, with 49,000 respondents, found that more developers actively distrust the accuracy of AI tools (46%) than trust them (33%). The same survey reports that positive sentiment for AI tools dropped from over 70% in 2023–2024 to 60% in 2025. The decline isn't coming from non-users: experienced developers were the most cautious of any bracket, with only 2.6% reporting they "highly trust" AI outputs and 20% reporting they "highly distrust" them.

> **Option B (tighter, drops the time series):**
> Stack Overflow's 2025 Developer Survey, separately, with 49,000 respondents, found that 46% of developers actively distrust AI output accuracy. Of the experienced developers in the sample, only 2.6% reported "highly trusting" AI outputs and 20% reported "highly distrusting" them — the lowest trust and highest distrust of any experience bracket.

> **Option C (drop Stack Overflow entirely, lean on JetBrains alone):**
> Loses the "convergent validity" framing the article currently has, but avoids the contradiction completely. Use only if a clean rewrite is hard to land in voice.

Recommend Option B — it's the most defensible against verification, supports the article's thesis (*"the more time you spend with the tool, the less you trust it"*), and removes the hardest-to-verify claim (the year-over-year trust trend) without losing the load-bearing observation (experienced devs most cautious).

**Notes**:
- The HAN registry's P2-H1b cited Stack Overflow trust-by-experience as "Junior 38%, Mid 44%, Senior 52%" — those numbers do not appear in the primary source page. Likely fabricated or extrapolated in the analysis layer. Worth flagging back to the HAN project team if appropriate.
- The 65,000 sample number used in both the article and the registry is **wrong** per Stack Overflow's own 2025 landing page, which says 49,000+. Possible explanations: (a) carryover from a previous year's survey, (b) early reported number that was later revised, (c) hallucinated. Treat as wrong.

---

## Claim 3 — METR 2025: 19% slower, felt 20% faster

**Article wording (paragraph 6)**:
> The other 2025 study worth pairing with this is METR's. They put senior open-source contributors on tasks in their own codebases, with and without AI assistance. The contributors were 19% slower with AI. They reported feeling 20% faster.

| Check | Result |
|---|---|
| Registry IDs | P1-H1a, P1-H1b `[VERIFIED]` `[P0]` |
| Source | Becker, J., Rush, N., Barnes, B., & Rein, D. (2025, July 25). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.* arXiv:2507.09089v2. |
| Blog URL (Step 0) | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ |
| Paper URL | https://arxiv.org/abs/2507.09089 |
| Local PDF | `OneDrive - HAN/Research/Digital engineers/sources/pdfs/METR-2025-AI-Developer-Productivity-RCT.pdf` |
| Sample size | 16 developers; 246 tasks (2.0 hours on average); repos averaging 23,000 stars; average 5 years of prior experience on those projects; RCT crossover design with screen-recording instrumentation |
| Step 4 (scope match) | ✓ Study explicitly measures AI impact on open-source developer productivity, frontier AI tools (Cursor Pro + Claude 3.5/3.7 Sonnet) at Feb–Jun 2025 capability level |
| Step 5 (exact location) | Abstract, page 1: forecast −24%, measured +19% completion time (slower), post-study estimate −20%. Figure 1 (page 2) plots all forecasts vs observed. |
| Step 6 (read section) | ✓ **Direct primary-source verification done 2026-05-10.** All numbers exact-match against the article: 19% slower (observed), 20% faster (post-study estimate), 23K stars (article doesn't quote this), 16 developers, 246 tasks, RCT design with random allow/disallow per task. METR also reports forecasts 24% (devs pre-study), 38% (ML experts), 39% (econ experts) — all wrong direction. |
| Confidence tier | **ESTABLISHED** — primary-source verified, numbers exact |
| Article language | "were 19% slower with AI. They reported feeling 20% faster" — appropriate for ESTABLISHED tier |

**Notes**:
- METR's own framing is *"highly skilled open-source developers"* with *"average of 5 years of prior experience"* on the specific projects. The article's *"senior open-source contributors"* is a defensible paraphrase but not verbatim. Acceptable.
- METR explicitly states the slowdown does **not** demonstrate the pattern applies to most software developers broadly: *"these results do not imply that current AI systems are not useful in many realistic, economically relevant settings"* (page 3). The article's line *"the calibration is happening, but slowly, and not where the user can feel it"* is the article's reading of what the data implies for senior practitioners, not a METR conclusion. Acceptable for the article's voice but flagged for transparency.
- Authors all listed as METR (Model Evaluation & Threat Research). Two co-first authors (Becker, Rush). This matters for the Sources-block citation format.

---

## Sources block (to embed in the article)

The article uses inline links + a Sources block at the bottom (per the style decision logged 2026-05-10). The block should read:

```
Sources

JetBrains. (2025). The State of Developer Ecosystem 2025.
  https://www.jetbrains.com/lp/devecosystem-2025/
Stack Overflow. (2025). 2025 Developer Survey.
  https://survey.stackoverflow.co/2025
Becker, J., Rush, N., Barnes, B., & Rein, D. (2025).
  Measuring the Impact of Early-2025 AI on Experienced
  Open-Source Developer Productivity. arXiv:2507.09089.
  https://arxiv.org/abs/2507.09089
```

(Citation form for METR uses the arXiv paper rather than the blog post, since the paper is the canonical record. The blog post is a friendlier landing page; either URL is acceptable, but the arXiv paper is the version that survives long-term.)

---

## Local PDF library (HAN Digital Engineers project)

PDFs available locally for direct Step 6 verification:

| Source | Local PDF path |
|---|---|
| METR 2025 (this article, claim 3) | `OneDrive - HAN/Research/Digital engineers/sources/pdfs/METR-2025-AI-Developer-Productivity-RCT.pdf` ✓ Step 6 done |

PDFs *not* available locally for this article's claims:
- JetBrains 2025 — no local PDF, web only (URL https://www.jetbrains.com/lp/devecosystem-2025/)
- Stack Overflow 2025 — no local PDF, web only (URL https://survey.stackoverflow.co/2025)

---

## Outstanding tasks before publish

1. ~~**Rewrite the Stack Overflow paragraph**~~ ✅ Done 2026-05-10. Option B applied to the draft. Inline links added on JetBrains, Stack Overflow, and METR mentions. Sources block added at the end of article body.
2. ~~**WebFetch JetBrains 2025**~~ ✅ Attempted 2026-05-10. Sample size confirmed (24,534). Experience breakdown not on the landing page; AI section path returned 404. Claim 1 stays at SUPPORTED tier, registry-verified.
3. ~~**Audit paragraph 8 for modesty register**~~ ✅ Done 2026-05-10. Rewritten to *"Juniors will inherit a code base shaped by validation that did not happen."* — same point, no implication that juniors are the source of the problem.
4. ~~**Verify the paragraph-5 ese-bot retrieval-function moment**~~ ✅ Confirmed 2026-05-10 by Jeroen as broadly accurate to a real moment ("not exactly that, but something close"). Specific corrections applied: "twenty minutes" → "fifteen minutes" (real recall); "five seconds" → "seconds" (the "five" was unverified; the order-of-magnitude contrast is preserved without claiming a stopwatch value). Surrounding details (codebase, retrieval function, boundary error) accepted as close-enough characterisations of the actual moment.
5. Cold re-read the article one more time after the edits land, then move to `src/pages/writing/senior-developers-trust-ai-less.astro` and ship.

---

## Method note

This record applies the agent-ready-papers anti-hallucination checklist (Step 0 + Steps 4–6) at blog-post scale. The full Gate 1–4 academic flow (Toulmin/Whetten typing, peer-review simulation, equation verification) is overkill for a personal essay; the surviving move is *verify each pinned statistic, log the evidence, calibrate language to confidence tier*. The HAN Digital Engineers project's CLAIM-REGISTRY (258 claims, 82% verified) is treated as the authoritative chain-of-evidence. Where the registry is internally inconsistent (as on Stack Overflow's trust trend), the article must verify directly at primary source rather than picking one registry entry.
