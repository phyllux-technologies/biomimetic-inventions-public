"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Realistic neural interface calculation utilities for PNM electrode arrays.
Based on standard neural interface models and phyllotactic geometry.
"""

import numpy as np
from typing import Tuple, Optional
from scipy.spatial.distance import cdist
from scipy.special import erfc


def phyllotactic_electrode_positions(n_electrodes: int,
                                    electrode_diameter_um: float = 50.0,
                                    min_spacing_um: float = 200.0,
                                    golden_angle_deg: float = 137.508) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate phyllotactic electrode positions with realistic neural interface spacing.
    
    Args:
        n_electrodes: Number of electrodes
        electrode_diameter_um: Electrode diameter in micrometers
        min_spacing_um: Minimum center-to-center spacing in micrometers
        golden_angle_deg: Golden angle in degrees (default 137.508°)
    
    Returns:
        x, y: Electrode center positions in micrometers
    """
    indices = np.arange(1, n_electrodes + 1)
    
    # Phyllotactic radial growth: r = c * sqrt(n)
    # Scale by minimum spacing
    r = min_spacing_um * np.sqrt(indices)
    
    # Golden angle rotation
    theta = np.deg2rad(indices * golden_angle_deg)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y


def crosstalk_matrix(positions: Tuple[np.ndarray, np.ndarray],
                     electrode_diameter_um: float = 50.0,
                     tissue_conductivity_sm: float = 0.3,
                     frequency_hz: float = 1000.0) -> np.ndarray:
    """
    Calculate realistic crosstalk matrix for neural electrode array.
    
    Based on volume conductor theory and simplified tissue model.
    
    Args:
        positions: (x, y) tuple of electrode positions in micrometers
        electrode_diameter_um: Electrode diameter in micrometers
        tissue_conductivity_sm: Tissue conductivity in S/m
        frequency_hz: Signal frequency in Hz
    
    Returns:
        Crosstalk matrix (n_electrodes x n_electrodes), normalized
    """
    x, y = positions
    n_electrodes = len(x)
    
    # Convert to meters for calculations
    positions_m = np.column_stack([x, y]) * 1e-6
    electrode_radius_m = (electrode_diameter_um / 2.0) * 1e-6
    
    # Distance matrix in meters
    distances = cdist(positions_m, positions_m)
    
    # Volume conductor model: potential decays as 1/r for point sources
    # For finite electrodes, use simplified model
    crosstalk = np.zeros((n_electrodes, n_electrodes))
    
    for i in range(n_electrodes):
        for j in range(n_electrodes):
            if i == j:
                # Self-impedance (simplified)
                crosstalk[i, j] = 1.0 / (tissue_conductivity_sm * electrode_radius_m)
            else:
                # Mutual coupling: decays with distance
                # Simplified model: V = I / (4πσr) for point source
                # Add frequency-dependent effects
                r = distances[i, j]
                if r > 0:
                    # Base coupling
                    coupling = 1.0 / (4.0 * np.pi * tissue_conductivity_sm * r)
                    
                    # Frequency-dependent attenuation (simplified)
                    # Higher frequencies attenuate more in tissue
                    omega = 2 * np.pi * frequency_hz
                    skin_depth = np.sqrt(2.0 / (omega * tissue_conductivity_sm * 8.854e-12))
                    attenuation = np.exp(-r / skin_depth) if skin_depth > 0 else 1.0
                    
                    crosstalk[i, j] = coupling * attenuation
                else:
                    crosstalk[i, j] = 0.0
    
    # Normalize by diagonal (self-impedance)
    diagonal = np.diag(crosstalk)
    crosstalk_normalized = crosstalk / diagonal[:, np.newaxis]
    
    return crosstalk_normalized


def signal_to_crosstalk_ratio(positions: Tuple[np.ndarray, np.ndarray],
                              electrode_diameter_um: float = 50.0,
                              tissue_conductivity_sm: float = 0.3,
                              frequency_hz: float = 1000.0) -> np.ndarray:
    """
    Calculate signal-to-crosstalk ratio for each electrode.
    
    Args:
        positions: (x, y) tuple of electrode positions in micrometers
        electrode_diameter_um: Electrode diameter in micrometers
        tissue_conductivity_sm: Tissue conductivity in S/m
        frequency_hz: Signal frequency in Hz
    
    Returns:
        SCR values in dB for each electrode
    """
    crosstalk = crosstalk_matrix(positions, electrode_diameter_um, tissue_conductivity_sm, frequency_hz)
    
    # Signal is diagonal, crosstalk is off-diagonal sum
    signal = np.diag(crosstalk)
    total_crosstalk = np.sum(crosstalk, axis=1) - signal
    
    scr = signal / (total_crosstalk + 1e-10)
    scr_db = 20 * np.log10(scr)
    
    return scr_db


def coverage_area(positions: Tuple[np.ndarray, np.ndarray],
                 electrode_diameter_um: float = 50.0) -> dict:
    """
    Calculate coverage metrics for electrode array.
    
    Args:
        positions: (x, y) tuple of electrode positions in micrometers
        electrode_diameter_um: Electrode diameter in micrometers
    
    Returns:
        Dictionary with coverage metrics
    """
    x, y = positions
    
    # Array extent
    x_min, x_max = np.min(x), np.max(x)
    y_min, y_max = np.min(y), np.max(y)
    width = x_max - x_min
    height = y_max - y_min
    
    # Effective coverage radius (95% of electrodes within)
    center = np.array([np.mean(x), np.mean(y)])
    distances = np.linalg.norm(np.column_stack([x, y]) - center, axis=1)
    coverage_radius = np.percentile(distances, 95)
    
    # Electrode density
    total_area = np.pi * coverage_radius**2
    electrode_area = np.pi * (electrode_diameter_um / 2.0)**2
    density = len(positions[0]) * electrode_area / total_area if total_area > 0 else 0
    
    return {
        'width_um': width,
        'height_um': height,
        'coverage_radius_um': coverage_radius,
        'coverage_area_um2': np.pi * coverage_radius**2,
        'electrode_density': density,
        'n_electrodes': len(x)
    }
