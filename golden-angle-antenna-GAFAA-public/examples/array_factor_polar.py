import numpy as np
import matplotlib.pyplot as plt
from src.gafaa_public.phyllotaxis_utils import golden_like_spiral_points


def toy_array_factor_polar(n_elements=64, scan_angle_deg=0.0):
    """
    Simplified toy array-factor example in polar coordinates.
    
    Not calibrated to any real frequency, spacing, or claimed design.
    """
    x, y = golden_like_spiral_points(n_elements, radius_scale=0.05, angle_deg=137.0)

    theta = np.linspace(0, 2*np.pi, 360)  # observation angles
    k = 1.0  # arbitrary wavenumber for toy example

    af = np.zeros_like(theta, dtype=complex)
    for (xi, yi) in zip(x, y):
        phase = k * (xi * np.cos(theta) + yi * np.sin(theta))
        af += np.exp(1j * phase)

    af_db = 20 * np.log10(np.abs(af) / np.max(np.abs(af)) + 1e-9)
    return theta, af_db


def main():
    theta, af_db = toy_array_factor_polar()

    # Polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
    ax.plot(theta, af_db)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title("Toy Array Factor (Polar Plot)", pad=20)
    ax.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
