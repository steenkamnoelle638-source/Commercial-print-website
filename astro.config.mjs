import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// GitHub Pages serves this repository under /Commercial-print-website.
// Local development and Netlify use the domain root.
const base = process.env.GITHUB_ACTIONS === 'true' ? '/Commercial-print-website' : '/';

export default defineConfig({
  site: 'https://yourdomain.com',
  base,
  integrations: [sitemap()],
});
