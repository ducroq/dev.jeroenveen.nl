# LinkedIn cross-post: Senior developers trust AI less than juniors.

> **Status:** Draft, awaiting cold re-read. Article live at https://dev.jeroenveen.nl/writing/senior-developers-trust-ai-less/ since 2026-05-12.
> **Strategy:** Both surfaces. Long-form Pulse article for LinkedIn discovery, short post linking to the Pulse article for feed reach. Same call as work-is-splitting (post 1 of 3 in the WHY arc); the site has slightly more authority now (3 published pieces, one with the new figure) but still young.
> **Hashtag set:** #AI #DeveloperProductivity #AugmentedEngineering
> **Arc context:** Post 2 of 3. Post 1 (`the-work-is-splitting`) set up the produce-vs-validate split. This piece is the same observation from a different angle: the senior trust gap is what validation accumulating looks like at the individual level.

---

## 1. LinkedIn article (long-form / Pulse)

**Title:** Senior developers trust AI less than juniors. The data flips the conventional take.

**Subtitle:** What multiple 2025 surveys keep finding.

**Body:**

I notice the senior engineers I work with often trust AI output less than the juniors do. They read what the agent produced, recognise that it looks plausible, and slow down. The juniors paste it in. The conventional read is the generational one: older devs are slower to warm to new tools. The data points at something more specific.

The clearest measurement comes from METR's 2025 study. They put 16 experienced developers on tasks in their own codebases, with and without AI assistance. The contributors finished 19% slower with AI. After the study they reported feeling 20% faster. That is a 39 percentage point gap between what was measured and what was felt, in people who do this work full-time, on code they wrote themselves. The slowdown is real. The felt experience lags behind it.

The pattern shows up at scale too. JetBrains' 2025 Developer Ecosystem survey of 24,500 software developers found that those with ten or more years of experience report low trust in AI output 61% of the time. Those with zero to two years of experience report low trust 48% of the time. Stack Overflow's 2025 Developer Survey, separately, with 49,000 respondents, found that 46% of developers actively distrust AI output accuracy. Of the experienced developers in the sample, only 2.6% reported "highly trusting" AI outputs and 20% reported "highly distrusting" them: the lowest trust and highest distrust of any experience bracket.

Engineers with more years of practice trust the tool less.

The piece I wrote last week argued that engineering work has decomposed into producing output and validating it, and that validation is the harder of the two. The senior-trust gap is the same observation from a different angle. Seniors trust less because they have validated more, and validation has shown them more. They have seen the plausible-but-wrong code enough times to recognise the pattern in AI output specifically. Juniors have not yet seen enough wrong-looking code in general to develop the calibration.

A small concrete example. Three weeks ago I was reviewing a retrieval function the agent had written for the ese-bot codebase. Plausible. Type-checked. Wrong about which boundary the retrieval was supposed to respect. It took me fifteen minutes to find the error. The generation had taken seconds. The trust calibration in that moment was not about familiarity with AI. It was about familiarity with the failure modes of code that looks right but is not.

The conventional take in industry coverage is that AI is a junior-shaped problem. It replaces junior work, and seniors will be fine because they were already fine. The data flips this. AI is most disruptive to the population that knows enough to validate what it produced. Seniors are the ones currently noticing. Juniors will inherit a code base shaped by validation that did not happen.

This matters for how teams invest in their AI practice. If aggregate productivity numbers look positive but the senior productivity number is negative, the aggregate is hiding a population split. The investment that pays off is not training juniors to prompt better. It is making the validation work that seniors are already doing legible enough to scale.

The next piece will be about another split that aggregate numbers hide. The data I cited above is software-developer survey data: JetBrains, Stack Overflow, METR's open-source contributors. Equivalent surveys do not exist for hardware, embedded, or control. What does exist in those domains is validation-failure research that did not measure trust. The next piece looks at that asymmetry.

If you have noticed your own trust in AI output going down rather than up, where in your work did that shift happen?

---

*Originally published at [dev.jeroenveen.nl/writing/senior-developers-trust-ai-less](https://dev.jeroenveen.nl/writing/senior-developers-trust-ai-less/)*

#AI #DeveloperProductivity #AugmentedEngineering

---

## 2. Short LinkedIn post (links to the Pulse article)

Senior developers trust AI less than juniors. The data flips the conventional take.

I keep noticing this in my own teams: senior engineers read AI output, recognise that it looks plausible, and slow down. The juniors paste it in. It is tempting to call this generational. The data points elsewhere.

In JetBrains' 2025 survey of 24,500 developers, those with ten or more years of experience report low trust in AI output 61% of the time. The zero-to-two-years bracket: 48%. Stack Overflow's 2025 survey of 49,000 developers found the same direction: experienced developers have the lowest "highly trust" rate (2.6%) and the highest "highly distrust" rate (20%) of any bracket.

The conventional take is that AI is a junior-shaped problem. The data says AI is most disruptive to the population that knows enough to validate what it produced. Seniors are the ones currently noticing. Juniors will inherit a code base shaped by validation that did not happen.

Where in your work did your trust in AI output shift?

[paste LinkedIn article URL here once published]

#AI #DeveloperProductivity #AugmentedEngineering

---

## Publish order (suggested)

1. Publish the LinkedIn Pulse article first. Copy its URL once live.
2. Paste that URL into the short post in place of the placeholder.
3. Publish the short post.
4. Log this engagement in `memory/external-comments.md` after a day or two. Note any replies worth tracking, what landed, what didn't.
5. After publish: move this file from `drafts/` to `memory/posted-linkedin/senior-developers-trust-ai-less.md`, update its status header (per `docs/workflows/adding-an-article.md`).

## Notes for next time

- Reception comparison vs work-is-splitting Pulse: if this piece outperforms or underperforms post 1, that informs the framing for post 3 (the software-bias / hardware-embedded gap piece). The senior-trust framing is more counter-intuitive than work-is-splitting; expect either higher engagement or harder push-back.
- Watch for "but seniors are slow adopters, that's all this is" responses. The article's paragraph 1 already names that read; the response in comments is to point at the METR 19%-slower-with-AI finding (seniors who DO use AI are objectively slower, so their distrust matches measured reality, not generational lag).
- The closing question is the same shape as work-is-splitting's ("where has validation become heavier than production?"). Testing whether the "where in your work" prompt is the durable comment-prompt template for the arc.

## Pre-publish review pass (per writing-guide Section 9)

- [ ] First-sentence audit: filters for senior/AI-lead reader, not a teaching post
- [ ] Title is argument-form: "Senior developers trust AI less than juniors. The data flips the conventional take." (counter-claim + intensifier)
- [ ] Strongest line is the title; leads
- [ ] No HAN / institutional jargon
- [ ] No colleague's lived moment as load-bearing element
- [ ] One CTA (the closing question), not three
- [ ] Read aloud test: cold re-read tomorrow
- [ ] Voice intact: restrained, specific, modest, evidence-visible
- [ ] Numbers paired with meaning: 61%/48% (JetBrains), 2.6%/20% (Stack Overflow), 39 percentage points (METR)
- [ ] No em-dashes anywhere in the body (audited; only hyphens for compound modifiers like "type-checked", "zero-to-two-years")
- [ ] No "key takeaways" or "in conclusion"
- [ ] Cross-model review pass: run before publish (paste body into different model with `templates/review-prompt.md` Variant B; filter output against writing-guide Section 6)
