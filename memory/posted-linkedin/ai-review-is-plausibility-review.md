# LinkedIn cross-post record — AI review is plausibility review.

> **Status:** Published 2026-06-08 across both LinkedIn surfaces. URLs and reception notes are in `memory/external-comments.md` (section "2026-06-08 — Publish: AI review is plausibility review."). This file preserves the full text of what was posted (long-form Pulse article + short feed post) for reuse as a template.
> **Strategy as posted:** Both surfaces. Long-form Pulse article for LinkedIn discovery; short post linking to the Pulse article for feed reach.
> **Hashtag set:** #AI #ProductionAI #AugmentedEngineering
> **Arc position:** V&V arc post 4, framework-showcase slot per `project_vv_arc_closer.md`.
> **Register experiment:** This is the noise-injection cross-post — louder/conversational register vs. modesty-register baseline. See external-comments.md entry for the experiment framing, calibration targets, and decision rules.

---

## 1. LinkedIn article (long-form / Pulse)

**URL:** https://www.linkedin.com/pulse/ai-review-measures-plausibility-jeroen-veen-hyrde/

**Title:** AI review is plausibility review.

**Body (as posted, after Jeroen's in-LinkedIn-window edits):**

Two AI reviews in assessment mode caught zero errors in a 68-equation theory document. A third pass with the same model family but a reproduction instruction, caught three.

Some context. A theory document I had been working on for several months. Ten chapters, AI-assisted throughout, covering mechanics, synchronization, electromagnetism, control, power analysis, and the error budget. Hardware was about to be built on top of it. I needed to know whether the equations were right.

First, I ran two LLM reviews in the usual assessment mode: Read this, check it for physical soundness, and flag anything that looks wrong. One pass used Gemini, the other Claude. Both came back clean. No errors found. Dimensions checked out, magnitudes were in plausible ranges, and the prose was internally consistent.

Then I ran a third pass with a fundamentally different instruction. This time, the prompt forced reproduction rather than judgment: Substitute the stated input values into every equation. Compute the result step by step using code and calculation tools. Compare the output against the value in the document. Never skip a calculation; never paraphrase a table.

That pass caught the errors.

Coupling estimates came out optimistic by a factor; timing values were nearly an order of magnitude too small. Two were arithmetic bugs of the same kind; neither survived recomputation. The third error was sharper because it self-contradicted on the page: the text said one thing, but the math said another.

All three errors produced individually plausible numbers. They had the right units, reasonable magnitudes, and cohered perfectly with the surrounding prose. An assessment-mode reviewer checks whether an artifact looks right. These errors looked right.

Reproduction strips out the degree of freedom plausibility lives in. A calculator does not have an opinion about whether 3.3 times 3,600 equals 36 seconds per hour. The instruction to compute rather than to judge removes the move where "this reads as reasonable" gets to substitute for "this is correct." Same model. Different mode. Different result.

AI review is plausibility review, unless you force it not to be.

This mechanism isn't specific to arithmetic. Assessment checks the surface an artifact presents; reproduction operates on a reality the artifact cannot fake.

Citations are a perfect example. They are entirely plausibility-shaped: an invented DOI looks like a real DOI, and a hallucinated author sounds like a real author. An LLM asked "does this citation support the claim?" can answer fluently while referencing a paper that doesn't exist. The escape velocity is forcing the AI to verify that the source actually exists and explicitly matches the text, rather than judging whether the citation reads plausibly.

Code follows the exact same pattern. Functions that compile, pass their tests, but solve entirely the wrong problem are "plausibility-passing." When the same developer writes both the implementation and the test, the test inherits the implementer's blind spots. The only check that escapes this loop is reproduction in the runtime sense: executing the function against edge cases the implementer failed to anticipate.

In every instance, the pattern is identical: The artifact reads as right, so the reviewer accepts it. The escape is a completely different kind of check, not a sharper version of the same judgment.

These patterns form the backbone of a framework called agent-ready-papers, which includes the equation-checker for arithmetic, the anti-hallucination checklist for citations, and reproduction tests for code.

Rigorous verification costs real time and compute, and not every artifact warrants it. A weekend prototype probably doesn't. But a theory document with hardware waiting on it easily crosses the threshold. So does a €5k procurement exercise, or a production deployment whose failure mode is being quietly wrong for months.

The framework starts earning its keep the moment the cost of being wrong exceeds the cost of running the verification.

---

#AI #ProductionAI #AugmentedEngineering

---

## 2. Short LinkedIn post (links to the Pulse article)

**URL:** https://www.linkedin.com/posts/jeroen-veen-3244444_ai-productionai-augmentedengineering-activity-7469630799009574912-3TEj

**Pulse linkage:** Auto-card to Pulse article. URL not in body text; auto-card preserves click-through.

**Body (as posted, single block, no paragraph breaks):**

> We almost built expensive hardware using flawed math. We ran an equation-heavy design document through an AI reviewer twice, and both times it found zero errors. On the third try, using the exact same AI, it caught three critical mistakes. The only thing that changed was the instructions. The first two times, we asked the AI to assess the document: "Read this and flag anything that looks wrong." The problem is that AI is great at checking for plausibility. The errors it missed looked completely reasonable on the surface. The right units, normal magnitudes, and smart-sounding prose. Because it looked right, the AI skimmed right past the math. For the third pass, we forced the AI to reproduce the work: "Take these numbers, calculate every step from scratch, and compare your answers to the text." That instruction forced the AI to stop guessing and actually spin up its code and calculation tools. That is when the errors came to light. Assessment just checks if something looks right. Reproduction forces the AI to use its tools to prove the math, stripping away the "vibe check" entirely. If you want an AI to catch real mistakes, don't ask it to review your work. Make it do the work itself.

#AI #ProductionAI #AugmentedEngineering

---

## Notes on what was posted vs. what was drafted

The draft at `drafts/ai-review-is-plausibility-review-linkedin.md` proposed a short post in the modesty register, mirroring the article's voice with the calculator phrase + the explicit frame line + a closing question CTA. Jeroen posted a different short-post variant — louder/conversational register, "we" first-person, no frame line, closing imperative — explicitly as a noise-injection / register experiment to test whether the modesty-register cluster of low-engagement outcomes (verification-workflow, model-not-grader) is a local minimum. Calibration plan and decision rules are in `memory/external-comments.md`.

The Pulse article itself was posted close to the draft, with these Jeroen-edits in the LinkedIn window:
- Title changed from draft's "AI review measures plausibility." (article title-form) to "AI review is plausibility review." (frame-claim form)
- Spelling normalised to US (synchronization, not synchronisation)
- Reproduction instruction adds "using code and calculation tools" — accurate to actual tooling
- Frame line moved to its own one-line paragraph and sharpened to "force" not "make"
- Closing question CTA dropped; piece ends on the threshold statement
- Several adjectives added throughout ("perfect example," "entirely," "easily crosses," "rigorous") — slight louder register lean even in the long form
- Agent-ready-papers reference kept (per the in-conversation suggestion) but as plain text in body, not hyperlinked

## Calibration check date

**Target:** 2026-06-15 (~7 days post-publish). Compare to:
- verification-workflow baseline (modesty register, narrow distribution)
- model-not-grader baseline (modesty register, narrow distribution, similar hashtag set)
- the-work-is-splitting baseline (modesty register, frame-claim hook, saves earner)

Decision rules in `memory/external-comments.md` 2026-06-08 entry.

---

## Preserved variants for register-experiment comparison

Both versions captured side-by-side so the simulated-annealing decision rules in `external-comments.md` 2026-06-08 entry can be evaluated against the actual counterfactual draft, not a remembered approximation. **Variant B is the live post.** Variant A is what was drafted but not posted; it represents the modesty-register baseline that the experiment is testing against.

### Variant A — modesty register (drafted, NOT posted)

**Short post body (drafted at `drafts/ai-review-is-plausibility-review-linkedin.md` before deletion):**

> Two AI reviews caught zero errors in a 68-equation theory document. A third pass with the same model family caught three. Hardware was about to be built on it.
>
> What changed was the instruction. The first two ran in assessment mode: read this, flag what looks wrong. The third was forced into reproduction: substitute the values, compute step by step, compare against the document.
>
> All three errors produced plausible numbers. Right units, reasonable magnitudes, coherent prose. They passed assessment because assessment checks whether the artifact looks right. AI review measures plausibility, unless you make it not be.
>
> A calculator does not have an opinion about whether 3.3 times 3,600 equals 36 seconds per hour. Reproduction strips out the degree of freedom plausibility lives in.
>
> Which of your current review steps would survive being reframed as reproduction rather than assessment?
>
> [Pulse URL on its own line]
>
> #AI #ProductionAI #AugmentedEngineering

**Properties of Variant A:**
- First-person singular ("I" implicit; no first-person plural)
- Frame line present explicitly ("AI review measures plausibility, unless you make it not be")
- Mechanism phrase present ("A calculator does not have an opinion about whether 3.3 times 3,600 equals 36 seconds per hour")
- Closing CTA is an open question ("Which of your current review steps would survive being reframed as reproduction rather than assessment?")
- Five paragraph breaks for scannability
- Voice: restrained, modesty register, consistent with article + writing-guide rules
- Designed against the verification-workflow failure modes (concrete-case lead, adoptable frame, concrete-verb CTA)

### Variant B — louder / conversational register (POSTED 2026-06-08)

Full body captured above in "2. Short LinkedIn post (links to the Pulse article)". Summarised properties:

- First-person plural ("we" throughout)
- Frame line absent (substituted by "Assessment just checks if something looks right")
- Mechanism phrase absent (substituted by "spin up its code and calculation tools")
- Closing CTA is an imperative ("Make it do the work itself"), not a question
- No paragraph breaks (single block)
- Voice: conversational, idiom-rich ("smart-sounding prose," "skimmed past," "vibe check")
- Designed as noise-injection / register experiment vs. the modesty-register cluster

### Comparison axes for the 2026-06-15 read-in

| Axis | Variant A (not posted) | Variant B (posted, live) |
|---|---|---|
| First-person | singular ("I") | plural ("we") |
| Hook | numbers + stakes in three short sentences | stakes-first ("almost built expensive hardware") then context |
| Frame line | explicit, mid-paragraph | absent / diluted |
| Mechanism phrase | "calculator does not have an opinion" | "spin up its code and calculation tools" |
| CTA | open question (reproduction vs. assessment) | imperative ("make it do the work itself") |
| Paragraph breaks | five paragraphs | one block |
| Register | modesty | conversational/louder |

When the 2026-06-15 reception numbers come in for Variant B, this preserved Variant A is the imagined counterfactual. The experiment cannot run both versions, so the comparison is necessarily against the verification-workflow + model-not-grader baselines, with Variant A documented as "what the modesty register would have shipped given the same article underneath."
