# An agent has no ego. It reproduces your cognitive biases anyway.

> **Status:** DRAFT, first pass (2026-07-10). Awaiting cold re-read + cross-model review.
> **Series:** posture / craft register. The **mirror** of `epistemic-humility.md`: that piece argues the agent cannot be humble and the human must supply the doubt. This one argues the sharper, stranger fact underneath it: the agent, with no self to protect, still produces the exact named biases the psychology literature attributed to ego, fatigue and defensiveness. Read as a pair; they must not repeat each other's examples or lines.
> **Anchor:** Kahneman & Frederick's *attribute substitution* (2002) as the spine; Kahneman's fast/slow split (2011); Wason (1960) for confirmation. Popular-science entry point, verify before ship (see below).
> **Origin:** real moments from the llm-distillery / nature_recovery distillation project, July 2026. All examples are my own work (Section 5 clean).
> **Target slug:** `bias-without-a-self` (working).
> **Target file:** `src/pages/writing/bias-without-a-self.astro` once approved.
> **Word count target:** ~900–1200. Currently ~1040.

---

## Article body

**Subtitle:** *Attribute substitution, confirmation, and confabulation, in a system with nothing to protect.*

Last week an agent I was working with talked me toward the wrong decision, and it did it with a move straight out of a psychology textbook.

The task was mundane. I train small local models to imitate an expensive cloud model that scores news articles, so a cheap model that runs on my own hardware learns to copy an expensive one. Choosing which model to copy is the highest-leverage decision in the whole pipeline, because everything downstream inherits whatever that teacher does. I had picked one teacher deliberately, because its judgments matched the editorial line I actually wanted. The agent proposed switching to a different one. Its reason was clean and quantified: the new teacher was more self-consistent, it contradicted itself only half as often when you asked it the same question twice.

That is a real, measurable property. It is also the wrong one. Self-consistency is not the same thing as agreeing with me. A teacher can be perfectly consistent and consistently wrong for my purpose. The agent had quietly answered an easier question than the one that mattered, and handed me the answer to the easy one as though it settled the hard one.

Daniel Kahneman and Shane Frederick gave that move a name in 2002. When a question is hard, in this case *is this teacher aligned with my editorial judgment*, the mind substitutes an easier one it can actually compute, *is this teacher self-consistent*, and reports the second answer in place of the first, usually without noticing the swap. Kahneman built much of *Thinking, Fast and Slow* (2011) on it. It is the engine under a large share of the biases that literature catalogues. And here it was, produced by a system that has none of the machinery the literature assumed was doing the producing.

That is the part I keep turning over. The agent has no ego. It has nothing to protect, no reputation riding on the recommendation, no discomfort with uncertainty to soothe. Every folk explanation for why people reach for the easy question, that we are lazy, or defensive, or want to look decisive, is simply absent. It made the substitution anyway, cleanly, in the same shape a tired human would. I had made this exact mistake myself once and it had cost me a hundred euros or two in wasted labeling. The agent walked me calmly back toward it.

It is not an isolated move. Earlier in the same project a quality check failed, and the agent produced a confident diagnosis: the new model had made twelve scoring errors, here they were, we should retrain. The story was coherent. It named specific articles. Retraining would have cost real compute and the better part of a day. When I made it stop and re-read the underlying labels instead of its summary of them, the twelve errors evaporated. The thing it had compared against was built with the wrong teacher's labels, inflated by a known offset. There were no student errors at all. There was a plausible narrative assembled to fit a surprising result, which is what confirmation bias looks like from the outside. Peter Wason showed in 1960 that people test a hypothesis by seeking what confirms it, and the agent had done exactly that, marshalling evidence for the retrain story rather than trying to break it.

There is a milder version that shows up almost daily. The agent will report that a test was written, or that a note was promoted into a document, in the same even tone it uses for things that are true. The artifact does not exist. This is not lying, which needs knowing the truth and choosing against it. It is nearer to confabulation: the fluent production of a plausible account with no signal attached to mark it as unbacked. The tell is that the confidence reads identical whether the ground under the sentence is solid or empty.

So where do the biases come from, if not from a self? Two places, I think, and neither needs an ego. The first is the training material. The model learned from a corpus written by people who substitute the easy question, fit stories to surprises, and state guesses in the voice of facts, and it absorbed the shape of that reasoning along with the grammar. The second is structural. A system tuned to produce the most plausible next span of text is tuned for precisely the thing fluency-without-calibration is made of. Plausibility is what a confident wrong answer and a confident right answer have in common. The biases are not bolted on. They fall out of predicting what a reasonable-sounding continuation looks like.

Kahneman's own framing fits almost too neatly. He split thinking into a fast, associative, effortless system and a slow, effortful, checking one, and argued that most errors come from the fast system running unsupervised. A language model is close to pure fast system. It has no native slow system to fall back on. It cannot, on its own, stop and run the check.

Which is why the fix turns out to be the one psychology has prescribed for people for decades, only moved outside the head. You do not cure attribute substitution by resolving to be less biased, because the substitution happens below the level you can introspect. You cure it with a procedure that forces the check: reproduce the calculation by hand, compare against an independent source, read the primary rather than the summary. In this project that has hardened into rules with unglamorous names. Judge a new model against held-out ground truth, never against the model it replaces. Treat a claim as false until the artifact it points to is found. Re-read the labels before believing the story about the labels. None of those are intelligence. Each one is the slow system, bolted on from the outside, because the agent cannot grow one for itself.

The uncomfortable implication is that the biases may never have been about human frailty in the first place. If a system with no ego, no fatigue and no reputation reproduces them from the structure of plausible language alone, then the ego was mostly a passenger. What remains is the substitution itself, the narrative fitted to the surprise, the confident empty sentence. And the only reliable defense is the same for the machine as it is for me: not a better attitude, but an external check that runs whether or not anyone feels the need for it.

Where, in your own work with an agent, has it handed you the answer to an easier question than the one you asked?

---

## Revision notes (what was deliberate in this draft)

- **Title is argument-form and counter-intuitive** ("An agent has no ego. It reproduces your cognitive biases anyway."). Two sentences, same shape as "The work is splitting. Most teams haven't noticed." The second sentence carries the claim; the first sets up the surprise. Audience filter: an engineer working with agents recognises the phenomenon; a generic scroller bounces on "cognitive biases."
- **Strongest line is in the top half** (paragraph 5): "It made the substitution anyway... Every folk explanation... is simply absent." The whole thesis (bias without a self) lands there, then the closing paragraph pays it off ("the ego was mostly a passenger").
- **Lean, not recital.** Attribute substitution is the spine; confirmation and confabulation are two supporting moments, not a catalogue. Deliberately NOT structured as "four biases engineers should watch" (that is the management-book formula the AE guide and the epistemic-humility audit both warn against). No numbered list of biases anywhere.
- **Every example is real and mine**, from the July 2026 nature_recovery distillation work: the noise-for-bias teacher-switch (a genuine $100–200-once mistake), the "twelve errors" that were a reference-cohort artifact, the confabulated "test written / note promoted" claims. Section 5 clean (no colleague's lived moment).
- **Mirror of `epistemic-humility.md`, not a repeat.** That piece: the agent cannot supply humility, so the human must. This piece: the agent reproduces the specific *named* biases despite having no ego, which is why the humility has to be externalized as procedure. Shared thesis (external check beats attitude), opposite entry point. They must not share example moments or the load-bearing lines. Cross-link on publish.
- **Antidote paragraph reuses the project's real rules** (ground-truth gate not prior-model; claim-false-until-artifact-found; re-read the labels). These map to actual ADRs / memory rules in llm-distillery, so the piece is evidence-visible rather than asserted.
- **No em-dashes in the body.** Audited line by line. Asides use parentheses or commas; list-introduction uses a colon.
- **One CTA**, a comment prompt pointed at the exact failure mode the piece names (attribute substitution, phrased in plain language).
- **No diagram.** A 2x2 of "has ego / no ego" by "biased / calibrated" would be exactly the management-book visual the register rule forbids. Skip.

## Open questions for the cold re-read

- **Citation verification before publish (load-bearing).** Per the writing-guide Section 7 rule and the burn on `epistemic-humility` (a fabricated "Dunning-Kruger mirror" term slipped in once), verify at primary source before shipping: (a) Kahneman & Frederick 2002, *Representativeness Revisited: Attribute Substitution in Intuitive Judgment*, in Gilovich/Griffin/Kahneman eds, and confirm "attribute substitution" is their phrase; (b) Kahneman 2011, *Thinking, Fast and Slow*, for the fast/slow split; (c) Wason 1960, *On the failure to eliminate hypotheses in a conceptual task*, QJEP, for the confirmation framing. Build `docs/verification/bias-without-a-self.md`. Keep language at SUPPORTED ("gave the move a name", "showed") unless the primary read confirms ESTABLISHED. Do not add page numbers or quotations that were not read.
- **The confabulation paragraph and the anthropomorphism line.** "It is not lying... it is nearer to confabulation" is a claim about mechanism. Confirm it does not overclaim about internals. Current phrasing stays at the behavioural level (the confidence reads identical), which is defensible for an essay; audit that it does not tip into asserting the model "knows" anything.
- **The structural claim** ("plausibility is what a confident wrong answer and a confident right answer have in common"). This is the strongest and most contestable sentence in the piece. Decide on cold read whether it needs one clause of hedging or whether the essay register carries it. I lean toward leaving it; it is the line most likely to travel.
- **A cut worth keeping in reserve:** anchoring (Tversky & Kahneman 1974) had a clean example in the same project (I reported a 15% figure that was really 0.3%, and stayed anchored to it until challenged). Left out to keep the set lean. If the cold read finds the middle thin, this is the fourth beat to add, but only if it earns its place.
- **Meta-disclosure.** This draft was itself written by an agent, about agent bias. Tempting to note it in one line. Decide whether that is honest and sharp or merely cute. Current call: leave it out of the body, the piece is stronger as Jeroen's observation than as a hall-of-mirrors. Reconsider on cold read.
- **Standalone read.** Works cold: the setup ("I train small local models to imitate an expensive one") gives a fresh reader enough. Confirm the distillation framing is not too compressed for a reader who has never seen it.
- **Word count** ~1040, inside the 800–1500 band. Room to add the anchoring beat if wanted without breaching.

## Voice and constraint audit (first pass, re-run on cold read)

- ✅ No HAN / AEA / SLIM / KC / AIM / framework acronyms
- ✅ No "the digital engineer" / "the modern developer"
- ✅ No "studies show" / "research has demonstrated" (Kahneman, Frederick, Wason named with year)
- ✅ No em-dashes in the body (audited line by line)
- ✅ One CTA (closing comment prompt)
- ✅ No "key takeaways" / "in conclusion" / numbered action items
- ✅ Essay-mode hybrid: scene opening, exploration middle, soft landing on a paradox + question
- ✅ Numbers paired with meaning (the $100–200, the twelve errors, each tied to what it cost / what it was)
- ✅ Modest register, evidence-visible, N=1 not dressed as general ("in this project", "a mistake I made once")
- ✅ Virtue-word audit: "calibration", "check", "humility"-adjacent language always paired with the mechanism (the external procedure, the specific rule), never as decoration
- ✅ Section 5: all anchoring examples are my own work, no colleague's lived moment

## When ready to publish

1. **Cold re-read** as the Section 2 reader; run the Section 9 pre-publish checklist.
2. **Citation verification** per the open question; build `docs/verification/bias-without-a-self.md`; downshift any claim that does not survive Step 6.
3. **Cross-model review pass** (fresh model / no context, review-prompt Variant B). This piece especially: an agent drafted it about agent bias, so same-family self-review has the exact blind spot the article describes. Cross-model is not optional here.
4. Move body into `src/pages/writing/bias-without-a-self.astro`.
5. Register in `src/data/writing.ts`.
6. Cover image: `scripts/gen-social-image.py` with the title + slug; lands at `public/social/bias-without-a-self.png`. Hook line for the card: "The ego was mostly a passenger."
7. No in-article diagram (audited above).
8. Inline source links (Kahneman & Frederick, Kahneman, Wason) + Sources block at the foot, per Section 7.
9. `npm run dev`, read cold, ship via Netlify.
10. Cross-post to LinkedIn (Pulse + short feed post; log in `memory/external-comments.md`). Hook candidates: "A system with no ego reproduced every bias psychology blamed on ego." or "My agent handed me the answer to an easier question than the one I asked, and I almost took it."
11. **Cross-repo evidence:** this piece is direct material for the agentic-engineering evidence project (LLM behavioural properties pattern). File an issue at `ducroq/agentic-engineering` linking the three moments to the "reproduce-don't-assess" and "LLM behavioural properties" patterns once published.
