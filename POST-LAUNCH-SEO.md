# Post-launch SEO verification

The owner confirmed that `automatelanka.koungasolutions.co.nz` is the correct current hosting alias. Use it for current production verification. The business plans to move to its proper domain later; the public `www.automatelanka.nz` site currently has different content, so reconcile that content and prepare redirects as part of the future migration. Keep the alias canonical until then.

## 1. HTTP, HTTPS, canonical and crawl files

From a terminal, replace `https://CONFIRMED-HOST/` with the selected canonical URL:

```sh
curl -sSIL https://CONFIRMED-HOST/
curl -sS https://CONFIRMED-HOST/ | head -c 3000
curl -sSIL https://CONFIRMED-HOST/robots.txt
curl -sS https://CONFIRMED-HOST/robots.txt
curl -sSIL https://CONFIRMED-HOST/sitemap.xml
curl -sS https://CONFIRMED-HOST/sitemap.xml
```

Confirm the preferred homepage returns HTTP 200, HTTPS works, aliases redirect once to the preferred host, HTML canonical matches the preferred host, and sitemap/robots return HTTP 200 with valid content. Check that no staging host is indexable.

## 2. Search Console and indexing

1. In Google Search Console, add the production domain property and verify it via DNS (requires domain access) or use the URL-prefix property verification method offered by Google.
2. Inspect the homepage URL. Confirm Google-selected canonical matches the chosen URL and page fetch/indexing is allowed.
3. Submit `/sitemap.xml`; monitor processing and indexing reports.
4. Request indexing only after the final canonical host is live and stable.
5. Check search queries, impressions, clicks, country/device, and page indexing weekly at first.

## 3. Google Business Profile and Maps

1. Sign in as the business owner and locate the existing profile before creating another.
2. Confirm the business name; select the best currently available primary category for the real business and only justified secondary categories.
3. Select storefront or service-area setup accurately. Do not show a residential address publicly unless it is a customer-facing location and the owner intends to publish it.
4. Verify phone, canonical website, booking path (if any), actual hours, holiday hours and areas genuinely served.
5. Add services and real business photos; complete ownership/verification prompts.
6. Ask customers for honest, unbiased reviews after genuine service and respond without disclosing private details. Never buy, gate or fabricate reviews.
7. Understand that Maps visibility is influenced by relevance, distance and prominence; no placement is guaranteed.

## 4. Bing Webmaster Tools and AI discovery

1. Verify the preferred domain in Bing Webmaster Tools and submit the sitemap.
2. Review crawl/index reports and correct canonical, DNS or crawl issues.
3. Keep the public HTML, robots policy and business identity accurate. Do not add speculative AI-specific metadata or hidden content.

## 5. Quality and conversions

- Run `python3 scripts/check_seo.py` locally before publishing.
- Run [PageSpeed Insights](https://pagespeed.web.dev/) on the production homepage for mobile and desktop; keep lab results separate from field Core Web Vitals.
- Validate JSON-LD with [Schema.org Validator](https://validator.schema.org/) and check Google-specific features with [Rich Results Test](https://search.google.com/test/rich-results). Valid Schema.org markup does not guarantee a Google rich result.
- Test phone, email, map and service enquiry actions on a real device without placing an unintended call or sending an enquiry.
- If analytics is approved, verify property ownership, privacy/consent settings, no duplicate tags, and events that represent completed conversions. Do not count a click as a successful booking.
- Confirm Search Console and analytics are not polluted by validation traffic; block analytics during automated tests.
