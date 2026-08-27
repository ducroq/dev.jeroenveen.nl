# Memory

<!-- Loaded every session. Keep this lean.
     Use this as an index — deep knowledge goes in topic files.

     END-OF-SESSION CURATION:
     1. Review gotcha-log for recurring patterns — promote them here or to topic files
     2. Check if any entries below are stale — retire them
     3. Update "Current State" to reflect what shipped or changed
     Monthly: audit everything. Prune as much as you add. -->

## Topic Files

| File | When to load | Key insight |
|------|-------------|-------------|
| `memory/gotcha-log.md` | Stuck or debugging | Problem-fix archive |
| `memory/hypothesis-log.md` | Recording a provisional editorial position to revisit later (post-publish reception checks, frame-landing bets, reframe outcomes) | Position / Alternative / Method / Revisit trigger / Review by. New 2026-05-18 per agent-ready-projects v1.10.0. |
| `docs/writing-guide.md` | Drafting / reviewing / planning an article (or a LinkedIn cross-post of one) | Audience filtering, LinkedIn packaging, named-colleague rule, what to avoid |

## Current State

- Site live at https://dev.jeroenveen.nl — **hosted on Netlify** (auto-deploys on push to `main`). `.github/workflows/deploy.yml` is orphaned from the prior GitHub Pages setup; kept but inactive.
- **9 projects** defined in the `projects` array, **first 3 publicly visible** via `VISIBLE_PROJECT_COUNT = 3` in `src/pages/index.astro` (drip-feed stance, 2026-04-21; count was 2 until at least 2026-08-26, and this row said so until 2026-08-27). Bump the constant to re-expose more. Order as of 2026-08-27: **DSP Workshop, Augur, ese-bot**; `agent-ready-papers` was demoted out of view on 2026-08-27 to make room and remains in the array.
- **Hero section commented out** (JSX `{/* ... */}` wrapper). Source intact for restore.
- **New /writing section** (2026-04-21): index at `src/pages/writing/index.astro`, per-article pages, shared metadata in `src/data/writing.ts`. First article: "A small GDPR-safe chatbot" at `/writing/ese-bot-eu-sovereign-rag/`.
- Homepage Writing section shows the 2 most recent articles between Projects and Background.
- **Background section rewritten** 2026-04-21 — real positioning (physics + signals + AI), concrete examples (Parkinson's ESP32 / Augur / ESE Bot / vmodel.eu), soft freelance availability.
- **Project-local writing guide added** 2026-04-28 (`docs/writing-guide.md`). Captures lessons from the ESE Bot LinkedIn post-mortem (audience filtering, packaging), the named-colleague rule, and the no-em-dashes voice preference. CLAUDE.md "Before You Start" + "Adding an Article" point to it. Replaces two short-lived auto-memory feedback files (now removed; canonical content lives in the guide).
- **WHY / V&V arc, 2 of 3 published; post 3 reset** (state as of 2026-05-18):
  - Post 1: `the-work-is-splitting` (published 2026-05-01). Validation as new structural problem.
  - Post 2: `senior-developers-trust-ai-less` (published 2026-05-12). Plausibility-vs-correctness from senior trust data.
  - Post 3: **still to come.** Will be grounded in own methods work (candidates: Reproduce-Don't-Assess, OPAL's layered verification, the assertion patterns used in practice). The article `who-runs-the-drc` was published 2026-05-18 as a candidate post 3 and pulled the same day after recognising it was AE-cross-domain work, not V&V arc closure. Post 2 promised the survey/research asymmetry in non-software domains; the pulled article delivered a platform-architecture comparison in non-software AI. Same domain, different topic. The pulled article may be recast later as the first of a sibling AE-cross-domain arc.
  - Both the shelved `drafts/ai-productivity-software-bias.md` (literature-bias frame) and the pulled `drafts/who-runs-the-drc.md` (cross-domain platform survey) are retained; neither is the V&V arc closer.
- **Verification record** for `who-runs-the-drc` retained at `docs/verification/who-runs-the-drc.md` as audit trail. Verification work itself was sound: 4/5 sources verified at primary; Adafruit upgraded SPECULATIVE → SUPPORTED after browser-fetch; cross-model review pass run (Haiku + Opus, disjoint coverage). The decision to pull was about arc-position, not verification.
- **Three new seed notes filed 2026-05-18** sketching follow-on pieces, all *Hold as seed*: `code-native-vs-agent-native.md` (load-bearing property = code-nativity), `validation-along-the-stack.md` (long view across SW/embedded/PCB/CAD), `where-value-is-migrating.md` (practitioner-convergence thesis; waits for one more source). Sequence: WHY arc → these.
- **New standalone LinkedIn draft, 2026-07-08**: `drafts/linkedin-post-better-hallucination-prompt-unpublished.md` ("You can't prompt your way out of hallucination"). Reply to the viral 7-rule "paste this and Claude stops lying" prompt (Harish Kumar) a colleague forwarded, who then asked for a better prompt. Spine: a prompt sets a prior, it cannot check anything. Payload is a shorter better prompt that asks for checkable work (source / DOI / provenance) over promised honesty. Sibling to the parked essay stub `drafts/the-spell-feeling-is-the-bug.md`. Not posted; when it ships, log in `external-comments.md` and consider a reception hypothesis then.
- **DSP Workshop launched 2026-08-27.** The site (`dsp-workshop.nl`, separate repo `veen-systems/dsp-workshop`) was already live but unannounced and mislinked. This session: card moved to first position and repointed from `ducroq.github.io/dsp-workshop` to `dsp-workshop.nl`, counts corrected (the card claimed 6 chapters / 15 topics / 114 exercises; verified figures are 12 / 34 / 115 plus 30 embedded pages), screenshot refreshed. Announced via a **standalone LinkedIn feed post** (not an article cross-post, so no `memory/posted-linkedin/` record): https://www.linkedin.com/posts/jeroen-veen-3244444_dsp-workshop-activity-7498650986190671872-ZjDt. Draft retained at `drafts/linkedin-post-dsp-workshop-launch.md`; publish logged in `memory/external-comments.md`; reception bet open in `memory/hypothesis-log.md` (review 2026-09-10).
- **Audience correction worth carrying (2026-08-26).** Jeroen's LinkedIn following is **old DSP colleagues and former students**, not the AI/V&V audience the `/writing/` corpus is written for. A draft aimed at the V&V following had to be scrapped. `docs/writing-guide.md` Section 2 describes the *article* reader; it does not describe the *feed* audience, and the two are different.
- **Do not quote dsp-workshop's build-provenance tiers in external copy.** They describe what a given *page* carries as on-page evidence, not what has been built and measured over a career, and they read as the latter outside the repo. An early launch draft led with "zero have been built and measured on a bench", which was false about Jeroen. Detail in `memory/external-comments.md` under the 2026-08-27 publish entry.
- Three review agents in `.claude/agents/` (copy, design, SEO).
- No test suite — static site, build success is the gate.
- **Open issues**: #2 (case study pages) — arguably served by the new /writing section; consider closing or reframing.

## Recently Promoted

<!-- "if [situation], then [what to do] — promoted from gotcha-log YYYY-MM-DD" -->

- if drafting or reviewing an article (or its LinkedIn cross-post), then read `docs/writing-guide.md` first — promoted from this session's analytics-driven post-mortem (2026-04-28)
- if proposing an article anchored on a named colleague's anecdote, then substitute with own work or an aggregate pattern — see `docs/writing-guide.md` Section 5 (2026-04-28)
- if substituting a draft for an arc position, then audit against the arc's promised topic from prior posts' forward-looks before evaluating the draft on its own merits — see `docs/writing-guide.md` Section 9 and gotcha-log entry (2026-05-18)

## Key File Paths

<!-- Supplement the project file's list with paths discovered during work -->

- `docs/writing-guide.md`: project-local writing guide — read before drafting any article
- `src/pages/index.astro`: `projects` array (9 cards), `VISIBLE_PROJECT_COUNT` constant, hero block (currently JSX-commented), Writing section importing from `src/data/writing.ts`
- `src/data/writing.ts`: article metadata (slug, title, excerpt, date, readTime) shared between homepage and `/writing/` index
- `src/pages/writing/index.astro`: article listing page
- `src/pages/writing/ese-bot-eu-sovereign-rag.astro`: first article (2026-04-21)
- `src/styles/global.css` lines 9-25: CSS custom properties (design tokens, --text-dim bumped to #8585a0 for WCAG AA). Note: global `p { max-width: 65ch }` is overridden by `.bio p` (homepage) and `.article-body p` (article) to allow full-width prose where needed.
- `src/layouts/Layout.astro`: canonical, OG, Twitter cards, JSON-LD Person schema, manifest
- `astro.config.mjs`: site URL + @astrojs/sitemap integration
- `public/robots.txt`, `public/site.webmanifest`: crawl rules and PWA manifest
- `public/screenshots/`: project + article screenshots (PNG, 2x retina)
- `.github/workflows/deploy.yml`: **orphaned** GitHub Pages workflow from pre-Netlify era — kept but inactive

## Active Decisions

<!-- One-liners about recent architectural choices -->

- Single-page architecture chosen deliberately — no routing, no page transitions, just a fast portfolio (a /writing section was added 2026-04-21 but kept minimal — plain `.astro` pages, no content collections)
- JetBrains Mono loaded from Google Fonts for headings and mono elements; system-ui for body
- Per-card accent colors via CSS custom property `--card-accent` set inline
- **Drip-feed publishing** (2026-04-21): expose projects one at a time via `VISIBLE_PROJECT_COUNT`; each LinkedIn drop points to one piece at a time
- **Writing as `.astro` pages, not content collections** (2026-04-21): upgrade to Astro content collections when the article count exceeds ~3
- **Hosting: Netlify, not GitHub Pages** (migration pre-dates this session). The GitHub Actions workflow file is retained but inactive
