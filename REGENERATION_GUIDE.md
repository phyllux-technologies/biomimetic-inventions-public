# Image Regeneration Guide

**Quick Start:** Run the PowerShell script or follow the manual steps below.

## Option 1: Automated (Recommended)

Run the PowerShell script:

```powershell
.\regenerate_images.ps1
```

This script will:
1. Check for Python and pip
2. Install dependencies (numpy, matplotlib, scipy)
3. Run all image generation scripts
4. Show you what images were created

## Option 2: Manual Steps

### Step 1: Install Dependencies

Open PowerShell in the repository root and run:

```powershell
# Check Python version
python --version

# If Python is not found, try:
py --version

# Install dependencies
pip install numpy matplotlib scipy

# Or if pip doesn't work:
python -m pip install numpy matplotlib scipy
```

### Step 2: Generate Images

Run these commands in order:

```powershell
# Generate plot images
python generate_plot_images.py

# Generate SVG visualizations
python generate_visualizations.py

# Generate individual images
python PNM-public/src/pnm_public/spiral_utils.py
python PhiKey-public/src/phikey_public/geometric_utils.py
python golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py
python golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py
python golden-angle-antenna-GAFAA-public/src/gafaa_public/phyllotaxis_utils.py
```

### Step 3: Verify Images

Check that images were created:

```powershell
# List images in the images directory
Get-ChildItem images
```

## Troubleshooting

### "Python is not recognized"

**Solution:** Python is not in your PATH.

1. Install Python from https://www.python.org/
2. During installation, check "Add Python to PATH"
3. Restart PowerShell after installation
4. Verify with: `python --version`

### "pip is not recognized"

**Solution:** Use Python module syntax:

```powershell
python -m pip install numpy matplotlib scipy
```

### "ModuleNotFoundError: No module named 'numpy'"

**Solution:** Dependencies not installed. Run:

```powershell
pip install numpy matplotlib scipy
```

Or if that doesn't work:

```powershell
python -m pip install numpy matplotlib scipy
```

### "Permission denied" or "Access denied"

**Solution:** Run PowerShell as Administrator, or use user installation:

```powershell
pip install --user numpy matplotlib scipy
```

### Scripts run but no images appear

**Check:**
1. Look in the `images/` directory in the repository root
2. Check for error messages in the script output
3. Verify the scripts completed without errors

### Unicode/Encoding Errors

If you see encoding errors with emoji characters, the scripts will still work - just ignore those warnings.

## Expected Output

After successful generation, you should have these files in `/images/`:

**PNG Images (12):**
- array_factor_polar.png
- phikey_121_clean.png
- spiral_positions.png
- toy_electrode_array.png
- gafaa_121_clean.png
- gafaa_rf_121_clean.png (if you run 005 script)
- gafaa_multi_freq_121_clean.png (if you run 007 script)
- pnm_121_clean.png (if you run 025 script)
- pnm_crosstalk_121_clean.png (if you run 027 script)
- phyllotaxis-plot.png
- spiral-plot.png
- geometric-plot.png

**SVG Images (3):**
- gafaa-array-layout.svg
- pnm-electrode-array.svg
- phikey-lattice.svg

## Need Help?

If you're still having issues, please share:
1. The exact error message you're seeing
2. Output of `python --version`
3. Output of `pip --version` (or `python -m pip --version`)
