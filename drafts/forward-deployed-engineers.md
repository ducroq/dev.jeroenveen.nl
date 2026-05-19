# Forward-Deployed Engineers as an AE foil

*Status: seed note, parked for later AE writing. Captured 2026-05-12 from a chat excerpt about the FDE role (Palantir-pioneered, now copied by OpenAI/Anthropic).*

*Cross-link: this is plausibly the same trend the breathless "Agentic Consulting Mega Companies" LinkedIn post (logged in `memory/external-references.md` candidate) was reacting to. That post saw it as consulting-disruption; this framing sees it as vendor-embedded-engineering. Same trend, different angles. Worth holding both.*

---

## Why this matters for AE

The FDE pattern is the organisational form that emerges when the splitting-work thesis (post 1 of the WHY arc) plays out at vendor-customer scale:

- The LLM is the cheap-production half. The integration / evals / guardrails / domain-fit is the validation half. Vendors realised customers cannot do the validation half fast enough, so they loan out senior engineers to do it for them.
- This is the same gap the senior-trust article names (post 2 of the WHY arc), translated up to the company level. Customers' juniors paste model output in; customers' seniors are too few or too slow to validate; vendors send their own seniors to bridge the gap.
- The Palantir history is the proof-of-concept: their Foundry / Gotham products are "too configurable to sell off the shelf", which is just another way of saying "validation cannot be shipped in a box". OpenAI / Anthropic / friends are now finding the same constraint applies to frontier models in production.

## Connection to "Where do future seniors come from?"

The two notes are siblings of one question, viewed from opposite sides:

| Note | Question | Where the seniors are |
|---|---|---|
| `where-do-future-seniors-come-from.md` | What happens when agents absorb the apprenticeship that builds senior judgement? | Future seniors are uncertain to exist, because the pipeline that produced today's seniors is being foreshortened |
| This note | How are vendors filling the senior-judgement gap *right now*, while waiting for customers to grow their own? | Today's vendor-side seniors are being loaned out as FDEs, because the customer side cannot build the library fast enough |

Both notes describe the same structural shortage of senior pattern-library holders. One is about the supply pipeline, the other is about how the market is currently routing around the shortage. An AE essay on this could cover both halves.

## Positioning angle for Jeroen

The chat excerpt flagged this directly:

> This is essentially what a senior independent technical consultant does, embedded, hands-on, ships running systems, not decks. Your ZZP pitch competes with (and can complement) FDEs.

Two positioning options worth thinking about before writing anything:

1. **Against FDEs.** "You don't need an OpenAI FDE locking you into one vendor's stack." Strength: it names the lock-in cost. Risk: framing his own work as the cheap alternative to a vendor sales motion is a smaller story than what he is actually doing.
2. **Alongside FDEs.** "I do the work an FDE would, vendor-neutral." Strength: it positions him as the same kind of senior pattern-library holder, just unlocked from a single vendor's product surface. This reads more honestly given the actual work (vmodel.eu, AE, Digital Engineers, ese-bot).

Lean: option 2. The story is that the validation half is now the value, and Jeroen has been doing the validation half for years across multiple vendors and domains. Vendor FDEs are doing it inside a single vendor's gravity.

## Open questions before drafting

- Verify the specific OpenAI / Anthropic FDE arm claims against primary sources. The chat excerpt asserts they are spinning these up; the breathless LinkedIn post named "The Deployment Company" and an "Anthropic Finance Co" with Blackstone / Goldman / H&F. These may all be the same announcements seen through different filters, or they may not. Trace each named entity before any public writing.
- Is there a published Palantir piece (engineering blog, recruiting page, talk) that we can cite for the FDE definition rather than relying on second-hand summary?
- Where does this sit relative to "Reproduce, Don't Assess" and a possible apprenticeship pattern? FDE looks like a *commercial workaround* for the validation gap. The AE patterns are about how engineers themselves close the gap. Two different rooms of the same house.

## Reusable framing

- *"The LLM is the cheap-production half. The integration / evals / guardrails / domain-fit is the validation half."*: clean restatement of the splitting-work argument applied to the vendor stack.
- *"Vendors are loaning out senior engineers because customers cannot build the pattern library fast enough."*: connects FDE to the senior-trust article and to the future-seniors question.
- *"Validation cannot be shipped in a box."*: candidate sharp line. Names *why* both Palantir-then and the LLM labs-now arrived at FDE.

## Decision

Park as a seed. Revisit when (a) the WHY arc is finished and the AE pattern essays are next on the queue, or (b) a positioning piece on Jeroen's ZZP work is being drafted and the FDE foil is needed.

---

## Appendix: original chat excerpt

Preserved verbatim for future re-reading, so the framing is not laundered through a paraphrase.

> Forward-Deployed Engineer (FDE) is a role pioneered by Palantir and now copied by OpenAI/Anthropic. It's an engineer who works on-site (or embedded) inside the customer's organization instead of at the vendor's HQ.
>
> **What they actually do:**
> - Sit with the customer's business teams, learn their workflows, data, jargon
> - Build/wire up the vendor's product into that specific customer's stack
> - Iterate on prototypes in days, not quarters, they have commit rights to the vendor's product
> - Translate vague business pain ("our underwriters take 3 weeks per deal") into concrete software
>
> **How it's different from a consultant:**
>
> | | Consultant (McKinsey, Accenture) | Forward-Deployed Engineer |
> |---|---|---|
> | Output | Slide decks, recommendations | Running code in production |
> | Hands on keyboard | No (juniors maybe) | Yes, senior people |
> | Loyalty | Bills the client | Employed by the AI vendor |
> | Time horizon | Engagement-bounded | Stays until it works |
>
> **How it's different from a sales engineer:**
> A sales engineer demos and answers RFPs. An FDE builds the thing, then often stays for months. The vendor is essentially loaning out senior engineers as a customer-acquisition + retention mechanism.
>
> **Why Palantir invented it:**
> Their software (Foundry, Gotham) is too configurable to sell off the shelf. The product only delivers value once it's wired into the customer's messy reality. So Palantir sends engineers in, gets one division working, then expands. Insanely high gross margins because the customers can't unwind it.
>
> **Why OpenAI/Anthropic are copying it now:**
> LLMs have the same problem in 2026. The model is the easy part; the value comes from integrating it into workflows, retrieval, tools, evals, guardrails. Customers can't do this themselves fast enough, and traditional SIs (Accenture, Deloitte) don't have the depth on frontier models. So the labs are spinning up their own embedded-engineering arms.
>
> **Relevance to your positioning:** This is essentially what a senior independent technical consultant does, embedded, hands-on, ships running systems, not decks. Your ZZP pitch competes with (and can complement) FDEs: you're cheaper, more independent, and not locked to one vendor's stack. Worth thinking about whether to position against "you don't need an OpenAI FDE locking you in" or alongside ("I do the work an FDE would, vendor-neutral").
