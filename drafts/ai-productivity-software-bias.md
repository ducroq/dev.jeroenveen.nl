# AI productivity research has a software bias problem.

> **Status:** DRAFT, awaiting cold re-read (parked 2026-05-07).
> **Series:** post 3 of 3 in the WHY arc. Domain-differentiation post.
> **Anchor:** TBD published study (hardware / embedded / control domain) + OPAL case study. Park HAZOP dropped 2026-05-11 to avoid AlphaFold foil; candidate replacements in publish-prep section.
> **Target slug:** `ai-productivity-software-bias`
> **Target file:** `src/pages/writing/ai-productivity-software-bias.astro` once approved.
> **Word count:** ~720.

---

## Article body

**Subtitle:** *What gets measured, and what doesn't.*

If you read most industry coverage of AI in engineering, you would conclude that engineering means writing software. The published evidence has a strong opinion about which engineering counts. Most of it counts only one kind.

JetBrains, Stack Overflow, GitHub, METR. Each of these names a survey or study with thousands of respondents. Each is, on inspection, a software-developer survey. The "AI productivity" findings circulating in engineering management discussions trace back, in nearly every case, to a software-developer benchmark or a software-developer survey. The senior-trust gap I wrote about last week was no different. It was JetBrains, Stack Overflow, METR. Three software studies.

Hardware, embedded, and control engineering have AI assistance too. They do not have these surveys. That absence has consequences for how the field talks about AI.

<!-- TODO 2026-05-11: published-study anchor (hardware / embedded / control). Park HAZOP dropped to avoid AlphaFold foil. Replacement candidates in publish-prep section: Naser 2023 (FE/PE exam, civil / structural — local PDF available, registry VERIFIED P0, dramatic 0% structural-design number), Akolekar 2025, Moss 2025 (arXiv:2506.14567), Ghosh & Mittal (arXiv:2511.14478), other registry P1-H4 entries (IC, power, electronics). Verify domain alignment + run Step 0-6 anti-hallucination checklist before drafting the paragraph here. The article needs a published study to back OPAL (N=1); without one the argument rests on Jeroen's own work alone, which his own rules flag as insufficient. -->

A concrete moment from my own work. On OPAL, an ESP32-based optical instrument I have worked on, a five-layer verification process found ten defects in AI-assisted code. A typical single-layer review, of the kind that constitutes most "review" in industry, would have found two. Eight defects required someone to look at the same output through a different lens: not "does it compile" but "does it correspond to the actual sensor's behaviour." The validation work was not optional. It was load-bearing.

This is one project. It is the kind of evidence the published-research conversation does not have for non-software domains, and it suggests the pattern: AI output that passes a software-style review can fail when subjected to physics, hardware, or domain-specific verification.

Why does the software bias matter? Because the conventional narrative (AI is making engineers more productive, here are the numbers) is doing population-extension work the data does not support. When a chemical engineer or an embedded systems engineer reads a productivity statistic, what is in front of them is software-developer productivity, even if the headline says "engineers." The senior-trust calibration described in last week's piece, the validation gap from two pieces ago, both of those patterns are at work in those domains. They just have not been measured.

This matters for procurement, for training programmes, and for what teams choose to invest in. If you are running an embedded, hardware, or control engineering team and the case for AI tooling is built on benchmarks from a different discipline, the case is weaker than it looks.

The pieces after this one will not be more arguments about the gap. They will be about what people are doing in their actual work, mine included. Less rhetoric, more craft.

If your domain has been left out of the AI-productivity conversation, what does the conversation get wrong about your work?

---

## Series glue check (Post 1 → Post 2 → Post 3)

- **Post 1** sets up validation as the new structural problem and ends pointing forward to "the next pieces" about the gap.
- **Post 2** tightens to software-developer trust data (JetBrains, Stack Overflow, METR), explicitly flags the data as software-only, and forward-points to "another split that aggregate numbers hide."
- **Post 3** opens directly into the software-bias problem, references the senior-trust gap from last week's piece by name, and references "the validation gap from two pieces ago." Direct callback to both prior pieces, no need to re-explain.
- **Forward look from Post 3** pivots away from arc-arguments toward solution-shaped pieces ("what people are doing in their actual work, mine included. Less rhetoric, more craft."). Sets up the three solution sketches in `drafts/` (`task-triggered-pointers`, `layered-memory`, `adaptive-curate`) without naming them, so the pivot is open.

The arc closes coherently: each post hits a different cognitive register (argument → data → domain), each forward look earns the next piece, the third forward look hands the reader off to a new register (craft) rather than promising a fourth WHY post.

## Revision notes (what was deliberate in this draft)

- **Title is argument-form** and audience-filtering: an embedded, hardware, or control engineer recognises themselves in "software bias problem"; a software-only reader stays for the methodological argument.
- **Strongest line is the opening sentence**: *"If you read most industry coverage of AI in engineering, you would conclude that engineering means writing software."* Counter-claim, modest delivery, sets the audience filter on contact.
- **Three sources, two indirect, one direct**: JetBrains / Stack Overflow / METR (named as the software trio that Post 2 leaned on, now reframed as the bias's exemplar); TBD replacement published study from hardware / embedded / control domain (Park HAZOP dropped 2026-05-11 to avoid AlphaFold foil; candidate replacements in publish-prep section); OPAL (Jeroen's own concrete moment, the kind of evidence the literature does not have for non-software domains).
- **Numbers paired with meaning**: TBD (replacement study's headline numbers); 10 defects (five-layer review) vs 2 (single-layer).
- **Connection to Post 1 and Post 2** explicit but lean: one short clause linking the senior-trust calibration and the validation gap to the domains under discussion, no re-explaining.
- **Forward look pivots register** rather than promising another argument piece. The arc closes.
- **One CTA**, an open question pointed at the underrepresented domains.
- **No em-dashes.** Originally drafted with two; both rewritten with parentheses.

## Open questions for the cold re-read

- Is the OPAL paragraph's claim verifiable for a senior reviewer who clicks through to the augmented-engineering case study? The "ten defects vs two" framing is documented; the "five layers" needs to map cleanly to what the case study actually documents (bench tests, simulation, peer review, etc.). Verify before publishing.
- Is the sentence "Less rhetoric, more craft" too taglineable? It is at the structural pivot point of the arc, so it carries weight. But it has the rhythm of a slogan. Audit on cold read: does it land as observation or as pull-quote bait? If the latter, soften.
- Does the closing question land specifically enough? "If your domain has been left out…" is broad. A domain-naming variant ("If you are doing hardware, embedded, or control work…") might earn more replies. Test on cold read.
- Word count is ~720, well inside the 600 to 800 series target.

## Voice and constraint audit (already passed)

- ✅ No HAN / AEA / SLIM / KC / AIM
- ✅ No "the digital engineer" / "the modern developer" framing
- ✅ No "studies show" / "research has demonstrated"
- ✅ No "we at HAN" / "in our course"
- ✅ No framework labels in capitalised form
- ✅ No em-dashes anywhere in the body
- ✅ One CTA only
- ✅ Sources named, not parenthesised in IEEE form
- ✅ Modest register: observational, evidence-visible
- ✅ Non-management-book audit: no BEFORE/AFTER framing, no numbered patterns, no taglineable single image (closing line audited explicitly above), no "five things engineers should do"

## Diagram

Figure needs regeneration. The current `public/diagrams/ai-productivity-software-bias.svg` shows the Park HAZOP 86% / 19-37% pair, which is no longer the article's anchor (dropped 2026-05-11 along with chemistry). Regenerate after the replacement study from the hardware / embedded / control domain is chosen and verified. The register stays the same (Tufte typographic, not a sketch; not a coverage diagram per the *It Is Both* memory rule).

## When ready to publish

1. **Citation verification.** Build a verification record at `docs/verification/ai-productivity-software-bias.md` modeled on the post-2 record. Required Step 6 reading at primary source for each cited claim. Local PDFs available in HAN Digital Engineers project at `OneDrive - HAN/Research/Digital engineers/sources/pdfs/`:
   - **Recommended candidate**: `Naser-2023-FE-PE-Exam.pdf` — 0% structural design, 70.9% FE overall (registry P1-H4b VERIFIED P0). Civil / structural is physical-stakes-adjacent to embedded; dramatic 0% number parallels the dropped Park HAZOP 19-37% finding without invoking AlphaFold counter-foil.
   - Other candidates: Akolekar 2025, Oblitas, Moss 2025 (arXiv:2506.14567), Ghosh & Mittal (arXiv:2511.14478) — fetch via arXiv / DOI. Confirm domain alignment with hardware / embedded / control before selecting.
   - HAN registry has these all at VERIFIED P0/P1 — see `propositions/CLAIM-REGISTRY.md` claims P1-H4a–h
2. **Consider broadening the evidence base** beyond Park + OPAL. Registry P1-H4 has 8 cross-domain validation studies (chemical, civil, mechanical, IC, power, electronics) showing the same plausible-but-wrong pattern. Currently the article uses 1 + own work. Stronger argument with 3–4 + own work (the cross-domain convergence is itself the evidence for "this isn't software-specific").
3. Verify the OPAL paragraph against the actual case study documentation (`OneDrive - HAN/Research/Digital engineers/case-studies/opal-design-review.md`). Article's "five-layer verification process found ten defects… single-layer review would have found two" needs to match registry P1-H8a–c claims.
4. Move body into `src/pages/writing/ai-productivity-software-bias.astro` (use ese-bot or splitting article as template).
5. Register in `src/data/writing.ts`.
6. Generate cover image: edit headline and slug in `scripts/gen-social-image.py`, run, lands at `public/social/ai-productivity-software-bias.png`.
7. Embed `public/diagrams/ai-productivity-software-bias.svg` (already generated).
8. Add inline source links + Sources block at the bottom of the article (style decision logged 2026-05-10).
9. Run `npm run dev`, read cold, ship via Netlify.
10. Cross-post to LinkedIn (Pulse + short feed post + log in `memory/external-comments.md` per CLAUDE.md's three-surface default).
