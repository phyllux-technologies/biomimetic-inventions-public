import numpy as np
import hashlib

def geokey(N=121, seed=''):
    phi = (1 + np.sqrt(5)) / 2
    theta = np.arange(1, N+1) * (360 / phi) % 360
    r = np.sqrt(np.arange(1, N+1))
    points = str(r * np.cos(np.deg2rad(theta)) + r * np.sin(np.deg2rad(theta)))
    return hashlib.sha256((points + seed).encode()).hexdigest()

print(geokey())
