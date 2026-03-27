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

## Current State

- Site is live at https://dev.jeroenveen.nl with 8 project cards
- Last work (2026-03-27): added Augur card, renamed DSP Lab → DSP Workshop, broadened hero to "Engineer & Researcher", per-card accent color stripes, SEO/accessibility audit fixes (canonical, Twitter cards, JSON-LD, sitemap, skip-nav, WCAG contrast, aria attributes)
- Three review agents in `.claude/agents/` (copy, design, SEO)
- No test suite — static site, build success is the main gate
- CI deploys on every push to main via GitHub Actions
- Open issues: #1 (screenshots in cards), #2 (case study pages), #4 (move to Netlify + Resend contact form)

## Recently Promoted

<!-- "if [situation], then [what to do] — promoted from gotcha-log YYYY-MM-DD" -->

## Key File Paths

<!-- Supplement the project file's list with paths discovered during work -->

- `src/pages/index.astro` lines 4-69: the `projects` array (8 cards with accent colors)
- `src/styles/global.css` lines 9-25: CSS custom properties (design tokens, --text-dim bumped to #8585a0 for WCAG AA)
- `src/layouts/Layout.astro`: canonical, OG, Twitter cards, JSON-LD Person schema, manifest
- `astro.config.mjs`: site URL + @astrojs/sitemap integration
- `public/robots.txt`, `public/site.webmanifest`: crawl rules and PWA manifest

## Active Decisions

<!-- One-liners about recent architectural choices -->

- Single-page architecture chosen deliberately — no routing, no page transitions, just a fast portfolio
- JetBrains Mono loaded from Google Fonts for headings and mono elements; system-ui for body
- Per-card accent colors via CSS custom property `--card-accent` set inline
