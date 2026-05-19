# Plausibility passes the AI review. Correctness does not.

*Status: seed note. Captured 2026-05-12 from a fresh read of agent-ready-papers README, in particular the 68-equation case study (`audits/equation-verification-journey.md` and `audits/driven-pendulum-retrofit.md` §9).*

---

## The seed

The agent-ready-papers framework has an empirical anchor that the WHY arc has so far cited only in passing: a 68-equation document where an LLM asked to "review for soundness" caught 0 of 3 arithmetic errors, while the same LLM asked to "numerically reproduce every calculation" caught all 3. The errors survived plausibility review because they produced correct-magnitude, correct-unit, coherent-prose numbers. The reviewer was not stupid. The review type was wrong.

This is the cleanest possible demonstration of a general claim: **AI review is plausibility review unless you make it not be.** Engineers who have only met the "LLM hallucinates a citation" version of this failure have not yet met the harder version: plausibility-passing artifacts that are wrong in ways the AI's own evaluator cannot detect from the artifact alone.

## Why this is article-worthy on dev.jeroenveen.nl

- The empirical hook is sharper than anything else in the framework portfolio (3/3 vs 0/3 in a 68-unit document).
- It is the engineer-facing complement to Paper 1 (Verification Gap perspective for Learned Publishing). Same anchor, different reader.
- It connects directly to the WHY arc (validation-half is invisible because plausibility is what AI does well) but stands alone if cold-read.
- It also connects to the senior-trust article: seniors trust less *because* they distinguish plausibility from correctness; that distinction is exactly what the equation-checker prompt forces the model to make.

## Possible homes

1. **New dev.jeroenveen.nl article.** Argument-form title candidates: *"Plausibility passes the AI review. Correctness does not."* (strongest), or *"AI review is plausibility review unless you make it not be."* (the generalised claim). Either could carry the piece.
2. **AE pattern essay extending Reproduce, Don't Assess.** The pattern exists; this is the *evidence* for why it has to exist. Could be a long evidence-anchor essay sitting alongside the pattern.
3. **Paragraph inside WHY post 3.** Probably too good for a paragraph. Better as its own piece.

Lean: option 1. The empirical anchor is strong enough to carry an article, the audience filter is automatic (engineers who use AI-assisted review will recognise the shape immediately), and it does not require having read the WHY arc.

## Open questions before drafting

- Is the full driven-pendulum case study public-citable yet, or only in agent-ready-papers `audits/`? An engineer-facing article needs a public link the reader can follow. If not public yet, either wait, or extract the 68-equation result into a self-contained narrative the article can carry on its own.
- Is there a non-equation example of the same failure mode that travels to non-physics readers? Hallucinated-citation is the obvious second instance; there should be a code-review instance and a prose-claim instance to round out the gallery.
- How much of the "asked to review for soundness vs. asked to reproduce" prompt-engineering detail is *generalisable* vs. *artifact of the specific prompts used*? The article either argues a general principle or reports a specific result; the line between them matters.

## Reusable phrasings

- *"Plausibility passes the AI review. Correctness does not."*: strongest line. Argument-form title, closing aphorism, and quote-pull for the cover image.
- *"AI review is plausibility review unless you make it not be."*: generalised version. Travels to citation, equation, and code-review contexts.
- *"The errors survived plausibility review because they produced correct-magnitude, correct-unit, coherent-prose numbers."*: concrete mechanism. Useful when the abstract claim needs to land harder.

## Decision

Hold as seed until WHY post 3 ships. Then decide: standalone article on dev.jeroenveen.nl (lean), or AE pattern evidence-essay companion to Reproduce-Don't-Assess.
