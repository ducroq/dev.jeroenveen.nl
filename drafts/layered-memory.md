# Layered memory (sketch)

> **Status:** SKETCH (working title and angle, not drafted yet).
> **Working slug:** `layered-memory` (rename when finalising)
> **Series:** standalone solution piece. Not part of WHY arc.
> **Audience filter:** Engineer or AI lead who has tried setting up a memory or notes system for their agent and watched it bloat or rot.

---

## Working title options

1. **"Memory should grow with the project."** (current favourite: argument-form, frames the contradiction with the "set up the perfect system on day one" instinct)
2. "I started writing for the agent the way I write for a new colleague."
3. "A new layer when the old one bloats."
4. "Most agent memory advice starts with the wrong file."

## Subtitle options

- "An incremental approach that has held up across nine projects."
- "What I have settled on after enough rewrites."
- "Start narrow. Grow only when something is doing two jobs."

## The observation (modest register, one paragraph)

For a while I tried to set up the perfect memory system on day one of every project. It always over-fitted. What works, in the projects I have run for long enough to notice, is starting with one file, growing layers only when the existing one starts doing two jobs, and being willing to retire layers that stop earning their place.

## Anchor evidence

- **`agent-ready-projects` v1.9.0**: the README's growth path goes project file only, then gotcha log, then curate, then memory index, then topic files, then coordination, then ADRs.
- **One concrete project example**: `dev.jeroenveen.nl` itself. Started with `CLAUDE.md` only. Added `docs/writing-guide.md` when prose-drift in agent-generated drafts became a recurring issue. Added `memory/external-comments.md` when LinkedIn-replies log filled CLAUDE.md. Each layer was a response to a real recurring problem, not to a guess about what would be needed.
- **Counterexample worth using**: a project that started with full layered structure on day one, where most files stayed empty and the agent rarely consulted them. Mention without naming if a real one is at hand.

## Key claims to develop

1. **A monolithic project file gets reread in full every session.** Keep it short. Anything you put there has a per-session attention cost.
2. **Adding a layer is a response to a real problem**, not a hypothesis. The triggering symptom is usually one of: section getting too long, recurring confusion, knowledge that does not fit the always-loaded shape.
3. **Layers can be retired.** Most projects do not need the full stack. The honest move is to delete a layer when its triggering symptom no longer applies.
4. **The instinct to start perfect** comes from infrastructure-as-code disciplines. It is not wrong in those disciplines. It is wrong here, because the cost function is different: in a memory system, every layer you add is a small attention tax on every future session.
5. **The order of layer addition is project-specific.** What works in a writing-heavy project (writing guide, voice rules) is different from what works in a code-heavy project (gotcha log, ADRs).

## Closing options (pick one)

- **Forward look**: "I am still discovering which layers retire and which become permanent."
- **Open question**: "What did you add to your project file last week that made the agent dumber, not smarter?"
- **Soft contact**: "If you are running a long enough project to have grown a memory system, I would like to compare growth paths."

## Register notes (audit before drafting)

- ❌ Do NOT title "The Five-Layer Memory System" or any capitalised framework label.
- ❌ Do NOT present the layer order as canonical, numbered, or universal.
- ❌ Do NOT include a comparison table of "before / after" or "naive / advanced." The article shape that lands is one observation, one project example, one personal failure mode (over-fitting on day one).
- ✅ Modest register: "I tried different orders and this one stuck for me."
- ✅ Lead with the failure (over-fitting on day one) before the fix.
- ✅ Acknowledge the discipline this contradicts (the start-perfect instinct from IaC, terraform, etc.).
- ✅ Cite `agent-ready-projects` once as the longer artefact.

## Word count target

~700 to 900.

## When promoted to draft

Move from `drafts/layered-memory.md` to a full draft body in this same file (cold-read), then `src/pages/writing/<slug>.astro` once approved.
