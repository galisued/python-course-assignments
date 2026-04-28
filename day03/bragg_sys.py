import sys
from bragg_module import calculate_d_spacing

def main():
    # Check if the user provided at least the 2theta argument
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python bragg_sys.py <2theta_angle> [wavelength]")
        print("Example: python bragg_sys.py 27.5")
        sys.exit(1)
    
    try:
        # Get the inputs
        two_theta = float(sys.argv[1])
        wavelength = float(sys.argv[2]) if len(sys.argv) == 3 else 1.5406
        
        # NEW VALIDATION CHECK: Are the numbers negative or zero?
        if two_theta <= 0 or wavelength <= 0:
            print("Error: Both the angle and wavelength must be greater than zero.")
            sys.exit(1) # Stop the script immediately!
            
        # If we made it past the check, do the math
        theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
        
        print("\n--- Results ---")
        print(f"Calculated θ: {theta_degrees:.2f}°")
        print(f"d-spacing: {d_spacing:.4f} Å")
        
    except ValueError:
        print("Error: Please provide valid numeric values for the arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()