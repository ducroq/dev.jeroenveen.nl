# Measure the geometry before reaching for a bigger model.

*Working subtitle:* When a single cosine threshold can't separate your clusters from your non-clusters, the reflex is to add a reranker. The discipline is to look at the joint distribution first and let the shape pick the treatment.

*Working slug:* `measure-the-geometry-before-the-model` (open to alternatives — see candidates below)

*Drafted: 2026-05-20. Status: stub / cold-re-read parking. Source data and decision already on disk; prose not yet attempted.*

---

## Title candidates (pick at review time)

- **Measure the geometry before reaching for a bigger model.** (mechanism-forward, working pick)
- *When cosine doesn't separate.* (sharper, more concrete)
- *Add features, not rerankers.* (declarative — the contrarian thesis stated outright)
- *A three-shape decision tree for embedding overlap.* (most pedagogical; closer to a how-to header)

---

## Thesis

The default move when an embedding-similarity threshold misclassifies pairs in both directions — false negatives below the threshold, false positives above — is to bolt a second-stage classifier on top. An LLM verifier. A cross-encoder. Something bigger.

There is a cheaper, more disciplined branch that usually gets skipped: **measure the joint distribution of labeled pairs first**, classify the failure into one of three shapes, and let the shape — not the architectural reflex — pick the treatment.

The three shapes:

1. **Clean separation** — distributions don't overlap meaningfully. Tune the threshold; you're done.
2. **Partial overlap** — distributions overlap in a band that no single threshold can resolve. *This is the interesting case.* Two valid treatments: (a) second-stage rerank, or (b) feature augmentation. (b) is almost always the better starting move and almost always the one skipped.
3. **Both jammed at the top of the substrate's range** — the embedding itself can't tell them apart. Different substrate.

The post argues that (2b) — feature augmentation — is under-used because the literature reflex is to architect, not to measure. Once you have the labeled pairs and have read their geometry, augmenting the existing scoring step with cheap, interpretable, *falsifiable* features (entity overlap, time delta, lead-paragraph cosine, source-pair priors) is usually both better-performing and more debuggable than escalating to a heavier comparator.

---

## The worked example (source repo)

Repo: **NexusMind** — https://github.com/ducroq/NexusMind

The example is a story-deduplication problem inside a news-aggregation pipeline. Articles from many feeds get clustered if their `e5-large` embeddings cross a cosine threshold (0.92 within-source, 0.88 cross-source). When clustering is too strict, real duplicates split; when too loose, topical near-misses (e.g., two unrelated malaria articles from the same week) merge.

I had been carrying a provisional position that this was a threshold-tuning problem. The disciplined move was to measure first.

### The measurement

Script: `scripts/research/measure_matching_geometry.py` — commit `633850f`.

Eight hand-curated test cases from production failures spanning April 2026 — three should-cluster, five should-NOT-cluster. 120 articles, 3538 pairs.

Outputs live at `data/research/matching-geometry-2026-05-20/` on `sadalsuud` (gitignored under `data/`):

- `cases.json` — resolved per-case article list
- `sims.json` — pairwise cosine similarity matrix per case, with same-source flag
- `histogram.json` — flat should-cluster vs should-NOT-cluster sims
- `summary.md` — per-case min/median/max + band counts
- `manifest.json` — provenance: git rev, archives used, model

### The headline numbers (all cross-source pairs, where all the action is)

| | n | min | median | max | ≥ 0.88 |
|---|---:|---:|---:|---:|---:|
| should-cluster (positive) | 22 | 0.806 | 0.886 | 0.996 | 14 (8 miss) |
| should-NOT-cluster (negative) | 3497 | 0.750 | 0.807 | 0.891 | 1 |

At the live 0.88 cross-source threshold: **recall 63.6%, precision 93.3%**. The recall-vs-precision asymmetry is sharp — and the overlap band [0.80, 0.89] contains real examples of both classes that the substrate cannot rank apart by cosine alone.

→ Shape: **partial overlap.** Branch (2).

### Why not "throw an LLM at it"

The same-source / cross-source split doesn't help — 22 of 23 should-cluster pairs are cross-source; the 18 same-source negatives all sit at 0.844–0.870 (already rejected by the 0.92 within-source threshold). Tightening or relaxing thresholds, or splitting more finely on source, doesn't separate the overlap band.

But a small set of *features* would. From the per-case shapes:

| Candidate feature | Why it would help the specific failures |
|---|---|
| Named-entity Jaccard (PERSON/ORG/LOC/EVENT) | Hippo-cull pairs share entities; topical near-misses don't |
| Title-only cosine | Hero-event articles repeat the title noun-phrase; aggregator/topic-page false positives don't |
| Publication-time delta | The case-8 false-positive cluster spans weeks of unrelated AI news; real should-cluster pairs sit within hours |
| Source-pair prior | Some source pairs co-cluster constantly on topics, never on stories |
| Lead-paragraph cosine (first ~300 chars) | Cuts the long-tail body noise driving the false-similars |

A logistic regression on these features against the existing labeled pairs would almost certainly out-perform a 0.88 threshold *and* be debuggable in a way no LLM-verifier is. The 23 should-cluster pairs is a small training set; direction-finding is feasible, production thresholds need more data.

---

## Associated issues

- **#213** (open, status: measured, decision branched) — https://github.com/ducroq/NexusMind/issues/213
  *Investigate story-dedup matching-pass: precision + recall gap (sibling to centroid-policy investigation).*
  The investigation that produced the measurement above. Issue is method-locked: a comment posted before the data landed declared the three-shape decision tree and committed to following whatever shape the data showed. The "agent does not pre-decide" pattern carries over from the centroid-policy sibling investigation.

- **#214** (closed 2026-05-20) — https://github.com/ducroq/NexusMind/issues/214
  *story_dedup: drift check uses E5(title) against E5(title+content) centroid — structurally confused for 6.2% of clusters.*
  Sibling fix shipped earlier in the same session, demonstrates the same "measure before architecting" discipline applied to a smaller question.

- **#211** (closed 2026-05-18) — https://github.com/ducroq/NexusMind/issues/211
  *story_dedup migration runs full embedding pass every cycle (~14 min).*
  Earlier centroid-policy investigation that established the locked-decision-tree pattern this work inherits.

---

## Distinctive angle vs. typical writeups in this space

What I have that the standard "RAG / dedup architecture" post doesn't:

- **A published labeled dataset.** `sims.json` (679 KB) plus the eight case studies are a small but real reference benchmark for cross-source story-dedup. I'm not aware of an equivalent open dataset.
- **A pre-registered decision tree.** The issue lock comment (in #213) commits to the branching diagnosis *before* the data is collected. Most writeups are post-hoc rationalizations of an architectural choice.
- **A reproducible measurement script in version control.** `scripts/research/measure_matching_geometry.py` runs against two tarballs in `data/archived/`, ~8 min on CPU. Anyone with the archives can re-run it.

These three together turn the post from "here's an opinion about retrieval architecture" into "here's a measurement protocol, here's the data it produced, here's the decision it forced."

---

## Reflexivity note (likely a closing paragraph)

The thesis of this post — *measure-then-design, prefer cheap interpretable features* — is exactly what the `dev.jeroenveen.nl` publishing pipeline already enforces with `docs/verification/<slug>.md` (anti-hallucination audit on load-bearing numbers, traced to primary sources). Same discipline, different domain. Worth a short closing paragraph noting that the move generalizes — the artifact (article, retrieval system, equation, ML model) keeps changing; the move (measure before reaching for architecture) stays the same.

---

## For the writeup (open questions when prose-drafting begins)

- **Lead with the contrarian thesis or with the worked example?** "Add features, not rerankers" is a sharper opening; the worked example builds the case more honestly. The V&V-arc drafts in this folder lean toward the worked-example opening.
- **How much measurement-script detail belongs in the post vs. linked-out?** The reproducibility angle suggests inlining the schema (case → resolve other_sources → embed → pairwise sim → label) but not the full 576 lines.
- **Should the small-n caveat dominate?** n=23 should-cluster pairs is small. The conclusion (overlap exists, can't be split by single threshold) is robust; specific feature-classifier thresholds will need more data. Honest framing: this is direction-setting work, not a production result.
- **Cross-post target?** Same as `the-model-is-not-the-grader` and `the-work-is-splitting` — LinkedIn Pulse longform + short feed post. Audience overlaps: applied ML / retrieval engineers who keep getting told to add an LLM.

---

## Open follow-ups (don't lose these)

- Implementation lane in NexusMind: **feature augmentation** under #213, *not* second-stage rerank. Branch decided 2026-05-20 from the measurement above.
- The `sims.json` / `cases.json` will need a license decision before any public release as a reference dataset (CC0? CC-BY?). The source articles are URL-referenced, not redistributed, so the open question is the labeling work itself.
- The locked-decision-tree workflow pattern (`#213` lock comment + sibling investigation discipline from `#211`) is itself worth a separate post — there's overlap with the V&V-arc material but the agent-collaboration angle is distinct. Park for now.
