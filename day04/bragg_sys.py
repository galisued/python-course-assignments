import sys
from bragg_module import calculate_d_spacing, calculate_lattice_parameter

def main():
    # Check if they provided 2theta, wavelength, and optionally h, k, l (which makes 6 total arguments)
    if len(sys.argv) < 2:
        print("Usage: python bragg_sys.py <2theta> [wavelength] [h k l]")
        print("Example 1 (d-spacing only): python bragg_sys.py 26.64 1.5406")
        print("Example 2 (with lattice param): python bragg_sys.py 26.64 1.5406 1 0 0")
        sys.exit(1)
        
    try:
        two_theta = float(sys.argv[1])
        wavelength = float(sys.argv[2]) if len(sys.argv) >= 3 else 1.5406
        
        if two_theta <= 0 or wavelength <= 0:
            print("Error: Both the angle and wavelength must be greater than zero.")
            sys.exit(1)
            
        theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
        
        print("\n--- Results ---")
        print(f"Calculated θ: {theta_degrees:.2f}°")
        print(f"d-spacing: {d_spacing:.4f} Å")
        
        # NEW: Check if h, k, l were provided
        if len(sys.argv) == 6:
            h = int(sys.argv[3])
            k = int(sys.argv[4])
            l = int(sys.argv[5])
            
            a = calculate_lattice_parameter(d_spacing, h, k, l)
            print(f"Lattice parameter 'a': {a:.4f} Å")
            
    except ValueError:
        print("Error: Please provide valid numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()