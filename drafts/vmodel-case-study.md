# vmodel.eu as application-evidence case study

*Status: seed note. Captured 2026-05-12 from a real read of `C:\local_dev\vmodel.eu\CLAUDE.md`. Fifth seed in the framework-articles queue, alongside `if-it-has-claims-it-has-tests`, `plausibility-vs-correctness`, `cross-model-review`, `auto-loading-cliff`.*

*This seed is a different shape from the other four. Those are about generalisable claims (theory, evidence, mitigation, workflow). This is about a specific running instantiation that anchors them all.*

---

## The seed

vmodel.eu is a production AI requirements-review system for engineering students. Self-hosted, GDPR-compliant. Six-agent pipeline (structure check, INCOSE 42-rule, quality review, coverage, traceability, problem-statement alignment) on one GPU, two model families (Gemma 3 27B and Phi-4 14B), deterministic scoring on top of LLM findings (no LLM scoring), temperature=0 enforced by ADR-018, calibration gate of within-1 agreement ≥80% against baseline before deploying prompt changes. 870 tests, 122-report ground-truth baseline, 64-report held-out validation set, 20 ADRs.

This is *exactly* what the WHY-arc prescription looks like when an engineer who actually believes "validation is the harder half" builds an AI system. Every architectural choice is the answer to a validation question that most AI products skip. The case study writes itself once the story is named.

## Why this is strong application-evidence

For the four framework seeds:

| Framework seed | What vmodel.eu instantiates |
|---|---|
| `if-it-has-claims-it-has-tests` | Findings have priority and confidence; trace to IEEE 29148 / INCOSE / V-model citations; calibration gate is the SE quality gate; held-out validation set is the test coverage. SE shape, in production. |
| `plausibility-vs-correctness` | `_validate_findings()` drops garbage, per-finding confidence levels, `context_warning` propagation, deterministic-scoring-not-LLM-scoring. The system explicitly does not trust plausible-looking LLM output. |
| `cross-model-review` | Different models for different agents (Gemma 3 27B for quality/alignment, Phi-4 14B for coverage/traceability). Cross-model *task allocation* rather than cross-model *review of same output*; sibling pattern worth naming. |
| `auto-loading-cliff` | Standard agent-ready-projects scaffolding at production scale: Before You Start with 8 task-triggered pointers, memory/ with privacy-protocol + calibration-history + gotcha-log, 20 ADRs. |

For the AE patterns directly: Learn the Material (20 ADRs document reasoning), Layer Your Verification (four distinct verification layers: structural detectors → heuristic checks → LLM agents → deterministic scoring → self-validation), Context Is Architecture (privacy protocol, multi-agent pipeline, schemas), Reproduce Don't Assess (temperature=0, deterministic scoring, calibration gates, 122+64 baseline+heldout). vmodel.eu's CLAUDE.md already documents this as a source project for augmented-engineering.

## Why this is article-worthy on dev.jeroenveen.nl

- The site already has `ese-bot-eu-sovereign-rag` as the year-in-review piece on a smaller student-facing AI system. vmodel.eu is the deeper sibling: same student-data sensitivity, more substantive engineering, more defensible-because-graded-against-standards.
- It is the concrete evidence layer that the framework articles need. Theory and evidence travel further as a pair than either does alone.
- The argument shape is different from the framework articles: not "here is the principle," but "here is what happens when you actually try to do this." That is a register the dev.jeroenveen.nl audience reads carefully.

## Possible homes

1. **New standalone dev.jeroenveen.nl article (case study).** Argument-form title candidates:
   - *"Calibration gates before prompt changes: a year of running AI requirements review."* (mechanism-foregrounded)
   - *"How to ship an AI review system you can actually defend."* (audience-filter foregrounded)
   - *"What an AI grader looks like when validation is the harder half."* (WHY-arc connected)

   Lean: the first, with the third as the subtitle.

2. **Cross-referenced evidence inside the framework articles.** Each of the four framework seeds gets one or two paragraphs pointing at vmodel.eu as the worked example. Lower lift, but you spend the strongest evidence cheaply.

3. **Conference talk material.** A 30-minute walkthrough of vmodel.eu under the heading "validation infrastructure in production" would be a strong talk for an engineering-AI / requirements-engineering audience. Talk and article can share the same evidence skeleton.

Lean: ship a framework article first using vmodel.eu as the implicit worked example (option 2), then write the standalone case study (option 1) afterwards with the framework article linkable as the theory this case instantiates. That gets double value out of the same evidence.

## Open questions before drafting

- **Disclosure.** vmodel.eu's CLAUDE.md hard constraint: "Never read raw student files. Never `--verbose` on PII scripts." The article needs to be aggregate-level only. Specific student examples are out; aggregate calibration metrics, agreement rates, false-positive / false-negative counts on the held-out set are in. Worth confirming with Jeroen which numbers can be public.
- **What is the strongest single headline number?** Candidates: within-1 agreement ≥80%, 122-report baseline + 64-report held-out, 870-test suite, six-agent pipeline running on a single GPU. The opening paragraph needs *one* number that earns the reader's attention. Probably the calibration gate number (80% within-1) because it doubles as the validation-discipline signal.
- **Positioning relative to ese-bot.** Two different student-facing AI systems running in production at HAN, both GDPR-safe, both written up by Jeroen. Risk of looking like "another notes from my classroom" piece. Fix: anchor the article around the *engineering* (calibration gates, validation layers) rather than the *classroom* (students, courses). The students are the data source, not the subject.
- **Cross-model task allocation vs cross-model review.** vmodel.eu does the former, not the latter. If `cross-model-review.md` ships first, this article should be clear about the distinction so the two pieces are siblings rather than overlapping.
- **The agent-ready-projects version drift.** vmodel.eu pins v1.3.4, framework is at v1.10.0. Same class as issue #6 here. If a version-pull happens before this article ships, the article can name v1.10.0; if not, name v1.3.4 honestly and note the drift.

## Reusable phrasings

- *"Calibration gates before prompt changes."*: strongest mechanism-line. Names the discipline in one phrase. Reusable as title, opening, and closing.
- *"Deterministic scoring on top of LLM findings (no LLM scoring)."*: names the structural fix that most production AI systems do not bother with. Sharp.
- *"The implementation is the contract."*: phrase already in the Witek 2026-04-29 thread; fits naturally inside this article when explaining why requirements review is exactly the domain where validation cannot be skipped.
- *"Within-1 agreement ≥80% against baseline before deploying prompt changes."*: concrete version of the calibration-gate claim. Numbers make the discipline visible.
- *"Six agents on one GPU, sequential, temperature=0."*: economic restatement of the pipeline. Reads as engineering, not productivity-deck.

## Connection to the WHY arc

This case study is the natural *coda* for the WHY arc. The arc says:

- Post 1: production is cheap, validation is hard
- Post 2: seniors validate because they have the pattern library
- Post 3 (pending): HAZOP / domain bias / who-validates

The vmodel.eu article would be the implicit "here is what one engineer who took the arc seriously actually built." Not an explicit "as I wrote in posts 1-3", but the engineering reads as the answer the arc was setting up. That positioning makes the case study work whether or not the reader has read the arc.

## How it sits next to the other four seeds

Update to the quartet table in `if-it-has-claims-it-has-tests.md`:

| Seed | Layer | What it provides |
|---|---|---|
| `if-it-has-claims-it-has-tests` | Theory | The SE shape that generalises |
| `plausibility-vs-correctness` | Evidence (failure mode) | What goes wrong without the framework |
| `cross-model-review` | Mitigation | What partially fixes one class of failure |
| `auto-loading-cliff` | Workflow | The repo-level scaffolding |
| `vmodel-case-study` (this) | Application | A running instantiation that anchors all four |

## Decision

Hold as seed. Strongest path is: ship one framework article first (probably `plausibility-vs-correctness` because the empirical hook is sharpest) using vmodel.eu as the implicit worked example, then write the standalone case study afterward. Revisit when WHY post 3 ships and a framework article is next on the queue.
