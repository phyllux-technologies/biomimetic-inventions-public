# Final Polish Plan

**Date:** January 22, 2026  
**Repository:** biomimetic-inventions-public  
**Purpose:** License detection verification, README badges, Dependabot merge plan

---

## 1. License Detection Analysis

### License-Related Files Found

#### Root Directory

1. **`LICENSE`** (root)
   - **Status:** ✅ Canonical MIT license file
   - **Content:** Pure MIT License text (21 lines, standard format)
   - **GitHub Detection:** Should be detectable as MIT
   - **Last Modified:** Commit 4379f57 (license cleanup)
   - **Issue:** None - file is clean and properly formatted

2. **`LICENSE-IP-NOTICE.md`**
   - **Status:** ✅ Properly named (won't confuse detection)
   - **Content:** Intellectual property notice
   - **GitHub Detection Impact:** None (not named LICENSE.md)
   - **Action:** None needed

3. **`DOCS_LICENSE.md`**
   - **Status:** ✅ Properly named (won't confuse detection)
   - **Content:** CC BY-SA 4.0 license for documentation
   - **GitHub Detection Impact:** None (not named LICENSE.md)
   - **Action:** None needed

4. **`LICENSE_SUMMARY.md`**
   - **Status:** ✅ Properly named (won't confuse detection)
   - **Content:** Human-readable dual licensing guide
   - **GitHub Detection Impact:** None (not named LICENSE.md)
   - **Action:** None needed

5. **`LICENSE_AND_MAINTENANCE_CHECK.md`**
   - **Status:** ✅ Report file (won't confuse detection)
   - **Action:** None needed

6. **`LICENSE_DETECTION_NUDGE_SUMMARY.md`**
   - **Status:** ✅ Report file (won't confuse detection)
   - **Action:** None needed

#### Subproject Directories

7. **`golden-angle-antenna-GAFAA-public/LICENSE`**
   - **Status:** ✅ Subproject license (won't affect root detection)
   - **Action:** None needed

8. **`PNM-public/LICENSE`**
   - **Status:** ✅ Subproject license (won't affect root detection)
   - **Action:** None needed

9. **`PhiKey-public/LICENSE`**
   - **Status:** ✅ Subproject license (won't affect root detection)
   - **Action:** None needed

#### Other License-Related Files

10. **`PATENTS.md`**
    - **Status:** ✅ Not a license file (won't confuse detection)
    - **Action:** None needed

11. **`COPYRIGHT`**
    - **Status:** ✅ Not a license file (won't confuse detection)
    - **Action:** None needed

### License Detection Suspects

**Analysis:** No files found that would confuse GitHub license detection.

- ✅ No `LICENSE.md` file exists (good - would conflict with LICENSE)
- ✅ All license-related files are properly named
- ✅ Root LICENSE file is clean MIT text
- ✅ No conflicting license declarations

**Potential GitHub "Unknown License" Causes:**
1. **Cache delay:** GitHub may cache license detection; recent changes may not be reflected yet
2. **File format:** LICENSE file is correctly formatted (standard MIT)
3. **File naming:** No conflicts detected

**Conclusion:** Repository structure is optimal for license detection. If GitHub still shows "Unknown license," it is likely a caching issue that will resolve within 24-48 hours.

### Proposed File Name Adjustments

**None needed.** All license-related files are properly named and won't interfere with GitHub detection.

---

## 2. Workflow Inventory for CI Badge

### Existing Workflows

1. **`.github/workflows/reproducibility.yml`**
   - **Name:** "Verify Image Reproducibility"
   - **Triggers:** Push/PR on Python files, workflow_dispatch
   - **Stability:** Medium (runs on specific file paths)
   - **Suitable for badge:** No (name not generic, path-specific)

2. **`.github/workflows/lint.yml`**
   - **Name:** "Lint Markdown"
   - **Triggers:** Push/PR on markdown files, workflow_dispatch
   - **Stability:** Medium (runs on markdown files)
   - **Suitable for badge:** Partial (good name, but path-specific)

3. **`.github/workflows/links.yml`**
   - **Name:** "Check Links"
   - **Triggers:** Push/PR on markdown files, workflow_dispatch
   - **Stability:** Medium (runs on markdown files)
   - **Suitable for badge:** Partial (good name, but path-specific)

### CI Badge Strategy

**Option 1 (Recommended):** Use `lint.yml` workflow
- **Workflow file:** `.github/workflows/lint.yml`
- **Workflow name:** "Lint Markdown"
- **Badge URL:** `https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml/badge.svg`
- **Link URL:** `https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml`
- **Pros:** Simple, existing workflow, runs on markdown changes
- **Cons:** Only runs on markdown file changes (may show "no status" if no recent markdown changes)

**Option 2:** Create a lightweight "CI" workflow that runs on all pushes
- **Workflow file:** `.github/workflows/ci.yml` (to be created)
- **Workflow name:** "CI"
- **Triggers:** Push and PR on all files
- **Actions:** Run lint and link checks
- **Pros:** Always runs, stable badge status
- **Cons:** Requires creating new workflow

**Recommendation:** Use Option 1 (lint.yml) for now. If badge stability is an issue, implement Option 2 in Phase 4.

---

## 3. Disclosure Document Identification

### Disclosure Files Found

1. **`DISCLOSURE.md`** (root)
   - **Status:** ✅ Canonical disclosure framework
   - **Content:** Maturity levels, disclosure practices
   - **References:** Links to phyllux-framework/DISCLOSURE.md for canonical framework
   - **Suitable for badge:** ✅ Yes (primary disclosure document)

2. **`INVENTION_DISCLOSURE.md`** (root)
   - **Status:** ✅ High-level invention summary
   - **Content:** Internal-style invention report
   - **Suitable for badge:** No (more technical, less accessible)

**Selected Disclosure File:** `DISCLOSURE.md`
- **Reason:** Primary disclosure framework document
- **Link:** `DISCLOSURE.md` (relative link)
- **Badge text:** "Disclosure" or "Disclosure Framework"

---

## 4. README Structure Analysis

### Current README Structure

```
Line 1:  # Phyllux Biomimetic Inventions – Public Demos
Line 2:  (empty)
Line 3:  Biomimetic multi-domain system fusing phyllotaxis...
Line 4:  (empty)
Line 5:  **Provisional application prepared for filing...**
```

### Badge Insertion Point

**Location:** After line 1 (title), before line 3 (description)

**Proposed structure:**
```
# Phyllux Biomimetic Inventions – Public Demos

[License: MIT](LICENSE) | [CI](.github/workflows/lint.yml) | [Disclosure](DISCLOSURE.md)

Biomimetic multi-domain system fusing phyllotaxis...
```

**Alternative (shields.io badges):**
```
# Phyllux Biomimetic Inventions – Public Demos

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![CI](https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml/badge.svg) [![Disclosure](https://img.shields.io/badge/Disclosure-Framework-green.svg)](DISCLOSURE.md)
```

**Recommendation:** Use simple text links for minimal, professional appearance. Shields.io badges are acceptable if preferred.

---

## 5. Proposed README Badge Strip

### Option A: Simple Text Links (Recommended)

```markdown
[License: MIT](LICENSE) | [CI](.github/workflows/lint.yml) | [Disclosure](DISCLOSURE.md)
```

**Pros:**
- Minimal, professional
- No external dependencies
- Fast rendering
- Works even if GitHub Actions badge is unavailable

**Cons:**
- No visual status indicator for CI

### Option B: Shields.io Badges

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![CI](https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml/badge.svg)](.github/workflows/lint.yml) [![Disclosure](https://img.shields.io/badge/Disclosure-Framework-green.svg)](DISCLOSURE.md)
```

**Pros:**
- Visual status indicators
- Standard GitHub badge format
- CI status visible

**Cons:**
- External dependency (shields.io)
- Slightly more complex

### Selected Option: Option B (Shields.io)

**Rationale:** CI badge provides useful status information. Shields.io is reliable and widely used.

**Exact Markdown:**
```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![CI](https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml/badge.svg)](.github/workflows/lint.yml) [![Disclosure](https://img.shields.io/badge/Disclosure-Framework-green.svg)](DISCLOSURE.md)
```

**Insertion:** After line 1 (title), with blank line before and after.

---

## 6. Dependabot Configuration

### Current Configuration

**File:** `.github/dependabot.yml`

**Ecosystems:**
1. **pip** (Python packages)
   - Directory: `/`
   - Schedule: Weekly
   - PR limit: 5
   - Labels: `dependencies`

2. **github-actions** (GitHub Actions)
   - Directory: `/`
   - Schedule: Weekly
   - PR limit: 3
   - Labels: `dependencies`, `github-actions`

### Dependencies That May Be Updated

#### Python Dependencies (from `requirements.txt`)
- `numpy>=1.21.0`
- `matplotlib>=3.5.0`
- `scipy>=1.7.0`

#### GitHub Actions (from workflows)
- `actions/checkout@v4` (used in all 3 workflows)
- `actions/setup-python@v5` (used in reproducibility.yml)
- `DavidAnson/markdownlint@v0.9.0` (used in lint.yml)
- `lycheeverse/lychee-action@v1.8.0` (used in links.yml)

---

## 7. Dependabot Merge Plan Checklist

### Safe Merge Order

1. **First Priority: actions/checkout**
   - **Why:** Most stable, widely used, backward compatible
   - **Risk:** Very Low
   - **CI Check:** All workflows will test immediately
   - **Action:** Merge if CI green, no changelog review needed for patch/minor

2. **Second Priority: lychee-action (link checker)**
   - **Why:** Link checking is non-critical, updates are usually safe
   - **Risk:** Low
   - **CI Check:** Links workflow will test
   - **Action:** Merge if CI green

3. **Third Priority: markdownlint**
   - **Why:** Linting tool, updates may change rules slightly
   - **Risk:** Low-Medium
   - **CI Check:** Lint workflow will test
   - **Action:** Review changelog if major version, merge if CI green

4. **Fourth Priority: setup-python**
   - **Why:** Python setup action, usually stable
   - **Risk:** Low
   - **CI Check:** Reproducibility workflow will test
   - **Action:** Merge if CI green

5. **Fifth Priority: Python dependencies (numpy, matplotlib, scipy)**
   - **Why:** Scientific libraries, usually backward compatible
   - **Risk:** Low-Medium (version bumps may have subtle changes)
   - **CI Check:** Reproducibility workflow will test scripts
   - **Action:** Review release notes for major versions, merge if CI green

### Manual Merge Checklist (Per PR)

For each Dependabot PR:

- [ ] **Review PR title and description**
  - Confirm what is being updated
  - Check if it's a major, minor, or patch version bump

- [ ] **Check CI status**
  - All workflows should show green/passing
  - If any workflow fails, investigate before merging

- [ ] **Review release notes (for major versions)**
  - Check GitHub releases page for breaking changes
  - Review changelog if available

- [ ] **Merge strategy**
  - **Recommended:** Squash and merge (keeps history clean)
  - **Alternative:** Merge commit (preserves PR history)

- [ ] **After merge**
  - Verify CI still passes on main branch
  - Check if any follow-up actions needed

### Low-Risk PRs (Can Merge Quickly)

- `actions/checkout@v4` → `@v4.x` (patch/minor)
- `lychee-action@v1.8.0` → `@v1.8.x` (patch)
- `markdownlint@v0.9.0` → `@v0.9.x` (patch)
- Python dependencies: patch/minor versions

### Medium-Risk PRs (Review First)

- `actions/checkout@v4` → `@v5` (major version)
- `actions/setup-python@v5` → `@v6` (major version)
- Python dependencies: major version bumps
- Any PR with breaking changes noted in description

---

## 8. Summary

### License Detection
- **Status:** ✅ Optimal structure, no changes needed
- **Expected:** GitHub should detect MIT (may be cached if still showing "Unknown")
- **Action:** None required

### README Badges
- **Location:** After title, before description
- **Badges:** License (MIT), CI (lint.yml), Disclosure (DISCLOSURE.md)
- **Format:** Shields.io badges with relative links

### Dependabot Merge Plan
- **Order:** actions/checkout → lychee-action → markdownlint → setup-python → Python deps
- **Strategy:** Check CI, review major versions, squash merge
- **Risk:** Low for most updates, medium for major versions

### Workflow for CI Badge
- **Selected:** `lint.yml` ("Lint Markdown")
- **Alternative:** Create `ci.yml` if badge stability is an issue

---

**End of Final Polish Plan**

**Next Steps:**
1. Phase 1: License detection fix (if needed) - **No action needed**
2. Phase 2: Add README badges
3. Phase 3: Create Dependabot merge plan document
4. Phase 4: Optional CI workflow stabilization
5. Phase 5: Final report
