# SEO checklist for future changes

## New route or service page

- [ ] Confirm the service is genuinely provided and obtain owner-approved, accurate source information.
- [ ] Give the page one distinct customer intent; avoid thin duplicate or suburb doorway pages.
- [ ] Add a unique title, meta description, absolute canonical, robots policy and social title/description/URL/image.
- [ ] Use crawlable HTML content and existing site navigation patterns; don't introduce visible UI without design approval.
- [ ] Relate service structured data to the one stable AutoMate Lanka `#business` entity. Mark only facts visible on the page and verified by the owner.
- [ ] Add the canonical public URL to `sitemap.xml`; never list fragments, aliases, private or redirected URLs.
- [ ] Add internal links and verify all fragment targets and telephone/email/booking destinations.
- [ ] Run `python3 scripts/check_seo.py`; extend the checker for new route expectations.
- [ ] Run the normal site review and visual/functional comparison before publishing.

## New image

- [ ] Use genuine, licensed/approved imagery; don't imply a stock/generated image depicts the business or completed work.
- [ ] Provide concise, contextual alt text for meaningful images; decorative imagery should have empty alt.
- [ ] Keep intrinsic dimensions and responsive behavior to avoid layout shifts; preserve approved crop and presentation.
- [ ] Use appropriate compression without visible quality loss; don't lazy-load the above-the-fold hero.
- [ ] Update social metadata only to an existing, publicly accessible image URL.

## Technical and local changes

- [ ] Keep business name, phone, hours, address/service area and website consistent with owner-confirmed source of truth.
- [ ] Confirm whether an address is public/customer-facing before publishing in visible content, schema or external listings.
- [ ] Keep one canonical host, correct redirect behavior, crawlable robots policy and matching sitemap.
- [ ] Do not invent ratings, reviews, locations, prices, specializations, credentials, availability or guarantees.
- [ ] Preserve privacy controls and existing analytics settings; don't add duplicate analytics scripts.
- [ ] Don't submit real booking/enquiry actions in automated checks.
