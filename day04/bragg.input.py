from bragg_module import calculate_d_spacing, calculate_lattice_parameter

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

    print("\n--- Optional: Cubic Lattice Parameter ---")
    while True:
        calc_a = input("Do you want to calculate the lattice parameter 'a'? (y/n): ").strip().lower()

        if calc_a == 'n':
            print("Calculation complete. Goodbye!")
            break

        elif calc_a == 'y':
            try:
                print("Enter the Miller Indices (must be whole integers):")
                h = int(input("h: "))
                k = int(input("k: "))
                l = int(input("l: "))

                a = calculate_lattice_parameter(d_spacing, h, k, l)
                print(f"\nCalculated Lattice parameter 'a': {a:.4f} Å")
                break
            except ValueError:
                print("Error: Miller indices must be whole integers (e.g., 1, 0, 2). Try again.\n")
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()