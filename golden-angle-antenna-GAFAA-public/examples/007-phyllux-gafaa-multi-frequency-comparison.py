"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Compare GAFAA performance across multiple frequencies (sub-6GHz, mmWave 5G, satellite).
"""

import numpy as np
import matplotlib.pyplot as plt
from src.gafaa_public.rf_utils import (
    phyllotactic_positions,
    array_factor_2d,
    grating_lobe_analysis
)

def main():
    # Multiple frequency bands
    frequencies = {
        'Sub-6GHz 5G': 3.5e9,  # 3.5 GHz
        'mmWave 5G': 28e9,      # 28 GHz
        'Satellite Ku': 12e9,   # 12 GHz
        'WiFi 6E': 6e9          # 6 GHz
    }
    
    n_elements = 121
    spacing_factor = 0.5
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()
    
    results = {}
    
    for idx, (name, freq) in enumerate(frequencies.items()):
        wavelength = 299792458.0 / freq
        
        # Generate positions
        x, y = phyllotactic_positions(n_elements, wavelength, spacing_factor)
        
        # Array factor
        az_angles = np.linspace(-90, 90, 181)
        el_angles = np.zeros_like(az_angles)
        obs_angles = np.column_stack([az_angles, el_angles])
        
        _, af_db = array_factor_2d((x, y), freq, 
                                   scan_angle_deg=(0.0, 0.0),
                                   observation_angles=obs_angles)
        
        # Grating lobe analysis
        grating = grating_lobe_analysis((x, y), freq)
        
        # Plot
        ax = axes[idx]
        ax.plot(az_angles, af_db, 'b-', linewidth=2)
        ax.set_xlabel('Azimuth Angle (deg)')
        ax.set_ylabel('Array Factor (dB)')
        ax.set_title(f'{name}\n{freq/1e9:.1f} GHz, λ={wavelength*1000:.2f}mm')
        ax.grid(True, alpha=0.3)
        ax.set_ylim([-40, 5])
        
        # Add grating lobe info
        grating_text = f"Grating lobes: {'Yes' if grating['has_grating_lobes'] else 'No'}"
        ax.text(0.05, 0.95, grating_text, transform=ax.transAxes,
               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        results[name] = {
            'frequency': freq,
            'wavelength': wavelength,
            'grating_analysis': grating,
            'max_af': np.max(af_db),
            'beamwidth_3db': calculate_beamwidth(az_angles, af_db)
        }
    
    plt.tight_layout()
    plt.savefig('images/gafaa_multi_freq_121_clean.png', dpi=300, bbox_inches='tight', facecolor='white')
    
    # Print summary
    print("Multi-Frequency GAFAA Comparison")
    print("=" * 60)
    for name, res in results.items():
        print(f"\n{name}:")
        print(f"  Frequency: {res['frequency']/1e9:.2f} GHz")
        print(f"  Wavelength: {res['wavelength']*1000:.2f} mm")
        print(f"  Max AF: {res['max_af']:.2f} dB")
        print(f"  3dB Beamwidth: {res['beamwidth_3db']:.2f}°")
        print(f"  Grating lobes: {res['grating_analysis']['has_grating_lobes']}")
    
    plt.show()

def calculate_beamwidth(angles, af_db):
    """Calculate 3dB beamwidth."""
    max_idx = np.argmax(af_db)
    max_val = af_db[max_idx]
    threshold = max_val - 3.0
    
    # Find points where AF crosses threshold
    above_threshold = af_db >= threshold
    if np.sum(above_threshold) == 0:
        return 0.0
    
    indices = np.where(above_threshold)[0]
    beamwidth = angles[indices[-1]] - angles[indices[0]]
    return beamwidth

if __name__ == "__main__":
    main()
