# Verification record — *The work is splitting. The conversations haven't caught up.*

**Article**: `src/pages/writing/the-work-is-splitting.astro` (status: published 2026-05-01)
**Article slug**: `the-work-is-splitting`
**LinkedIn surfaces**: short post, Pulse article, canonical home — see `memory/external-comments.md` 2026-05-01 entry
**Last verified (retroactive)**: 2026-05-10
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md).
**Ground truth**: HAN Digital Engineers research project (`OneDrive - HAN/Research/Digital engineers/propositions/CLAIM-REGISTRY.md`, v0.15, 258 claims, 82% verified). Primary-source extractions in `OneDrive - HAN/Research/Digital engineers/sources/`.

This record is a **retroactive verification** — the article shipped before this verification framework was set up. The goal here is to confirm the article's load-bearing claims survive the same checklist applied to draft articles, and to flag any open issues that should be corrected if the article is revised.

---

## Claim 1 — "About 90% of engineering teams use AI tools now"

**Article wording (paragraph 6)**:
> About 90% of engineering teams use AI tools now, depending on which survey you trust. That number reads like a triumph.

| Check | Result |
|---|---|
| Registry IDs | P6-H1b `[VERIFIED]` `[P0]`; P2-H3.5e `[VERIFIED]` `[P1]`; P6-H1c `[VERIFIED]` `[P0]` (multi-source) |
| Sources | Jellyfish 2025; DORA 2025 (90% of survey respondents use AI at work); cross-source convergence |
| URLs (Step 0) | https://jellyfish.co/resources/2025-state-of-engineering-management-report/ (registry); https://jellyfish.co/blog/2025-software-engineering-management-trends/ (HAN extract) |
| Sample (Jellyfish) | 600+ engineering professionals |
| Step 4 (scope match) | ✓ Jellyfish 2025 reports *"90% of engineering teams now use AI coding tools (up from 61% annually)"* |
| Step 5 (exact location) | Jellyfish 2025 State of Engineering Management Report, "AI Adoption" section |
| Step 6 (read section) | ✓ HAN source extract confirms verbatim: *"90% of engineering teams now use AI coding tools (up from 61% annually)"*. JetBrains 2025 (85% individual adoption) and Stack Overflow 2025 (84% individual adoption) corroborate the order of magnitude. |
| Confidence tier | **ESTABLISHED** |
| Article language | "About 90%… depending on which survey you trust" — honest hedge, appropriate for ESTABLISHED tier |

**Notes**: The hedge "depending on which survey you trust" is well-calibrated. Jellyfish gives 90% for *teams*, JetBrains 85% for *individuals*, Stack Overflow 84% for *individuals* — different populations, but all in the 84–90% band. The article's framing survives all three.

---

## Claim 2 — "In Jellyfish's 2025 survey, only 20% of organisations using AI extensively could measure its impact"

**Article wording (paragraph 6)**:
> Underneath it sits a different number: the share of teams that can say, with evidence, what their AI use is actually doing to their output quality. In Jellyfish's 2025 survey, only 20% of organisations using AI extensively could measure its impact. The other 80% are doing the work and hoping.

| Check | Result |
|---|---|
| Registry ID | P5-H4b `[VERIFIED]` `[P1]` |
| Source | Jellyfish. (2025). *State of Engineering Management Report.* |
| URL (Step 0) | https://jellyfish.co/resources/2025-state-of-engineering-management-report/ |
| Sample | 600+ engineering professionals |
| Step 4 (scope match) | ✓ Survey covers AI investment, ROI, measurement gap |
| Step 5 (exact location) | Jellyfish 2025, "The Measurement Gap" section |
| Step 6 (read section) | ✓ HAN source extract confirms verbatim: *"Only 20% use metrics to measure AI impact"*. The same section also says: *"61% increased engineering budgets in 2025"* and *"Gap between investment and measurable ROI persists"*. |
| Confidence tier | **SUPPORTED** — registry-verified, primary-source extract confirms |
| Article language | "only 20% of organisations using AI extensively could measure its impact" — see *Caveat* |

**Caveat**: The article's *"using AI extensively"* qualifier is slightly tighter than the Jellyfish source supports. The source says *"Only 20% use metrics to measure AI impact"* without restricting to "extensive" AI users. The article narrows the population implicitly.

The "extensively" qualifier in the article likely came from a memory of an earlier framing (possibly McKinsey's 2025 State of AI report, which segments by AI adoption maturity). The exact phrasing in Jellyfish does not include it.

**Recommended (if the article is ever revised)**: drop "extensively" — *"In Jellyfish's 2025 survey, only 20% of organisations could measure its impact."* Loses no rhetorical force, becomes exactly faithful to the source.

---

## Sources block (recommended if article is ever revised)

The article currently does not have inline links or a Sources block (it predates the convention adopted 2026-05-10). If revised, the recommended block:

```
Sources

Jellyfish. (2025). 2025 State of Engineering Management Report.
  https://jellyfish.co/resources/2025-state-of-engineering-management-report/
```

(Only one citation source in this article — Jellyfish — since the 90% claim and the 20% claim both trace to the same survey.)

---

## Local PDF library

No local PDF for Jellyfish 2025 in the HAN project. The HAN project has a primary-source text extract at `OneDrive - HAN/Research/Digital engineers/sources/jellyfish-2025-state-of-engineering-management.txt` which has been used for Step 6 verification above.

---

## Outstanding tasks

1. ~~Drop the "using AI extensively" qualifier from claim 2~~ ✅ Applied 2026-05-10. Article now reads *"only 20% of organisations could measure its impact"*, exactly matching Jellyfish's wording.
2. ~~Add inline link + Sources block~~ ✅ Applied 2026-05-10. Inline link on "Jellyfish's 2025 survey" + Sources block at the end of the article body.

Status: **VERIFIED retroactively. Both claims survive the checklist. Calibrations and references added. Article re-published 2026-05-10.**
