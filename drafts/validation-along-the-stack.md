# AI is moving down the engineering stack. Validation isn't going with it.

*Status: seed note. Captured 2026-05-18 from the same investigation that produced `who-runs-the-drc.md`. Broadest of the four pieces sketched that day: where `who-runs-the-drc` is about three hardware platforms, and `code-native-vs-agent-native.md` is about tooling substrates, this is the long view across software, embedded, and physical hardware. Possible WHY arc post 3, or a separate series intro.*

---

## The seed

In 2023 the AI-augmented engineer was a software developer with Copilot. In 2024 the work spread to embedded systems: Andreas Spiess, several Sirris case studies, the lean Embedded World interviews. In 2025 it reached PCB design (tscircuit). In 2026 it reached mechanical CAD (Zoo.dev's Zookeeper shipped in January). The pattern is consistent: AI moves down the engineering stack, one discipline at a time, from the artifact furthest from physical matter (software) toward the artifact closest to it (a fabricated board, a machined part).

The validation question goes with it. It does not arrive intact. At the software end the validation infrastructure was already mature: linters, compilers, type checkers, unit tests, CI pipelines, code review tooling. AI-generated software still produced verification debt (Sonar 2026: only 48% of developers verify AI-generated code before committing), but the infrastructure existed to catch some of it. At the hardware end the equivalent infrastructure either does not exist yet (tscircuit ships boards without an automated design rule check) or exists but is being bypassed by the new agent-first platforms (Zoo.dev's Zookeeper relies on the agent's own visual inspection rather than on an independent rule checker).

The argument: **the validation infrastructure that already existed at the software end is not propagating down the stack at the same speed as the production tooling.** Production capability moves quickly. Verification capability does not. The gap between the two widens with every step the agents take toward physical matter.

This is not a hand-wave. It is the reason the question in `who-runs-the-drc` even has to be asked. If validation had moved with production, the DRC would already live in the toolchain, and the question would not arise.

## Why this is article-worthy

- The long view earns the right to be told. The previous two WHY arc posts (or the first two if this is post 3) will have shown the shape of the split (`the-work-is-splitting`) and the shape at one specific end of the stack (`who-runs-the-drc`). This piece pulls back and shows the trajectory.
- The trajectory framing has rhetorical leverage. A senior engineer who works in embedded or hardware reads this and recognises which step of the trajectory they are on. The article hands them a frame for what is coming.
- It naturally reaches the AE site's framing of validation as independence, without retreading the platform argument. The validation infrastructure that does not propagate is exactly the independent-evaluation infrastructure that AE has been documenting.

## Possible homes

1. **WHY arc post 3.** Direct sequel to `who-runs-the-drc`. Pulls back from one disciplinary slice to the long view. Risk: three posts in a row about validation may exhaust even an interested reader. Mitigation: this one closes the WHY arc and the next pieces move to specific patterns and case studies.
2. **Standalone series intro at dev.jeroenveen.nl.** Independent of the WHY arc; sets up a longer series tracking specific disciplines (one post per: SW, embedded, PCB, mechanical CAD). Larger commitment.
3. **AE site essay.** AE's framing already presumes the trajectory. An AE essay version would be more pattern-focused and would lean harder on independent-evaluation as the corrective.

Lean: option 1 (WHY arc post 3). The arc benefits from closing with a wide view. The standalone-series version is a stronger commitment than is sensible right now.

## Open questions before drafting

- Avoid the academic vocabulary the writing guide bans: not "phase transition," not "crystallization window," not "epistemological void," not "the digital engineer" as a noun. The trajectory framing has to land in plain language.
- The trajectory claim risks being too neat. SW → embedded → PCB → CAD is a clean story; reality is messier. Embedded AI integration is patchy; CAD AI integration in industrial settings (Solidworks, NX, Catia) lags behind the consumer-facing demos. The piece needs to acknowledge this without losing the through-line.
- One concrete data point per step is the minimum. SW: a verification-debt number (Sonar 2026 is the strongest single source). Embedded: a Spiess-style practitioner workflow or a Sirris case study, observable rather than surveyed. PCB: tscircuit and the Adafruit "vibed PCB" report. CAD: Zoo's Zookeeper and cad-khana. The piece does not have room for more than four; it needs one strong example per step, not coverage.
- The closing move is the hardest. The previous two WHY arc posts close with invitations. A trajectory piece can close with an invitation too, but it can also close with a question: which step of the trajectory is your discipline on, and what is missing from the verification infrastructure at that step? The question is sharper. The invitation is warmer. Pick one.

## Reusable phrasings

- *"AI moves down the engineering stack, one discipline at a time."*: the trajectory claim. Strong opener-or-pivot line.
- *"Production capability moves quickly. Verification capability does not."*: the asymmetry, in plain English.
- *"The validation infrastructure that already existed at the software end is not propagating down the stack at the same speed as the production tooling."*: the precise version. Middle-of-article.
- *"The gap between the two widens with every step the agents take toward physical matter."*: the consequence, with image.
- *"From an artifact you can recompile, to an artifact you have to fabricate."*: the cost of being wrong at each step.

## Decision

Hold as seed. Probable WHY arc post 3 if the arc closes with a wide view. If `who-runs-the-drc` lands well, this is the natural next piece. If the WHY arc is shorter than three posts, this becomes a standalone follow-up. Either way it depends on the platform-validation piece having shipped first; without that anchor the trajectory argument has nothing concrete to point at.
