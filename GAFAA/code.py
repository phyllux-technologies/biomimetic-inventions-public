import numpy as np

def gafaa_positions(N=121, lambda_w=0.0107):
    phi = (1 + np.sqrt(5)) / 2
    theta = np.arange(1, N+1) * (360 / phi) % 360
    r = (lambda_w / (2 * np.pi)) * np.sqrt(np.arange(1, N+1))
    x = r * np.cos(np.deg2rad(theta))
    y = r * np.sin(np.deg2rad(theta))
    return np.column_stack((x, y))

pos = gafaa_positions()
print("Sample positions:", pos[:5])
