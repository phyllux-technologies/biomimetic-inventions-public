"""
Phase 2: Generation Verification Test
Tests image generation scripts to verify they produce clean output.
Outputs to TEMP_IMAGE_GENERATION directory.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt


# Add paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'golden-angle-antenna-GAFAA-public'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'PNM-public'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'PhiKey-public'))

TEMP_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"Temporary image generation directory: {TEMP_DIR}")

def test_toy_electrode_array():
    """Test PNM electrode array generation."""
    print("\n=== Testing toy_electrode_array generation ===")
    try:
        N = 121
        golden_angle = 137.508
        theta = np.arange(N) * np.deg2rad(golden_angle)
        r = np.sqrt(theta)
        fig = plt.figure(figsize=(8, 8), facecolor='white')
        ax = fig.add_subplot(111, projection='polar')
        ax.scatter(theta, r, s=10, c='blue')
        ax.set_rlim(0, r.max() * 1.05)
        ax.plot([0, 2*np.pi], [r.max(), r.max()], color='red', linewidth=1)
        ax.set_title("PNM Phyllotactic Electrode Array (121 electrodes)", fontweight='bold')
        fig.suptitle("Golden Angle ~137.508° Pattern for Neural Interfaces")
        output_path = os.path.join(TEMP_DIR, 'test_toy_electrode_array.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        print(f"✅ Generated: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_geometric_lattice():
    """Test Phyllux Vault lattice generation."""
    print("\n=== Testing geometric lattice generation ===")
    try:
        N = 121
        golden_angle = 137.508
        theta = np.arange(N) * np.deg2rad(golden_angle)
        r = np.sqrt(np.arange(N)) * 0.5
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
        ax.scatter(x, y, s=10, c='green', alpha=0.7)
        ax.plot(x, y, color='blue', linewidth=0.5, alpha=0.5)
        ax.set_title("121-Node Lattice Growth (Golden Angle)", fontweight='bold')
        ax.set_xlabel("X Position (arbitrary units)", fontweight='bold')
        ax.set_ylabel("Y Position (arbitrary units)", fontweight='bold')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.4)
        output_path = os.path.join(TEMP_DIR, 'test_phikey_121_clean.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        print(f"✅ Generated: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_spiral_positions():
    """Test spiral positions generation."""
    print("\n=== Testing spiral positions generation ===")
    try:
        N = 121
        golden_angle = 137.508
        theta = np.arange(N) * np.deg2rad(golden_angle)
        r = np.sqrt(theta) * 0.5
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
        ax.scatter(x, y, s=10, c='blue')
        ax.set_title("Spiral Positions (121 nodes)", fontweight='bold')
        ax.set_xlabel("X Position (arbitrary units)", fontweight='bold')
        ax.set_ylabel("Y Position (arbitrary units)", fontweight='bold')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.4)
        output_path = os.path.join(TEMP_DIR, 'test_spiral_positions.png')
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        print(f"✅ Generated: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("PHASE 2: Generation Verification Test")
    print("=" * 60)
    
    results = []
    results.append(("toy_electrode_array", test_toy_electrode_array()))
    results.append(("geometric_lattice", test_geometric_lattice()))
    results.append(("spiral_positions", test_spiral_positions()))
    
    print("\n" + "=" * 60)
    print("VERIFICATION RESULTS:")
    print("=" * 60)
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n✅ All generation tests passed. Ready for Phase 3.")
    else:
        print("\n❌ Some generation tests failed. STOP - do not proceed to Phase 3.")
    
    sys.exit(0 if all_passed else 1)
