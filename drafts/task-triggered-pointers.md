# Task-triggered pointers (sketch)

> **Status:** SKETCH (working title and angle, not drafted yet).
> **Working slug:** `task-triggered-pointers` (rename when finalising)
> **Series:** standalone solution piece. Not part of WHY arc.
> **Audience filter:** Senior engineer or AI lead who has tried writing a project README, CLAUDE.md, or AGENTS.md for an AI agent and noticed the agent ignores most of it.

---

## Working title options

1. **"Most agent docs assume the agent has already read them."** (current favourite: argument-form, counter-intuitive, audience-filtering)
2. "An agent only sees what is auto-loaded."
3. "Project files for agents are not READMEs."

Pick on cold read. Option 1 is sharpest; option 2 is most accurate; option 3 frames the failure mode best.

## Subtitle options

- "What I started writing differently after enough sessions to notice."
- "A small fix for a quiet failure mode."
- "The most leveraged 200 lines you will write for an agent."

## The observation (modest register, one paragraph)

I kept finding myself surprised that my agent was not pulling from documents I had written for exactly the situation it was in. The fix was not better docs. It was teaching the always-loaded layer to point at the on-demand layer.

## Anchor evidence

- **`agent-ready-projects` v1.9.0**: the "Before You Start" table pattern as the load-bearing element of a project file.
- **One concrete project moment**: this very repo (`dev.jeroenveen.nl`). The CLAUDE.md "Before You Start" table has a row that says: *when drafting in Jeroen's voice, read `docs/writing-guide.md`*. The agent follows it because the pointer is in the auto-loaded layer; the writing guide itself does not need to be auto-loaded. Without the pointer, the agent ignored the guide.

## Key claims to develop

1. **Auto-loaded context is finite.** A few thousand tokens, depending on the agent. Most useful project knowledge cannot fit there.
2. **READMEs and CLAUDE.md / AGENTS.md are different artefacts.** A README is for a human who clicks. A project file is for an agent that has already loaded it and will not navigate further unless told to.
3. **The bridge is task-triggered pointers**, short conditional rules of the form *"when doing X, read Y"*. They sit in the auto-loaded layer and tell the agent which on-demand doc applies to which kind of task.
4. **The pointer table is the most leveraged section** in any agent-facing project file. It is short, it is concrete, and it changes agent behaviour on the next session.
5. **This works as a retrofit.** Existing repos can add a pointer table without restructuring. The cost is fifteen minutes; the return is a less confused agent immediately.

## Closing options (pick one)

- **Forward look**: "I am still learning what kinds of pointers earn their place and which ones become noise."
- **Open question**: "Where in your project file does the agent reach for something that is not there?"
- **Soft contact**: "If you are doing similar work in a different agent, I would like to compare notes."

## Register notes (audit before drafting)

- ❌ Do NOT title with capitalised framework labels ("The Three-Layer Context Hierarchy").
- ❌ Do NOT pretend to have invented this from scratch. Note that it builds on widely-shared patterns and the `agent-ready-projects` guide is the longer artefact.
- ❌ Do NOT include a numbered "five steps to better agent docs" list. The article shape that lands is one observation, one habit, one project example.
- ✅ Frame as personal habit ("I started doing X"), not as a methodology ("here is the framework").
- ✅ Cite `agent-ready-projects` once, as the longer artefact, not as the article's subject.
- ✅ One concrete project moment, modest register.
- ✅ Acknowledge that the pattern is craft, not invention. The contribution is naming and routinising a small habit.

## Word count target

~700 to 900. Same shape as the splitting / ese-bot articles. Less is fine.

## When promoted to draft

Move from `drafts/task-triggered-pointers.md` to a full draft body in this same file (sit on it, cold-read), then to `src/pages/writing/<slug>.astro` once approved.
