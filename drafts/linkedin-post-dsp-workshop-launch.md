# LinkedIn post — DSP Workshop launch (dsp-workshop.nl)

> **Status:** PUBLISHED 2026-08-27. Post: https://www.linkedin.com/posts/jeroen-veen-3244444_dsp-workshop-activity-7498650986190671872-ZjDt
> **Type:** short feed post (no Pulse article).
> **Audience:** old DSP colleagues and former students (author's own read, 2026-08-26). NOT the
> AI/V&V following the `/writing/` corpus was built for. This drove every choice below.
> **Hashtags** (added by edit, forgotten at post time):
> `#DSP #SignalProcessing #EmbeddedSystems #Python #EngineeringEducation`
> **Logged:** `memory/external-comments.md`, section "2026-08-27 — Publish: DSP Workshop launch".
> Kept rather than deleted: the editing history and the two cut decisions below are reusable.

---

## The post

Author's own draft (2026-08-27), with two hard details restored. See "Editing history" below for
what changed and why.

> Most DSP teaching stops at the Python or Matlab prototype. The part that actually breaks is
> what comes next: the same filter in C or VHDL, on a part with no floating-point unit, where an
> elegant biquad becomes a question about coefficient scaling and headroom.
>
> I have been putting years of DSP course material into one place, and it is now live at
> dsp-workshop.nl.
>
> Twelve chapters from sampling through filter design, dozens of standalone topics, and over a
> hundred exercises. Thirty pages put the embedded C next to the theory, from an 8-bit AVR up to
> a Cortex-M33 with an NPU, and a couple go to VHDL. Python and scipy throughout.
>
> Which DSP topic did you end up learning twice, once in theory and then again on hardware?

**Image:** none needed. `dsp-workshop.nl` now serves an og:image, so the link card carries the
generated cover automatically (`scripts/gen-social-cover.py` in the dsp-workshop repo). Check the
card in the composer before posting: LinkedIn caches previews aggressively and crops on its own
terms.

---

## Claims checked (2026-08-27)

Measured against the repo, not taken from prose.

| Claim | Status | Source |
|-------|--------|--------|
| Twelve chapters | 12 | `sh tests/verify_state.sh basics_chapters` |
| "dozens of standalone topics" | 34 | `sh tests/verify_state.sh topics` |
| "over a hundred exercises" | 115 | `sh tests/verify_state.sh exercises` |
| Thirty embedded pages | 30 | `sh tests/verify_state.sh embedded_pages` |
| AVR → Cortex-M33 + NPU | ADR-005 capability ladder | `dsp-workshop/CLAUDE.md` hard constraints |
| "a couple go to VHDL" | 3 `vhdl` blocks on 2 pages | `basics/08-smoothing/embedded.qmd` (x2, incl. a bit-accurate Python model of the VHDL entity), `basics/10-multirate/embedded.qmd` |
| "Python and scipy throughout" | stated | `dsp-workshop/README.md`: "No MATLAB required" |

The vague quantities are deliberate: "dozens" and "over a hundred" cannot go stale as the site
grows, and both understate rather than overstate. "Thirty pages" is kept hard because it is the
one number doing real work, and it only ever grows.

---

## Editing history

Three passes. The author's rewrite was better than the drafted version and is the base here.

**What the author changed, and why it was right:**
- **Added Matlab and VHDL to the hook.** Widens it from "embedded C" to the whole
  prototype-to-hardware gap, which is the actual shared experience of this audience. VHDL was
  checked before keeping it: the site really does carry HDL, so the hook is not writing a cheque
  the site cannot cash.
- **Dropped the topic list and the "two things changed" paragraph.** Both were mildly boastful
  and slowed the post down.
- **Softened the counts** to "dozens" and "over a hundred". Removes a rot vector.

**What was restored, and why:**
- **"Thirty pages" instead of "lots of pages."** Every quantity had gone soft, and "lots" reads
  as hand-waving to an engineering audience in the one place there is a hard, verified number.
- **The AVR → Cortex-M33 ladder.** It was dropped in the last pass. It is the most concrete
  "metal" detail available and the one this audience savours; without it the paragraph promises
  hardware and names none.
- **Split the run-on** that the added VHDL clause created, into a counts sentence and a hardware
  sentence.

---

## Why it is written this way

The audience is people who already know DSP and already know the author. That removes most of the
usual packaging work:

- **No explaining what DSP is, or why embedded is hard.** They lived it. Explaining would read as
  talking down to former colleagues.
- **The hook filters on shared experience, not credentials.** Anyone who has ported a filter to a
  part without an FPU recognises the biquad-scaling problem in one line; anyone who has not is
  not the audience.
- **The comment prompt asks for their memory, not their opinion.** "Which topic did you learn
  twice" is answerable in one line from experience, without visiting the site, which is what
  makes it get answered. It also invites former students to say hello, which is most of the point
  of announcing at all.

**Language.** English, matching every prior post in `memory/posted-linkedin/`. If the following
is mostly Dutch, a Dutch version is worth considering: the shared-experience hook works harder in
the reader's own language, and the courses themselves were partly Dutch.

---

## Deliberately not in this post

**The V&V / build-provenance mechanism.** Asked and decided 2026-08-27. Three reasons:

1. **It is a second theme.** The post has one job: recognition, and one question. A verification
   thread pulls toward a different register and competes with the comment prompt.
2. **It is a better article than a paragraph.** The provenance scheme — named states, a CI gate
   forcing every page to declare one — is a `/writing/` piece in the V&V arc, aimed at the
   AI/verification following, which is a *different audience* from this post's. Announce here
   now; write that separately and let it link back.
3. **The mechanism was mid-refactor when this was written.** On 2026-08-27 around 08:20, 39 files
   in the dsp-workshop repo had the provenance line stripped from all 30 `embedded.qmd` pages,
   `tests/test_embedded_provenance.py` staged for deletion, and `verification.qmd`, ADR-005,
   CLAUDE.md and MEMORY.md edited to match. Do not reference that surface publicly until it has
   settled and you can see what the page actually says.

**The trap to remember if a V&V piece is ever written:** the provenance tiers describe what a
given *page* carries as on-page evidence. They are not a record of what has been built and
measured over a career, and they read as one the moment they leave the repo. An early draft of
this post led with "zero have been built and measured on a bench", which was false about the
author and was cut for that reason. Keep those categories out of external copy.
