"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Script to generate SVG visualizations for GitHub display.
"""

import sys
import os
import numpy as np

# Add paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'golden-angle-antenna-GAFAA-public'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'PNM-public'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'PhiKey-public'))

from src.gafaa_public.rf_utils import phyllotactic_positions
from src.gafaa_public.svg_utils import generate_array_svg
from src.pnm_public.neural_utils import phyllotactic_electrode_positions, coverage_area
from src.pnm_public.svg_utils import generate_electrode_array_svg
from src.phikey_public.geometric_utils import toy_lattice_growth
from src.phikey_public.geometric_utils import toy_lattice_growth as phikey_lattice

def generate_gafaa_svg():
    """Generate GAFAA antenna array SVG."""
    frequency_hz = 28e9  # 28 GHz
    wavelength = 299792458.0 / frequency_hz
    n_elements = 121
    spacing_factor = 0.5
    
    x, y = phyllotactic_positions(n_elements, wavelength, spacing_factor)
    
    # Color gradient based on radial distance
    r = np.sqrt(x**2 + y**2)
    r_norm = (r - np.min(r)) / (np.max(r) - np.min(r))
    colors = []
    for r_val in r_norm:
        blue = int(0x00 + (0xFF - 0x00) * r_val)
        green = int(0x66 + (0x00 - 0x66) * r_val)
        red = int(0xCC + (0x00 - 0xCC) * r_val)
        colors.append(f"#{red:02X}{green:02X}{blue:02X}")
    
    # Save to /images/ directory
    REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
    IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
    os.makedirs(IMAGE_DIR, exist_ok=True)
    filename = os.path.join(IMAGE_DIR, 'gafaa-array-layout.svg')
    generate_array_svg((x, y), filename, element_size=3.0, width=1000, height=1000, colors=colors)
    print(f"Generated: {filename}")

def generate_pnm_svg():
    """Generate PNM electrode array SVG."""
    n_electrodes = 121
    electrode_diameter_um = 50.0
    min_spacing_um = 200.0
    
    x, y = phyllotactic_electrode_positions(n_electrodes, electrode_diameter_um, min_spacing_um)
    coverage = coverage_area((x, y), electrode_diameter_um)
    
    # Color gradient
    r = np.sqrt(x**2 + y**2)
    r_norm = (r - np.min(r)) / (np.max(r) - np.min(r))
    colors = []
    for r_val in r_norm:
        red = int(0xAD + (0x00 - 0xAD) * r_val)
        green = int(0xD8 + (0x00 - 0xD8) * r_val)
        blue = int(0xE6 + (0x8B - 0xE6) * r_val)
        colors.append(f"#{red:02X}{green:02X}{blue:02X}")
    
    # Save to /images/ directory
    REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
    IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
    os.makedirs(IMAGE_DIR, exist_ok=True)
    filename = os.path.join(IMAGE_DIR, 'pnm-electrode-array.svg')
    generate_electrode_array_svg(
        (x, y), filename, electrode_diameter_um=electrode_diameter_um,
        width=1000, height=1000, colors=colors,
        show_coverage=True, coverage_radius_um=coverage['coverage_radius_um']
    )
    print(f"Generated: {filename}")

def generate_phikey_svg():
    """Generate PhiKey lattice SVG."""
    n_nodes = 121
    nodes = toy_lattice_growth(n_nodes, growth_angle_deg=137.508)
    x, y = nodes[:, 0], nodes[:, 1]
    
    # Color gradient
    r = np.sqrt(x**2 + y**2)
    r_norm = (r - np.min(r)) / (np.max(r) - np.min(r))
    colors = []
    for r_val in r_norm:
        red = int(0x00 + (0xFF - 0x00) * r_val)
        green = int(0x80 + (0x00 - 0x80) * r_val)
        blue = int(0xFF + (0x00 - 0xFF) * r_val)
        colors.append(f"#{red:02X}{green:02X}{blue:02X}")
    
    # Generate SVG manually for PhiKey
    x_norm = x - np.min(x)
    y_norm = y - np.min(y)
    max_dim = max(np.max(x_norm), np.max(y_norm))
    margin = 50
    width, height = 1000, 1000
    scale = min((width - 2*margin) / max_dim, (height - 2*margin) / max_dim)
    x_svg = x_norm * scale + margin
    y_svg = y_norm * scale + margin
    
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .node {{ stroke: #000000; stroke-width: 1; }}
      .spiral {{ stroke: #0066CC; stroke-width: 0.5; fill: none; opacity: 0.3; }}
    </style>
  </defs>
  <rect width="{width}" height="{height}" fill="#FFFFFF"/>
  <path class="spiral" d="M {x_svg[0]:.2f},{y_svg[0]:.2f} {' '.join([f'L {x_svg[i]:.2f},{y_svg[i]:.2f}' for i in range(1, n_nodes)])}"/>
'''
    for i in range(n_nodes):
        svg_content += f'  <circle class="node" cx="{x_svg[i]:.2f}" cy="{y_svg[i]:.2f}" r="3.0" fill="{colors[i]}"/>\n'
    
    svg_content += f'''
  <text x="{width/2}" y="30" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold">
    Phyllux Vault Geometric Lattice ({n_nodes} nodes)
  </text>
</svg>
'''
    
    # Save to /images/ directory
    REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
    IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
    os.makedirs(IMAGE_DIR, exist_ok=True)
    filename = os.path.join(IMAGE_DIR, 'phikey-lattice.svg')
    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Generated: {filename}")

if __name__ == "__main__":
    print("Generating SVG visualizations...")
    generate_gafaa_svg()
    generate_pnm_svg()
    generate_phikey_svg()
    print("All visualizations generated!")
