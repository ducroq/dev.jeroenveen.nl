# dev.jeroenveen.nl

Personal portfolio site for Jeroen Veen (Research & Engineering). Astro static site with a homepage (projects, writing, background) and a `/writing/` section for articles. Dark theme with amber accent. Deployed to Netlify (auto-rebuilds on push to `main`).

- **Stack**: Astro 5, TypeScript (strict), CSS custom properties, GitHub Actions
- **Status**: Production (live at https://dev.jeroenveen.nl)
- **Repo**: github.com/ducroq/dev.jeroenveen.nl
- **agent-ready-projects**: v1.3.2

## Before You Start

| When | Read |
|------|------|
| Adding or editing a project card | `src/pages/index.astro` — the `projects` array at the top defines all cards |
| Drafting, reviewing, or planning an article | `docs/writing-guide.md` — voice, audience, LinkedIn packaging, what to avoid |
| Adding an article | `src/pages/writing/<slug>.astro` + register in `src/data/writing.ts` |
| Changing layout, SEO, or meta tags | `src/layouts/Layout.astro` — head, OG tags, structured data |
| Changing design tokens or global styles | `src/styles/global.css` — all CSS custom properties live here |
| Stuck or debugging something weird | `memory/gotcha-log.md` — problem-fix archive |
| Reviewing copy, design, or SEO concerns | `.claude/agents/` — three review docs from previous audit sessions |
| Ending a session | `memory/gotcha-log.md` — review, promote patterns, retire stale entries |

## Hard Constraints

- Minimal client-side JS is fine (e.g., card filtering, theme toggle) but avoid heavy frameworks — keep the site fast and lightweight
- All styling uses CSS custom properties defined in `global.css` — do not introduce Tailwind, Sass, or CSS modules
- The `CNAME` file must stay as `dev.jeroenveen.nl` — retained from the GitHub Pages era; Netlify uses the DNS settings directly
- `.github/workflows/deploy.yml` is an orphaned GitHub Pages workflow — do not treat it as active CI. Deployment goes through Netlify.
- Keep the site accessible: skip-nav link, `aria-label` on external links, `:focus-visible` styles, semantic HTML

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
    writing-guide.md                # Voice, audience, LinkedIn packaging — read before drafting
  public/
    CNAME                           # GitHub Pages custom domain
    robots.txt                      # Crawl rules + sitemap pointer
    site.webmanifest                # PWA manifest (name, colors)
    screenshots/                    # Project card screenshot images (PNG, 2x retina)
  .github/workflows/
    deploy.yml                      # Orphaned GitHub Pages workflow (Netlify is the active deploy)
  astro.config.mjs                  # Site URL + sitemap integration
```

The homepage is one page driven by the `projects` array in `index.astro` — each object has `title`, `desc`, `tags`, `link`, `linkLabel`, `accent` color, and optional `img` (screenshot path). Cards render in a responsive CSS grid with optional 16:9 screenshot thumbnails.

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
| `astro.config.mjs` | Site URL, sitemap integration |
| `package.json` | Dependencies (astro, @astrojs/sitemap) and scripts |
| `public/robots.txt` | Crawl directives |
| `public/screenshots/` | Project card screenshot images |
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

## Adding a Project Card

Add an object to the `projects` array in `src/pages/index.astro`:

```js
{
  title: 'Project Name',
  desc: 'One-line description with concrete numbers if possible.',
  tags: ['Tag1', 'Tag2'],
  link: 'https://example.com',
  linkLabel: 'Live',   // or 'Demo', 'Repo'
  accent: '#hex',      // unique accent color for the card top border
  img: '/screenshots/name.png',  // optional screenshot
},
```

## Adding an Article

1. Read `docs/writing-guide.md` first — voice, audience, LinkedIn packaging, what to avoid.
2. Create `src/pages/writing/<slug>.astro` (use the existing article as a template).
3. Register the article in `src/data/writing.ts` so it appears on `/writing/`.
4. Run `npm run dev` and check the article reads cleanly cold.
5. Push to `main`; Netlify rebuilds and deploys.

## Commit Conventions

Conventional-style with `feat:`, `fix:`, etc. Imperative mood. See git log for examples.
