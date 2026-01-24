# Audit Notes – Biomimetic Inventions Public Repository

**Date:** January 21, 2026  
**Auditor:** AI Analysis System  
**Scope:** Mandatory analysis phase - documentation and code review

## Summary

This repository serves as a public demonstration and prior-art archive for biomimetic phyllotactic systems (GAFAA, PNM, Phyllux Vault). The structure is well-organized with clear separation of concerns, appropriate disclaimers, and consistent branding. Several minor issues were identified that do not require immediate action but should be noted for future maintenance.

---

## Issues Identified

### 1. Hardcoded Absolute Paths in Image Generation Scripts
**Risk Level:** Medium  
**Status:** ✅ **RESOLVED** (January 21, 2026)

**Files Affected:**
- `PNM-public/src/pnm_public/spiral_utils.py` (line 14)
- `PhiKey-public/src/phikey_public/geometric_utils.py` (line 14)
- `golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py` (line 14)
- `golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py` (line 14)

**Issue Description:**
Multiple image generation scripts used hardcoded absolute paths:
```python
IMAGE_DIR = r"D:\Phyllux Project\biomimetic-inventions-public\images"
```

This would fail on other systems or when the repository is cloned to different locations.

**Resolution:**
All scripts now use portable relative path resolution that automatically detects the repository root by searching for `README.md` and `LICENSE.md` marker files:
```python
# Find repository root by looking for README.md or LICENSE.md
REPO_ROOT = SCRIPT_DIR
for _ in range(5):  # Max 5 levels up
    if os.path.exists(os.path.join(REPO_ROOT, 'README.md')) and \
       os.path.exists(os.path.join(REPO_ROOT, 'LICENSE.md')):
        break
    parent = os.path.dirname(REPO_ROOT)
    if parent == REPO_ROOT:  # Reached filesystem root
        REPO_ROOT = SCRIPT_DIR  # Fallback to script directory
        break
    REPO_ROOT = parent

IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
```

**Impact:** Scripts now work portably across different systems and repository locations.

---

### 2. Image Directory Structure Inconsistency
**Risk Level:** Low  
**Status:** ✅ **RESOLVED** (January 21, 2026)

**Files Affected:**
- Root `/images/` directory contains: `array_factor_polar.png`, `phikey_121_clean.png`, `spiral_positions.png`, `toy_electrode_array.png`
- `golden-angle-antenna-GAFAA-public/images/` contains: `gafaa_121_clean.png`
- `PNM-public/images/` is empty
- `PhiKey-public/images/` is empty

**Issue Description:**
Image files were stored in different locations. Some scripts generated to root `/images/`, while README files referenced subproject-specific image locations.

**Resolution:**
Image directory structure strategy has been documented in `docs/directory_layout.md`:
- Root `/images/` is the primary location for generated visualization images
- Subproject `/docs/assets/` directories contain SVG layouts and documentation-specific images
- All image generation scripts now consistently output to root `/images/` using portable path resolution

**Impact:** Image organization is now clearly documented and consistent.

---

### 3. Golden Angle Value Consistency
**Risk Level:** Low  
**Status:** ✅ Verified Consistent

**Issue Description:**
All code uses `137.508°` consistently. This is correct and aligned with documentation.

**Impact:** None - this is a positive finding.

---

### 4. PPA Disclaimer Coverage
**Risk Level:** Low  
**Status:** ✅ Well Covered

**Issue Description:**
All visualization and analysis scripts contain the required PPA disclaimer:
```python
"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
```

**Impact:** None - this is a positive finding.

---

### 5. Documentation Cross-References
**Risk Level:** Low  
**Status:** ✅ Well Structured

**Issue Description:**
Cross-references between repos are documented in README.md and project_overview.md. Links are consistent and point to correct GitHub repositories.

**Impact:** None - this is a positive finding.

---

## Positive Findings

1. **Clear Repository Roles:** The distinction between public demos (this repo), framework, and WIP repos is well-documented.

2. **Appropriate Disclaimers:** Medical, security, and performance disclaimers are present and appropriately worded.

3. **Consistent Branding:** "Phyllux" branding is consistent, with clear notes about "PhiKey" → "Phyllux Vault" transition.

4. **Ethical IP Framework:** The tiered licensing model is clearly documented and accessible.

5. **Prior Art Documentation:** PRIOR_ART.md, PATENTS.md, and TIMESTAMP.md provide appropriate context without making unsubstantiated claims.

---

## Recommendations

1. ✅ **Path Portability:** RESOLVED - All hardcoded absolute paths have been replaced with portable relative path resolution.

2. ✅ **Image Organization:** RESOLVED - Image directory structure strategy has been documented in `docs/directory_layout.md`.

3. **No Immediate Action Required:** Issues #3, #4, #5 are positive findings or low-risk items that do not require immediate correction.

---

## Notes on Repository Policy Compliance

This repository (biomimetic-inventions-public) follows the **REPLACEMENT ALLOWED** policy:
- Images may be replaced if contaminated or incorrect
- Code may be modified to fix bugs or improve correctness
- Documentation may be updated for clarity

All changes made should maintain:
- Conceptual coherence
- PPA alignment
- Appropriate disclaimers
- Cross-repo consistency

---

**End of Audit Notes**
