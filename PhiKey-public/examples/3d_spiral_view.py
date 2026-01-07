import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def helical_spiral(n_points=200, turns=5):
    theta = np.linspace(0, turns*2*np.pi, n_points)
    r = np.sqrt(np.arange(n_points))
    z = theta / (2*np.pi)  # Helical rise
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, z

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
x, y, z = helical_spiral()
ax.scatter(x, y, z, c=z, cmap='viridis', s=20)
ax.set_title("Toy 3D Helical Antenna Array")
plt.show()
