# Every AI agent starts every session cold

*Status: seed note. Captured 2026-05-12 from a fresh read of agent-ready-projects README (v1.10.0).*

---

## The seed

The agent-ready-projects framework opens with a sentence that does very effective audience filtering:

> Your AI agent starts every session cold. It doesn't remember yesterday's bugs, your architectural decisions, or what it tried and failed last week.

Every engineer who has used Claude Code, Cursor, Copilot, or any similar tool recognises the symptom immediately. The framework's claim is that the fix is not "remember harder" at the model level (memory features, longer context windows) but "scaffold the project so the agent auto-loads orientation and self-navigates" at the repo level. The mechanism is **task-triggered pointers** ("when doing X, read Y first", not "see file Y") plus an incremental layered model that adds layers only as complexity demands.

This is a teachable, transferable workflow argument that does not require buying into a specific tool. It also names a constraint that most "I tried agent X and it forgot everything" complaints are actually about, but without using that vocabulary.

## Why this is article-worthy on dev.jeroenveen.nl

- The opening sentence is strong enough to carry the LinkedIn share by itself.
- Audience filter is automatic: engineers using AI coding agents recognise it on the first sentence; everyone else bounces.
- The fix is concrete (task-triggered pointers + layered model + self-learning loop), which means the piece can be substantive without slipping into productivity-deck rhetoric.
- This project's own `CLAUDE.md` is a worked example, including the `Before You Start` table that *is* the task-triggered-pointer pattern.

## Possible homes

1. **New dev.jeroenveen.nl article.** Argument-form title candidates: *"Every AI agent starts every session cold. Fix the repo, not the model."* or *"Auto-loaded vs. on-demand is the real boundary."* (sharper but more abstract). Either works.
2. **Recruiting / adoption piece for agent-ready-projects.** Slightly different shape: instead of arguing the underlying observation, walk the reader through what to do about it. Same opening sentence, different middle and ending.
3. **AE pattern essay.** The auto-loading cliff is a *prerequisite* for any AE pattern that depends on the agent carrying context across sessions. Worth at least a short pattern note linking to agent-ready-projects for the long version.

Lean: option 1 first, with option 2 as a follow-up once option 1 has done the audience-filtering work. Option 3 is parallel writing for a different surface and can happen any time.

## Open questions before drafting

- Is this primarily about *agent-ready-projects as a framework* or about *the underlying observation that auto-loaded vs. on-demand is the real boundary*? The framework framing is naturally a recruiting piece. The observation framing is more general and probably travels further. The two cannot be the same article without one diluting the other.
- Does the v1.3.2 → v1.10.0 drift on this project (tracked in issue #6) become an embarrassment if this article ships before the project adopts the update? Probably not (a writer using v1.3 honestly can write about the cliff that v1.3 was already responding to), but worth noting that some readers will check.
- The agent-ready-projects README itself does most of the framing work. The article needs to add something the README does not, or it is a recruiting piece in disguise. Candidate additions: the specific worked example of this project's `Before You Start` table evolving over time, or the *failure mode* of the cliff (what specifically goes wrong when there is no scaffold, not just "the agent is amnesic").

## Reusable phrasings

- *"Every AI agent starts every session cold."*: strongest line. Opens the article, opens the LinkedIn share, closes the cover image.
- *"Auto-loaded vs. on-demand is the real boundary."*: names the constraint sharply for readers who already know the symptom.
- *"Task-triggered pointers: not 'see file Y', but 'when doing X, read Y first'."*: the mechanism in one sentence. Reusable as a teaching line.

## Decision

Hold as seed until WHY arc is complete. Then either ship as the next standalone article, or write the recruiting piece for agent-ready-projects and decide which to publish first based on where the WHY arc lands.
