import numpy as np
import matplotlib.pyplot as plt


def toy_electrode_array(n_electrodes: int, spacing_scale: float = 1.0, angle_deg: float = 137.0):
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
    plt.figure(figsize=(8, 8))
    plt.scatter(positions[:, 0], positions[:, 1], s=100)
    plt.xlabel('X (mm)')
    plt.ylabel('Y (mm)') 
    plt.title('121 Electrodes - Phyllotactic Pattern')
    plt.axis('equal')
    plt.grid(True)
    plt.show()
