# Writing Guide — dev.jeroenveen.nl

This guide covers what is distinctive about writing for this site. Universal craft principles (voice protection, the five voice traps, essay vs. chapter, logic audit, tension holding, self-reference dosing) live in the canonical Augmented Engineering writing guide at `C:\local_dev\augmented-engineering\docs\writing-guide.md`. Read that first for craft. This guide adds the project-specific layer: who reads dev.jeroenveen.nl, how articles travel beyond it, and the rules that come from learning what works on this audience.

The voice is the same Jeroen voice used across projects. The audience and packaging are different, and that difference is what this guide is for.

---

## 1. What this site is for

dev.jeroenveen.nl is a personal portfolio with an occasional writing section. Articles live at `src/pages/writing/<slug>.astro` and are listed via `src/data/writing.ts`. The site is the canonical home for each article. LinkedIn posts cross-reference and quote from them, but the article on the site is the durable artifact.

This is *not* a pattern library (that is the Augmented Engineering site). It is *not* a research log. It is *not* a teaching channel. It is the place a senior engineer or AI lead lands when they want to see whether the person behind the projects has anything substantive to say.

Each article should be readable cold by someone who arrived from a Google search or a LinkedIn share. No prior context required.

---

## 2. The reader

| Dimension | Reader |
|-----------|--------|
| Professional context | Mid-to-senior engineer, AI/ML lead, technical decision-maker at an EU company |
| Knowledge level | Has shipped systems. May be using AI tools, may be evaluating them. Has heard the hype |
| Disposition | Pragmatic skepticism. Tired of LinkedIn productivity decks. Reads carefully when given a reason |
| Self-awareness | Suspects most "AI in engineering" coverage is recycled. Wants the specific thing that is actually new |
| What they're NOT | Not students. Not HAN colleagues. Not academic researchers. Not managers reading strategy decks |

Note the difference from the AE guide's reader: that one narrows to engineers *already working with agents*. This site's reader includes engineers who have not yet committed to the practice but read carefully when someone they trust writes about it. Articles here can assume less direct AI tooling experience than AE articles can.

### What they want
- Recognition: "yes, I have noticed that"
- A specific thing they had not noticed before
- A reason to trust the writer enough to follow

### What they don't want
- Promises of transformation
- Institution-flavoured posturing
- A pitch dressed as an essay

---

## 3. Article form

Articles on this site are typically **800–1,500 words**, with the [ESE Bot article](../src/pages/writing/ese-bot-eu-sovereign-rag.astro) as the working template.

The form is **hybrid** (per the AE guide's Section 3): essay-mode opening (observation, scene, paradox), exploration in the middle, and a soft landing. The landing can be a question, a forward look, or a concrete pattern, whichever the body earned. No "key takeaways" boxes. No numbered action items. No "in conclusion."

### Structure that has worked

1. **Opening (1–3 short paragraphs)**: observation grounded in something specific. Either a moment, a project, or a concrete finding. Opening sentence does the audience filtering: a senior engineer should read it and recognize themselves; a generic LinkedIn scroller should bounce.
2. **Middle (5–9 paragraphs)**: the exploration. One idea per paragraph. Specific examples (your own work, named external sources, aggregate observations). Numbers paired with what they mean.
3. **Closing (1–2 short paragraphs)**: image, paradox, forward look, or open question. Optionally a soft contact line.

Avoid lists where prose will do. The bulleted-list problem from the canonical guide applies here too.

---

## 4. LinkedIn packaging

Articles cross-post to LinkedIn, where the title, opening sentence, and a comment prompt do most of the work. These are not optional. Skip them and the substance reaches the wrong audience or none at all.

### Pre-publish packaging checklist

- [ ] **Title is an argument, not an artifact.** "GDPR compliance is a location problem", not "Notes on a chatbot." The reader should know the claim before they click.
- [ ] **Opening sentence test.** If a CTO scanning LinkedIn would scroll past it, rewrite. The sentence has to filter for the audience the article is built for.
- [ ] **Lead with the strongest line.** Find the most quotable, debate-starting sentence in the draft. Move it to the top, or to the title, or to the subtitle. Strong lines buried at paragraph seven do not travel.
- [ ] **One comment prompt at the end.** A sentence that publicly asks the reader something they would answer in comments. Without it, engagement caps at reactions and the algorithm does not push the post into second-degree networks.
- [ ] **Watch for extractable standalone posts inside long articles.** If a section could carry its own LinkedIn post, you may be burying it. Either pull it out for a separate piece or commit to subordinating it.
- [ ] **Voice intact.** Restrained, specific, modest. The fix for low engagement is in *packaging* (title, opening, hook, CTA), not in adopting a louder tone.

### What "argument-form title" looks like

| Artifact-form (avoid) | Argument-form (use) |
|-----------------------|---------------------|
| Notes on a side project | GDPR compliance is a location problem |
| What I learned from N projects | The work is splitting. Most teams haven't noticed |
| A small chatbot | Most "GDPR-compliant" products aren't |

---

## 5. Whose story is yours to tell

Personal practice is yours. Aggregate observations are yours. Published external sources are public material. A named colleague's specific anecdote is not, even when documented in your own case studies, transcripts, or symposium notes.

The rule is not "do not mention colleagues." It is "do not anchor a piece on a colleague's lived moment as if it were yours to narrate."

| OK to use | Not OK | Borderline (ask first) |
|-----------|--------|------------------------|
| Your own projects (OPAL, ese_bot, agent-ready-projects, etc.), even when AI-assisted | Articles centred on a named colleague's anecdote | Brief mention where the article does not depend on them |
| Aggregate / anonymised patterns across multiple cases | Quoting a colleague's specific words from a private symposium as the load-bearing element | Quoting from a published talk or paper they authored |
| Published external sources (METR, JetBrains, Microsoft/CMU, McKinsey…) | "Hugo did X" / "Vincent said Y" framings | Mentioning a debate without naming participants |
| Public debates where the *argument* is the subject, not the named participants | | |

**Substitute pattern.** When a colleague's story is the natural anchor, find the equivalent moment in your own work, or write the cross-case pattern that aggregates without identifying anyone.

---

## 6. What to avoid (specific to this site)

These show up reliably when drafts drift toward institutional or academic framing. Strip them.

| Pattern | Problem | Fix |
|---------|---------|-----|
| HAN / AEA / SLIM / KC / AIM | Institution-flavoured; means nothing to a senior engineer at an EU manufacturer | Drop entirely |
| "Phase transition" / "crystallization window" / "epistemological void" | Academic vocabulary; reads as urgency theatre | Plain language: "practices are forming now"; cut if not load-bearing |
| "The digital engineer" / "the modern developer" as a noun | Sounds like a marketing buzzword | Talk about *engineers*, not *the engineer* |
| "I wanted my students to…" / "in our course we…" | Teacher-coding; pulls the post into the HAN orbit | Reframe around the engineering problem; mention students only if essential |
| "Studies show…" / "Research has demonstrated…" | Academic posturing | Name the source: "METR's 2025 study found…" |
| "Our research shows…" / "We at HAN…" | This is a personal site, not institutional | First person singular when the experience is the point; observation otherwise |
| "If you are building in this space, get in touch" stacked at the bottom | Reads as fundraising | One soft contact line at most. Not on every piece |
| Framework labels: "P1 Validation Primacy," "Three-Layer Competency Architecture" | PhD-defence flavour | Use the underlying idea without the capitalised label |
| **Em-dashes (—)** | Personal voice preference: dislike. Also a known LLM tic; graders and discerning readers spot them | Avoid. Use a colon for list-introduction (`output: the code, the schematic`), a comma or period for pauses, or restructure the sentence. Hyphens (`-`) and en-dashes (`–`) for ranges are fine. **Scope:** the em-dash rule applies to *prose* committed to this repo (articles, glossary entries, draft notes, internal docs, commit messages), not only voice-channel output. The rule is about the repo's prose style. **Non-prose contexts are exempt:** UI labels, project-card titles, navigation separators, and similar short-form headings can use em-dashes if the established pattern does. Canonical example: the project-card titles in `src/pages/index.astro` follow `Name — Tagline`. |

---

## 7. Evidence and citation

Same principle as the canonical guide's *Integrating Evidence* section: weave sources, do not display them.

- Name the source naturally: "JetBrains' 2025 Developer Ecosystem survey found…" not "Studies show…"
- Lead with the finding, then the citation: "Senior developers using AI were 19% slower while feeling 20% faster (METR, 2025)"
- Pair every number with what it means. A statistic alone is inert
- Acknowledge sample honestly: "across the four projects I have looked at" is fine; "engineers in general" is not, unless you cite a study with that scope
- Never present your N=1 observations with the same confidence as a controlled study

When citing your own work, link to the project page or the source (GitHub, the AE pattern page) rather than re-narrating it.

### Verify before publish

Every load-bearing statistic, named study, or coined attribution gets a verification record at `docs/verification/<slug>.md` before the article ships. Apply Step 0 + Steps 4–6 of the [agent-ready-papers anti-hallucination checklist](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md). Trace each number to primary source, not to an intermediate ANALYSIS file or a downstream registry that says it's already verified. The fluency of an existing summary is exactly the surface where citation drift hides.

Map confidence tier to article language:

| Tier | Use when… | Article language |
|---|---|---|
| ESTABLISHED | Verified at primary source, exact numbers | "demonstrates", "shows", "found" |
| SUPPORTED | Verified via registry chain or a partial primary-source extract | "found", "indicates" |
| EMERGING | Plausible but disputed or only partially extracted | "may", "preliminary evidence suggests" |
| SPECULATIVE | Plausible, unverified | "warrants investigation", "remains unclear" |

If a number cannot survive Step 6 (read the relevant section of the primary source and confirm it says what you claim it says), the article either drops the claim or downshifts the language to match the actual confidence tier. Citation drift is silent: the failure mode is to leave the language at ESTABLISHED ("demonstrates X") when the source only supports SUPPORTED ("found X in this sample").

### Cross-model review pass

Every article gets a cross-model review before publish. An agent that helped draft a section has sunk-cost bias in its context and will not catch its own errors there. Same-family models share enough of that bias for the same blind spot to apply at the family level, not just the session level.

Procedure:

1. Article is final in `src/pages/writing/<slug>.astro`, reads cleanly cold.
2. Open a different model (GPT, Gemini) or at minimum a fresh Claude session with no project context.
3. Paste the article body together with the agent-ready-papers [`templates/review-prompt.md`](file:///C:/local_dev/agent-ready-papers/templates/review-prompt.md) (Variant B, non-empirical) as the prompt.
4. Address logic gaps, unsupported assertions, citation drift, and tone issues before pushing. Trivial fixes get a small follow-up commit; structural issues mean back to the draft.

This step is *not* bundled with the heavier academic gates (Toulmin typing, equation verification) that an essay does not need. Those genuinely are overkill for a personal essay. Cross-model review costs a few minutes and catches the class of error that same-model self-review reliably misses, which is a different cost-benefit profile.

### In-article references

Cited sources get two surfaces, working together:

- **Inline link** on the first mention in the prose: `<a href="..." target="_blank" rel="noopener">JetBrains' 2025 Developer Ecosystem survey</a>`. One link per source, on first mention only; repeated mentions don't get re-linked.
- **Sources block** at the end of the article body, listed alphabetically by first author/org. Use `<aside class="article-sources">` with `<span class="article-label">Sources</span>` heading + `<ul>` of citations. The `.article-sources` CSS rule is defined in each article's style block (mono caps amber heading, dim mono list, dotted-amber link underlines). See `src/pages/writing/the-work-is-splitting.astro` or `src/pages/writing/senior-developers-trust-ai-less.astro` for the working pattern.

The verification record (in `docs/verification/`) is the internal audit trail; the inline links + Sources block are the public-facing version of the same evidence chain. Anyone asking *"where does that number come from?"* should be able to follow the inline link to the source page; anyone asking *"how do I know you read it?"* should be able to find the verification record.

---

## 8. End-of-article CTA

Most articles benefit from a short closing line that points somewhere, but only one. Stack three CTAs and the post reads as a marketing page.

Options that have worked:

- **A comment prompt** (LinkedIn-shaped): "When did you start trusting AI less, not more?"
- **A soft contact line**: "If you are building in that space and want to trade notes, I will read the email."
- **A forward look**: "In the next pieces I will write about what I have been noticing, starting with where the work has actually changed."
- **An open question**: leave the reader holding the tension.

Pick one. Not three.

---

## 9. Pre-publish review pass

Read the draft as the target reader (Section 2). Specifically check:

- [ ] **Arc-position audit**: if this article is part of an ongoing arc, does its topic match what prior posts' forward-looks explicitly promised? A stronger draft in the wrong arc is still in the wrong arc. Run this before evaluating the draft on its own merits.
- [ ] **First-sentence audit**: does it filter for the right reader, or could it open a teaching post?
- [ ] **Title is argument-form**, not artifact-form
- [ ] **Strongest line is in the top half**: if it is buried at paragraph seven, restructure
- [ ] **No HAN / institutional jargon** anywhere
- [ ] **No colleague's lived moment** as load-bearing element
- [ ] **One CTA, not three**
- [ ] **Read aloud test**: any sentence that is awkward to say is awkward to read
- [ ] **Voice intact**: restrained, specific, modest, evidence-visible
- [ ] **Numbers paired with meaning**, not floating
- [ ] **No em-dashes** anywhere in the body (use a colon, comma, or sentence break instead)
- [ ] **No "key takeaways" or "in conclusion"**: essay-mode landing
- [ ] **Cross-model review pass** run (different model, or fresh Claude session with no project context, using `templates/review-prompt.md` Variant B). See Section 7.

---

## 10. When to use this guide vs. the AE guide

| If you are writing… | Use |
|---------------------|-----|
| An article for dev.jeroenveen.nl | This guide + canonical guide for craft |
| An article for the Augmented Engineering site | AE guide |
| A LinkedIn post that quotes from / points at a dev.jeroenveen.nl article | This guide (packaging section) |
| A podcast script | AE guide (Section 9) |
| Anywhere there is potential to mention a named colleague | This guide's Section 5 applies regardless of where you publish |

The voice is shared. The audience and form rules diverge. When in doubt, the audience and form constraints in *this* guide override the AE guide's calibration examples (which were written for a narrower reader).

---

## 11. The honest disclaimer

This guide is a working document, not a finished system. It will be wrong about something, and the way to find out is to publish, watch what happens (analytics, comments, who actually shows up to read), and update accordingly. The lessons in Sections 4–6 each came from a specific moment of "oh, that did not land the way I thought." More moments like that are coming. Update this file when they happen.
