# Code-native tools acquire AI faster than AI-native tools acquire engineering rigour

*Status: seed note. Captured 2026-05-18 from the same investigation that produced `who-runs-the-drc.md`. Adjacent to that piece: shares the cad-khana / build123d evidence, but the argument is different. Where `who-runs-the-drc` is about which platform validates, this is about which tools acquire agents in the first place, and what that tells us about how to build for the next five years.*

---

## The seed

Two tools were investigated at the same time. One is [tscircuit](https://tscircuit.com/), an AI-native PCB platform built from scratch to host a Claude / Codex skill, with 2.2k stars, a custom JSX syntax, and a first-party CLI. The other is [CadQuery](https://github.com/CadQuery/cadquery), a Python parametric CAD library released in 2018, with 5.2k stars and zero first-party AI integration. CadQuery has no Claude partnership, no agent skill, no "AI" on its homepage. It is older, more boring, and not marketed as a 2026 thing.

In 2025–2026 a half-dozen Claude skills and MCP servers appeared on top of CadQuery and its derivative [build123d](https://github.com/gumyr/build123d) anyway: `flowful-ai/cad-skill`, `cyberchitta/cad-khana`, `rishigundakaram/cad-query-workspace`, the 3DP server, Svetlana-DAO-LLC/cad-agent. None of these were built by the CadQuery maintainers. None required cooperation from the project. The substrate was code-native, had a text-based API, ran inside a Python process, and accepted assertions. That was sufficient. Agents found it on their own.

The argument: **the load-bearing property is code-nativity, not agent-native intent.** A boring, well-shaped, code-first tool acquires agent integration from the ecosystem without trying. An AI-native tool has to commit to being AI-native from the start to compete on a property the boring tool already has for free.

The corollary matters for how to invest. If you are building a new engineering tool in 2026 and you choose between "design it for an LLM" and "design it as a clean code-native library," the second path is cheaper and probably wins. The agents will come. The reverse is not symmetrical: an AI-native tool with bad code semantics does not retroactively become a good library.

## Why this is article-worthy

- The argument runs against a common assumption in tooling pitches ("agent-native is the new standard"). Senior engineers and AI leads at EU companies have heard the pitch. The counter-evidence is empirical, recent, and not yet a meme.
- It is a tooling-investment claim, not a research claim. The reader (Section 2 of `docs/writing-guide.md`) is the person who decides what infrastructure their team adopts. This is the audience the article filters for.
- Connects naturally to the validation thesis without repeating `who-runs-the-drc`. The cad-khana exemplar sits in both, but the argument here is "why did cad-khana exist at all," not "what does cad-khana do for validation."
- Avoids the marketing register the canonical writing guide warns about (Section 1, DO/DON'T table). The piece is observational, not pitching anyone's tool.

## Possible homes

1. **New dev.jeroenveen.nl article.** Argument-form title candidates:
   - *"Code-native tools acquire AI faster than AI-native tools acquire engineering rigour."* (precise but long)
   - *"CadQuery wasn't built for AI. AI uses it anyway."* (vivid, single-example anchored)
   - *"The boring tool wins."* (sharpest, possibly too cute)
   - Lean: the second one for the title, the first one in the subtitle.
2. **AE pattern essay.** Could land as a positioning note for the AE site's approach to tooling: AE bets on code-nativity as the engineering substrate, not on agent-native frameworks. Useful as internal positioning, less so as outward-facing essay.
3. **A LinkedIn-only post.** The argument compresses well to ~200 words. If the dev.jeroenveen.nl article slot is full for the WHY arc, the LinkedIn version is a viable consolation. Filed at `drafts/linkedin-post-code-nativity-unpublished.md` if so.

Lean: option 1, sequenced after the WHY arc's hardware-validation piece (`who-runs-the-drc`) has shipped. The two articles share evidence; running them close together would fatigue.

## Open questions before drafting

- The argument needs at least one more substrate-example to avoid resting on CadQuery alone. Candidates: any code-first tool that gained AI integration the same way (LangChain has it, but is itself an AI thing, so circular). What about pandas, numpy, or scipy and the agent skills built on them? Worth a brief scan to find one or two clean parallels.
- How much of the AI-native side is genuinely the foil? tscircuit and Zoo.dev are the obvious comparison cases, but both *do* work, both *have* communities, both *are* shipping. The argument is not "agent-native is bad" but "code-native is sufficient and probably underrated." The piece needs to steelman the agent-native case before answering it; otherwise it reads as anti-vendor screed.
- The counter-example to watch for: an AI-native tool that succeeded specifically because it was AI-native and that a code-native equivalent could not have caught. If one exists and is convincing, the argument needs to soften from "code-native wins" to "code-native is sufficient for far more cases than the marketing suggests."
- Tone risk: this argument is closer to a tooling-strategy hot take than to the WHY arc's observational register. The voice has to stay in the curious-humble stance (canonical guide, Section 1) and not drift into verdict-delivery.

## Reusable phrasings

- *"The load-bearing property is code-nativity, not agent-native intent."*: the precise version of the claim. Strong middle-of-article line.
- *"CadQuery wasn't built for AI. AI uses it anyway."*: vivid title candidate and lede.
- *"The agents found it on their own."*: closing-ish line about CadQuery's accidental acquisition of an AI ecosystem.
- *"A boring, well-shaped, code-first tool acquires agent integration from the ecosystem without trying."*: the generalisation, useful when the CadQuery example needs to escape its particulars.
- *"Agent-native frameworks have to commit to being agent-native to compete on a property the boring tool already has for free."*: the dual claim, useful for the steelman/answer move.

## Decision

Hold as seed. Sequence behind `who-runs-the-drc` so the shared evidence does not fatigue the reader. Revisit after that piece ships and after the second substrate-example has been confirmed. If the WHY arc's third piece turns out to be something else, this is a natural Post 4 candidate.
