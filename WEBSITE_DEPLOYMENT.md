# Phyllux Website Deployment

## Netlify + GitHub: No Extra Storage Needed

Everything in your GitHub repo is deployed as a static site. There is no separate “storage” account—docs, images, and HTML all live in the repo and are served from the same domain.

## Test locally

```powershell
cd d:\Workspace\website
python -m http.server 8080
```

Open http://localhost:8080 in a browser.

## Quick Deploy to phyllux.io

1. **Copy website contents into the GitHub repo**
   - Copy everything from `d:\Workspace\website\` into the root of `biomimetic-inventions-public`:
     - `index.html` (hub)
     - `vision.html`, `technology.html`, `engenica.html`, `proof.html`, `partners.html`, `ip.html`, `ethics.html`, `docs.html`, `about.html`, `ecosystem.html`
     - `assets/` (all images)
     - `docs/` (full docs folder)
   - Do not nest them inside another folder; they should be at the repo root

2. **Commit and push**
   ```bash
   git add .
   git commit -m "Add website and docs"
   git push origin main
   ```

3. **Netlify auto-deploys**
   - If Netlify is connected to the repo, it will deploy automatically
   - Your site will be live at the configured domain (e.g. phyllux.io)

## URLs After Deploy

| Link | Live URL |
|------|----------|
| Home | `https://phyllux.io/` |
| Docs | `https://phyllux.io/docs/` |
| VAULT | `https://phyllux.io/docs/vault/` |
| ENGENICA | `https://phyllux.io/docs/engenica/` |
| CORE | `https://phyllux.io/docs/core/` |
| Partner intake | `https://phyllux.io/docs/partner/` |
| Proof packs | `https://phyllux.io/docs/proof/` |
| IP posture | `https://phyllux.io/docs/ip/` |
| Ethics | `https://phyllux.io/docs/ethics/` |
| Demos | `https://phyllux.io/docs/demos/` |

All site links use relative paths (e.g. `docs/vault/`), so they work both locally and on the deployed domain.
