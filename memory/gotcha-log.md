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
**Root cause**: I treated "add an article" as a one-file change. On a static site, content has no built-in navigation; discovery is deliberate.
**Fix**: Added `src/pages/writing/index.astro` (listing page), a Writing section on the homepage that pulls from `src/data/writing.ts`, and a "Writing" link in the footer. One commit, three entry points.
**Pattern**: When adding a new page to the Astro site, always add the discovery path in the same change: homepage entry, listing page, or nav link. A page without a link is not published; it's just uploaded.

### Sub-agents inherit the parent's working-directory sandbox (2026-04-28)
**Problem**: Dispatched a sub-agent to investigate `C:\local_dev\augmented-engineering` while working in `C:\local_dev\dev.jeroenveen.nl`. The agent could `Glob` paths there but every `Read`, `Grep`, and `Bash` call was denied. It returned a structural map and a list of what it could not answer. I had to substitute by reading the files myself in the parent session, which had access.
**Root cause**: Sub-agent permissions inherit the parent session's working-directory restrictions. Sibling project folders are outside the sandbox, even though file paths look reachable from the OS.
**Fix**: For cross-project investigations, do the cross-project file reads in the parent session before (or instead of) dispatching an agent. Keep agent scopes inside the current working directory, or arrange the work so the agent only needs to operate on data the parent has already pasted into the prompt.
**Pattern**: When dispatching multiple parallel investigation agents, route any work that touches sibling repos through the parent session, not through agents. The parent's reach is broader than its children's.

### Em-dashes in LinkedIn comment drafts despite project rule (2026-04-29) [PROMOTED]
**Problem**: While drafting Dutch LinkedIn comment variants (a reply to Witek's post), I used em-dashes throughout the first four variants. Jeroen had to flag the slip. Em-dashes are explicitly disallowed in the project's writing voice per `docs/writing-guide.md` (personal preference + known LLM tic).
**Root cause**: The auto-memory index says to read the writing-guide "before drafting or reviewing any article". A LinkedIn comment felt like a different category, so I skipped the guide before drafting and applied a generic LLM register instead. The rule applies to voice, not to publication channel.
**Fix**: Re-read the guide, found the explicit em-dash rule, rewrote variants with colons, commas, or sentence breaks. Updated MEMORY.md scope text to include external comments and replies, not just articles.
**Pattern**: When drafting anything that will appear in Jeroen's voice (articles, LinkedIn comments, replies, posts), read `docs/writing-guide.md` first. The voice rules are channel-independent.

### Argument-form title crossed into "you missed it" register (2026-05-01) [PROMOTED]
**Problem**: Drafted title "The work is splitting. Most teams haven't noticed." for the WHY post. The second sentence reads as "I see what they don't", which implicates the reader's team and crosses into the kind of arrogance the site is built to avoid. Jeroen flagged it before LinkedIn went live, so we updated four files (website .astro, registry, both drafts) before publishing externally.
**Root cause**: I leaned on the writing-guide's argument-form title example (which literally cites this exact phrasing as the model) without filtering it through the documented modesty register from `user_profile.md` and `feedback_modest_hero.md`. The writing-guide's title example is craft-correct but does not carry the personal-voice override.
**Fix**: Revised the second sentence to "The conversations haven't caught up." Same argument-form rhythm; criticism shifts from teams (implicating the reader) to public discourse (impersonal). Updated all four occurrences in sync (h1, registry, article draft, LinkedIn draft) so copy-paste at publish was current.
**Pattern**: When drafting two-sentence argument-form titles for publication, audit the second sentence specifically against the modesty register. Acceptable targets of criticism: discourse, conventions, frameworks, the public conversation. Risky targets: "teams," "people," "engineers", anything that implicates the reader directly. The writing-guide's craft examples are not exempt.

### Em-dashes in `docs/glossary.md` despite the project rule (2026-05-04) [PROMOTED]
**Problem**: While drafting `docs/glossary.md` I added 11 em-dashes to the file. Caught on review only because Jeroen asked for one. The em-dash rule from the writing-guide had already been promoted (2026-04-29) after the same slip in LinkedIn comment drafts. This is the second recurrence inside roughly a week.
**Root cause**: The previously-promoted rule was scoped to "anything that will appear in Jeroen's voice (articles, LinkedIn comments, replies, posts)." A glossary file in `docs/` is internal reference material, not voiced output, so the channel-independence framing did not catch it. The pattern is repo-style, not just voice-style.
**Fix**: Stripped all 11 em-dashes from `docs/glossary.md`, replaced with colons, commas, semicolons, or sentence breaks. Widened the em-dash rule in `docs/writing-guide.md` Section 6 to apply to any text committed to this repo, voiced or not. Updated the Promoted table below.
**Pattern**: The em-dash rule is repo-scoped, not voice-scoped. Apply it to articles, glossary entries, draft notes, and internal docs alike. Anything written into this repo. (Memory log files in the auto-memory dir at `C:\Users\scbry\.claude\projects\...` remain outside that scope, since the user maintains those for their own use.)

### Glossary scope creep: from 3 to 15 entries despite "small and organic" agreement (2026-05-04)
**Problem**: Recommended seeding the glossary with 2-3 entries and growing organically when triggers fire. Two messages later, when the user asked for field vocabulary too, I added 12 entries in one pass. This is the opposite of the principle I had just stated. Several "Jeroen's positioning" notes in those entries were extrapolations rather than grounded preferences.
**Root cause**: A user request to "expand to include field vocabulary" felt like authorisation to add comprehensively rather than to add the next 1-2 useful entries. Compounded by a tendency to fill structural fields (e.g., "Jeroen's positioning") even when there was no real input to base them on.
**Fix**: Reviewed the glossary against the original principle, trimmed back to 7 earned entries, restructured "Jeroen's positioning" as "Relevance to AE frame" so the section describes adjacency rather than prescribing usage. Removed entries where I had no grounded basis for the positioning notes.
**Pattern**: When the user expands the scope of a thing we agreed to keep small, the right move is to add 1-2 entries that match the new scope, not to populate the whole space. If a structural field would require extrapolation to fill, leave it empty or rename the field. Comprehensive-feeling drafts read as overreach; under-filled drafts that earn each line read as honest.

### Diagram register slipped into management-book mode (2026-05-07) [PROMOTED]
**Problem**: While building the first in-article sketch for "The work is splitting", I produced a polished BEFORE/AFTER panel diagram with a "Same work. Different shape." caption and a warm radial gradient. Jeroen flagged the mirror to *It Is Both* (his satirical book that deconstructs the management-book formula). The diagram I built had four of the formula's tells: BEFORE/AFTER framing, taglineable three-word caption, asymmetry-as-the-whole-argument, and atmospheric gradient polish.
**Root cause**: I treated visuals as decoration to add, not as register to audit. The article voice was carefully modest; my diagram voice imported HBR conventions because that is the default for "polished argument figure." There was no audit gate between conceiving a figure and shipping it.
**Fix**: Pivoted the diagram to sketch register: jittered SVG paths, mono lowercase labels, plain `--bg`, no captions, no atmosphere. Saved a new feedback memory (`feedback_visual_register.md`) that audits future visuals against the four formula tells before shipping. Updated `CLAUDE.md` to point at the memory rule from the diagram-generator workflow.
**Pattern**: Before shipping any figure for Jeroen's articles (sketch, infographic, social image, hero), audit against the management-book formula tells: BEFORE/AFTER framing, taglineable caption, asymmetry-as-argument, atmospheric polish. Default to a sketch register or a Tufte-style typographic citation. If unsure, drop the figure: the urge to "add a visual" is itself part of the formula.

### Repo em-dash debt from before rule scope widened (2026-05-07)
**Problem**: After the em-dash rule scope was widened to "any text committed to this repo" (commit af417cc, 2026-04-28), pre-existing em-dashes remained in older repo files. Counted at curate time on 2026-05-07: `CLAUDE.md` had 19 (all fixed in this session), `memory/gotcha-log.md` had 7 (fixed in this session), `docs/writing-guide.md` had 13, `memory/external-comments.md` had 10, `memory/external-references.md` had 24. Roughly 47 remain across three files.
**Root cause**: Rule scope was widened retroactively without a sweep pass. Each file's authors used em-dashes per the older (voice-only) rule; the scope change made them violations but did not trigger cleanup.
**Fix**: `CLAUDE.md` and this gotcha log fixed in this session. `docs/writing-guide.md`, `memory/external-comments.md`, `memory/external-references.md` need a careful sweep pass: the writing guide uses some em-dashes as character labels (legitimate, since the em-dash itself is the subject), and the external-comments / external-references logs may quote external posts where the em-dashes are not Jeroen's text and should be preserved as quotations.
**Pattern**: When widening a repo-style rule's scope, run a sweep on existing files in the same commit so the rule's enforcement matches its claim. Otherwise pre-existing violations linger and signal that the rule is aspirational rather than enforced. For inherited or quoted text, mark the boundary explicitly (block-quote, code fence) so the rule can skip those passages.
**Verification (2026-05-08)**: Re-counted at curate time. Still 47 em-dashes across the three files (`docs/writing-guide.md`: 13, `memory/external-comments.md`: 10, `memory/external-references.md`: 24). State claim accurate; sweep still pending.

### Hallucinated a named pop-psych concept during fluent drafting (2026-05-08) [PROMOTED]
**Problem**: While drafting `drafts/epistemic-humility.md`, I confidently introduced "Dunning-Kruger mirror" as David Robson's term for expert overconfidence in adjacent domains. A Wikipedia check found that (a) "Dunning-Kruger mirror" is not a recognised term, (b) the original 1999 Dunning-Kruger effect is statistically contested (regression to the mean, Nuhfer et al., Gignac and Zajenkowski), and (c) Robson may not even use the phrase. Without the check the article would have shipped staking its main mechanism on a fabricated citation.
**Root cause**: I treated a plausible-sounding pop-psych framing as verified because I had seen similar framings in the wild. The fluency of my own draft phrasing washed the signal that the citation was unverified. Compounded by the user's "pay homage to Robson" prompt, which I read as authorisation to lean harder on the named-effect scaffolding rather than as a fact-check trigger.
**Fix**: Verified via Wikipedia fetch mid-draft rather than at publication. Removed the Dunning-Kruger scaffolding from body, subtitle, revision notes, and voice audit of the epistemic-humility draft. Reformulated paragraph 3 around Robson's broader intelligence-trap thesis (paraphrase, not quotation) so the argument survives even if the contested 1999 effect is set aside. Created auto-memory `feedback_verify_named_attributions.md` and updated `MEMORY.md`.
**Pattern**: When a draft pins an argument on a named scholarly concept, named effect, or coined phrase attributed to a specific author, treat the citation as a verification gate, not as decoration. If verification cannot happen in-session, restructure so the broader thesis is load-bearing and the named concept is one example among several. The "what X calls Y" construction is the particular trap: it sounds scholarly, slides in easily during fluent drafting, and is exactly where Claude can fabricate without flagging. User phrasings like "pay homage to X" are fact-check triggers, not authorisation.

### Reflexive rejection of virtue-adjacent vocabulary (2026-05-08) [PROMOTED]
**Problem**: When the user proposed framing the new article around "epistemic humility", I pushed back toward "verification discipline" as a less-virtue-flavoured alternative. The user pushed back: he likes humility as the frame, it is authentic to his voice, and the concept has real structure (Robson, fallibilism). My push toward more clinical vocabulary was register-substitution, not sharpening.
**Root cause**: Pattern-matched on virtue-word-in-title to management-book-trap because of the *It Is Both* / visual-register feedback rule. The rule targets stanceless tidy-list treatments, not virtue-adjacent vocabulary itself; I applied it to the word rather than the treatment. Also imposed an engineering-clinical register that is not Jeroen's.
**Fix**: Conceded honestly, kept "humility" as the frame, sharpened the mechanism underneath (the dyad asymmetry: agent cannot be humble, human carries the epistemic stance) so the virtue word is everywhere paired with mechanism. Saved auto-memory `feedback_virtue_words_with_mechanism.md`.
**Pattern**: When auditing a frame against the *It Is Both* test, audit the *treatment* (does it give mechanism, take a stance, name the failure mode?) not the *vocabulary*. Words like humility, judgment, integrity, care can land cleanly with mechanism underneath. When sharpening, reach for more mechanism under the word, not register-substitution of the word.

### Em-dash recurrence in verification records and feedback file (2026-05-12)
**Problem**: While building the per-article verification records (`docs/verification/*.md`, three files) and the agent-ready-papers feedback document (`docs/agent-ready-papers-feedback-2026-05-12.md`), I introduced 73 em-dashes across these files plus two more in the writing-guide additions and three in the external-comments log entry. This is the **third recurrence** of the em-dash slip after the rule has been promoted twice (2026-04-29 voice-channel rule, 2026-05-04 widened to all repo text). Compounded by irony: the verification records were supposed to embody the framework's strictness, and they themselves shipped violating the project's most-promoted style rule.
**Root cause**: When generating long structured documents (audit records, methodology notes, PR drafts), the LLM-default register relies heavily on em-dashes for parenthetical clauses and clause-joining. The previous promotion landed the rule at draft time for *prose* (articles, comments, glossary entries) but did not sufficiently transfer to *structured/audit/meta* documents, which feel like a different register. Compounded by the rule being widened to all-repo-text on 2026-05-04 without me re-internalising the wider scope as I produced new file types.
**Fix (partial, this session)**: Added this gotcha entry to the log. Did not sweep all 73 em-dashes in this session. Flagged as a remaining task for next-session pickup, alongside the existing "Repo em-dash debt" entry from 2026-05-07. Sweep priority: published `.astro` files first (none of mine had em-dashes outside the title-separator convention; 5 total in published articles, 4 of which are HTML title separators), then verification records, then feedback file (which may move to agent-ready-papers anyway).
**Pattern**: When producing **structured/audit/meta** documents (verification records, audit logs, methodology notes, PR drafts), the em-dash rule applies the same as in prose. The repo-wide scope from 2026-05-04 is not voice-mode-specific. New file-type defaults: instead of "X — Y", default to ". X. Y." or ". X: Y." and only restructure if the punctuation gets in the way. The frequency of em-dashes in a fresh draft of a structured doc is itself a smell. More than a handful per page means the document is in LLM-default register, not in repo register.
**Outstanding**: Sweep the 73 em-dashes I introduced this session (docs/verification/*.md, docs/agent-ready-papers-feedback-2026-05-12.md, plus +2 in writing-guide and +3 in external-comments) in a dedicated cleanup pass next session.

## Promoted

<!-- Track gotchas that have been promoted to topic files or the memory index.
     This helps you avoid re-promoting and shows the loop is working.

     STATUS TAGS:
     - [PROMOTED]: lesson was moved up the stack (to a topic file, memory index, or project file)
     - [RESOLVED]: root cause was fixed; entry stays as history

| Entry | Promoted to | Date |
|-------|------------|------|
| Em-dashes in LinkedIn comment drafts despite project rule | `docs/writing-guide.md` Section 6 (em-dash rule) + `MEMORY.md` scope-widening note (voice rules apply channel-independently) | 2026-04-29 |
| Argument-form title crossed into "you missed it" register | Auto-memory `feedback_title_tone.md` (audit second sentence of "[Claim]. [Sentence]." titles against the modesty register; criticise the discourse, not the reader's team) | 2026-05-01 |
| Em-dashes in `docs/glossary.md` despite the project rule | `docs/writing-guide.md` Section 6 (em-dash rule scope widened from voice-channels to all repo docs) | 2026-05-04 |
| Diagram register slipped into management-book mode | Auto-memory `feedback_visual_register.md` (audit visuals against the *It Is Both* management-book formula: BEFORE/AFTER framing, taglineable caption, asymmetry-as-argument, atmospheric polish) | 2026-05-07 |
| Reflexive rejection of virtue-adjacent vocabulary | Auto-memory `feedback_virtue_words_with_mechanism.md` (audit the treatment for mechanism, not the vocabulary; humility/judgment/integrity carry if mechanism is paired) | 2026-05-08 |
| Hallucinated a named pop-psych concept during fluent drafting | Auto-memory `feedback_verify_named_attributions.md` (verify named scholarly attributions against primary source or Wikipedia before publication; "what X calls Y" framings are the particular hallucination surface) | 2026-05-08 |

-->
