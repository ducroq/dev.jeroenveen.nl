# The work is splitting. The conversations haven't caught up.

> **Status:** DRAFT, awaiting cold re-read (parked 2026-04-28).
> **Series:** post 1 of 3 (the WHY / framing post).
> **Target slug:** `the-work-is-splitting`
> **Target file:** `src/pages/writing/the-work-is-splitting.astro` once approved.
> **Word count:** ~810.

---

## Article body

**Subtitle:** *An observation from a few years of building with AI agents.*

I keep running into the same moment in my own work. I review something AI helped me produce, and the validation is harder than the production was. Not by a small margin. The output is plausible, well-structured, often impressive on first read. The work of deciding whether it is actually right takes longer than the work of generating it would have, and demands more of me than the generation did.

This is not a complaint about AI. The tools are useful. I have shipped things faster than I would have without them. But somewhere in that speed-up, the work changed shape, and most of the conversations I read about engineering with AI are still describing the old shape.

The standard takes are familiar. Productivity will go up. Junior work will be automated. Learn to prompt. None of them say what I keep noticing, which is more specific and harder to reduce to a slide.

What is happening, in the projects I have looked at carefully, is that engineering work is decomposing into two activities that used to be one. There is the work of producing engineering output: the code, the schematic, the calculation, the report. And there is the work of validating that output: checking it against the physics, the requirements, the standards, the system, the room of possible failure modes that does not appear on the screen. These two were always nominally separate, but in practice they were tangled. You could not produce competent output without thinking about what could be wrong with it. Validation was distributed through the act of writing.

AI breaks that. Production is now cheap and fast. Validation is not. The people I see adopting AI most successfully are the ones who have noticed this and are paying attention to validation as if it were a new kind of work, because in a sense it is. The people I see frustrated are often the ones still treating it as something that happens automatically when the output looks right.

Adoption numbers do not tell you anything about this. About 90% of engineering teams use AI tools now, depending on which survey you trust. That number reads like a triumph. Underneath it sits a different number: the share of teams that can say, with evidence, what their AI use is actually doing to their output quality. In Jellyfish's 2025 survey, only 20% of organisations using AI extensively could measure its impact. The other 80% are doing the work and hoping.

I do not think this is a transient problem. The shape of the change is structural. We are forming habits about how we trust AI-assisted output: in our teams, in our review processes, in our personal sense of what counts as "checked." Habits are easier to form than to revise. Most of the engineers I talk to suspect this without quite naming it. They sense that something about their work has shifted in the last two years, and they are not sure whether to call it productivity gain or something else.

I want to call it something else. The next few pieces here are going to be about what I have been seeing across my own projects, across the engineers I work with, across the published evidence I can verify. The first lens I want to pick up is the one I keep needing in my own work: the gap between producing engineering output and validating it. It is the lens that makes most of the rest of the picture clearer.

If you have noticed your own version of this, if validation has become heavier than production somewhere in your work, or if you have not noticed it but suspect you should be looking, I would like to know where you have seen it. Engineering work is a quiet kind of evidence. Most of it lives in heads and pull requests and design reviews, never written down. The more specifically I can trace where the shape of the work has changed, the less of this I have to write from one engineer's window.

---

## Series context (for the cold re-read pass)

This is the framing post for a three-post arc:

1. **The work is splitting. The conversations haven't caught up.** (this post). Sets up the validation-vs-production lens. Argument-driven, observational voice.
2. **Senior developers trust AI less than juniors.** Counter-intuitive data post. Anchor: JetBrains 2025 Developer Ecosystem survey. ~600 to 800 words. Engagement-shaped.
3. **AI productivity research has a software bias problem.** Domain-differentiation post. Anchor: HAZOP study (86% textual plausibility, 19 to 37% semantic validity). Carves a senior embedded/hardware audience. Soft link out to OPAL on the Augmented Engineering site for methodology depth.

Each post hits a different cognitive register: argument, data, domain. By post 3 the reader has a clear picture of the writer's stance, which is what makes someone hit *follow*.

## Revision notes (what was deliberate in this draft)

- **Opening sentence is the audience filter.** A senior practitioner reads "I keep running into the same moment in my own work" and recognises the habit of pattern-spotting their work depends on. A scroll-by reader does not.
- **The strongest line is sentence two**: *"the validation is harder than the production was."* Per the writing guide's packaging rule, lead with the strongest line.
- **Two numbers, both Jellyfish 2025.** Adoption (90%) paired with measurement (20%) does the structural argument quietly. METR's productivity data is held for post 2.
- **Tension held, not resolved.** "This is not a complaint about AI. The tools are useful. I have shipped things faster than I would have without them. But somewhere in that speed-up, the work changed shape." Both sides on the page.
- **No named colleague.** All observations framed as "the projects I have looked at carefully," "the engineers I work with," "the engineers I talk to." Aggregate, no anchoring on someone else's lived moment.
- **One CTA.** The closing prompt is a single ask, not a contact-stack.
- **Forward look previews post 2** ("the gap between producing and validating") without spending its thesis.
- **No em-dashes.** Five sites in the original draft were converted: four colons, one removal, one comma sequence.

## Open questions for the cold re-read

- Does the third paragraph ("The standard takes are familiar…") drift into the *anti-thing thing* trap (writing guide Section 2 of the canonical AE guide)? "Harder to reduce to a slide" reads sharp. May be fine; may be slightly superior. Check on a fresh read.
- Does the closing trail off, or land? The intent was *open question* per essay-mode rules, not summary. Worth re-reading with that lens specifically.
- Word count is 810. A frame post can be shorter than a thesis post, but check whether any paragraph is doing two jobs and could be split into two cleaner sentences each.
- Subtitle works, but a sharper one might land harder. "An observation that keeps surfacing across my projects" is one alternative. "Notes from inside several years of building with AI agents" is another.

## When ready to publish

1. Move this body into `src/pages/writing/the-work-is-splitting.astro` (use ESE Bot as template).
2. Register in `src/data/writing.ts`.
3. Verify on `npm run dev` reads cleanly cold.
4. Commit, push, deploy.
5. Cross-post to LinkedIn with the title as the post's first line, the comment prompt as the closing line, and a link to the article on the site.
