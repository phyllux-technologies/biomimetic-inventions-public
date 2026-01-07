import numpy as np

def golden_like_spiral_points(n_points: int,
                              radius_scale: float = 1.0,
                              angle_deg: float = 137.0):
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
