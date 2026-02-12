# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- phyllux-repo-archive (workspace) for deprecated process/docs

### Changed
- README streamlined to match phyllux.io quality
- README links updated to phyllux-technologies org

### Removed (moved to d:\Workspace\phyllux-repo-archive\biomimetic-inventions-public\)
- Internal alignment/audit/review/polish reports
- CI badge notes, dependabot merge plan, duplicate notes
- Image regeneration/reset plans, license detection fix reports
- REGENERATION_GUIDE, REPOSITORY_SUMMARY, WEBSITE_DEPLOYMENT
- test_generation.py

## [2026-01-25] - Repository Optimization

### Added
- CONTACT.md with inquiry guidelines
- Ecosystem footer in README with cross-repo links
- Installation section with step-by-step instructions
- Usage examples for all three core technologies

### Changed
- README updated with Overview, Quick Start, Installation, Usage, Integration sections
- Contact information standardized across documentation

## [2026-01-22] - License Normalization

### Changed
- LICENSE file cleaned to contain only MIT text
- LICENSE-IP-NOTICE.md created for IP notices
- DOCS_LICENSE.md created for documentation licensing
- LICENSE_SUMMARY.md created for quick reference

### Fixed
- GitHub license detection now correctly identifies MIT
- All script references updated from LICENSE.md to LICENSE

## [2026-01-21] - Image Regeneration System

### Added
- Centralized `/images/` directory
- `generate_plot_images.py` for phyllotaxis, spiral, and geometric plots
- `generate_visualizations.py` for SVG layouts
- `regenerate_all_images.py` master script
- `regenerate_images.ps1` PowerShell automation

### Changed
- All Python scripts updated for portable path detection
- Headless plotting implemented (matplotlib.use('Agg'))
- All markdown references updated to point to `/images/`

### Fixed
- Removed plt.show() calls for automated generation
- Clean white backgrounds for all images
- Fixed Unicode encoding issues in PowerShell scripts

## [2026-01-07] - Initial Public Disclosure

### Added
- Initial repository structure
- Three core technology demos (PNM, GAFAA, Phyllux Vault)
- Prior art establishment via commits
- MIT license as defensive publication

### Notes
- Priority Date: January 7, 2026
- Provisional Patent Application prepared for filing (to be filed late January 2026)

---

**Legend:**
- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security fixes
