from bragg_module import calculate_d_spacing

def main():
    print("--- Bragg's Law d-spacing Calculator ---")
    
    # --- GET WAVELENGTH ---
    while True:
        wl_input = input("Enter the X-ray wavelength in Ångströms (default is usually 1.5406 Å): ")
        
        if wl_input.strip() == "":
            wavelength = 1.5406
            print("No input detected. Using standard wavelength: 1.5406 Å")
            break  # Escape the loop!
            
        try:
            wavelength = float(wl_input)
            if wavelength <= 0:
                print("Error: Wavelength must be greater than zero. Please try again.\n")
            else:
                break  # Escape the loop!
        except ValueError:
            print("Error: Please enter a valid number. Try again.\n")
            
    # --- GET 2THETA ANGLE ---
    while True:
        try:
            two_theta = float(input("Enter the measured 2θ angle (in degrees): "))
            if two_theta <= 0:
                print("Error: Angle must be greater than zero. Please try again.\n")
            else:
                break  # Escape the loop!
        except ValueError:
            print("Error: Please enter a valid number. Try again.\n")

    # --- CALCULATION ---
    theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
    
    print("\n--- Results ---")
    print(f"Calculated θ: {theta_degrees:.2f}°")
    print(f"d-spacing: {d_spacing:.4f} Å")

if __name__ == "__main__":
    main()