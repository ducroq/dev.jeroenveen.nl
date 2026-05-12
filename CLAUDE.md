# dev.jeroenveen.nl

Personal portfolio site for Jeroen Veen (Research & Engineering). Astro static site with a homepage (projects, writing, background) and a `/writing/` section for articles. Dark theme with amber accent. Deployed to Netlify (auto-rebuilds on push to `main`).

- **Stack**: Astro 5, TypeScript (strict), CSS custom properties, GitHub Actions
- **Status**: Production (live at https://dev.jeroenveen.nl)
- **Repo**: github.com/ducroq/dev.jeroenveen.nl
- **agent-ready-projects**: v1.3.2

## Before You Start

| When | Read |
|------|------|
| Adding or editing a project card | `docs/workflows/adding-a-project-card.md`: the `projects` array shape (`src/pages/index.astro`) and screenshot conventions |
| Drafting in Jeroen's voice (articles, LinkedIn comments, replies, posts) | `docs/writing-guide.md`: voice, audience, LinkedIn packaging, em-dash rule, what to avoid. Applies to anything published under his name, not only `/writing/` articles |
| Defining or auditing a term Jeroen uses (coined frames like validation, AE, ground truth; or field vocabulary like agent, workflow, evaluator-optimizer, HITL) | `docs/glossary.md`: working definitions, drift notes, AE-frame relevance |
| Continuing a parked draft | `drafts/<slug>.md`: articles in progress live here until they ship |
| Reviewing past LinkedIn comments or external replies | `memory/external-comments.md`: log of posted reactions and publish events with framing notes, URLs, and reception history |
| Continuing or referencing a previously posted LinkedIn cross-post | `memory/posted-linkedin/<slug>.md`: full text of posted Pulse articles + short feed posts. Reuse as templates for new cross-posts. Records exist for `the-work-is-splitting` and `ese-bot-eu-sovereign-rag` |
| Filing or recalling an external post / talk / paper for later reference | `memory/external-references.md`: observed-but-not-engaged-with material (foils, vocabulary, citation candidates) |
| Adding an article | `docs/workflows/adding-an-article.md`: full publishing workflow including draft, verification record, page file, registry, cover image, references, and LinkedIn cross-post |
| Verifying claims in an article (draft or published) | `docs/verification/<slug>.md`: per-article anti-hallucination record. Apply Step 0 + Steps 4–6 of the [agent-ready-papers](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md) checklist for every load-bearing statistic, named study, or coined attribution before publish. Trace each number to primary source, not to an intermediate ANALYSIS file. Confidence tier maps to article language per `docs/writing-guide.md` Section 7. |
| Generating a social/cover image for an article | `scripts/gen-social-image.py`. Outputs typographic 1200×630 PNG to `public/social/<slug>.png`. Doubles as the LinkedIn Pulse cover. |
| Generating an in-article diagram or figure | `scripts/gen-<slug>-diagram.py` (sketch register: jittered SVG paths, mono lowercase labels) or `scripts/gen-<slug>-figure.py` (Tufte typographic: numbers + citation, no shapes). Output to `public/diagrams/<slug>.svg`. Audit against the visual-register memory rule (`feedback_visual_register.md`) before shipping any figure. |
| Changing layout, SEO, or meta tags | `src/layouts/Layout.astro`: head, OG tags, structured data |
| Changing design tokens or global styles | `src/styles/global.css`: all CSS custom properties live here |
| Stuck or debugging something weird | `memory/gotcha-log.md`: problem-fix archive |
| Reviewing copy, design, or SEO concerns | `.claude/agents/`: three review docs from previous audit sessions |
| Ending a session | `memory/gotcha-log.md`: review, promote patterns, retire stale entries |

## Hard Constraints

- Minimal client-side JS is fine (e.g., card filtering, theme toggle) but avoid heavy frameworks. Keep the site fast and lightweight.
- All styling uses CSS custom properties defined in `global.css`. Do not introduce Tailwind, Sass, or CSS modules.
- The `CNAME` file must stay as `dev.jeroenveen.nl`. Retained from the GitHub Pages era; Netlify uses the DNS settings directly.
- `.github/workflows/deploy.yml` is an orphaned GitHub Pages workflow. Do not treat it as active CI. Deployment goes through Netlify.
- Keep the site accessible: skip-nav link, `aria-label` on external links, `:focus-visible` styles, semantic HTML
- **LinkedIn drafts are SSoT here**, not in `work-income`. Two patterns:
  - **General LinkedIn drafts** (ideas backlog, replies, standalone posts): `drafts/linkedin-post-<topic>-unpublished.md`. Drop `-unpublished` once posted, or log the publish in `memory/external-comments.md` and delete the draft.
  - **Article-specific cross-post drafts** (Pulse + short feed post tied to a `/writing/<slug>/` article): `drafts/<slug>-linkedin.md`. After posting, log URLs in `memory/external-comments.md` AND move the full text to `memory/posted-linkedin/<slug>.md`. See `docs/workflows/adding-an-article.md` for the lifecycle. The `the-work-is-splitting` and `ese-bot-eu-sovereign-rag` records are the working examples.

  Career strategy stays in `work-income/cv/`.

## Architecture

```
dev.jeroenveen.nl/
  src/
    layouts/Layout.astro            # HTML shell: head, meta, OG, structured data, fonts
    pages/index.astro               # Homepage: projects array + hero + grid + bio + footer
    pages/writing/index.astro       # Writing index: lists articles from src/data/writing.ts
    pages/writing/<slug>.astro      # Individual articles (one .astro file per article)
    data/writing.ts                 # Article metadata: slug, title, date, excerpt, readTime
    styles/global.css               # Design tokens, reset, typography, scrollbar
  docs/
    writing-guide.md                # Voice, audience, LinkedIn packaging, read before drafting
    glossary.md                     # Working definitions for terms Jeroen uses (validation, AE, ground truth, …)
    verification/<slug>.md          # Per-article anti-hallucination audit (Step 0 + Steps 4–6, confidence tiers, Sources block)
    workflows/                      # Numbered workflow steps for adding cards / articles, loaded on demand
  drafts/
    <slug>.md                       # Article drafts in progress (cold-re-read parking spot)
    <slug>-linkedin.md              # Article-specific LinkedIn cross-post drafts; moved to memory/posted-linkedin/ after publish
    linkedin-post-<topic>-unpublished.md  # General LinkedIn drafts (ideas, replies, standalone posts) — SSoT, not in work-income
  memory/
    external-comments.md            # Publish events + reply log: URLs, reception, reusable phrasings
    external-references.md          # Observed-but-not-engaged-with external content
    gotcha-log.md                   # Problem-fix archive; reviewed at end of session
    posted-linkedin/<slug>.md       # Full text of posted LinkedIn cross-posts (Pulse body + short feed post), for template reuse
    visual-references/              # Local reference images (gitignored; allowlist exception for files the diagram scripts reference)
  public/
    CNAME                           # GitHub Pages custom domain
    robots.txt                      # Crawl rules + sitemap pointer
    site.webmanifest                # PWA manifest (name, colors)
    screenshots/                    # Project card screenshot images (PNG, 2x retina)
    social/                         # Article cover / OG images (1200×630 PNG, generated)
    diagrams/                       # In-article SVG diagrams and figures (generated)
  scripts/
    gen-social-image.py             # Generates the typographic cover image for an article
    gen-<slug>-diagram.py           # Per-article sketch generators (jittered SVG paths)
    gen-<slug>-figure.py            # Per-article Tufte-style typographic figure generators
  .github/workflows/
    deploy.yml                      # Orphaned GitHub Pages workflow (Netlify is the active deploy)
  astro.config.mjs                  # Site URL + sitemap integration
```

The homepage is one page driven by the `projects` array in `index.astro`. Each object has `title`, `desc`, `tags`, `link`, `linkLabel`, `accent` color, and optional `img` (screenshot path). Cards render in a responsive CSS grid with optional 16:9 screenshot thumbnails.

The `/writing/` section is a list-plus-detail pattern: `src/data/writing.ts` is the registry; `src/pages/writing/index.astro` lists from it; each article is its own `.astro` file under `src/pages/writing/`.

## Key Paths

| Path | What it is |
|------|-----------|
| `src/pages/index.astro` | Homepage: project data + HTML + scoped CSS |
| `src/pages/writing/index.astro` | Writing index page |
| `src/pages/writing/<slug>.astro` | Individual articles |
| `src/data/writing.ts` | Article registry (slug, title, date, excerpt, readTime) |
| `src/styles/global.css` | Design tokens, reset, typography |
| `src/layouts/Layout.astro` | HTML head, SEO meta, OG tags, structured data |
| `docs/writing-guide.md` | Project-specific writing guide for articles |
| `docs/glossary.md` | Working definitions: Jeroen's coined frames + field vocabulary, with drift notes |
| `docs/verification/<slug>.md` | Per-article anti-hallucination verification record. One file per article slug. Step 0 + Steps 4–6 of the agent-ready-papers checklist; confidence tier per claim; recommended Sources block to embed in the article. |
| `docs/workflows/<name>.md` | Numbered workflow steps for adding a project card or an article, loaded on demand from the Before You Start table. |
| `memory/external-comments.md` | Publish events + log of posted LinkedIn / external replies (URLs, reception, reusable phrasings) |
| `memory/external-references.md` | Observed external content filed for later reference (foils, vocabulary) |
| `memory/posted-linkedin/<slug>.md` | Full text of posted LinkedIn cross-posts (Pulse body + short feed post). For reuse as templates. Working examples: `the-work-is-splitting`, `ese-bot-eu-sovereign-rag` |
| `memory/gotcha-log.md` | Problem-fix archive; reviewed at end of session |
| `astro.config.mjs` | Site URL, sitemap integration |
| `package.json` | Dependencies (astro, @astrojs/sitemap) and scripts |
| `public/robots.txt` | Crawl directives |
| `public/screenshots/` | Project card screenshot images |
| `public/social/` | Article cover / OG images (generated, 1200×630 PNG) |
| `public/diagrams/` | In-article SVG diagrams and figures (generated) |
| `scripts/gen-social-image.py` | Generates a typographic cover image; edit the headline + slug constants per article and run `python scripts/gen-social-image.py` |
| `scripts/gen-<slug>-diagram.py` | Per-article sketch diagram generators (jittered paths, sketch register) |
| `scripts/gen-<slug>-figure.py` | Per-article typographic figure generators (Tufte-style data citations) |
| `.claude/agents/` | Three review agents (copy, design, SEO) from prior audits |

## How to Work Here

```bash
# Install dependencies
npm install

# Run local dev server (hot reload)
npm run dev

# Production build (outputs to dist/)
npm run build

# Preview production build locally
npm run preview
```

Deployment is automatic: push to `main` triggers Netlify to rebuild and deploy. Build log visible at https://app.netlify.com.

## Commit Conventions

Conventional-style with `feat:`, `fix:`, etc. Imperative mood. See git log for examples.
