export interface Article {
  slug: string;
  title: string;
  excerpt: string;
  date: string;
  readTime: string;
}

export const articles: Article[] = [
  {
    slug: 'ese-bot-eu-sovereign-rag',
    title: 'Building an EU-sovereign AI chatbot for my students',
    excerpt:
      'Lessons from roughly 1,400 real student questions across one semester: GDPR as architecture, a minimal stack, why chunking beats embeddings, and the state of the European AI ecosystem.',
    date: '2026-04-21',
    readTime: '~8 min',
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
