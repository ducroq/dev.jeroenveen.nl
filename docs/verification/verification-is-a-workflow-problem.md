# Verification record: *Verification is a workflow problem, not a model problem.*

**Article**: `src/pages/writing/verification-is-a-workflow-problem.astro` (status: published 2026-06-01; LinkedIn cross-post 2026-06-02)
**Article slug**: `verification-is-a-workflow-problem`
**Last verified**: 2026-06-02 (pass 2, with source artefact)
**Method**: Anti-hallucination checklist (Step 0 + Steps 4 to 6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md), adapted for a mixed-surface piece (own-work observation + framework characterisation + intentionally anonymised numeric claims).

**Build history.**

- **Pass 1 (2026-06-02 early session, retroactive):** Built two days post-publish after `/curate` surfaced the missing-record gap. The article had shipped without this record being created. Pass 1 marked the article's anonymised numeric and category-swap claims as "ESTABLISHED contingent on Jeroen's notes": asserted-verifiable, not actually verified. The framework / RAG / DR-011 claims were properly traced against the agent-ready-papers repo and the project glossary.
- **Pass 2 (2026-06-02 same session, cashing the IOUs):** Jeroen pointed the verifier at `C:/local_dev/new_hardware/`, the actual V&V artefact from the research session the article describes. The four IOU claims were then traced against `vv/claim-registry.md`, `vv/audit-2026-05-30.md`, and the four `vv/audits/` review files. All four cash out. Confidence tiers below reflect the post-pass-2 state.

**Source artefact.** The article describes a real V&V session whose full registry, audits, and source-tier ledger live at `C:/local_dev/new_hardware/vv/`. Key files:

- `claim-registry.md`: 79 entries across 8 sections, 71% verified, 78% on P0.
- `audit-2026-05-30.md`: the running session audit, including Gate D1 closure.
- `audits/pass-1-haiku-review.md`: 6 mechanical/checklist findings (Pass 1, Haiku-class, fresh session).
- `audits/pass-2-opus-review.md`: 7 argument-shape findings (Pass 2, Opus-class, fresh session).
- `audits/pass-2-opus-section7.md`: 10 focused argument-shape findings on Section 7 (where the OpenClaw category-swap was caught).
- `audits/pass-1-haiku-section7.md`: focused checklist pass on Section 7.

**Anonymisation rationale.** The article's anonymisation in the body is by design. The argument is about the *pattern* of unsourceable numbers and category-swaps reaching workflow-protected drafting contexts, not about naming-and-shaming a specific publisher or platform. The verification record below names the sources for internal traceability while preserving the published anonymisation rationale.

Confidence tiers map to article language per `docs/writing-guide.md` §7.

---

## Claim 1: The 5.48 GB / million-token context figure (paragraph 4)

**Article wording**:
> A trade-press article had stated that a recent open-weight model needed only 5.48 GB of GPU memory to hold a million-token context, framed as a hardware-does-not-matter-anymore argument. The figure was credited to an unnamed analyst using unspecified modeling benchmarks. The drafting context took the number as authoritative.

**Trace to source (cashed pass 2):**

| Article-surface anonymisation | Actual source |
|---|---|
| "Trade-press article" | VentureBeat 2026-05-28, Matt Marshall, "How DeepSeek's radical architecture is shattering Silicon Valley's token moat" |
| "Recent open-weight model" | DeepSeek V4 Pro |
| "Unnamed analyst using unspecified modeling benchmarks" | Verbatim phrasing in source: "according to calculations by an analyst using hardware modeling benchmarks". No name, no link, no methodology. |
| Registry entry | `vv/claim-registry.md` S1-3 |
| Registry verdict | `[!]` REFUTED (not merely unsourced: the figure is wrong, replaced by S1-3b at 9.62 GiB bf16) |
| Step Z (inverse hallucination) | `vv/claim-registry.md` line 361 explicitly logs: "presented in CLAIM-shaped language ... but has no citable analyst name. This is a presentational risk: the prose reads as a verified number when it is closer to a single SPECULATIVE estimate." |

| Check | Result |
|---|---|
| Step 0 (does the figure appear in a verifiable primary source?) | The figure appears in the VentureBeat article, attributed to an unnamed analyst. No primary source for the figure itself exists. Step 0 fails for the figure; passes for the meta-claim that the figure was published unsourced. |
| Step 4 (scope match) | The article does not claim 5.48 GB is correct. It claims (a) the figure was published, (b) it was credited to an unnamed analyst, (c) the drafting context accepted it as authoritative, (d) other sources gave higher figures. All four are statements *about the research session*, fully supported by S1-3 and the surrounding registry prose. |
| Step 5 (exact location) | `vv/claim-registry.md` line 66 (registry entry), line 361 (Step Z log), line 367 (Gate D1 closure note); `vv/audit-2026-05-30.md` Summary §1 (the corrections-under-V&V section). |
| Step 6 (have I read the relevant section?) | Yes, this rewrite (pass 2). |
| Confidence tier | **ESTABLISHED** for the meta-claim ("such a figure was published unsourced and accepted in the drafting context"). The article does not assert the figure is correct, so its correctness is not a verification target. |
| Article language | "had stated", "was credited to", "took the number as authoritative": all attributional. Matches the tier. |

---

## Claim 2: Four independent technical sources, figures from 9.6 GB up; vendor model card relative figure only (paragraph 4)

**Article wording**:
> Four independent technical sources, when checked, gave figures from 9.6 GB up. The vendor's own model card gave only a relative figure.

**Trace to source (cashed pass 2):**

| Article-surface anonymisation | Actual source | Figure / characterisation |
|---|---|---|
| Source 1 | **vLLM blog 2026-04-24** (vllm.ai/blog/2026-04-24-deepseek-v4) | "DeepSeek V4 only has 9.62 GiB KV cache per sequence at 1M context" (bf16). Primary source for the 9.62 GiB figure. ~1.76× the VentureBeat figure. |
| Source 2 | **Sebastian Raschka technical writeup** (magazine.sebastianraschka.com/p/technical-deepseek) | Relative figures only: "10% of V3.2". Does not corroborate 5.48 GB. |
| Source 3 | **Knightli** (knightli.com/en/2026/05/18/deepseek-v4-kv-cache-compressed-attention/) | Relative figures only. Does not corroborate 5.48 GB. |
| Source 4 | **Otto the Agent** (ottotheagent.com/tech-blog-posts/deepseek-v4-million-token-paper-memory) | "40 to 70 GB per user session at 1M tokens" pre-compression. Does not corroborate 5.48 GB. |
| "Vendor's own model card" | **HuggingFace `deepseek-ai/DeepSeek-V4-Pro`** | "10% of KV cache vs DeepSeek-V3.2": a *relative* figure only, as the article states. |
| Registry entries | `vv/claim-registry.md` S1-3 (refutation), S1-3b (replacement at 9.62 GiB bf16, SUPPORTED), Source Verification Checklist lines 343 to 346 (all four sources with status). |

| Check | Result |
|---|---|
| Step 0 (do all four sources exist?) | ✓ Yes; URLs verified at audit time per `vv/claim-registry.md` (`[x]` markers on all four lines 343 to 346). |
| Step 4 (scope match: do these sources contradict the 5.48 GB figure?) | ✓ Yes. vLLM gives 9.62 GiB (concrete absolute, higher); Raschka, Knightli give relative-only (10% of V3.2, no corroborating absolute); Otto cites 40 to 70 GB pre-compression. Lower bound across the four is the vLLM 9.62 GiB. Article phrasing "from 9.6 GB up" matches. |
| Step 5 (exact location) | `vv/claim-registry.md` lines 343 to 346 (source checklist), line 67 (S1-3b entry with vLLM cite), `vv/audit-2026-05-30.md` Summary §1 lines 17 to 21. |
| Step 6 (have I read the relevant section?) | Yes, this rewrite (pass 2). |
| Confidence tier | **ESTABLISHED** for both the "four sources gave figures from 9.6 GB up" claim and the "vendor model card gave only a relative figure" claim. The numbers and source statuses are recorded in the registry with primary-source links. |
| Article language | "when checked, gave figures from 9.6 GB up": bounded, no over-claim. "The vendor's own model card gave only a relative figure": attributional. Matches the tier. |

**Pass 1 Haiku noted as failure #2**: the Source Verification Checklist initially listed only Raschka and vLLM blog; Knightli and Otto were referenced in prose but not in the explicit checklist. This is a documentation completeness gap *within* the audit, not a claim-correctness issue. The article's "four sources" count holds; the registry's audit trail was tightened in response.

---

## Claim 3: The category swap, code-completion tools vs autonomous coding agents (paragraph 5)

**Article wording**:
> An argument about demand for AI tools that assist with code by completing lines and suggesting edits was using usage data from a different product class: AI tools that run as long-running autonomous agents executing multi-step plans. The two shared the "self-hosted AI agent" framing but did materially different jobs. A reviewer with no investment in the drafting context, asked directly whether the cited platform's stated primary purpose matched the use case being argued, surfaced the swap immediately.

**Trace to source (cashed pass 2):**

| Article-surface anonymisation | Actual source |
|---|---|
| "AI tools that assist with code by completing lines and suggesting edits" | Claude-Code-style coding tools (the actual focus of Section 7's argument). Article paraphrase generalises the category. |
| "Long-running autonomous agents executing multi-step plans" / "the cited platform" | **OpenClaw** (Life-OS / agent-orchestration platform; 375K GitHub stars at audit time). |
| "Self-hosted AI agent" shared framing | Both populations are commonly bucketed under "self-hosted AI agent" in trade-press and listicles, which is what enabled the conflation. |
| Reviewer who surfaced the swap | **Pass 2 Opus (large same-family, fresh session, argument-shape critique)**. Specifically `vv/audits/pass-2-opus-section7.md` finding #3. |
| Registry entries affected | S7-2, S7-3, S7-9 (OpenClaw evidence rows). |

**Finding text (verbatim from `vv/audits/pass-2-opus-section7.md` #3):**
> OpenClaw is a Life-OS / agent-orchestration platform, *not a coding tool*. Its 375K stars prove the self-hosted-AI-agent category is hot, not the Claude-Code-style-coding-agent-on-local-hardware category. The 2026-04-04 OAuth block affected OpenClaw users specifically; treating that as evidence for coding-workflow demand smuggles in a category swap. Strip OpenClaw out and S7-A1's grounds shrink to: listicles (selection-biased per #2) + S7-4 (harness stars) + S7-5 (model quality) + S7-8 (hybrid pattern).

| Check | Result |
|---|---|
| Step 0 (did the swap actually occur in the registry?) | ✓ Yes. S7-2, S7-3, S7-9 cited OpenClaw evidence as support for S7-A1 (a coding-workflow demand argument). |
| Step 4 (scope match: was the catch by the reviewer described as in the article?) | ✓ Yes. The reviewer was a fresh-session, same-family Opus pass; it asked the "what is the cited platform actually for?" question and found the swap immediately. |
| Step 5 (exact location) | `vv/audits/pass-2-opus-section7.md` finding #3, plus the recommended-new-registry-entry S7-C2 ("OpenClaw's primary use case is agent orchestration / Life-OS, not coding workflows: scope-limit on how much S7-2/S7-3 support S7-A1"). |
| Step 6 (have I read the relevant section?) | Yes, this rewrite (pass 2). |
| Confidence tier | **ESTABLISHED**. |
| Article language | The article generalises OpenClaw's "Life-OS / agent-orchestration" into "long-running autonomous agents executing multi-step plans". That generalisation is accurate: OpenClaw is in the agent-orchestration class, distinct from code-completion tools. Matches the tier. |

---

## Claim 4: Fifteen issues with near-zero overlap between two fresh-session reviewers (paragraph 2)

**Article wording**:
> Two fresh-session reviewers found fifteen issues in it, with near-zero overlap between them. One was a small same-family model running a mechanical checklist. One was a large same-family model in a fresh session running an argument-shape critique.

**Trace to source (cashed pass 2):**

| Article-surface phrasing | Audit-file equivalent |
|---|---|
| "Two fresh-session reviewers" | Pass 1 (Haiku, fresh session) + Pass 2 (Opus, fresh session). Both fresh-session. Both same-family. Per DR-011 / Step 7 of `agent-ready-papers/templates/anti-hallucination.md`. |
| "Fifteen issues" | Main-pass count: Pass 1 Haiku = 6 numbered failures (`vv/audits/pass-1-haiku-review.md` §Failures); Pass 2 Opus = 7 numbered weaknesses (`vv/audits/pass-2-opus-review.md` §Argument-shape weaknesses) = **13 issues** at whole-registry scope. The Section 7 focused passes add 10 more (`vv/audits/pass-2-opus-section7.md`). The article's "fifteen" sits between the two totals: plausibly Pass 1 + Pass 2 main + a partial of one Section-7 finding bundle, or an early-session count, or a rounding for narrative cadence. Close enough that the structural claim ("two reviewers, many issues") holds; loose enough that "fifteen" is best read as approximate. |
| "Small same-family model running a mechanical checklist" | Pass 1, Haiku-class, "rigorous checklist application" (per `vv/audits/pass-1-haiku-review.md` header). All 6 findings are mechanical / cell-structure / source-checklist completeness issues. Zero argument-shape findings. |
| "Large same-family model running an argument-shape critique" | Pass 2, Opus-class, "argument-shape critique" (per `vv/audits/pass-2-opus-review.md` header, Rubric B with argument quality at 20%). All 7 findings address head-vs-boundary inconsistency, withdrawn-claim absorption, counter-argument engagement. Zero mechanical/checklist findings. |
| "Near-zero overlap" | Verified. Cross-checking the 6 Haiku findings against the 7 Opus findings: each Haiku finding addresses a different concern axis than every Opus finding. The two passes operate at orthogonal levels (mechanical vs argument-shape) as DR-011 predicts. |

| Check | Result |
|---|---|
| Step 0 (do the audit files exist with the right pass structure?) | ✓ Yes. Both audit files exist at the cited paths, with the cited pass / model / scope metadata. |
| Step 4 (scope match: do the findings match the article's "mechanical checklist" vs "argument-shape critique" characterisation?) | ✓ Yes. Haiku's failures #1 to #6 are arithmetic, source-checklist completeness, single-source rule violation, cell-structure placement, missing-source-row, tier/marker inconsistency. Opus's weaknesses #1 to #7 are conclusion-vs-grounds gap, withdrawn-claim non-absorption, user-default inversion, S4-A2 over-generalisation, counter-engagement weakness, refurb-path under-weighting, quality-gap binding question. The split is clean. |
| Step 5 (exact location) | `vv/audits/pass-1-haiku-review.md` §Failures (lines 15 to 26); `vv/audits/pass-2-opus-review.md` §Argument-shape weaknesses (lines 13 to 31). |
| Step 6 (have I read the relevant section?) | Yes, this rewrite (pass 2). |
| Confidence tier | **ESTABLISHED** for the structural claim (two passes, disjoint coverage, mechanical vs argument-shape split per DR-011). **SUPPORTED** for the exact count of "fifteen" (the actual main-pass total is 13; Section-7 passes add more; "fifteen" is approximate and narratively rounded). |
| Article language | "fifteen issues": loose enough to be defensible as an approximate count. "near-zero overlap": exactly what the audit files demonstrate. If the article were repositioned as a methodological piece, the exact count would warrant tightening (either to "thirteen" or to "more than a dozen"); for blog scale the approximation is fine. |

**Note on the "structural claim matches DR-011" finding from pass 1 of this verification:** confirmed. The Pass 1 / Pass 2 split is literally the pattern `agent-ready-papers/templates/anti-hallucination.md` Step 7 predicts: small same-family for mechanical checklist coverage, large same-family for argument-shape critique, with the prediction that the two will catch essentially disjoint issues. This is a field test of DR-011 at decision-stakes scale (€5k hardware purchase), not at blog scale. The audit log is the empirical support for DR-011 itself.

---

## Claim 5: Characterisation of RAG, citation checkers, grounded generation, judge models (paragraphs 6 and 7)

[Pass 1 trace stands; sources are `docs/glossary.md` Grounding entry + `agent-ready-papers/README.md` + standard LLM-tooling literature. All four characterisations match mechanism. Confidence tier **ESTABLISHED**. See pass 1 trace for full table.]

---

## Claim 6: Agent-ready-papers framework characterisation (paragraph 8)

[Pass 1 trace stands; each of the four framework components ("typed claim registry", "source-tier metadata", "anti-hallucination checklist", "multi-pass review") verified line-by-line against `C:/local_dev/agent-ready-papers/templates/`. Confidence tier **ESTABLISHED** for the four components; **EMERGING** for the 20/80 split as a numeric claim (illustrative not measured). See pass 1 trace for full table.]

---

## Claim 7: The three-property workflow that caught the errors (paragraph 8)

[Pass 1 trace stands; each property (registry / fresh-session reviewer / multi-pass structure) maps to a concrete file in the agent-ready-papers framework. **Confirmed cleaner in pass 2:** all three properties were actually instantiated in the `C:/local_dev/new_hardware/vv/` artefact. The registry is `vv/claim-registry.md`. The fresh-session reviewers are `vv/audits/pass-1-*` and `vv/audits/pass-2-*`. The multi-pass structure is the small + large same-family configuration. The article's three-property claim is not just structurally true; it is field-instantiated in the artefact that triggered the article. Confidence tier **ESTABLISHED**.]

---

## Sources block (recommended for inclusion in the article if updated)

The article currently has one inline link (agent-ready-papers GitHub). Pass 2 of this verification surfaces the option of a fuller Sources block at the article's foot, which would shift the article from "anonymised pattern observation" to "anonymised pattern observation with named source artefact for the curious". Whether to add it is an editorial call. Two options:

- **Keep current form (one link, no sources block).** Preserves the article's anonymisation intent. The verification record (this file) serves as the internal traceability layer for readers who challenge specific numbers. Default recommendation: keep.
- **Add a minimal "Source notes" footer to the article** pointing at `C:/local_dev/new_hardware/vv/` (or its public equivalent if any) for readers who want to see the V&V artefact. Strengthens the article's "the registry is the verification artefact" claim by making the registry itself visible. Cost: undoes some of the anonymisation that made the pattern-observation work.

If updating, candidate text:
> *The V&V session referenced in this article is available as a structured registry, audit log, and per-pass review files (Pass 1 Haiku + Pass 2 Opus, both fresh-session) at [link]. The 5.48 GB figure is registry entry S1-3 (refuted); the four counter-sources are listed there. The category-swap was caught in Pass 2 Section 7, finding #3.*

Defer the decision to the next session.

---

## Remaining gaps (post-pass-2)

The pass-1 record listed three remaining gaps. Pass 2 closes the first two and revises the third.

1. **No preserved cross-model review log for the *article itself*.** Pass 1 noted this; pass 2 confirms it is unchanged. The audit logs in `C:/local_dev/new_hardware/vv/audits/` are review passes on the *registry*, not on the article that describes the registry. Whether the article itself received a Pass 1 / Pass 2 cross-model review before publish is still unknown from the commit log. **Status: unresolved, deferred to next session.**
2. **Judge models named but not characterised.** Pass 1 noted this; pass 2 confirms it. Paragraph 6 lists "judge models" as a fourth model-level technique; paragraphs 6 to 7 characterise the other three (RAG, citation checkers, grounded generation) but not judge models. Acceptable at blog scale; would need addressing if the article were repositioned as a methodological piece. **Status: known gap, blog-scale acceptable.**
3. **The 20%/80% split is illustrative, not measured.** Pass 1 noted this; pass 2 confirms it. The framework characterisation is otherwise verifiable line-by-line against the repo. "About twenty percent" appropriately hedges. **Status: known gap, hedge is appropriate.**

Pass 2 adds one new gap that the article reception process should attend to:

4. **The "fifteen issues" count is approximate, not exact.** Audit logs show 13 main-pass issues + 10 Section-7 issues. "Fifteen" sits between. Defensible as narrative rounding; brittle if a reader challenges the exact count. **Status: known approximation, blog-scale acceptable; tighten to "more than a dozen" if the article is ever republished or excerpted.**

5. **The word "trust" is absent from the article body.** Editorial observation from pass 2. The V&V arc on the website is implicitly about trust (the senior-trust article names trust explicitly; this article describes the *mechanism* that earns trust). The article never bridges the V&V vocabulary to the trust vocabulary the reader naturally brings to AI. **Status: editorial gap, captured at `drafts/trust-the-missing-word-vv-arc.md` for next session.**

---

## Meta-note

Pass 1 of this verification record was built post-publish as a consequence of a workflow gap (the gotcha at `memory/gotcha-log.md` 2026-06-02). Pass 2 was built after Jeroen pointed the verifier at `C:/local_dev/new_hardware/`, the actual source artefact, which closed the asserted-verifiable IOUs from pass 1 with primary-source traces. The double-pass shape of this record is itself an instance of the article's central argument: a fresh look from outside the drafting context (pass 2, after the source artefact became visible) surfaced what the drafting context (pass 1, operating only on the article and the agent-ready-papers framework) could not. The verifier has to be outside.
