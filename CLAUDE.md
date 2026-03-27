# dev.jeroenveen.nl

Personal portfolio site for Jeroen Veen (Engineer & Researcher). Single-page Astro static site with project cards, hero section, bio, and footer. Dark theme with amber accent. Deployed to GitHub Pages via CI on push to main.

- **Stack**: Astro 5, TypeScript (strict), CSS custom properties, GitHub Actions
- **Status**: Production (live at https://dev.jeroenveen.nl)
- **Repo**: github.com/ducroq/dev.jeroenveen.nl
- **agent-ready-projects**: v1.3.2

## Before You Start

| When | Read |
|------|------|
| Adding or editing a project card | `src/pages/index.astro` — the `projects` array at the top defines all cards |
| Changing layout, SEO, or meta tags | `src/layouts/Layout.astro` — head, OG tags, structured data |
| Changing design tokens or global styles | `src/styles/global.css` — all CSS custom properties live here |
| Stuck or debugging something weird | `memory/gotcha-log.md` — problem-fix archive |
| Reviewing copy, design, or SEO concerns | `.claude/agents/` — three review docs from previous audit sessions |
| Ending a session | `memory/gotcha-log.md` — review, promote patterns, retire stale entries |

## Hard Constraints

- No JavaScript frameworks or client-side JS — this is a pure static site, zero JS shipped to the browser
- All styling uses CSS custom properties defined in `global.css` — do not introduce Tailwind, Sass, or CSS modules
- The `CNAME` file must stay as `dev.jeroenveen.nl` — GitHub Pages custom domain
- Node 20 for CI (pinned in `.github/workflows/deploy.yml`)
- Keep the site accessible: skip-nav link, `aria-label` on external links, `:focus-visible` styles, semantic HTML

## Architecture

```
dev.jeroenveen.nl/
  src/
    layouts/Layout.astro    # HTML shell: head, meta, OG, structured data, fonts
    pages/index.astro       # Single page: projects array + hero + grid + bio + footer
    styles/global.css       # Design tokens, reset, typography, scrollbar
  public/
    CNAME                   # GitHub Pages custom domain
    robots.txt              # Crawl rules + sitemap pointer
    site.webmanifest        # PWA manifest (name, colors)
  .github/workflows/
    deploy.yml              # CI: npm ci -> build -> deploy to GitHub Pages
  astro.config.mjs          # Site URL + sitemap integration
```

The entire site is one page. The `projects` array in `index.astro` is the primary content — each object has `title`, `desc`, `tags`, `link`, `linkLabel`, and `accent` color. Cards render in a responsive CSS grid.

## Key Paths

| Path | What it is |
|------|-----------|
| `src/pages/index.astro` | The entire page: project data + HTML + scoped CSS |
| `src/styles/global.css` | Design tokens, reset, typography |
| `src/layouts/Layout.astro` | HTML head, SEO meta, OG tags, structured data |
| `astro.config.mjs` | Site URL, sitemap integration |
| `package.json` | Dependencies (astro, @astrojs/sitemap) and scripts |
| `.github/workflows/deploy.yml` | CI/CD pipeline |
| `public/robots.txt` | Crawl directives |
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

Deployment is automatic: push to `main` triggers the GitHub Actions workflow that builds and deploys to GitHub Pages.

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
},
```

## Commit Conventions

Conventional-style with `feat:`, `fix:`, etc. Imperative mood. See git log for examples.
