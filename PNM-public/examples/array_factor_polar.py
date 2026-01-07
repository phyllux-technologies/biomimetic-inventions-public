import numpy as np
import matplotlib.pyplot as plt

def toy_array_factor(n_elements=64, scan_angle=30):
    theta = np.linspace(0, 2*np.pi, 360)
    k = 2*np.pi  # Normalized
    dtheta = np.deg2
