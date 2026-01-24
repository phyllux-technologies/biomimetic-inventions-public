"""
Simulation-based; empirical validation required per provisional application prepared for filing (to be filed late January 2026).

Realistic RF analysis of GAFAA antenna array with proper frequency, wavelength, and array factor calculations.
"""

import numpy as np
import matplotlib.pyplot as plt
from src.gafaa_public.rf_utils import (
    phyllotactic_positions,
    array_factor_2d,
    mutual_coupling_matrix,
    grating_lobe_analysis
)

def main():
    # Realistic 5G/6G parameters
    frequency_hz = 28e9  # 28 GHz (mmWave 5G)
    wavelength = 299792458.0 / frequency_hz  # ~10.7 mm
    
    # Array parameters
    n_elements = 121  # Standard GAFAA size
    spacing_factor = 0.5  # Half-wavelength minimum spacing
    
    # Generate positions
    x, y = phyllotactic_positions(n_elements, wavelength, spacing_factor)
    
    # Grating lobe analysis
    grating_analysis = grating_lobe_analysis((x, y), frequency_hz)
    
    print("GAFAA Realistic RF Analysis")
    print("=" * 50)
    print(f"Frequency: {frequency_hz/1e9:.2f} GHz")
    print(f"Wavelength: {wavelength*1000:.2f} mm")
    print(f"Number of elements: {n_elements}")
    print(f"Min spacing: {grating_analysis['min_spacing']*1000:.2f} mm")
    print(f"Max spacing: {grating_analysis['max_spacing']*1000:.2f} mm")
    print(f"Mean spacing: {grating_analysis['mean_spacing']*1000:.2f} mm")
    print(f"Spacing ratio (d/λ): {grating_analysis['spacing_ratio']:.3f}")
    print(f"Grating lobes expected: {grating_analysis['has_grating_lobes']}")
    
    # Array factor calculation (azimuth cut at elevation = 0)
    az_angles = np.linspace(-90, 90, 181)
    el_angles = np.zeros_like(az_angles)
    obs_angles = np.column_stack([az_angles, el_angles])
    
    _, af_db = array_factor_2d((x, y), frequency_hz, 
                               scan_angle_deg=(0.0, 0.0),
                               observation_angles=obs_angles)
    
    # Mutual coupling matrix
    coupling = mutual_coupling_matrix((x, y), frequency_hz)
    
    # Visualization
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    
    # 1. Array layout
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(x*1000, y*1000, s=50, c='red', edgecolors='black', alpha=0.7)
    ax1.set_xlabel('X position (mm)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Y position (mm)', fontsize=11, fontweight='bold')
    ax1.set_title(f'GAFAA Array Layout ({n_elements} elements)', fontsize=12, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.4, linewidth=0.8)
    
    # 2. Array factor
    ax2 = plt.subplot(2, 3, 2)
    ax2.plot(az_angles, af_db, 'b-', linewidth=2.5)
    ax2.set_xlabel('Azimuth Angle (deg)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Array Factor (dB)', fontsize=11, fontweight='bold')
    ax2.set_title('Array Factor (Elevation = 0°)', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.4, linewidth=0.8)
    ax2.set_ylim([-40, 5])
    
    # 3. Mutual coupling magnitude
    ax3 = plt.subplot(2, 3, 3)
    coupling_mag_db = 20 * np.log10(np.abs(coupling) + 1e-10)
    im = ax3.imshow(coupling_mag_db, cmap='hot', aspect='auto', origin='lower')
    ax3.set_xlabel('Element Index', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Element Index', fontsize=11, fontweight='bold')
    ax3.set_title('Mutual Coupling Matrix (dB)', fontsize=12, fontweight='bold')
    plt.colorbar(im, ax=ax3, label='Coupling (dB)')
    
    # 4. Spacing distribution
    ax4 = plt.subplot(2, 3, 4)
    positions_2d = np.column_stack([x, y])
    distances = []
    for i in range(len(positions_2d)):
        for j in range(i + 1, len(positions_2d)):
            dist = np.linalg.norm(positions_2d[i] - positions_2d[j])
            distances.append(dist * 1000)  # Convert to mm
    ax4.hist(distances, bins=50, edgecolor='black', alpha=0.7)
    ax4.axvline(wavelength * 1000, color='r', linestyle='--', label=f'λ = {wavelength*1000:.2f} mm')
    ax4.set_xlabel('Element Spacing (mm)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Count', fontsize=11, fontweight='bold')
    ax4.set_title('Spacing Distribution', fontsize=12, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.4, linewidth=0.8)
    
    # 5. Polar array factor
    ax5 = plt.subplot(2, 3, 5, projection='polar')
    theta_rad = np.deg2rad(az_angles)
    ax5.plot(theta_rad, af_db, 'b-', linewidth=2.5)
    ax5.set_theta_zero_location('N')
    ax5.set_theta_direction(-1)
    ax5.set_ylim([-40, 5])
    ax5.set_title('Array Factor (Polar)', pad=20)
    
    # 6. Grating lobe analysis
    ax6 = plt.subplot(2, 3, 6)
    ax6.text(0.1, 0.8, f"Grating Lobe Analysis", fontsize=14, weight='bold', transform=ax6.transAxes)
    ax6.text(0.1, 0.7, f"Critical spacing: {grating_analysis['critical_spacing']*1000:.2f} mm", 
             transform=ax6.transAxes)
    ax6.text(0.1, 0.6, f"Max spacing: {grating_analysis['max_spacing']*1000:.2f} mm", 
             transform=ax6.transAxes)
    ax6.text(0.1, 0.5, f"Grating lobes: {'Yes' if grating_analysis['has_grating_lobes'] else 'No'}", 
             transform=ax6.transAxes, 
             color='red' if grating_analysis['has_grating_lobes'] else 'green')
    ax6.text(0.1, 0.4, f"Spacing ratio: {grating_analysis['spacing_ratio']:.3f}λ", 
             transform=ax6.transAxes)
    ax6.axis('off')
    
    plt.tight_layout()
    # Find repository root for proper path
    import os
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    REPO_ROOT = SCRIPT_DIR
    for _ in range(5):
        if os.path.exists(os.path.join(REPO_ROOT, 'README.md')) and \
           os.path.exists(os.path.join(REPO_ROOT, 'LICENSE')):
            break
        parent = os.path.dirname(REPO_ROOT)
        if parent == REPO_ROOT:
            REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
            break
        REPO_ROOT = parent
    IMAGE_DIR = os.path.join(REPO_ROOT, 'images')
    os.makedirs(IMAGE_DIR, exist_ok=True)
    image_path = os.path.join(IMAGE_DIR, 'gafaa_rf_121_clean.png')
    plt.savefig(image_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\nAnalysis complete. Figure saved as '{image_path}'")
    plt.close()

if __name__ == "__main__":
    main()
