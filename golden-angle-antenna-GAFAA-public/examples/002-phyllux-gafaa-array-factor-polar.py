# To use: Run this script to generate the image. Output saves to 'images/' relative to this file. Install requirements: pip install numpy matplotlib.
"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).
"""
import os
import numpy as np
import matplotlib.pyplot as plt

# Safe IMAGE_DIR - find repository root
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

# Find repository root by looking for README.md or LICENSE
REPO_ROOT = SCRIPT_DIR
for _ in range(5):  # Max 5 levels up
    if os.path.exists(os.path.join(REPO_ROOT, 'README.md')) and \
       os.path.exists(os.path.join(REPO_ROOT, 'LICENSE')):
        break
    parent = os.path.dirname(REPO_ROOT)
    if parent == REPO_ROOT:  # Reached filesystem root
        REPO_ROOT = SCRIPT_DIR  # Fallback to script directory
        break
    REPO_ROOT = parent

IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)
print(f"Image output directory: {IMAGE_DIR}")

# Section 1: array_factor_polar.py
print("Running array_factor_polar section...")
try:
    f = 28e9
    c = 3e8
    lambda_ = c / f
    N = 121
    theta = np.linspace(0, 10 * np.pi, N)
    r = np.sqrt(theta) * 0.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    positions = np.column_stack((x, y))
    theta_grid, phi_grid = np.mgrid[0:np.pi:50j, 0:2*np.pi:50j]
    k = 2 * np.pi / lambda_
    phase = k * (positions[:, 0, np.newaxis, np.newaxis] * np.sin(theta_grid) * np.cos(phi_grid) +
                 positions[:, 1, np.newaxis, np.newaxis] * np.sin(theta_grid) * np.sin(phi_grid))
    AF = np.sum(np.exp(1j * phase), axis=0) / N
    AF_dB = 20 * np.log10(np.abs(AF) + 1e-10)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='polar')
    contour = ax.contourf(phi_grid, theta_grid * (180/np.pi), AF_dB, levels=30, cmap='viridis')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title("Array Factor Polar Plot (dB)")
    fig.colorbar(contour)
    plt.savefig(os.path.join(IMAGE_DIR, 'array_factor_polar.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)
    print("Generated: array_factor_polar.png")
except Exception as e:
    print(f"Error in array_factor_polar: {e}")
