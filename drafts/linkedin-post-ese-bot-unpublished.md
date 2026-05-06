# LinkedIn post — ESE Bot (UNPUBLISHED)

*Status: drafted, not yet posted. Moved from `work-income/cv/linkedin_post_ese_bot.md` on 2026-05-06 to keep LinkedIn post drafts SSoT here.*

---

Last year I built a RAG chatbot for my students. This week, the second batch starts using it.

ese-bot lets embedded systems engineering students at HAN University query their course documents in natural language. No more digging through PDFs — ask a question, get an answer with source references.

The stack:
- Weaviate vector database (hosted in NL)
- Mistral AI (hosted in FR)
- Local embeddings — no student data leaves the EU
- FastAPI + Vue.js frontend
- GDPR-compliant logging, JWT auth

Why I built it: students were spending too much time searching and not enough time building. The first cohort last year used it heavily during their projects. This week a new batch of students gets access.

Total infrastructure cost: a small Hetzner VPS, Weaviate free tier, Mistral free tier, local embeddings. No excuses left for not deploying AI in education.

What I learned building it:
- EU AI Act compliance isn't as painful as people think, but you have to design for it from day one
- Vector search quality depends more on chunking strategy than embedding model choice
- Students will find every edge case in your system within 48 hours

The system is live at ese-bot.jeroenveen.nl

If you're thinking about deploying RAG in an educational or enterprise setting, happy to share what worked and what didn't.

#AI #RAG #EdTech #EUAIAct #LLM #Engineering
