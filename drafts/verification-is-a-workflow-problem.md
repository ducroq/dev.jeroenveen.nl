# Verification is a workflow problem, not a model problem

*Status: draft. Captured 2026-05-31 from a V&V battery run during a 2026-05-30 personal hardware research session. The session itself is the worked example, now living at `new_hardware/vv/` (typed claim registry, per-pass review records, gotcha log).*

*Position vs sibling drafts: this is the **focused argument** on layer (where verification needs to live), narrower than `if-it-has-claims-it-has-tests.md` (the umbrella thesis on what is verifiable at all) and adjacent to `cross-model-review.md` (the DR-011 recipe). Three drafts, three different angles on the same conviction.*

---

## The draft

Most advice about catching AI mistakes points at the model. Retrieval-augmented generation, citation checkers, grounded generation, judge models. Better grounding, better calibration, better evaluators. The implicit picture is that if the model just had more information, or the right kind of supervision, the output would be more reliable.

I have just spent a long session watching that picture fail at two different kinds of error, and the fix in both cases lived somewhere else.

The session was a hardware-purchase research exercise for myself. Around €2k of equipment in November, gated on revenue. I drafted a verdict using a strong frontier model with full session context. The verdict read internally consistent. Two fresh-session reviewers, one small same-family model running a mechanical checklist, one large same-family model in a fresh session running an argument-shape critique, found fifteen issues between them with near-zero overlap.

Two of those issues are useful here.

The first was a quantitative claim. A trade-press article had stated that a recent open-weight model needed only 5.48 GB of GPU memory to hold a million-token context, framed as a hardware-does-not-matter-anymore argument. The figure was credited to an unnamed analyst using unspecified modeling benchmarks. The drafting context took the number as authoritative. Four independent technical sources, when checked, gave figures from 9.6 GB up; the vendor's own model card gave only a relative figure. The 5.48 number could not be sourced.

The second was a category-shape error. An argument about demand for a specific kind of AI coding tool was using a different kind of AI agent platform as load-bearing evidence. The two products shared the "self-hosted AI agent" framing. The drafting model did not flag the conflation. A reviewer with no investment in the drafting context, asked directly whether the cited platform's stated primary purpose matched the use case being argued, surfaced the swap immediately.

Neither error would have been caught by the model-level interventions that dominate current AI-verification advice.

RAG retrieves what you ask for. The drafting agent had access to the trade-press article and to vendor documentation; what was missing was a prompt to compare the two against each other. A citation checker confirms that a referenced source exists. The 5.48 number had a citation, vaguely. The citation just had no name and no methodology, and a model-level checker has no way to flag that pattern as suspicious. Grounded generation pins outputs to a corpus; it does not ask whether the claim, having been generated from real evidence, is the kind of claim that evidence supports.

What did catch the errors was a workflow with three properties: a registry that named which claims supported which conclusions and required source-tier metadata on each, a fresh-session reviewer with no investment in the conclusion, and a multi-pass structure that escapes the bias of the drafting session at two different scales. The registry is the verification artefact. The reviewer is the verifier. The multi-pass structure is the redundancy. None of this lives inside the model.

The framework I used is called [agent-ready-papers](https://github.com/ducroq/agent-ready-papers), and the name almost gates the invitation. The author has been steadily extending it: a recent decision-record opened it to speculative-design work, another added the multi-pass review pattern using a blog article and a LinkedIn cross-post as the empirical surface. The README explicitly names WhatsApp and Slack messages with quantitative claims as in-scope. None of this is paper-specific. The paper-specific bits, page budgets, LaTeX, journal style guides, are about twenty percent of the framework. The other eighty percent is "AI failure modes need verification infrastructure because the failures are not noise, they are structural."

What I have come to see is that this generalises cleanly to research and decision-making. If you are about to commit money or reputation based on AI-synthesised claims, the typed registry, source tiering, anti-hallucination checklist, and multi-pass review apply identically. None of them require the artefact to be a paper.

The honest counter-argument is overhead. A V&V battery costs real time. For low-stakes work the model-level interventions are the right tool: cheap, fast, no infrastructure. The framework starts earning its keep where the cost of being wrong exceeds the cost of running the verification. Hardware purchase decisions cross that threshold. Most strategic decisions do. Most personal coding sessions do not.

The discourse will catch up to this distinction slowly. Every AI-engineering thread right now defaults to model-level: which retriever, which evaluator, which prompt template. These are real, and they matter. But they will not catch the failures whose cause lives in the workflow that wraps the model. Category-shape and source-shape are not properties the model has access to from inside a single call. The verifier has to be outside.

Where have you seen verification at the wrong layer catch up with you?

---

## Pre-publish TODO

- [ ] Verification record at `docs/verification/verification-is-a-workflow-problem.md` per writing guide §7 (anti-hallucination Step 0 + Steps 4-6 on every load-bearing claim)
- [ ] Confirm the "fifteen issues between them" number matches what Pass 1 (8 mechanical) + Pass 2 (7 argument-shape) actually produced in `new_hardware/vv/audits/`
- [ ] Decide whether to name VentureBeat / DeepSeek V4 / OpenClaw explicitly or keep them as "trade-press article" / "open-weight model" / "AI agent platform" (current draft keeps them anonymised; the argument lands either way, naming would add specificity at the cost of side-quests for readers unfamiliar with the names)
- [ ] Add `Sources` block per writing guide §7: agent-ready-papers, DR-010, DR-011, vLLM blog 2026-04-24 (the 9.6 GB figure), DeepSeek V4 Pro model card
- [ ] Read-aloud test pass
- [ ] Cross-model review pass per writing guide §7 (fresh Claude session OR different vendor, Variant B of `templates/review-prompt.md`, voice rules inlined)
- [ ] LinkedIn cross-post draft at `drafts/verification-is-a-workflow-problem-linkedin.md` per `docs/workflows/adding-an-article.md`
- [ ] Title-form audit: "Verification is a workflow problem, not a model problem" is argument-form. Alternative title candidates if A/B-testing the LinkedIn hook: "Better models will not catch your category swap" / "RAG cannot catch what process can" / "Citation-checkers do not catch the errors that matter"
- [ ] Em-dash audit: verified zero em-dashes in current draft; re-check after revisions

## Notes for cross-model review

When the cross-model pass runs, ask specifically about:
1. Does the opening sentence filter for the right reader (mid-to-senior engineer, AI/ML lead at EU company), or does it open a teaching post?
2. Is the strongest line ("The verifier has to be outside") in the top half of the article, or buried in the closing?
3. Is the relationship to `if-it-has-claims-it-has-tests.md` and `cross-model-review.md` clear enough that a reader who lands on this one will understand it stands alone, without needing the other two?
4. Does the "twenty percent / eighty percent" split land as honest observation or as too-tidy framing?
