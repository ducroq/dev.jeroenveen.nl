# Grounding is not ground truth.

*Working subtitle:* RAG anchors a model to retrieved sources at inference time. That mitigates hallucination. It does not validate the output, because the validator and the generator end up reading from the same chain. "Grounded model" in product copy collapses two things that need to stay separate.

*Working slug:* `grounding-is-not-ground-truth` (alternatives below)

*Drafted: 2026-05-29. Status: stub / parking. Glossary entry shipped; article angle not yet attempted.*

---

## Title candidates (pick at review time)

- **Grounding is not ground truth.** (declarative, working pick; mirrors the Validation entry's positioning)
- *RAG is not validation.* (sharper, technique-named; risks reading as a one-liner)
- *The grounded-model fallacy.* (most contrarian; depends on the foil section landing)
- *Two senses of "grounded" your stack is conflating.* (longer, audience-flagging)

---

## Thesis

A model "grounded" via RAG is anchored to retrieved sources at inference time. That is a hallucination-mitigation technique. It is not validation.

Validation requires an evidence source independent of the generation chain (per the **Validation** entry in `docs/glossary.md`). The retrieval corpus is part of the generation chain. When the validator checks the model's output against the same corpus the model retrieved from, validation has collapsed into self-consistency: the output is "grounded" in the source the validator is also using as ground truth.

The vocabulary is doing real damage. Product copy uses "grounded model" as if the term were synonymous with "trustworthy" or "validated." It is not. Grounding addresses one specific failure mode (fabrication of facts not in any source) and leaves the harder failure modes intact: wrong facts present in the source, right facts misapplied to the engineer's context, the chain of retrieval itself contaminated.

There is also a deeper layer (Lakoff and Johnson; the symbol-grounding problem from cognitive science). Even past the retrieval question, an LLM has the linguistic residue of human experiences without the experiences themselves. It has read millions of descriptions of borders shifting and never watched one shift. That is not solvable by adding more documents to the retrieval index.

So "grounded model" inherits two ambiguities: grounded-in-sources (technical, partially addressed by RAG) and grounded-in-the-world (deeper, not addressed). Conflating them is how vendor copy claims a solved problem the field has not solved.

---

## Why now

Specifics to confirm before drafting. Grounded generation has become the default vendor pitch for enterprise AI offerings. Multiple major vendors lean on "grounded in your data" framings. The site's audience has heard it enough times to be suspicious; the article would need to name what is actually being claimed versus what the engineering achieves.

Risk: the piece can read as semantic policing if the engineering observation is not concrete enough. The bar is to show a specific failure mode that the "grounded" claim invites.

---

## Working structure

1. **Opening.** Specific moment: a "grounded" system gives a confidently wrong answer where the source was correct but the retrieval-and-stitching went sideways. Need a real example before drafting; placeholder for now.
2. **The technique.** What RAG actually does. One paragraph; no schematics.
3. **The conflation.** "Grounded" in vendor copy means several things. Pull apart the retrieval sense from the validation sense from the understanding sense.
4. **The validation gap.** Once the validator and the generator share the same retrieval pool, validation has collapsed into self-consistency. Tie to **Ground truth** entry's independence requirement.
5. **The deeper miss.** Lakoff/Johnson layer. Even with retrieval working perfectly, the model is grounded in linguistic residue, not in the world the residue describes.
6. **Close.** Practical implication: when an offering says "grounded," ask what the validator checks against and whether it sits on the same chain.

---

## Foils to engage (find specifics before drafting)

- **FOUND 2026-06-12: Elsevier LeapSpace** ("research-grade AI"; Trust Cards judge claim-source alignment from inside the generation chain). Filed in `memory/external-references.md`. Note: `drafts/claim-verification-is-now-a-product.md` already uses one paragraph of the chain critique against this foil; if that piece ships first, this draft should go deeper (the Lakoff/Johnson layer) rather than repeat it.
- Vendor "grounded in your enterprise data" framings (Anthropic Workspace, OpenAI enterprise, Google Vertex). Need at least one concrete piece of marketing copy to argue against.
- The "15 Agent Patterns" foil (`memory/external-references.md`): same family of confusion. Evaluator-Optimizer presumes validator independence and almost never has it.
- Anything published claiming RAG "solves" or "eliminates" hallucination.

---

## Connecting tissue (already in the repo)

- Glossary: **Grounding** (just added; five senses), **Ground truth** (independence requirement), **Validation** (the activity grounding does not perform), **Evaluator-Optimizer** (closest pattern-library foil), **HITL** (where humans actually sit in the loop).
- Agent-ready-papers: `docs/framework-summary.md` Terminology Note disambiguates GROUNDED (PROVOCATION tier) from grounding (technique). The article on this side can stay clean of the PROVOCATION layer; cite the framework only if a reader asks where the terminological work lives.

---

## What would make it real

- One concrete failure-mode example, ideally from a project that's mine to talk about.
- One piece of vendor copy to argue against by name (per writing-guide section 7: weave, do not display).
- A check that the argument is not just a restatement of the Validation entry. The marginal contribution is the *vocabulary* observation: the field is using "grounded" to claim a problem solved that isn't.

---

## What could go wrong

- Reads as definitional rather than argumentative. Mitigate by anchoring on a concrete failure case in the opening.
- Reads as vendor-bashing. Mitigate by including all major vendors in the foil set and being specific about what the engineering does and does not achieve.
- Reads as the Validation post in a costume. Mitigate by making the Lakoff/Johnson layer load-bearing rather than ornamental.
