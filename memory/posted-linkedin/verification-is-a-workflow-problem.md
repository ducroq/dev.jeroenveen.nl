# LinkedIn cross-post record — Verification is a workflow problem, not a model problem

> **Status:** Published 2026-06-02 across both LinkedIn surfaces. URLs and reception notes are in `memory/external-comments.md` (section "2026-06-02 — Publish: Verification is a workflow problem, not a model problem"). This file preserves the full text of what was posted (long-form Pulse article + short feed post) for reuse as a template.
> **Strategy as posted:** Both surfaces. Long-form Pulse article for LinkedIn discovery; short post linking to the Pulse article for feed reach. Same default as `the-work-is-splitting`, `senior-developers-trust-ai-less`, and `the-model-is-not-the-grader`.
> **Hashtag set:** #AI #ProductionAI #AugmentedEngineering
> **Arc position:** V&V arc continuation, interleaved evidence-from-own-work. Frame-traveling design.

---

## 1. LinkedIn article (long-form / Pulse)

**URL:** https://www.linkedin.com/pulse/verification-workflow-problem-model-jeroen-veen-6nrie/

**Title:** Verification is a workflow problem, not a model problem.

**Subtitle:** Notes from a €5k hardware research session.

**Body:**

A €5k hardware-purchase research exercise. I drafted a verdict using a strong frontier model with full session context. The verdict read internally consistent.

Two fresh-session reviewers found fifteen issues in it, with near-zero overlap between them. One was a small same-family model running a mechanical checklist. One was a large same-family model in a fresh session running an argument-shape critique.

Two of those issues are useful here.

The first was a number nobody could source. A trade-press article had stated that a recent open-weight model needed only 5.48 GB of GPU memory to hold a million-token context, framed as a hardware-does-not-matter-anymore argument. The figure was credited to an unnamed analyst using unspecified modeling benchmarks. The drafting context took the number as authoritative. Four independent technical sources, when checked, gave figures from 9.6 GB up. The vendor's own model card gave only a relative figure.

The second was a category swap the drafter never flagged. An argument about demand for AI tools that assist with code by completing lines and suggesting edits was using usage data from a different product class: AI tools that run as long-running autonomous agents executing multi-step plans. The two shared the "self-hosted AI agent" framing but did materially different jobs. A reviewer with no investment in the drafting context, asked directly whether the cited platform's stated primary purpose matched the use case being argued, surfaced the swap immediately.

Notice what would not have caught either of these. Most advice on catching GenAI mistakes points at the model. Retrieval-augmented generation, citation checkers, grounded generation, judge models. The implicit picture is that if the model had more information, or the right kind of supervision, the output would be more reliable. Neither error here lives in the model's output. Both live in the drafting context, which the model cannot see from inside.

RAG retrieves what you ask for. The drafter had access to the trade-press article and to vendor documentation; what was missing was a prompt to compare them against each other. Citation checkers confirm that referenced sources exist. The 5.48 number had a citation, vaguely, with no name and no methodology. That is exactly the pattern model-level checkers cannot flag. Grounded generation pins outputs to a corpus. It does not check whether the corpus supports the kind of claim the output makes. All three operate on the model's output. None of them operate on the context that produced it.

What did catch the errors was a workflow with three properties: a registry that named which claims supported which conclusions and required source-tier metadata on each, a fresh-session reviewer with no investment in the conclusion, and a multi-pass structure that escapes the bias of the drafting context at two different scales. The registry is the verification artefact. The reviewer is the verifier. The multi-pass structure is the redundancy. None of this lives inside the model.

The framework I have been building is agent-ready-papers (https://github.com/ducroq/agent-ready-papers). The name is paper-specific; the discipline is not. Typed claim registry. Source-tier metadata on every load-bearing claim. Anti-hallucination checklist applied before commit. Multi-pass review with reviewer-bias escapes at two different scales. The paper-specific bits, page budgets, LaTeX, journal style guides, are about twenty percent of it. The other eighty percent is "GenAI failure modes need verification infrastructure because the failures are not noise, they are structural."

What I have come to see is that this generalises cleanly to research and decision-making. If you are about to commit money or reputation based on GenAI-synthesised claims, the typed registry, source tiering, anti-hallucination checklist, and multi-pass review apply identically. None of them require the artefact to be a paper.

The honest counter-argument is overhead. A V&V battery costs real time. For low-stakes work the model-level interventions are the right tool: cheap, fast, no infrastructure. The framework starts earning its keep where the cost of being wrong exceeds the cost of running the verification. Hardware purchase decisions cross that threshold. Most strategic decisions do. Most personal coding sessions do not.

The discourse will catch up to this distinction slowly. Every GenAI-engineering thread right now defaults to model-level: which retriever, which evaluator, which prompt template. These are real, and they matter. But they will not catch the failures whose cause lives in the workflow that wraps the model. Category-shape and source-shape are not properties the model has access to from inside its own context. The verifier has to be outside.

Where have you seen verification at the wrong layer catch up with you?

---

*Originally published at [dev.jeroenveen.nl/writing/verification-is-a-workflow-problem](https://dev.jeroenveen.nl/writing/verification-is-a-workflow-problem/)*

#AI #ProductionAI #AugmentedEngineering

---

## 2. Short LinkedIn post (links to the Pulse article)

**URL:** https://www.linkedin.com/posts/jeroen-veen-3244444_ai-productionai-augmentedengineering-activity-7467455776672972800--QlF

**Body (as posted):**

The verifier has to be outside.

A €5k decision. A frontier model with full session context drafted the verdict. Two fresh-session reviewers found fifteen issues with near-zero overlap.

The drafter missed nothing the model itself could have caught. The failures lived in the drafting context, where RAG, citation checkers, and grounded generation cannot reach.

Where have you seen verification at the wrong layer catch up with you?

https://www.linkedin.com/pulse/verification-workflow-problem-model-jeroen-veen-6nrie/

[auto-card linking to the Pulse article]

#AI #ProductionAI #AugmentedEngineering

---

## Notes for next time

- **Hook test:** The short post opens with the kicker ("The verifier has to be outside") as a frame-claim hook, then delivers the €5k case as supporting evidence. Frame-claim hooks landed work-splitting's saves and reposts (best frame-adoption signal of the four prior posts). If under-performing after 5–7 days, the hook is the first thing to revise; a concrete-case-first version is the alternative.
- **CTA calibration:** "Where have you seen verification at the wrong layer catch up with you?" is medium-tight (specific topic, personal-experience question). Per `project_linkedin_post_reception_patterns.md`, this should produce more comments than the over-tight model-not-grader CTA (which zeroed out at 1,250 impressions) and similar to work-splitting / senior-trust CTAs. If it still returns zero, the topic itself may be the filter, not the wording.
- **vmodel.eu non-disclosure:** the article does not name vmodel.eu. The €5k case is a *different* shipped system (personal hardware research, not the production AI). If a commenter asks "is this vmodel?", honest answer is no — that one is the system referenced in `the-model-is-not-the-grader`.
- **LinkedIn slug unpredictability:** the assigned Pulse slug dropped "not" from the article title (`verification-workflow-problem-model-jeroen-veen-6nrie` instead of `verification-workflow-problem-not-model-jeroen-veen`). Worth remembering for future cross-posts: do not pre-bake the Pulse URL into the short-post draft; wait for the actual slug after publish.
- **Frame-adoption signal:** "verification lives in the workflow, not the model" is the most adoptable frame in the V&V arc to date. If reposts appear on this one (they have not on any of the four prior posts), it would be the first signal that an adoptable frame can earn public endorsement, not just private save.
