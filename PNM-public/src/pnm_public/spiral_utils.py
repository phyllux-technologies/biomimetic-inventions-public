# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Safe IMAGE_DIR - find repository root
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

# Find biomimetic-inventions-public root (has images/ and generate_plot_images.py)
REPO_ROOT = SCRIPT_DIR
for _ in range(6):  # Up to biomimetic-inventions-public root
    has_images = os.path.exists(os.path.join(REPO_ROOT, 'images'))
    has_generate = os.path.exists(os.path.join(REPO_ROOT, 'generate_plot_images.py'))
    if has_images and has_generate:
        break
    parent = os.path.dirname(REPO_ROOT)
    if parent == REPO_ROOT:
        REPO_ROOT = SCRIPT_DIR
        break
    REPO_ROOT = parent
IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)
print(f"Image output directory: {IMAGE_DIR}")

# Section 3: toy_electrode_array.py
print("Running toy_electrode_array section...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(theta)
    fig = plt.figure(figsize=(8, 8), facecolor='#FAFAFA')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#FAFAFA')
    ax.scatter(theta, r, s=45, c='#0066B3', alpha=0.9, edgecolors='#003366', linewidths=0.8)
    ax.set_rlim(0, r.max() * 1.05)
    ax.set_title("PNM Phyllotactic Electrode Array (121 electrodes)", fontsize=12, fontweight='bold')
    fig.suptitle("Golden Angle ~137.508° Pattern for Neural Interfaces", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'toy_electrode_array.png'), dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    plt.close(fig)
    print("Generated: toy_electrode_array.png")
except Exception as e:
    print(f"Error in toy_electrode_array: {e}")
