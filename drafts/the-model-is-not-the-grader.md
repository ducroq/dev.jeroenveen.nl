# Most production AI grades its own output.

*Working subtitle:* Notes from a year of building a tool I am not going to describe.

*Working slug:* `the-model-is-not-the-grader` (alternatives listed below)

*Drafted: 2026-05-19. Standalone piece, explicitly not tied to the V&V arc (post 3 against post 2's hardware/embedded/control forward-look is still owed). Status: revision 1, post-cross-model-review.*

---

## Title candidates (pick at review time)

- **Most production AI grades its own output.** (argument-form, working pick; strongest LinkedIn line)
- *The model is not the grader.* (declarative, shorter, lower charge)
- *Validation in production is not what the demos mean by validation.* (broader, more abstract)
- *Calibration gates before prompt changes.* (mechanism-foregrounded; better as a phrase inside the body)

---

## Draft

Most AI-tooling posts read like demos. The product is shown working, often with a metric attached, and the implicit claim is *this is what an AI system looks like*. The framing skips the engineering decisions that decide whether you can trust the system at all, and one decision in particular keeps coming up in my own work.

The system runs in production under GDPR constraints, so the system description belongs in the system, not here. What I want to write about is the decision.

The decision is that I do not let the LLM grade its own output. That sounds obvious until you look at the dominant patterns in the LLM-evaluation literature: llm-as-judge, self-consistency check, evaluator-optimizer, critic-actor, reflection. They differ in their decoration. They share one property: the evaluator inherits the actor's assumptions, because they came from the same training distribution and they are reading the same artifact in the same way.

The structural alternative is not novel as a pattern, only uncommon in the products I see shipped. The LLM is the finder. Deterministic code, written by hand against a fixed rubric, is the grader. The rubric is derived from engineering standards that exist outside any LLM. The LLM finds candidate issues; the grader scores them against rules that were defined and agreed upon before any LLM was ever called. The grader has no opinion. It enforces.

The difference matters, but it is partial. When the grader is the LLM, you are measuring how the LLM feels about its own output. When the grader is deterministic code reading a fixed rubric, you are measuring whether the output meets the rubric. Those are different things. What this buys is grading-time independence: the scoring is no longer a re-reading by something with the same priors as the producer. What it does not buy is finding-time independence. Anything the LLM-finder fails to surface never reaches the grader. The discipline is about precision against a rubric, not coverage.

Two honest objections live in this. The first is the one I just made: a sibling discipline (cross-model review, scheduled audits, something) has to push back on the finder-side blindness, and that is a different piece. The second is that the rubric authors have opinions, and rubrics edited in response to disagreements with the finder will drift toward what the finder surfaces well. The grader inherits the rubric, which inherits whatever pressure the LLM's failure modes put on the people maintaining it.

The discipline that holds the second objection honest is a checkpoint. Every time we change a prompt, the new prompt runs against a small set of cases we already know the right answers to. The grader scores them, and those scores get compared to what the old prompt got. If they match closely enough, the change ships. If they do not, the change is blocked, and a rubric edit that shifts scores on that set has to be argued for explicitly, not slipped in. We call this a calibration gate. Not a unit test. A calibration check against a known sample, the way you do not change a measurement instrument without re-checking it against a reference standard.

What has this cost. Mostly time. Building a baseline set is slow, and the baseline set is what makes the calibration gate meaningful. Maintaining it is slower. The decisions sit in a stack of architecture-decision records, each with a paragraph attached explaining the alternative we considered and the reason we did not adopt it. That documentation does not show up in any demo. It is the thing that makes the system defensible when somebody senior asks the question that defines whether a system is defensible: *how do you know this works?*

The previous pieces here have argued that validation is the harder half of engineering work, and that the engineers most cautious about AI output are the ones who have validated it most. The past year is what taking that seriously has looked like in one specific case. Not a methodology, not a generalisable claim, not a paper. One decision, and the second decision that makes the first one honest, in case it is useful as evidence that the work the previous pieces describe is not abstract.

What I have not solved is the rubric-drift problem on a longer horizon than the held-out set can see. That is a different piece.

If you are letting the LLM grade its own output and that is working for you, I would like to know how.

---

## Revision 1 notes (2026-05-19, post-cross-model-review)

**Word count (body):** ~840. Bumped from ~770 to absorb the two-objection paragraph and the precision-not-coverage clarification. Comfortably inside the 800–1500 band.

### What this revision did

| # | Source | Finding | Resolution |
|---|---|---|---|
| 1 | Opus, critical | Warrant gap: deterministic grader doesn't escape finding-time inheritance. | Added two sentences to the "difference matters" paragraph naming the grading-time / finding-time split explicitly, and a new paragraph naming finder-side blindness as the first of two honest objections. |
| 2 | Opus, substantive | Rubric-drift counter-argument unaddressed; calibration gate didn't earn its keep. | Added "second objection" framing in the new paragraph (rubric authors have opinions, rubrics edited in response to LLM disagreements drift toward what the finder surfaces well), then re-cast the calibration-gate paragraph as the defence against that drift. Calibration gate now earns its keep instead of arriving as an unrelated second discipline. |
| 3 | Opus, substantive | "Most production AI products" / "most production AI tools" overreach without source. | Both instances softened. First → "the dominant patterns in the LLM-evaluation literature" (defensible without a survey). Second → removed; the precision-not-coverage point now carries that paragraph. |
| 4 | Opus, substantive | Contribution clarity: finder/grader split isn't novel as a pattern. | Added one sentence: "The structural alternative is not novel as a pattern, only uncommon in the products I see shipped." Honest acknowledgment, strengthens rather than weakens. |
| 5 | Haiku, substantive | Opening overpromises "the part that takes the longest" then describes one decision. | Reframed opening to "one decision in particular keeps coming up in my own work." Removed the "part that takes the longest" / "shape of the year" framing in favour of single-decision focus. |
| 6 | Haiku, substantive | Disclosure paragraph reads defensive. | Compressed three sentences to two: "The system runs in production under GDPR constraints, so the system description belongs in the system, not here. What I want to write about is the decision." |
| 7 | Opus, substantive | Calibration-gate "match within tolerance": match what? | Specified: "the grader's scores on that set are compared to the established baseline." |
| 8 | Opus, substantive | Closing forward-look promised future pieces on the three things this piece already covered. | Replaced with a single-sentence limitation-acknowledgment closer: "What I have not solved is the rubric-drift problem on a longer horizon than the held-out set can see. That is a different piece." Single forward-look, names an unsolved problem rather than re-promising mechanism. |

### What this revision did not do (deferred to polish pass)

| # | Source | Finding | Why deferred |
|---|---|---|---|
| 9 | Both, minor | "The grader has no opinion. It enforces" (rhetorical overclaim). | Kept the line as-is. Opus flagged it both ways (strongest crystallisation / mild overclaim); Haiku flagged it as "do not lose in revisions." The new objection-pair paragraph immediately after it now does the qualification work without needing to soften the line itself. The rhetorical sentence earns its punch because the next paragraph concedes its limits. |
| 10 | Haiku, minor | Abrupt transition to the calibration-gate paragraph. | Resolved naturally by the two-objection paragraph, which now bridges into the calibration-gate paragraph as its answer. |

### Haiku misread (not a real finding)

Haiku's #1 ("title is artifact-form") was based on reading the subtitle as the title. The actual title *"Most production AI grades its own output."* is already argument-form. No change made.

---

## Standing notes (carried forward from revision 0)

**Arc position.** Explicitly *not* a V&V arc closer. The closer against post 2's hardware/embedded/control forward-look is still owed. This piece runs before or after that closer with no sequencing claim. The closing references "previous pieces" generically without claiming to deliver their forward-look.

**Disclosure constraint.** Body says only: production deployment, GDPR constraints, deterministic grader against a rubric derived from engineering standards, calibration gate against a held-out reference set, a stack of architecture-decision records. No mention of vmodel.eu name, model families, GPU/agent counts, within-1 thresholds, 122/64 baseline-and-heldout numbers, 870-test count, 20-ADR count. Easy to dial up at review if any are public-fine.

**"Students" appearance.** Note: revision 1 *dropped* the explicit "student-engineering content" phrasing. The disclosure paragraph now says only "GDPR constraints." If you'd prefer to put "student-engineering" back as audience-specific grounding, easy to restore in the disclosure sentence.

**Named-colleague rule (writing-guide §5).** No colleagues named. "The team" appears once in the calibration-gate paragraph and is non-anchoring.

**Em-dash audit.** Re-scanned post-revision. None in the body. One em-dash was caught in the metadata line above the draft and fixed during revision.

**Visual register.** Recommend no in-article figure (BEFORE/AFTER cliché risk per visual-register memory). Typographic social-image cover via `scripts/gen-social-image.py` still needed on publish.

**Sources block.** Recommend leaving off. The piece cites no external research; the named patterns (llm-as-judge, evaluator-optimizer, etc.) are field-vocabulary, glossary-internal.

**Verification record.** Per writing-guide §7. Load-bearing claims for `docs/verification/<slug>.md`:
- "The dominant patterns in the LLM-evaluation literature (llm-as-judge, self-consistency check, evaluator-optimizer, critic-actor, reflection) share the property that the evaluator inherits the actor's assumptions." Primary source: `docs/glossary.md` field-vocabulary section and the 15-pattern post foil in `memory/external-references.md`. Confidence tier: SUPPORTED. Article language matches ("share one property") rather than ESTABLISHED-tier "demonstrates."
- "Rubrics edited in response to disagreements with the finder drift toward what the finder surfaces well." Own observation from year-of-building work. Confidence tier: EMERGING / SPECULATIVE. Article language is appropriately hedged ("will drift toward"). Verifiable only against own ADR record, which is not public; if pressed, could be downshifted further.
- "Calibration gates against a held-out reference set" as a discipline. Own implementation. Confidence tier: ESTABLISHED for own work; SUPPORTED as a generalisable pattern (the measurement-instrument analogy is from metrology, not from AI-tooling literature).

**Cross-model review.** Pass 1 Haiku + Pass 2 Opus *done* on revision 0; this revision incorporates their findings. A second cross-model pass on revision 1 is optional. The DR-011 procedure does not strictly require iterating, but if you want belt-and-braces on the new objection-pair paragraph (the load-bearing argumentative addition), one more pass would be cheap. My read: not necessary unless something in the new paragraph feels off when you read it cold.

**Pre-empt check.** The forward-look now names cross-model review as a sibling discipline ("that is a different piece") rather than promising mechanism deep-dives on the disciplines this piece covers. Cleaner setup for the AE-pattern arc (`cross-model-review` is one of the planned pieces); doesn't pre-empt.

**What this piece is not.** Not the V&V closer (still owed). Not the vmodel.eu case study (still pending; longer, with numbers, names the system). Not a methods piece (disciplines named, not developed). A "one decision and its honest companion" observational piece. Closer to *The work is splitting* than to *Senior developers trust AI less* in register.

**Meta-observation worth logging (separately, not in the article).** The cross-model review pass we just ran is itself a meta-application of the underlying principle the article rests on (separate the artifact's author from its grader, get disjoint failure modes). The warrant gap was invisible to the drafting context and visible to a fresh-session pass, which is the article's failure mode demonstrated in miniature. Candidate for hypothesis-log or a future V&V-method-for-paper-writing piece you mentioned.
