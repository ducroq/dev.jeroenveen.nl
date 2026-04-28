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
| `docs/writing-guide.md` | Drafting / reviewing / planning an article (or a LinkedIn cross-post of one) | Audience filtering, LinkedIn packaging, named-colleague rule, what to avoid |

## Current State

- Site live at https://dev.jeroenveen.nl — **hosted on Netlify** (auto-deploys on push to `main`). `.github/workflows/deploy.yml` is orphaned from the prior GitHub Pages setup; kept but inactive.
- 8 projects defined in the `projects` array, but only the **first 2 publicly visible** via `VISIBLE_PROJECT_COUNT = 2` in `src/pages/index.astro` (drip-feed stance, 2026-04-21). Bump the constant to re-expose.
- **Hero section commented out** (JSX `{/* ... */}` wrapper). Source intact for restore.
- **New /writing section** (2026-04-21): index at `src/pages/writing/index.astro`, per-article pages, shared metadata in `src/data/writing.ts`. First article: "A small GDPR-safe chatbot" at `/writing/ese-bot-eu-sovereign-rag/`.
- Homepage Writing section shows the 2 most recent articles between Projects and Background.
- **Background section rewritten** 2026-04-21 — real positioning (physics + signals + AI), concrete examples (Parkinson's ESP32 / Augur / ESE Bot / vmodel.eu), soft freelance availability.
- **Project-local writing guide added** 2026-04-28 (`docs/writing-guide.md`). Captures lessons from the ESE Bot LinkedIn post-mortem (audience filtering, packaging) and the named-colleague rule. CLAUDE.md "Before You Start" + "Adding an Article" point to it. Replaces two short-lived auto-memory feedback files (now removed; canonical content lives in the guide).
- Three review agents in `.claude/agents/` (copy, design, SEO).
- No test suite — static site, build success is the gate.
- **Open issues**: #2 (case study pages) — arguably served by the new /writing section; consider closing or reframing.

## Recently Promoted

<!-- "if [situation], then [what to do] — promoted from gotcha-log YYYY-MM-DD" -->

- if drafting or reviewing an article (or its LinkedIn cross-post), then read `docs/writing-guide.md` first — promoted from this session's analytics-driven post-mortem (2026-04-28)
- if proposing an article anchored on a named colleague's anecdote, then substitute with own work or an aggregate pattern — see `docs/writing-guide.md` Section 5 (2026-04-28)

## Key File Paths

<!-- Supplement the project file's list with paths discovered during work -->

- `docs/writing-guide.md`: project-local writing guide — read before drafting any article
- `src/pages/index.astro`: `projects` array (8 cards), `VISIBLE_PROJECT_COUNT` constant, hero block (currently JSX-commented), Writing section importing from `src/data/writing.ts`
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
