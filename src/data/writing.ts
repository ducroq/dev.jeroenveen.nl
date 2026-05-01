export interface Article {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readTime: string;
}

export const articles: Article[] = [
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
