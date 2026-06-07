export interface Article {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readTime: string;
}

export const articles: Article[] = [
  {
    slug: 'ai-review-is-plausibility-review',
    title: 'AI review measures plausibility.',
    excerpt:
      'In a 68-equation theory document, two AI reviews in assessment mode caught zero errors. A third pass with the same model family but a reproduction instruction caught three. AI review is plausibility review unless you make it not be.',
    date: '2026-06-05',
    readTime: '~4 min',
  },
  {
    slug: 'verification-is-a-workflow-problem',
    title: 'Verification is a workflow problem, not a model problem.',
    excerpt:
      'A frontier model drafted a verdict on a €5k decision. Two fresh-session reviewers caught fifteen issues with near-zero overlap. The failures lived in the drafting context, where model-level interventions cannot reach.',
    date: '2026-06-01',
    readTime: '~4 min',
  },
  {
    slug: 'the-model-is-not-the-grader',
    title: 'Most production AI grades its own output.',
    excerpt:
      'Most production AI lets the LLM grade its own output. Notes from a year of building one that does not, and the second decision that makes the first one honest.',
    date: '2026-05-19',
    readTime: '~5 min',
  },
  {
    slug: 'senior-developers-trust-ai-less',
    title: 'Senior developers trust AI less than juniors.',
    excerpt:
      'Three 2025 surveys keep finding the same pattern: more experience, less trust in AI output. The data flips the conventional take that AI is a junior-shaped problem.',
    date: '2026-05-12',
    readTime: '~5 min',
  },
  {
    slug: 'the-work-is-splitting',
    title: "The work is splitting. The conversations haven't caught up.",
    excerpt:
      'Engineering work is decomposing into producing output and validating it. Production is now cheap and fast. Validation is not. An observation from a few years of building with AI agents.',
    date: '2026-05-01',
    readTime: '~5 min',
  },
  {
    slug: 'ese-bot-eu-sovereign-rag',
    title: 'A small GDPR-safe chatbot',
    excerpt:
      'Notes from a side project that stuck around. Observations on location as architecture, why chunking beat embeddings, and how the European AI picture shifted in a year.',
    date: '2026-04-21',
    readTime: '~5 min',
  },
];

export function formatDate(iso: string): string {
  const d = new Date(iso);
  return d.toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });
}
