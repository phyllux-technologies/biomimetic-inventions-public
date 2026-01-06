import numpy as np
import matplotlib.pyplot as plt
import hashlib
import os

os.makedirs('images', exist_ok=True)

def phikey_lattice(N=121):
    phi = (1 + np.sqrt(5)) / 2
    theta = np.arange(1, N+1) * (360 / phi) % 360
    r = np.sqrt(np.arange(1, N+1))
    x = r * np.cos(np.deg2rad(theta))
    y = r * np.sin(np.deg2rad(theta))
    return np.column_stack((x, y))

# Plot lattice
pos = phikey_lattice()
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(pos[:, 0], pos[:, 1], s=40, color='gold', edgecolors='purple', linewidth=0.8)
ax.set_title('PhiKey Lattice Nodes\nGolden-Angle Phyllotactic Growth', fontsize=20)
ax.axis('equal')
ax.axis('off')
plt.tight_layout()
fig.savefig('images/phikey_lattice.png', dpi=300, bbox_inches='tight')
plt.close()
print("Lattice image saved to images/phikey_lattice.png")

# Simple key demo (no full lattice sim – for illustration)
def demo_key(seed='PhiKeySeed2026'):
    h = hashlib.sha3_256(seed.encode()).hexdigest()
    print(f"Demo key from seed '{seed}': {h[:64]}...")

demo_key()
