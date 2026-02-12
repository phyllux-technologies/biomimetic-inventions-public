"""
Regenerate all images from source scripts.
Outputs all images to /images/ directory.
"""
import os
import sys
import subprocess

# Find repository root
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

print(f"Repository root: {REPO_ROOT}")
print(f"Image output directory: {IMAGE_DIR}")
print("=" * 60)

# Scripts that generate images to /images/
scripts = [
    ('PNM-public/src/pnm_public/spiral_utils.py', 'toy_electrode_array.png'),
    ('PhiKey-public/src/phikey_public/geometric_utils.py', 'phikey_121_clean.png'),
    ('golden-angle-antenna-GAFAA-public/examples/002-phyllux-gafaa-array-factor-polar.py', 'array_factor_polar.png'),
    ('golden-angle-antenna-GAFAA-public/examples/004-phyllux-gafaa-spiral-points-demo.py', 'spiral_positions.png'),
]

print("\nRegenerating PNG images...")
for script_path, expected_image in scripts:
    full_script = os.path.join(REPO_ROOT, script_path)
    if os.path.exists(full_script):
        print(f"\nRunning: {script_path}")
        try:
            result = subprocess.run([sys.executable, full_script], 
                                   cwd=REPO_ROOT, 
                                   capture_output=True, 
                                   text=True,
                                   timeout=60)
            if result.returncode == 0:
                image_path = os.path.join(IMAGE_DIR, expected_image)
                if os.path.exists(image_path):
                    print(f"  [OK] Generated: {expected_image}")
                else:
                    print(f"  [WARN] Script ran but {expected_image} not found")
            else:
                print(f"  [ERROR] {result.stderr}")
        except Exception as e:
            print(f"  [ERROR] Exception: {e}")
    else:
            print(f"  [WARN] Script not found: {full_script}")

# Generate GAFAA image (needs path fix)
print("\nGenerating GAFAA image...")
gafaa_script = os.path.join(REPO_ROOT, 'golden-angle-antenna-GAFAA-public/src/gafaa_public/phyllotaxis_utils.py')
if os.path.exists(gafaa_script):
    try:
        result = subprocess.run([sys.executable, gafaa_script], 
                               cwd=REPO_ROOT, 
                               capture_output=True, 
                               text=True,
                               timeout=60)
        if result.returncode == 0:
            gafaa_image = os.path.join(IMAGE_DIR, 'gafaa_121_clean.png')
            if os.path.exists(gafaa_image):
                print(f"  [OK] Generated: gafaa_121_clean.png")
            else:
                print(f"  [WARN] Script ran but gafaa_121_clean.png not found")
        else:
            print(f"  ❌ Error: {result.stderr}")
    except Exception as e:
        print(f"  ❌ Exception: {e}")

# Generate SVGs using generate_visualizations.py (will modify to save to /images/)
print("\nGenerating SVG images...")
svg_script = os.path.join(REPO_ROOT, 'generate_visualizations.py')
if os.path.exists(svg_script):
    try:
        result = subprocess.run([sys.executable, svg_script], 
                               cwd=REPO_ROOT, 
                               capture_output=True, 
                               text=True,
                               timeout=60)
        if result.returncode == 0:
            print("  [OK] SVG generation completed")
        else:
            print(f"  ❌ Error: {result.stderr}")
    except Exception as e:
        print(f"  ❌ Exception: {e}")

print("\n" + "=" * 60)
print("Image regeneration complete!")
print(f"Check {IMAGE_DIR} for generated images.")
