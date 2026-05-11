# Adding an article

The publishing workflow for a `/writing/` article on `dev.jeroenveen.nl`.

## Steps

1. Read `docs/writing-guide.md` first: voice, audience, LinkedIn packaging, what to avoid.
2. Draft in `drafts/<slug>.md` first. Sit on it overnight. Cold re-read tomorrow.
3. **Build a verification record at `docs/verification/<slug>.md`** for every load-bearing statistic, named study, or coined attribution. Apply Step 0 + Steps 4–6 of the [agent-ready-papers](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md) checklist; trace each number to primary source; map confidence tier to article language per `docs/writing-guide.md` Section 7. If a claim cannot be traced to primary source, weaken the language or drop the claim.
4. Once approved, move the body into `src/pages/writing/<slug>.astro` (use the existing article as a template).
5. Register the article in `src/data/writing.ts` so it appears on `/writing/`.
6. **Add inline links + Sources block** per `docs/writing-guide.md` Section 7. Inline link on first mention of each cited source; Sources `<aside class="article-sources">` block at the end of the article body. Working examples: `src/pages/writing/the-work-is-splitting.astro`, `src/pages/writing/senior-developers-trust-ai-less.astro`.
7. Generate a cover image: edit the headline and slug constants in `scripts/gen-social-image.py`, then `python scripts/gen-social-image.py`. Output lands at `public/social/<slug>.png` and doubles as the LinkedIn Pulse cover.
8. Decide if the argument earns an in-article figure. Most do not. If yes, follow one of the patterns: `scripts/gen-<slug>-diagram.py` (sketch register, see `gen-article-diagram.py` and `gen-ese-bot-diagram.py`) or `scripts/gen-<slug>-figure.py` (Tufte typographic, see `gen-senior-trust-figure.py`). Output to `public/diagrams/<slug>.svg`. Embed via `<figure class="article-sketch">` (borderless), distinct from `<figure class="article-figure">` (the polished card used for screenshots). Audit against the *It Is Both* visual-register memory rule (`feedback_visual_register.md`) before shipping any figure.
9. Run `npm run dev` and check the article reads cleanly cold.
10. **Cross-model review pass.** Paste the article body (or the live preview URL once deployed) into a different model (GPT, Gemini) or a fresh Claude session with no project context, using [`templates/review-prompt.md`](file:///C:/local_dev/agent-ready-papers/templates/review-prompt.md) Variant B (non-empirical) as the prompt. Address logic gaps, unsupported assertions, citation drift, and tone issues before pushing. Filter the review output against the project's voice rules in `docs/writing-guide.md` Section 6 (cross-vendor reviewers do not read your voice and will frequently suggest label-coining, subheadings, or popular-psychology references that the rule rejects). Per `docs/writing-guide.md` Section 7.
11. Commit and push to `main`. Netlify rebuilds and deploys.

## LinkedIn cross-post (after the article is live)

The default packaging for a published article is **all three surfaces**:

1. **Pulse article (long-form)**: body copied from the website article, with `Originally published at dev.jeroenveen.nl/writing/<slug>` footer.
2. **Short feed post**: links to the Pulse article (or to the website, depending on goal). Hook in first ~210 chars; one comment prompt at the end.
3. **Canonical home**: the dev.jeroenveen.nl article page itself.

Draft both LinkedIn pieces in `drafts/<slug>-linkedin.md` before publishing. Log the publish in `memory/external-comments.md` with all three URLs and a 5–7 day check-in note (which surface out-reached, what landed, what to feed into the next post).

The Pulse vs short-post-only choice is a tradeoff. Pulse gives more LinkedIn reach but creates a duplicate-content situation that hurts website SEO (LinkedIn Pulse can outrank a young site). Default to both surfaces while the site is young and inbound is thin; revisit when the site has authority.
