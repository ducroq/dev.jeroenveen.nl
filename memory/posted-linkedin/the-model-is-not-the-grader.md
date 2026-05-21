# LinkedIn cross-post record — Most production AI grades its own output

> **Status:** Published 2026-05-21 across both LinkedIn surfaces. URLs and reception notes are in `memory/external-comments.md` (section "2026-05-21 — Publish: Most production AI grades its own output"). This file preserves the full text of what was posted (long-form Pulse article + short feed post) for reuse as a template.
> **Strategy as posted:** Both surfaces. Long-form Pulse article for LinkedIn discovery; short post linking to the Pulse article for feed reach. Same default as `the-work-is-splitting` and `senior-developers-trust-ai-less`.
> **Hashtag set:** #AI #ProductionAI #AugmentedEngineering
> **Arc position:** Standalone. *Not* the V&V arc closer. Post 2's hardware/embedded/control forward-look is still owed.

---

## 1. LinkedIn article (long-form / Pulse)

**URL:** https://www.linkedin.com/pulse/most-production-ai-grades-its-own-output-jeroen-veen-3aoke/

**Title:** Most production AI grades its own output.

**Subtitle:** An observation from a year of building a production AI tool.

**Body:**

Most AI-tooling posts read like demos. The product is shown working, often with a metric attached, and the implicit claim is *this is what an AI system looks like*. The framing skips the engineering decisions that decide whether you can trust the system at all, and one decision in particular keeps coming up in my own work.

The system runs in production under GDPR constraints, so the system description belongs in the system, not here. What I want to write about is the decision.

The decision is that I do not let the LLM grade its own output. That sounds obvious until you look at the dominant patterns in the LLM-evaluation literature: llm-as-judge, self-consistency check, evaluator-optimizer, critic-actor, reflection. They differ in their decoration. They share one property: the evaluator inherits the actor's assumptions, because they came from the same training distribution and they are reading the same artifact in the same way.

The structural alternative is not novel as a pattern, only uncommon in the products I see shipped. The LLM is the finder. Deterministic code, written by hand against a fixed rubric, is the grader. The rubric is derived from engineering standards that exist outside any LLM. The LLM finds candidate issues; the grader scores them against rules that were defined and agreed upon before any LLM was ever called. The grader has no opinion. It enforces.

The difference matters, but it is partial. When the grader is the LLM, you are measuring how the LLM feels about its own output. When the grader is deterministic code reading a fixed rubric, you are measuring whether the output meets the rubric. Those are different things. What this buys is grading-time independence: the scoring is no longer a re-reading by something with the same priors as the producer. What it does not buy is finding-time independence. Anything the LLM-finder fails to surface never reaches the grader. The discipline is about precision against a rubric, not coverage.

Two honest objections live in this. The first is the one I just made: a sibling discipline (cross-model review, scheduled audits, something) has to push back on the finder-side blindness, and that is a different piece. The second is that the rubric authors have opinions, and rubrics edited in response to disagreements with the finder will drift toward what the finder surfaces well. The grader inherits the rubric, which inherits whatever pressure the LLM's failure modes put on the people maintaining it.

The discipline that holds the second objection honest is a checkpoint. Every time we change a prompt, the new prompt runs against a small set of cases we already know the right answers to. The grader scores them, and those scores get compared to what the old prompt got. If they match closely enough, the change ships. If they do not, the change is blocked, and a rubric edit that shifts scores on that set has to be argued for explicitly, not slipped in. We call this a calibration gate. Not a unit test. A calibration check against a known sample, the way you do not change a measurement instrument without re-checking it against a reference standard.

What has this cost. Mostly time. Building a baseline set is slow, and the baseline set is what makes the calibration gate meaningful. Maintaining it is slower. The decisions sit in a stack of architecture-decision records, each with a paragraph attached explaining the alternative we considered and the reason we did not adopt it. That documentation does not show up in any demo. It is the thing that makes the system defensible when somebody senior asks the question that defines whether a system is defensible: *how do you know this works?*

The previous pieces here have argued that validation is the harder half of engineering work, and that the engineers most cautious about AI output are the ones who have validated it most. The past year is what taking that seriously has looked like in one specific case. Not a methodology, not a generalisable claim, not a paper. One decision, and the second decision that makes the first one honest, in case it is useful as evidence that the work the previous pieces describe is not abstract.

What I have not solved is the rubric-drift problem on a longer horizon than the held-out set can see. That is a different piece.

If you have landed on a different grader architecture and it is working for you, I would like to know what made the trade-off come out that way.

---

*Originally published at [dev.jeroenveen.nl/writing/the-model-is-not-the-grader](https://dev.jeroenveen.nl/writing/the-model-is-not-the-grader/)*

#AI #ProductionAI #AugmentedEngineering

---

## 2. Short LinkedIn post (links to the Pulse article)

**URL:** https://www.linkedin.com/feed/update/urn:li:ugcPost:7463114007982325761/

**Body (as posted):**

Most production AI tools let the LLM evaluate its own work. Some tools I have been building for the past year do not.

The LLM finds. Deterministic code grades against a fixed rubric from engineering standards. Every prompt change runs against a held-out reference set first; if scores drift from baseline, the change does not deploy.

Not exotic. Their absence in most public AI tooling is a choice, not a constraint.

If you have landed on a different grader architecture and it is working for you, I would like to know what made the trade-off come out that way.

https://www.linkedin.com/pulse/most-production-ai-grades-its-own-output-jeroen-veen-3aoke/

[auto-card linking to the Pulse article]

#AI #ProductionAI #AugmentedEngineering

**Publish-time edit vs draft:** "The tool I have been building … does not" → "Some tools I have been building … do not". Plural-indefinite softens the singling-out of any one product, consistent with the disclosure constraint (the system is not named in the article surface). Live wording is the canonical record.

**Post-publish edit (2026-05-21, same day as publish):** Initial publish was card-only (the auto-generated Pulse card rendered below the body; the explicit URL was not in the body text). Edited later that day to add the explicit Pulse URL on its own line between the CTA and the hashtags, in addition to the card. Final state: URL + card.

---

## Notes for next time

- **Hook test:** opening sentence of the short post ("Most production AI tools let the LLM evaluate its own work. The tool I have been building for the past year does not.") lands the divergence in the first ~120 characters. If the post under-performs, the hook is the first thing to revise, not the body.
- **Audience filter:** the CTA explicitly asks people who are doing the opposite to defend the choice. Genuine curiosity, not gotcha. If the comment section becomes adversarial, soften the CTA on the next post in the same register.
- **vmodel.eu visibility:** the article does not name the system; the public vmodel.eu site does not disclose its scoring architecture. A reader who clicks through will not be able to verify the central architectural claim against the public surface. That is by design (disclosure constraint). If a commenter asks "is this vmodel.eu?", honest acknowledgement is fine; the disclosure constraint is about the *system description*, not about the *system identity*.
- **Domain-applicability caveat:** the finder/grader split works because the rubric here is expressible (engineering standards). For LLM-as-judge use cases where the rubric is the hard problem (tone, helpfulness), the split collapses. Worth flagging in replies if someone challenges the generality of the claim. The article concedes this implicitly via the closing limitation, but not explicitly.
