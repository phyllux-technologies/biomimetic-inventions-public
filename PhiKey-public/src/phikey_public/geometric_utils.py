# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Safe IMAGE_DIR
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()
IMAGE_DIR = r"D:\Phyllux Project\biomimetic-inventions-public\images"
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
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x, y, s=10, c='green', alpha=0.7)
    ax.plot(x, y, color='blue', linewidth=0.5, alpha=0.5)
    ax.set_title("121-Node Lattice Growth (Golden Angle)")
    ax.set_xlabel("X Position (arbitrary units)")
    ax.set_ylabel("Y Position (arbitrary units)")
    ax.set_aspect('equal')
    ax.grid(True)
    plt.savefig(os.path.join(IMAGE_DIR, 'phikey_121_clean.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated: phikey_121_clean.png")
except Exception as e:
    print(f"Error in geometric_utils: {e}")
