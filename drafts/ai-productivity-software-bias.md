# AI productivity research has a software bias problem.

> **Status:** SHELVED 2026-05-18. The Reframe note below (also 2026-05-18) was the first attempt to redirect this draft from literature-bias complaint toward practitioner observation. It pointed in the right direction but the resulting framing (descriptive AE-cross-domain map) is closer to AE-cross-domain work than V&V arc closure. A subsequent attempt at a V&V arc post 3 (`drafts/who-runs-the-drc.md`) was published 2026-05-18 and pulled the same day after recognising the same arc mismatch: AE-cross-domain piece, not V&V arc closer. Both this draft and `who-runs-the-drc.md` are retained, but neither is the V&V arc post 3. The V&V arc closer remains to be written, grounded in own methods work (Reproduce-Don't-Assess, OPAL's layered verification, etc.). Do not work this file further unless the descriptive-map shape becomes desirable as a later AE-cross-domain piece. See `memory/hypothesis-log.md` for the full diagnosis.
>
> **Status:** REFRAMED 2026-05-18 — see "Reframe note" section directly below. The body further down ("Article body") is the pre-reframe draft, retained for reference but no longer the working spine.
> **Series:** post 3 of 3 in the WHY arc. Closes the arc by *describing* what augmented engineering is, across engineering domains. Bridges into the next arc (AE patterns).
> **Target slug:** TBD. `ai-productivity-software-bias` no longer fits. Candidates: `augmented-engineering-across-domains`, `what-augmented-engineering-is`, `engineering-with-ai-across-domains`. Decide closer to publish.
> **Word count target:** ~600–900 (was ~720; a descriptive map may want slightly more, but tighten relentlessly).

## Reframe note (2026-05-18)

**What changed.** The pre-reframe thesis ("the AI-productivity literature is software-developer literature, therefore the conversation has a software bias") is a methodological complaint about the literature. Posts 1 and 2 are about the *work*; post 3 as drafted pivots to a meta-argument about who got measured. Register shift down, not across. The HAZOP-symmetry note from 2026-05-12 was never actually used in the body. The OPAL N=1 worry was a symptom of the wrong thesis, not the disease.

**New thesis.** Post 3 is the *descriptive piece that earns the #AugmentedEngineering tag.* AI is doing materially different work across engineering domains — code generation in software, surrogate models and topology optimisation in mechanical / aerospace, controller tuning and system identification in control, structure prediction in chemistry, HDL / firmware generation in embedded, RTL / EDA assistance in IC, design-and-compliance assistance in civil / structural — and the validation work has to match the artifact and the ground truth in each domain. The piece *describes* that cross-domain practice, names it as augmented engineering, and the literature-bias observation reduces to one sentence inside the description, not the spine.

**How the arc reads after this reframe.**
- **Post 1**: validation is the new structural problem (the work is splitting).
- **Post 2**: seniors hold the validation cost (pattern library for plausible-but-wrong).
- **Post 3 (reframed)**: here is what that work looks like across engineering domains — this is what augmented engineering means.

The forward pivot then hands cleanly to the AE patterns (Reproduce-Don't-Assess, etc.) at the AE site. Post 3 describes *what AE is*; the next pieces describe *how it's done*.

**What the description carries (the implicit argument).** "AI productivity" and "AI in engineering" name an object that doesn't actually exist as a uniform thing — and the real practice (augmented engineering) is defined by the cross-domain match between AI's output and the validation work, not by the AI tool itself. Sharper than the original literature-bias claim. The description does the argumentative work because the description is what the field is missing.

**Implications for the existing draft.**
- The pre-reframe body (audience-filter opener, JetBrains/Stack Overflow/METR exemplar paragraph, literature-bias spine, "less rhetoric, more craft" closer) is no longer the working draft. All of it needs revisiting under the new thesis.
- The evidence base is no longer "1 published study + OPAL." It's a domain-by-domain descriptive map. OPAL becomes one row (embedded / sensor-shaped output) rather than the load-bearing example.
- Park HAZOP / Naser 2023 / N studies + OPAL — secondary. Cited studies illustrate rows of the map; they do not carry the argument.
- The current diagram (`public/diagrams/ai-productivity-software-bias.svg`, the 86 / 19-37 figure) is obsolete twice over (anchor dropped + the article isn't about numbers anymore). A new typographic *map* (domain × what AI does × validation object) is the candidate, with a hard *It Is Both* register check before drawing (no BEFORE/AFTER, no 2×2 quadrant, no taxonomy tree).
- "Less rhetoric, more craft" may be too taglineable AND may have less work to do if the body is already descriptive. Audit on rewrite.
- AI Transfer Lab's held phrasings ("silent debt until an unrelated change surfaces it" / "the window for noticing closes well before symptoms do") drop off post 3's critical path. Return to the candidate-phrasings bucket in `memory/external-comments.md` for adjacent work.
- The original-draft framing-risk note from 2026-05-12 (post 2 reception, conservative misread risk, HAZOP symmetry, defer adoption pivot) is *defused* by this reframe: a descriptive AE piece cannot easily be claimed as "don't adopt AI" because it describes what adoption already looks like across domains.

**Consultations before drafting the rewrite.**
1. **HAN Digital Engineers literature repo.** Two questions, in order:
   - **Domain × AI-application × validation-object map.** Does the registry already have a table (even partial) for each engineering domain: named AI tools / studies, kind of artifact produced, kind of ground truth required? Skeleton material for post 3's spine. If absent, the article has to assemble it from scratch — and may need to be honest about where the map is thin.
   - **Per-domain validation-practice texture.** Where a domain is covered, what does the registry say about *how* validation is done in that domain (bench tests, simulation, standards compliance, expert reproduction, fabrication, closed-loop stability, etc.)?
2. **AE site (`C:\local_dev\augmented-engineering\`).** What patterns are already publicly named? Post 3 needs to *set up* the patterns the AE site teaches, not duplicate or pre-empt them. The forward pivot only works if the next pieces have somewhere to land.

**Risk to watch on the rewrite.** A pure descriptive piece can read as a survey article — competent but flat. Keep some of the original draft's bite *inside* the description, so the reader's "so what?" lands. The argumentative claim is now structural ("AI in engineering" names a non-uniform object; AE is the frame that captures the real practice), not rhetorical, but it still needs to be felt.

---

## Article body

> **Pre-reframe draft, retained for reference. No longer the working spine. See Reframe note above.**

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
