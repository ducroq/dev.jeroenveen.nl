# External References Log

Observed external content (LinkedIn posts, articles, talks, papers) worth filing for later use — quoting, writing against, harvesting vocabulary, or treating as a foil. Distinct from `external-comments.md`, which logs *posted reactions*. This file logs material we *noticed* but did not engage with publicly.

Each entry captures: what the artifact is, why it's worth keeping, useful extracts, and potential uses in upcoming work.

---

## 2026-05-03 — "15 Crucial AI Agent Design Patterns" (LinkedIn list-post, course-seller)

**Source:** LinkedIn post (URL not captured at time of filing; paste in if/when re-encountered). Author is a course seller ("AI Agents Mastery 5-in-1," 2,300 students, 60% off CTA). Self-credentialing line: "After building 400+ AI Agents, this is the AI Agent Architecture Designs I wish I had on day one."

**Why filed:** This post is a near-perfect crystallisation of the production-side view that WHY post 1 ("The work is splitting") critiques. Fifteen patterns, three tiers, all organised by *coordination shape*. None of them are organised by *where verification comes from*. As a foil for upcoming posts in the WHY arc — especially post 3 (HAZOP / domain bias) — it's load-bearing reference material.

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
- "Critic-Actor" and "Evaluator-Optimizer" both assume the critic / evaluator is independent of the actor. The moment a single team builds both — typical case — that independence collapses.
- "Debate / Adversarial" comes closest to independence by spinning up opposing agents, but the judge inherits whatever shared training distribution all the agents share. Not truly independent.
- "HITL" is the only pattern that grounds verification *outside* the agent stack — and it's listed last, in tier 3, as a fallback rather than a foundation.
- The whole list is about *coordination*, not *truth*. The conversation hasn't caught up, in pattern-library form.

**Useful phrasings to harvest (genre-vocabulary, mostly as foil):**

- "After building 400+ AI Agents, this is the [thing] I wish I had on day one" — credibility-claim rhythm in this genre.
- "Most AI engineers don't know half of these exist" — gatekeeping phrasing.
- "Three tiers. Fifteen patterns. One decision before every build" — list-post tricolon. Jeroen could parody / contrast: *"Three tiers. Fifteen patterns. One bottleneck none of them addresses."*
- The pattern names themselves (ReAct, Plan-and-Execute, Orchestrator-Subagent, Critic-Actor, Evaluator-Optimizer) are vocabulary in circulation. Using them signals fluency when writing against the frame.

**Potential uses:**

- **WHY post 3 (HAZOP / domain bias)**: open with this taxonomy as the foil. "There are fifteen well-circulated agent patterns. Three of them name a critic. None of them say where the critic's evidence comes from."
- **AE pattern-library work**: explicit positioning. The AE patterns (Reproduce-Don't-Assess, etc.) are organised by *evidence source*, not coordination shape. That's the structural difference.
- **A standalone short post**: "The pattern libraries you've seen organise agents by who-talks-to-whom. The hard problem is what counts as ground truth, and that's not in any of them." Self-contained, ~200 words, could go on LinkedIn before post 3.

**Decision rule for this kind of artifact:**
List-post taxonomies in this genre are useful as foils when they crystallise the dominant view *cleanly*. Don't engage in the comments — that drives traffic to a course-seller's funnel. File for use under Jeroen's own name where the analytical move can do its work.
