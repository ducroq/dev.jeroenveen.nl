# LinkedIn cross-post draft: Claim verification is now a product. For reading, not writing.

> **Status:** Draft 2026-06-12. Do not post until the article is live at dev.jeroenveen.nl (workflow: article first, Pulse second, short post third).
> **Strategy:** Both surfaces (Pulse + short post), same call as the previous five cross-posts; site authority still young.
> **Hashtag set:** #AI #AugmentedEngineering #ResearchIntegrity
>
> **Decision: link to Elsevier's promo post?** No, not in either body. Rationale: (a) the durable artifacts are the report page and press release, which the article already links; the promo post is marketing surface and adds no evidence; (b) linking a company's campaign post mostly feeds their campaign metrics and frames this piece as a reaction to an ad rather than an argument about a launch; (c) the piece half-credits, half-critiques Elsevier, and anchoring it on their ad sharpens the "dunking" reading we want to avoid. **Optional move after posting:** drop the promo-post URL in a first comment ("the launch post that prompted this: ...") if a cross-reference feels useful, or leave a short pointer comment *on their post* linking the article once reception on our side is known. Their post URL is filed in `memory/external-references.md` (2026-06-12 entry) either way.
>
> **Decision: company hashtags (#Elsevier #LeapSpace)?** No. Company hashtags are brand-follower channels: they put the post in front of people tracking the brand, including its comms team, and they read as affiliation or campaign-riding on a post that is neither. Naming Elsevier and LeapSpace in the text (which we do, repeatedly) is what carries search and mention-pickup. Topic hashtags stay; #DeveloperProductivity from the arc set is swapped for #ResearchIntegrity because this piece's second audience is research-adjacent, not dev-productivity.

---

## 1. LinkedIn article (long-form / Pulse)

**Title:** Claim verification is now a product. For reading, not writing.

**Subtitle:** Elsevier's LeapSpace bets on claim-level trust. Half of the bet is missing.

**Body:**

[Copy the final article body from dev.jeroenveen.nl once live. Footer below.]

---

*Originally published at [dev.jeroenveen.nl/writing/claim-verification-is-now-a-product](https://dev.jeroenveen.nl/writing/claim-verification-is-now-a-product/)*

#AI #AugmentedEngineering #ResearchIntegrity

---

## 2. Short LinkedIn post (links to the Pulse article)

Claim verification is now a product. For reading, not writing.

Elsevier surveyed 3,200 researchers across 113 countries: 84% have used AI tools, 22% believe those tools are trustworthy. Then they built a product on the gap. LeapSpace ships Trust Cards (does this AI statement align with its cited source?) and Claim Radar (how does the claim hold up across the literature?). Claim-level verification, from the world's largest scientific publisher. The instinct is right.

But every one of those features runs while you read. None of them run while you write. The citation your AI assistant pastes in at five o'clock, the "demonstrates" sitting on evidence that only suggests, the table number no calculation produced: nothing in the product touches those.

The split is structural. Reading-side verification is a corpus business; you cannot open-source sixteen million licensed articles. Writing-side verification is a practice; you cannot really productize a discipline. One half got a flagship launch. The other half is still a workflow you have to run yourself. This week mine caught 19 numerical errors in 20 chapters of my own published teaching material. No corpus would have found them; the ground truth was arithmetic.

If an AI assistant helped write your last document, what checked its claims before it shipped?

[PULSE URL PLACEHOLDER]

#AI #AugmentedEngineering #ResearchIntegrity

---

## Publish order (suggested)

1. Publish the website article first (it is the canonical home).
2. Publish the Pulse article, copy its URL.
3. Paste the Pulse URL into the short post placeholder. Publish the short post.
4. Log all three URLs in `memory/external-comments.md` with a 5-7 day check-in note.
5. Move this file to `memory/posted-linkedin/claim-verification-is-now-a-product.md`, update the status header.

## Notes for next time

- Watch for the "but Scite / startup X already does authoring-side checks" comment. The verification record (Claim 6) has the prepared answer: citation-context tools classify how published papers cite each other (reading side); the article's claim is about claim-level checks at authoring time. If a genuine counter-example shows up, concede in comments and tighten the article's wording to "no publisher ships one".
- Watch for "only 22%? what about the neutrals?" The trust figure is a bipolar spectrum item (Trustworthy vs Unreliable, midpoint not charted): 22% trustworthy side, 39% actively unreliable, ~39% neutral. The article's claim ("22% believe those tools are trustworthy") is exact; nobody should read it as "78% distrust". Details in the verification record, Claim 1.
- Watch for "so researchers should just trust LeapSpace then?" The grounding-chain paragraph is the prepared answer: the card lowers the cost of checking; it does not finish the checking.
- If Elsevier comms engages, the tone is already set by the piece: their bet is called right twice. Engage on the open half ("when does the authoring side get the same treatment?"), not on the product's quality.
- Reception comparison: this is the first piece aimed partly at a research-adjacent audience. If #ResearchIntegrity pulls a different commenter population than the arc's usual #DeveloperProductivity crowd, note it for the next cross-domain piece.
