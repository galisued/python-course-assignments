import sys
from bragg_module import calculate_d_spacing

def main():
    # Check if the user provided at least the 2tpython3 day03/bragg_sys.py 27.5 0.7107heta argument
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python bragg_sys.py <2theta_angle> [wavelength]")
        print("Example: python bragg_sys.py 27.5")
        print("Example: python bragg_sys.py 27.5 1.5406")
        sys.exit(1)
    
    try:
        two_theta = float(sys.argv[1])
        # Use provided wavelength or default to 1.5406
        wavelength = float(sys.argv[2]) if len(sys.argv) == 3 else 1.5406
        
        theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
        
        print(f"Calculated θ: {theta_degrees:.4f}°")
        print(f"d-spacing: {d_spacing:.4f} Å")
        
    except ValueError:
        print("Error: Please provide valid numeric values for the arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()