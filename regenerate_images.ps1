# PowerShell script to regenerate all images
# This script installs dependencies and runs all image generation scripts

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Image Regeneration Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python not found in PATH!" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/" -ForegroundColor Red
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Red
    exit 1
}

# Check if pip is available
Write-Host "Checking pip installation..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    Write-Host "Found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: pip not found!" -ForegroundColor Red
    Write-Host "Trying: python -m pip --version" -ForegroundColor Yellow
    try {
        $pipVersion = python -m pip --version 2>&1
        Write-Host "Found: $pipVersion" -ForegroundColor Green
        $usePipModule = $true
    } catch {
        Write-Host "ERROR: pip is not available!" -ForegroundColor Red
        exit 1
    }
}

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
if ($usePipModule) {
    python -m pip install --upgrade pip
    python -m pip install numpy matplotlib scipy
} else {
    pip install --upgrade pip
    pip install numpy matplotlib scipy
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies!" -ForegroundColor Red
    exit 1
}

Write-Host "Dependencies installed successfully!" -ForegroundColor Green
Write-Host ""

# Run image generation scripts
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Generating Images..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Generate plot images first (simpler)
Write-Host "Step 1: Generating plot images..." -ForegroundColor Yellow
python generate_plot_images.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: generate_plot_images.py failed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 2: Generating SVG visualizations..." -ForegroundColor Yellow
python generate_visualizations.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: generate_visualizations.py failed" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 3: Generating additional images..." -ForegroundColor Yellow
python PNM-public/src/pnm_public/spiral_utils.py
python PhiKey-public/src/phikey_public/geometric_utils.py
python golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py
python golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py
python golden-angle-antenna-GAFAA-public/src/gafaa_public/phyllotaxis_utils.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Checking generated images..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

$imageDir = "images"
if (Test-Path $imageDir) {
    $images = Get-ChildItem -Path $imageDir -File
    Write-Host "Found $($images.Count) images in ${imageDir}:" -ForegroundColor Green
    foreach ($img in $images) {
        Write-Host "  - $($img.Name)" -ForegroundColor White
    }
} else {
    Write-Host "WARNING: ${imageDir} directory not found!" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Image regeneration complete!" -ForegroundColor Green
