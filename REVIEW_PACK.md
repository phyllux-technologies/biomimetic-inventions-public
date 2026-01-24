# Review Pack — biomimetic-inventions-public

**Date:** January 22, 2026  
**Analyst:** AI Systems Integrator  
**Scope:** Comprehensive hardening and alignment audit

---

## A) Repository Role Summary

**biomimetic-inventions-public** serves as canonical public prior art and reproducible demonstrations for core Phyllux technologies (Phyllux Mesh/PNM, Phyllux Wave/GAFAA, Phyllux Vault/PhiKey, Phyllux Core/IBS). This repository establishes dated prior art, provides toy-level code demonstrations, and maintains reproducibility through script-based image generation. Images can be regenerated from code (replacement allowed policy). The repo supports PPA filings without competing with them, using appropriate disclaimers for medical, security, and performance claims.

---

## B) Findings by Category

### 1) Secrets & Credentials Hygiene

**FINDINGS:**
- ✅ **No API keys found** in repository
- ✅ **No hardcoded credentials** detected
- ✅ **`.gitignore` properly configured** (excludes `.env`, `venv/`, etc.)
- ✅ **Scripts use relative paths** (portable path resolution implemented per AUDIT_NOTES.md)

**RECOMMENDATIONS:**
- Continue current practices
- No changes needed

---

### 2) Dependency & Supply Chain

**FINDINGS:**
- ✅ **`requirements.txt` present** in root directory
- ✅ **Dependencies listed:** `numpy>=1.21.0`, `matplotlib>=3.5.0`, `scipy>=1.7.0`
- ⚠️ **No version pinning** (uses `>=` instead of `==`)
- ⚠️ **No lockfile** (no `requirements.lock`)
- ✅ **Subprojects have their own `requirements.txt`** (GAFAA, PNM, PhiKey)

**RECOMMENDATIONS:**
- Consider pinning versions for reproducibility
- Document minimum Python version
- Consider `pip-tools` for dependency management

---

### 3) Licensing Consistency

**FINDINGS:**
- ✅ **LICENSE file present** (MIT License)
- ✅ **LICENSE.md also present** (contains MIT + IP notice)
- ⚠️ **Two license files** — verify they're consistent
- ✅ **IP notice clear:** Core inventions proprietary, code/docs MIT/CC BY-SA
- ✅ **Subprojects have LICENSE files** (GAFAA, PNM, PhiKey)

**RECOMMENDATIONS:**
- Verify LICENSE and LICENSE.md are consistent (they appear to be)
- Consider consolidating to single LICENSE file (optional)
- No critical issues

---

### 4) Disclosure & Claim Language

**FINDINGS:**
- ✅ **Well-qualified language** throughout:
  - "Conceptual/educational only"
  - "Toy demos only"
  - "Not production-ready"
  - "Simulation-based; empirical validation required"
- ✅ **Appropriate disclaimers:**
  - Medical: "not clinical devices, have not been tested in vivo"
  - Security: "not production-grade or security-reviewed cryptography"
  - Performance: "not to specify any validated RF design or guaranteed performance"
- ⚠️ **"Quantum-resistant" language found** in:
  - `PITCH.md`: "quantum-resistant security"
  - `README ALT.md`: "quantum-resistant cryptography", "Quantum-resistant"
  - `project_overview.md`: "quantum-resistant security"
- ✅ **No performance guarantees** detected

**RECOMMENDATIONS:**
- Soften "quantum-resistant" language to "explores quantum resistance" or "aims for quantum resistance"
- Update PITCH.md, README ALT.md, project_overview.md
- Continue qualified language practices

---

### 5) Link Rot & Cross-Repo Navigation

**FINDINGS:**
- ✅ **Cross-repo links** point to correct GitHub URLs:
  - phyllux-framework: https://github.com/phibronotchi-beep/phyllux-framework
  - phyllux-inventions-wip: https://github.com/phibronotchi-beep/phyllux-inventions-wip
- ✅ **Internal links** appear correct (subproject READMEs)
- ⚠️ **No external link validation** (links to creativecommons.org, etc. not checked)

**RECOMMENDATIONS:**
- Add external link validation to CI (warn, don't fail)
- Consider `LINKS.md` catalog for important external references

---

### 6) Repo Hygiene

**FINDINGS:**
- ✅ **`.gitignore` present** and properly configured
- ✅ **Images in `/images/` directory** (organized per AUDIT_NOTES.md)
- ✅ **Clean structure** (subprojects well-organized)
- ✅ **No duplicate files** detected
- ✅ **Consistent naming** conventions
- ⚠️ **Some documentation files** may be redundant:
  - `README ALT.md` (what is this?)
  - `The Phyllitactic Commons` (file or directory?)

**RECOMMENDATIONS:**
- Clarify purpose of `README ALT.md`
- Document `The Phyllitactic Commons` if it's important
- Minor cleanup, not critical

---

### 7) CI/Automation Readiness

**FINDINGS:**
- ❌ **No `.github/workflows/` directory** found
- ❌ **No CI/CD automation** present
- ❌ **No Dependabot configuration**
- ❌ **No pre-commit hooks**

**RECOMMENDATIONS:**
- Add GitHub Actions for:
  - Image regeneration verification (run scripts, verify outputs created)
  - Markdown linting (warn only)
  - Internal link checking (fail on broken)
  - External link checking (warn only)
- Add Dependabot for dependency updates
- Consider pre-commit hooks (whitespace, private key detection)

---

## C) Risk Assessment

### High Risk
- **None detected**

### Medium Risk
1. **No CI/CD automation**
   - **Impact:** Reproducibility not automatically verified
   - **Mitigation:** Add GitHub Actions to verify image generation
   - **Status:** Recommended improvement

2. **No dependency pinning**
   - **Impact:** Scripts may break with library updates
   - **Mitigation:** Pin versions in requirements.txt
   - **Status:** Should be addressed

### Low Risk
1. **Two license files** (LICENSE and LICENSE.md)
   - **Impact:** Potential confusion
   - **Mitigation:** Verify consistency, consider consolidation
   - **Status:** Minor cleanup

2. **Unclear file purposes** (`README ALT.md`, `The Phyllitactic Commons`)
   - **Impact:** Confusion
   - **Mitigation:** Document or remove
   - **Status:** Minor cleanup

---

## D) Proposed Changes

### High Priority (Functionality)
1. **Add GitHub Actions workflows**
   - Image regeneration verification (run scripts, check outputs)
   - Markdown lint (warn only)
   - Internal link check (fail on broken)
   - External link check (warn only)
   - Files: `.github/workflows/reproducibility.yml`, `.github/workflows/lint.yml`, `.github/workflows/links.yml` (new)

2. **Add Dependabot configuration**
   - Weekly schedule
   - Python ecosystem
   - File: `.github/dependabot.yml` (new)

3. **Pin dependency versions**
   - Update `requirements.txt` to use `==` instead of `>=`
   - File: `requirements.txt` (update)

### Medium Priority (Documentation)
1. **Create `SECURITY.md`**
   - Vulnerability reporting instructions
   - File: `SECURITY.md` (new)

2. **Create `DISCLOSURE.md`** (canonical)
   - Maturity tag definitions
   - Image role classifications
   - Public disclosure intent
   - File: `DISCLOSURE.md` (new)

3. **Create `PHYLUX_SPINE.md`** (canonical)
   - Repository roles
   - Cross-repo relationships
   - Maturity tagging rules
   - File: `PHYLUX_SPINE.md` (new)

4. **Update `CONTRIBUTING.md`**
   - Already exists
   - Add link to `SECURITY.md`
   - Add "Reproducible Figures" section
   - File: `CONTRIBUTING.md` (update)

5. **Add "Reproducible Figures" section to README**
   - Link to image generation scripts
   - Explain reproducibility culture
   - File: `README.md` (small addition)

### Low Priority (Cleanup)
1. **Clarify file purposes**
   - Document `README ALT.md` or remove if obsolete
   - Document `The Phyllitactic Commons` if important
   - Files: Various (documentation)

---

## E) What I Will NOT Change

**Reproduction Policy:**
- ❌ **NO deletion** of prior art documentation
- ❌ **NO modification** of core demonstration code (except bug fixes)
- ❌ **NO changes** to PPA disclaimers or prior art statements
- ❌ **Image replacement allowed** (per repo policy, if contaminated)

**Additive Only:**
- ✅ Add new files (SECURITY.md, DISCLOSURE.md, PHYLUX_SPINE.md)
- ✅ Add CI/CD automation (new workflows)
- ✅ Update dependency versions (pinning)
- ✅ Add "Reproducible Figures" section to README (small addition)
- ✅ Update CONTRIBUTING.md (add links, sections)

---

## F) Files to be Modified/Created

### New Files
- `SECURITY.md`
- `DISCLOSURE.md`
- `PHYLUX_SPINE.md`
- `.github/dependabot.yml`
- `.github/workflows/reproducibility.yml`
- `.github/workflows/lint.yml`
- `.github/workflows/links.yml`

### Modified Files
- `requirements.txt` (pin versions)
- `CONTRIBUTING.md` (add links, sections)
- `README.md` (add "Reproducible Figures" section)

---

## G) Notes

- All changes will be **additive only** (except dependency pinning, which is a safety improvement)
- No destructive operations
- Image regeneration CI will run scripts in temporary directory (no commits)
- Repository structure and prior art preserved
- PPA alignment maintained

---

**End of Review Pack**
