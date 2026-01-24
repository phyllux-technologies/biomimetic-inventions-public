# License Detection Fix Plan

**Date:** January 22, 2026  
**Repository:** biomimetic-inventions-public  
**Purpose:** Ensure GitHub reliably detects MIT license

---

## Phase 1 — Diagnosis

### 1. LICENSE File Status

**File:** `LICENSE` (root directory)

**Content:** ✅ Standard MIT License text only
- 21 lines of pure MIT License text
- No appended IP notice or extra content
- Properly formatted with trailing newline
- Copyright: 2026 David Edward Sproule

**Status:** ✅ Optimal for GitHub detection

---

### 2. LICENSE.md File Status

**File:** `LICENSE.md`

**Exists:** ❌ **NO** - File does not exist

**Previous Status:** 
- According to historical reports, `LICENSE.md` was previously deleted
- Content was moved to `LICENSE-IP-NOTICE.md` in commit 4379f57
- File was properly renamed to avoid license detection conflicts

**Current Status:** ✅ No action needed - file does not exist

---

### 3. References to LICENSE.md

**Found:** 3 Python scripts reference `LICENSE.md` in path detection code

**Files:**
1. `golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py` (line 19)
2. `golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py` (line 19)
3. `golden-angle-antenna-GAFAA-public/examples/005-phyllux-gafaa-realistic-rf-analysis.py` (line 130)

**Current Behavior:**
- Scripts check for `LICENSE.md` as repository root marker
- Since file doesn't exist, scripts fall back to checking for `LICENSE` (which exists)
- Scripts still work correctly, but reference is inaccurate

**Impact on License Detection:** None (doesn't affect GitHub detection)

**Action Required:** Update scripts to check for `LICENSE` instead of `LICENSE.md` for accuracy

---

## Phase 2 — Fix Plan

### No LICENSE.md to Rename

Since `LICENSE.md` does not exist, there is nothing to rename.

### Required Actions

1. **Update Python Script References**
   - Change `LICENSE.md` references to `LICENSE` in 3 Python scripts
   - This improves accuracy but doesn't affect license detection
   - Scripts will directly check for `LICENSE` instead of falling back

### Files to Update

1. `golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py`
   - Line 19: Change `'LICENSE.md'` to `'LICENSE'`

2. `golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py`
   - Line 19: Change `'LICENSE.md'` to `'LICENSE'`

3. `golden-angle-antenna-GAFAA-public/examples/005-phyllux-gafaa-realistic-rf-analysis.py`
   - Line 130: Change `'LICENSE.md'` to `'LICENSE'`

---

## Phase 3 — Verification Plan

### Verification Steps

1. **Confirm no LICENSE.md exists**
   - ✅ Already verified: File does not exist
   - ✅ No LICENSE.md in root directory
   - ✅ No LICENSE.md in subdirectories

2. **Confirm canonical LICENSE file**
   - ✅ LICENSE exists in root
   - ✅ Contains pure MIT text
   - ✅ No conflicting files

3. **Confirm README links**
   - ✅ README "Licensing" section links to:
     - `LICENSE` (MIT for code)
     - `DOCS_LICENSE.md` (CC BY-SA 4.0 for docs)
     - `LICENSE-IP-NOTICE.md` (IP notice)
     - `LICENSE_SUMMARY.md` (summary)

4. **Update Python script references**
   - Update 3 scripts to use `LICENSE` instead of `LICENSE.md`
   - Verify scripts still work correctly

---

## Summary

### Current State

- ✅ LICENSE file: Clean MIT text, optimal for detection
- ✅ LICENSE.md: Does not exist (good - no conflicts)
- ✅ README links: Correctly point to LICENSE and related files
- ⚠️ Python scripts: Reference non-existent LICENSE.md (should be updated)

### Required Changes

**Minimal changes needed:**
- Update 3 Python scripts to reference `LICENSE` instead of `LICENSE.md`
- This is a code accuracy improvement, not a license detection fix

### Why GitHub Should Detect MIT

1. **Single canonical file:** Only `LICENSE` exists (no `LICENSE.md`)
2. **Clean MIT text:** Standard format, no appended content
3. **Proper structure:** IP notice separated, won't interfere

**Expected Result:** GitHub should detect MIT License (may take 24-48 hours if cached)

---

**End of License Detection Fix Plan**
