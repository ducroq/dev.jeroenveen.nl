# LinkedIn draft (general / standalone) — You can't prompt your way out of hallucination

> **Status:** Unpublished draft. General standalone post, not tied to a `/writing/` article. SSoT here per CLAUDE.md. Drop `-unpublished` or log in `memory/external-comments.md` once posted.
> **Origin:** A Dutch colleague forwarded the viral "paste this 7-rule prompt into settings and Claude stops lying" post (Harish Kumar, LinkedIn) and asked whether there is a better prompt. This is the reply as a standalone post. Sibling to the parked essay `drafts/the-spell-feeling-is-the-bug.md` (the spell-feeling is the tell that validation got skipped) and to `verification-is-a-workflow-problem` / `the-model-is-not-the-grader`. Same spine: a prompt sets a prior, it cannot check anything.
> **Form:** short-to-medium feed post. No Pulse long-form planned unless it lands.
> **Verification:** argument-only, no load-bearing statistics. Recorded-skip is the honest call (writing-guide 7). If the METR 19%/20% figure gets added, it needs a verification record first.

---

## Title / hook candidates (argument-form)

- **You can't prompt your way out of hallucination.** (pick: front-loads the claim, matches the arc's declarative pattern)
- A prompt is a prior, not a gate.
- Don't ask a model to be honest. Ask it to show its work.

---

## Post body (as drafted)

A prompt doing the rounds this week promises that if you paste seven rules into your settings, the AI "stops lying to you." I got sent it twice. The instinct behind it is right. The mechanism is not.

Here is the problem the viral prompt cannot solve. A model does not know when it is wrong. The confident mistakes, the invented citation, the function that does not exist, the plausible wrong number, arrive feeling exactly as certain from the inside as the correct answers do. So "flag anything you are unsure about" only catches the cases where the model already felt some doubt. Those are the easy ones. The ones that cost you feel certain, so they sail straight through the filter.

The second problem is quieter. Tell a model to caveat everything and it caveats everything, including what it actually knows. Uniform hedging carries no signal. You learn to skip past "I am not certain, but" the same way you skip a cookie banner, and now the warning means nothing on the one occasion it should have stopped you.

A prompt sets a prior. It nudges tone. It cannot check a single fact, because the thing doing the checking is the same fallible process that produced the claim.

So if you want a better prompt, the move is not a longer list of promises. It is to stop asking the model to be honest and start asking it to show its work: something you can verify without trusting it. A source you can open. A number you can trace. A function you can look up. Honesty you can check beats honesty you have to take on faith.

The shorter prompt I actually use, roughly:

> When you answer, show your work instead of just asserting it.
> - Separate what you know from what you are inferring. Do not spread uncertainty evenly. Flag the specific claims you are actually unsure of and state the confident ones plainly. Blanket hedging is noise.
> - For any factual claim I could check, give me the source I can check it against: a title, an author, a DOI, a link. If you cannot name a real one, say "no verified source" instead of inventing a plausible one.
> - For numbers, dates, and quotes: give the value and where it came from. If you are reconstructing from memory, say so and point me at the primary source.
> - For code: if you are not sure a function or API exists, tell me which doc to check rather than presenting it as fact.
> - If a tool is available to verify something (search, a file, a database), prefer checking over recalling.
> - If the question is missing something you need, ask before answering. Do not fill the gap with an assumption.

It is better. It is still not a guarantee. The real fix for hallucination was never a paragraph in your settings, it is grounding the model in sources it can cite and putting a checking step outside the model, where the model's confidence has no vote. The prompt is the seatbelt. It is not the brakes.

If a machine could reliably tell you when it was guessing, we would have solved the hard part already.

What is the last confident answer an AI gave you that turned out to be wrong, and what would have caught it?

#AI #AugmentedEngineering #LLM

---

## Notes for next time

- **Hook test:** first ~120 chars have to land the "instinct right, mechanism wrong" turn or the post reads as anti-AI. It is not anti-AI, it is anti-placebo. Watch the comment tone.
- **Overlap watch:** shares a spine with `the-spell-feeling-is-the-bug`. This is the concrete, prompt-shaped cousin; that essay is the phenomenology. Do not let this post consume the essay's move. If both ship, this one links to the essay, not the reverse.
- **The forwarded prompt is the payload.** The colleague asked for a better prompt; the post's value is that it hands one over while explaining why the genre it comes from is oversold. Keep the prompt block intact if trimming for length.
- **CTA:** one question, genuine. If replies turn into "so AI is useless," redirect to the seatbelt/brakes line, that is the intended read.
- **Em-dash check:** none in body. Verify before posting.
