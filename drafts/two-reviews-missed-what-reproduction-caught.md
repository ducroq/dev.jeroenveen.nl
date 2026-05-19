# Two reviews missed what one reproduction caught.

*Working subtitle:* A case from my own work in a domain where the trust surveys don't reach.

*Working slug:* `two-reviews-missed-what-reproduction-caught` (open to alternatives; see notes at bottom)

*Drafted: 2026-05-19. V&V arc closer (post 3). Status: first pass, awaiting review.*

---

## Title candidates (pick at review time)

- **Two reviews missed what one reproduction caught.** (mechanism-forward, working pick)
- *The errors two reviews didn't see.* (artifact-leaning, sharper number-in-title)
- *Plausibility passes the review. Correctness does not.* (overlaps with the standalone seed in `drafts/plausibility-vs-correctness.md`, so probably leave it for that piece)
- *Reproduce, don't assess.* (overlaps with the AE pattern name; better as a phrase inside the body than as the title here)

---

## Draft

The last piece here cited three developer surveys on AI trust. All three measured software developers. Equivalent surveys for hardware, embedded, or control engineering don't exist, partly because the populations are smaller and partly because trust is harder to measure where validation work is itself less standardised. What does exist in those domains is concrete validation-failure evidence. Here is one such case, from a project of my own.

Over recent months I have been working on a non-software design project: a small electromagnetic system that nudges mechanical pendulum clocks toward atomic-clock accuracy. AI-assisted throughout. By February the theory document covered ten chapters and 68 equations across pendulum mechanics, synchronisation theory, electromagnetism, control, power analysis, and the error budget. Before any hardware was built on top of those equations, I needed to know whether they were right.

I ran two LLM reviews in the usual assessment mode. Read this, check it for physical soundness, flag anything that looks wrong. One pass used Gemini, one used Claude. Both came back the same. No errors found. Dimensions checked out, magnitudes were in plausible ranges, the prose was internally consistent.

Then I ran a third pass with a different instruction. Same model family as the second pass (Claude Sonnet), but the prompt forced reproduction rather than judgment. Substitute the stated input values into every equation. Compute the result step by step. Compare against the value in the document. Never skip a calculation, never paraphrase a table.

That pass caught three errors.

The first was a label mismatch. A table headed "5 degrees" contained values that had been computed at 1 degree. Coupling estimates in the relevant chapter were therefore five times more optimistic than the design called for. The second was a formula error in a dwell-time calculation: a missing variable and a spurious factor of two made the tabulated values roughly seven times too small. The third was an internal inconsistency: an hourly correction stated as 36 s/hr did not survive the arithmetic. 3.3 ms per swing, times 3,600 swings per hour, lands near 12 s/hr, not 36. The text said one thing, the underlying numbers said another.

All three errors produced individually plausible numbers. Right units, reasonable magnitudes, coherent with the surrounding prose. An assessment-mode reviewer is checking whether the artifact *looks right*. These errors looked right.

Reproduction strips out the degree of freedom plausibility lives in. A calculator does not have an opinion about whether 3.3 times 3,600 equals 36 seconds per hour. The instruction to compute rather than to judge removes the move where "this reads as reasonable" gets to substitute for "this is correct." Same model. Different mode. Different result.

The bridge to the previous piece is direct. Senior engineers trust AI output less than juniors, the surveys keep finding, and the reason is that experienced engineers have seen the gap between plausible and correct often enough to recognise the pattern. In code, the gap shows up as functions that compile, pass their tests, and solve the wrong problem. In equations, it shows up as numbers that pass plausibility review and fail the arithmetic. The validation move is the same in both cases. Do not assess. Reproduce.

Software has tests as a partial fallback for whatever review misses. A non-software design project does not, until the prototype exists, at which point design errors have already been baked into hardware. The validation discipline has to happen earlier, on the artifacts themselves rather than on simulations of those artifacts. That is the part the developer-trust surveys cannot reach in software, and would not measure in pendulum-clock design either, because there are not enough of us to survey.

There is a pattern for this on the <a href="https://augmented-engineering.eu/patterns/reproduce-dont-assess" target="_blank" rel="noopener">augmented engineering site</a> that names the move and gives a usable prompt template. I will not re-narrate it here. What I want to log on this site is the specific evidence: in one 68-equation document, two assessment-mode reviews returned zero errors and one reproduction-mode review returned three. That is a small data point. It is also exactly the kind of data point that does not appear in any developer-trust survey, and would not appear in any equivalent survey for the domain this artifact comes from.

The next pieces will look at where validation work shows up across the rest of the practice. If you have run into your own version of this, a plausibility-passing artifact that turned out to be wrong in a way only a different kind of check could catch, what was the check?

---

## Notes for the review pass

**Word count (body, excluding title and subtitle):** ~870.

**Arc-position audit.** Post 2's forward-look promised "another split that aggregate numbers hide... Equivalent surveys do not exist for hardware, embedded, or control. What does exist in those domains is validation-failure research that did not measure trust. The next piece looks at that asymmetry." This draft opens by naming the asymmetry explicitly (paragraph 1), delivers the worked case as the validation-failure evidence (paragraphs 2–7), then returns to the asymmetry frame in the closing (paragraphs 9–10). Arc match: yes.

**Source-material accuracy check.** The plan memo and glossary entry refer to "two LLMs found zero errors, manual reproduction caught three." The audit document (`agent-ready-papers/audits/driven-pendulum-retrofit.md` §9.1) and the AE pattern page (`augmented-engineering/site/src/pages/patterns/reproduce-dont-assess.astro`) both show the reproduction was *also* LLM-driven (Claude Sonnet 4.5 with a structured "substitute, compute, compare" prompt), not manual. This draft uses the LLM-reproduction framing because (a) it matches the canonical AE pattern doc, (b) it is more honest, and (c) it makes a stronger point: same model family, different mode, different result. Flagging in case "manual reproduction" was the framing you actually wanted. The glossary entry at `docs/glossary.md` may need a one-line correction either way.

**Named-colleague rule (writing-guide §5).** No named colleagues in the body. The Dutch horological sources (van Baalen, Hodzelmans, Notenboom) are background context not load-bearing for this piece, so left out.

**Em-dash audit.** None in the body. Used colons, commas, periods, parentheses, and sentence breaks. Worth re-scanning during your review pass since this is exactly where I drift.

**Cover image / in-article figure.** Recommend *no* in-article figure. The natural candidate ("assessment mode → 0 / reproduction mode → 3" as a diagram) lands in the BEFORE/AFTER cliché the visual-register rule explicitly warns against. The piece is short enough to read cleanly without one. A typographic social-image cover via `scripts/gen-social-image.py` is still needed for the OG image on publish; lean phrase for that: *"Plausibility passes the review. Correctness does not."* or just the title.

**Sources block content to embed in the `.astro` file.** Minimal — only the AE pattern page is publicly linkable as of today. The audit doc lives in `agent-ready-papers/audits/` which I don't know is public yet. Worth a check before publish.

**Verification record.** Needs `docs/verification/<slug>.md` per writing-guide §7 before publish. Load-bearing claims that need primary-source verification:
- "Two LLM reviews in assessment mode returned zero errors" — primary source: `audits/driven-pendulum-retrofit.md` §9.1 and the AE pattern page. Confidence tier: ESTABLISHED (own work, both sources align).
- "One reproduction-mode review caught three errors" — same primary source. ESTABLISHED.
- The three specific errors (label, formula, inconsistency, with the 5x / 7x / 36-vs-12 numbers) — primary source: the audit doc §9.1 and the AE pattern page list. ESTABLISHED.
- The forward-look paraphrase of post 2 — primary source: `src/pages/writing/senior-developers-trust-ai-less.astro`. ESTABLISHED.

**Cross-model review.** Per writing-guide §7 + DR-011: Pass 1 Haiku and Pass 2 Opus on the final `.astro` body before publish.

**Pre-empt check.** This piece names Reproduce-Don't-Assess once via the AE link without re-explaining it, and uses the "do not assess, reproduce" line as the in-text crystallisation. It does not pre-empt the standalone `plausibility-vs-correctness` framework piece because:
- This piece is grounded in *one* case from own work and frames the broader claim only at the closing.
- The standalone piece would generalise: plausibility-vs-correctness across citation, code-review, and prose-claim contexts; this case as one of several pieces of evidence.
- The standalone piece would also have to make the prompt-engineering generalisation argument explicitly; this piece punts to the AE pattern page.

If you'd prefer the standalone framing instead of the V&V-closer framing, that's a different draft that probably borrows two paragraphs from this one and reshapes the rest. Flag if you want me to take that path instead.
