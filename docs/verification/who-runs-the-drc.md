# Verification record — *Who runs the design-rule check?*

**Article**: was at `src/pages/writing/who-runs-the-drc.astro`, deleted 2026-05-18 (status: **PULLED**)
**Former live URL**: https://dev.jeroenveen.nl/writing/who-runs-the-drc/ (now 404)
**Pull note (2026-05-18, same day as publish):** Article was published earlier today and pulled the same day after recognising an arc-position mismatch. Live for approximately two hours. No LinkedIn cross-post issued; no external links recorded. This verification record is retained as the audit trail of the verification work that was done. The decision to pull was about arc-position, not verification: post 2 promised the survey/research asymmetry in non-software domains; the published article delivered a platform-architecture comparison in non-software AI. Same domain, different topic. The piece pre-empted the methods pieces that should be the V&V arc closer. See `memory/hypothesis-log.md` Resolved entry for the full diagnosis. The draft and the post-publish edits (credit paragraph, validation-tone tune-downs) live on in `drafts/who-runs-the-drc.md` for any future recast as an AE-cross-domain piece.

**Post-publish edit (2026-05-18, before pull):** Added an upfront credit paragraph naming the three teams' engineering achievement (paragraph 2, between Adafruit lede and tscircuit-docs paragraph). Tuned down validation-criticism in three places to make room and soften the verdict-tone: (1) removed the abstract *"the verification distribution is the agent's verification distribution"* sentence in the Zoo paragraph (mechanism + intuition sentences still close the warrant); (2) *"failure mode"* → *"limit"* in the Zoo comparative paragraph; (3) *"correctly identifies what validation requires"* → *"treats independence as a structural property of the system rather than a habit of the user"* in the cad-khana comparative paragraph. Description in frontmatter softened from *"Only one answer holds up to the definition of the word"* to *"One structural answer stands apart from the other two."* **No claim status changes; all verified claims still hold.** Net word change roughly +45.
**Article slug**: `who-runs-the-drc`
**Last verified**: 2026-05-18
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md).
**Ground truth**: Primary-source URLs (platform documentation, GitHub repositories, vendor research pages). No HAN registry chain for this article — the claims are about live platforms, not academic studies, so primary-source URLs are the ground truth.
**Arc**: WHY post 3 (closes the arc; posts 1 & 2 published).

This record is the audit trail for every load-bearing fact in the article: each direct quote, each numeric claim, each platform attribution. Confidence tier per claim maps to article language per writing-guide Section 7.

---

## Confidence tiers used in this record

Per agent-ready-papers convention, a claim's tier maps to the language used in the article:

| Tier | Language | Use when |
|---|---|---|
| ESTABLISHED | "demonstrates", "shows", "confirms" | Verified at primary source, exact quote / number match |
| SUPPORTED | "found", "reports", "evidence suggests" | Verified via canonical secondary source or registry chain; primary-source extraction may be partial |
| EMERGING | "may", "appears to" | Plausible but not yet primary-source-verified |
| SPECULATIVE | "may be", "warrants investigation" | Hedged claim; verification pending |

---

## Claim 1 — Adafruit "first vibed PCB" opening

**Article wording (paragraph 1)**:
> In May, [Adafruit](https://blog.adafruit.com/2026/05/07/making-electronics-with-tscircuit-via-codex-no-kicad-altium-eagle/) reported what may be the first PCB that was "vibed" into a fab order: a complete board, designed end to end by an agent, sent straight to manufacturing. The platform was [tscircuit](https://tscircuit.com/), and the agent was Codex. No human touched the layout. The brief was a sentence; the output was a board.

| Check | Result |
|---|---|
| Source URL | `https://blog.adafruit.com/2026/05/07/making-electronics-with-tscircuit-via-codex-no-kicad-altium-eagle/` |
| Step 0 (existence) | ✓ Post exists. Browser-fetched by Jeroen 2026-05-18 (full text relayed). |
| Step 4 (scope match) | ✓ Post is Adafruit's coverage of tscircuit founder Seve Ibarluzea showing Codex + tscircuit producing PCBs from prompts, with photos of the unboxed boards. |
| Step 5 (exact location) | ✓ The "first" framing appears in the post as a verbatim quote from Seve (apparently from his X posts), embedded in the Adafruit write-up. |
| Step 6 (read section) | ✓ **Direct primary-source verification done 2026-05-18 (via browser).** |
| Confidence tier | **SUPPORTED** — article's "may be the first" matches Seve's "these may be the first fully vibed PCBs ever made" hedge exactly. Adafruit is a secondary source (relaying Seve's tweets); Seve is the primary. The "may be" hedge originates in the primary source itself. |
| Article language | "may be the first" — appropriate for SUPPORTED tier with the hedge preserved |

**Primary-source findings (2026-05-18)**:

The post's date is **May 7, 2026, 2:23 pm**. Title: *"Making electronics with TSCircuit via Codex, without KiCad/Altium/Eagle"*. Adafruit summarises: *"Seve shows how Codex, working with tscircuit, can design an electronic circuit and have it build a PCB, ready to fabricate with design files, using simple prompts."* Adafruit then quotes Seve verbatim:

> *"The PCBs we unboxed today. Perfectly working (within their tolerances), these may be the first fully vibed PCBs ever made. No KiCad/Altium, no manual routing, made by software devs in our community. I didn't review the designs but software devs in the community reviewed it – these are definitely not 'one shot'."*

This changes three details in the article's current opening, all minor but worth fixing:

**Nuance A — "No human touched the layout" is too strong.** Seve's actual claim: *"No KiCad/Altium, no manual routing, made by software devs in our community."* Humans wrote the prompts; humans reviewed the designs ("software devs in the community reviewed it"); the iteration was multi-shot ("definitely not 'one shot'"). What was absent is *manual routing in conventional CAD tools*, not *human involvement in the loop*. Recommended fix: *"No conventional CAD, no manual routing. The brief was prompts; the output was a board."* Keeps the punchy opening, accurate to source.

**Nuance B — "The brief was a sentence" overstates.** Adafruit's wording is *"simple prompts"* (plural). Recommended fix above already addresses this with *"The brief was prompts"*. Alternative: *"The brief was natural language."*

**Nuance C — Paragraph 3's "same engineer who wrote the prompt" framing is too narrow for the Adafruit/Seve case.** Seve says *"I didn't review the designs but software devs in the community reviewed it."* So in the actual reported case, review *was* done by humans other than the prompter — a social-validation form that is more independent than "same engineer in same session." The article's broader point (tscircuit has no platform-side automated validation; validation is wherever humans choose to put it) survives. But the literal *"same engineer who wrote the prompt, looking at the same artifact… in the same session"* doesn't describe what Seve reported.

Two ways to handle Nuance C:

- **Option C1 (keep the platform-mechanism focus):** Rewrite the offending sentence to *"The check is by whichever humans the user enlists — themselves, their team, their community. None of them is the build system. None of them runs automatically. That is not platform-side independence; whether it is human-side independence depends entirely on who is enlisted and how."*
- **Option C2 (concede the social-review variant explicitly):** *"In Adafruit's reporting, the boards were reviewed by software devs in the founder's community — humans, not the platform. That is social validation, which has its own independence properties, but it is not validation the platform provides. The platform has no automated check. Whatever validation happens, the user provides — by themselves, or by enlisting others."*

Recommend **Option C1** — keeps the article's parallel structure across the three platforms (each section ends with a verdict on independence) without diverting into a sub-paragraph about social vs. automated validation. Option C2 is more honest to the specific Adafruit case but breaks the parallel cadence; worth it only if you want the article to engage the community-review point head-on.

**Note on attribution layering**: The article currently reads as *"Adafruit reported [X]."* More precise: *"Adafruit reported on tscircuit founder Seve Ibarluzea's claim that [X]."* Probably overcorrection for a blog-format piece — *"Adafruit reported"* + the "may be" hedge is defensible, and the inline link lets the reader trace the chain. Worth noting but not necessarily worth rewriting.

---

## Claim 2 — tscircuit quote + absence of automated validation

**Article wording (paragraphs 2–3)**:
> The tscircuit documentation, in its own words, names the safety net. "Always check that all components are properly connected." That sentence is the entire validation layer between the model and the fabrication house. The maintainers are not hiding it. They mean it.
>
> […]
>
> The first answer is tscircuit's […]. The platform has no automated electrical rule check, no automated design rule check, no manufacturability gate. The board you receive from the agent goes to the fab unless you stop it.

| Check | Result |
|---|---|
| Source URL | `https://docs.tscircuit.com/guides/circuit-generation/generating-circuit-boards-with-ai` |
| Step 0 (existence) | ✓ Page exists, fetched 2026-05-18 |
| Step 4 (scope match) | ✓ Page documents the AI generation flow for tscircuit |
| Step 5 (exact location) | ✓ Quote appears in the "Tips for Working with AI" section as the first bullet |
| Step 6 (read section) | ✓ **Direct primary-source verification done 2026-05-18.** Quote is exact: *"Always check that all components are properly connected."* Full surrounding sentence: *"Verify connections: Always check that all components are properly connected."* (The article extracts the substring after the colon.) |
| Confidence tier | **ESTABLISHED** for the quote and for the absence of automated validation gates |
| Article language | Direct quotation. Appropriate. |

**Primary-source findings (2026-05-18)**:

The "Tips for Working with AI" section contains **three** manual review steps, not one:

1. *"Verify connections: Always check that all components are properly connected"*
2. *"Review footprints: Confirm that selected footprints match your manufacturing requirements"*
3. *"Preview and iterate: Run `tsci dev` to see the design"*

The page does **not** describe any automated ERC, DRC, or manufacturability gate built into the AI generation flow. All three review steps are user-side. The article's broader claim ("no automated electrical rule check, no automated design rule check, no manufacturability gate") is **verified by the absence** of such language at the primary source.

**Phrasing flag worth a cold-read pass**:

The article's line *"That sentence is the entire validation layer between the model and the fabrication house"* is rhetorically punchy but technically slightly overstates: the docs offer three manual review steps, not one. The argument the article makes (none of them are automated; all rely on the user) is untouched.

Two options for the rewrite, by preference:

- **Option A (acknowledge the three steps, keep the argument):** *"The tscircuit documentation, in its own words, names the safety net — three bullet points in a 'Tips for Working with AI' section: 'Verify connections,' 'Review footprints,' 'Preview and iterate.' All three are user-side. None are automated. The first reads: 'Always check that all components are properly connected.' The maintainers are not hiding it. They mean it."*
- **Option B (soften the framing without showing the list):** *"The tscircuit documentation, in its own words, names the safety net. 'Always check that all components are properly connected.' That sentence captures the entire validation posture between the model and the fabrication house — a manual review checklist, no automated gate. The maintainers are not hiding it. They mean it."*

Recommend **Option A** for the verification-record-grade version, **Option B** if the article is tight on length and Jeroen wants to keep the punchy original cadence. Either is defensible; the *current* phrasing as drafted (*"That sentence is the entire validation layer"*) is the only one that's technically inaccurate.

---

## Claim 3 — Zoo Zookeeper: launch date + two direct quotes

**Article wording (paragraph 4)**:
> The second answer is [Zoo.dev's](https://zoo.dev/research/zookeeper), built into Zookeeper, the conversational CAD agent shipped with Zoo Design Studio in January. Zoo describes the agent's verification posture this way: it "frequently executes the model to check for errors, and it reviews the geometry via multi-view snapshots," with access to "computational tools for engineering, such as center of mass location, mass calculation, and surface area and volume measurements." The agent behaves like an engineer. It runs the model. It looks at it. It measures.

| Check | Result |
|---|---|
| Source URL | `https://zoo.dev/research/zookeeper` |
| Step 0 (existence) | ✓ Page exists, fetched 2026-05-18 |
| Step 4 (scope match) | ✓ Page is Zoo.dev's research write-up on Zookeeper |
| Step 5 (exact location) | ✓ Both quotes appear in a single paragraph describing Zookeeper's design philosophy. Launch date appears in adjacent context. |
| Step 6 (read section) | ✓ **Direct primary-source verification done 2026-05-18.** Both quotes verbatim. Launch date verbatim: *"In January 2026, we shipped our conversational agent as 'Zookeeper' with Zoo Design Studio v1.1."* The article's *"shipped with Zoo Design Studio in January"* is correct paraphrase. |
| Confidence tier | **ESTABLISHED** for both quotes and the launch date |
| Article language | Direct quotations + paraphrase. Appropriate. |

**Primary-source context (2026-05-18)**:

- Quote 1 verbatim source: *"Zookeeper is designed to behave like an engineer: It searches for and reads documentation as it works, it frequently executes the model to check for errors, and it reviews the geometry via multi-view snapshots."*
- Quote 2 verbatim source: *"…additional tools for connecting to the Zoo CAD engine, writing, executing and debugging KCL, and analyzing 3D models via visual snapshots and computational tools for engineering, such as center of mass location, mass calculation, and surface area and volume measurements."*
- The article's *"The agent behaves like an engineer"* is essentially a paraphrase of Zoo's own *"Zookeeper is designed to behave like an engineer"* — the article presents this as the article's own characterisation. Worth noting in case a careful reader spots the near-identity; either is fine, but if Jeroen wants to be explicit he could rephrase to *"Zoo's own framing is that the agent behaves like an engineer"* or keep as-is.
- Launch date: January 2026, with Zoo Design Studio v1.1. Article's "in January" is correct in voice. If the publish date of post 3 is in May 2026, "in January" reads as "January of this year" — clear from context.

---

## Claim 4 — cad-khana metadata + the assertion-as-build-failure quote

**Article wording (paragraphs 5–6)**:
> The third answer is [cad-khana's](https://github.com/cyberchitta/cad-khana) […]. cad-khana is a Claude Code skill on top of [build123d](https://github.com/gumyr/build123d), a Python parametric CAD library that was not designed for AI agents and acquired one through the community. The project has five stars and forty commits at the time of writing. What it does is small and exact. The build script defines geometric constraints as assertions: `.assert_no_interference()`, `.assert_min_wall()`, and a few others. The build runs. If the assertion fails, the build fails. The agent does not get to proceed past a violation, because the violation halts the build before the agent reads the result. The README puts it bluntly: "Assertions in the script become build failures when violated, so geometric constraints are enforced, not hoped for."

| Check | Result |
|---|---|
| Source (quote) | `https://github.com/cyberchitta/cad-khana/blob/main/README.md` |
| Source (metadata) | `https://api.github.com/repos/cyberchitta/cad-khana` |
| Step 0 (existence) | ✓ Repository exists. README fetched 2026-05-18 via `gh api` |
| Step 4 (scope match) | ✓ README describes a Claude Code skill + Build123d wrapper for LLM-driven CAD iteration |
| Step 5 (exact location) | ✓ Quote in "What it does" section of the README. Metadata from GitHub REST API. |
| Step 6 (read section) | ✓ **Direct primary-source verification done 2026-05-18.** Quote is verbatim: *"Assertions in the script become build failures when violated, so geometric constraints are enforced, not hoped for."* |
| Confidence tier | **ESTABLISHED** for the quote and the metadata |

**Primary-source metadata (2026-05-18)**:

| Article claim | Primary source | Verdict |
|---|---|---|
| "five stars" | 5 stargazers (GitHub API) | ✓ Exact match |
| "forty commits at the time of writing" | 40 commits (GitHub API, per_page=100) | ✓ Exact match |
| "Claude Code skill on top of build123d" | README: "A CLI tool and agent skill for designing 3D-printable mechanisms in Build123d, built for LLM-driven iteration." | ✓ Match |
| "build123d… a Python parametric CAD library that was not designed for AI agents" | build123d repo description: "A python CAD programming library" (2,289 stars). cad-khana README: "Existing code-CAD tools (OpenSCAD, CadQuery, Build123d) assume a human with a render window." | ✓ Match. "Parametric" is implied by Build123d's nature (BREP-based parametric CAD); description confirms build123d was not designed for agent use. |
| "`.assert_no_interference()`, `.assert_min_wall()`, and a few others" | README example shows: `.assert_no_interference("lever", "housing")`, `.assert_clearance("lever", "housing", min_mm=0.2)`, `.assert_min_wall("housing", min_mm=1.5)` | ✓ Match. Article paraphrases ("and a few others") accurately. |

**Note on "at the time of writing"**:

Metadata is current as of **2026-05-18**. The 5/40 numbers will drift as the project develops. If the article publishes more than a few weeks later, the numbers may need re-checking. Two mitigations available:

- Pin the commit hash at the time of writing: cad-khana HEAD at 2026-05-09 (last push per GitHub API). The article doesn't currently pin a hash but could.
- Leave "at the time of writing" as the hedge and accept drift. Acceptable.

---

## Claim 5 — Validation independence as the definitional move

**Article wording (paragraph 7)**:
> If validation is establishing that a generated artifact meets the requirement against an evidence source independent of the generation process, then assertions running in a build system the agent did not write are independent.

| Check | Result |
|---|---|
| Source | `docs/glossary.md` — "Validation (As Jeroen uses it)" entry |
| Step 0 (existence) | ✓ Glossary entry confirmed at `docs/glossary.md` line 20 |
| Step 4 (scope match) | ✓ The glossary entry's definition reads: *"establishing that a generated artifact actually meets the requirement, against an evidence source independent of the generation process."* Article's phrasing is near-verbatim. |
| Confidence tier | **ESTABLISHED** — definition is Jeroen's own house definition, used consistently across the WHY arc and the AE site |
| Article language | The article uses the definition without naming the glossary. Per draft's own notes (line 70 of draft), this is intentional and correct for the audience. |

**Note**: This is a meta-claim — the article is *applying* Jeroen's own coined definition of validation to the three platforms. Verification here is internal consistency (article matches glossary), not external primary-source.

---

## Sources block (to embed in the article)

Following the inline-link + Sources-block convention from the senior-trust article. Recommended block at the bottom of the article body:

```
Sources

Adafruit. (2026, May 7). Making electronics with TSCircuit via Codex,
  without KiCad/Altium/Eagle.
  https://blog.adafruit.com/2026/05/07/making-electronics-with-tscircuit-via-codex-no-kicad-altium-eagle/

tscircuit. (n.d.). Generating Circuit Boards with AI.
  https://docs.tscircuit.com/guides/circuit-generation/generating-circuit-boards-with-ai

Zoo. (2026). Zookeeper: The Conversational CAD Agent For Parametric Modeling.
  https://zoo.dev/research/zookeeper

cyberchitta. (2026). cad-khana.
  https://github.com/cyberchitta/cad-khana

gumyr. (n.d.). build123d.
  https://github.com/gumyr/build123d
```

(Adafruit citation pending browser verification of date/title. If the URL turns out not to exist or to claim something different than the article describes, drop this row and rewrite paragraph 1 per Claim 1 fallback options.)

---

## Outstanding tasks before publish

1. ~~**Jeroen browser-fetches the Adafruit URL**~~ ✅ Done 2026-05-18. Post verified at primary source; Claim 1 upgraded SPECULATIVE → SUPPORTED.
   - ~~**Nuance A** (paragraph 1): "No human touched the layout"~~ ✅ Applied 2026-05-18 → *"No conventional CAD, no manual routing."*
   - ~~**Nuance B** (paragraph 1): "The brief was a sentence"~~ ✅ Applied 2026-05-18 → *"The brief was prompts; the output was a board."*
   - ~~**Nuance C** (paragraph 3): "same engineer who wrote the prompt, in the same session"~~ ✅ Applied 2026-05-18 via Option C1 → *"The check is by whichever humans the user enlists: the user alone, a teammate, a community. None of them is the build system. None of them runs automatically. That is not platform-side independence."* The change "not independence" → "not platform-side independence" also sets up the cad-khana paragraph's structural-independence claim more cleanly.
2. ~~**Decide on the tscircuit phrasing**~~ ✅ Applied 2026-05-18 via Option A (em-dash removed for voice compliance). Paragraph 2 now shows all three "Tips for Working with AI" bullet points before isolating the first one as the article's quote. Adds ~30 words; gains precision and grounded specificity.
3. ~~**Decide on cad-khana hash pinning**~~ ✅ Decision 2026-05-18: leave *"at the time of writing"* as-is. Hash pinning would be over-engineering for blog register; the smallness (not the exact number) is the argument's point; publish date disambiguates the hedge.
4. ~~**Cold re-read**~~ ✅ Done 2026-05-18 via Pass 1 reviewer (Haiku, fresh session). All direct quotes confirmed character-by-character.
5. ~~**Cross-model review**~~ ✅ Done 2026-05-18. Pass 1 (Haiku, intra-family small, fresh session, checklist rigour) and Pass 2 (Opus, intra-family large, fresh session, argument-shape critique) both run in parallel. Pass 1 returned ready-to-publish with all 9 hard rules and 8 structural checks passing. Pass 2 returned minor-revisions with 5 numbered argument-shape findings. Pattern from DR-011 N=1 observation (disjoint coverage between intra-family small and large) replicated cleanly: Pass 1 caught zero argument-shape issues; Pass 2 caught five; neither would have caught the other's findings. Four of Pass 2's five findings applied; one skipped (closer phrasing kept for rhythm — Pass 2 itself flagged it as optional). Specific outcomes:
   - ~~**P2-1**: Cut redundant transition sentence~~ ✅ Applied. Section now opens directly with *"tscircuit is the most polished of the three."*
   - ~~**P2-2**: Add mechanism sentence in Zoo paragraph~~ ✅ Applied: *"The errors a model is most likely to make when generating are the errors it is most likely to find plausible when reviewing, because both passes draw on the same priors."* Closes the half-stated warrant against agent-self-review.
   - ~~**P2-3**: Tighten cad-khana independence phrase~~ ✅ Applied. *"a build system the agent did not write"* → *"a build system separate from the agent's generation step"*. Names runtime separation rather than authorship.
   - ~~**P2-4**: Cut inheritance line~~ ✅ Applied. Removed *"The choices the platforms are making now are the practices the next cohort of hardware engineers will inherit."* Avoids overreach into prediction and removes implicit promise to an unwritten Post 4.
   - **P2-5 (closer "does not count" phrasing)**: SKIPPED. Pass 2 flagged this as optional and acknowledged rhythm wins. Surrounding sentences make *"as validation"* clear enough. Kept as drafted.
   - Pass 2's three strategic framing concerns (AI-bad misread, cad-khana booster risk, inheritance overreach) all assessed as low or addressed by the fixes above. No additional action required.
   - **Pattern observation worth filing back**: this run replicates the DR-011 N=1 finding at N=2 (blog scale). Worth a note in `audits/feedback-from-blog-application.md` in agent-ready-papers next time that file is touched. Empirical record: Haiku 0 substantive findings; Opus 5; disjoint coverage; combined coverage strictly greater than either alone.
6. ~~**Embed the Sources block**~~ ✅ Done 2026-05-18. Inline links on first mention of each cited source (Adafruit, tscircuit homepage, tscircuit docs, Zoo, cad-khana, build123d). Sources block at article end, alphabetical by org/author.
7. ~~**Length pass**~~ ✅ Decision 2026-05-18: accept ~1130 words (after Pass-2 edits). Comparative three-platform structure justifies the length; sits inside the 800-1500 writing-guide range.
8. ~~**Move to `src/pages/writing/who-runs-the-drc.astro`**~~ ✅ Done 2026-05-18. Registered in `src/data/writing.ts`. Cover image generated at `public/social/who-runs-the-drc.png` (typographic register, three-line headline with build-system line in amber). No in-article diagram (decision per visual-register memory rule — the three-platform parallel prose is already a figure-in-prose).
9. **LinkedIn cross-post draft** at `drafts/who-runs-the-drc-linkedin.md` (after the article ships). Move to `memory/posted-linkedin/who-runs-the-drc.md` after posting.

---

## Method note

This record applies the agent-ready-papers anti-hallucination checklist (Step 0 + Steps 4–6) to a platform-citation article rather than an academic-claim article. The same checklist applies, but the primary sources are vendor documentation, vendor research pages, and GitHub repositories rather than peer-reviewed papers. The notion of "ground truth" maps cleanly: a quote verified against vendor documentation is at the same evidence layer as a number verified against a study's primary source.

Four of five claims are at ESTABLISHED tier (quotes verbatim, metadata exact). The Adafruit claim is at SPECULATIVE pending browser-fetch by Jeroen; the article's *"may be"* hedge is the correct tier-language for that state.

DR-011 (multi-model review pattern, agent-ready-papers, 2026-05-11): plan to apply Pass 1 (intra-family small / fresh session) before publish, per writing-guide Section 7. Pass 2 (intra-family large) optional for an article of this scale.
