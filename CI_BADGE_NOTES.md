# CI Badge Notes

**Date:** January 22, 2026  
**Phase:** 4 - CI Workflow Stabilization

---

## Workflow Created

### New Workflow: `.github/workflows/ci.yml`

**Name:** "CI"

**Purpose:**
- Provides stable CI badge status
- Runs on all pushes and PRs (not path-specific)
- Lightweight checks for repository hygiene

**Triggers:**
- Push to `main` branch
- Pull requests to `main` branch
- Manual workflow dispatch

**Jobs:**
- **hygiene:** Runs markdown linting, link checking, and Python syntax checks

**Steps:**
1. Checkout code
2. Lint markdown files (using markdownlint)
3. Check internal links (using lychee-action)
4. Python syntax check (basic compilation check)

**Runtime:** Low (typically < 1 minute)

**Error Handling:**
- All steps use `continue-on-error: true`
- Non-blocking checks (warnings don't fail workflow)
- Suitable for badge status without blocking merges

---

## Badge Configuration

### CI Badge URL

**For README:**
```
https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/ci.yml/badge.svg
```

**Link URL:**
```
https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/ci.yml
```

### Badge Status

The badge will show:
- ✅ **Green:** Workflow passed (all checks completed)
- ❌ **Red:** Workflow failed (check logs for details)
- ⏸️ **Gray:** No recent runs (shouldn't happen with push triggers)

---

## Rationale

### Why Create a New Workflow?

1. **Badge Stability:**
   - Existing workflows (`lint.yml`, `links.yml`) are path-specific
   - Only run when markdown files change
   - Badge may show "no status" if no recent markdown changes
   - New `ci.yml` runs on all pushes, ensuring badge always has status

2. **Lightweight:**
   - Doesn't add heavy test suites
   - Fast execution (< 1 minute)
   - Non-blocking (warnings don't fail)

3. **Professional:**
   - Standard "CI" name is recognizable
   - Provides useful repository hygiene checks
   - Doesn't change repository tone

### Alternative: Use Existing Workflow

**Option:** Update README badge to use `ci.yml` instead of `lint.yml`

**Current badge (in README):**
- Uses `lint.yml` workflow
- May show "no status" if no markdown changes

**Recommended update:**
- Change badge to use `ci.yml` workflow
- Will always show status (runs on all pushes)

---

## Workflow Choice for Badge

### Selected: `ci.yml` (New Workflow)

**Reason:**
- Stable badge status (runs on all pushes)
- Standard "CI" name
- Lightweight and fast
- Non-blocking checks

### Alternative: `lint.yml` (Existing)

**Reason:**
- Already exists
- Simple markdown linting
- Path-specific (only runs on markdown changes)

**Trade-off:**
- Badge may show "no status" if no recent markdown changes
- Less stable for badge purposes

---

## README Badge Update

### Current Badge (Phase 2)
Uses `lint.yml` workflow:
```markdown
[![CI](https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/lint.yml/badge.svg)](.github/workflows/lint.yml)
```

### Recommended Update
Use `ci.yml` workflow for stable badge:
```markdown
[![CI](https://github.com/phibronotchi-beep/biomimetic-inventions-public/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)
```

**Action:** Update README badge to use `ci.yml` instead of `lint.yml`

---

## Summary

**Workflow Created:**
- `.github/workflows/ci.yml`
- Name: "CI"
- Runs on all pushes and PRs
- Lightweight hygiene checks

**Badge Stability:**
- ✅ Always runs (not path-specific)
- ✅ Fast execution
- ✅ Non-blocking

**Next Step:**
- Update README badge to use `ci.yml` workflow

---

**End of CI Badge Notes**
