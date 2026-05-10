# Adding a project card

Add an object to the `projects` array in `src/pages/index.astro`:

```js
{
  title: 'Project Name',
  desc: 'One-line description with concrete numbers if possible.',
  tags: ['Tag1', 'Tag2'],
  link: 'https://example.com',
  linkLabel: 'Live',   // or 'Demo', 'Repo'
  accent: '#hex',      // unique accent color for the card top border
  img: '/screenshots/name.png',  // optional screenshot
},
```

Cards render in a responsive CSS grid on the homepage. The `accent` color is the card top border; pick something distinct from the existing cards for visual separation. The `img` field is optional; if present, the card shows a 16:9 screenshot thumbnail.

Place project screenshots at `public/screenshots/<name>.png`. Use 2x retina resolution.
