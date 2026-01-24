"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Compare crosstalk performance of phyllotactic vs. regular grid electrode arrays.
"""

import numpy as np
import matplotlib.pyplot as plt
from src.pnm_public.neural_utils import (
    phyllotactic_electrode_positions,
    crosstalk_matrix,
    signal_to_crosstalk_ratio
)

def regular_grid_positions(n_electrodes: int, spacing_um: float):
    """Generate regular grid electrode positions."""
    # Calculate grid dimensions
    side_length = int(np.ceil(np.sqrt(n_electrodes)))
    
    positions = []
    for i in range(side_length):
        for j in range(side_length):
            if len(positions) < n_electrodes:
                x = (i - side_length/2 + 0.5) * spacing_um
                y = (j - side_length/2 + 0.5) * spacing_um
                positions.append([x, y])
    
    positions = np.array(positions[:n_electrodes])
    return positions[:, 0], positions[:, 1]

def main():
    n_electrodes = 121
    electrode_diameter_um = 50.0
    min_spacing_um = 200.0
    tissue_conductivity_sm = 0.3
    frequency_hz = 1000.0  # 1 kHz neural signal frequency
    
    # Phyllotactic array
    x_phyl, y_phyl = phyllotactic_electrode_positions(n_electrodes, electrode_diameter_um, min_spacing_um)
    crosstalk_phyl = crosstalk_matrix((x_phyl, y_phyl), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    scr_phyl = signal_to_crosstalk_ratio((x_phyl, y_phyl), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    
    # Regular grid array (same number of electrodes, similar spacing)
    x_grid, y_grid = regular_grid_positions(n_electrodes, min_spacing_um)
    crosstalk_grid = crosstalk_matrix((x_grid, y_grid), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    scr_grid = signal_to_crosstalk_ratio((x_grid, y_grid), electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    
    # Statistics
    off_diag_phyl = crosstalk_phyl.copy()
    np.fill_diagonal(off_diag_phyl, 0)
    max_crosstalk_phyl = np.max(off_diag_phyl)
    mean_crosstalk_phyl = np.mean(off_diag_phyl[off_diag_phyl > 0])
    
    off_diag_grid = crosstalk_grid.copy()
    np.fill_diagonal(off_diag_grid, 0)
    max_crosstalk_grid = np.max(off_diag_grid)
    mean_crosstalk_grid = np.mean(off_diag_grid[off_diag_grid > 0])
    
    print("Crosstalk Comparison: Phyllotactic vs. Regular Grid")
    print("=" * 60)
    print(f"\nPhyllotactic Array:")
    print(f"  Max crosstalk: {max_crosstalk_phyl:.4f}")
    print(f"  Mean crosstalk: {mean_crosstalk_phyl:.4f}")
    print(f"  Mean SCR: {np.mean(scr_phyl):.2f} dB")
    print(f"  Min SCR: {np.min(scr_phyl):.2f} dB")
    
    print(f"\nRegular Grid Array:")
    print(f"  Max crosstalk: {max_crosstalk_grid:.4f}")
    print(f"  Mean crosstalk: {mean_crosstalk_grid:.4f}")
    print(f"  Mean SCR: {np.mean(scr_grid):.2f} dB")
    print(f"  Min SCR: {np.min(scr_grid):.2f} dB")
    
    improvement = ((mean_crosstalk_grid - mean_crosstalk_phyl) / mean_crosstalk_grid) * 100
    print(f"\nCrosstalk Reduction: {improvement:.1f}%")
    
    # Visualization
    fig = plt.figure(figsize=(16, 10), facecolor='white')
    
    # Layouts
    ax1 = plt.subplot(2, 3, 1)
    ax1.scatter(x_phyl, y_phyl, s=50, c='blue', edgecolors='black', alpha=0.7)
    ax1.set_xlabel('X position (μm)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Y position (μm)', fontsize=11, fontweight='bold')
    ax1.set_title('Phyllotactic Array', fontsize=12, fontweight='bold')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.4, linewidth=0.8)
    
    ax2 = plt.subplot(2, 3, 2)
    ax2.scatter(x_grid, y_grid, s=50, c='red', edgecolors='black', alpha=0.7)
    ax2.set_xlabel('X position (μm)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Y position (μm)', fontsize=11, fontweight='bold')
    ax2.set_title('Regular Grid Array', fontsize=12, fontweight='bold')
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.4, linewidth=0.8)
    
    # Crosstalk matrices
    ax3 = plt.subplot(2, 3, 3)
    crosstalk_phyl_db = 20 * np.log10(np.abs(crosstalk_phyl) + 1e-10)
    im3 = ax3.imshow(crosstalk_phyl_db, cmap='hot', aspect='auto', origin='lower', vmin=-40, vmax=0)
    ax3.set_xlabel('Electrode Index', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Electrode Index', fontsize=11, fontweight='bold')
    ax3.set_title('Phyllotactic Crosstalk (dB)', fontsize=12, fontweight='bold')
    plt.colorbar(im3, ax=ax3)
    
    ax4 = plt.subplot(2, 3, 4)
    crosstalk_grid_db = 20 * np.log10(np.abs(crosstalk_grid) + 1e-10)
    im4 = ax4.imshow(crosstalk_grid_db, cmap='hot', aspect='auto', origin='lower', vmin=-40, vmax=0)
    ax4.set_xlabel('Electrode Index', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Electrode Index', fontsize=11, fontweight='bold')
    ax4.set_title('Grid Crosstalk (dB)', fontsize=12, fontweight='bold')
    plt.colorbar(im4, ax=ax4)
    
    # SCR comparison
    ax5 = plt.subplot(2, 3, 5)
    ax5.scatter(range(n_electrodes), scr_phyl, label='Phyllotactic', alpha=0.6, s=20)
    ax5.scatter(range(n_electrodes), scr_grid, label='Grid', alpha=0.6, s=20)
    ax5.set_xlabel('Electrode Index', fontsize=11, fontweight='bold')
    ax5.set_ylabel('SCR (dB)', fontsize=11, fontweight='bold')
    ax5.set_title('Signal-to-Crosstalk Ratio', fontsize=12, fontweight='bold')
    ax5.legend(fontsize=10)
    ax5.grid(True, alpha=0.4, linewidth=0.8)
    
    # Statistics comparison
    ax6 = plt.subplot(2, 3, 6)
    categories = ['Max\nCrosstalk', 'Mean\nCrosstalk', 'Mean\nSCR (dB)']
    phyl_values = [max_crosstalk_phyl, mean_crosstalk_phyl, np.mean(scr_phyl)]
    grid_values = [max_crosstalk_grid, mean_crosstalk_grid, np.mean(scr_grid)]
    
    x = np.arange(len(categories))
    width = 0.35
    
    ax6.bar(x - width/2, phyl_values, width, label='Phyllotactic', color='blue', alpha=0.7)
    ax6.bar(x + width/2, grid_values, width, label='Grid', color='red', alpha=0.7)
    ax6.set_ylabel('Value')
    ax6.set_title('Performance Comparison')
    ax6.set_xticks(x)
    ax6.set_xticklabels(categories)
    ax6.legend()
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('images/pnm_crosstalk_121_clean.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("\nAnalysis complete. Figure saved as 'images/pnm_crosstalk_121_clean.png'")
    plt.show()

if __name__ == "__main__":
    main()
