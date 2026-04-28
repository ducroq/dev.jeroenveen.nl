# Gotcha Log

<!-- Structured problem/solution journal. Append-only.
     Part of the self-learning loop: Capture > Surface > Promote > Retire.

     PROMOTION LIFECYCLE:
     - New entries start here (Capture phase)
     - At end-of-session, review for patterns (Surface phase)
     - When an entry recurs 2-3 times, promote it to the relevant topic file
       as an "if X, then Y" pattern (Promote phase)
     - When a gotcha's root cause is fixed, mark it [RESOLVED] (Retire phase)
     - Track what you've promoted in the "Promoted" section below

     When the root cause is fixed, mark it resolved here (don't delete). -->

<!-- Template for new entries:

### [Short description] (YYYY-MM-DD)
**Problem**: What went wrong or was confusing.
**Root cause**: Why it happened.
**Fix**: What solved it.

-->

### New content shipped without a discovery path (2026-04-21) [RESOLVED]
**Problem**: First draft of the Writing section shipped the article at `src/pages/writing/ese-bot-eu-sovereign-rag.astro` with no homepage link and no `/writing/` index page. A reader handed the direct URL would find it, but nobody else would. Flagged by Jeroen before publication.
**Root cause**: I treated "add an article" as a one-file change. On a static site, content has no built-in navigation — discovery is deliberate.
**Fix**: Added `src/pages/writing/index.astro` (listing page), a Writing section on the homepage that pulls from `src/data/writing.ts`, and a "Writing" link in the footer. One commit, three entry points.
**Pattern**: When adding a new page to the Astro site, always add the discovery path in the same change — homepage entry, listing page, or nav link. A page without a link is not published; it's just uploaded.

### Sub-agents inherit the parent's working-directory sandbox (2026-04-28)
**Problem**: Dispatched a sub-agent to investigate `C:\local_dev\augmented-engineering` while working in `C:\local_dev\dev.jeroenveen.nl`. The agent could `Glob` paths there but every `Read`, `Grep`, and `Bash` call was denied. It returned a structural map and a list of what it could not answer. I had to substitute by reading the files myself in the parent session, which had access.
**Root cause**: Sub-agent permissions inherit the parent session's working-directory restrictions. Sibling project folders are outside the sandbox, even though file paths look reachable from the OS.
**Fix**: For cross-project investigations, do the cross-project file reads in the parent session before (or instead of) dispatching an agent. Keep agent scopes inside the current working directory — or arrange the work so the agent only needs to operate on data the parent has already pasted into the prompt.
**Pattern**: When dispatching multiple parallel investigation agents, route any work that touches sibling repos through the parent session, not through agents. The parent's reach is broader than its children's.

## Promoted

<!-- Track gotchas that have been promoted to topic files or the memory index.
     This helps you avoid re-promoting and shows the loop is working.

     STATUS TAGS:
     - [PROMOTED] — lesson was moved up the stack (to a topic file, memory index, or project file)
     - [RESOLVED] — root cause was fixed; entry stays as history

| Entry | Promoted to | Date |
|-------|------------|------|

-->
