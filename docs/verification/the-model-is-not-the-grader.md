# Verification record: *Most production AI grades its own output.*

**Article**: `src/pages/writing/the-model-is-not-the-grader.astro` (status: shipping 2026-05-19)
**Article slug**: `the-model-is-not-the-grader`
**Last verified**: 2026-05-19
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md), adapted for a non-citation-heavy observational piece.

This piece has no external statistics, no named studies, and no quantitative claims to verify against primary sources. The verifiable surface is the characterisation of field patterns and the own-work disciplines. Confidence tiers map per `docs/writing-guide.md` §7.

---

## Claim 1: Named LLM-evaluation patterns

**Article wording (paragraph 3)**:
> The dominant patterns in the LLM-evaluation literature: llm-as-judge, self-consistency check, evaluator-optimizer, critic-actor, reflection. They differ in their decoration. They share one property: the evaluator inherits the actor's assumptions, because they came from the same training distribution and they are reading the same artifact in the same way.

| Check | Result |
|---|---|
| Are these terms in circulation? | ✓ All five appear in standard LLM-eval / agent-pattern vocabulary |
| Primary references | `docs/glossary.md` field-vocabulary section (llm-as-judge, evaluator-optimizer/critic-actor); Anthropic's "Building effective agents" essay (evaluator-optimizer); the "15 Agent Patterns" post filed in `memory/external-references.md` (all five) |
| Step 4 (scope match) | ✓ All five patterns are mechanisms where an LLM evaluates LLM output. The article's characterisation matches what these patterns are designed to do. |
| Step 5 (exact location) | Glossary entries on evaluator-optimizer / critic-actor, llm-as-judge are house-defined; the 15-pattern foil entry lists all five as Tier 3 patterns. |
| Step 6 (the shared-property characterisation) | ✓ The "evaluator inherits the actor's assumptions" reading is exactly what the glossary's evaluator-optimizer entry says under "Drift to watch for": *"the patterns presume the evaluator or critic is independent of the actor. In production this is usually false: same team builds both, same training distribution underlies both, often the same base model with different prompts."* |
| Confidence tier | **SUPPORTED** for the vocabulary; **SUPPORTED** for the shared-property claim |
| Article language | "share one property" (appropriate; no "demonstrates" / "proves" claim) |

**Notes**: The shared-property claim is a structural argument, not an empirical one. The article presents it as a structural property of these patterns (which it is), not as something measured. Confidence tier matches the language used.

---

## Claim 2: "Most production AI grades its own output" (title and central thesis)

**Article wording (title and paragraph 3)**:
> Most production AI grades its own output. […] That sounds obvious until you look at the dominant patterns in the LLM-evaluation literature.

| Check | Result |
|---|---|
| Is "most" a quantified claim? | The title is a colloquial generalisation; the body softens to "the dominant patterns in the literature… share this property." That is the actually-defended claim. |
| Step 4 (scope match) | ✓ The defended claim (the dominant *patterns* in the *literature* share this property) is what the rest of the article actually argues. The title is a stronger colloquial phrasing of it. |
| Step 6 (would a survey support the title literally?) | No survey of production AI tools and their evaluation architectures exists, as far as I am aware. The title is therefore unverifiable as a strict empirical claim. The body's reframing to "the dominant patterns in the literature" is the defensible version. |
| Confidence tier | **EMERGING** for the literal title; **SUPPORTED** for the body's reframed version |
| Article language | Body language is appropriately hedged. The title is more polemical, which is the function of titles. |

**Caveat**: A reader who challenges the title literally has a defensible challenge. The body's hedging is what answers it. If the title is excerpted (e.g., in a LinkedIn share) without the body's reframing, the excerpted form is over-confident. Acceptable risk for the LinkedIn-cross-post context; flag if the title appears as a standalone in future surfaces.

---

## Claim 3: Rubric drift in response to LLM behaviour

**Article wording (paragraph 6)**:
> Rubrics edited in response to disagreements with the finder will drift toward what the finder surfaces well. The grader inherits the rubric, which inherits whatever pressure the LLM's failure modes put on the people maintaining it.

| Check | Result |
|---|---|
| Source type | Own observation from the year of building work |
| Primary reference | Author's ADR record (not public; lives in the production system the article does not describe) |
| Step 4 (scope match) | ✓ The phenomenon described is what happens in any rubric-maintenance loop where the rubric authors see the LLM's outputs |
| Step 6 (independent corroboration) | Indirect: the broader literature on Goodhart-style measure-drift in evaluation pipelines supports the structural mechanism. No specific cited source. |
| Confidence tier | **EMERGING** to **SPECULATIVE** for the general claim; **SUPPORTED** for the author's own case |
| Article language | "will drift toward what the finder surfaces well": modal "will" is slightly stronger than the evidence supports for the general claim. "Tend to drift" would be tighter. Acceptable as written because the surrounding context makes clear this is observation, not assertion. |

**Open**: This is the article's most aggressive own-observation claim. The closing paragraph ("what I have not solved is the rubric-drift problem on a longer horizon than the held-out set can see") explicitly hedges it as an unsolved problem. The combination of body assertion + closing concession reads as honest.

---

## Claim 4: Calibration gates as an own-work discipline

**Article wording (paragraph 7)**:
> Every time we change a prompt, the new prompt runs against a small set of cases we already know the right answers to. The grader scores them, and those scores get compared to what the old prompt got. If they match closely enough, the change ships. If they do not, the change is blocked.

| Check | Result |
|---|---|
| Source type | Own implementation, not described in detail per disclosure constraint |
| Primary reference | Author's production system (not public); ADR record (not public) |
| Step 6 (is the discipline as described real?) | ✓ Yes. The author has been running this for ~one year. |
| Confidence tier | **ESTABLISHED** for own implementation; **SUPPORTED** as a generalisable pattern (the measurement-instrument analogy is from metrology; calibration-against-baseline is standard ML/eval practice) |
| Article language | Procedural description, no over-claim on generality |

---

## Sources block

Not recommended for inclusion in the article. The piece does not cite external research; an empty Sources block would look weird. The references that *do* matter (glossary, 15-pattern foil) are internal vocabulary infrastructure, not citable evidence.

---

## Cross-model review log

| Pass | Model | Date | Findings |
|---|---|---|---|
| Pass 1 | Haiku | 2026-05-19 | Surface/structural (rev 0): title misread artifact, opening overpromise, defensive disclosure, ADR mid-stream weak, "only question that matters" superlative, transition smoothness, "previous pieces" assumes prior reading |
| Pass 2 | Opus | 2026-05-19 | Argument-quality (rev 0): **critical warrant gap** (finder-side inheritance not addressed), overreach on "most production AI" without source, contribution clarity (finder/grader split is not novel as a pattern), calibration-gate "match within tolerance" under-defined, rubric-drift counter-argument unaddressed, forward-look collapses value |
| Pass 1 | Haiku | 2026-05-19 (rev 1) | Delayed claim-naming, unsourced literature claim, weak ending CTA, paragraph redundancy, "tests is the wrong word" weak, pronoun scope to prior pieces |
| Pass 2 | Opus | 2026-05-19 (rev 1) | Second warrant gap (human-priors-in-rubric), structural inconsistency (calibration gate addresses prompt drift not rubric drift), voice register drift identified with specific paragraphs, unaddressed counter-argument on domain applicability |

**Revisions applied**: rev 0 findings #1–4 + #8 substantively; rev 1 findings addressed via the polish pass (paragraph 6 redundancy trimmed, "tests is the wrong word" caveat dropped, CTA sharpened). Voice-register drift acknowledged but not fully fixed (would require scene-anchored rewrite, deferred as proportionality call for blog-scale piece).

**Remaining known issues**:
- Voice register tightens in paragraphs 3–6 ("they differ in their decoration", "the grader has no opinion. it enforces" identified as rhetorical anchors).
- Domain-applicability counter-argument (finder/grader split assumes rubric is expressible as deterministic code) is not engaged in the body. Acceptable for a piece grounded in a domain where the rubric is in fact expressible; would need to be addressed if the piece is repositioned as a general claim.

These are documented here rather than blocking publish per the writing-guide §11 framing: ship, watch reception, update.

---

## Meta-note

This article was the worked example for `drafts/vv-method-for-paper-writing.md`. The cross-model review pass we just used to verify it is also the subject of that future piece. The disjoint-coverage pattern reproduced at both rev 0 and rev 1.
