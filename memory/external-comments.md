# External Comments Log

Reactions and replies posted on LinkedIn or other external platforms. Captured here so we can revisit framing, track which threads we've engaged with, and reuse phrasings later.

## 2026-04-29 — Reply to Witek ten Hove on spec-driven assessment

**Context:** Witek posted on LinkedIn (28 April 2026) framing AI's assessment shift in education using Karpathy's "software 3.0" analogy. Students submit a specification, the AI generates the artifact, and the artifact becomes a "wegwerpartefact". The rubric shifts to: are assumptions explicit, are alternatives weighed, is the scope right, is the problem understood. He posed three questions about what this means at the level of beroepsproduct, docentschap, and opleiding.

**Reply posted (mix of Reproduce-Don't-Assess and voorzichtig tegendraads on "wegwerpartefact"):**

> Eens met de richting, Witek. In eigen werk zien we vaker dat AI-agents een berekening 'fysisch correct' verklaren waar reproductie alsnog fouten oplevert. Dat maakt me voorzichtig met "wegwerpartefact": voor code die je goedkoop kunt regenereren klopt het, maar voor embedded firmware die één keer geflasht wordt, gecertificeerde medische of automotive software, etc. is de implementatie zelf het contract, en dat was nu net wat het V-model probeerde te ondervangen. De student-vraag van morgen lijkt me dus dubbel: kan ze de spec verantwoorden, én aantonen dat de gegenereerde uitkomst eraan voldoet?

**What this draws on:**
- Augmented Engineering pattern: Reproduce, Don't Assess (driven-pendulum case: 68 equations, two LLMs found zero errors, reproduction caught three)
- vmodel.eu: V-model framing, requirements as artifact-not-throwaway
- Domain pushback: embedded firmware, certified medical/automotive software, numerical implementations — domains where the implementation is the contract, not a throwaway

**Why this framing:** Witek is a friend in the same Dutch AI-onderwijs space, not a debate opponent. Goal was to add a dimension (validation of output) without overwriting his three questions, and to gently complicate the "wegwerpartefact" analogy without dismissing it. The V-model reference is a subtle nod to vmodel.eu work that Witek can pick up if he wants to follow the thread.

**Iterations the comment went through (for future reuse):**
- A: short, plain "validation matters" addition — too generic
- B: SER-2025 / Digital Engineers framing — too research-paper for a comment
- C: full Reproduce-Don't-Assess case with numbers (68/0/3, factor 5) — too many specifics for a comment
- D: tegendraads on "wegwerpartefact" — risk of reading as correction to a friend
- E (final, mix of C+D): empirical pattern in one line + voorzichtige nuance + domain examples + V-model + dual student-vraag closing

---

## 2026-04-21 — Publish: "A small GDPR-safe chatbot" (ese-bot)

**Surfaces shipped (all three live):**
- Short LinkedIn post (link share): https://www.linkedin.com/posts/jeroen-veen-3244444_a-year-ago-my-honest-answer-to-is-there-activity-7452614482687819776-vp4V
- LinkedIn Pulse (long-form): https://www.linkedin.com/pulse/small-gdpr-safe-chatbot-jeroen-veen-sotoe/
- Canonical home: https://dev.jeroenveen.nl/writing/ese-bot-eu-sovereign-rag/

**Posted short-post body (full, captured 2026-05-10, confirmed complete by Jeroen 2026-05-11):**

> A year ago my honest answer to "is there a European alternative?" was "not really." Today it is "yes, probably, depending on your horizon."
>
> Notes from running a small GDPR-safe chatbot for my students, one year in.

The auto-card under the hook links to the Pulse article ("A small GDPR-safe chatbot"). No additional hashtags or closing prompt. At first fetch (2026-05-10): 29 reactions, 2 comments (Rudie Van Den Heuvel, Casper T.).

**Full Pulse article body:** captured at `memory/posted-linkedin/ese-bot-eu-sovereign-rag.md` (supplied by Jeroen 2026-05-11 from the live Pulse URL).

**Notes:**
- Logged retroactively (URLs supplied 2026-05-10, full bodies supplied 2026-05-11). Strategy notes from publish-time were not captured.
- The published version reframed substantially from the original short-post draft, which opened "Last year I built a RAG chatbot for my students." That draft (formerly at `drafts/linkedin-post-ese-bot-unpublished.md`) has been retired. The European-alternative framing in the live post is the canonical record.

**Phrasing worth reusing:**
- *"A year ago my honest answer to '[X]?' was 'not really.' Today it is 'yes, probably, depending on your horizon.'"* — durable opener structure for tracking shifts in capability or availability over time. The "depending on your horizon" hedge does real work: it concedes that "yes" isn't unconditional without retreating to "no."

---

## 2026-05-01 — Publish: "The work is splitting" (post 1 of 3 in WHY arc)

**Surfaces shipped (all three live):**
- Short LinkedIn post (link share): https://www.linkedin.com/posts/jeroen-veen-3244444_ai-developerproductivity-augmentedengineering-ugcPost-7455865870616244224-Dp9C
- LinkedIn Pulse (long-form): https://www.linkedin.com/pulse/work-splitting-conversations-havent-caught-up-jeroen-veen-kcnne/
- Canonical home: https://dev.jeroenveen.nl/writing/the-work-is-splitting/

**Strategy choices (worth re-examining after data comes in):**
- Both LinkedIn surfaces, not post-only. Site too young to outrank a Pulse copy on Google, so SEO purity was deliberately traded for LinkedIn reach.
- Title revised pre-publish from "Most teams haven't noticed" to "The conversations haven't caught up." Same argument-form rhythm; criticism shifted from teams (implicating the reader) to public discourse (impersonal).
- Cover image typographic, dark + amber, quotes the body's strongest line ("Production is now cheap and fast. Validation is not."), not the title. Generated by `scripts/gen-social-image.py` (reusable for future posts).
- Hashtags: #AI #DeveloperProductivity #AugmentedEngineering. Three only. #AugmentedEngineering planted as a positioning tag to be reused across the arc.

**To revisit in ~5–7 days (gives the algorithm time to settle):**
- Reactions and comments on each surface separately. Did Pulse out-reach the short post or vice versa? Answers whether to repeat the both-surfaces strategy on posts 2 and 3.
- Did the closing prompt ("Where in your work has validation become heavier than production?") draw specific, domain-named replies (audience filter worked) or generic "interesting!" reactions (it didn't)?
- Reshare patterns. Who reshared, what context they added. Anyone we should engage with directly?
- Any phrasings from comments worth reusing in posts 2 (JetBrains senior-trust data) and 3 (HAZOP / domain bias).
- If the validation-vs-production framing landed, post 2 can build on it directly without re-explaining; if it didn't, posts 2 and 3 need more independent framing of their own.

---

## 2026-05-03 — Reply to Witek on "tests in the context" (follow-up to WHY post 1)

**Context:** Witek replied (under the WHY post 1 thread, "The work is splitting") raising "tests in the context" as a counter / mitigation: that having tests alongside the code in the agent's context narrows the gap between generated output and correct output.

**Reply posted:**

> Fair, with one caveat. Tests in the context help, but the gap between "passes the suite" and "is correct" predates AI. What AI changes is the leverage on that gap. Two shifts. One: production is cheap now, so test-passing-but-incorrect output is generated at much higher rates than humans ever could. Two: if the same agent writes the code and proposes the tests, "tests in the context" stops being an independent check; the validator inherits the implementation's assumptions. So validation tests in the context, yes; keeping the validator independent of what is being validated, harder.

**Why this framing:**
- Concession-then-nuance ("Fair, with one caveat") preserves collegial tone. Witek is a friend, not a sparring partner; doesn't overwrite his point.
- Two-shift structure rather than one separates the *rate* problem (more wrong-but-passing artifacts per unit time) from the *independence* problem (single agent authoring both sides). These are distinct failure modes and both matter.
- Closing aphorism deliberately mirrors the "Production is cheap. Validation is not." rhythm from the article: parallel "yes, ... harder" structure. Reinforces the article's frame without repeating it verbatim.
- Stays inside the audience filter: anyone whose tests are written by the same agent that writes the code recognises the problem immediately; anyone for whom this is news isn't the target reader.

**Phrasings worth reusing:**
- "the validator inherits the implementation's assumptions": sharp one-liner, candidate for post 3 (HAZOP / domain bias) where the same dynamic shows up at the *requirements* layer (agent that elicits requirements also proposes the design that satisfies them).
- "test-passing-but-incorrect output is generated at much higher rates than humans ever could": concrete restatement of the production-cheap / validation-hard asymmetry, useful when the abstract framing doesn't land.
- "leverage on the gap": economical way to say "AI didn't create the problem, it amplified it." Reusable whenever someone says "but X predates AI."

**To watch for:**
- Whether Witek picks up the independence point or stays on the rate point. The independence problem (agent authoring both code and tests) is the harder of the two and the more useful thread to continue if he engages with it.
- If the exchange goes another round, this is approaching the territory of post 2 (JetBrains senior-trust data); at some point it's worth saying "I'm writing about exactly this, here's where it goes" rather than developing the argument privately in the comments.

---

## 2026-05-03 — Reply to Geert van Kollenburg on "Lazy prompting"

**Context:** Geert van Kollenburg (1st-degree connection, Co-founder/CTO Precubitus, Professor of Human-AI collaboration) posted on LinkedIn about "Lazy prompting", a method of using minimum-effort prompts to test what AI can and can't do. His worked example: posing a suggestive question about palm oil to Gemini Pro, where he already knew the answer (palm oil is the most efficient vegetable oil crop in the EU), to see whether the model would surface that critical evaluation. The post then generalised: "for everyday applications, try to be lazy. Don't put too much effort in, these tools should make your life easier."

**Reply posted (additive, not corrective):**

> Useful frame, Geert. One extension: when you don't have a known answer to check against, fire the same lazy question at two different models. Where they disagree is where the boundary you're probing tends to show up. Same lazy spirit, different check source.

**Why this framing:**
- Audience-relationship constraint dictated the move: Jeroen doesn't know Geert well, may need him in future, no rapport bank to spend on substantive public pushback.
- Add-don't-carve approach: extends his frame instead of dividing it into halves. The validation-independence point (two models = independent check sources) travels in without ever being named as a correction.
- Closing line "Same lazy spirit, different check source" reinforces his frame as the parent idea, not the target. Easy for him to like, build on, or share.

**The punchier version, NOT posted (saved for reuse if rapport allows or in adjacent future contexts):**

> Like the frame, Geert, with one distinction. Posing a lazy question and checking against ground truth you already have is more probe than shortcut: it works because you have somewhere independent to check. The generalisation to everyday use is a different claim. Without ground truth, lazy prompting doesn't make AI more useful; it just hides whether the answer is correct. The saving isn't in the prompt effort. It's having validation independent of the model. Generating is cheap now; verifying isn't.

**Why the punchier version was held back:**
- It does substantive disagreement in 75 words. Compression made the disagreement land harder than the same content at 200 words would.
- Two lines do most of the cutting: "doesn't make AI more useful; it just hides whether the answer is correct" reads as declaring his everyday-use advice misleading; "the saving isn't in the prompt effort" negates the headline takeaway of his post.
- Geert is a peer-with-standing (professor, CTO) and Jeroen has no relationship history with him to soften how a public carve-up would land. The collegial-pushback move worked with Witek (close friend) but the relationship asymmetry made it the wrong call here.

**Phrasings worth reusing from the held-back version:**
- "more probe than shortcut": useful any time someone calls a methodologically rigorous move "casual" or "lightweight."
- "Without ground truth, lazy prompting doesn't make AI more useful; it just hides whether the answer is correct": sharp condensed form of the validation asymmetry. Candidate for post 2 or 3 in the WHY arc, or for a context where direct framing is welcome (talk, internal doc, AE post).
- "Same lazy spirit, different check source": reusable parallel structure for "yes, and here's a sibling pattern" moves where you want to honour the original frame.

**Decision rule learned:**
- When relationship rapport is thin and the interlocutor named/coined the frame, default to add-don't-carve. Save the carve-version for: known peers who welcome it, or for first-person publishing where the analytical move is the point.

---

## 2026-05-04 — DRAFT (pending, not yet posted) — Reply to Geert van Kollenburg's "another model, or new instance" follow-up

**Context:** Geert replied to the 2026-05-03 thread above with: *"I generally ask another model, or at least a new instance, to validate the answer I get. Like in humans: it's much easier to criticize someone else's work than to produce new content :)"*. Friendly, additive, but the "or at least a new instance" caveat flattens a distinction that matters for the validation argument.

**Draft reply (to be posted by Jeroen, with possible edits):**

> Nice analogy. Worth pulling on: a different reviewer has different knowledge and blind spots, which is what makes the criticism useful. A fresh instance in critic mode catches things the original prompt missed (overlooked case, sloppy step), but can't see past the model's own blind spots. Closer to re-reading your own draft an hour later than to a colleague reviewing it. Both useful, different reach.

**Why this framing:**
- Add-don't-carve still applies (thin rapport with Geert; per `feedback_thin_rapport_add_dont_carve.md`).
- Honours his human analogy as the load-bearing device, then uses it to surface the distinction he flattened.
- Concedes that critic-mode prompts genuinely catch things (so the reply doesn't read as dismissive of his habit).
- Names the limit precisely: same model can't see past its own blind spots, regardless of prompt.
- "Closer to re-reading your own draft" / "than to a colleague reviewing it": concrete reframe, both familiar, both have value but they're not the same operation.
- "Both useful, different reach" closes warmly without negating his practice.

**Analytical refinement (came out of an internal pushback round):**
The first draft used "different priors / same priors" to frame the cross-model vs. same-model-new-instance distinction. That framing is imprecise: a different prompt does shift *something* (stance, what knowledge is foregrounded, role adopted), and "prior" can defensibly refer to that shift. The sharper distinction is by error class:
- **Stance-shaped errors** (overlooked case, sloppy reasoning step, ambiguous phrasing): same-model-different-prompt can catch these. Critic-mode prompts genuinely work for this class.
- **Knowledge-shaped errors** (hallucinated API, factual error baked into training, blind spot in the training distribution): same-model-different-prompt typically cannot catch these, because the gap is the same. A different model has different gaps and so different reach.

This split is sharper than "independence vs not" and worth keeping for future writing on validation independence.

**Phrasings worth reusing:**
- "stance-shaped errors / knowledge-shaped errors": clean two-bucket distinction for what same-model-different-prompt critique can and can't catch. Candidate for post 3 (HAZOP / domain bias) or for AE pattern writing on evaluator-optimizer / critic-actor.
- "Closer to re-reading your own draft an hour later than to a colleague reviewing it": concrete analogy that travels. Reusable any time someone proposes self-critique as a validation move.
- "Both useful, different reach": gracious closer for "yes, and here's a distinction" moves where you want to preserve the interlocutor's practice.

**To do once posted:**
- Promote this entry from DRAFT to a regular dated entry (drop the "pending" marker).
- Watch whether Geert engages with the stance-shaped vs. knowledge-shaped split. If he does, this thread is approaching post 2 / 3 territory and may be worth signalling redirect rather than continuing to refine privately.


---

## 2026-05-12 — Publish: "Senior developers trust AI less than juniors." (post 2 of 3 in WHY arc)

**Surfaces shipped (all three live):**
- Short LinkedIn post (link share): https://www.linkedin.com/posts/jeroen-veen-3244444_the-conventional-take-is-that-ai-replaces-activity-7459851440463904768-sPvM
- LinkedIn Pulse (long-form): https://www.linkedin.com/pulse/senior-developers-trust-ai-less-than-juniors-jeroen-veen-1biue/
- Canonical home: https://dev.jeroenveen.nl/writing/senior-developers-trust-ai-less/

**Strategy choices (worth re-examining after data comes in):**
- **Both surfaces** (Pulse + short feed post). Same as work-is-splitting. The site has a touch more authority now but is still young.
- **Subtitle rewritten pre-publish**: from "What multiple 2025 surveys keep finding." to "An observation from three developer surveys." (matches work-is-splitting register, drops year-stamping).
- **Punchline paragraph rewritten pre-publish** for the conventional-take-flip. Original was abstract ("AI is most disruptive to the population that knows enough to validate what it produced"); rewrote to functional ("Seniors are the ones currently absorbing the cost, because they do the validation: recognising what looks plausible but isn't, slowing down on each piece"). This was driven by Jeroen flagging the original didn't land conceptually on first read. Worth watching whether the rewrite improves comment quality vs. work-is-splitting's punchline.
- **Sketch figure** (vectorised junior/senior validation comparison) on the website article only; not embedded in Pulse (LinkedIn doesn't handle SVG cleanly, and the cover image at `public/social/senior-developers-trust-ai-less.png` carries the visual presence on the Pulse + feed-post-auto-card surfaces).
- **Hashtag set consistent with post 1**: `#AI #DeveloperProductivity #AugmentedEngineering`. Maintains series signal for the algorithm.

**Review trail (multi-model in-family review pattern applied for the first time):**
- Opus subagent review on the LinkedIn draft: 4.3/5.0, accept with minor revisions. Found subtitle drift and CTA pre-loading. Both fixed pre-publish.
- Haiku subagent review on the same draft: 4.3/5.0, accept with minor revisions. All hard rules pass. Two soft additions suggested (sample-scope clarity, METR N=16 parenthetical); neither applied.
- Gemini cross-vendor review on the short post: 4.56/5.0, accept. Most suggestions failed project voice rules (label-coining "Validation Tax", slogan "technical debt at the speed of light", subheading suggestion, chart suggestion, popular-psych reference); all filtered. Net actionable findings after voice-rule filter: 0.
- Empirical finding from this triple-review: intra-family multi-size review (Haiku for rule compliance, Opus for argument-shape) caught the substantive issues; cross-vendor review surfaced mostly voice-rule violations on this voice-sensitive content. Captured as `agent-ready-papers` issue #7 (DR-011 proposal: Multi-Model Review Pattern).

**To do (5-7 day check-in):**
- Compare reception against work-is-splitting (Pulse views, short-post reactions, comments).
- Watch the comment-prompt response rate. The closing question ("Where in your work did your trust in AI output shift?") is the tightened version of the original 23-word formulation; testing whether the 9-word neutral form earns better replies than the original directional form.
- Watch for "but seniors are slow adopters" responses. The article's paragraph 1 names that read; the response in comments is to point at METR's 19%-slower-with-AI finding (seniors who DO use AI are objectively slower, so their distrust matches measured reality, not generational lag).
- If the rewritten punchline paragraph performs well (clearer comments, more on-topic replies), promote the rewrite pattern: when a conceptual punchline depends on bridging abstractions, unpack to functional terms.

**Phrasing worth reusing:**
- *"Seniors are the ones currently absorbing the cost, because they do the validation."* — names *who* and *why* in one sentence. Reusable for any "who pays the hidden cost?" framing.
- *"The code base will be shaped by whatever validation did not happen."* — the inheritance frame for skipped validation work. Travels to debt / maintainability / institutional-memory contexts.
- *"recognising what looks plausible but isn't, slowing down on each piece"* — what validation actually feels like, in concrete terms. Reusable when "validation work" needs to stop being abstract.

**Strategic note on post 3 — draft carefully (added 2026-05-12, immediately after post 2 publish):**

Sensed risk after post 2 went live: conservative-leaning readers may claim it as ammunition for "don't adopt AI," which inverts its actual frame (seniors are *absorbing the validation cost while using AI*, not refusing to use it). Post 3 closes the WHY arc (HAZOP / domain bias) and needs to land carefully without breaking frame.

Points to think through when drafting:

- **Don't break frame mid-arc.** Post 3 is still WHY. A defensive "but I'm pro-AI" rider would muddle the argument and tell against posts 1 and 2.
- **The domain-bias frame has both edges — use both.** HAZOP / domain-specific failure modes show where seniors are *right* to distrust AI in their own field, and where they're *wrong* to distrust in fields they don't know. Skepticism is domain-specific, and so is trust. This symmetry defuses the "seniors are blanket skeptics" read that conservatives would want to keep.
- **Watch the closing line.** Don't terminate the arc on a note conservatives can frame as a finishing flourish. Depending on post-2 reception data, one sentence pointing forward (to a HOW arc) may be needed; or the closer may need to name the asymmetry explicitly (skepticism that does work vs. skepticism that's just refusal).
- **The actual adoption pivot belongs in the next arc, not in post 3.** Adoption-with-validation is promoted *through evidence of Jeroen's own use* — ese-bot in production, Reproduce-Don't-Assess catching what two LLMs missed, vmodel.eu, Linumiz / Zephyr-Meetup talk — not through defensive statements in the WHY arc. Conservatives can claim a defensive line; they can't claim "here's what I shipped."
- **Pre-publish review:** apply the multi-model review pattern as on post 2 (Opus + Haiku in-family for argument shape and rule compliance; cross-vendor optional). Verify every named study / statistic via `docs/verification/<slug>.md` before publish.

Revisit this note after the post-2 5–7 day reception check-in.

---

## 2026-05-12 — Held reply (like only) to AI Transfer Lab on senior-trust post

**Context:** AI Transfer Lab (small account, 129 followers, no prior interaction) commented under the senior-trust short post:

> The trust inversion makes sense when you think about what experience actually is pattern recognition for when something looks right but isn't. Juniors haven't built enough of that library yet to know what to distrust. The dangerous part isn't the junior pasting it in, it's that the validation gap is invisible until something ships that shouldn't have.

Substantive, additive sharpening. Restated experience as a pattern library for spotting plausible-but-wrong output, then pushed past the obvious "junior pasting it in" framing to the structural invisibility of the validation gap.

**Decision:** Like only. No reply posted (yet). Thin rapport with the account, the comment stands well on its own, and a reply with no relationship history risks reading as "always-have-to-have-the-last-word."

**Draft reply (held, not posted):**

> Yes. And the "until something ships" cutoff may be optimistic. Sometimes the code ships, works, and sits as silent debt until an unrelated change later surfaces what the original validation would have caught. The window for noticing closes well before symptoms do.

**Why this framing (kept for reuse if posted later or in adjacent context):**
- Concession-extension pattern (same shape as the Witek "Fair, with one caveat" reply). Honours their sharpening, pushes one notch further.
- Extends the "invisibility" axis from temporal (pre-ship) to structural (post-ship-but-latent). Doesn't contradict their read; deepens it.
- "validation gap" stays their phrase; no label-coining on top.

**Phrasings worth reusing:**
- *"silent debt until an unrelated change later surfaces what the original validation would have caught"* — concrete form of the latent-debt failure mode. Candidate for post 3 of the WHY arc, or for AE pattern writing on validation independence.
- *"The window for noticing closes well before symptoms do"* — sharp closing line for the production-cheap / validation-hard asymmetry when the audience needs the *temporal* version of it rather than the *rate* version.

**Revisit trigger:** If the thread develops more replies, or AI Transfer Lab engages further on the post, reconsider posting the draft (or a trimmed version). If post 3 of the WHY arc draws on the latent-debt framing, this phrasing is the candidate to lift.
