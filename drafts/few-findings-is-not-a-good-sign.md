# Few findings is not a good sign.

*Working subtitle:* An AI reviewer that returns little to say is read as evidence the work was good. In a production requirements reviewer, that reading was wrong often enough to be measured: reports with few model findings were frequently the ones the model could not get purchase on. Silence from a reviewer is ambiguous, and nothing in the output distinguishes the two cases.

*Working slug:* `few-findings-is-not-a-good-sign` (alternatives below)

*Drafted: 2026-08-29. Status: outline. Source system: vmodel.eu (production, MVP feature-complete). Numbers NOT yet verified to primary — see the Verification section at the bottom before any of this becomes prose.*

---

## Title candidates (pick at review time)

- **Few findings is not a good sign.** (declarative, working pick; the finding stated flat)
- *An empty review is ambiguous.* (more general, less concrete; loses the measurement)
- *Silence is not a passing grade.* (most quotable; risks reading as aphorism-first)
- *The quiet-report problem.* (names a phenomenon; weakest as an argument-shaped title)

Per the packaging checklist, the title must be an argument. All four are. The working pick is the one that states the counterintuitive claim without metaphor.

---

## Thesis

An LLM used as a reviewer produces findings. The natural reading of *few findings* is *good work*. That reading is unsafe, because a short, thin or badly formatted document gives the model less to criticise — so it also produces few findings, and the output looks identical.

This is not a hypothetical failure mode. It was measured on a production system, and it killed a feature.

The deeper claim, which is the one worth carrying away: **a signal that does not move when quality moves is not a measurement.** That applies to an LLM's finding count, and it applies just as brutally to conventional checks. Two independent parts of the same project failed that way in the same year.

---

## Why this is on-corpus, not a new direction

This is the shipped system underneath three already-published pieces:

- `the-model-is-not-the-grader` argued the separation. vmodel.eu is where the separation was actually built, and the article can now say what it cost.
- `ai-review-is-plausibility-review` argued that a single pass measures plausibility. The INCOSE detector tuning below is that argument with a trigger-rate table attached.
- `verification-is-a-workflow-problem` argued the verifier has to sit outside. Here the scorer is deterministic Python sitting outside the model entirely.

The reader gets the pattern they have already met, with a production system and numbers behind it for the first time.

---

## Structure (hybrid form, target 1,100–1,300 words)

### Opening — 2 short paragraphs

Open on the concrete decision, not on AI-in-education framing. Something close to:

> We built a thing that reads student requirements documents and writes them feedback. The obvious next step was to let it grade them too. We tried that, measured it, and took it back out.

The second paragraph names the trap in one line: the model's own findings looked like the perfect scoring signal, and using them made every threshold worse.

Audience filter check: a senior engineer evaluating an LLM-as-judge pipeline recognises themselves in sentence one. A generic scroller bounces. Do **not** open on students, on education, or on the tool — the reader is not in that world.

### Middle — 6–8 paragraphs, one idea each

1. **The setup, minimally.** A pipeline over a structured document: extract typed units, run several narrow reviewers, produce findings and a score. Enough detail to make the rest legible; no architecture tour. Resist listing the agents.

2. **The regression-to-mean wall.** Local models at 14B compress high baselines severely — good work and mediocre work both drift toward the middle. This is stated in the calibration record as unsolvable at that scale. That is what forced scoring out of the model and into deterministic Python, which reached 96% within-1 of expert scores.

3. **The tempting shortcut.** With a deterministic scorer working, the remaining question was whether the model's findings could refine it — a bounded ±1 adjustment driven by how many serious findings the reviewer raised. Intuitive, cheap, and it uses signal already being computed.

4. **The measurement.** It hurt at every threshold tried: 0 helped / 3 hurt, then 3 / 15, then 5 / 17. Within-1 accuracy fell from 96% to 92% at the most permissive setting. This is the paragraph that earns the article; give the numbers room and do not soften them.

5. **The root cause, which is the actual insight.** Few findings does not mean good. A short or badly formatted document hands the model less to work with, and the model reports what it found, which was little. The output cannot distinguish "this is clean" from "I could not read this." *Absence of criticism is not evidence of quality* — and an LLM reviewer has no way to signal the difference, because both cases genuinely produced few findings.

6. **The same failure from the opposite end.** The rule-based detectors had the mirror problem. Passive voice fired on 58–88% of reports **at every quality level**. EARS non-conformance fired on 75–100%. A detector that fires on everything discriminates nothing, and together they buried the output at 27.7 findings per report. Tuning cut that to roughly one. What survived were the detectors whose rate actually tracked quality — subjective terms at 18% on the worst reports and 0% on the best. What died were the ones that were always right and never informative.

7. **The generalisation, stated once.** Both failures are the same shape: a quantity that does not move when the thing it claims to measure moves. The finding count does not fall when quality rises. The passive-voice rate does not fall either. Each looks like a signal, and each is a constant wearing a signal's clothes.

8. **The uncomfortable mirror.** The same project's test harness had a check that parsed the *passed* count from a test run — a number invariant under failure, so it reported healthy on a red suite. That is not an analogy. It is the identical defect, in the plainest possible code, found by people who had just spent months learning it about a language model. Worth one paragraph, stated without triumph. This is where the piece stops being about LLMs.

### Closing — 1–2 short paragraphs

Land on the question the reader can act on rather than a summary. Something in the direction of: before trusting any reviewer, human or model, ask what its output looks like when it has nothing to say — and whether you could tell that apart from approval.

**Comment prompt (required).** Draft: *"Where in your pipeline does 'nothing to report' get read as 'nothing wrong'?"* — medium-tight per the calibration note in `memory/external-comments.md`: specific enough to filter, broad enough that the answering population actually exists. Avoid the over-tight shipped-system-specific ask that zeroed out comments on `the-model-is-not-the-grader`.

---

## What to leave out

- **The agent architecture.** Six reviewers, model assignments, merge logic. It is the most interesting part to the author and the least interesting to the reader. One clause, no diagram.
- **The tool as a tool.** No link-led plug, no capability list, no "you can try it." `memory/project_not_commercial.md` rules out marketing framing, and the honest register is stronger anyway. The site link belongs at the end, once, as provenance.
- **Students and education.** The subject is LLM-as-judge failure. The domain is incidental and naming it invites the wrong audience.
- **The general-feedback-engine thesis.** `docs/open-questions/02` is still at diverge phase with the prior-art sweep pending. Speculative, and it would dilute a piece whose strength is that everything in it was measured.
- **Model-shootout detail.** Gemma 27B vs Phi-4 14B vs Qwen 3 14B is a good technical note but a different article; Qwen's thinking mode costing ~7x latency for no quality gain is its own hook. Do not smuggle it in — the packaging checklist calls this the extractable-standalone-post problem.

---

## Institutional framing — decide before drafting

The dsp-workshop decision of 2026-08-29 was to withhold the employer's name to keep it negotiable (`dsp-workshop/memory/feedback_institutional_attribution.md`). This article should be consistent with that or consciously depart from it.

Evidence that consistency is easy here: `docs/RUNBOOK.md` documents the two machines as a Hetzner VPS and a home-lab Proxmox host, and `server/app.py` gates on educational email worldwide — 20+ international suffixes plus 25 Dutch institutions, with no single institution privileged. So the piece can be written truthfully with no institution named, because none is architecturally special. **Confirm the runbook is current before relying on this.**

No real student work in any example. Synthetic requirements only, per the project's privacy protocol.

---

## Verification — REQUIRED before prose

Every number in this outline came from `memory/calibration-history.md`, which is an **intermediate analysis file**. `CLAUDE.md` is explicit: trace each load-bearing number to primary source, not to an intermediate. Nothing here is publishable until that is done.

Primaries named in the calibration record:

| Claim | Primary artifact | Reachable? |
|---|---|---|
| ±1 adjustment hurt at every threshold (0/3, 3/15, 5/17) | `calibration/results/held_out_pipeline.json` | on gpu-server, not in repo |
| 96% within-1 deterministic scorer | same batch run | on gpu-server |
| Passive voice 58–88%, EARS 75–100%, 27.7 → ~1 findings | `calibration/calibrate_incose.py` output | check repo |
| Subjective terms 18% vs 0% | same | check repo |
| Corpus sizes: 122 baseline / 50 annotated / 64 held-out | `dataset/`, extraction records | check repo |
| passed-count test defect | `dsp-workshop` gotcha log + `tests/verify_state.sh` history | in repo, verifiable |

Open the verification record as `docs/verification/few-findings-is-not-a-good-sign.md` and apply Step 0 plus Steps 4–6. Assign a confidence tier per claim and map it to article language per writing-guide Section 7. Any number that cannot be traced to a primary gets requalified or cut — not hedged into the prose.
