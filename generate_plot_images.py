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
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
    ax.scatter(x, y, s=50, c='red', alpha=0.7, edgecolors='black', linewidths=1)
    ax.plot(x, y, 'b-', alpha=0.3, linewidth=1.0)
    ax.set_xlabel('X position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_title('GAFAA: Phyllotactic Spiral Pattern (121 elements)', fontsize=14, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.4, linewidth=0.8)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'phyllotaxis-plot.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("  ✅ Generated: phyllotaxis-plot.png")
except Exception as e:
    print(f"  ❌ Error: {e}")

# Generate spiral-plot.png (PNM)
print("\nGenerating spiral-plot.png...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(theta) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
    ax.scatter(x, y, s=50, c='blue', alpha=0.7, edgecolors='black', linewidths=1)
    ax.plot(x, y, 'b-', alpha=0.3, linewidth=1.0)
    ax.set_xlabel('X position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_title('PNM: Phyllotactic Spiral Pattern (121 electrodes)', fontsize=14, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.4, linewidth=0.8)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'spiral-plot.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("  ✅ Generated: spiral-plot.png")
except Exception as e:
    print(f"  ❌ Error: {e}")

# Generate geometric-plot.png (Phyllux Vault)
print("\nGenerating geometric-plot.png...")
try:
    N = 121
    golden_angle = 137.508
    theta = np.arange(N) * np.deg2rad(golden_angle)
    r = np.sqrt(np.arange(N)) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
    ax.scatter(x, y, s=50, c='green', alpha=0.7, edgecolors='black', linewidths=1)
    ax.plot(x, y, 'b-', alpha=0.3, linewidth=1.0)
    ax.set_xlabel('X position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y position (arbitrary units)', fontsize=12, fontweight='bold')
    ax.set_title('Phyllux Vault: Geometric Lattice Pattern (121 nodes)', fontsize=14, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.4, linewidth=0.8)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGE_DIR, 'geometric-plot.png'), dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("  ✅ Generated: geometric-plot.png")
except Exception as e:
    print(f"  ❌ Error: {e}")

print("\nPlot image generation complete!")
