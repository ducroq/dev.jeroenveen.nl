# V&V method for paper writing

*Status: seed note. Captured 2026-05-19 from the working session that drafted, reviewed, and revised `the-model-is-not-the-grader.md`. The session itself is the worked example. Jeroen will write the article in his own voice; this seed exists to preserve the raw material so it does not have to be reconstructed from cold memory.*

---

## The seed

A blog draft on "do not let the LLM grade its own output" was almost shipped with a load-bearing warrant gap that the drafting context did not see. A fresh-session-no-project-context cross-model review pass surfaced it within minutes. The revision addressed it. A second fresh pass on the revision surfaced new issues, including a structural inconsistency the revision had introduced and a voice-register drift the disclosure constraint was forcing. The disjoint-coverage pattern between Haiku (surface/structural) and Opus (argument-quality) reproduced cleanly at both revisions.

The meta-irony is the article-worthy part: an article whose central argument is *do not let the LLM grade its own output* was, in flight, in danger of being graded by the LLM that wrote it. The discipline the article was prescribing for production AI tools is the same discipline the article itself needed. The fresh-pass procedure is the writing-side equivalent of the deterministic-grader move the article describes.

## Why this is article-worthy on dev.jeroenveen.nl

- The session is N=2 within a single working day of the same method on the same piece. Disjoint-coverage reproduced both times with the same shape (Haiku catches surface, Opus catches argument-quality). At blog scale, the method works and is repeatable.
- The meta-frame is genuinely rare. Most pieces about AI writing workflow describe what should happen. This one would describe what *did* happen, with specific findings and specific paragraphs.
- The disclosure constraint that hobbled the first article (no scene available, conceptual mode forced) is not a constraint for this article. The session itself is the scene.
- It is a natural companion to the AE-site cross-model-review pattern essay if/when that lands. Same mechanism, different surface (paper writing rather than equation verification or code review).
- It would land where the V&V arc closer is still owed, without pre-empting the hardware/embedded/control asymmetry post 2 promised. Different fork.

## What happened, in order

**Phase 1: Draft.** Drafted `the-model-is-not-the-grader.md`. Central claim: separating finder from grader (LLM finds, deterministic code grades against a fixed rubric) escapes the evaluator-inherits-actor-assumptions trap that LLM-as-judge / evaluator-optimizer / critic-actor / reflection all share. Length ~770 words. Disclosure constraint: do not describe the system (vmodel.eu), just point at the disciplines.

**Phase 2: Pass 1 cross-model review (rev 0).** Spawned Haiku and Opus in parallel, fresh-session-no-project-context, Variant B of `agent-ready-papers/templates/review-prompt.md`, explicit style/voice rules from `docs/writing-guide.md` §6 inlined.

- **Haiku surfaced (surface/structural):** title misread (Haiku read the subtitle as title), opening overpromise ("the part that takes the longest"), defensive disclosure paragraph, ADR mid-stream lacking grounding, "only question that matters" superlative, abrupt transition to calibration-gate paragraph, "previous pieces" assumes prior reading.
- **Opus surfaced (argument-quality):** *critical warrant gap.* Deterministic grader does not escape finding-time inheritance, only grading-time inheritance; anything the LLM-finder fails to surface never reaches the grader; the claim was too strong. Plus: overreach on "most production AI" without source, contribution clarity (finder/grader split is not novel as a pattern), calibration-gate "match within tolerance" under-defined, rubric-drift counter-argument unaddressed, closing forward-look collapses the value of the piece by promising future pieces on what this piece just discussed.

**The warrant gap was invisible to the drafting context.** The article's whole point depends on the finder/grader split being a structural escape from the inheritance problem. It only half-escapes. The drafting context (Opus with full project context) did not see this. A fresh Opus pass with no project context saw it within minutes.

**Phase 3: Revision 1.** Addressed #1–4 + #8 of the synthesized findings. Key change: new objection-pair paragraph after "the grader has no opinion. it enforces" naming both objections (finder-side blindness defers to a sibling piece; rubric drift sets up the calibration gate as its answer). Softened "most production AI" to "the dominant patterns in the LLM-evaluation literature." Replaced three-mechanism forward-look with single-sentence limitation closer ("what I have not solved is the rubric-drift problem on a longer horizon than the held-out set can see"). Length ~840.

**Phase 4: Pass 2 cross-model review (rev 1).** Same procedure, same model pair.

- **Haiku surfaced (rev 1):** delayed argument naming (decision named in p4, opening in p1), unsourced literature claim, weak ending CTA, paragraph 6 redundancy with paragraph 5 closing, "tests is the wrong word" reads like self-doubt, pronoun scope to prior pieces.
- **Opus surfaced (rev 1):** *second warrant gap.* Claiming grading-time independence does not say why human-priors-in-rubric is *categorically* better than LLM-priors-in-judge (the rubric authors also have priors). *Structural inconsistency.* Paragraph 6 raises rubric drift, paragraph 7 offers the calibration gate as the answer, but the gate only catches *prompt drift against a fixed rubric*, not *rubric drift itself*, which the closing then concedes is unsolved. *Voice register drift identified with specific paragraphs:* paragraphs 2, 8, 9, 10 hold observational voice; paragraphs 3, 5, 6 drift to argument-mode ("They differ in their decoration" and "the grader has no opinion. it enforces" identified as the most rhetorically polished / screenshottable sentences, i.e. the tell). *Unaddressed counter-argument:* the finder/grader split assumes the rubric is expressible as deterministic code; in domains where llm-as-judge actually got traction (tone, helpfulness, "does this answer the question"), the rubric is the hard problem and the split collapses. Domain property, not discipline property.

**The disjoint-coverage pattern held at both revisions.** Haiku caught structural/surface issues both times. Opus caught argument-quality issues both times. The union of the two passes was larger than either alone, both times.

**The voice register drift was forced by the disclosure constraint.** With no scene and no number available (system internals withheld), the load landed on conceptual prose, and conceptual prose under pressure tightens into essay-defense. Opus's specific phrasing: *"the middle of the piece feels written to be defended, where the opening and closing feel written to be recognised."* Independently identified by the drafting context after the first pass; the second pass corroborated with paragraph-level specificity.

## Reusable phrasings (Jeroen's framings during the session)

- *"And is this action we do now a sort of meta-application of the stuff we describe?"* Jeroen's own framing of the meta-frame. Sharp. Probably the article's hook.
- *"Pretty important right?"* The moment of recognising the warrant gap mattered.
- *"Let us do a fresh one then."* When corroboration via a fresh pass was needed because the drafting context could no longer be trusted to grade itself.
- *"Same context with one more iteration on it is not an independent grade."*
- *"The article was almost graded by the LLM that wrote it."*
- *"Don't let me grade my own work in the same context that drafted it."*

## Possible homes

1. **New standalone dev.jeroenveen.nl article.** Argument-form title candidates: *"The article I wrote about not letting the LLM grade itself almost was."* / *"Cross-model review caught what same-model review missed, twice."* / *"A working session that became its own worked example."* / *"The fresh-session discipline."* Lean: first or last. The first leans on the meta-irony; the last names the procedure plainly.
2. **AE-site pattern essay extending cross-model review.** The mechanism is the same as the AE Reproduce-Don't-Assess pattern, applied to writing rather than equations. Could live as a sibling pattern doc on the AE site.
3. **A subsection inside the planned `cross-model-review.md` framework piece** (currently a seed in `drafts/cross-model-review.md`). Lower lift but spends the strongest worked example cheaply.
4. **DR-011 case study.** Lives internally in agent-ready-papers as evidence that the procedure works at blog scale, not just at paper scale.

Lean for the dev.jeroenveen.nl version: option 1 as the standalone, with one paragraph pointing at the AE pattern doc (option 2) once that lands. The standalone earns the meta-frame; the AE doc carries the canonical pattern.

## Open questions before drafting

- **Generality.** This is N=1 piece with N=2 revisions. The disjoint-coverage pattern is consistent within the session. Is it robust across other pieces drafted under different conditions, or specific to this drafting context? Worth checking against the `who-runs-the-drc` pre-pull session and the `senior-developers-trust-ai-less` cross-model pass before publishing any generality claim.
- **How much meta to dwell on.** The article-about-grading-itself almost-graded-itself moment is striking, and one paragraph on it is probably right. Two paragraphs reads as too cute. The piece is stronger if the meta is the hook and the body is the procedure.
- **Whether to include the actual findings or just describe the process.** Including findings (with paragraph references) makes the worked example concrete and verifiable; lengthens the piece. Describing the process generically makes it travel further but undermines the "this actually happened" force. Probably: include 2–3 of the sharpest findings as illustration, do not enumerate all of them.
- **Whether to subject this article to the same procedure.** Almost certainly yes. The piece's authority depends on the procedure being applied to itself. The fresh-pass-on-revision-1 pattern of `the-model-is-not-the-grader` would carry over directly.
- **Cross-reference to `the-model-is-not-the-grader`.** Whether the worked-example article ships before, after, or instead of the piece that prompted it is a separate decision. If `the-model-is-not-the-grader` ships first, this piece can reference it as the case study. If this piece ships first, `the-model-is-not-the-grader` becomes the application of the discipline this piece names. Either order works; the second is more honest about which piece earned which insight.

## Connection to the V&V arc and what's been promised

- **Not** the V&V arc closer against post 2's hardware/embedded/control forward-look (still owed).
- **Adjacent** to the AE-pattern arc that follows. Cross-model review is one of the planned pattern essays; this piece is the worked-example version of it applied to writing.
- **Honestly grounded.** This piece does not need to make any claim about non-software domains, validation-failure asymmetry, or trust surveys. It is a piece about a writing procedure that worked, with the meta-irony of being self-applicable as the hook.

## Decision

Hold as seed. Jeroen will draft when he is ready, in his own voice. This seed preserves the raw material so the working session does not have to be reconstructed from cold memory. The two drafts of `the-model-is-not-the-grader.md` (revision 0 in git history once promoted; revision 1 in the current draft) plus the two cross-model review transcripts (in conversation history) are the primary source material.
