import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// GitHub Pages serves this repository under /Commercial-print-website.
// Keep the base fixed so local builds and GitHub Pages generate identical asset URLs.
const base = '/Commercial-print-website/';

export default defineConfig({
  site: 'https://steenkamnoelle638-source.github.io',
  base,
  integrations: [sitemap()],
});
