"""
Generate plot images that were previously in docs/assets/.
All images saved to /images/ directory.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Headless
import matplotlib.pyplot as plt

# Find repository root
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

print(f"Generating plot images to: {IMAGE_DIR}")

# Generate phyllotaxis-plot.png (GAFAA)
print("\nGenerating phyllotaxis-plot.png...")
try:
    N = 121
    golden_angle = 137.508
    indices = np.arange(1, N + 1)
    r = np.sqrt(indices) * 0.5
    theta = np.deg2rad(indices * golden_angle)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FAFAFA')
    ax.set_facecolor('#FAFAFA')
    ax.scatter(x, y, s=80, c='#C41E3A', alpha=0.9, edgecolors='#8B0000', linewidths=1.2, zorder=3)
    ax.set_xlabel('X position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_title('GAFAA: Phyllotactic Spiral Pattern (121 elements)', fontsize=13, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.35, linewidth=0.7, color='#CCCCCC')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'phyllotaxis-plot.png'), dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    plt.close()
    print("  [OK] Generated: phyllotaxis-plot.png")
except Exception as e:
    print(f"  [ERROR] Error: {e}")

# Generate spiral-plot.png (PNM)
print("\nGenerating spiral-plot.png...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(theta) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FAFAFA')
    ax.set_facecolor('#FAFAFA')
    ax.scatter(x, y, s=80, c='#0066B3', alpha=0.9, edgecolors='#003366', linewidths=1.2, zorder=3)
    ax.set_xlabel('X position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_title('PNM: Phyllotactic Spiral Pattern (121 electrodes)', fontsize=13, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.35, linewidth=0.7, color='#CCCCCC')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'spiral-plot.png'), dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    plt.close()
    print("  [OK] Generated: spiral-plot.png")
except Exception as e:
    print(f"  [ERROR] Error: {e}")

# Generate geometric-plot.png (Phyllux Vault)
print("\nGenerating geometric-plot.png...")
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
    ax.set_xlabel('X position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=11, fontweight='bold')
    ax.set_title('Phyllux Vault: Geometric Lattice Pattern (121 nodes)', fontsize=13, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.35, linewidth=0.7, color='#CCCCCC')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'geometric-plot.png'), dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    plt.close()
    print("  [OK] Generated: geometric-plot.png")
except Exception as e:
    print(f"  [ERROR] Error: {e}")

print("\nPlot image generation complete!")
