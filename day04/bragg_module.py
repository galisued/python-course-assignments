import math

def calculate_d_spacing(wavelength, two_theta):
   
    theta_degrees = two_theta / 2.0
    theta_radians = math.radians(theta_degrees)
    
    # Bragg's Law: d = lambda / (2 * sin(theta))
    d_spacing = wavelength / (2 * math.sin(theta_radians))
    
    return theta_degrees, d_spacing

def calculate_lattice_parameter(d_spacing, h, k, l):
  
    return d_spacing * math.sqrt(h**2 + k**2 + l**2)
