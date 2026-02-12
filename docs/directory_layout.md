# Directory Layout

## Root Structure

```
biomimetic-inventions-public/
├── docs/                          # Documentation (this directory)
│   └── directory_layout.md        # This file
├── golden-angle-antenna-GAFAA-public/  # GAFAA/Phyllux Wave demos
│   ├── docs/                     # GAFAA-specific documentation
│   ├── examples/                 # Numbered demo scripts (001-004)
│   ├── src/                      # Source code modules
│   └── README.md                # GAFAA overview
├── PhiKey-public/                # Phyllux Vault crypto demos
│   ├── docs/                     # PhiKey-specific documentation
│   ├── examples/                 # Numbered demo scripts (011-014)
│   ├── src/                      # Source code modules
│   └── README.md                 # PhiKey overview
├── PNM-public/                    # PNM/Phyllux Mesh demos
│   ├── docs/                     # PNM-specific documentation
│   ├── examples/                 # Numbered demo scripts (021-024)
│   ├── src/                      # Source code modules
│   └── README.md                 # PNM overview
├── README.md                      # Main repository overview
├── LICENSE.md                     # License and ethical tiers
├── CONTRIBUTING.md                # Contribution guidelines
├── project_overview.md            # PPA reference and extensions
├── PITCH.md                       # Market and partnership info
└── [other documentation files]    # Prior art, patents, etc.
```

## File Naming Convention

All example Python files follow numbered lowercase-hyphenated format:
- **GAFAA examples**: `001-phyllux-gafaa-*.py` through `007-phyllux-gafaa-*.py`
  - 001-004: Basic demos and visualizations
  - 005-007: Realistic RF analysis, SVG visualization, multi-frequency comparison
- **PhiKey examples**: `011-phyllux-phikey-*.py` through `014-phyllux-phikey-*.py`
- **PNM examples**: `021-phyllux-pnm-*.py` through `027-phyllux-pnm-*.py`
  - 021-024: Basic demos and visualizations
  - 025-027: Realistic neural analysis, SVG visualization, crosstalk optimization

## Image Directory Structure

**Root `/images/` Directory:**
- Primary location for generated visualization images
- Contains clean reference images (e.g., `*_121_clean.png` patterns)
- All image generation scripts output to this directory using relative path resolution
- Scripts automatically detect repository root by searching for `README.md` and `LICENSE.md`

**Subproject `/docs/assets/` Directories:**
- `golden-angle-antenna-GAFAA-public/docs/assets/` - SVG layouts and PNG plots for GAFAA
- `PNM-public/docs/assets/` - SVG layouts and PNG plots for PNM
- `PhiKey-public/docs/assets/` - SVG layouts and PNG plots for Phyllux Vault
- These contain SVG visualizations and documentation-specific images referenced in README files

**Image Generation:**
- All Python visualization scripts use portable relative paths
- Scripts locate repository root automatically
- Images are saved to root `/images/` directory for consistency

## Unified Under PPA Embodiments

All implementations are unified under phyllotactic system principles per PPA "Phyllotactic Multi-Domain System for Neural Interfaces, Wireless Communications, and Cryptographic Security" prepared for filing (to be filed late January 2026).
