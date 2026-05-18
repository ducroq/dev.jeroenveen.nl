# Who runs the design-rule check?

*Status: PULLED 2026-05-18 (same day as publish). The article shipped briefly to the live site (live for approximately two hours) and was then pulled after recognising the deeper diagnosis: this is AE-cross-domain work, not V&V arc closure. Post 2 promised the survey/research asymmetry in non-software domains; this article delivered a platform-architecture comparison in non-software AI. Same domain, different topic. The piece pre-empted the methods pieces that should be the V&V arc closer (Reproduce-Don't-Assess, OPAL's layered verification, the assertion patterns used in own work). Body, verification record, and cover-image generation logic retained. Possible future use: recast as the first piece in a sibling AE-cross-domain arc rather than as the V&V arc closer. Do not promote to `src/pages/writing/` again without re-positioning the arc framing. See `memory/hypothesis-log.md` Resolved entry for the full diagnosis.*

*Original status (now superseded): first draft, 2026-05-18. WHY arc, post 3 closes the arc. Sequel to "Senior developers trust AI less than juniors" (post 2, published 2026-05-12) and "The work is splitting" (post 1). Verification record at `docs/verification/who-runs-the-drc.md` (built 2026-05-18; four of five sources verified at primary; Adafruit pending browser fetch). Confidence tier per claim recorded there; article language already matches tier per writing-guide Section 7.*

---

**Title:** Who runs the design-rule check?
**Subtitle:** Three platforms now ship AI-designed hardware. They answer the question differently.
**Slug:** `who-runs-the-drc`
**Target length:** ~1100 words. Current: ~1150.
**Arc position:** WHY post 3 — closes the WHY arc. Post 1: `the-work-is-splitting`. Post 2: `senior-developers-trust-ai-less` (published 2026-05-12).

---

In May, [Adafruit](https://blog.adafruit.com/2026/05/07/making-electronics-with-tscircuit-via-codex-no-kicad-altium-eagle/) reported what may be the first PCB that was "vibed" into a fab order: a complete board, designed end to end by an agent, sent straight to manufacturing. The platform was [tscircuit](https://tscircuit.com/), and the agent was Codex. No conventional CAD, no manual routing. The brief was prompts; the output was a board.

What tscircuit is doing, and what Zoo and cad-khana are doing alongside it, is on its own terms an engineering achievement. Natural language to compile-ready board layout. Conversational reasoning over geometry with engineering tools in the loop. Diagnostic-first agent-assisted CAD. None of these existed a year ago. The question this piece traces is narrower: where, in each, does validation live?

The tscircuit documentation, in its own words, names the safety net. Three bullet points in a "Tips for Working with AI" section: "Verify connections," "Review footprints," "Preview and iterate." All three are user-side. None are automated. The first reads: "Always check that all components are properly connected." The maintainers are not hiding it. They mean it.

This is what *the work is splitting* looks like when production is hardware. Generation is now cheap and instant. Validation is whatever happens between the prompt and the fab order. Where exactly that validation lives in the stack is the question that the design-rule check used to answer, and the question I have been watching three platforms try to answer differently. There are surely others; these three are the ones I have looked at carefully.

---

The first answer is tscircuit's, and it is the answer of the platform that shipped the vibed PCB. Validation lives in the user. The platform has no automated electrical rule check, no automated design rule check, no manufacturability gate. The board you receive from the agent goes to the fab unless you stop it. The check is by whichever humans the user enlists: the user alone, a teammate, a community. None of them is the build system. None of them runs automatically. That is not platform-side independence.

The second answer is [Zoo.dev's](https://zoo.dev/research/zookeeper), built into Zookeeper, the conversational CAD agent shipped with Zoo Design Studio in January. Zoo describes the agent's verification posture this way: it "frequently executes the model to check for errors, and it reviews the geometry via multi-view snapshots," with access to "computational tools for engineering, such as center of mass location, mass calculation, and surface area and volume measurements." The agent behaves like an engineer. It runs the model. It looks at it. It measures. This is more than tscircuit offers. But the check is by the same agent that produced the artifact. The errors a model is most likely to make when generating are the errors it is most likely to find plausible when reviewing, because both passes draw on the same priors. If the agent missed a kind of failure when it generated the part, it will probably miss the same kind of failure when it inspects the part.

The third answer is [cad-khana's](https://github.com/cyberchitta/cad-khana), and it is the least polished of the three. cad-khana is a Claude Code skill on top of [build123d](https://github.com/gumyr/build123d), a Python parametric CAD library that was not designed for AI agents and acquired one through the community. The project has five stars and forty commits at the time of writing. What it does is small and exact. The build script defines geometric constraints as assertions: `.assert_no_interference()`, `.assert_min_wall()`, and a few others. The build runs. If the assertion fails, the build fails. The agent does not get to proceed past a violation, because the violation halts the build before the agent reads the result. The README puts it bluntly: "Assertions in the script become build failures when violated, so geometric constraints are enforced, not hoped for."

The check, in cad-khana's design, is by something that is not the agent. It is in the build system. It runs whether or not the agent thought to check for it. It does the work of independence by structural separation. Even when the agent has produced something plausible, the assertions can disagree.

---

tscircuit is the most polished of the three. It has the largest community, the cleanest documentation, the most active development, and the most striking demo. The agent generates JSX, the JSX compiles to a typed intermediate format, the intermediate exports to Gerber, the Gerber goes to the fab. The pipeline works. What it does not yet have is the layer that historically caught the errors that the designer overlooked. The platform's bet is that the designer will catch them, or that the layer is on the way.

Zoo is the most ambitious. The platform was built around the conversational agent from the start, with a custom CAD language and its own geometry kernel. Zookeeper's snapshot-and-measure loop is genuinely more thoughtful than the absence in tscircuit's docs. But the loop has the limit that all single-model loops have: it can only catch what its training distribution lets it notice. There is no independent ground truth in the check.

cad-khana is the smallest and probably the least known. It also happens to be the only one of the three whose design treats independence as a structural property of the system rather than a habit of the user. If validation is establishing that a generated artifact meets the requirement against an evidence source independent of the generation process, then assertions running in a build system separate from the agent's generation step are independent. The agent's plausible output and the assertion's verdict are different distributions. The assertion can be right when the agent is wrong, and that is the whole point.

I work this way in my own AI-assisted reviews, and I rely on it. My own reproductions, my own assertions, my own re-derivations are what catch the errors the AI's plausibility check passed. I do not trust the agent's review of the agent's output for the same reason I do not trust my own review of my own writing on a tired day. Independence is the load-bearing part.

---

The three platforms are making three different bets about who provides that independence. tscircuit bets on the user. Zoo bets on the agent. cad-khana, alone of the three, bets on the build system. The smallest of the three is the one whose answer holds up to the definition of the word.

If you are shipping hardware with an AI in the loop, the question worth tracing is which part of your stack actually runs the check. The agent that wrote the artifact does not count, regardless of how thoughtful the loop looks. Without independence, validation collapses into plausibility review, and the difference between plausibility and correctness is what hardware costs you a fab cycle to learn.

---

## Sources (working list, pre-verification)

- Adafruit (7 May 2026). *Making electronics with TSCircuit via Codex, without KiCad/Altium/Eagle.* `blog.adafruit.com/2026/05/07/...`
- tscircuit. *Generating Circuit Boards with AI.* `docs.tscircuit.com/guides/circuit-generation/generating-circuit-boards-with-ai`
- Zoo. *Zookeeper: The Conversational CAD Agent For Parametric Modeling.* `zoo.dev/research/zookeeper`
- cyberchitta/cad-khana. `github.com/cyberchitta/cad-khana`
- gumyr/build123d. `github.com/gumyr/build123d`

---

## Notes for self before next pass

- Run cross-model review per `docs/writing-guide.md` Section 7 before promoting to `src/pages/writing/`.
- Open verification record `docs/verification/who-runs-the-drc.md` and trace every quoted phrase to its primary source. The four direct quotes are load-bearing:
  - tscircuit: "Always check that all components are properly connected." (docs.tscircuit.com/guides/circuit-generation/generating-circuit-boards-with-ai)
  - Zoo: "frequently executes the model to check for errors, and it reviews the geometry via multi-view snapshots" (zoo.dev/research/zookeeper)
  - Zoo: "computational tools for engineering, such as center of mass location, mass calculation, and surface area and volume measurements" (same source)
  - cad-khana: "Assertions in the script become build failures when violated, so geometric constraints are enforced, not hoped for." (cad-khana README)
- The Adafruit "first vibed PCB" claim is the load-bearing opening fact. WebFetch returned 403 in this session; re-verify by direct browser visit before publish, and downshift the language to "may be" if the post does not actually claim "first." Current draft already says "may be."
- cad-khana stars/commits count is from May 2026 GitHub state; cite as "at the time of writing" or pin the commit hash if more rigour is wanted.
- The article uses the validation definition from `docs/glossary.md` ("an evidence source independent of the generation process") without naming the glossary. That is correct for the audience.
- One CTA at the end. Reads as a soft invitation, not a fundraise.
- Self-implication used once mid-piece ("I work this way in my own AI-assisted reviews"). Per Section 7 of the canonical guide: one strategic meta-confession per piece.
- No em-dashes. Verified by sweep.
- HAN/AEA/SLIM/KC/AIM strings: none present. Verified by sweep.
- Framework labels (P1/P2/P5, Three-Layer, Tool Agnosticism): none present. The underlying ideas are there without the capitalised labels.
- LinkedIn cross-post draft: write separately at `drafts/who-runs-the-drc-linkedin.md` after the article ships.
