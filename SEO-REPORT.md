# SEO implementation report

**Date:** 26 November 2026  
**Release recommendation:** **CONDITIONAL GO** for merging/review; **not production-verified**.

## Summary

Implemented SEO foundations for the static one-page site: page title/description, canonical and social metadata, linked `WebSite`/`AutoRepair` JSON-LD with currently visible services and contact information, `robots.txt`, a one-route sitemap, and a lightweight SEO checker. Following the owner's approval, several existing copy blocks now explain the mobile service model, current service scope and phone/email enquiry path more clearly. Small text sizes were enlarged for readability; section structure, colors, imagery, interaction and domain configuration remain unchanged.

## Architecture and route inventory

- Architecture: plain HTML, CSS, JavaScript; GitHub Pages custom domain in `CNAME`; no build step or CI workflow.
- Public routes: `/` (one). Existing anchors: `#services`, `#about`, `#contact`.
- Automotive service pages: none as separate routes; six service groups appear on the homepage.
- Market shown on site: mobile vehicle care across the Auckland region, New Zealand.
- Homepage target: mobile mechanic Auckland / mobile vehicle servicing and repairs Auckland.

## Changes

- `index.html`: title, description, index/follow robots directive, canonical, Open Graph and Twitter card, stable `WebSite`/`AutoRepair` graph and visible-service catalog.
- `css/style.css`: increased formerly 10–13px text to 13–15px minimum across navigation, body copy, contact details, buttons and supporting labels; retained existing typefaces, colors and layout rules.
- `robots.txt`, `sitemap.xml`: crawl access and one canonical URL.
- `scripts/check_seo.py`: dependency-free local regression validation.
- `README.md`: SEO checker and sitemap/robots documentation.
- `SEO-AUDIT.md`, `SEO-STRATEGY.md`, `SEO-GROWTH-PLAN.md`, `SEO-CONTENT-RECOMMENDATIONS.md`, `SEO-CHECKLIST.md`, `POST-LAUNCH-SEO.md`: audit and operator docs.

## Coverage and results

- Metadata: one unique title/description; canonical and social URLs consistently use the CNAME host.
- Structured data: one `WebSite` entity and one linked `AutoRepair` entity; no unconfirmed street address, coordinates, reviews, ratings, credentials or prices.
- Sitemap: the sole homepage route. Fragments are not sitemap URLs.
- Robots: public crawl allowed; sitemap declared.
- Checker: run `python3 scripts/check_seo.py` (result recorded after final validation).
- Visual, functional, browser console, Lighthouse, HTML validator, production HTTP/DNS, and Core Web Vitals: not run because browser/network validation tooling was unavailable. Larger typography and copy may affect text wrapping; no before/after pixel comparison or visual-equivalence claim is made.
- Existing phone/email interactions remain present in source; no test enquiry was submitted.

## Blockers and classification

- **Confirmed:** `automatelanka.koungasolutions.co.nz` is the correct current hosting alias and is used consistently as canonical. Production HTTP/DNS responses still need verification.
- **Future migration:** the business plans to move to its proper domain later. Public `www.automatelanka.nz` content differs from this repository; reconcile it and prepare DNS, HTTPS, one-hop redirects, canonical/social/schema URLs, sitemap, robots and Search Console/Bing properties during that migration. No migration was attempted.
- **Requires business confirmation:** whether the visible Sunnyhills address is a public business location or private residence; posted weekday hours and “on-call” wording; exact service areas and high-voltage service scope.
- **Requires external account access:** Google Search Console, Google Business Profile, Bing Webmaster Tools, analytics/consent state, and domain/DNS. None were accessed or modified.
- **Implemented, awaiting production verification:** canonical, metadata, JSON-LD, sitemap, robots response and indexability on the final public host.
- **Requires separate factual approval:** service-specific pages, trust information, customer case studies, or additional service-area details; source evidence is still needed.
- **Environment limitation:** no browser screenshot/visual regression, Lighthouse or live HTTP test.
- **Not applicable:** multi-page route mapping, online form submission tests (site uses phone/email actions, not a booking form), redirect testing within this repository.

## Readiness

The code is ready for review. Before calling it production-ready, verify the current alias responses and address privacy question, publish to the confirmed host, then follow [POST-LAUNCH-SEO.md](POST-LAUNCH-SEO.md). The future domain migration is not a blocker to the current canonical setup. No deployment was performed.
