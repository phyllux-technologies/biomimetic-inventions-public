# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Safe IMAGE_DIR - find repository root
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

# Find repository root by looking for README.md or LICENSE.md
REPO_ROOT = SCRIPT_DIR
for _ in range(5):  # Max 5 levels up
    if os.path.exists(os.path.join(REPO_ROOT, 'README.md')) and \
       os.path.exists(os.path.join(REPO_ROOT, 'LICENSE.md')):
        break
    parent = os.path.dirname(REPO_ROOT)
    if parent == REPO_ROOT:  # Reached filesystem root
        REPO_ROOT = SCRIPT_DIR  # Fallback to script directory
        break
    REPO_ROOT = parent

IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)
print(f"Image output directory: {IMAGE_DIR}")

# Section 2: spiral_utils.py
print("Running spiral_utils section...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(theta) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    print("Number of nodes:", N)
    print("First 5 node positions (x, y):")
    print(np.column_stack((x[:5], y[:5])))
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x, y, s=10, c='blue')
    ax.set_title("Spiral Positions (121 nodes)")
    ax.set_xlabel("X Position (arbitrary units)")
    ax.set_ylabel("Y Position (arbitrary units)")
    ax.set_aspect('equal')
    ax.grid(True)
    plt.savefig(os.path.join(IMAGE_DIR, 'spiral_positions.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated: spiral_positions.png")
except Exception as e:
    print(f"Error in spiral_utils: {e}")
