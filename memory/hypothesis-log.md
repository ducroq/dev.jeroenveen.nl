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

### [2026-05-12] Post-2 (senior-trust) reception will not be successfully claimed by conservatives as anti-adoption ammunition — *DUE FOR REVIEW*

**Position (provisional):** Senior-trust article (published 2026-05-12) will not be successfully misread as "don't adopt AI" by conservative-leaning readers. The frame ("seniors are absorbing the validation cost *while using* AI") is robust enough on its own. If misreads happen, they will be isolated, not amplified.

**Alternative:** Comments / shares pick up the post as evidence for "AI is bad / AI doesn't work" or for refusing AI adoption. Signal: comments using "this is why we shouldn't use AI" framing; shares to anti-AI accounts or communities; requests to elaborate the anti-adoption read; AI-skeptic LinkedIn voices reposting without the validation-cost framing.

**Method:** Monitor post-2 LinkedIn comments + repost behaviour for 5-7 days. Skim engagement for the misread frame. Three outcomes: misread is rare and not amplified → Position holds. Misread is present but not dominant → file post-3 framing-risk note (already done 2026-05-12) and proceed. Misread dominates → intervene with a clarifying reply or a short follow-up note before post 3.

**Revisit trigger:** 5-7 days post-publish (2026-05-17 to 2026-05-19). **Trigger has fired — entry is due for revisit as of 2026-05-18.**

**Review by:** 2026-05-22 — hard backstop.

**Domain:** WHY arc, post 2, reception monitoring
**Status:** open — **DUE FOR REVIEW**

---

### [2026-05-18] The V&V arc closer is a methods piece grounded in own work

**Position (provisional):** Post 3 of the V&V arc should be one of the methods pieces Jeroen actually uses (candidates: Reproduce-Don't-Assess from the driven-pendulum case; OPAL's five-layer verification; the assertion patterns in OPAL or vmodel.eu; whatever the AE site's most-developed pattern is). The substitution attempts with `ai-productivity-software-bias` (shelved 2026-05-18, literature-bias frame) and `who-runs-the-drc` (pulled 2026-05-18, cross-domain platform survey) were both diagnosed as wrong shape for an arc that's been about practitioner cognitive work. The right shape: one specific method, grounded in own work, with what it catches and what it costs, framed as observation rather than how-to.

**Alternative:** The methods piece, when drafted, lands as too narrow or too internal. Reads as tool documentation rather than the closing piece of an observation arc. Signal: in cold-read, the piece doesn't bridge naturally to the practitioner pattern-library framing from post 2; comments engage with the method's particulars but not with the arc-level observation that makes the method matter.

**Method:** Draft one methods piece. Cold re-read against the arc's promised tone (observation grounded in own work, plus a forward look that lets the AE-pattern pieces follow naturally). If the piece reads as observation + arc closure, Position holds. If it reads as how-to, restructure to lead with the observation that the method is grounded in, with the method itself in the second half.

**Revisit trigger:** Drafting begins on a methods piece for the V&V arc.

**Review by:** 2026-07-01 (give it about six weeks for the drafting to begin).

**Domain:** WHY/V&V arc, post 3, methods pieces
**Status:** open

---

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

### [2026-05-18] Post-3 reframe holds: descriptive AE-definitional shape lands cleaner than the literature-bias shape

**Outcome (2026-05-18, same-day pull after publish):** Refuted at the arc level. The reframe correctly pointed away from literature-bias complaint and toward practitioner observation, and the three-platform comparative (`who-runs-the-drc`) shipped that day. Within roughly two hours of publishing, the deeper diagnosis surfaced: the article is doing AE-cross-domain work, not V&V arc closure. Post 2 promised the survey/research asymmetry in non-software domains; the published article delivered a platform-architecture comparison in non-software AI. Same domain, different topic. The piece pre-empted the methods pieces that should be the V&V arc closer (Reproduce-Don't-Assess, OPAL's layered verification, the assertion patterns used in own work). Pulled the same day. Article body, draft, verification record, and cover image retained for potential recast as an AE-cross-domain piece in a sibling arc. The article never reached LinkedIn cross-post; lived on the site for about two hours, zero known external readers.

**Larger lesson logged:** When substituting a draft for an arc position, audit against the arc's *promised topic* (from prior posts' forward-looks), not just against the draft's own merits. The substitution attempt (`who-runs-the-drc` for `ai-productivity-software-bias`) seemed better in isolation because the new draft was concrete and well-argued; it was actually worse for the arc because Post 2 had promised one specific follow-on topic (survey-data asymmetry) and the substitute delivered a different topic (platform architecture). Both involve hardware; only one is a V&V arc continuation. Both candidate post-3 drafts (`ai-productivity-software-bias` shelved; `who-runs-the-drc` pulled) are now off the V&V arc track.
