#!/usr/bin/env python3
"""Dependency-free SEO regression checks for this static single-page site."""

from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "https://automatelanka.koungasolutions.co.nz/"
errors = []


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.metas = {}
        self.canonicals = []
        self.title = ""
        self.in_title = False
        self.jsonld = []
        self.in_jsonld = False
        self.script_text = []
        self.images_missing_alt = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.metas.setdefault(key.lower(), []).append(attrs.get("content", ""))
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonicals.append(attrs.get("href", ""))
        if tag == "title":
            self.in_title = True
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.script_text = []
        if tag == "img" and not attrs.get("alt", "").strip():
            self.images_missing_alt.append(attrs.get("src", "(unknown image)"))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_jsonld:
            self.jsonld.append("".join(self.script_text))
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_jsonld:
            self.script_text.append(data)


def check(condition, message):
    if not condition:
        errors.append(message)


html = (ROOT / "index.html").read_text(encoding="utf-8")
doc = Document()
doc.feed(html)
check(bool(doc.title.strip()), "Missing page title")
check(len(doc.title.strip()) <= 70, "Title is longer than 70 characters")
check(len(doc.metas.get("description", [])) == 1, "Expected one meta description")
description = doc.metas.get("description", [""])[0]
check(70 <= len(description) <= 170, "Meta description should be 70–170 characters")
check(doc.canonicals == [CANONICAL], "Canonical URL is missing, duplicated, or differs from the configured domain")
for name in ("og:title", "og:description", "og:url", "og:image", "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
    check(len(doc.metas.get(name, [])) == 1 and bool(doc.metas[name][0]), f"Missing or duplicated {name}")
check(doc.metas.get("og:url") == [CANONICAL], "Open Graph URL differs from canonical")
check(doc.metas.get("robots") == ["index,follow,max-image-preview:large"], "Expected the production index/follow policy")

duplicates = sorted({value for value in doc.ids if doc.ids.count(value) > 1})
check(not duplicates, f"Duplicate HTML IDs: {', '.join(duplicates)}")
ids = set(doc.ids)
bad_fragments = [href for href in doc.links if href.startswith("#") and href[1:] not in ids]
check(not bad_fragments, f"Broken internal fragment links: {', '.join(bad_fragments)}")
check(not doc.images_missing_alt, f"Images missing alt text: {', '.join(doc.images_missing_alt)}")

schema_entities = []
for raw in doc.jsonld:
    try:
        data = json.loads(raw)
        schema_entities.extend(data.get("@graph", [data]))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON-LD: {exc}")
businesses = [item for item in schema_entities if item.get("@type") == "AutoRepair"]
check(len(businesses) == 1, "Expected exactly one AutoRepair entity")
if businesses:
    business = businesses[0]
    check(business.get("@id") == CANONICAL + "#business", "AutoRepair entity ID does not use the canonical business ID")
    check(bool(business.get("telephone")) and bool(business.get("email")), "AutoRepair contact details are incomplete")
    check(bool(business.get("areaServed")), "AutoRepair service area is missing")
    check(len(business.get("hasOfferCatalog", {}).get("itemListElement", [])) >= 1, "Visible services are missing from the service catalog")

try:
    sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [node.text for node in sitemap.findall("sm:url/sm:loc", ns)]
    check(locations == [CANONICAL], "Sitemap must contain each canonical public URL exactly once")
except (ET.ParseError, OSError) as exc:
    errors.append(f"Invalid sitemap XML: {exc}")

robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
check(re.search(r"(?im)^User-agent:\s*\*\s*$", robots) is not None, "robots.txt has no general crawler policy")
check(re.search(r"(?im)^Allow:\s*/\s*$", robots) is not None, "robots.txt must allow public site crawling")
check(f"Sitemap: {CANONICAL}sitemap.xml" in robots, "robots.txt sitemap URL is incorrect")

if errors:
    print("SEO checks failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("SEO checks passed: metadata, canonical, social cards, JSON-LD, links, sitemap and robots.txt.")
