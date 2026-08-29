# Verification record: *Few findings is not a good sign.*

**Article**: not yet written — outline at `drafts/few-findings-is-not-a-good-sign.md`
**Article slug**: `few-findings-is-not-a-good-sign`
**Last verified**: 2026-08-29
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per the agent-ready-papers template. This piece is unusual for this site: every load-bearing number is **own-work measurement** from `~/repos/veen-systems/vmodel.eu`, not external literature. That does not lower the bar. `CLAUDE.md` requires tracing each number to primary source rather than to an intermediate ANALYSIS file, and the intermediate here is `vmodel.eu/memory/calibration-history.md`, which is where the outline's numbers came from.

**Headline result of this pass: the supporting thread verifies cleanly against primary data; the central claim does not, because its primary artifact is not on this machine.**

---

## Status summary

| # | Claim | Primary | Tier |
|---|---|---|---|
| 1 | Corpus is 122 baseline + 64 held-out = 186 | `incose_calibration.json` | **VERIFIED** |
| 2 | Subjective terms discriminate: 18% → 0% | `incose_calibration.json` | **VERIFIED** |
| 3 | EARS ubiquitous share 7% → 27% | `incose_calibration.json` | **VERIFIED** |
| 4 | Post-tuning ~1 finding/report | `incose_calibration.json` | **VERIFIED, number wrong in the intermediate** |
| 5 | Vague terms 52% vs 22% | `incose_calibration.json` | **VERIFIED BUT SELECTIVE — do not use as stated** |
| 6 | Passive voice 58–88% at every quality level | not in repo | **UNVERIFIABLE HERE** |
| 7 | EARS non-conforming 75–100% trigger rate | not in repo | **UNVERIFIABLE HERE** |
| 8 | Pre-tuning 27.7 findings/report | not in repo | **UNVERIFIABLE HERE** |
| 9 | ±1 adjustment hurt at every threshold (0/3, 3/15, 5/17); 96% within-1 | `held_out_pipeline.json` — **on gpu-server only** | **UNVERIFIABLE HERE — and it is the article's spine** |

---

## Claim 1 — corpus size

Intermediate says 122 baseline reports + 64 held-out.

Measured directly from `calibration/results/incose_calibration.json`: `n = 186`, `Counter({'baseline': 122, 'held_out': 64})`. Exact match, independently arrived at.

**Tier: VERIFIED.** Safe to state as fact.

---

## Claim 2 — subjective terms discriminate

Intermediate: *"subjective terms (18% score-1, 0% score-5)"*.

Measured, share of reports where the detector fired, by expert quality score:

| score | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| subjective | 18% | 11% | 6% | 0% | 0% |
| (reports) | 33 | 36 | 52 | 50 | 15 |

Endpoints match the intermediate exactly, **and the middle is monotone**, which the intermediate did not claim and which strengthens it. This is the cleanest discriminator in the set.

**Tier: VERIFIED.** The monotone middle can be stated too.

---

## Claim 3 — EARS ubiquitous share tracks quality

Intermediate: *"the summary stat (% ubiquitous) IS useful: 7% (score 1) → 27% (score 4)"*.

Measured as `(total_reqs − non_conforming) / total_reqs`, aggregated per score:

| score | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| conforming share | 7.6% | 10.9% | 18.3% | 26.9% | **25.0%** |

7.6% → 26.9% matches. **Caveat the intermediate omits**: score 5 does not continue the trend, it plateaus slightly below score 4 (25.0%, n=15).

**Tier: VERIFIED with a caveat.** Cite it as 1→4 and say so, or state the plateau. Do not write "rises with quality" unqualified.

---

## Claim 4 — findings per report after tuning

Intermediate: *"After tuning: ~1 finding/report."*

Measured mean over 186 reports: **0.67**.

The intermediate rounds up, and in the direction that flatters the tuning less, so nothing is being oversold — but 0.67 is the number and it is more striking than "~1".

**Tier: VERIFIED, use 0.67.** This is exactly why the trace-to-primary rule exists.

---

## Claim 5 — vague terms

Intermediate: *"vague terms (52% vs 22%)"*.

Measured:

| score | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| vague_terms | 52% | 28% | 27% | 22% | **40%** |

52% and 22% are real — they are scores 1 and 4. But score 5 rises to 40%, so the detector is **not** monotone and the "52% vs 22%" framing works only by stopping at score 4.

n=15 at score 5, so this may be noise. It may also be real: the best reports are longer and more specific, and a longer document has more surface for a vague-term regex to hit.

**Tier: DO NOT USE AS STATED.** Either drop this claim, or state the full row including the score-5 reversal and say the sample is small. Using "52% vs 22%" as-is would be exactly the selective-endpoint reporting the article is arguing against, which would be a bad look in this piece specifically.

---

## Claims 6–8 — the pre-tuning detector rates

Intermediate: passive voice fired on 58–88% of reports at every quality level; EARS non-conformance 75–100%; output ran at 27.7 findings/report before tuning.

`incose_calibration.json` is the **post-tuning** run. Passive voice and EARS non-conformance had already been demoted to summary stats, so neither appears in `detector_counts` and the mean findings figure is the tuned 0.67. The pre-tuning run is not in the repository.

**Tier: UNVERIFIABLE ON THIS MACHINE.** These are load-bearing for outline middle-paragraph 6, which is the "a detector that fires on everything discriminates nothing" beat. Either locate the pre-tuning results, re-run `calibrate_incose.py` against the pre-demotion config, or rewrite that paragraph around the verified subjective/vague/EARS numbers alone — which do carry the point, since claim 2 shows what discrimination looks like by contrast.

---

## Claim 9 — the ±1 adjustment failure (THE SPINE)

Intermediate: adjustment hurt at every threshold — `max_serious=0`: 0 helped / 3 hurt; `=1`: 3 / 15; `=2`: 5 / 17; within-1 falling 96% → 92%. Root cause: few findings does not mean good work.

Primary named by the intermediate itself: `calibration/results/held_out_pipeline.json`, **"on gpu-server"**.

Searched the working tree: no `held_out_pipeline*` anywhere. The generating script `calibration/run_held_out_pipeline.py` and the analysis script `calibration/calibrate_score_adjustment.py` are both present, so the result is reproducible in principle — but it was a 3-hour batch job over 64 reports and needs Ollama plus the models.

**Tier: UNVERIFIABLE ON THIS MACHINE — and this is the article's central claim.** Nothing in the outline's middle paragraphs 3–5 or its thesis can ship until this is traced.

**Three routes, cheapest first:**

1. `ssh gpu-server` and read the JSON. If it is still there, copy it into the repo — see the standing risk below.
2. Re-run `calibrate_score_adjustment.py` against a retained held-out artifact, if one exists on that host.
3. Re-run the full 3-hour batch. Last resort.

**Standing risk, and it is the dsp-workshop lesson repeating.** The single number this article rests on lives on one machine, in one file, outside version control, produced by a job nobody wants to re-run. That is the same shape as the deploy-artifact finding in `dsp-workshop/docs/hypothesis-log.md` — *the artifact size is not recoverable after the fact, so a skipped reading is a permanent hole, not a delay.* Whatever happens with the article, that file should be in the repository.

---

## Institutional and privacy checks

| Check | Result |
|---|---|
| Any institution named in the planned piece? | No. Consistent with `dsp-workshop/memory/feedback_institutional_attribution.md` (2026-08-29). |
| Is any institution architecturally special, such that omitting it would misdescribe the system? | **No.** `server/app.py` gates on educational email worldwide — 20+ international suffixes plus 25 Dutch institutions, none architecturally special. `docs/RUNBOOK.md` documents a Hetzner VPS and a home-lab Proxmox host. **Confirm the runbook is current** before relying on the hosting half. |
| Student work in examples? | None planned. Synthetic requirements only, per the project privacy protocol. |
| Commercial framing? | Excluded by `vmodel.eu/memory/project_not_commercial.md`. Outline's "What to leave out" enforces it. |

---

## Verdict

**Not ready to draft prose.** The supporting material (claims 1–4) is verified and stronger than the intermediate suggested. The spine (claim 9) is untraced, and three of the four detector-rate claims cannot be checked here.

Recommended order: retrieve `held_out_pipeline.json` from gpu-server and commit it; drop or restate claim 5; decide whether paragraph 6 gets its pre-tuning numbers or gets rewritten around the verified ones. Then draft.
