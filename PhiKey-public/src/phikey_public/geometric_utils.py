"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import numpy as np
import matplotlib.pyplot as plt

def toy_lattice_growth(n_nodes: int, growth_angle_deg: float = 137.508):
    """
    Generic toy lattice growth demo.
    
    Educational only – NOT the real PhiKey algorithm.
    """
    indices = np.arange(n_nodes)
    # Simplified radial + angular growth
    r = np.sqrt(indices)
    theta = np.deg2rad(indices * growth_angle_deg)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return np.column_stack([x, y])


if __name__ == "__main__":
    # Generate 121 nodes
    nodes = toy_lattice_growth(121, growth_angle_deg=137.508)

    # Print results
    print("Number of nodes:", len(nodes))
    print("First 5 node positions (x, y):")
    print(nodes[:5])

    # Plot
    plt.figure(figsize=(8, 8), facecolor='white')
    plt.scatter(nodes[:, 0], nodes[:, 1], s=80, c='green', alpha=0.7, edgecolors='black', linewidths=1.5)
    plt.plot(nodes[:, 0], nodes[:, 1], 'b-', alpha=0.3, linewidth=1.0)
    plt.xlabel('X position', fontsize=12, fontweight='bold')
    plt.ylabel('Y position', fontsize=12, fontweight='bold')
    plt.title('121-Node Lattice Growth (Golden Angle)', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.grid(True, alpha=0.4, linewidth=0.8)
    plt.tight_layout()
    plt.savefig('images/phikey_121_clean.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("\nFigure saved to images/phikey_121_clean.png")
    plt.show()
