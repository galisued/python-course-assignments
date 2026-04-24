import math

def calculate_d_spacing():
    print("--- Bragg's Law d-spacing Calculator ---")
    
    # 1. Ask for the wavelength, mentioning the standard Cu K-alpha value
    wl_input = input("Enter the X-ray wavelength in Ångströms (default is usually 1.5406 Å): ")
    
    # If the user just presses Enter, use the default 1.5406
    if wl_input.strip() == "":
        wavelength = 1.5406
        print("No input detected. Using standard wavelength: 1.5406 Å")
    else:
        wavelength = float(wl_input)
        
    # 2. Ask for the 2theta measurement
    two_theta = float(input("Enter the measured 2θ angle (in degrees): "))
    
    # 3. Divide 2theta by 2 to get theta
    theta_degrees = two_theta / 2.0
    
    # 4. Convert theta from degrees to radians (math.sin requires radians)
    theta_radians = math.radians(theta_degrees)
    
    # 5. Calculate d-spacing assuming first-order diffraction (n = 1)
    # Bragg's Law: n*lambda = 2*d*sin(theta) -> d = lambda / (2 * sin(theta))
    d_spacing = wavelength / (2 * math.sin(theta_radians))
    
    # Print the results rounded to 4 decimal places
    print("\n--- Results ---")
    print(f"Calculated θ: {theta_degrees:.4f}°")
    print(f"d-spacing: {d_spacing:.4f} Å")

if __name__ == "__main__":
    calculate_d_spacing()
    