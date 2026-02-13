# Mega Site — Image Map

**Purpose:** Every image from ROOT and MASTERMIND mapped to website pages. Run `sync-images-from-root.ps1` before deploy.

**Sources:** ROOT/images, Me images/output, mastermind/assets  
**Existing assets:** See ASSETS_AND_IMAGES.md for website/assets/ inventory.

---

## Image Paths (website/assets/)

| Subfolder | Source | Use |
|-----------|--------|-----|
| david/ | ROOT/images/david-tech, Me images | About, index, profile |
| products/ | ROOT/images/products, Me images | Product heroes, social cards |
| platform/ | ROOT/images/platform | X, LinkedIn, GitHub (not on site) |
| marketing/ | ROOT/images/marketing | CTAs, section headers |
| embellishments/ | ROOT/images/embellishments | Dividers, corners |
| modules/ | mastermind/assets | MASTERMIND module images |

---

## Page → Image Map

### index.html
- Hero: assets/david/david-desk-mastermind-hero.png → fallback phyllux-hero-banner
- CTAs: assets/marketing/cta-get-mastermind-400x80.png, cta-try-phyllux-400x80.png, cta-partner-with-us-400x80.png, badge-open-source.png
- At work: 6 David images grid (desk, presenting, coding, whiteboard, nature-tech, celebrating)
- About section: assets/david/david-about-page-headshot.png → fallback assets/phyllux-about-hero.png
- Embellishments: assets/products/phyllux-embellishment.png (hero corners)
- Footer: assets/products/phyllux-footer-divider.png

### products.html
- Product heroes: assets/products/mastermind-hero-banner-1920x600.png, phyllux-hero-banner-1920x600.png, bwurm-hero-banner-1920x600.png, engenica-hero-banner-1920x600.png
- MASTERMIND card: assets/products/mastermind-social-card-1200x630.png
- Phyllux/ENGENICA cards: assets/products/* with fallback to assets/phyllux-*

### path.html
- Mutual flourishing: assets/products/mutual-flourishing-mission-card.png

### vision.html
- Hero: assets/phyllux-vision-hero.png
- Golden angle: assets/phyllux-golden-angle.png

### about.html
- Hero: assets/david/david-desk-mastermind-hero.png → fallback phyllux-about-hero.png
- Profile: assets/david/david-about-page-headshot.png
- At work gallery: 15 David images
- Find me: assets/platform/x-banner-1500x500.png, linkedin-banner-1584x396.png, github-org-500x500.png

### ecosystem.html
- Hero: assets/products/ecosystem-overview-1200x800.png → fallback phyllux-ecosystem-hero.png

### engenica.html
- Hero: assets/phyllux-engenica-hero.png
- Or: assets/products/engenica-hero-banner-1920x600.png

### technology.html
- Hero: assets/phyllux-tech-hero.png

### partners.html
- Hero: assets/david/david-collaborative-pair.png → fallback phyllux-partners-hero
- Ladder: assets/products/phyllux-partners-ladder.png
- CTA: assets/marketing/cta-partner-with-us-400x80.png

### ip.html, proof.html, ethics.html
- Heroes: assets/products/phyllux-*-hero.png (IP, proof, ethics) with fallback to assets/phyllux-*
- Ethics: assets/products/phyllux-ethics-commitments.png

### docs.html, ecosystem.html
- Docs hero: assets/products/phyllux-docs-hero.png
- Badge: assets/marketing/badge-open-source.png

---

## ROOT Image Catalog (from IMAGE_CATALOG.md)

**David + Tech:** david-desk-mastermind-hero, david-phyllux-presenting, david-coding-hands-on-keyboard, david-confident-founder-pose, david-explaining-whiteboard, david-tablet-phyllux-casual, david-side-profile-engenica, david-celebrating-success, david-nature-tech-outdoor, david-about-page-headshot, david-conference-speaking, david-workshop-leading, david-collaborative-pair, david-podcast-recording, david-workspace-behind-scenes, david-deep-work-thoughtful, david-reviewing-documents, david-reviewing-tech-contemplative

**Product:** mastermind-social-card, phyllux-social-card, engenica-social-card, bwurm-social-card, mutual-flourishing-mission-card, mastermind-launch-announcement, event-promo-workshop, ecosystem-overview, testimonial-placeholder-card, mastermind-hero-banner-1920x600, phyllux-hero-banner-1920x600, engenica-hero-banner-1920x600, bwurm-hero-banner-1920x600

**Marketing:** cta-get-mastermind, cta-try-phyllux, cta-partner-with-us, badge-open-source, newsletter-header, blog-header-template, blog-header-creator-notes, contact-section-header, about-david-section-header, video-thumbnail-template

**Embellishments:** phyllux-divider-embellishment, phyllux-corner-embellishment, phyllux-footer-embellishment

---

## Sync & Deploy

1. **Sync images:** `.\sync-images-from-root.ps1` (from website/)
2. **Deploy to repo:** `.\deploy-to-repo.ps1`

Images not yet in ROOT/Me images will use fallbacks (existing phyllux-* in assets/).

---

*Mega Site. February 2026.*
