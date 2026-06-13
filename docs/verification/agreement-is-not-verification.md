# Verification record: *Agreement is not verification.*

**Article**: `src/pages/writing/agreement-is-not-verification.astro` (status: drafted to page 2026-06-13; not yet pushed; pending cross-model review pass + cover image)
**Article slug**: `agreement-is-not-verification`
**Last verified**: 2026-06-13 (pass 1, with source artefact)
**Method**: Anti-hallucination checklist (Step 0 + Steps 4 to 6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md), adapted for an own-work piece (N=1 personal practice + one external market claim). Confidence tiers map to article language per `docs/writing-guide.md` §7.

**Source artefact.** The article narrates a real research session whose full registry, plan, and reconciliation live at `C:/local_dev/new_hardware/`. Key files:

- `server-gpu/gpu-buy-research-plan.md`: the RQ set, frozen inputs, and two-workflow method.
- `server-gpu/research.md`: the "GPU sizing 3090 vs A6000 reconciliation" section (the spec-read that killed the 48GB plan) and the "Build / housing / sourcing finalized 2026-06-13" section (the €2,500 to €3,000 total).
- `vv/claim-registry.md` §S9 (card landscape, 35-card wide re-open, three-model verification) and §S10 (build/housing/sourcing, the DRAM-shortage price correction, the incomplete Copilot re-verify).
- `memory/gotcha-log.md` (2026-06-12 phantom ThinkPad P16s Gen 3 SKU; 2026-06-13 cross-repo "locked"-plan drift).
- Freelance grant artefact at `C:/local_dev/work-income/freelance/grants/nlnet-commons-fund-2026-resubmit/` (the A6000 "lock" in `claims.md` item 8 / `status.md`; the earlier RTX 4090 24GB budget line in `application.md`).

**Anonymisation rationale.** As with the sibling V&V-arc pieces, the body anonymises ("another working session", "a Dutch investment-deduction argument", "a specific laptop"). The argument is about the *pattern* (a self-consistent unverified plan reaching a decision), not about naming a grant, a vendor, or a product. The record below names sources for internal traceability while preserving the published anonymisation. Whose-story (writing-guide §5): every load-bearing element is the author's own work or his own prior AI-assisted session. No colleague's lived moment is used.

---

## Claim 1: The €8,000 / €4,500–5,500 "locked" plan (paragraphs 1, 3)

**Article wording**: "around €8,000, with the graphics card alone at €4,500 to €5,500 ... The word attached to it was 'locked.'" ... "a Dutch investment-deduction argument that genuinely does reward buying more in a given tax year."

| Check | Result |
|---|---|
| Trace | `work-income/freelance/grants/nlnet-commons-fund-2026-resubmit/claims.md` item 8 ("RTX A6000 48GB single-card locked (€4,500–5,500); hardware total ~€7,500–8,500") + `status.md` line 119 + `section-budget-draft-2026-05-27.md` ("RTX A6000 48GB single-card, ~€7,500–8,500"). KIA / investeringsaftrek mechanics in the same budget draft. Re-stated in `new_hardware/vv/claim-registry.md` §S9 intro + reconciliation. |
| Step 0 | Internal artefacts, present and read this session. |
| Step 4 (scope) | Article claims the plan *existed*, carried those figures, and was labelled "locked." All three are true of the artefact. The article does not claim the plan was a good idea. |
| Step 6 | Yes, read the budget draft + claims.md item 8 this session. |
| Confidence tier | **ESTABLISHED** (tier I, own artefact) for "such a plan existed with these figures and this label." |
| Article language | "around €8,000", "€4,500 to €5,500", "the word attached to it was 'locked'": attributional, matches. |

---

## Claim 2: 48GB unneeded — frozen oracle does inference, 27B at 4-bit ≈ 17GB, 24GB sufficient, earlier budget specced 24GB (paragraph 4)

**Article wording**: "The large model in this system runs as a frozen oracle: it does inference to generate training labels. It is never itself trained ... Running a 27-billion-parameter model for inference at 4-bit precision needs roughly 17GB. A 24GB card covers it ... an earlier version of the budget had specced a 24GB card."

| Check | Result |
|---|---|
| Trace | Oracle-is-inference: `work-income/.../application.md` ("replace the cloud oracle with a local open-weights teacher") + `claims.md` A-4 (the oracle baseline-comparison) + llm-distillery framing (student = Qwen2.5-1.5B+LoRA). VRAM math + 24GB-sufficiency: `new_hardware/vv/claim-registry.md` §S9 + S8-16 (gemma3:27b Q4 ~17GB peak) + reconciliation section. Earlier-budget-specced-24GB: `application.md` budget line "RTX 4090 24GB" (the grant version, before the A6000 upgrade). |
| Step 0 | Internal artefacts, present and read. |
| Step 4 (scope) | The "~17GB at 4-bit" figure is hedged "roughly"; matches the ~17GB Q4 peak in S8-16. The "frozen oracle / never itself trained" characterisation matches the distillation design (big model labels; small model trains). The "earlier budget specced 24GB" matches the application's RTX 4090 24GB line. |
| Step 6 | Yes. |
| Confidence tier | **ESTABLISHED** (tier I/D) for the oracle-is-inference structure and the earlier-24GB-budget fact; **SUPPORTED** for the "roughly 17GB" figure (hedged, model/quant-dependent). |
| Article language | "runs as a frozen oracle", "roughly 17GB", "covers it with room to spare": appropriately hedged where the number is approximate. |

---

## Claim 3: The phantom laptop SKU — composite of three machines, surfaced by a second and third engine (paragraph 5)

**Article wording**: "a specific laptop ... The machine did not exist ... a composite, real parts from three different laptops fused into one model number that no shop had ever sold ... asking a second and a third engine the same narrow question independently, and watching them fail to confirm."

| Check | Result |
|---|---|
| Trace | `new_hardware/memory/gotcha-log.md` entry 2026-06-12: "ThinkPad P16s Gen 3 (AMD)" failed at the *model* level (PSREF shows P16s AMD skipped Gen 3; the Ryzen 7 PRO 8840HS shipped in other chassis; the €1200/64GB/2.5K combo matched no SKU). Cross-engine refutation: "3 Claude agents + Copilot CLI + Gemini CLI, 2026-06-12 independently refuted it." |
| Step 0 | Internal artefact, read. |
| Step 4 (scope) | "Composite, real parts from three different laptops" matches the gotcha's "a real CPU, a real chassis line, a real price point, but from different machines." "Second and third engine ... fail to confirm" matches the Copilot + Gemini cross-engine refutation. |
| Step 6 | Yes. |
| Confidence tier | **ESTABLISHED** (tier I, own gotcha record). |
| Article language | "did not exist", "a composite", "fail to confirm": matches. |

---

## Claim 4: Three-model check; one card confirmed by only a single outside model because the other hit a usage limit (paragraph 6)

**Article wording**: "two others, different families ... were each handed the same narrow questions: does this card exist, is this price plausible ... One card in the set came back confirmed by only a single outside model, because the other hit a usage limit mid-run."

| Check | Result |
|---|---|
| Trace | `new_hardware/vv/claim-registry.md` §S9-4 (Intel Arc Pro B70: "cross-verification was single-source — Copilot quota-blocked; only Gemini confirmed") and §S10-9 (the re-verify also failed: "Copilot hard quota-blocked, HTTP 402, monthly cap"). Method = Claude primary + Gemini CLI + Copilot CLI, per `gpu-buy-research-plan.md`. |
| Step 0 | Internal artefact, read; CLI invocations (`gemini --skip-trust -p`, `copilot -p --allow-all-tools`) tested live this session. |
| Step 4 (scope) | "Different families, different failure modes" matches Claude/Gemini/Copilot. "One card ... single outside model ... usage limit" matches the B70 + Copilot 402 quota block exactly. |
| Step 6 | Yes. |
| Confidence tier | **ESTABLISHED** (tier I). |
| Article language | "came back confirmed by only a single outside model", "a check you did not actually complete is not a check": matches and is honest about the gap. |

---

## Claim 5: 35-card wide re-open confirmed the cheap pick; one genuinely new alternative (paragraph 7)

**Article wording**: "thirty-five cards, new and used, consumer and datacenter and even the odd memory-modified import. The sweep did not overturn the cheap option. It confirmed it. A used 24GB card was the only strong single-card fit at a sensible price, and the search surfaced exactly one genuinely new alternative."

| Check | Result |
|---|---|
| Trace | `new_hardware/vv/claim-registry.md` §S9-2 ("35-card wide re-open ... only two cards scored 5/5 ... the 3090 is the only fit-5 card at a sane price") + landscape list (35 unique, incl. Tesla P40/V100 datacenter + China-modded 4090 48GB + modded 2080Ti 22GB). The "one genuinely new alternative" = Intel Arc Pro B70 32GB (§S9-4). |
| Step 0 | Internal artefact, read; landscape count of 35 confirmed in the workflow result. |
| Step 4 (scope) | "Thirty-five cards" = exact (35 unique). "Datacenter and ... memory-modified import" matches Tesla/V100 + China-modded entries. "Only strong single-card fit at a sensible price" matches §S9-2 (the RTX 5000 Ada also scored 5/5 but at ~5x price). "Exactly one genuinely new alternative" = the B70. |
| Step 6 | Yes. |
| Confidence tier | **ESTABLISHED** (tier I) for the count + the confirm-not-overturn outcome. |
| Article language | "thirty-five cards", "the only strong single-card fit at a sensible price", "exactly one genuinely new alternative": matches. |

---

## Claim 6: "verification is a workflow problem" back-reference (paragraph 8)

**Article wording**: inline link "[verification is a workflow problem](/writing/verification-is-a-workflow-problem/) rather than a model problem."

| Check | Result |
|---|---|
| Step 0 (link resolves) | Internal site route. Target file `src/pages/writing/verification-is-a-workflow-problem.astro` exists (published 2026-06-01, registered in `writing.ts`). Resolves within the site build. |
| Step 4 (scope) | The prior article's thesis is exactly "verification is a workflow problem, not a model problem." The back-reference is accurate. |
| Confidence tier | **ESTABLISHED** (own published article). |
| Note | This is the only link in the article body. No external URLs are embedded, which keeps link-rot risk near zero (cf. gotcha-log 2026-06-05 on 404'd primary-source links). |

---

## Claim 7: Total build ~€2,500–3,000; the gap is a memory-chip shortage, not the card (paragraph 9)

**Article wording**: "roughly €2,500 to €3,000, and almost all of the gap between that and a cheaper figure I would have quoted a year ago is a memory-chip shortage, not the card."

| Check | Result |
|---|---|
| Trace | Total: `new_hardware/vv/claim-registry.md` §S10-8 (~€2,500–3,000 sensible build / ~€2,300–2,500 value path, vs €2,040 baseline). Shortage attribution: §S10-1 (64GB DDR5 €200 → ~€600–750) + §S10-2 (NVMe NAND spike), sourced to Tom's Hardware / TrendForce / wccftech (tier D, external). GPU itself still €700–950 (§S9-1, §S10-8). |
| Step 0 | Total + GPU price: internal artefact, read. DRAM-shortage external sources: cited in §S10 but **not** Step-0 live-resolved this session (future-dated 2026 trade-press URLs from the research workflow). The article makes the claim only at the general level ("a memory-chip shortage"), with no embedded external link, so no live URL is shipped. |
| Step 4 (scope) | "Roughly €2,500 to €3,000" matches §S10-8's sensible-build band. "Almost all of the gap is a memory-chip shortage" matches §S10's finding that RAM (+~€450) and NVMe (+~€120) drove the rise while the GPU was unchanged. |
| Step 6 | Yes (internal); the external DRAM coverage is read via the §S10 summaries, not re-fetched at primary source this session. |
| Confidence tier | **SUPPORTED** for the €2,500–3,000 total (volatile, spike-driven, hedged "roughly"); **ESTABLISHED** that a 2026 memory shortage (not the GPU) drove the increase. |
| Article language | "roughly €2,500 to €3,000", "a memory-chip shortage, not the card": hedged on the number, confident on the attribution. Matches the tiers. |

---

## Pre-push gates (writing-guide §9 + adding-an-article step 11)

- [x] **Cross-model review pass** — run 2026-06-13 via **Gemini CLI** (different vendor, no project context), `review-prompt.md` Variant B, voice rules supplied as the filter. **Score 4.6/5, "submission-ready for a personal blog."** Dispositions: applied the one substantive fix ("nobody's actual workload" → "the actual workload", an N=1-scope tightening per writing-guide §7); rejected the voice/scope suggestions (globalize "Dutch investment-deduction", add a bridging sentence, add "allowing for overhead") as either already-handled or against §6. Accepted and woven in (2026-06-13): the "different model family" line now carries the caveat that cross-family models are only partly independent ("models trained on overlapping slices of the same internet can share a blind spot, so two of them agreeing is weaker than it looks"), which also reinforces the essay's thesis. No label/subhead drift to filter (clean cross-vendor pass).
- [x] **LinkedIn cross-post** — intentionally skipped per author (2026-06-13): site-only, no Pulse/feed cross-post for this article. No `memory/posted-linkedin/` record needed.
- [x] **Verification record present** — this file.
- [x] **No external URLs in body** — only one internal site link; GitHub-visibility gate N/A.
- [ ] **Cover image** — `public/social/agreement-is-not-verification.png` not yet generated (`scripts/gen-social-image.py` with headline + slug constants).
- [x] **Em-dash scan** — body confirmed clean (0 em-dashes).
- [ ] **Delete `drafts/agreement-is-not-verification.md`** once the article is live.

## Optional Sources block

If a Sources block is wanted (the body currently has none, matching the anonymised-pattern default of `verification-is-a-workflow-problem`), the one external claim worth backing is the DRAM shortage. Candidate entry, **Step 0 to confirm the URL resolves before adding**:

> Tom's Hardware / TrendForce 2026 DRAM-shortage coverage (basis for "a memory-chip shortage").

Default recommendation: keep the body link-light; this record is the traceability layer.
