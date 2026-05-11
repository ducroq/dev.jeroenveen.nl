# LinkedIn cross-post record — A small GDPR-safe chatbot (ese-bot)

> **Status:** Published 2026-04-21 across all three surfaces. URLs and reception notes in `memory/external-comments.md` (section "2026-04-21 — Publish: A small GDPR-safe chatbot"). This file preserves the full text of what was posted (Pulse article body + short feed hook) for reuse as a template.
> **Provenance:** The original short-post draft at `drafts/linkedin-post-ese-bot-unpublished.md` was retired pre-publish (the live version reframed substantially around the European-alternative question). This record is reconstructed from the live URLs, supplied by Jeroen 2026-05-11.

---

## 1. LinkedIn article (long-form / Pulse)

**URL:** https://www.linkedin.com/pulse/small-gdpr-safe-chatbot-jeroen-veen-sotoe/

**Title:** A small GDPR-safe chatbot

**Author byline (as displayed on Pulse):** Jeroen Veen — Engineer-Researcher | AI/ML, Computer Vision, DSP, Embedded, Instrumentation | PhD (TU/e) | Freelance R&D

**Posted date (per Pulse):** April 22, 2026

**Canonical footer:** *Originally posted on dev.jeroenveen.nl/writing/ese-bot-eu-sovereign-rag.*

**Body:**

I wanted my students to have a better way to search their course materials than Ctrl-F. They study embedded machine learning, so the sources are lecture slides, datasheets, the usual MCU reference manuals, a few standards documents. A ChatGPT-style interface for that pile would obviously be useful.

The hesitation was simple. Every option I looked at would have sent their queries, their phrasing, their confusion, and their names to servers outside Europe. Under GDPR that is a problem. Every question a student asks about the course is personal data about how they are learning, and shipping all of it to a US cloud to get paraphrased felt like a strange thing to do on their behalf.

[Figure: ESE Bot landing screen]

So I built a small one that stays in the EU. Weaviate in the Netherlands for the vector store, Mistral in France for the model, a Hetzner box in Germany for hosting, a FastAPI service with a Vue frontend in front. It comes up with one docker compose up on a cheap VPS.

A year later, two cohorts have used it. I have noticed a few things.

Avoiding orchestration frameworks saved me. I looked at LangChain, decided I wanted a codebase I could read end-to-end in an afternoon, and called the APIs directly instead. The code is now small enough to fit in my head. When a student reports a weird answer I can trace it. When Dependabot opens a PR I can usually decide quickly. Nothing about this feels clever; it is just the absence of hidden machinery. I have since noticed that most of the projects that give me trouble are the ones where I took a framework's word for something.

What I have come to see more clearly is that GDPR compliance is a location problem, not a policy problem. If the vector store is in us-east-1 and the model is in California and the logs ship to a SaaS in Delaware, no amount of cookie-banner work changes where the data lives. The only way to get compliance cleanly is to pick components first and let that decision constrain the rest. It sounds obvious when written down. It does not look obvious given how many "GDPR-compliant" products are shipped that are neither.

I also wasted more time than I should have on embedding models. Swapping embeddings moved retrieval quality in small ways. Changing how documents were chunked moved it a lot. Sentence boundaries, heading context, leaving tables alone, not letting a chunk straddle two unrelated sections. The embedding model turned out to be the part I thought about first and should have thought about last.

The European AI picture is less bleak than I assumed a year ago. Mistral has been fine for what I need. Around it, EuroLLM now covers 35 EU languages under Apache 2.0. GPT-NL is underway with TNO and SURF. Salamandra sits at the Barcelona Supercomputing Center. Teuken is a German initiative. I am not claiming any of these replace Mistral for my workload today, and some of them are still more announcement than product. But a year ago my honest answer to "is there a European alternative?" was "not really." Today it is "yes, probably, depending on your horizon." That is not a small shift.

The questions that came in were a mix: conceptual ones, hardware-choice ones, and debugging questions where the student was stuck on a piece of code or a datasheet. The bot ended up being a patient first-line reader, which is what students often ask lecturers for and which lecturers do not always have time to be.

I am quietly trying the same pattern in other contexts where data cannot leave Europe but the users still want an assistant. If you are building in that space and want to trade notes, I will read the email.

The chatbot will stay where it is. A small server, one course, something I built for my students in evenings that ended up being useful enough to keep running.

---

## 2. Short feed post (link share)

**URL:** https://www.linkedin.com/posts/jeroen-veen-3244444_a-year-ago-my-honest-answer-to-is-there-activity-7452614482687819776-vp4V

**Body:**

> A year ago my honest answer to "is there a European alternative?" was "not really." Today it is "yes, probably, depending on your horizon."
>
> Notes from running a small GDPR-safe chatbot for my students, one year in.

**Auto-card under the hook (links to Pulse article):** A small GDPR-safe chatbot

---

## 3. Canonical home

https://dev.jeroenveen.nl/writing/ese-bot-eu-sovereign-rag/

---

## Reusable phrasings (cross-reference with `memory/external-comments.md`)

- *"A year ago my honest answer to '[X]?' was 'not really.' Today it is 'yes, probably, depending on your horizon.'"* — durable opener structure for tracking shifts in capability or availability over time. The "depending on your horizon" hedge does real work: it concedes that "yes" isn't unconditional without retreating to "no."
- *"GDPR compliance is a location problem, not a policy problem."* — the article's argument-form pivot. Single declarative sentence that names the misframing the reader has been carrying. Works as a Pulse-article landing line or as a one-line LinkedIn comment when the topic comes up in someone else's thread.
- *"A small server, one course, something I built for my students in evenings that ended up being useful enough to keep running."* — modest closing register. Earns the right to have been read by giving back rather than upselling.
