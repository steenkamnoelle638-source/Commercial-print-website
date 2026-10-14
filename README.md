# Your Print Partner — Astro website starter

Responsive, SEO-oriented commercial printing website with:
- Homepage, on-page product/service keyword search, and nine dedicated product landing pages.
- South Africa landing page at `/za/`.
- Specification checklist and quote enquiry form prepared for Netlify Forms.
- Mobile navigation, floating WhatsApp CTA, semantic HTML, metadata, canonical/hreflang tags, robots.txt and sitemap generation via Astro.
- GA4 snippet placeholder.

## Before launch — important placeholders
1. Replace `Your Print Partner` with the real business / trading name and adjust all brand copy.
2. In `src/layouts/BaseLayout.astro`, replace `https://yourdomain.com` with the purchased domain. Also update `public/robots.txt` to the real sitemap URL.
3. Replace `G-XXXXXXXXXX` with the actual Google Analytics 4 measurement ID, or remove the GA script until configured.
4. Replace `https://wa.me/27XXXXXXXXX...` in `BaseLayout.astro` with the WhatsApp Business number in international digits (no `+`, spaces or leading `0`).
5. Add the account manager's phone/email, company address, business registration/privacy details as appropriate. Do not publish private details without consent.
6. The quote form is set up for Netlify Forms. Deploy on Netlify and confirm form detection in the dashboard, then test a real submission. For GitHub Pages, choose a separate form handler before launch.
7. Add genuine, licensed photos to `public/images/` if desired. The homepage hero currently uses a CSS illustration, so it loads without heavy imagery.
8. Verify sitemap output and submit it in Google Search Console. Create/verify Google Business Profile if eligible. Add an actual privacy notice before activating analytics in line with applicable privacy requirements.
9. Test mobile layout, links, form submission, keyboard navigation, page speed and structured data before announcing the website.

## Run locally
Install Node.js LTS, then in this folder:

```bash
npm install
npm run dev
```

Build production output:

```bash
npm run build
npm run preview
```

## Deploy to Netlify
1. Push this folder to a GitHub/GitLab repository.
2. In Netlify, import the repository.
3. Build command: `npm run build`
4. Publish directory: `dist`
5. Add your custom domain in Netlify and follow its DNS instructions. HTTPS is issued automatically after DNS verification.

## SEO notes
This starter improves crawlability and page targeting but cannot guarantee rankings, Discover inclusion, AI-feature citations, or a particular PageSpeed score. Search performance depends on real content quality, authority, user intent, site reputation, competition and ongoing measurement. Add verified business details and useful original project examples over time.


## GitHub Pages deployment

This repository includes `.github/workflows/astro.yml`. In GitHub, open **Settings → Pages** and set **Build and deployment → Source** to **GitHub Actions** (not Deploy from a branch/Jekyll). Push the files to the `main` branch; the workflow will build Astro and publish `dist`.

The current workflow assumes the repository is named `Commercial-print-website` and therefore builds project-page URLs under `/Commercial-print-website/`. If the repository name changes, update the `base` value in `astro.config.mjs`. If you connect a custom domain to GitHub Pages, change the base to `/`.

Before publishing, replace the example domain and WhatsApp placeholder number in `src/layouts/BaseLayout.astro`. The WhatsApp link currently contains `27XXXXXXXXX`, so it will not reach a real account until the correct number is entered.


## Design and launch notes (14 October 2026)

- The homepage includes a responsive, illustrated portfolio section for calendars/diaries, books/yearbooks, retail print and packaging/distribution. These are clearly labelled as illustrative concepts, not real client work. Replace them with approved photographs of completed work if/when available.
- The positioning is intentionally focused on high-volume commercial print, tailored briefs, a dedicated account contact and distribution coordination rather than trying to copy Jetline's broad franchise/store model. The visual palette uses deep blue and red accents inspired by Novus Print’s public-facing brand colours; it does not use Novus Print’s logo or imply the website is owned by Novus.
- Internal navigation uses Astro's configured base path so it works on the GitHub Pages project URL as well as root-domain hosting.
- Before launch, replace `https://yourdomain.com` in `astro.config.mjs` and `src/layouts/BaseLayout.astro` with the actual purchased domain; replace the WhatsApp placeholder `27XXXXXXXXX`; and connect the quote form to Netlify Forms (or another working form handler).
- Do not claim certifications, production capacity, delivery guarantees or client testimonials unless the business can verify them.
