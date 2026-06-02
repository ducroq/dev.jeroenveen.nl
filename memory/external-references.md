# External References Log

Observed external content (LinkedIn posts, articles, talks, papers) worth filing for later use: quoting, writing against, harvesting vocabulary, or treating as a foil. Distinct from `external-comments.md`, which logs *posted reactions*. This file logs material we *noticed* but did not engage with publicly.

Each entry captures: what the artifact is, why it's worth keeping, useful extracts, and potential uses in upcoming work.

---

## 2026-05-03 — "15 Crucial AI Agent Design Patterns" (LinkedIn list-post, course-seller)

**Source:** LinkedIn post (URL not captured at time of filing; paste in if/when re-encountered). Author is a course seller ("AI Agents Mastery 5-in-1," 2,300 students, 60% off CTA). Self-credentialing line: "After building 400+ AI Agents, this is the AI Agent Architecture Designs I wish I had on day one."

**Why filed:** This post is a near-perfect crystallisation of the production-side view that WHY post 1 ("The work is splitting") critiques. Fifteen patterns, three tiers, all organised by *coordination shape*. None of them are organised by *where verification comes from*. As a foil for upcoming posts in the WHY arc (especially post 3, HAZOP / domain bias), it's load-bearing reference material.

**The taxonomy (verbatim, for reuse / reference):**

*Tier 1: Single-Agent Patterns*
1. ReAct — alternate reasoning and acting
2. Plan-and-Execute — generate full plan upfront, execute sequentially
3. Reflection / Self-Critique — agent reviews own output, iterates
4. Tool Use / Function Calling — agent decides which tool to invoke

*Tier 2: Multi-Agent Orchestration*
5. Orchestrator-Subagent — coordinator delegates to specialised workers
6. Supervisor — routes tasks, monitors outputs, enforces quality gates
7. Hierarchical Agents — orchestrators managing orchestrators
8. Sequential Pipeline — each agent passes result to next
9. Parallel Fan-Out / Fan-In — split, then merge
10. MapReduce — distribute, then aggregate
11. Debate / Adversarial — agents argue, judge resolves

*Tier 3: Iterative & Feedback Loop*
12. Evaluator-Optimizer — generate, score, loop until quality met
13. Critic-Actor — critic feedback, actor refines
14. Self-Healing / Retry Loop — diagnose error, retry with corrected strategy
15. HITL — human checkpoints to approve, correct, redirect

**The structural critique (load-bearing for future posts):**

- "Self-Healing / Retry Loop" assumes the agent can diagnose its own error. That's the validator-inherits-implementation-assumptions problem (from the Witek thread) at runtime.
- "Critic-Actor" and "Evaluator-Optimizer" both assume the critic / evaluator is independent of the actor. The moment a single team builds both (typical case), that independence collapses.
- "Debate / Adversarial" comes closest to independence by spinning up opposing agents, but the judge inherits whatever shared training distribution all the agents share. Not truly independent.
- "HITL" is the only pattern that grounds verification *outside* the agent stack, and it's listed last, in tier 3, as a fallback rather than a foundation.
- The whole list is about *coordination*, not *truth*. The conversation hasn't caught up, in pattern-library form.

**Useful phrasings to harvest (genre-vocabulary, mostly as foil):**

- "After building 400+ AI Agents, this is the [thing] I wish I had on day one": credibility-claim rhythm in this genre.
- "Most AI engineers don't know half of these exist": gatekeeping phrasing.
- "Three tiers. Fifteen patterns. One decision before every build": list-post tricolon. Jeroen could parody / contrast: *"Three tiers. Fifteen patterns. One bottleneck none of them addresses."*
- The pattern names themselves (ReAct, Plan-and-Execute, Orchestrator-Subagent, Critic-Actor, Evaluator-Optimizer) are vocabulary in circulation. Using them signals fluency when writing against the frame.

**Potential uses:**

- **WHY post 3 (HAZOP / domain bias)**: open with this taxonomy as the foil. "There are fifteen well-circulated agent patterns. Three of them name a critic. None of them say where the critic's evidence comes from."
- **AE pattern-library work**: explicit positioning. The AE patterns (Reproduce-Don't-Assess, etc.) are organised by *evidence source*, not coordination shape. That's the structural difference.
- **A standalone short post**: "The pattern libraries you've seen organise agents by who-talks-to-whom. The hard problem is what counts as ground truth, and that's not in any of them." Self-contained, ~200 words, could go on LinkedIn before post 3.

**Decision rule for this kind of artifact:**
List-post taxonomies in this genre are useful as foils when they crystallise the dominant view *cleanly*. Don't engage in the comments. That drives traffic to a course-seller's funnel. File for use under Jeroen's own name where the analytical move can do its work.

---

## 2026-05-12 — Linumiz GmbH talk announcement: "Embedded DX: From Datasheet to Zephyr Driver" (LinkedIn post)

**Source:** LinkedIn post by Linumiz GmbH, URN `urn:li:activity:7459131799605190656`. Live URL: https://www.linkedin.com/feed/update/urn:li:activity:7459131799605190656/. Talk scheduled for 2026-05-12 at the Zephyr Project Meetup in Copenhagen, hosted by Demant.

**Why filed:** This is the embedded-domain version of post 3's argument happening in real time. Linumiz is asking, in public on LinkedIn: *can offline AI help embedded teams move faster from datasheets to working Zephyr drivers?* And framing the question honestly: *"where AI-assisted hardware enablement proves genuinely valuable and where careful oversight remains essential."* That is the produce-vs-validate split transposed onto embedded firmware work. The conversation is happening; the published-research surveys (JetBrains, Stack Overflow, METR) do not see it.

**Talk title (verbatim, for reuse / reference):**
*"Embedded DX: From Datasheet to Zephyr Driver — Can Offline AI Accelerate Hardware Enablement?"*

**Hashtag set** (heavily embedded-domain, useful as a reference for post 3 audience-filtering hashtag selection): #ZephyrRTOS, #EmbeddedSystems, #FirmwareDevelopment, #DeviceDrivers, #Devicetree, #HardwareEnablement, #EdgeAI, #AIForEmbedded, #EmbeddedDX, plus the broader #EmbeddedLinux, #YoctoProject, #Semiconductor.

**Why this matters for the WHY arc:**

- Post 3 (`drafts/ai-productivity-software-bias.md`) argues that AI-productivity research is software-developer-centric and misses hardware / embedded / control. The Linumiz post is a live data point: an embedded firm publicly asking the AI-acceleration question, framing it carefully, soliciting community feedback. This is the conversation post 3 is claiming exists, and provides external evidence for it.
- The Linumiz framing ("where it proves genuinely valuable and where careful oversight remains essential") maps directly to the produce-vs-validate frame from post 1 and the senior-trust validation work from post 2. Useful as evidence that embedded practitioners are arriving at similar conclusions independently.
- "Offline AI" specifically (local LLMs, not cloud) is an EU-relevant angle (GDPR adjacency, same as the ese-bot piece). Reinforces that the EU-embedded-engineering audience is differentiated from the US-cloud-AI audience.

**Engagement context (not engaged with publicly yet):**

- Johan Korten commented and tagged Jeroen and Victor Hogeweij. Comment text not captured at filing time (auth-gated for the WebFetch tool). Worth reading the tag in-app to understand what Johan is asking.
- Decided 2026-05-12 not to engage publicly yet. Filed for reference; possible engagement after post 3 ships (then the redirect-to-post move is natural: "wrote about this here, would be useful to compare notes with what you're seeing in Zephyr work").
- Potential foil: if Linumiz's talk lands with a strong "AI accelerates, here's how" message, that's a positive case to engage with. If their talk lands with a strong "here's where it breaks" message, that's the same case post 3 is making.

**To revisit:** After the Zephyr meetup (post-2026-05-12), check whether Linumiz published a recap or slides. If yes, those are concrete embedded-domain evidence for post 3.

---

## 2026-05-21 — Andrej Karpathy 2025 corpus (Software 3.0, decade-of-agents, vibe coding, year-in-review)

**Why filed:** Karpathy is the dominant popular voice in the territory Jeroen's writing inhabits. The "Software 3.0" framing is now ambient vocabulary (already showed up in Witek's 2026-04-28 spec-driven-assessment post, logged in `external-comments.md`). For ~70% of Jeroen's frame, Karpathy is an ally; the 30% gap is exactly where Jeroen's contribution lives. He is therefore a high-value foil-and-ally to cite *deliberately*: agree where the agreement is real (and use his vocabulary as bridge), then extend at the validator-independence layer where his frame does not yet reach. Per `feedback_verify_named_attributions.md`: any specific quote that lands in a draft must be verified against primary source before publish, not paraphrased from secondary.

### Primary-source items (verifiable now, lifted from the source)

- **2025 LLM year-in-review blog post**: https://karpathy.bearblog.dev/year-in-review-2025/
  - Verbatim on benchmark gaming (confirmed by direct fetch 2026-05-21):
    > "The core issue is that benchmarks are almost by construction verifiable environments and are therefore immediately susceptible to RLVR."
    Plus: *"benchmaxxing"* leads teams to *"construct environments adjacent to little pockets of the embedding space occupied by benchmarks and grow jaggies to cover them. Training on the test set is a new art form."*
  - Notable absence: the post does **not** discuss LLM-as-judge, the pass@1-vs-pass@k reliability gap, or the actor-validator-independence question. These are gaps in his summary frame.
  - References a separate Karpathy blog post titled *"Verifiability"* (linked from the year-in-review; not yet read here, worth fetching before any draft that engages his validation frame directly).
- **YC AI Startup School talk, 2025-06-19: "Software Is Changing (Again)"**. https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again. Transcript + annotations: https://www.latent.space/p/s3.
- **2025 year-in-review** also flags **Claude Code** as the first convincing demonstration of what an LLM agent looks like, and that running it locally (vs OpenAI's cloud-orchestrated approach) is the right architecture. Useful as ally-citation for any post that argues for local/on-prem AI tooling (ese-bot territory).

### Secondary-source positions (cite only after primary-source verification)

Reported but not yet personally verified to primary source. Treat as candidates, not facts, until traced.

- **"Decade of agents, not year"**: Dwarkesh Patel interview, Oct 2025. Reported framing: cognitive limitations, no continual learning, unreliable memory, can't handle complex computer tasks. Reported quote: *"If I just average it out, it just feels like a decade to me."* Strong ally for Jeroen's WHY arc; *exact attribution* requires fetching the Dwarkesh transcript before any draft uses the quote.
- **"Fallible people spirits"**: YC talk, June 2025. Karpathy's framing for what LLMs are; verification required by humans. Vivid, memorable phrasing. Worth using as bridge-vocabulary if attribution holds up at primary source.
- **"Partial autonomy" + "autonomy sliders"**: YC talk. Championed Cursor, Perplexity as the right pattern: AI + fast visual verification loops, human in loop. Aligns with Jeroen's frame but stops one level short: talks about *human* verification, not architectural validator-independence.
- **"Jagged intelligence" / "anterograde amnesia"**: YC talk. Named limitations of current LLMs. Useful vocabulary for any post that needs to characterise "where LLMs are weirdly weak."
- **"Vibe coding"**: coined Karpathy, February 2025. Originally framed for *throwaway weekend projects*; popular adoption distorted it toward production. METR's 2025 randomised trial (19%-slower-with-AI, believed 20%-faster) directly relevant to the senior-trust article's main statistic, and this study is already cited in `senior-developers-trust-ai-less` verification record.

### Where Karpathy's frame and Jeroen's frame converge

- Validation is the hard half. (Karpathy: "fallible people spirits", "fast verification loops"; Jeroen: "production is cheap and fast. Validation is not.")
- Skepticism toward LLM-only evaluation. (Karpathy: benchmarks gameable via RLVR; Jeroen: the evaluator inherits the actor's assumptions.)
- Reliability gaps in current systems. (Karpathy: no continual learning, jagged intelligence; Jeroen: validation independence required, calibration gates needed.)
- Decade not year. (Karpathy: explicit; Jeroen: implicit in WHY arc framing.)
- Local / on-prem AI as architectural good. (Karpathy: Claude Code on your computer beats cloud-orchestrated agents; Jeroen: ese-bot GDPR-safe chatbot, EU-sovereign RAG.)

### Where Jeroen's frame extends Karpathy's

- **Architectural validator-independence.** Karpathy talks about *human-in-loop* verification. Jeroen's *the-model-is-not-the-grader* argues for *deterministic-code* validators against fixed rubrics, with the explicit claim that "the evaluator inherits the actor's assumptions, because they came from the same training distribution and they are reading the same artifact in the same way." This is the sharper version of Karpathy's verification frame.
- **Engineering-domain anchoring.** Karpathy stays at the software/agent layer (Cursor, Perplexity, Claude Code). Jeroen's frame extends to HAZOP, V-model, certified domains (medical, automotive), embedded firmware: places where validation *has to* live outside the LLM because the consequences live outside the LLM.
- **Production discipline.** Karpathy describes "verification loops" but stays underspecified about *what* the verifier is doing. Jeroen specifies: held-out reference set, scores compared to baseline, calibration gate, ADRs documenting alternatives considered. Concrete and reproducible.
- **The publish-discipline meta-move.** Jeroen runs `docs/verification/<slug>.md` per-article anti-hallucination audits. Karpathy's posts do not appear to have an equivalent surface-level verification record (and given his February 2025 "vibe coding" tweet's hedging, the surrounding discourse has not yet developed one). Worth noting as a methodological gap if/when a draft engages his work directly.

### Potential uses

- **Ally-citation in any V&V arc post.** "As Karpathy puts it, [primary-source quote about fallible spirits / verification loops], and one layer further down, the validator itself has to be independent of the actor." Lifts him as bridge, then extends. Per `feedback_thin_rapport_add_dont_carve.md`, this is the add-don't-carve move at citation-scale.
- **Pickup vocabulary.** "Software 3.0", "jagged intelligence", "anterograde amnesia", "partial autonomy", "autonomy slider", "vibe coding": all in circulation now and signal fluency with the current discourse. Use sparingly; the visual-register rule applies (don't over-rely on borrowed vocabulary at the expense of mechanism).
- **Foil for the post about pattern libraries** (already filed under the "15 Crucial AI Agent Design Patterns" entry above). Karpathy's "partial autonomy" frame and the pattern-library taxonomy are both coordination-centric; both miss validator-independence. Could pair them as twin foils.
- **Dedicated read of Karpathy's "Verifiability" post** (linked from the 2025 year-in-review) before any post directly engaging his evaluation frame. The year-in-review pointed at it without summarising. That is exactly the post that will tell us whether the validator-independence gap is genuinely his blind spot or simply not in the year-end summary.

### Caveats

- Some of the most quotable phrasings ("fallible people spirits", "decade not year", "jagged intelligence") came through secondary commentary; primary-source verification is mandatory before any of them ships in a Jeroen-authored piece. The Dwarkesh interview transcript and the YC talk full transcript are the targets when that work is needed.
- Karpathy posts heavily on X. Anything sourced from a tweet is more time-bound and more retract-prone than his blog posts; weight blog + talks higher than tweets for citation.
- He is a high-status interlocutor with a different audience. Citing him is a positioning move with consequences both ways (signals fluency; can read as deference if the citation is uncritical). The add-don't-carve frame applies: cite where the agreement is genuine, then extend in Jeroen's own register.

---

## 2026-05-21 — Caveman (Claude Code output-compression skill by Julius Brussee)

**Source:** https://github.com/JuliusBrussee/caveman. Claude Code / Cursor / Codex skill that forces terse "caveman speak" output. Project site: https://juliusbrussee.github.io/caveman/. Author: Julius Brussee, 19, Leiden University student. Repo climbed from dozens to >20k stars in ~half a day on HN. Picked up by Dutch press as a "Dutch student amazes AI companies" piece.

**Why filed:** Not the technique. Output-terseness via system prompt is well-trodden (LLMLingua etc.). The interesting artifact is the **framing**. "Talk like caveman" is a memorable, playful packaging of a known idea (be concise). That framing is what drove ~20k stars and NVIDIA attention, not novel mechanism. Direct lesson for Jeroen's writing arc: **fun framing sells**, even (maybe especially) for technical work that would otherwise read as dry prompt-engineering tips.

**What's actually under the hood:**

- A system-prompt skill that constrains output style. Does not touch model weights, inference, or reasoning tokens (author explicitly clarified on HN).
- Reports ~65% output-token reduction vs no-system-prompt baseline.
- **Three-arm evaluation methodology** (baseline / "Answer concisely" terse / full caveman rules). Honest framing: the *real* delta vs a one-line "be concise" instruction is ~24%, not 65%. Most prompt-skill claims compare skill-vs-baseline and overstate.
- Includes sub-skills: `caveman-commit`, `caveman-review`, `caveman-compress` (compresses CLAUDE.md / memory files).
- Cites a March 2026 paper *"Brevity Constraints Reverse Performance Hierarchies in Language Models"* claiming brevity improves accuracy by 26pp. Worth primary-source check before citing.

**Useful phrasings to harvest:**

- *"why use many token when few token do trick"*: tagline. Memorable because it performs its own claim. Compare with the typical engineering-blog headline "Optimizing token usage in large language models."
- *"the most powerful prompt skill in 2026"*: community reception phrasing; foil for any post arguing reach ≠ depth.
- The **three-arm comparison** as a methodological move: "the fair comparison is not vs baseline, it's vs the simplest reasonable alternative." This is the same shape as Jeroen's "compare to baseline, not to nothing" rule in the validation arc. Concrete external instance.

**Potential uses:**

- **As a framing case study** in any meta-post about technical communication / why some engineering writing travels. The mechanism is unremarkable; the wrapper is everything. Pairs with the WHY arc's question of how validation-discipline ideas get adopted vs ignored.
- **As an honest-evaluation foil.** Most "X% improvement" claims in the prompt-engineering genre do not run a three-arm comparison. Caveman does and reports the smaller honest number alongside the bigger marketing number. That's the same epistemic move as `docs/verification/<slug>.md` per-article audits, worth citing as an example of a vendor / tool author doing it right.
- **Cautionary use:** the lesson is *frame memorably*, not *frame goofily*. Jeroen's register is dry-precise; copying caveman-speak would break voice. Take the principle (vivid packaging), not the surface (broken English).

**Caveats:**

- Loading the skill itself costs context tokens. End-to-end savings ≠ README headline.
- Compresses *output*, not *input*. Useless for batch text-processing pipelines (where LLMLingua or routing to Haiku is the right tool).
- The paper citation needs primary-source verification before use; "26pp accuracy improvement from brevity" is the kind of headline number that often doesn't survive scrutiny.
