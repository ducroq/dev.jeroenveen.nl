# Hypothesis Log

Provisional editorial positions under observation. Each entry is a bet whose evidence to confirm or revise lives in the future. Different from:

- **`drafts/<slug>.md`** — articles in progress; not yet a bet
- **commit messages / editorial decisions** — decisions accepted, with rationale frozen
- **`memory/gotcha-log.md`** — problems encountered & solved

Lifecycle: **open** → dormant → revisit (with evidence) → resolved (close or promote to a memory entry / writing-guide update / ADR).

**How to use this file:**

- Add an entry when you take a provisional position you want to revisit later — typically a frame, a reframe, a positioning bet, or a reception check.
- Each entry has a `Review by:` date and a `Revisit trigger:` so `/curate` can surface due items at session start.
- The **Method** field pins the falsification criterion *before* the data lands. Don't loosen Method when the answer arrives; if you want to redefine the bet, open a new entry.
- When an entry is resolved, move it to `## Resolved` with a one-line outcome.
- Keep entries tight. If an entry grows a plan, it becomes a TODO; if it grows a rationale, it becomes a writing-guide update.

## Entry template

```markdown
### [YYYY-MM-DD] One-sentence position

**Position (provisional):** What you're betting on, with concrete forecasts. Cite the evidence that motivates the bet.

**Alternative:** The failure mode you'd see if the position is wrong, with a *signal* — not just "it could fail." Tell future-you exactly what observation would refute the Position.

**Method:** How you'll test it later. Pre-commit the falsification criterion.

**Revisit trigger:** What event causes the entry to become reviewable. Prefer evidence triggers over calendar triggers when the data drives the decision.

**Review by:** YYYY-MM-DD — backstop date. `/curate` flags entries past this.

**Domain:** Tags for filtering (e.g. "WHY arc", "AE positioning", "reception monitoring")
**Status:** open | open (low priority) | open (blocked on X) | dormant
```

---

## Open

### [2026-05-18] First inversion trigger fires within 12 months

**Position (provisional):** dev.jeroenveen.nl is in deliberate mid-drift toward AE-method-leading positioning (see `project_inversion_plan.md` in auto-memory). Three candidate inversion triggers are named: (1) critical mass of AE-pattern articles at the AE site, (2) ovr.news launch needing a clean personal-site point-of-reference, (3) external use of "augmented engineering" returning to Jeroen and sticking. **At least one will fire within 12 months of today, i.e. by 2027-05-18.**

**Alternative:** None of the three triggers fire. The drift continues passively but no inflection point arrives. Signal: no critical mass of AE patterns published at the AE site; ovr.news pushed beyond 12 months; no external "augmented engineering" return. Site stays as "dev projects + writing" without the inversion forcing itself.

**Method:** Quarterly check at 2026-08-18, 2026-11-18, 2027-02-18, 2027-05-18. Each check asks: did any trigger fire? What's closest? If by 2027-05-18 no trigger has fired, Position is refuted and the inversion plan needs revisiting — maybe a fourth trigger is needed; maybe the positioning model itself needs revision.

**Revisit trigger:** Any of: (1) AE site publishes its 5th-or-later named pattern; (2) ovr.news has a public surface; (3) someone uses "augmented engineering" in writing about Jeroen's work or back at him; (4) quarterly calendar checkpoints above.

**Review by:** 2027-05-18 — long-horizon backstop.

**Domain:** Site strategy, AE positioning, inversion plan
**Status:** open (low priority, calendar-paced)

---

## Resolved

### [2026-05-18] The V&V arc closer is a methods piece grounded in own work

**Outcome (2026-06-01):** Position validated by the drafting choices made over the following two weeks. Both drafts in the V&V arc closer slot are methods pieces grounded in own work: `two-reviews-missed-what-reproduction-caught.md` (the driven-pendulum Reproduce-Don't-Assess case, already at READY status by 2026-05-19) and `cross-model-review.md` (the multi-pass review pattern, touched up to first-pass prose 2026-06-01 with the senior-trust empirical case as anchor). Neither candidate is the wrong-shape attempts that triggered the original entry (`ai-productivity-software-bias` and `who-runs-the-drc`). The arc-shape constraint is now an active criterion in the drafting pool, not a re-litigated question. Closing the entry; the resolution of *which* methods piece ships first is downstream and depends on the verification-is-a-workflow-problem reception data.

**Larger lesson logged:** When a hypothesis bets on a future drafting direction, the resolution signal is the drafts themselves, not the published artifact. If the drafts being produced match the bet's predicted shape, the position is validated even before publish-time data lands. This is the logbook function of the hypothesis log (per the 2026-06-01 user / blog + logbook memory): hypotheses about drafting direction get resolved on the drafting record, not on reception.

---

### [2026-05-12] Post-2 (senior-trust) reception will not be successfully claimed by conservatives as anti-adoption ammunition

**Outcome (2026-05-21, t+9 days post-publish, LinkedIn analytics + comment-thread review):** Position holds, weakly. The misread frame did not materialise in observable reception. Specifically: 0 reposts on the short post against 8,521 impressions (the post was not picked up to reframe in either direction); 1 comment (AI Transfer Lab, sharpening the on-frame "experience as pattern library for plausible-but-wrong" axis; no anti-adoption framing in the thread); the predicted "seniors are slow adopters" pushback never surfaced. Engagement rate 0.20% (the broad reach diluted to a thin profile). The thin engagement means the right framing is *no evidence of misread amplification* rather than *Position robustly confirmed by lots of on-frame engagement* — a more robust confirmation would have required more comments engaging with the validation-cost framing specifically. The reach went broad enough to escape the HAN bubble but didn't generate enough reception to fully stress-test the frame.

**Larger lesson logged:** Conservative-misread risk on counter-intuitive framing observations was likely overestimated at publish time. The post-publish framing-risk note (added 2026-05-12 to the `external-comments.md` publish entry) cautioned against breaking frame mid-arc to inoculate against the misread; that caution turned out to be unneeded — the misread didn't materialise. Worth noting for future arc-position drafting: don't pre-emptively defend against misreads that haven't shown signal of materialising; the defensive register costs more than the speculative misread it tries to head off.

---

### [2026-05-18] Post-3 reframe holds: descriptive AE-definitional shape lands cleaner than the literature-bias shape

**Outcome (2026-05-18, same-day pull after publish):** Refuted at the arc level. The reframe correctly pointed away from literature-bias complaint and toward practitioner observation, and the three-platform comparative (`who-runs-the-drc`) shipped that day. Within roughly two hours of publishing, the deeper diagnosis surfaced: the article is doing AE-cross-domain work, not V&V arc closure. Post 2 promised the survey/research asymmetry in non-software domains; the published article delivered a platform-architecture comparison in non-software AI. Same domain, different topic. The piece pre-empted the methods pieces that should be the V&V arc closer (Reproduce-Don't-Assess, OPAL's layered verification, the assertion patterns used in own work). Pulled the same day. Article body, draft, verification record, and cover image retained for potential recast as an AE-cross-domain piece in a sibling arc. The article never reached LinkedIn cross-post; lived on the site for about two hours, zero known external readers.

**Larger lesson logged:** When substituting a draft for an arc position, audit against the arc's *promised topic* (from prior posts' forward-looks), not just against the draft's own merits. The substitution attempt (`who-runs-the-drc` for `ai-productivity-software-bias`) seemed better in isolation because the new draft was concrete and well-argued; it was actually worse for the arc because Post 2 had promised one specific follow-on topic (survey-data asymmetry) and the substitute delivered a different topic (platform architecture). Both involve hardware; only one is a V&V arc continuation. Both candidate post-3 drafts (`ai-productivity-software-bias` shelved; `who-runs-the-drc` pulled) are now off the V&V arc track.
