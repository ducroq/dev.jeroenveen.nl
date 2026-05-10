# Verification record — *A small GDPR-safe chatbot*

**Article**: `src/pages/writing/ese-bot-eu-sovereign-rag.astro` (status: published 2026-04-21)
**Article slug**: `ese-bot-eu-sovereign-rag`
**LinkedIn surfaces**: short post, Pulse article, canonical home — see `memory/external-comments.md` 2026-04-21 entry
**Last verified (retroactive)**: 2026-05-10
**Method**: Anti-hallucination checklist (Step 0 + Steps 4–6) per [agent-ready-papers framework](file:///C:/local_dev/agent-ready-papers/templates/anti-hallucination.md).
**Ground truth**: For European-AI claims, primary-source verification via WebFetch on each project's canonical page. The HAN Digital Engineers research project's CLAIM-REGISTRY does not cover European AI alternatives (different research focus), so registry chain not applicable here.

This record is a **retroactive verification**. The article is published. The goal is to confirm load-bearing factual claims survive the same checklist applied to draft articles, and flag any open issues for future revision.

---

## Claim 1 — Infrastructure stack and locations

**Article wording (paragraph 4)**:
> Weaviate in the Netherlands for the vector store, Mistral in France for the model, a Hetzner box in Germany for hosting, a FastAPI service with a Vue frontend in front.

| Component | Location claim | Verification |
|---|---|---|
| Weaviate | Netherlands | ✓ Weaviate B.V. is headquartered in Amsterdam (well-known industry fact; SaaS hosted in EU regions) |
| Mistral AI | France | ✓ Mistral AI is a Paris-based AI company (well-known industry fact) |
| Hetzner | Germany | ✓ Hetzner Online GmbH is a German hosting company headquartered in Gunzenhausen, Bavaria (well-known industry fact) |
| FastAPI / Vue | (own implementation choice) | ✓ Own work, no external citation needed |

**Confidence tier**: **ESTABLISHED**. These are well-known facts about the named companies. No verification gate needed.

---

## Claim 2 — EuroLLM "covers 35 EU languages under Apache 2.0"

**Article wording (paragraph 9)**:
> EuroLLM now covers 35 EU languages under Apache 2.0.

| Check | Result |
|---|---|
| Source | EuroLLM model family, UTTER project consortium |
| Primary URL | https://huggingface.co/utter-project/EuroLLM-9B-Instruct |
| Project URL | https://he-utter.eu/ |
| Step 0 | ✓ Project and models confirmed to exist |
| Step 4 (scope match) | ✓ EuroLLM is a multilingual LLM family targeting European languages |
| Step 5 (exact location) | Model card "Language(s) (NLP)" field; "License" field |
| Step 6 (read section) | ✓ Verbatim from model card: *"Language(s) (NLP): Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian."* (35 languages total) — and *"License: apache-2.0"* |
| Confidence tier | **PARTIALLY CONFIRMED with factual caveat** |

**Caveat** (the article slightly overstates EU-specificity):

The article says *"35 EU languages"*. The model card lists 35 languages, of which:
- **24 are EU official languages**: Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish (= the full set of 24 EU official languages)
- **11 are non-EU**: Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, Ukrainian (some are regional EU languages like Catalan, Galician; most are global pivot languages)

The number 35 is accurate. The Apache 2.0 license is accurate. The framing *"35 EU languages"* is not — only 24 of the 35 are EU official languages.

**Recommended (if the article is ever revised)**: rewrite to one of:
- *"EuroLLM now covers all 24 EU official languages, plus 11 others, under Apache 2.0"*
- *"EuroLLM now covers 35 languages including the full EU official set, under Apache 2.0"*

Both keep the article's point (EuroLLM is a credible European-led alternative covering the EU language space) without the factual stretch.

**Bonus**: EuroLLM is funded by the European Union and developed by a consortium including Unbabel, Instituto Superior Técnico, Instituto de Telecomunicações, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Université.

---

## Claim 3 — "GPT-NL is underway with TNO and SURF"

**Article wording (paragraph 9)**:
> GPT-NL is underway with TNO and SURF.

| Check | Result |
|---|---|
| Source | GPT-NL project |
| Primary URL | https://gpt-nl.nl/ |
| Step 6 (read section) | ✓ Verbatim from project homepage: *"GPT-NL is een samenwerking van non-profitorganisaties TNO, NFI en SURF."* (GPT-NL is a collaboration of non-profit organisations TNO, NFI and SURF.) |
| Confidence tier | **CONFIRMED with minor omission** |

**Note**: The article names two of the three partners (TNO and SURF). The third partner is **NFI** (Netherlands Forensic Institute). This is an omission, not an error — the article's claim is true as written but incomplete. Status as of Q1 2026 per the homepage: *"van ontwikkeling naar gebruik in de praktijk"* — moved from development to practical use, working with launching customers.

**Recommended (if the article is ever revised)**: extend to *"GPT-NL is underway with TNO, NFI, and SURF"* or just *"GPT-NL is a Dutch initiative now moving from development to practical use"* (the partners list isn't essential).

---

## Claim 4 — "Salamandra sits at the Barcelona Supercomputing Center"

**Article wording (paragraph 9)**:
> Salamandra sits at the Barcelona Supercomputing Center.

| Check | Result |
|---|---|
| Source | Salamandra model family, BSC-LT |
| Primary URL | https://huggingface.co/BSC-LT |
| Step 6 (read section) | ✓ Verbatim affiliation: *"Language Technologies Laboratory @ Barcelona Supercomputing Center"*. Models include `BSC-LT/salamandra-7b-instruct-tools-16k` and `BSC-LT/salamandraTA-7b-instruct`. Org type: non-profit. Official site: https://www.bsc.es/discover-bsc/organisation/research-structure/language-technologies-laboratory |
| Confidence tier | **ESTABLISHED** |
| Article language | "sits at the Barcelona Supercomputing Center" — accurate |

---

## Claim 5 — "Teuken is a German initiative"

**Article wording (paragraph 9)**:
> Teuken is a German initiative.

| Check | Result |
|---|---|
| Source | Teuken-7B, OpenGPT-X project |
| Primary references | Fraunhofer IAIS / IIS press releases; Deutsche Telekom commercialisation announcement |
| Step 6 (read section) | ✓ Confirmed: Teuken-7B is from the OpenGPT-X research project led by Fraunhofer IAIS and Fraunhofer IIS, funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK, ~€14M), trained on Forschungszentrum Jülich's JUWELS supercomputer. Consortium: Fraunhofer IAIS, Fraunhofer IIS, Forschungszentrum Jülich, TU Dresden, DFKI, IONOS, Aleph Alpha, ControlExpert, WDR, KI Bundesverband. |
| Confidence tier | **ESTABLISHED** |
| Article language | "a German initiative" — accurate |

**Bonus context worth knowing for related articles**: Teuken-7B is trained in all 24 EU official languages, available under Apache 2.0 for commercial use (Teuken-7B-instruct-commercial-v0.4), and is now commercialised by Deutsche Telekom T-Systems. This is a useful counterpoint for any future article on European AI sovereignty.

---

## Claim 6 — *"Mistral has been fine for what I need"*

**Article wording (paragraph 9)**:
> Mistral has been fine for what I need.

This is a personal-experience claim, not a citation-load-bearing one. Own work. **Confidence tier: own observation, no verification gate.**

---

## Claim 7 — Architectural / personal observations

The article makes several observations grounded in personal practice:
- *"Avoiding orchestration frameworks saved me. I looked at LangChain, decided I wanted a codebase I could read end-to-end in an afternoon, and called the APIs directly instead."* — own work
- *"GDPR compliance is a location problem, not a policy problem."* — own framing, supported by the article's own argument
- *"Swapping embeddings moved retrieval quality in small ways. Changing how documents were chunked moved it a lot."* — own observation; convergent with industry consensus on RAG quality drivers but not citation-anchored
- *"comes up with one `docker compose up`"* — own infrastructure claim, verifiable in the public repo at https://github.com/ducroq/ese_bot

These are own work. **Confidence tier: own observation, no verification gate. Standard for personal-essay form.**

---

## Sources block (recommended if article is ever revised)

The article currently does not have inline links or a Sources block (it predates the convention adopted 2026-05-10). If revised, the recommended block:

```
Sources

EuroLLM (UTTER project consortium). EuroLLM-9B-Instruct model card.
  https://huggingface.co/utter-project/EuroLLM-9B-Instruct
GPT-NL. https://gpt-nl.nl/
Salamandra (Language Technologies Laboratory, Barcelona Supercomputing Center).
  https://huggingface.co/BSC-LT
Teuken-7B (OpenGPT-X / Fraunhofer IAIS).
  https://www.iais.fraunhofer.de/en/industries_and_cross-sector_solutions/cross-sector_solutions/generative-ai/opengpt-x.html
```

---

## Outstanding tasks

1. ~~EuroLLM "35 EU languages" → "35 languages including the full EU official set"~~ ✅ Applied 2026-05-10. Article now states the language coverage accurately.
2. ~~GPT-NL "with TNO and SURF" → "with TNO, NFI, and SURF"~~ ✅ Applied 2026-05-10. Partner list now complete.
3. ~~Add inline links + Sources block~~ ✅ Applied 2026-05-10. Four inline links in the European-AI paragraph (EuroLLM, GPT-NL, Salamandra, Teuken) + Sources block at the end of the article body.

Status: **VERIFIED retroactively. All five external-fact claims survive the checklist. Calibrations and references added. Article re-published 2026-05-10.**
