# Repository Summary: biomimetic-inventions-public

**Repository:** `phibronotchi-beep/biomimetic-inventions-public`  
**Type:** Public demos and prior art archive  
**Status:** Active development  
**Last Updated:** January 25, 2026

---

## Executive Summary

This repository serves as a public demonstration and prior art archive for three biomimetic inventions that apply phyllotactic patterns (golden angle ~137.508°) across multiple domains: neural interfaces, wireless communications, and cryptographic security. The repository establishes prior art through public disclosure and commits, supporting a provisional patent application (PPA) prepared for filing in late January 2026.

**Core Principle:** Unified phyllotactic system using the golden angle (~137.508°) as a geometric blueprint for multi-domain applications.

---

## Repository Purpose

### Primary Functions
1. **Prior Art Establishment**: Public disclosure via commits (Jan 7, 2026) and MIT license as defensive publication
2. **Educational Demos**: Conceptual demonstrations of phyllotactic applications
3. **Research Collaboration**: Open-source code for academic and research use
4. **IP Documentation**: Clear licensing structure with ethical IP tiers

### Status
- **Maturity**: Conceptual/educational only – not production-ready
- **Validation**: Simulation-based; empirical validation required
- **PPA Status**: Prepared for filing (to be filed late January 2026)
- **Priority Date**: January 7, 2026 (via first commit)

---

## Core Technologies

### 1. Phyllotactic Neural Meshing (PNM) - Phyllux Mesh
**Domain:** Neural interfaces, brain-computer interfaces  
**Concept:** Electrode array layouts using phyllotactic spiral patterns to minimize crosstalk and optimize neural signal acquisition.

**Location:** `PNM-public/`  
**Key Files:**
- `src/pnm_public/neural_utils.py` - Neural interface utilities
- `src/pnm_public/spiral_utils.py` - Spiral pattern generation
- `src/pnm_public/svg_utils.py` - SVG visualization
- `examples/` - 7 demonstration scripts

**Disclaimer:** Mathematical layouts only; not clinical devices; no medical performance claims.

---

### 2. Golden-Angle Fractal Antenna Array (GAFAA) - Phyllux Wave
**Domain:** Wireless communications, RF antenna arrays  
**Concept:** Antenna element placement using phyllotactic spiral layouts for wideband performance and reduced mutual coupling.

**Location:** `golden-angle-antenna-GAFAA-public/`  
**Key Files:**
- `src/gafaa_public/phyllotaxis_utils.py` - Phyllotactic position generation
- `src/gafaa_public/rf_utils.py` - RF analysis and array factor calculations
- `src/gafaa_public/svg_utils.py` - SVG visualization
- `examples/` - 7 demonstration scripts

**Disclaimer:** Illustrative code; not validated RF design; no guaranteed performance claims.

---

### 3. Phyllux Vault Geometric Security Protocol
**Domain:** Cryptographic security, post-quantum cryptography exploration  
**Concept:** Lattice-based cryptography using golden ratio lattice structures and geometric path traversal.

**Location:** `PhiKey-public/` (folder name retained for continuity; technology branded as Phyllux Vault)  
**Key Files:**
- `src/phikey_public/geometric_utils.py` - Geometric lattice generation
- `examples/` - 4 demonstration scripts

**Disclaimer:** Conceptual experiments; not production-grade cryptography; not security-reviewed; must not be used for real-world data protection.

---

## Repository Structure

```
biomimetic-inventions-public/
├── README.md                    # Main overview and navigation
├── CONTACT.md                   # Contact information and inquiry guidelines
├── CONTRIBUTING.md              # Contribution guidelines and PPA alignment
├── SECURITY.md                  # Security policy and vulnerability reporting
├── DISCLOSURE.md                # Disclosure framework and maturity levels
│
├── Licensing Files
│   ├── LICENSE                  # MIT License (canonical, code only)
│   ├── DOCS_LICENSE.md          # CC BY-SA 4.0 (documentation)
│   ├── LICENSE-IP-NOTICE.md     # Intellectual property notice
│   └── LICENSE_SUMMARY.md       # Licensing summary and quick reference
│
├── IP & Legal Documentation
│   ├── PRIOR_ART.md             # Public prior-art summary
│   ├── PATENTS.md               # Patenting intentions and notes
│   ├── INVENTION_DISCLOSURE.md  # High-level disclosure summary
│   ├── INVENTORSHIP_DECLARATION.md
│   ├── TIMESTAMP.md             # Timing and disclosure log
│   └── COPYRIGHT                # Copyright information
│
├── Project Documentation
│   ├── project_overview.md       # PPA reference and unifying concepts
│   ├── PITCH.md                 # Market and partnership information
│   ├── INTEGRATED_SYSTEM.md     # Concept for combining all three technologies
│   ├── PHYLUX_SPINE.md          # Multi-repository governance framework
│   └── PHYLUX_VISION.md         # Long-term vision document
│
├── Image Generation
│   ├── generate_plot_images.py  # Generates phyllotaxis, spiral, geometric plots
│   ├── generate_visualizations.py # Generates SVG layouts for all three technologies
│   ├── regenerate_all_images.py  # Master script for image regeneration
│   ├── regenerate_images.ps1    # PowerShell automation script
│   └── images/                   # Centralized image directory
│       ├── *.png                 # Raster visualizations
│       └── *.svg                 # Vector layouts
│
├── Subprojects
│   ├── PNM-public/              # Neural meshing demos
│   │   ├── src/pnm_public/       # Source code
│   │   ├── examples/             # 7 demonstration scripts
│   │   ├── docs/                 # Background and overview
│   │   └── README.md
│   │
│   ├── golden-angle-antenna-GAFAA-public/  # Antenna array demos
│   │   ├── src/gafaa_public/     # Source code
│   │   ├── examples/             # 7 demonstration scripts
│   │   ├── docs/                 # Background and overview
│   │   └── README.md
│   │
│   └── PhiKey-public/           # Cryptographic security demos (Phyllux Vault)
│       ├── src/phikey_public/   # Source code
│       ├── examples/             # 4 demonstration scripts
│       ├── docs/                 # Background and overview
│       └── README.md
│
├── CI/CD & Automation
│   └── .github/
│       ├── dependabot.yml        # Dependency updates (pip, GitHub Actions)
│       └── workflows/
│           ├── ci.yml            # Main CI workflow (lint, links, syntax)
│           ├── lint.yml          # Markdown linting
│           ├── links.yml         # Link checking
│           └── reproducibility.yml  # Image generation verification
│
└── Documentation & Reports
    ├── docs/directory_layout.md  # Directory structure documentation
    ├── REGENERATION_GUIDE.md    # Image regeneration instructions
    └── [Various audit and alignment reports]
```

---

## Licensing Structure

### Dual-Licensing Model

1. **Source Code**: MIT License (`LICENSE`)
   - Applies to: Python scripts, executable code, source files
   - Permissive, allows commercial use
   - Requires attribution

2. **Documentation**: CC BY-SA 4.0 (`DOCS_LICENSE.md`)
   - Applies to: Markdown files, documentation, README files
   - Requires attribution and ShareAlike

3. **IP Notice**: Proprietary (`LICENSE-IP-NOTICE.md`)
   - Core inventions (PNM, GAFAA, Phyllux Vault) are proprietary
   - Commercial use requires licensing
   - Repository establishes prior art

### Ethical IP Tiers

1. **Free Tier**: Research, education, open-source contributions
2. **Commercial Tier**: Fair royalties for profit use
3. **Pioneer Tier**: Low/no-fee for high-impact players (sustainability, space, longevity)
4. **Community Defense**: No misuse; revocation for bad faith; no patent trolling

---

## Technical Stack

### Dependencies
- **Python 3.x** (primary language)
- **NumPy**: Numerical computations
- **Matplotlib**: Plotting and visualization
- **SVG generation**: Custom utilities for vector graphics

### Key Scripts
- **Image Generation**: All images are reproducible from Python scripts
- **Path Detection**: Portable repository root detection (checks for `README.md` and `LICENSE`)
- **Headless Plotting**: Uses `matplotlib.use('Agg')` for automated generation

### Image Management
- Centralized `/images/` directory
- All images generated from source code
- Clean backgrounds, no OS artifacts
- SVG and PNG formats

---

## CI/CD Automation

### GitHub Actions Workflows

1. **CI Workflow** (`.github/workflows/ci.yml`)
   - Runs on: push/PR to main, manual dispatch
   - Checks: Markdown linting, internal links, Python syntax
   - Status: Non-blocking (continue-on-error)

2. **Lint Workflow** (`.github/workflows/lint.yml`)
   - Markdown linting with `.markdownlint.json` config
   - Uses `DavidAnson/markdownlint-cli2-action@v16`

3. **Links Workflow** (`.github/workflows/links.yml`)
   - Link checking with `lycheeverse/lychee-action`
   - Internal links fail on broken; external links warn only

4. **Reproducibility Workflow** (`.github/workflows/reproducibility.yml`)
   - Verifies image generation capability
   - Runs on Python file changes

### Dependabot
- **Configuration**: `.github/dependabot.yml`
- **Updates**: Weekly for pip dependencies and GitHub Actions
- **Merge Plan**: Documented in `DEPENDABOT_MERGE_PLAN.md`

---

## Cross-Repository Ecosystem

This repository is part of a multi-repository Phyllux ecosystem:

1. **biomimetic-inventions-public** (this repo)
   - Public demos and prior art
   - Educational demonstrations
   - Prior art establishment

2. **phyllux-framework**
   - Core governance framework
   - Cross-repository alignment
   - Documentation standards

3. **phyllux-inventions-wip**
   - Work-in-progress laboratory
   - Experimental concepts
   - Strict preservation rules

4. **Phyllux-Monollux** (Private)
   - Full scope hub
   - NDA access required

---

## Key Documentation Files

### Legal & IP
- `PRIOR_ART.md`: Public prior-art summary for key concepts
- `PATENTS.md`: Informal notes on patenting intentions
- `INVENTION_DISCLOSURE.md`: High-level disclosure summary
- `INVENTORSHIP_DECLARATION.md`: Inventorship documentation
- `TIMESTAMP.md`: Timing and disclosure log

### Project Management
- `project_overview.md`: PPA reference and unifying fusions
- `PITCH.md`: Market and partnership information
- `INTEGRATED_SYSTEM.md`: Concept for combining PNM, GAFAA, and Phyllux Vault
- `CONTRIBUTING.md`: Contribution guidelines with PPA alignment

### Governance
- `SECURITY.md`: Security policy and vulnerability reporting
- `DISCLOSURE.md`: Disclosure framework and maturity levels
- `PHYLUX_SPINE.md`: Multi-repository governance framework

---

## Contact Information

**David Edward Sproule**  
Independent Inventor | Phyllux Technologies  
Alberta, Canada

**Email**: phibronotchi@gmail.com

### Inquiry Guidelines
- **Technical questions**: Open an issue in the relevant repository
- **Commercial licensing**: Email with subject "Commercial Licensing - [Technology Name]"
- **Research collaboration**: Email with subject "Research Collaboration - [Topic]"

---

## PPA (Provisional Patent Application) Details

**Title:** "Phyllotactic Multi-Domain System for Neural Interfaces, Wireless Communications, and Cryptographic Security"

**Status:** Prepared for filing (to be filed late January 2026)  
**Priority Date:** January 7, 2026 (via repository first commit)  
**Defensive Publication:** MIT License  
**Disclosures:** @Phibronotchi Jan 2026  
**Federal Funding:** None

**Field:** Biomimetic phyllotactic systems for neural/antenna/crypto/integration

---

## Extensions & Embodiments

The PPA embodiments unify multiple domains under phyllotactic system principles:

- **Biological**: Mycelium networks, biomimetic structures
- **AI/ML**: Mandelbrot optimizations, geometric learning
- **Medical**: Neuroprosthetics, brain-computer interfaces
- **Space**: Propulsion systems, orbital mechanics
- **Quantum**: Post-quantum cryptography exploration, quantum-resistant security research

All extensions unified under phyllotactic system principles per PPA embodiments.

---

## Image Reproducibility

### Master Scripts
- `generate_plot_images.py`: Generates phyllotaxis, spiral, and geometric plots
- `generate_visualizations.py`: Generates SVG layouts for GAFAA, PNM, and Phyllux Vault
- `regenerate_all_images.py`: Orchestrates regeneration of all images

### Automation
- `regenerate_images.ps1`: PowerShell script for Windows automation
- Portable path detection (finds repository root automatically)
- Headless plotting (no GUI required)

### Image Directory
- Centralized `/images/` directory
- All markdown references point to `/images/`
- Clean outputs (white backgrounds, no UI artifacts)

---

## Badges & Status

**README Badges:**
- License: MIT (links to LICENSE)
- CI: GitHub Actions workflow status
- Disclosure: Framework badge (links to DISCLOSURE.md)

**Status Indicators:**
- Conceptual/educational only
- Not production-ready
- Simulation-based
- Empirical validation required

---

## Important Disclaimers

1. **No Performance Guarantees**: Nothing guarantees any particular performance, safety level, or regulatory status
2. **Not Medical Advice**: PNM demos are not clinical devices; no medical claims
3. **Not Security-Reviewed**: Phyllux Vault is not production-grade cryptography
4. **Not Validated RF Design**: GAFAA demos are illustrative only
5. **Use at Own Risk**: All content provided as-is

---

## Citation

If referencing in academic work:

> Sproule, D. E. (2026). Biomimetic Inventions: Phyllotactic Neural Meshing (Phyllux Mesh), Golden-Angle Fractal Antenna Arrays (Phyllux Wave), and Phyllux Vault Cryptography (conceptual demos). GitHub repository: github.com/phibronotchi-beep/biomimetic-inventions-public

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/phibronotchi-beep/biomimetic-inventions-public.git
cd biomimetic-inventions-public

# Install dependencies
pip install -r requirements.txt

# Run example scripts
python PNM-public/examples/021-phyllux-pnm-3d-spiral-view.py
python golden-angle-antenna-GAFAA-public/examples/001-phyllux-gafaa-3d-spiral-view.py
python PhiKey-public/examples/011-phyllux-phikey-3d-spiral-view.py

# Regenerate all images
python regenerate_all_images.py
```

---

## Repository Statistics

- **Subprojects**: 3 (PNM, GAFAA, Phyllux Vault)
- **Example Scripts**: 18 total (7 PNM, 7 GAFAA, 4 Phyllux Vault)
- **Source Modules**: 3 main source directories
- **Documentation Files**: 20+ markdown files
- **CI/CD Workflows**: 4 GitHub Actions workflows
- **License Files**: 4 (MIT, CC BY-SA 4.0, IP Notice, Summary)

---

## Notes for Other Workspaces

### Key Concepts to Preserve
1. **Phyllotaxis & Golden Angle**: Core principle (~137.508°)
2. **Multi-Domain System**: Unified application across neural/antenna/crypto
3. **Prior Art Strategy**: Public disclosure via commits and MIT license
4. **Ethical IP Model**: 4-tier licensing structure
5. **Reproducibility**: All images generated from code

### Critical Files
- `README.md`: Main navigation and overview
- `LICENSE`: Canonical MIT license (GitHub detection)
- `CONTACT.md`: Contact information
- `project_overview.md`: PPA reference and extensions
- `LICENSE_SUMMARY.md`: Licensing quick reference

### Repository-Specific Rules
- **Image Replacement**: Allowed (clean regeneration)
- **Code Modification**: Allowed for fixes and improvements
- **Documentation**: Additive changes preferred
- **Preservation**: Maintain prior art record integrity

---

**End of Repository Summary**
