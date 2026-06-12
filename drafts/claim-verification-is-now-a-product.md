# Claim verification is now a product. For reading, not writing.

> **Status:** Drafted 2026-06-12. Awaiting overnight cold re-read (workflow step 2). Verification record drafted alongside at `docs/verification/claim-verification-is-now-a-product.md`; one outstanding item there (report PDF fieldwork dates) before publish.
> **Slug:** `claim-verification-is-now-a-product` (sentence-form, mirrors title, per V&V arc pattern)
> **Arc context:** Extends the V&V arc sideways from engineering into research writing. Picks up the trust frame the arc has been circling (see `drafts/trust-the-missing-word-vv-arc.md`): this piece names trust explicitly with survey data behind it, the same move as `senior-developers-trust-ai-less`. Borrows one paragraph of the grounding-chain critique without burning `drafts/grounding-is-not-ground-truth.md`, which keeps its deeper Lakoff/Johnson layer for its own piece.
> **Foil:** Elsevier LeapSpace launch (filed in `memory/external-references.md`, 2026-06-12 entry).
> **Cover:** typographic title-card (default), `scripts/gen-social-image.py`.
> **In-article figure:** none. The argument is a contrast, not a mechanism; prose carries it.

---

Elsevier surveyed 3,200 researchers across 113 countries and published two numbers that belong side by side: 84% have used AI tools. 22% believe those tools are trustworthy. That is a sixty-two-point spread between use and trust, reported by people whose job is knowing what evidence is worth. Adoption is no longer the story. Trust is.

What Elsevier did with that spread is the interesting part. Last November they launched LeapSpace, an AI research workspace, and its flagship features are verification features. Trust Cards show how each AI-generated statement aligns with the source it cites. Claim Radar shows how a claim holds up across the wider literature: how much published evidence supports it, how much contradicts it. The pitch is "research-grade AI", and it is aimed squarely at the 22%.

I read the feature list with some recognition. I have spent the past months building verification infrastructure for AI-assisted writing, and the instinct behind those features is one I share: trust does not come back through more fluent prose or a bigger model. It comes back claim by claim. This statement, that source, does the one actually support the other. The world's largest scientific publisher just bet a flagship product on that view, and I think the bet is right.

Here is what I keep turning over. Every one of those verification features runs while you read. None of them run while you write.

Follow a manuscript through one working day and the asymmetry is hard to unsee. The literature summary you read at nine arrives grounded, carded, checked against sixteen million articles. The paragraph you write at five, with an AI assistant in the loop, gets nothing. The citation the assistant suggested is pasted in unchecked. The word "demonstrates" lands on a finding that only suggests. The number in your comparison table follows from no calculation anyone performed. Those are the errors that end up in submitted papers, and they happen at the keyboard, after the reading tools have clocked out.

The gap has a structural explanation, and it is not that publishers failed to notice it. Reading-side verification is a corpus business. Trust Cards work because Elsevier holds sixteen million full-text articles and books, plus licensing deals with other publishers, to check claims against. The corpus is the moat; the verification feature is what the moat makes possible. Writing-side verification has no corpus to own. Checking that your citations exist and say what you claim, that your confidence language matches your evidence, that your derived numbers reproduce: that is a workflow. You cannot license a workflow, so nobody ships one as a flagship.

Which also answers a question I asked myself while reading the launch coverage: why would anyone pay for corporate verification tooling when the techniques are reproducible for free? Because the two halves split exactly along that line. The reading half cannot be open-sourced; the thing doing the verifying is licensed full text. The writing half cannot really be productized; the thing doing the verifying is discipline. A claim registry, a citation checklist, an equation check, run as steps instead of virtues. One half is a business. The other half is a practice. The product launch covers the business half and leaves the practice half where it has always been: with the author.

One caveat before the reading half sounds finished. A Trust Card is the system's own judgment of how well its statement aligns with the source it retrieved. The generator and the judge sit on the same chain, reading from the same corpus. Surfacing the source is honest design, and it lowers the cost of checking enormously. But the checking is still yours to finish. "Grounded" and "verified" are not yet the same word, and product copy across this industry works hard to make them rhyme.

As for the practice half, it is less glamorous than a radar. This week I ran an automated equation check across a signal-processing teaching site I maintain: 390 checks over 20 chapters turned up 19 hard numerical errors, including a performance-budget table whose cycle counts contradicted their own total. Every error sat in prose I had written and published. No retrieval system could have flagged a single one, because there was no source to check them against; the ground truth was arithmetic. What caught them was a workflow step, the prose equivalent of a unit test. The templates I use for this are open source, in [agent-ready-papers](https://github.com/ducroq/agent-ready-papers), so I have skin in this half of the argument. That is partly why the launch caught my eye.

The 22% gets reported as a problem to fix. I read it as calibration. Researchers distrust AI output because most of it reaches them unverified, and rational trust tracks verification, not fluency. LeapSpace extends verification over the reading half, and trust there may genuinely recover. The writing half stays open, and no corpus will close it. If an AI assistant helped write your last document, what checked its claims before it shipped?

---

*Sources block (for the .astro version, per writing-guide Section 7):*

- Elsevier. (2025). *Researcher of the Future: a Confidence in Research report.* https://www.elsevier.com/insights/confidence-in-research/researcher-of-the-future
- Elsevier. (2025, November). *Elsevier launches LeapSpace: an AI-assisted workspace to accelerate research and discovery.* Press release. https://www.elsevier.com/about/press-releases/elsevier-launches-leapspace-an-ai-assisted-workspace-to-accelerate-research-and-discovery
- Elsevier. (2026). *LeapSpace: the research-grade AI workspace.* Product page. https://www.elsevier.com/products/leapspace/introducing-research-grade-ai

*Inline-link plan: first mention of the survey links the report page; first mention of LeapSpace links the press release; "research-grade AI" links the product page; agent-ready-papers linked at first mention (public repo, pre-push gate: confirm `gh api repos/ducroq/agent-ready-papers --jq .visibility` returns `public`). The dsp-workshop site is not linked (repo visibility unconfirmed; the anecdote stands without it).*
