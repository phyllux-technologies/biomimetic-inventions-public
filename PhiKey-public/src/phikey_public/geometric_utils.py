import numpy as np
import matplotlib.pyplot as plt

def toy_lattice_growth(n_nodes: int, growth_angle_deg: float = 137.0):
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
    plt.figure(figsize=(8, 8))
    plt.scatter(nodes[:, 0], nodes[:, 1], s=80, c='green', alpha=0.6)
    plt.plot(nodes[:, 0], nodes[:, 1], 'b-', alpha=0.2, linewidth=0.5)
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('121-Node Lattice Growth (Golden Angle)')
    plt.axis('equal')
    plt.grid(True, alpha=0.3)
    plt.show()
