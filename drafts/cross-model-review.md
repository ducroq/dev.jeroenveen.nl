# The same model that wrote it cannot catch its own errors

*Status: seed note. Captured 2026-05-12 from agent-ready-papers DR-011 (multi-model review pattern), with fresh empirical data from the senior-trust article publish on the same day.*

---

## The seed

agent-ready-papers DR-011 names a **multi-model review pattern** with three passes that each escape a distinct bias:

| Pass | Escape mechanism | When |
|---|---|---|
| Pass 1: intra-family small | sunk-cost from the session that built the draft | every publish |
| Pass 2: intra-family large | different review character / depth | every major revision |
| Pass 3: cross-vendor | training and stylistic priors | high-stakes only, with mandatory style filter |

The senior-trust article (post 2 of the WHY arc) was the first project here to run the pattern empirically (logged in `memory/external-comments.md` 2026-05-12 publish entry):

- Haiku review surfaced rule-compliance issues
- Opus review surfaced argument-shape issues
- Gemini cross-vendor review surfaced voice-rule violations (after voice-rule filter, net actionable findings: 0)

The empirical finding worth its own article: **cross-vendor review is the right pass for some content classes and the wrong pass for others.** On voice-sensitive content (this article), cross-vendor review mostly surfaces *house-style violations* that any in-house reviewer would not raise. The cost-benefit depends entirely on what failure mode you are trying to escape.

## Why this is article-worthy on dev.jeroenveen.nl

- Connects three existing threads in one piece: the validator-inherits-implementation-assumptions point from the Witek reply (2026-05-03), the senior-trust article's frame on what seniors do that AI does not, and the DR-011 pattern as a *recipe* for the same insight.
- Has fresh empirical data Jeroen just collected. Concrete numbers > abstract argument every time.
- Audience filter: every engineer who has asked an AI to review its own output recognises the problem on first read.
- The voice-rule-filter observation is the kind of nuance that earns LinkedIn engagement, because most "use a different model" advice skips it.

## Possible homes

1. **New dev.jeroenveen.nl article.** Argument-form title candidate: *"The same model that wrote it cannot catch its own errors. A different model often can."* Connects the existing threads, has the empirical anchor, and the closing nuance (some classes of content do not want cross-vendor review) is the kind of thing that makes the piece quotable.
2. **AE pattern essay (or AE pattern note linking to DR-011).** This is genuinely AE territory: it is the *mitigation* pattern for the validation-inherits-implementation-assumptions failure mode.
3. **Standalone short LinkedIn post.** The empirical finding compresses to one strong post: "I just ran three reviewers on the same draft. Each caught a different class of problem. Cross-vendor caught the voice violations everyone else missed, including ones I didn't want flagged." Could draw comments and serve as a teaser for option 1.

Lean: option 1 *after* WHY post 3 ships, because the article will be stronger if it can build on the splitting-work / senior-distrust / domain-bias arc rather than introducing them.

## Open questions before drafting

- DR-011 details above are paraphrased from the agent-ready-papers README, not from the DR itself. Before drafting, read `decisions/DR-011_multi-model-review-pattern.md` directly so the three-pass structure and the language are not laundered through summary. The READMEs's framework-overview style smooths edges that a DR may keep sharp.
- Are the senior-trust review numbers (scores per model, findings filtered, voice-rule filter rate) publishable in detail, or do they belong only in the verification record? The article is stronger with concrete numbers. Needs Jeroen's call on disclosure.
- The "stance-shaped errors vs. knowledge-shaped errors" distinction from the Geert thread (2026-05-04 entry in `memory/external-comments.md`) is the natural conceptual scaffolding for this article. Worth checking it travels cleanly into a longer piece.

## Reusable phrasings

- *"The same model that wrote it cannot catch its own errors. A different model often can."*: strongest line. Title and one-sentence summary.
- *"Cross-vendor review is the right pass for some content classes and the wrong pass for others."*: names the nuance most "use a different model" advice skips.
- *"Stance-shaped errors and knowledge-shaped errors require different reviewers."*: phrasing carried over from the Geert thread, fits naturally here.
- *"The validator inherits the implementation's assumptions."*: phrasing carried over from the Witek thread. Fits as a one-liner inside the article when explaining why same-model self-review fails.

## Decision

Hold as seed. Strongest article path is *after* WHY post 3 ships, so it can build on the validation-asymmetry arc rather than re-establishing it. Until then, the short-LinkedIn-post version (option 3) is available as a teaser if the moment comes.
