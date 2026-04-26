import math

def calculate_d_spacing(wavelength, two_theta):
   
    theta_degrees = two_theta / 2.0
    theta_radians = math.radians(theta_degrees)
    
    # Bragg's Law: d = lambda / (2 * sin(theta))
    d_spacing = wavelength / (2 * math.sin(theta_radians))
    
    return theta_degrees, d_spacing