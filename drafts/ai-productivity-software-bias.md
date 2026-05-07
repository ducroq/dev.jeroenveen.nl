# AI productivity research has a software bias problem.

> **Status:** DRAFT, awaiting cold re-read (parked 2026-05-07).
> **Series:** post 3 of 3 in the WHY arc. Domain-differentiation post.
> **Anchor:** Park et al. 2025 (HAZOP, 86% textual / 19 to 37% semantic) + OPAL case study.
> **Target slug:** `ai-productivity-software-bias`
> **Target file:** `src/pages/writing/ai-productivity-software-bias.astro` once approved.
> **Word count:** ~720.

---

## Article body

**Subtitle:** *What gets measured, and what doesn't.*

If you read most industry coverage of AI in engineering, you would conclude that engineering means writing software. The published evidence has a strong opinion about which engineering counts. Most of it counts only one kind.

JetBrains, Stack Overflow, GitHub, METR. Each of these names a survey or study with thousands of respondents. Each is, on inspection, a software-developer survey. The "AI productivity" findings circulating in engineering management discussions trace back, in nearly every case, to a software-developer benchmark or a software-developer survey. The senior-trust gap I wrote about last week was no different. It was JetBrains, Stack Overflow, METR. Three software studies.

Hardware, embedded, control engineering, and chemistry have AI assistance too. They do not have these surveys. That absence has consequences for how the field talks about AI.

The clearest published exception is a 2025 paper by Park and colleagues on AI-assisted hazard and operability analysis in chemical engineering. They asked an LLM to produce HAZOP output for plant scenarios. The result, scored against the textual conventions of HAZOP reports, was 86% plausible. Scored against semantic validity (whether the hazards identified were the actual ones in the scenario) the number was between 19% and 37% correct. The model produced output that read like a HAZOP report. Less than half of it found the hazards.

If you only read the textual-plausibility number, AI is good at HAZOP. If you read the semantic-validity number, AI is in the failure regime where the output looks correct and is not. The two numbers do different jobs. Most coverage uses the first.

A concrete moment from my own work. On OPAL, an ESP32-based optical instrument I have worked on, a five-layer verification process found ten defects in AI-assisted code. A typical single-layer review, of the kind that constitutes most "review" in industry, would have found two. Eight defects required someone to look at the same output through a different lens: not "does it compile" but "does it correspond to the actual sensor's behaviour." The validation work was not optional. It was load-bearing.

This is one project. It is the kind of evidence the published-research conversation does not have for non-software domains, and it suggests the same pattern as Park: AI output that passes a software-style review can fail when subjected to physics, hardware, or domain-specific verification.

Why does the software bias matter? Because the conventional narrative (AI is making engineers more productive, here are the numbers) is doing population-extension work the data does not support. When a chemical engineer or an embedded systems engineer reads a productivity statistic, what is in front of them is software-developer productivity, even if the headline says "engineers." The senior-trust calibration described in last week's piece, the validation gap from two pieces ago, both of those patterns are at work in those domains. They just have not been measured.

This matters for procurement, for training programmes, and for what teams choose to invest in. If you are running an embedded team and the case for AI tooling is built on benchmarks from a different discipline, the case is weaker than it looks. If you are running a chemical engineering team and the only domain-specific study you can cite flagged 19 to 37% semantic validity, the case is something else entirely.

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

- **Title is argument-form** and audience-filtering: an embedded, hardware, control, or chemistry engineer recognises themselves in "software bias problem"; a software-only reader stays for the methodological argument.
- **Strongest line is the opening sentence**: *"If you read most industry coverage of AI in engineering, you would conclude that engineering means writing software."* Counter-claim, modest delivery, sets the audience filter on contact.
- **Three sources, two indirect, one direct**: JetBrains / Stack Overflow / METR (named as the software trio that Post 2 leaned on, now reframed as the bias's exemplar); Park et al. 2025 (the published exception, the article's anchor); OPAL (Jeroen's own concrete moment, the kind of evidence the literature does not have for non-software domains).
- **Numbers paired with meaning**: 86% (textual plausibility) vs 19 to 37% (semantic validity); 10 defects (five-layer review) vs 2 (single-layer).
- **Connection to Post 1 and Post 2** explicit but lean: one short clause linking the senior-trust calibration and the validation gap to the domains under discussion, no re-explaining.
- **Forward look pivots register** rather than promising another argument piece. The arc closes.
- **One CTA**, an open question pointed at the underrepresented domains.
- **No em-dashes.** Originally drafted with two; both rewritten with parentheses.

## Open questions for the cold re-read

- Is the OPAL paragraph's claim verifiable for a senior reviewer who clicks through to the augmented-engineering case study? The "ten defects vs two" framing is documented; the "five layers" needs to map cleanly to what the case study actually documents (bench tests, simulation, peer review, etc.). Verify before publishing.
- Is the sentence "Less rhetoric, more craft" too taglineable? It is at the structural pivot point of the arc, so it carries weight. But it has the rhythm of a slogan. Audit on cold read: does it land as observation or as pull-quote bait? If the latter, soften.
- Does the closing question land specifically enough? "If your domain has been left out…" is broad. A domain-naming variant ("If you are doing chemistry, hardware, embedded, or control work…") might earn more replies. Test on cold read.
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

A small typographic figure is pre-generated at `public/diagrams/ai-productivity-software-bias.svg`. Not a sketch; not a coverage diagram (a domain-coverage sketch would be the asymmetry-as-the-whole-argument move that the *It Is Both* memory rule warns against). Just the headline pair from Park et al. 2025: 86% textual plausibility / 19 to 37% semantic validity. Tufte-style. Drop in mid-article when promoting to `src/pages/writing/`, between paragraph 4 ("...less than half of it found the hazards") and paragraph 5 ("If you only read the textual-plausibility number..."), or wherever the cold re-read lands it.

## When ready to publish

1. Verify the OPAL paragraph against the actual case study documentation.
2. Move body into `src/pages/writing/ai-productivity-software-bias.astro` (use ese-bot or splitting article as template).
3. Register in `src/data/writing.ts`.
4. Generate cover image: edit headline and slug in `scripts/gen-social-image.py`, run, lands at `public/social/ai-productivity-software-bias.png`.
5. Embed `public/diagrams/ai-productivity-software-bias.svg` (already generated).
6. Run `npm run dev`, read cold, ship via Netlify.
7. Cross-post to LinkedIn (Pulse + short feed post + log in `memory/external-comments.md` per CLAUDE.md's three-surface default).
