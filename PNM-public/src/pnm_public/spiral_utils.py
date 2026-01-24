"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import numpy as np
import matplotlib.pyplot as plt


def toy_electrode_array(n_electrodes: int, spacing_scale: float = 1.0, angle_deg: float = 137.508):
    """
    Generic phyllotactic electrode placement demo.
    
    Educational toy – NOT real PNM geometry.
    """
    indices = np.arange(n_electrodes)
    r = spacing_scale * np.sqrt(indices)
    theta = np.deg2rad(indices * angle_deg)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.column_stack([x, y])


if __name__ == "__main__":
    # Generate 121 electrodes
    positions = toy_electrode_array(121, spacing_scale=0.15, angle_deg=137.508)

    # Print results
    print("Number of electrodes:", len(positions))
    print("First 5 electrode positions (x, y):")
    print(positions[:5])

    # Make plot
    plt.figure(figsize=(8, 8), facecolor='white')
    plt.scatter(positions[:, 0], positions[:, 1], s=100, c='blue', alpha=0.7, edgecolors='black', linewidths=1.5)
    plt.xlabel('X (mm)', fontsize=12, fontweight='bold')
    plt.ylabel('Y (mm)', fontsize=12, fontweight='bold')
    plt.title('121 Electrodes - Phyllotactic Pattern', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.grid(True, alpha=0.4, linewidth=0.8)
    plt.tight_layout()
    plt.savefig('images/pnm_121_clean.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("\nFigure saved to images/pnm_121_clean.png")
    plt.show()
