# Draft seed: trust is the word the V&V arc never says

> **Status:** seed observation captured 2026-06-02 during the retroactive verification pass on `verification-is-a-workflow-problem`. Not yet a draft. Possibly belongs in: a revision note for the just-published article, the V&V arc closer, or as a standalone bridge piece.

## The observation

The V&V arc on dev.jeroenveen.nl is implicitly about trust. The senior-developers-trust-ai-less article named trust explicitly. The model-is-not-the-grader article was about defensibility, which is the engineered surface of trust. The work-is-splitting article was about validation, which is what *earns* trust. The verification-is-a-workflow-problem article describes the *mechanism* that earns trust.

But `verification-is-a-workflow-problem` never uses the word "trust" once. Checked: 0 occurrences in the article body.

## Why this matters

A reader brings "do I trust this AI output" to every paragraph of an AI-engineering article. The article answers the question at the mechanism level (registry, fresh-session reviewer, multi-pass structure) without bridging back to the affective stakes the reader started with. The V&V vocabulary lands; the trust vocabulary the reader is operating in is left untouched.

The risk is not that readers miss the argument. It's that the argument lands as a technical contribution rather than as the answer to a question they were already asking. AI and trust are in real tension right now: every senior engineer working with AI is doing trust calibration constantly, often without a working framework for it. The V&V arc *is* a framework for trust calibration. The arc doesn't say so.

## Where this could go

Three options, in increasing scope:

1. **Add a single bridging sentence to the published `verification-is-a-workflow-problem` article.** Somewhere in the closing run, name trust explicitly: "The workflow is the trust artefact; the model is not." Or similar. Low-cost revision. Risk: feels tacked-on if the body doesn't develop the word.
2. **Make the V&V arc closer the trust-naming piece.** If the closer is the cross-model-review or driven-pendulum methods piece, frame it as the trust calibration mechanism. The mechanics piece becomes the trust-mechanics piece. Higher payoff; needs the next draft to absorb the frame.
3. **Standalone bridge piece between the V&V arc and whatever comes next.** Short, single-thesis: "Trust is what verification produces, not what it presupposes." The V&V arc is then retrospectively the trust-mechanism arc. Cleanest reframe; most expensive (a new piece, not a revision).

## Forecasts

- If option 1 is chosen, the bridging sentence should be tested for whether it adds or feels welded on. Cross-model review pass advised before pushing.
- If option 2 is chosen, the trust frame should appear in the closer's opening, not just the conclusion. The reader should know within the first 200 chars that this is a trust piece.
- If option 3 is chosen, the trust piece is a different audience than the technical-mechanics V&V audience. Calibrate hashtags accordingly.

## Source of the observation

Jeroen, during the retroactive verification pass on `verification-is-a-workflow-problem` on 2026-06-02. Specifically: "Also, we forgot to use the word 'trust'. AI and trust are really on tension." Captured here so the next session's drafting work can act on it rather than rediscover it.

## Next-session triggers

- Whoever drafts the V&V arc closer should re-read this file before deciding whether the trust frame is a single sentence, a paragraph, or the article's central anchor.
- If a third party engages with the published `verification-is-a-workflow-problem` article using the word "trust" in a comment or reply, option 1 (the bridging sentence) becomes more attractive: the reader is already supplying the bridge.
