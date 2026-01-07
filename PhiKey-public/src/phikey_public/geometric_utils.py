import numpy as np

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
