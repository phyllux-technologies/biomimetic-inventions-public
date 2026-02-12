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
for _ in range(6):
    if os.path.exists(os.path.join(REPO_ROOT, 'images')) and \
       os.path.exists(os.path.join(REPO_ROOT, 'generate_plot_images.py')):
        break
    parent = os.path.dirname(REPO_ROOT)
    if parent == REPO_ROOT:
        REPO_ROOT = SCRIPT_DIR
        break
    REPO_ROOT = parent

IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)
print(f"Image output directory: {IMAGE_DIR}")

# Section 4: geometric_utils.py
print("Running geometric_utils section...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(np.arange(N)) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FAFAFA')
    ax.set_facecolor('#FAFAFA')
    ax.scatter(x, y, s=80, c='#2E7D32', alpha=0.9, edgecolors='#1B5E20', linewidths=1.2, zorder=3)
    ax.plot(x, y, color='#0066B3', linewidth=1.0, alpha=0.2, zorder=1)
    ax.set_title("121-Node Lattice Growth (Golden Angle)", fontsize=13, fontweight='bold')
    ax.set_xlabel("X Position (arbitrary units)", fontsize=11, fontweight='bold')
    ax.set_ylabel("Y Position (arbitrary units)", fontsize=11, fontweight='bold')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.35, linewidth=0.7, color='#CCCCCC')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'phikey_121_clean.png'), dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    plt.close(fig)
    print("Generated: phikey_121_clean.png")
except Exception as e:
    print(f"Error in geometric_utils: {e}")
