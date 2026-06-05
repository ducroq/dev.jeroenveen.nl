# Draft seed — AI-augmented math: risk-mitigation, not acceleration

> **Status:** Raw seed material captured 2026-06-01 from a working session on the PDE blow-up computability project (`C:\local_dev\pde-blowup-computability`). Not yet shaped for publication.
> **Empirical backing:** Five DRs of identified-and-retracted gaps in a single day of V&V work (DR-015, DR-018, DR-019, DR-020 + one deferred). All caught by V&V machinery; none caught by additional AI authoring.

---

## Core quote

> What actually gets faster with AI is iteration cost on the **verification** side. Spinning up four parallel reviewers and getting four independent verdicts in 90 seconds is the genuinely accelerated thing. The math itself isn't faster — and the empirical evidence here is that under-verified AI math is **negatively productive**: it generates load-bearing errors that sit dormant in audit-passed registries.

## Context for the quote

A research session that adopted a V&V framework (agent-ready-papers v1.3.0) into an existing AI-generated mathematics project, then applied the framework's own machinery (anti-hallucination Step 0 / verbatim quotation; Toulmin/Whetten skeletons; multi-pass cross-model review) to its existing claim registry. The first audit pass identified one retraction (BGP Theorem 6.7 parallelization-hat misreading → DR-018) that had sat in the proof corpus for six months marked `[VERIFIED]`. A second pass — a "full review battery" of four independent reviewers — identified three further material gaps in Steps 2, 3, 4 of the project's six-step proof chain.

The math content the AI generated was sophisticated, internally coherent, and confidently presented. The errors were always in the *qualifiers*: a dropped oracle annotation in `LPO ≤_W f` (DR-015 — Theorem 6.20), a dropped parallelization hat in `LPÔ ≡_sW lim` (DR-018 — Theorem 6.7), a scope mismatch in "T* is not continuous" (DR-019 — Q&S Theorem 22.13 actually gives continuity in subcritical bounded), an oracle call in a pre-processor that's supposed to be oracle-free (DR-020 — Step 3 reduction).

None of these errors were caught by writing more proofs. All four were caught by checking — specifically: verbatim quotation of the cited source against the registered claim, and structural review forcing grounds/warrants/rebuttals to be made explicit.

## The reframe

The hype narrative: AI accelerates research output. The empirical observation from this session: AI-generated math sits at `[VERIFIED]` confidently and wrongly. The acceleration that's real lives one layer up — in the *verification iteration*: four parallel cross-model reviews complete in the time a human would spend reading the first proof.

So AI in mathematical research is a **risk-mitigation discipline**, not an acceleration discipline. Under-verified AI math is negatively productive: it manufactures confident errors at scale, which then take more verification-effort to remove than they took to generate.

The discipline-shape that follows:
- Verification tooling has to be *outside* the drafting context. Same-context "self-check" doesn't catch these errors — they were written by the same context that would self-check.
- Verbatim quotation against source PDFs catches qualifier-drops that paraphrase-based audits miss. This is a recurring pattern: the misreadings always sat in the gap between "what BGP says" and "what the project notes about BGP says".
- Multi-model cross-review with independent re-derivation catches load-bearing inferences that a single reviewer would skim. Two of the four DRs in the session came directly from cross-model agreement that the original proof's chain was unsound.

## Potential framings (for shaping later)

- "What gets faster with AI in research is not the work. It's the auditing of the work."
- "AI math is a high-error-rate, low-cost-per-iteration regime. The combination is valuable only if you spend the cost-savings on verification."
- "Under-verified AI math is negatively productive: confidence at scale."
- (LinkedIn-style hook) "The math AI wrote in this session was wrong four times in ways nobody noticed for six months. AI didn't catch them either — until four AIs were asked the same question independently."

## Adjacent drafts in this folder

- `cross-model-review.md` — the pattern itself
- `epistemic-humility.md` — adjacent stance
- `if-it-has-claims-it-has-tests.md` — the unit-of-claim discipline
- `ai-review-is-plausibility-review.md` — the gap this exploits
- `two-reviews-missed-what-reproduction-caught.md` — related failure mode
- `verification-is-a-workflow-problem-linkedin.md` — already-shaped-for-publish sibling. Consider whether this draft is a Pulse companion or a separate frame.

---

*Source session: PDE blow-up computability project, 2026-06-01 — full session committed as `d465004`..`32ea81b` on master. The DRs (`decisions/DR-015`, `DR-018`, `DR-019`, `DR-020`) are the empirical evidence trail.*
