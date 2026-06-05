# Plausibility passes the AI review. Correctness does not.

*Working subtitle:* Notes on a 68-equation case and what it shows about the kit.

*Status: DRAFT first-pass prose, written 2026-06-05 by cannibalising the case-study material from `two-reviews-missed-what-reproduction-caught.md` (drafted 2026-05-19) and reframing through the standalone seed (captured 2026-05-12). Continues from `verification-is-a-workflow-problem` (published 2026-06-01), which named agent-ready-papers and listed its tools at one remove; this piece walks through one of those tools, the empirical anchor for it, and why the kit has more than one. Replaces `two-reviews-missed` as the planned V&V arc post 3, since both pieces share the empirical anchor and this framing makes the framework's strengths visible rather than narrating one slice as a finding.*

*Working slug:* `ai-review-is-plausibility-review`

---

## Draft

In a 68-equation theory document, two AI reviews in assessment mode caught zero errors. A third pass with the same model family but a reproduction instruction caught three.

Some context. A theory document I had been working on for several months. Ten chapters, AI-assisted throughout, covering pendulum mechanics, synchronisation, electromagnetism, control, power analysis, and the error budget. Hardware was about to be built on top of it. I needed to know whether the equations were right.

I ran two LLM reviews in the usual assessment mode. Read this, check it for physical soundness, flag anything that looks wrong. One pass used Gemini, one used Claude. Both came back the same. No errors found. Dimensions checked out, magnitudes were in plausible ranges, the prose was internally consistent.

Then I ran a third pass with a different instruction. Same family as the Claude pass, but the prompt forced reproduction rather than judgment. Substitute the stated input values into every equation. Compute the result step by step. Compare against the value in the document. Never skip a calculation, never paraphrase a table.

That pass caught three errors.

The first was a label mismatch. A table headed "5 degrees" contained values that had been computed at 1 degree. Coupling estimates in the relevant chapter were therefore five times more optimistic than the design called for. The second was a formula error in a dwell-time calculation: a missing variable and a spurious factor of two made the tabulated values roughly seven times too small. The third was an internal inconsistency. An hourly correction stated as 36 s/hr did not survive the arithmetic. 3.3 ms per swing, times 3,600 swings per hour, lands near 12 s/hr, not 36. The text said one thing, the underlying numbers said another.

All three errors produced individually plausible numbers. Right units, reasonable magnitudes, coherent with the surrounding prose. An assessment-mode reviewer is checking whether the artifact looks right. These errors looked right. AI review is plausibility review unless you make it not be.

Reproduction strips out the degree of freedom plausibility lives in. A calculator does not have an opinion about whether 3.3 times 3,600 equals 36 seconds per hour. The instruction to compute rather than to judge removes the move where "this reads as reasonable" gets to substitute for "this is correct." Same model. Different mode. Different result. The pattern lives in <a href="https://github.com/ducroq/agent-ready-papers" target="_blank" rel="noopener">agent-ready-papers</a> as the equation-checker template, and the decision record behind it is DR-009 (calculation-verification). The 68-equation case is the empirical anchor for both. The controlled variable was the mode of instruction; readers who want the full prompt-counterfactual will find it in the audit doc.

The mechanism is not arithmetic-specific. Assessment checks the surface the artifact presents. Reproduction operates on a surface the artifact cannot fake. Citations are plausibility-shaped too. An invented DOI looks like a real DOI, an invented author looks like a real author, a paraphrased abstract looks like an abstract. An LLM asked "does this citation support the claim" can answer fluently and confidently while the citation does not exist. The anti-hallucination checklist in the same framework is the citation-equivalent of the equation-checker. It forces a check that the source exists and says what the prose says it says, rather than a judgment about whether the citation reads plausible.

Citations have an external registry to check against; code does not, and the same shape still recurs. Functions that compile, pass their tests, and solve the wrong problem are plausibility-passing. A reviewer running the tests reads the output as evidence of correctness, but when the same head writes test and implementation, the test inherits the implementer's frame. The check that escapes the loop is reproduction in the runtime sense: run the function against a case the implementer did not write the test for, ideally generated by a different head.

Each instance of the pattern is the same. The artifact reads as right. The reviewer accepts what reads as right. The escape is a different kind of check, not a sharper version of the same judgment but a check that operates on a different surface from the artifact itself.

Structural problems take a set of tools, not one. Calculation-verification handles equations. The anti-hallucination checklist handles citations. The other parts of the kit fill in failures that neither of those catches alone. The shape is not "more tools is better". It is that no single check escapes a structural failure mode.

This set of tools costs real time, and not every artifact warrants it. A personal scratch script does not need a claim registry. The framework starts earning its keep where the cost of being wrong exceeds the cost of running the verification. A theory document with hardware about to be built on top of it crosses that threshold. A €5k research exercise crosses it. A blog post about a topic the reader will quote at you publicly crosses it. So does a production deployment whose failure mode is being wrong, quietly, for months. A weekend prototype probably does not. The pattern that names the equation-specific move is on the <a href="https://augmented-engineering.eu/patterns/reproduce-dont-assess" target="_blank" rel="noopener">augmented engineering site</a>; this piece is the evidence-anchor for why that pattern, and the others alongside it, have to exist.

Which of your current review steps would survive being reframed as reproduction rather than assessment?

---

## Notes for the review pass

**Word count (body, excluding title and subtitle):** ~885 after the 2026-06-05 review-battery fixes. Within the 800–1,500 target band per writing-guide §3, on the short end. Acceptable for a single-conviction piece.

**Arc-position audit.** *Resolved 2026-06-05.* Post 2's forward-look promised the asymmetry-of-validation-evidence frame between software and non-software domains. This rewrite softens that closure in favour of framework-showcase. Jeroen accepted the trade-off because current work is mostly software, research, and writing, and the asymmetry-frame closure depends on hardware-side evidence that isn't currently fresh. The asymmetry-frame closure is deferred, not abandoned. `two-reviews-missed-what-reproduction-caught.md` is superseded as the post-3 slot but retained as alternate pending full retirement decision. See `memory/project_vv_arc_closer.md` (2026-06-05 reframe section) and `memory/feedback_multi_pass_review_frame.md`.

**Source-material accuracy check.** The reproduction pass was LLM-driven (Claude Sonnet with a structured "substitute, compute, compare" prompt), not manual. The audit document (`agent-ready-papers/audits/driven-pendulum-retrofit.md` §9.1) and the AE pattern page (`augmented-engineering/site/src/pages/patterns/reproduce-dont-assess.astro`) both align on this. The draft uses the LLM-reproduction framing because (a) it matches the canonical AE pattern doc, (b) it is more honest, and (c) it makes a stronger point: same model family, different mode, different result.

**Named-colleague rule (writing-guide §5).** No named colleagues in the body.

**Em-dash audit.** None in the body. Used colons, commas, periods, parentheses, and sentence breaks. Re-scan during review.

**Cover image / in-article figure.** Recommend *no* in-article figure. The natural candidate ("assessment mode → 0 / reproduction mode → 3" as a diagram) lands in the BEFORE/AFTER cliché the visual-register rule explicitly warns against. Typographic social-image cover generated 2026-06-05 via `scripts/gen-social-image.py` (three-line title split with the third line in amber: "Plausibility passes" / "the AI review." / "Correctness does not."). Output: `public/social/ai-review-is-plausibility-review.png` (29 KB).

**Sources block content to embed in the `.astro` file.** Two publicly linkable sources:
- agent-ready-papers framework page (`github.com/ducroq/agent-ready-papers`)
- AE pattern page for Reproduce-Don't-Assess (`augmented-engineering.eu/patterns/reproduce-dont-assess`)

The audit doc in `agent-ready-papers/audits/` is the primary source for the three specific errors. Check whether the audits directory is publicly browsable before publish; if yes, link directly to `audits/driven-pendulum-retrofit.md` §9.1 from the Sources block.

**Verification record.** Built 2026-06-05 at `docs/verification/ai-review-is-plausibility-review.md` (moderate-formality calibration per `feedback_polish_loop_calibration.md`). Seven claims traced. Five ESTABLISHED, two ESTABLISHED-pending-IOU-cash. Five pre-publish IOUs flagged in the record: DR-009 body read, anti-hallucination checklist body read, agent-ready-papers public URL fetch, AE pattern public URL fetch, audits-directory browsability check. Cash before promoting to `src/pages/writing/`.

**Cross-model review.** Per writing-guide §7 + DR-011: Pass 1 small same-family on the final `.astro` body, Pass 2 large same-family fresh-session, Pass 3 cross-vendor with explicit voice-rule filter (skippable if the workflow-vs-model reception checkpoint suggests this piece does not warrant the full battery).

**Pre-empt check vs. cross-model-review.md.** This piece mentions multi-pass review once in the kit list. It does not pre-empt the standalone `cross-model-review` piece because the standalone piece goes deep on the structural argument (two-axes-of-outside-ness, when each pass earns its cost), and this one only names multi-pass review as one tool among several. If cross-model-review ships as the week-after sibling, the kit-list mention here is the right level of foreshadowing.

**Title and subtitle alternatives at review time:**
- Title: *Plausibility passes the AI review. Correctness does not.* (current, strongest)
- Title alternative: *AI review is plausibility review unless you make it not be.* (the generalised claim; longer, less argument-form)
- Subtitle current: *Notes on a 68-equation case and what it shows about the kit.*
- Subtitle alternative: *Notes on a 68-equation document.* (tighter, less framework-forward)

## Reusable phrasings (preserve through revision)

- *"Plausibility passes the AI review. Correctness does not."* Title; strongest line.
- *"AI review is plausibility review unless you make it not be."* Generalised version; travels across citation, equation, and code-review contexts.
- *"The errors survived plausibility review because they produced correct-magnitude, correct-unit, coherent-prose numbers."* Concrete mechanism; useful when the abstract claim needs to land harder. (Not in the current draft body verbatim, but the same idea is in paragraph 7. Consider reinstating the phrasing if the body needs sharpening.)
- *"Same model. Different mode. Different result."* Punchy crystallisation of the calculation-verification finding.
- *"A different kind of check, not a sharper version of the same judgment."* Useful for the generalisation paragraph.
- *"Structural problems take a set of tools, not one."* Kit-justification line.

## Decision log

- **2026-06-05 (morning):** Pivoted from `two-reviews-missed-what-reproduction-caught` to this framing after Jeroen flagged the framework-showcase gap. The case-study form named one slice (reproduce-don't-assess) without making the framework's other tools visible. First-pass prose drafted by cannibalising the case-study material and reframing through the standalone seed.
- **2026-06-05 (review battery):** Three-reviewer pass (mechanical / argument-shape / cold-read voice) run on first-pass body. Consensus finding: kit-list paragraph tipped into list-disguised-as-paragraph. High-severity disjoint findings: generalisation-move lacked bridge sentence; code-review analogy hand-waved. Medium: strongest line buried past midpoint; closing question already answered by body; honest-scope examples all author-side; "The honest scope." opening label teacherly; opaque "second pass" reference. Trim items: italics on *looks right* and *kind*, authorial-declaration phrasing.
- **2026-06-05 (fixes applied):** All consensus + high + medium + trim items applied in one pass. Kit-list paragraph restructured (lead with structural claim, two illustrative tools); bridge sentence added before citations generalisation; code-review analogy softened to "test inherits implementer's frame"; "AI review is plausibility review unless you make it not be" lifted into paragraph 7; closing question reworked to pull reader onto their own artifacts; production-deployment reader-side example added to honest-scope; controlled-variable acknowledgment added to address hidden-assumption flags (prompt-engineering confound, "you held it wrong" reading). Em-dash count after fixes: zero. Body word count: 885.
- **2026-06-05 (downstream artifacts):** Verification record built at `docs/verification/ai-review-is-plausibility-review.md`. Cover image generated at `public/social/ai-review-is-plausibility-review.png`. V&V arc closer memory entry updated to reflect the reframe. Feedback memory written for the trust + context-orchestration frame Jeroen surfaced mid-battery. Cross-model-review draft also updated to weave in the trust + orchestration frame (this is the natural article-surface for that frame; see updated status line in that draft).
- **Remaining before promotion to `src/pages/writing/`:** five IOUs from the verification record (URL fetches and template-body reads), the cross-model review pass per writing-guide §7 (calibrated to blog-scale: Pass 1 + Pass 2 sufficient, Pass 3 skippable), Jeroen's cold re-read.
