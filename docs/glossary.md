# Glossary

Working definitions for terms that show up in Jeroen's writing or in posts he engages with. Dual purpose: keep his own usage consistent across drafts, and track where common usage drifts from what he means or what an authority means.

Two kinds of entries:

1. **Coined or repositioned**: terms Jeroen uses with a specific load-bearing meaning. The "As Jeroen uses it" definition is the house definition.
2. **Field vocabulary (in circulation)**: terms imported from the wider field (Anthropic, agent-pattern posts, AI/ML literature). The standard definition leads; commentary on drift or AE-frame relevance follows.

Grows organically. An entry earns its place when (a) a term gets used twice and the two usages might not align, (b) someone else's usage drifts from what matters for positioning, or (c) the term is in heavy circulation and writing against it requires fluency.

Not a comprehensive field dictionary. If a term is widely understood and Jeroen uses it the same way everyone else does, it does not need an entry.

---

# Coined or repositioned

## Validation

**As Jeroen uses it:** establishing that a generated artifact actually meets the requirement, against an evidence source independent of the generation process. The independence is the load-bearing part. Reproducing a calculation by hand counts. A second model with a different training distribution counts (sometimes). A test suite written by the same agent that wrote the implementation does not count, because the validator inherits the implementation's assumptions.

**As commonly used (when it differs):** often used interchangeably with "verification" (does the output match its own spec) or "testing" (does it pass a defined suite). Pattern-library posts (the "15 Agent Patterns" foil filed in `memory/external-references.md` is a clean example) frame validation as a *stage in the loop* rather than as an external commitment. That conflation is what WHY post 1 is critiquing.

**Why noted:** central to the WHY arc. Post 1 ("The work is splitting") rests on the production-cheap / validation-not asymmetry. Posts 2 and 3 will keep leaning on it. The Witek and Geert reply threads both turn on the independence requirement.

**Where it appears:** `src/pages/writing/the-work-is-splitting.astro`, `memory/external-comments.md` (Witek and Geert threads).

---

## Augmented Engineering

**As Jeroen uses it:** engineering practice that systematically uses AI tooling while keeping engineering rigour intact, particularly on the validation side. Documented as a small set of named patterns at the AE site. Reproduce-Don't-Assess is one (driven-pendulum case: 68 equations, two LLMs found zero errors, manual reproduction caught three).

**As commonly used (when it differs):** the closest in-circulation terms are "AI-assisted coding" (too narrow, only about code generation), "agentic engineering" (implies autonomy and coordination, which is the production side), and "AI-pair programming" (one-on-one framing, does not scale to systems work). None of them name the validation problem.

**Why noted:** Jeroen's own coined frame, central to the AE site's positioning. Whenever it appears in writing on dev.jeroenveen.nl it should mean the same thing it means on the AE site. If usage drifts, fix here first.

**Where it appears:** AE site (`C:\local_dev\augmented-engineering\`), referenced in `memory/external-comments.md` (Witek thread, Reproduce-Don't-Assess case).

---

## Ground truth

**As Jeroen uses it:** an evidence source independent of the model whose output is being evaluated. Examples: physical reproduction of a calculation, domain knowledge with traceable provenance, measurement against a real system, a second model with materially different training distribution, human expert verification grounded in something checkable.

**As commonly used (when it differs):** often shorthand for "the correct answer," with the source of correctness left implicit. Geert's "Lazy prompting" post uses it correctly in the palm-oil example (he knew the answer beforehand and was checking the model against it) but the everyday-use generalisation slides into a fuzzier sense where "ground truth" effectively means "the user's expectation." Those are different things.

**Why noted:** load-bearing in the validation argument. Without independent ground truth, validation collapses into self-consistency checking, which is the failure mode WHY post 1 is naming. Useful term to nail down before it gets absorbed by looser usage.

**Where it appears:** `memory/external-comments.md` (Geert thread), implicit throughout the WHY arc.

---

## Interdependence Thesis

**As Jeroen uses it:** the claim that effective AI-augmented engineering requires three factors at once: domain expertise, validation capability, and context awareness. They combine multiplicatively, not additively. If any one approaches zero, overall competency collapses. An engineer without domain knowledge cannot evaluate AI output. An engineer without validation discipline cannot tell good output from plausible-looking wrong output. An engineer without situational awareness produces work that is technically correct but does not fit. Tool proficiency is not on the list. The capitalised label is from the broader research project these terms were coined in; in articles on this site the underlying idea travels, not the label (see writing-guide section 6).

**As commonly used (when it differs):** mainstream AI-productivity coverage tends to treat tool proficiency as the limiting factor: better prompts, better models, better workflows, and the rest follows. Multiplicative-three framings exist in academic competency literature but rarely cross over into engineering-practice writing. Coverage that fixes one factor in isolation, often validation, misses the point: domain and context are co-required, not exchangeable for more validation effort.

**Why noted:** validation alone is the term Jeroen has been writing about so far on this site. The Interdependence framing is what stops "validation" from collapsing into a workflow add-on. The entry is the house definition the drafts will reach for when a piece needs to argue that more-validation alone is not the answer, and why.

**Where it appears:** not yet in published articles. Canonical definition lives in the broader research project these terms were coined in. Closest neighbour on this site is the **Validation** entry above.

---

## Abstraction Principle

**As Jeroen uses it:** the claim that effective AI-augmented work proceeds Concept → Model → Implementation, in that order. Concept: what problem is actually being solved. Model: what components and relationships are at stake. Implementation: the specific code, calculation, or text. Skipping straight to implementation is the failure mode. AI makes that skip much more tempting because implementation is now cheap, and cheap output looks convincing whether or not the upstream thinking happened. As with **Interdependence Thesis**, the capitalised label is from the broader research project; in articles on this site the idea travels under its components, not as a label.

**As commonly used (when it differs):** "abstraction" in software circles usually means the noun: an abstraction layer, an abstract type, an interface. The Principle is not about that noun. It is a sequencing claim about where engineers should be thinking when AI is in the loop. The closest in-circulation neighbour is "problem framing before solving," which has the right spirit but does not name the cheap-implementation trap that makes the sequencing load-bearing in an AI context.

**Why noted:** this is what is upstream of validation. If implementation has already happened before the engineer has decided what the model should be, validation is checking output against a target that was never specified. A lot of "the AI just wrote it" failures are not validation failures. They are abstraction failures with validation downstream of the wrong thing. Worth a house definition so drafts can name that distinction precisely instead of folding it into "validation".

**Where it appears:** not yet in published articles. Canonical definition lives in the broader research project these terms were coined in. Connects directly to **Validation** (validates against what?) and **Interdependence Thesis** (abstraction is implicit in both context awareness and domain expertise).

---

# Field vocabulary (in circulation)

## Agent

**Standard definition:** a system where an LLM dynamically directs its own process and tool usage, deciding at runtime what to do next. Anthropic's "Building effective agents" essay draws a line between *agents* (which operate with autonomy and decide their own control flow) and *workflows* (which execute predefined paths even if they call LLMs along the way). [*Verify exact title and date before citing.*]

**Drift to watch for:** in mainstream LinkedIn / course-seller content, "agent" is used loosely for anything involving an LLM call, including pipelines that are clearly workflows. The "15 Agent Patterns" post filed in `memory/external-references.md` mixes both under a single label, which is part of why none of the patterns address verification independence. The adjective form, "agentic," tends to inflate further: vendor copy uses it for almost anything that calls a model.

**Relevance to AE frame:** the Anthropic distinction is useful when writing against agentic-flavoured material. Reserving "agent" for the genuine autonomy case and using "workflow" or "pipeline" for predefined orchestration preserves a distinction that the marketing register collapses. AE itself is not framed as "agentic engineering," since autonomy is not the load-bearing feature.

---

## Workflow

**Standard definition:** a predefined sequence of steps where LLMs may be called at specific points but the control flow is fixed. Paired with "agent" in Anthropic's framing. Most production "AI applications" are workflows, not agents.

**Drift to watch for:** marketing content tends to upsell workflows as agents because "agent" is the trendier word. The "15 Agent Patterns" post includes "Sequential Pipeline," "Parallel Fan-Out," and "MapReduce" as agent patterns, but these are workflow shapes: predefined orchestration where the LLM has no autonomy over control flow.

**Relevance to AE frame:** naming a workflow as a workflow is a small honesty move that signals fluency and avoids the inflationary register the AE voice avoids by default.

---

## Evaluator-Optimizer / Critic-Actor

**Standard definition:** multi-agent patterns where one agent generates output and another scores or critiques it, with the loop iterating until quality is met. Listed as Tier 3 patterns in the "15 Agent Patterns" post. The two terms are near-synonymous in practice; "Critic-Actor" tends to imply structured feedback, "Evaluator-Optimizer" tends to imply numeric scoring. The single-agent variant is "Reflection / Self-Critique," where one model both produces and critiques.

**Drift to watch for:** the patterns presume the evaluator or critic is independent of the actor. In production this is usually false: same team builds both, same training distribution underlies both, often the same base model with different prompts. Moving the critique into a separate prompt does not make it independent.

**Relevance to AE frame:** the cleanest single foil for the validation-independence argument. The patterns look like validation but are not, unless the evaluator is grounded outside the actor's distribution. The 15-pattern post shows this failure mode at scale across multiple tier-3 patterns.

**Where it appears:** `memory/external-references.md` (15-pattern foil entry).

---

## HITL (Human-in-the-loop)

**Standard definition:** any pattern where a human is inserted at defined checkpoints to approve, correct, or redirect the system's output. In agent-pattern taxonomies it is typically listed as one option among many, often as a fallback for high-risk decisions.

**Drift to watch for:** in mainstream framings (the "15 Agent Patterns" post is a clean example), HITL is treated as a recovery mechanism: the human catches what the agent missed. The AE frame inverts this. Calling it "HITL" already concedes that the human is in *the loop the agent runs*, rather than the agent being one component in a workflow the human governs.

**Relevance to AE frame:** useful term for matching mainstream vocabulary, but the loaded framing is worth noting. Putting a human or human-grounded evidence at the foundation of validation is a different stance from placing them as a checkpoint inside the agent's loop.

**Where it appears:** `memory/external-references.md` (15-pattern foil entry).

---

## Grounding

**Standard definition:** in everyday AI usage, "grounding" means anchoring a model's output to retrieved, verifiable sources at inference time, rather than letting it generate from training-memory alone. RAG, citation-enforced generation, and web-search-augmented answering are the common instances. The broader concept covers several distinct senses, often conflated:

- **Retrieval / factual:** anchor outputs to documents or live search at inference time. The "grounded generation" most product copy refers to.
- **Temporal:** keep outputs aligned with the current state of the world, not the training snapshot. Web-search integration is the usual implementation.
- **Symbolic / world (the symbol-grounding problem from cognitive science):** words have meaning only when connected to real-world referents. A model that knows the word "apple" but has no perceptual contact with one is ungrounded in this deeper sense.
- **Multimodal:** link language to images, audio, sensor data, so concepts connect to perceptual experience rather than only to other words.
- **Embodied / metaphorical (Lakoff and Johnson):** abstract concepts are grounded indirectly, through metaphor built on top of more concrete embodied experience. "A nation is strong" borrows from physical strength. "Argument is war" borrows from conflict. "Time is money" borrows from exchange. Abstraction sits on top of concrete grounding, not free-floating.

**Drift to watch for:** product copy and pattern-library posts use "grounded" as if all five senses were the same thing. They are not. The retrieval sense is an engineering technique against hallucination. The symbolic and embodied senses are claims about what it would take for a model to actually understand what it says. An LLM "grounded" via RAG is still not grounded in the Lakoff/Johnson sense: it has the linguistic residue of millions of human experiences baked into text, but none of the experiences. It has read millions of descriptions of nations but has never lived under one, felt belonging or exclusion, watched a border shift. The chain from embodied to social to abstract is missing, and what remains is a sophisticated map of how humans talk about the territory, without the territory itself. "Grounded model" in vendor copy almost always means only the first sense.

**Relevance to AE frame:** grounding-the-technique is upstream of validation, not a substitute for it. A well-grounded model can still produce output that follows from the retrieved sources but is wrong about the world the sources describe, or right about the world but wrong for the engineer's context. The independence requirement in **Ground truth** above is what stops grounding from collapsing into self-consistency: the source the model retrieves from and the source the validator checks against cannot sit on the same chain. The deeper senses (symbolic, embodied) are why even a well-grounded model produces outputs that sound competent and miss what a domain expert catches instantly. Worth keeping distinct so a draft can say "grounded" in the retrieval sense without inheriting the implication that the model now understands its subject.

**Where it appears:** not yet load-bearing in published articles. Connects directly to **Ground truth** (independence) and **Validation** (the activity grounding does not perform on its own).
