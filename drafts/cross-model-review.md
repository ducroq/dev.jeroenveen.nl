# The same model that wrote it cannot catch its own errors.

*Status: DRAFT first-pass prose, written 2026-06-01 from earlier seed (2026-05-12). Reception-checkpoint pending on `verification-is-a-workflow-problem` (published 2026-06-01, posts to LinkedIn 2026-06-02) before deciding publish timing. Sibling to that article, which uses the multi-pass review pattern as one of three workflow properties; this piece goes deep on the multi-pass component specifically. Two-axes-of-outside-ness beat added 2026-06-02 after today's IOU verification against `new_hardware/vv/` surfaced the gap; see also gotcha-log 2026-04-28 (sub-agent sandbox).*

*Working subtitle:* Notes from a three-pass review.

---

## Draft

Three reviewers ran across the same draft. Each caught a different class of problem. The most expensive of the three caught nothing I could use.

The reviewers were a small same-family model running a mechanical checklist, a large same-family model in a fresh session running an argument-shape critique, and a different vendor's model running a voice-and-tone pass with my house-style rules attached.

The mechanical pass surfaced rule compliance issues: phrasing that violated the writing guide's specific rules. Fast pass, narrow scope, immediate actionable list.

The argument-shape pass surfaced different things entirely. Paragraphs where the logic of the claim was weaker than its prose. Spots where the supporting evidence did not quite carry the load. Places where the conclusion outran what the body actually established.

The cross-vendor pass caught seven house-style violations that the previous two passes had missed. Of those seven, exactly zero were actionable. Every single one was either a stylistic preference the cross-vendor model would not recognise as a rule, or a voice convention specific enough to this site that no general-purpose reviewer would flag.

That is the finding worth thinking about. Each pass caught what only that pass could catch. And the most expensive pass, the cross-vendor one with its different training distribution and different stylistic priors, produced exactly zero usable corrections on a piece of voice-sensitive prose.

The structural insight is straightforward. A reviewer escapes the bias of the producer to the extent that it has different priors. A model from the same family shares enough of the producer's training distribution that it will accept assumptions the producer made by inheritance. Running the same family twice helps a little: fresh-session bias clears, the new instance reads with different mood and depth. Running a different family helps differently: the cross-vendor reviewer breaks out of a wider class of shared assumption, which catches a different kind of error.

But "different kind of error" is where the cost-benefit gets sharp. Cross-vendor review surfaces stance-shaped errors more reliably. Those are the assumptions, framings, and unspoken positions that the producer's training distribution baked in. It does not surface knowledge-shaped errors more reliably; those tend to come from the same evidence base regardless of model family. And it actively introduces noise on voice-sensitive material, where the cross-vendor reviewer has no way to distinguish house style from violation of general writing convention.

The naive version of the multi-model review advice says: use a different model to check your AI output, because a different model will catch what the original missed. That advice is right about the catching, and silent on what gets caught. For knowledge-shaped output, citations, factual claims, technical accuracy, cross-vendor review pays off cheaply. For stance-shaped output, essays, opinion pieces, anything with voice, cross-vendor review catches what the producer wrote on purpose and complains about it.

The pattern I have landed on is more discriminating. The two intra-family passes, mechanical plus argument-shape, run on every publish. They are cheap and they catch the classes of error the producer is most likely to miss for plain reasons. The cross-vendor pass runs only when the stakes warrant the noise: high-stakes claims, citation-heavy passages, anything where the cost of a missed error exceeds the cost of filtering false alarms. And when it runs, the house-style rules go with it as an explicit filter, so the cross-vendor reviewer's stylistic disagreements get categorised as out of scope before they reach the actionable list.

The validator inherits the implementation's assumptions. That is true at the model-family level. It is also true at the prompt level and the rubric level. A reviewer prompted by the producer, against criteria the producer wrote, will inherit a lot more than just the producer's family. It will inherit the producer's beliefs about what counts as a problem. Multi-pass review is most useful when the passes disagree about that.

It is also true at the context level, which is where multi-pass review hits a structural ceiling. A reviewer can be outside the drafting context (different model, fresh session, no carry-over) and still be inside the producer's filesystem reach. When the claim being verified lives in a sibling project, say a measurement record or source artefact in a separate repo, pasting that content into the reviewer's context loops the producer's selection back in. The producer chose what to paste; the reviewer reads what was chosen.

The honest verification move for cross-repo claims is to do the comparison in the session that has reach to both the article and the source, not in a downstream reviewer that has reach to only the article. Outside-ness has two axes. Multi-pass review handles the first: the producer wrote the draft and a different model reads it. It does not handle the second: the reviewer cannot reach the artefact the draft makes claims about.

What three reviewers showed me, in the article we ran them on, was that they disagreed in distinct ways. The mechanical pass disagreed with the producer about rule compliance. The argument-shape pass disagreed about logic. The cross-vendor pass disagreed about voice, and that disagreement was the one I needed to discount most carefully.

The advice that travels: match the pass to the failure mode you are trying to escape. Cheap passes for cheap escapes. Expensive passes only when the failure mode justifies the noise filtering.

Where has cross-vendor review paid off for you, and where has it produced mostly noise?

---

## Reference: DR-011 three-pass structure (for revision)

agent-ready-papers DR-011 names a multi-model review pattern with three passes that each escape a distinct bias:

| Pass | Escape mechanism | When |
|---|---|---|
| Pass 1: intra-family small | sunk-cost from the session that built the draft | every publish |
| Pass 2: intra-family large | different review character / depth | every major revision |
| Pass 3: cross-vendor | training and stylistic priors | high-stakes only, with mandatory style filter |

The senior-trust article (post 2 of the WHY arc) was the first project here to run the pattern empirically (logged in `memory/external-comments.md` 2026-05-12 publish entry):

- Haiku review surfaced rule-compliance issues
- Opus review surfaced argument-shape issues
- Gemini cross-vendor review surfaced voice-rule violations (after voice-rule filter, net actionable findings: 0)

The draft above uses the senior-trust review pass as its empirical anchor without naming the specific models. Decide at revision time whether to name them.

---

## Open questions before publish

- **DR-011 source verification.** The three-pass language above is paraphrased from the agent-ready-papers README and the seed note, not from the DR itself. Before publish, read `decisions/DR-011_multi-model-review-pattern.md` directly so the three-pass structure and the language are not laundered through summary. The README's framework-overview style smooths edges that a DR may keep sharp.
- **Disclosure of review numbers.** The draft uses qualitative descriptions ("seven house-style violations," "zero actionable") drawn from the senior-trust review. Are these numbers publishable as written, or do they belong only in the verification record? The article is sharper with the concrete count. Needs Jeroen's call on disclosure.
- **Naming the models.** The draft anonymises ("small same-family", "large same-family", "different vendor"). The seed proposed naming Haiku / Opus / Gemini. Anonymisation matches the register of the verification article; naming would add specificity at the cost of pinning the piece to a model lineup that will change. Decision at revision time.
- **Reception checkpoint.** Verification-is-a-workflow-problem ships to LinkedIn 2026-06-02. Check reception at 5–7 days. If the workflow-vs-model frame travels (saves, reposts, frame-adoption signals), this piece becomes the natural deeper sibling. If it does not, the cross-vendor angle may need recasting.

## Notes for revision pass

- **Strongest line.** The opening triplet ("Three reviewers ran across the same draft. Each caught a different class of problem. The most expensive of the three caught nothing I could use.") is the strongest passage in the piece, and the third sentence is the hook. Lead with it on LinkedIn cross-post.
- **Reusable phrasings worth preserving through revision:**
  - *"Cross-vendor review is the right pass for some content classes and the wrong pass for others."* (from the seed; not directly in the draft, but the idea is, and the phrasing is sharper than what made it in)
  - *"The validator inherits the implementation's assumptions."* (in the draft, mid-body)
  - *"Stance-shaped errors and knowledge-shaped errors require different reviewers."* (from the Geert thread; the draft uses the distinction without coining the phrase, worth pulling forward)
  - *"Match the pass to the failure mode you are trying to escape."* (closing line, candidate for subtitle or LinkedIn hook)
  - *"Outside-ness has two axes. Multi-pass review handles the first, not the second."* (added 2026-06-02; structural ceiling beat. Candidate for the LinkedIn cross-post hook if the workflow-piece reception suggests appetite for a deeper sibling.)
- **Possible homes:**
  - **dev.jeroenveen.nl article (current draft target).** Sibling to verification-is-a-workflow-problem. Cost: narrower audience than the parent article; pays off when the parent frame has traveled.
  - **AE pattern essay.** This is genuinely AE territory; it is the *mitigation* recipe for the validation-inherits-implementation-assumptions failure mode. Could live on the AE site as a pattern note linking to DR-011. The dev.jeroenveen.nl article would point to it.
  - **Short LinkedIn post (teaser).** The opening triplet compresses cleanly: *"Three reviewers ran across the same draft. Each caught a different class of problem. The most expensive of the three caught nothing I could use."* Could serve as a teaser if the moment comes before the long-form is ready.
- **Word count, current draft:** ~770 words. Within the 800–1500 target band per writing-guide §3, on the short end. Acceptable for a single-conviction piece. Adding the named-models specifics or the Geert-thread stance-vs-knowledge framing would lengthen toward the middle of the band.
- **Em-dash audit:** zero em-dashes in the draft body. Re-check after revisions.
