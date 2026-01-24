"""
Simulation-based; empirical validation required per provisional application prepared for filing Jan 21, 2026.

Realistic RF calculation utilities for GAFAA antenna arrays.
Based on standard antenna array theory and phyllotactic geometry.
"""

import numpy as np
from typing import Tuple, Optional

# Physical constants
C = 299792458.0  # Speed of light in m/s


def phyllotactic_positions(n_elements: int, 
                          wavelength: float,
                          spacing_factor: float = 0.5,
                          golden_angle_deg: float = 137.507764) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate phyllotactic antenna element positions with realistic spacing.
    
    Args:
        n_elements: Number of antenna elements
        wavelength: Operating wavelength in meters
        spacing_factor: Minimum spacing as fraction of wavelength (typically 0.4-0.6)
        golden_angle_deg: Golden angle in degrees (default 137.507764°, exact: 360 * (1 - 1/phi), phi = (1 + sqrt(5))/2)
    
    Returns:
        x, y: Element positions in meters
    """
    indices = np.arange(1, n_elements + 1)
    
    # Phyllotactic radial growth: r = c * sqrt(n)
    # Scale by wavelength and spacing factor
    min_spacing = wavelength * spacing_factor
    r = min_spacing * np.sqrt(indices)
    
    # Golden angle rotation
    theta = np.deg2rad(indices * golden_angle_deg)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y


def array_factor_2d(positions: Tuple[np.ndarray, np.ndarray],
                    frequency_hz: float,
                    scan_angle_deg: Tuple[float, float] = (0.0, 0.0),
                    observation_angles: Optional[np.ndarray] = None,
                    weights: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate realistic 2D array factor for phyllotactic array.
    
    Args:
        positions: (x, y) tuple of element positions in meters
        frequency_hz: Operating frequency in Hz
        scan_angle_deg: (azimuth, elevation) scan angle in degrees
        observation_angles: Array of (azimuth, elevation) observation angles in degrees
        weights: Complex weights for each element (default: uniform)
    
    Returns:
        observation_angles, array_factor_db: Observation angles and array factor in dB
    """
    x, y = positions
    n_elements = len(x)
    
    # Wavenumber
    k = 2 * np.pi * frequency_hz / C
    
    # Default uniform weights
    if weights is None:
        weights = np.ones(n_elements, dtype=complex)
    
    # Default observation grid
    if observation_angles is None:
        az = np.linspace(-180, 180, 361)
        el = np.linspace(-90, 90, 181)
        az_grid, el_grid = np.meshgrid(az, el)
        observation_angles = np.column_stack([az_grid.ravel(), el_grid.ravel()])
    
    # Scan direction unit vector
    scan_az, scan_el = np.deg2rad(scan_angle_deg)
    scan_dir = np.array([
        np.cos(scan_el) * np.sin(scan_az),
        np.cos(scan_el) * np.cos(scan_az),
        np.sin(scan_el)
    ])
    
    # Calculate array factor
    af = np.zeros(len(observation_angles), dtype=complex)
    
    for i, (obs_az, obs_el) in enumerate(observation_angles):
        obs_az_rad = np.deg2rad(obs_az)
        obs_el_rad = np.deg2rad(obs_el)
        
        obs_dir = np.array([
            np.cos(obs_el_rad) * np.sin(obs_az_rad),
            np.cos(obs_el_rad) * np.cos(obs_az_rad),
            np.sin(obs_el_rad)
        ])
        
        # Phase contribution from each element
        for j in range(n_elements):
            element_pos = np.array([x[j], y[j], 0.0])
            phase = k * np.dot(element_pos, obs_dir - scan_dir)
            af[i] += weights[j] * np.exp(1j * phase)
    
    af_db = 20 * np.log10(np.abs(af) / np.max(np.abs(af)) + 1e-10)
    
    return observation_angles, af_db


def mutual_coupling_matrix(positions: Tuple[np.ndarray, np.ndarray],
                          frequency_hz: float,
                          element_impedance: complex = 50.0 + 0j) -> np.ndarray:
    """
    Estimate mutual coupling matrix using simplified model.
    
    Args:
        positions: (x, y) tuple of element positions in meters
        frequency_hz: Operating frequency in Hz
        element_impedance: Element impedance in ohms
    
    Returns:
        Coupling matrix (n_elements x n_elements)
    """
    x, y = positions
    n_elements = len(x)
    wavelength = C / frequency_hz
    
    # Distance matrix
    positions_2d = np.column_stack([x, y])
    distances = np.sqrt(np.sum((positions_2d[:, np.newaxis, :] - 
                                   positions_2d[np.newaxis, :, :])**2, axis=2))
    
    # Simplified mutual coupling model (decays with distance)
    # Real implementation would use full-wave simulation
    coupling = np.exp(-2j * np.pi * distances / wavelength) / (1.0 + distances / wavelength)
    coupling = coupling / (1.0 + distances / (wavelength * 0.1))  # Additional decay
    
    # Self-coupling (diagonal)
    np.fill_diagonal(coupling, element_impedance)
    
    return coupling


def grating_lobe_analysis(positions: Tuple[np.ndarray, np.ndarray],
                          frequency_hz: float,
                          max_angle_deg: float = 90.0) -> dict:
    """
    Analyze grating lobe characteristics of phyllotactic array.
    
    Args:
        positions: (x, y) tuple of element positions in meters
        frequency_hz: Operating frequency in Hz
        max_angle_deg: Maximum scan angle to analyze
    
    Returns:
        Dictionary with grating lobe analysis results
    """
    x, y = positions
    wavelength = C / frequency_hz
    
    # Calculate minimum and maximum spacing
    positions_2d = np.column_stack([x, y])
    distances = []
    for i in range(len(positions_2d)):
        for j in range(i + 1, len(positions_2d)):
            dist = np.linalg.norm(positions_2d[i] - positions_2d[j])
            distances.append(dist)
    
    min_spacing = np.min(distances) if distances else 0
    max_spacing = np.max(distances) if distances else 0
    mean_spacing = np.mean(distances) if distances else 0
    
    # Grating lobe condition: d > λ/(1 + sin(θ_max))
    max_scan_rad = np.deg2rad(max_angle_deg)
    critical_spacing = wavelength / (1.0 + np.sin(max_scan_rad))
    
    has_grating_lobes = max_spacing > critical_spacing
    
    return {
        'min_spacing': min_spacing,
        'max_spacing': max_spacing,
        'mean_spacing': mean_spacing,
        'critical_spacing': critical_spacing,
        'has_grating_lobes': has_grating_lobes,
        'wavelength': wavelength,
        'spacing_ratio': max_spacing / wavelength if wavelength > 0 else 0
    }
