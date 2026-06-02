# The V-Model Is the Right Shape. The Reviewer Is the Mechanism.

*Status: draft, 2026-05-29. Triggered by Sebastian Völkl's (Dalus) LinkedIn post on the V-model framing. Audience: senior engineers and AI leads at EU manufacturers / engineering organisations. Tone: yes-and, not foil. Dalus is a potential conversation partner, not a competitor.*

*Target length: 900–1,100 words. Currently ~950.*

*Pre-publish: needs `docs/verification/whats-inside-the-loop.md` for the Seifert et al. 2025 Fraunhofer IESE claims (already drafted in `augmented-engineering/PROPOSITION-vmodel-reposition.md` but never primary-source verified). Also needs the cross-model review pass. Quasar product link to be added.*

---

A LinkedIn post by Sebastian Völkl, the CEO of [Dalus](https://www.linkedin.com/posts/sebastian-voelkl_saw-this-on-x-and-had-to-repost-the-skill-activity-7466114384071913472-lLEK), made the rounds this week. The argument runs like this. The skill in this era of AI software engineering is describing what you want clearly enough that something can build it without you babysitting. For systems engineers, he says, that's just Tuesday. Requirements first, design to them, verify against them. If a model can regenerate the implementation from the spec, the spec is the valuable part. The code is throwaway. *"Funny that the most modern way to use AI turns out to be a 40-year-old NASA diagram."*

I think he's right about the diagram. The V-model puts implementation at the bottom of the V and the artifacts that determine whether the work is correct, the requirements and the verification criteria, at the top. If generators can regenerate the bottom, leverage moves to the top. That is the right shape for AI-assisted engineering work, and it is a shape most software organisations have never really had to operate inside. But the shape is the easy part. The mechanism is where the next year of work lies.

The V-model tells you *where* verification happens. It does not tell you what makes verification work when a fluent generator can produce a plausible-looking spec, a plausible-looking design, and a plausible-looking test suite, none of which the reviewer may be competent to challenge. "Requirements first" presumes the requirements author can tell a good requirement from a bad one. "Verify against them" presumes the verifier can tell a passing system from one that merely looks like it passes.

That presumption is the load-bearing piece. And there is now evidence about whether it holds.

Researchers at Fraunhofer IESE, the same institute that builds the Quasar requirements review tool, published a study in 2025 finding that LLMs "substantially trail human reviewers" at requirements inspection, that results "don't vary across prompting techniques," and that "findings rarely match expert solutions" (Seifert et al., 2025). Their own blog asks the question this evidence raises directly: "AI writes code in seconds, but who guarantees it solves the right problem?" Their answer is "human-in-the-loop."

That's a design pattern. It tells you where the checkpoint is. It does not tell you what happens inside it.

What happens inside it is the whole question. If the human in the loop accepts plausible AI output without checking, the loop is empty: the checkpoint adds latency and nothing else. If the human refuses the tool entirely, the loop does not exist. Only when the human uses the tool while keeping independent judgment does the checkpoint actually do anything. Independent judgment, in this context, is not a personality trait. It is a working combination of domain knowledge, the skill of validating output you did not produce yourself, and an awareness of what you do not know.

A reasonable objection at this point: most engineers will never be expert reviewers, and probably should not have to be. If the realistic ceiling for a working engineer is a fraction of what a Fraunhofer-style expert can do at requirements inspection, training to that level is not where the investment goes. Fair. What this implies is not "develop expert reviewers" but "calibrate the tool against the team's actual competency floor, and shore up the floor where the calibration tells you that you must." That is harder than the human-in-the-loop pattern suggests, because it requires measuring the floor first and then designing the loop to clear it. It is also the part that the current category of AI requirements tools does not help with.

There are consequences worth naming for anyone building or deploying AI in an engineering process.

The spec becomes the bottleneck differently than expected. Völkl is right that the spec moves to the top of the value stack. What moves with it is the requirement to audit specs at a level most engineering organisations do not currently invest in. A specification that no one in the room can rigorously check is no better than throwaway code. It just feels more durable.

Tooling for the top of the V cannot stop at "we run an LLM over your requirements." Every product in this space pitches the same flow: submit document, receive feedback. The Fraunhofer evidence says that flow underperforms expert review at exactly the moments it matters. The interesting tooling question is not "can the LLM review the requirement." It is "can the tool develop the reviewer."

The competency the team brings is the differentiator. Two organisations adopt the same AI requirements tool. In one, engineers learn to read the tool's output critically, catch what it misses, and use it as a forcing function for their own judgment. In the other, the tool's output becomes the answer, and the engineers stop noticing what is not on the list. Same tool, different outcomes. The difference is not in the tool.

What this looks like when you actually try to build inside the constraint is the part most of these arguments skip.

I have been building one concrete instance of it for a year. [vmodel.eu](https://vmodel.eu) is a self-hosted requirements review system for engineering students. The constraints are tighter than a typical industrial deployment (no student data leaves the GPU, every prompt change has to clear a calibration gate), but the underlying problem is the same one. Six agents on one GPU. Deterministic scoring on top of LLM findings (no LLM scoring; the calibration drifts too much). An 80% within-1 agreement gate against an expert baseline that every prompt change has to clear before it ships. The architecture took the shape it did because the same problem Völkl names at the strategic level, the spec becoming the load-bearing artifact, applies inside the tool too. If the tool's output is plausible but wrong, the student learns to satisfy the tool rather than understand the criteria, and a year later you have trained a generation of engineers who pass automated review and fail real reviews.

The fix turned out to be specific. Separate what is deterministic from what is qualitative from what is calibrated. Put each in the component built for it. Treat the tool's own analysis as something the reviewer should be able to challenge, not just accept. That moves the work from "running the tool" to "developing the reviewer." It is slower. It is also the only direction the evidence supports.

So the V-model framing lands at the right place. The 40-year-old diagram is the right diagram. The question it does not answer is what the reviewers at the top of the V actually need to bring, and what discipline calibrates a tool to the floor they bring. That is the work.

If you are building tooling in this space, or running a team being asked to adopt it, I would be interested in trading notes.

---

## Drafting notes (not for publish)

**Tone pivot:** original draft (in `augmented-engineering/PROPOSITION-vmodel-reposition.md`) framed Dalus as a competitor and used "he's right but" structure. This version is "yes-and": Dalus names the shape, the mechanism is the open question, vmodel.eu is one worked example of working on the mechanism. The closing CTA is genuine, not pitched. If Völkl reads this, the implied next move is a conversation, not a competitive comparison.

**Cross-model review pass:** done 2026-05-29 via a fresh agent with no project context, using agent-ready-papers `templates/review-prompt.md` (Variant B). All ten writing-guide style rules cleared. Tone check confirmed the piece reads as invitation to Völkl, not competitive critique. Five revisions applied below; one open item escalated to verification queue.

**Revisions applied from cross-model review:**
1. Moved the thesis line ("The shape is the easy part. The mechanism is where the next year of work lies.") from its own paragraph 3 into the end of paragraph 2, so the concession and pivot land in the same paragraph and a senior-engineer skimmer hits the original move sooner.
2. Inserted a counter-argument paragraph after the taxonomy paragraph: names the "most engineers will never be expert reviewers" objection and answers it by reframing the work as "calibrate against the floor you have, shore up the floor where calibration tells you that you must." Sets up the vmodel.eu paragraph as the worked answer rather than just an example.
3. Added a bridge sentence at the end of the "competency the team brings" paragraph ("What this looks like when you actually try to build inside the constraint is the part most of these arguments skip.") so the move to first person feels earned, not abrupt.
4. Rewrote the closing line to name reviewer competency + calibration specifically rather than the generic "what makes the people at the top of the V good at the thing the diagram says they should do."
5. Added a cross-applicability sentence in the vmodel.eu paragraph noting the constraints differ from industrial deployment but the underlying calibration problem is the same.

**Verification queue:**
- Seifert et al. 2025 Fraunhofer IESE quotes: need primary-source check before publish. Three quoted phrases ("substantially trail human reviewers", "don't vary across prompting techniques", "findings rarely match expert solutions") plus the blog quote ("AI writes code in seconds, but who guarantees it solves the right problem?"). Currently pulled forward from PROPOSITION-vmodel-reposition.md without a verification trail. The reviewer flagged this as the highest-risk passage in the article: if even one quote is paraphrased or unverifiable, the "found" / "the Fraunhofer evidence says" language has to downshift from ESTABLISHED to SUPPORTED. Article structure survives the downshift; rhetorical force takes a small hit.
- Quasar tool: confirm still active, add inline link on first mention.
- vmodel.eu numbers ("80% within-1 agreement gate", "six agents on one GPU"): aggregate-level only per `vmodel.eu/CLAUDE.md` privacy constraint. Confirm 80% is the calibration gate, not the 93.8% held-out result. (Case-study seed quotes both; the gate is the discipline being named here.)

**Open questions for Jeroen:**
- The closing CTA reads as "trade notes" rather than "hire me." Right register for this audience, or should it point at something more specific (the vmodel.eu site, an email, a calendar link)?
- Should the article mention the Digital Engineer research framing (D×V×C) at all? Currently the framework label is stripped per writing-guide rule against capitalised framework names, and the underlying idea is described in plain language. That keeps the piece readable cold but loses the research anchor. Alternative: one footnote-style mention near the end.
- Slug: `whats-inside-the-loop.md` (current) vs. `shape-and-mechanism.md` (matches the title more directly). Slight preference for the latter on second read.
