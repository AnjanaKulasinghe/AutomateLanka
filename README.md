# AutoMate Lanka

A responsive, single-page website for AutoMate Lanka, a mobile automotive service in Auckland. The site is built with plain HTML, CSS, and JavaScript for GitHub Pages. It has no build step or server-side dependencies.

## Project files

- `index.html` contains the page content and metadata.
- `css/style.css` contains the responsive styles.
- `js/main.js` handles the mobile navigation and small page interactions.
- `img/` contains the favicon and optimized desktop and mobile photography.
- `robots.txt` and `sitemap.xml` provide crawler discovery for the public homepage.
- `scripts/check_seo.py` runs dependency-free SEO regression checks.

## Preview locally

Open `index.html` in a browser, or start a simple local web server from the project directory:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Check SEO metadata

Run `python3 scripts/check_seo.py` to validate the page metadata, canonical URL,
JSON-LD, internal fragment links, sitemap and robots policy. Update this checker,
the sitemap and the SEO documents when adding any public route. There is no CI
workflow in this repository today, so the checker is available for local and
pre-publish use.

## Publish with GitHub Pages

1. Push the project files to the GitHub repository.
2. In the repository, open **Settings** and then **Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select the branch to publish and choose `/(root)` as the folder.
5. Save. GitHub Pages will publish `index.html` and its sibling `css`, `js`, and `img` folders.

For a custom domain, configure it in GitHub Pages and add the matching DNS records at the domain provider. The site itself is static. Phone, email, and map actions open the visitor's corresponding app or service.
