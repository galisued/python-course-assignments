from bragg_module import calculate_d_spacing

def main():
    print("--- Bragg's Law d-spacing Calculator ---")
    
    wl_input = input("Enter the X-ray wavelength in Ångströms (default is usually 1.5406 Å): ")
    
    if wl_input.strip() == "":
        wavelength = 1.5406
        print("No input detected. Using standard wavelength: 1.5406 Å")
    else:
        wavelength = float(wl_input)
        
    two_theta = float(input("Enter the measured 2θ angle (in degrees): "))
    
    # Call the shared library function
    theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
    
    print("\n--- Results ---")
    print(f"Calculated θ: {theta_degrees:.4f}°")
    print(f"d-spacing: {d_spacing:.4f} Å")

if __name__ == "__main__":
    main()