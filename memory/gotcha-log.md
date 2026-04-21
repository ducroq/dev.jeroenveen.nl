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

## Promoted

<!-- Track gotchas that have been promoted to topic files or the memory index.
     This helps you avoid re-promoting and shows the loop is working.

     STATUS TAGS:
     - [PROMOTED] — lesson was moved up the stack (to a topic file, memory index, or project file)
     - [RESOLVED] — root cause was fixed; entry stays as history

| Entry | Promoted to | Date |
|-------|------------|------|

-->
