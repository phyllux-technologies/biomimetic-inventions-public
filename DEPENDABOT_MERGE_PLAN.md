# Dependabot Merge Plan

**Date:** January 22, 2026  
**Repository:** biomimetic-inventions-public  
**Purpose:** Safe merge strategy for Dependabot PRs

---

## Dependabot Configuration

### Location
- **File:** `.github/dependabot.yml`
- **Version:** 2

### Ecosystems Covered

1. **pip** (Python packages)
   - **Directory:** `/`
   - **Schedule:** Weekly
   - **Open PR limit:** 5
   - **Labels:** `dependencies`
   - **Commit prefix:** `deps`

2. **github-actions** (GitHub Actions)
   - **Directory:** `/`
   - **Schedule:** Weekly
   - **Open PR limit:** 3
   - **Labels:** `dependencies`, `github-actions`

---

## Dependencies That May Be Updated

### Python Dependencies

From `requirements.txt`:
- `numpy>=1.21.0`
- `matplotlib>=3.5.0`
- `scipy>=1.7.0`

### GitHub Actions

From workflows:
- `actions/checkout@v4` (used in all 3 workflows)
- `actions/setup-python@v5` (used in `.github/workflows/reproducibility.yml`)
- `DavidAnson/markdownlint@v0.9.0` (used in `.github/workflows/lint.yml`)
- `lycheeverse/lychee-action@v1.8.0` (used in `.github/workflows/links.yml`)

---

## Safe Merge Order

### Priority 1: actions/checkout

**Why first:**
- Most stable and widely used action
- Excellent backward compatibility
- Used in all workflows (high confidence in testing)
- Rarely has breaking changes

**Risk Level:** Very Low

**CI Coverage:**
- All 3 workflows use this action
- Will test immediately on merge

**Merge Criteria:**
- ✅ CI green
- ✅ No changelog review needed for patch/minor versions
- ✅ Review changelog for major version bumps (v4 → v5)

**Example PRs:**
- `actions/checkout@v4` → `@v4.1` (safe, merge quickly)
- `actions/checkout@v4` → `@v5` (review changelog first)

---

### Priority 2: lychee-action (Link Checker)

**Why second:**
- Link checking is non-critical (workflow uses `continue-on-error: true`)
- Updates are usually safe and backward compatible
- Low impact if something breaks

**Risk Level:** Low

**CI Coverage:**
- `.github/workflows/links.yml` will test
- Workflow won't block on failures

**Merge Criteria:**
- ✅ CI green (or yellow with warnings)
- ✅ No special review needed for patch/minor

**Example PRs:**
- `lycheeverse/lychee-action@v1.8.0` → `@v1.8.1` (safe, merge quickly)
- `lycheeverse/lychee-action@v1.8.0` → `@v2.0.0` (review changelog)

---

### Priority 3: markdownlint

**Why third:**
- Linting tool updates may change rules slightly
- Could affect markdown file validation
- Usually safe but worth checking

**Risk Level:** Low-Medium

**CI Coverage:**
- `.github/workflows/lint.yml` will test
- Workflow uses `continue-on-error: true`

**Merge Criteria:**
- ✅ CI green
- ✅ Review changelog if major version bump
- ✅ Check if linting rules changed

**Example PRs:**
- `DavidAnson/markdownlint@v0.9.0` → `@v0.9.1` (safe, merge quickly)
- `DavidAnson/markdownlint@v0.9.0` → `@v1.0.0` (review changelog, check rule changes)

---

### Priority 4: setup-python

**Why fourth:**
- Python setup action is usually stable
- Used in reproducibility workflow
- Important for Python script execution

**Risk Level:** Low

**CI Coverage:**
- `.github/workflows/reproducibility.yml` will test
- Will verify Python environment setup

**Merge Criteria:**
- ✅ CI green
- ✅ Review changelog for major version bumps

**Example PRs:**
- `actions/setup-python@v5` → `@v5.1` (safe, merge quickly)
- `actions/setup-python@v5` → `@v6` (review changelog)

---

### Priority 5: Python Dependencies (numpy, matplotlib, scipy)

**Why last:**
- Scientific libraries are usually backward compatible
- But version bumps may have subtle behavior changes
- Scripts may need updates for major versions

**Risk Level:** Low-Medium

**CI Coverage:**
- `.github/workflows/reproducibility.yml` will test scripts
- Will verify image generation still works

**Merge Criteria:**
- ✅ CI green
- ✅ Review release notes for major versions
- ✅ Check for deprecation warnings in CI logs

**Example PRs:**
- `numpy>=1.21.0` → `numpy>=1.24.0` (minor bump, usually safe)
- `numpy>=1.21.0` → `numpy>=2.0.0` (major bump, review release notes)

---

## Manual Merge Checklist

For each Dependabot PR, follow this checklist:

### Pre-Merge Review

- [ ] **Review PR title and description**
  - Confirm what dependency is being updated
  - Check version type (major/minor/patch)
  - Read Dependabot's description of changes

- [ ] **Check CI status**
  - All workflows should show green/passing
  - If any workflow fails, investigate the failure
  - Check CI logs for warnings or errors

- [ ] **Review release notes (for major versions)**
  - Visit the dependency's GitHub releases page
  - Check for breaking changes
  - Review changelog if available
  - Look for deprecation notices

- [ ] **Check PR labels**
  - Should have `dependencies` label
  - May have `github-actions` label for action updates

### Merge Strategy

**Recommended:** Squash and merge
- Keeps commit history clean
- Single commit per dependency update
- Easy to revert if needed

**Alternative:** Merge commit
- Preserves PR history
- Shows individual PRs in history

**Do NOT use:** Rebase and merge
- Can cause issues with Dependabot branches

### Post-Merge Verification

- [ ] **Verify CI still passes on main branch**
  - Check Actions tab after merge
  - Ensure all workflows complete successfully

- [ ] **Check for follow-up actions**
  - Review any comments Dependabot left
  - Check if any manual updates needed

---

## Low-Risk PRs (Can Merge Quickly)

These PRs can typically be merged with minimal review:

- `actions/checkout@v4` → `@v4.x` (patch/minor versions)
- `lychee-action@v1.8.0` → `@v1.8.x` (patch versions)
- `markdownlint@v0.9.0` → `@v0.9.x` (patch versions)
- `setup-python@v5` → `@v5.x` (patch/minor versions)
- Python dependencies: patch/minor version bumps

**Criteria for quick merge:**
- CI is green
- No breaking changes mentioned in PR description
- Patch or minor version bump

---

## Medium-Risk PRs (Review First)

These PRs require more careful review:

- `actions/checkout@v4` → `@v5` (major version)
- `actions/setup-python@v5` → `@v6` (major version)
- `lychee-action@v1.8.0` → `@v2.0.0` (major version)
- `markdownlint@v0.9.0` → `@v1.0.0` (major version)
- Python dependencies: major version bumps (e.g., `numpy>=1.21.0` → `numpy>=2.0.0`)

**Review checklist:**
- [ ] Read full changelog/release notes
- [ ] Check for breaking changes
- [ ] Verify CI passes
- [ ] Test locally if possible (for Python deps)
- [ ] Check for deprecation warnings

---

## How to Merge on GitHub UI

### Step-by-Step Process

1. **Navigate to PRs**
   - Go to: https://github.com/phibronotchi-beep/biomimetic-inventions-public/pulls
   - Filter by: "dependabot" or label "dependencies"

2. **Open the PR**
   - Click on the PR title
   - Review the changes tab
   - Check the "Files changed" tab

3. **Review CI Status**
   - Look for green checkmarks on the PR
   - Click "Details" on any workflow to see logs
   - Ensure all checks pass

4. **Review Changes**
   - Check what files are being updated
   - Verify version numbers look correct
   - Read Dependabot's description

5. **Merge the PR**
   - Scroll to bottom of PR page
   - Click dropdown next to "Merge pull request"
   - Select "Squash and merge" (recommended)
   - Click "Squash and merge" button
   - Confirm merge

6. **Verify After Merge**
   - Check Actions tab to ensure workflows run
   - Verify main branch CI is green

---

## Why These Updates Matter

### Supply Chain Security
- **Vulnerability fixes:** Dependabot updates often include security patches
- **Known vulnerabilities:** GitHub alerts for known CVEs
- **Dependency freshness:** Keeping dependencies current reduces attack surface

### Maintenance Hygiene
- **Bug fixes:** Updates include bug fixes and improvements
- **Performance:** Newer versions may have performance improvements
- **Compatibility:** Staying current helps with future compatibility

### CI/CD Reliability
- **Action updates:** Keep GitHub Actions current for reliability
- **Feature access:** Newer actions may have useful features
- **Deprecation avoidance:** Avoid using deprecated action versions

---

## Troubleshooting

### If CI Fails After Merge

1. **Check CI logs**
   - Go to Actions tab
   - Find the failed workflow
   - Review error messages

2. **Common issues:**
   - **Breaking changes:** New version may have changed behavior
   - **Deprecated APIs:** Scripts may need updates
   - **Configuration changes:** Action may need new parameters

3. **Resolution:**
   - Revert the merge if critical
   - Update code to match new version requirements
   - Or pin to previous version temporarily

### If Multiple PRs Conflict

1. **Merge in priority order** (see Safe Merge Order above)
2. **Resolve conflicts** if they occur
3. **Merge one at a time** to avoid cascading issues

---

## Summary

**Merge Order:**
1. actions/checkout (very low risk)
2. lychee-action (low risk)
3. markdownlint (low-medium risk)
4. setup-python (low risk)
5. Python dependencies (low-medium risk)

**General Rule:**
- Patch/minor versions: Merge if CI green
- Major versions: Review changelog, then merge if CI green

**Always:**
- Check CI status
- Use squash and merge
- Verify post-merge CI

---

**End of Dependabot Merge Plan**
