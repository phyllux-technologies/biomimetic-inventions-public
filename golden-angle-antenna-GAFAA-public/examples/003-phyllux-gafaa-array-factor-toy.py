"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.
"""
import numpy as np
import matplotlib.pyplot as plt
from src.gafaa_public.phyllotaxis_utils import golden_like_spiral_points

def toy_array_factor(num_elements=64, angle_scan_deg=0.0):
    """
    Extremely simplified toy array-factor example.

    Not calibrated to any real frequency, spacing, or claimed design.
    """
    x, y = golden_like_spiral_points(num_elements, radius_scale=0.05, angle_deg=137.507764)

    theta = np.linspace(-np.pi, np.pi, 721)  # observation angles
    k = 1.0  # arbitrary wavenumber for toy example

    af = np.zeros_like(theta, dtype=complex)
    for (xi, yi) in zip(x, y):
        phase = k * (xi * np.cos(theta) + yi * np.sin(theta))
        af += np.exp(1j * phase)

    af_db = 20 * np.log10(np.abs(af) / np.max(np.abs(af)) + 1e-9)
    return theta, af_db

def main():
    theta, af_db = toy_array_factor()

    plt.plot(np.degrees(theta), af_db)
    plt.xlabel("Angle (deg)")
    plt.ylabel("Normalized |AF| (dB)")
    plt.title("Toy array-factor of a generic spiral layout")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
