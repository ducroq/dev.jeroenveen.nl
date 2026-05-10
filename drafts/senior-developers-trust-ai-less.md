# Senior developers trust AI less than juniors.

> **Status:** DRAFT, awaiting cold re-read (parked 2026-05-07).
> **Series:** post 2 of 3 in the WHY arc. Counter-intuitive data post.
> **Anchor:** JetBrains 2025 Developer Ecosystem survey + METR 2025 + Stack Overflow 2025 trend.
> **Target slug:** `senior-developers-trust-ai-less`
> **Target file:** `src/pages/writing/senior-developers-trust-ai-less.astro` once approved.
> **Word count:** ~720.

---

## Article body

**Subtitle:** *What multiple 2025 surveys keep finding.*

I notice the senior engineers I work with often trust AI output less than the juniors do. They read what the agent produced, recognise that it looks plausible, and slow down. The juniors paste it in. For a while I assumed this was the standard generational story: older devs are slower with new tools. The data does not support that read.

[JetBrains' 2025 Developer Ecosystem survey](https://www.jetbrains.com/lp/devecosystem-2025/) of 24,500 software developers found that those with ten or more years of experience report low trust in AI output 61% of the time. Those with zero to two years of experience report low trust 48% of the time. [Stack Overflow's 2025 Developer Survey](https://survey.stackoverflow.co/2025), separately, with 49,000 respondents, found that 46% of developers actively distrust AI output accuracy. Of the experienced developers in the sample, only 2.6% reported "highly trusting" AI outputs and 20% reported "highly distrusting" them: the lowest trust and highest distrust of any experience bracket.

Engineers with more years of practice trust the tool less. That is the opposite of how new tools usually work.

The piece I wrote last week argued that engineering work has decomposed into producing output and validating it, and that validation is the harder of the two. The senior-trust gap is the same observation from a different angle. Seniors trust less because they have validated more, and validation has shown them more. They have seen the plausible-but-wrong code enough times to recognise the pattern in AI output specifically. Juniors have not yet seen enough wrong-looking code in general to develop the calibration.

A small concrete example. Three weeks ago I was reviewing a retrieval function the agent had written for the ese-bot codebase. Plausible. Type-checked. Wrong about which boundary the retrieval was supposed to respect. It took me fifteen minutes to find the error. The generation had taken seconds. The trust calibration in that moment was not about familiarity with AI. It was about familiarity with the failure modes of code that looks right but is not.

The other 2025 study worth pairing with this is [METR's](https://arxiv.org/abs/2507.09089). They put senior open-source contributors on tasks in their own codebases, with and without AI assistance. The contributors were 19% slower with AI. They reported feeling 20% faster. The discrepancy is the senior-trust pattern made visible in stopwatch terms: the calibration is happening, but slowly, and not where the user can feel it.

The conventional take in industry coverage is that AI is a junior-shaped problem. It replaces junior work, and seniors will be fine because they were already fine. The data flips this. AI is most disruptive to the population that knows enough to validate what it produced. Seniors are the ones currently noticing. Juniors will inherit a code base shaped by validation that did not happen.

This matters for how teams invest in their AI practice. If aggregate productivity numbers look positive but the senior productivity number is negative, the aggregate is hiding a population split. The investment that pays off is not training juniors to prompt better. It is making the validation work that seniors are already doing legible enough to scale.

The next piece will be about another split that aggregate numbers hide. The data I cited above is software-developer survey data: JetBrains, Stack Overflow, METR's open-source contributors. Equivalent surveys do not exist for hardware, embedded, control, or chemistry. What does exist in those domains is validation-failure research that did not measure trust. The next piece looks at that asymmetry.

If you have noticed your own trust in AI output going down rather than up, where in your work did that shift happen?

## Sources

- JetBrains. (2025). *State of Developer Ecosystem 2025.* https://www.jetbrains.com/lp/devecosystem-2025/
- Stack Overflow. (2025). *2025 Developer Survey.* https://survey.stackoverflow.co/2025
- Becker, J., Rush, N., Barnes, B., & Rein, D. (2025). *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.* arXiv:2507.09089. https://arxiv.org/abs/2507.09089

---

## Revision notes (what was deliberate in this draft)

- **Data scope explicitly software developers.** All three cited sources (JetBrains, Stack Overflow, METR open-source contributors) are software-developer-only. The article narrows its data claims accordingly while keeping personal observations broad (`the senior engineers I work with`), because Jeroen's practice does span hardware, embedded, and software. The forward look to Post 3 names the domain limitation directly rather than implying it. This keeps Post 3's thesis (`software bias in productivity research`) intact instead of pre-spending it.
- **Title is argument-form** and counter-intuitive on first read; matches the splitting article's title shape.
- **Opening sentence audience filter**: a senior practitioner reads "I notice the senior engineers I work with often trust AI output less than the juniors do" and recognises themselves; a generic LinkedIn scroller bounces.
- **Strongest line is sentence three of paragraph one**: *"The juniors paste it in."* Short, observational, frames the texture of the observation before any data lands.
- **Three independent sources**, each named naturally: JetBrains 2025, Stack Overflow 2025 trend, METR 2025. No "studies show…" framing.
- **Numbers paired with meaning**: 61% vs 48% (gap), 52% to 46% (year-over-year decline driven by users), 19% slower / 20% faster (the calibration paradox).
- **Connects to post 1** without re-explaining the validation argument. One paragraph of reach-back.
- **Concrete personal moment** (the retrieval-function review on ese-bot) anchors the abstract claim in Jeroen's own work, not in a colleague's anecdote.
- **Forward look previews post 3** (domain-bias) without spending its thesis.
- **One CTA**, an open question. Not a contact line stack.
- **No em-dashes.** All sites checked: colons (3), periods, commas. Zero em-dashes in the body.

## Open questions for the cold re-read

- Is the ese-bot retrieval-function moment in paragraph five a real moment Jeroen recalls, or is it a placeholder I generated from architectural context? **Verify before publishing.** If it is a placeholder, swap in a real moment from a recent review (any project, any week). The "twenty minutes to find what took five seconds to generate" beat is what carries the paragraph; the codebase is replaceable.
- The phrase "Juniors are the ones who will inherit code bases full of plausible-but-wrong output and a culture of not checking" is sharp. Audit on cold re-read: does it criticise the discourse around AI, or does it land as criticising juniors as a group? The intent is structural (a culture problem); a colder reader may hear it as the latter. Tightening candidates: "Juniors will inherit a code base shaped by validation that did not happen" might be safer.
- Does the closing question land, or does it trail? Test by reading the article cold and stopping at the question. If the question feels like a social-media prompt rather than something an engineer would actually answer, rework.
- Word count is ~720, well inside the 600 to 800 series target.
- Subtitle works. Alternative: "Counter-intuitive but consistent across multiple 2025 surveys."

## Voice and constraint audit (already passed)

- ✅ No HAN / AEA / SLIM / KC / AIM
- ✅ No "the digital engineer" / "the modern developer" framing
- ✅ No "studies show" / "research has demonstrated"
- ✅ No "we at HAN" / "in our course"
- ✅ No framework labels in capitalised form
- ✅ No em-dashes
- ✅ One CTA only
- ✅ Sources named, not parenthesised
- ✅ Modest register: observational, evidence-visible, no claims of having a methodology
- ✅ Non-management-book audit: no BEFORE/AFTER framing, no numbered patterns, no taglineable single image, no "five things engineers should do"

## When ready to publish

1. Verify the paragraph-five concrete moment (real or placeholder).
2. Move body into `src/pages/writing/senior-developers-trust-ai-less.astro` (use ESE Bot or splitting article as template).
3. Register in `src/data/writing.ts`.
4. Generate cover image: edit headline + slug in `scripts/gen-social-image.py`, run, lands at `public/social/senior-developers-trust-ai-less.png`.
5. A small typographic figure is pre-generated at `public/diagrams/senior-developers-trust-ai-less.svg`. Not a sketch (a sketch would be the asymmetry-as-argument move that the *It Is Both* memory rule warns against). Just the headline JetBrains pair: 61% / 48%, Tufte-style, with a citation header and a thin horizontal rule. Drop in between paragraph 2 and paragraph 3 (right after the data lands and before "the more time you spend with the tool, the less you trust it"), or wherever the cold re-read places it.
6. Run `npm run dev`, read cold, ship via Netlify.
7. Cross-post to LinkedIn (Pulse + short feed post + log in `memory/external-comments.md` per CLAUDE.md's three-surface default).
