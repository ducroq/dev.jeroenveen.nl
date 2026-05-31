# If it has claims, it has tests

*Status: seed note. Captured 2026-05-12 from a conversation about whether agent-ready-papers generalises beyond academic writing. Sibling to the three application-level seeds filed the same day (`plausibility-vs-correctness.md`, `auto-loading-cliff.md`, `cross-model-review.md`). Also adjacent to `verification-is-a-workflow-problem.md` (2026-05-31), which makes a narrower argument on the layer at which verification has to live. This is the **theory layer** that names the shape they all instantiate.*

---

## The seed

agent-ready-papers' actual scope is wider than its name. The README opens with "AI-augmented academic and structured non-fiction writing", the 2026-05 extension brought speculative-design under the same registry (DR-010), and the "what doesn't work" section explicitly names WhatsApp / Slack messages with quantitative claims as in-scope. The framework is already not just about papers, it just happens to be named for the application that drove its first three years.

The real generalisation is sharper than "structured non-fiction":

> Any artifact with decomposable units that exit to external evaluators, with confidence gradients and architectural constraints, and a quality gate before shipping, can be system-engineered.

That shape covers a much wider domain than the framework's name suggests:

- Papers (the original)
- Articles, blog posts, essays (already in scope, this site's `docs/verification/` is one instantiation)
- Talks, lectures, conference presentations
- Books and chapters (voice-driven non-fiction was the 2026-05 extension)
- Strategy briefs, policy memos, white papers
- Grant proposals (claims about feasibility, novelty, broader impact)
- Audit reports
- Investigative journalism (per-claim source traceability)
- Educational assessments (agent-ready-projects has a worked example)
- Technical specifications, RFCs, design documents
- Internal memos with quantitative claims
- WhatsApp / Slack with numbers in them (the framework's own "what doesn't work" item already names this)

## Why this is article-worthy on dev.jeroenveen.nl

- The other three seeds filed today are *applications* of the framework. This is the article *about* the framework's shape. Different kind of contribution: theory vs. practice.
- The meta-claim survives the audience filter cleanly. An engineer or AI lead reading "if it has claims, it has tests" recognises the shape, even if they have never written an academic paper.
- It connects the WHY arc's validation thesis to a *general* practice: senior-trust article says seniors validate, this article says validation is system-engineering-shaped wherever it happens.
- It positions the agent-ready-papers framework as one instantiation of a wider practice, not the practice itself. That repositioning makes the framework more recruiting-friendly (engineers who do not write papers can still see themselves in it).

## Possible homes

1. **New dev.jeroenveen.nl article.** Argument-form title candidates: *"If it has claims, it has tests."* (sharpest), *"The systems-engineering shape of any verifiable artifact."* (more descriptive), or *"Anything with claims can be system-engineered."* (closest to the original observation, slightly bland). Lean: the first.
2. **AE pattern essay on verification as a generalised practice.** Sibling to *Reproduce, Don't Assess*: that one is a specific verification move; this one is the meta-shape that says verification is system-engineering-applied-to-the-artifact-class. Could live on the AE site as the conceptual umbrella for several patterns.
3. **A section inside agent-ready-papers' own README** that surfaces the generalisation explicitly, rather than leaving it implicit in the scope line and the WhatsApp item. Lower-stakes, immediately useful, but does not produce a stand-alone article.

Lean: option 1, with option 3 as a small follow-up edit to the framework's README to make the generalisation explicit upstream.

## The boundary worth holding

Not "anything", but **anything whose claims exit to external evaluators.** Without that exit:

- there is no requirement (no one is checking)
- there is no test coverage (no claim is auditable)
- there is no quality gate (nothing is at stake)

So personal journals, working notes, private brainstorms, and "thinking in public" pieces that disclaim their tentativeness all sit *outside* the verifiable-claims family. The article needs to name this boundary, or it overstretches and someone in comments will produce the "what about my journal" counter-example before the second paragraph.

Refined formulation: **anything in the verifiable-claims family** (artifact + decomposable units + external evaluators + confidence gradient + quality gate) is system-engineering-shaped.

## Open questions before drafting

- Which three or four examples make the generalisation land for the dev.jeroenveen.nl audience? Strategy briefs and audit reports probably travel well; grant proposals are too academic; WhatsApp-with-numbers is a fun edge case that proves the framework's seriousness about *informal* technical communication. The opening paragraph needs one example that the senior engineer reader does themselves; the middle can range wider.
- Does the article position itself as *extending agent-ready-papers* (recruiting piece), or as a *standalone observation that agent-ready-papers happens to instantiate* (essayistic)? The two are different shapes. The essayistic version is voice-compatible and travels further; the recruiting version is more useful for the framework. Probably essayistic first, recruiting later as a follow-up.
- Connection to the senior-trust article: do this article and the senior-trust article share a closing sentence about validation being load-bearing wherever AI is augmenting human work? The phrasings should not be identical, but the shared frame should be visible to anyone reading both.

## How it sits next to the other three seeds

| Seed | Layer | Connection |
|---|---|---|
| `plausibility-vs-correctness.md` | Evidence (the 68-equation case) | What goes wrong without the framework |
| `cross-model-review.md` | Mitigation (DR-011 pattern) | What partially fixes it |
| `auto-loading-cliff.md` | Workflow (auto-load + task-triggered pointers) | The repo-level scaffolding |
| `if-it-has-claims-it-has-tests.md` (this) | Theory (verifiable-claims family) | The shape all three instantiate |

The four together would be a quartet, not a single article. If the writing capacity exists to ship them in sequence after the WHY arc, the natural order is: theory (this one) → evidence (plausibility) → mitigation (cross-model) → workflow (auto-loading). Or the reverse, starting with the concrete case and building up to the theory. Worth a separate decision when the moment comes.

## Reusable phrasings

- *"If it has claims, it has tests."*: strongest line. Argument-form title, closing aphorism, cover-image quote.
- *"Anything whose claims exit to external evaluators is system-engineering-shaped."*: the precise version of the meta-claim. Useful when "if it has claims, it has tests" needs to be defended against the "what about my journal" pushback.
- *"The framework is already wider than its name."*: short observation that fronts the article and gives the framework's actual scope visibility.
- *"Verification is system-engineering applied to the artifact class."*: candidate for the conceptual-umbrella version that sits over Reproduce-Don't-Assess and the other AE verification patterns.

## Decision

Hold as seed. This is probably the strongest of the four candidate articles, but it sits *after* the WHY arc finishes and likely *after* one of the application seeds ships first (so the theory article has concrete instances to point at rather than introducing the framework cold). Revisit when WHY post 3 ships.
