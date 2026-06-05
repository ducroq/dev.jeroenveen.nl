# Adaptive curate (sketch)

> **Status:** SKETCH (working title and angle, not drafted yet).
> **Working slug:** `adaptive-curate` (rename when finalising)
> **Series:** standalone solution piece. Not part of WHY arc.
> **Audience filter:** Engineer who has set up an agent memory or notes system and noticed it carrying entries that are no longer true.

---

## Working title options

1. **"An agent that prunes its own notes."** (current favourite: argument-form, modest, surfaces the act of deletion as the novel move)
2. "End-of-session is the wrong time to add memory. It is the right time to delete it."
3. "Memory rots faster than you think."
4. "The cheapest fix for a bloated memory system is asking 'is this still true?'"

## Subtitle options

- "A skill that asks 'is this still true?' before adding anything new."
- "What I started doing after the third stale-memory incident."
- "The end-of-session habit that made my agent useful."

## The observation (modest register, one paragraph)

### Option A (current): lead with the failure mode

The first time I built an agent memory system, I worried about how to capture lessons. Two months in, the problem had reversed. The system was full of lessons that were no longer true. The agent was confidently citing memory entries about a file that had been renamed two weeks earlier, an architectural decision that had been superseded, a workflow we no longer used. The fix turned out to be small, and on reflection obvious. At the end of every session, the agent reads the gotcha log and the memory index and asks of each entry: *is this still true?*

### Option B (added 2026-06-05): lead with the incantation

I noticed I say almost the same words at the end of every session. *Let us wrap up. Clean up the repo. Update the docs. Curate. Commit, push, deploy.* The phrase has hardened into a sequence, and it took me a while to see why *curate* in particular sat where it did, between the docs update and the commit.

The first time I built an agent memory system, I worried about how to capture lessons. Two months in, the problem had reversed. The memory was full of lessons that were no longer true. The agent was confidently citing entries about a file that had been renamed two weeks earlier, an ADR that had been superseded, a workflow we had stopped using. *Curate* is the slot in the closing sequence where that gets caught. The agent reads the gotcha log and the memory index and asks of each entry: *is this still true?*

**Trade-off note.** Option A is tighter (one paragraph) and lands the failure mode first, per the register-note rule. Option B trades a paragraph of length for a more concrete entry (an actual phrase Jeroen says, not a recalled feeling) and positions curate as a verb in a specific sequence rather than an abstract habit. Option B also opens a small follow-on beat available later in the piece: that crystallized closing phrases are evidence the underlying workflow has stabilised, which is a frame that travels to other AE rituals (the multi-model review battery being the obvious sibling).

## Anchor evidence

- **The `/curate` skill** in `agent-ready-projects` (templates/curate.md). Specifically Step 0, the freshness check: dead references, stale memory dates, ground-truth drift, unverified state claims with verify-comment commands, lingering gotchas, hypothesis log surface.
- **One concrete project moment**: dev.jeroenveen.nl's MEMORY.md was carrying entries from the GitHub Pages era after the project migrated to Netlify. Curate's freshness check flagged the dead `.github/workflows/deploy.yml` references. Without curation those would still be in the agent's context, confidently misleading every session.
- **Counterexample**: a memory system without retirement. Examples are easy to find: the agent that cites a file path that no longer exists, the entry that says "shipped" for something that was reverted, the gotcha that has been fixed but is still warned against.

## Key claims to develop

1. **Memory entries decay.** The decay rate is faster than the writing rate, in any active codebase. Every refactor, rename, ADR supersession, or workflow change ages a small number of memory entries.
2. **Without retirement, memory becomes net negative.** It confidently cites stale state. The agent reads it and acts on it. The cost is real: wrong answers from a system that looks well-organised.
3. **The cheap fix is end-of-session curation that interrogates each entry.** Dead reference? State changed? Promotion-worthy? Stale gotcha?
4. **"Adaptive" because curation runs against actual project state**, not a static checklist. Verify commands. File-existence checks. Modification dates. Hypothesis log triggers. The skill is small but it touches the project, not just the log.
5. **Without curation, the project file becomes a graveyard of lessons that no longer apply.** This is the failure mode to name explicitly: the disciplined-looking project that has fossilised.

## Closing options (pick one)

- **Forward look**: "I am still tuning when curation runs against the project versus against the agent's own log."
- **Open question**: "When was the last time you deleted something from your agent's memory?"
- **Soft contact**: "If you have built something similar in a different agent, I would like to compare what each of you decided to interrogate."

## Register notes (audit before drafting)

- ❌ Do NOT title "The Five-Phase Curation Loop" or similar.
- ❌ Do NOT present this as a complete methodology. It is one habit, named.
- ❌ Do NOT introduce a "before / after" comparison diagram. The argument is verbal: the cost of stale memory is invisible until you look for it.
- ✅ Lead with the failure (stale memory citing a file that no longer exists).
- ✅ One specific moment, modest framing.
- ✅ Acknowledge that other practitioners have similar loops. This is craft, not invention. The contribution is naming the freshness-check step explicitly and routinising it as a skill.
- ✅ Note the connection to the layered-memory piece without spending its thesis.

## Word count target

~700 to 900.

## Sequencing note

This sketch and `layered-memory.md` and `task-triggered-pointers.md` form a small triptych on agent context engineering. They could be published in any order. The natural order, if all three ship, is probably:

1. `task-triggered-pointers` (the entry pattern: how the agent finds its way around in the first place)
2. `layered-memory` (the structure: how the memory system is shaped and grown)
3. `adaptive-curate` (the maintenance: how the system stays true)

But each is also self-contained. None depends on the others having been published first.

## When promoted to draft

Move from `drafts/adaptive-curate.md` to a full draft body in this same file (cold-read), then `src/pages/writing/<slug>.astro` once approved.
