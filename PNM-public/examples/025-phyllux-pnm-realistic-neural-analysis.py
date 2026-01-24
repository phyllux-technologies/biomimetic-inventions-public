"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Realistic neural interface analysis of PNM electrode array with proper crosstalk and coverage calculations.
"""

import numpy as np
import matplotlib.pyplot as plt
from src.pnm_public.neural_utils import (
    phyllotactic_electrode_positions,
    crosstalk_matrix,
    signal_to_crosstalk_ratio,
    coverage_area
)

def main():
    # Realistic neural interface parameters
    n_electrodes = 121  # Standard PNM size
    electrode_diameter_um = 50.0  # 50 μm electrodes (typical for neural interfaces)
    min_spacing_um = 200.0  # 200 μm minimum spacing (prevents shorting)
    tissue_conductivity_sm = 0.3  # Brain tissue conductivity ~0.3 S/m
    frequency_hz = 1000.0  # 1 kHz neural signal frequency
    
    # Generate positions
    x, y = phyllotactic_electrode_positions(n_electrodes, electrode_diameter_um, min_spacing_um)
    
    # Calculate crosstalk matrix
    crosstalk = crosstalk_matrix((x, y), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    
    # Signal-to-crosstalk ratio
    scr_db = signal_to_crosstalk_ratio((x, y), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    
    # Coverage analysis
    coverage = coverage_area((x, y), electrode_diameter_um)
    
    print("PNM Realistic Neural Interface Analysis")
    print("=" * 50)
    print(f"Number of electrodes: {n_electrodes}")
    print(f"Electrode diameter: {electrode_diameter_um} μm")
    print(f"Minimum spacing: {min_spacing_um} μm")
    print(f"Coverage radius: {coverage['coverage_radius_um']:.1f} μm")
    print(f"Coverage area: {coverage['coverage_area_um2']/1e6:.2f} mm²")
    print(f"Electrode density: {coverage['electrode_density']:.3f}")
    print(f"Mean SCR: {np.mean(scr_db):.2f} dB")
    print(f"Min SCR: {np.min(scr_db):.2f} dB")
    print(f"Max SCR: {np.max(scr_db):.2f} dB")
    
    # Off-diagonal crosstalk statistics
    off_diag = crosstalk.copy()
    np.fill_diagonal(off_diag, 0)
    max_crosstalk = np.max(off_diag)
    mean_crosstalk = np.mean(off_diag[off_diag > 0])
    
    print(f"\nCrosstalk Statistics:")
    print(f"Max off-diagonal crosstalk: {max_crosstalk:.4f}")
    print(f"Mean off-diagonal crosstalk: {mean_crosstalk:.4f}")
    
    # Visualization
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    
    # 1. Array layout
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(x, y, s=100, c='blue', edgecolors='black', alpha=0.7)
    # Add electrode circles
    for xi, yi in zip(x, y):
        circle = plt.Circle((xi, yi), electrode_diameter_um/2, 
                          fill=False, color='black', linewidth=1, alpha=0.5)
        ax1.add_patch(circle)
    ax1.set_xlabel('X position (μm)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Y position (μm)', fontsize=11, fontweight='bold')
    ax1.set_title(f'PNM Electrode Array Layout ({n_electrodes} electrodes)', fontsize=12, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.4, linewidth=0.8)
    
    # 2. Crosstalk matrix
    ax2 = plt.subplot(2, 3, 2)
    crosstalk_db = 20 * np.log10(np.abs(crosstalk) + 1e-10)
    im = ax2.imshow(crosstalk_db, cmap='hot', aspect='auto', origin='lower', 
                    vmin=-40, vmax=0)
    ax2.set_xlabel('Electrode Index', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Electrode Index', fontsize=11, fontweight='bold')
    ax2.set_title('Crosstalk Matrix (dB)', fontsize=12, fontweight='bold')
    plt.colorbar(im, ax=ax2, label='Crosstalk (dB)')
    
    # 3. Signal-to-crosstalk ratio
    ax3 = plt.subplot(2, 3, 3)
    ax3.scatter(range(n_electrodes), scr_db, c=scr_db, cmap='viridis', 
               edgecolors='black', s=50, alpha=0.7)
    ax3.axhline(np.mean(scr_db), color='r', linestyle='--', label=f'Mean: {np.mean(scr_db):.1f} dB')
    ax3.set_xlabel('Electrode Index', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Signal-to-Crosstalk Ratio (dB)', fontsize=11, fontweight='bold')
    ax3.set_title('SCR per Electrode', fontsize=12, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.4, linewidth=0.8)
    
    # 4. Distance vs crosstalk
    ax4 = plt.subplot(2, 3, 4)
    positions_2d = np.column_stack([x, y])
    distances = []
    crosstalk_values = []
    for i in range(n_electrodes):
        for j in range(i + 1, n_electrodes):
            dist = np.linalg.norm(positions_2d[i] - positions_2d[j])
            distances.append(dist)
            crosstalk_values.append(np.abs(crosstalk[i, j]))
    ax4.scatter(distances, crosstalk_values, alpha=0.5, s=20)
    ax4.set_xlabel('Electrode Distance (μm)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Crosstalk Magnitude', fontsize=11, fontweight='bold')
    ax4.set_title('Crosstalk vs Distance', fontsize=12, fontweight='bold')
    ax4.set_yscale('log')
    ax4.grid(True, alpha=0.4, linewidth=0.8)
    
    # 5. Coverage visualization
    ax5 = plt.subplot(2, 3, 5)
    ax5.scatter(x, y, s=100, c='blue', edgecolors='black', alpha=0.7)
    center = np.array([np.mean(x), np.mean(y)])
    coverage_circle = plt.Circle(center, coverage['coverage_radius_um'], 
                                fill=False, color='red', linewidth=2, linestyle='--')
    ax5.add_patch(coverage_circle)
    ax5.set_xlabel('X position (μm)', fontsize=11, fontweight='bold')
    ax5.set_ylabel('Y position (μm)', fontsize=11, fontweight='bold')
    ax5.set_title(f"Coverage Area ({coverage['coverage_area_um2']/1e6:.2f} mm²)", fontsize=12, fontweight='bold')
    ax5.set_aspect('equal')
    ax5.grid(True, alpha=0.4, linewidth=0.8)
    
    # 6. Statistics summary
    ax6 = plt.subplot(2, 3, 6)
    ax6.text(0.1, 0.9, "Array Statistics", fontsize=14, weight='bold', transform=ax6.transAxes)
    ax6.text(0.1, 0.8, f"Electrodes: {n_electrodes}", transform=ax6.transAxes)
    ax6.text(0.1, 0.7, f"Coverage: {coverage['coverage_area_um2']/1e6:.2f} mm²", transform=ax6.transAxes)
    ax6.text(0.1, 0.6, f"Density: {coverage['electrode_density']:.3f}", transform=ax6.transAxes)
    ax6.text(0.1, 0.5, f"Mean SCR: {np.mean(scr_db):.1f} dB", transform=ax6.transAxes)
    ax6.text(0.1, 0.4, f"Max Crosstalk: {max_crosstalk:.4f}", transform=ax6.transAxes)
    ax6.text(0.1, 0.3, f"Mean Crosstalk: {mean_crosstalk:.4f}", transform=ax6.transAxes)
    ax6.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/pnm_121_clean.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("\nAnalysis complete. Figure saved as 'images/pnm_121_clean.png'")
    plt.show()

if __name__ == "__main__":
    main()
