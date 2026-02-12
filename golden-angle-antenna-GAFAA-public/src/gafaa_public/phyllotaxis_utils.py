"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).
"""
import numpy as np
import matplotlib.pyplot as plt

def golden_like_spiral_points(n_points: int,
                              radius_scale: float = 1.0,
                              angle_deg: float = 137.508):
    """
    Generate a simple phyllotactic-style spiral point set.
    This is a generic educational function. It is NOT a production
    GAFAA design and is intentionally simplified.
    """
    indices = np.arange(n_points)
    # Simple sqrt radial growth
    r = radius_scale * np.sqrt(indices)
    theta = np.deg2rad(indices * angle_deg)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


if __name__ == "__main__":
    # Generate 121 antenna positions for GAFAA
    x, y = golden_like_spiral_points(121, radius_scale=1.07, angle_deg=137.508)

    # Print results
    print("Number of antenna elements:", len(x))
    print("First 5 positions:")
    for i in range(5):
        print(f"  Element {i+1}: x={x[i]:.3f}, y={y[i]:.3f}")

    # Plot
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#FAFAFA')
    ax.set_facecolor('#FAFAFA')
    ax.scatter(x, y, s=100, c='#C41E3A', alpha=0.9, edgecolors='#8B0000', linewidths=1.2, zorder=3)
    ax.set_xlabel('X position (mm)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Y position (mm)', fontsize=11, fontweight='bold')
    ax.set_title('GAFAA: 121 Antenna Elements (Golden Angle Spiral)', fontsize=13, fontweight='bold')
    ax.axis('equal')
    ax.grid(True, alpha=0.35, linewidth=0.7, color='#CCCCCC')
    plt.tight_layout()
    # Find biomimetic-inventions-public root (has images/ and generate_plot_images.py)
    import os
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
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
    image_path = os.path.join(IMAGE_DIR, 'gafaa_121_clean.png')
    plt.savefig(image_path, dpi=300, bbox_inches='tight', facecolor='#FAFAFA')
    print(f"\nFigure saved to {image_path}")
    plt.close()
