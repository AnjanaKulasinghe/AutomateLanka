# SEO audit

**Audit date:** 26 November 2026 (New Zealand time)  
**Scope:** Current repository and publicly discoverable search results. No external accounts were accessed.

## Initial assessment

- Static, single-page HTML site hosted as a GitHub Pages custom domain; CSS and JavaScript are local and there is no build step.
- One public indexable route: `/`. The `#services`, `#about`, and `#contact` fragments are sections of that page, not separate pages.
- The page already contains the business name AutoMate Lanka, Auckland coverage, mobile service model, six service groups, phone, email, a street address and weekday hours.
- Existing SEO included a title, description, language, favicon, hero preloads and partial JSON-LD. It lacked a canonical, robots policy, Open Graph URL/image, Twitter card and sitemap/robots files. Structured data lacked stable identifiers and service relationships.
- Existing Git working tree was clean before changes. No framework, color system, section structure, imagery or interaction changes were made. Following the owner's approvals, existing copy was refined in place and small typography sizes were enlarged for readability; no new sections or pages were introduced.

## Findings and status

| Priority | Finding | Classification | Resolution/status |
| --- | --- | --- | --- |
| Implemented | Current hosting alias and canonical host are `automatelanka.koungasolutions.co.nz` per owner confirmation. | Confirmed business/hosting detail | Canonical, social URLs, sitemap and robots consistently use this alias. |
| High | Public address is marked “Find us” although the business is described as mobile; it is not confirmed as a customer-facing workshop rather than a private/residential address. | Business confirmation | Kept existing visible content untouched; omitted `PostalAddress` from structured data until confirmed. |
| Medium | Missing canonical, robots.txt, XML sitemap, complete social sharing metadata, stable entity IDs and service catalog relationships. | Safe non-visual | Implemented. |
| Medium | No project SEO regression checker or existing CI workflow. | Safe non-visual | Added a dependency-free local checker; no CI pipeline exists to integrate it into. |
| Medium / future | A public site at `www.automatelanka.nz` has different content from this repository; the business plans to move to its proper domain later. | Future domain migration | No migration attempted. Before the move, confirm destination, reconcile the live content, map redirects and update canonical/social/schema/sitemap/robots consistently. |
| Low | No verified coordinates, official profile URLs, Google Business Profile status, public booking URL, or analytics IDs in the repo. | Business/external account confirmation | Omitted rather than guessed. |
| Low | No service-specific routes. | Existing architecture | The current page is one homepage with service sections. No pages or visible sections were added. |

## Implemented resolutions

- Unique Auckland/mobile-mechanic title and meta description; production index/follow directive.
- Absolute canonical and consistent Open Graph/Twitter metadata, including the existing hero image.
- One `WebSite` and one `AutoRepair` JSON-LD entity linked by stable IDs; Auckland Region, public phone/email, posted weekday hours, and visible service catalog. No unverified address, rating, coordinates, review, award or price is represented.
- XML sitemap for the one canonical public route and a crawl-allowing robots policy that points to it.
- `scripts/check_seo.py` for metadata, uniqueness, internal fragments, JSON-LD, service/entity presence, sitemap and robots validation.

## Baseline and limitations

- Baseline route count: one. Baseline source already had one title, one description, `en-NZ`, favicon and partial `AutoRepair` JSON-LD.
- No browser/screenshot, Lighthouse, HTML validator, production HTTP, DNS, Search Console or real-user Core Web Vitals tooling was available in this environment. No before/after performance measurement or pixel comparison is claimed.
- The website was not run in a graphical browser. Edits include the document head, existing text nodes, font-size rules, schema data, crawler files, documentation and a developer checker; visual preservation is not browser-verified, and larger text/copy may affect wrapping.
- Production HTTP, HTTPS, canonical, sitemap and robots responses on the current alias remain unverified in this environment.

## Business information requiring confirmation

1. When the business is ready to move from the current alias, confirm the proper primary domain, migration date, DNS ownership and redirect plan. Keep the current alias canonical until that migration is ready.
2. Is 32A The Boulevard, Sunnyhills a customer-facing business location, or is it residential/private? Does it belong in public address, Maps and business listing data?
3. Are “Monday to Friday, 9:00 am to 5:00 pm” current public hours? What does “On-call availability across Auckland” mean operationally (and should it be shown as hours or by arrangement)?
4. Is “Auckland region” the complete service area? Identify only areas actually served.
5. Confirm business name styling/legal name, and whether current six service groups remain accurate, especially high-voltage service capability.
6. Confirm official social URLs, Google Business Profile, booking URL, and whether the existing address is safe to publish.

## Research sources

- [Public site at automatelanka.nz](https://www.automatelanka.nz/) (content differs from this repository; reconcile content and redirects during the planned domain migration).
- [AutoPlace listing for Auto Mate Lanka NZ](https://www.autoplace.co.nz/shops/sunnyhills/auto-mate-lanka-nz) (third-party listing uses a spaced name variant; it states that listing details are from public sources and not yet checked by the business).
- Competitor examples and comparison are summarized in [SEO-STRATEGY.md](SEO-STRATEGY.md); competitor claims are not business claims.
