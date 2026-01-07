import numpy as np
import matplotlib.pyplot as plt
from src.phikey_public.geometric_utils import toy_lattice_growth

def toy_path_traversal(n_nodes=121):
    """
    Simplified path demo through a lattice.
    NOT a real keystream generator.
    """
    nodes = toy_lattice_growth(n_nodes)
    
    # Toy path: spiral outward
    path_indices = np.arange(n_nodes)
    path = nodes[path_indices]
    
    # "Keystream" = toy hash of positions (educational)
    keystream = (path[:, 0] * 1000 + path[:, 1] * 10000) % 256
    
    return path, keystream.astype(int)

def main():
    path, keystream = toy_path_traversal()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot path
    ax1.plot(path[:, 0], path[:, 1], 'b-', marker='o', markersize=4)
    ax1.set_title("Toy Lattice Path Traversal")
    ax1.axis("equal")
    ax1.grid(True, alpha=0.3)
    
    # Plot "keystream"
    ax2.plot(keystream, 'r.-')
    ax2.set_title("Toy Keystream Sequence")
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Value (0-255)")
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("First 16 keystream bytes:", keystream[:16])

if __name__ == "__main__":
    main()
