import pytest
from bragg_module import calculate_d_spacing, calculate_lattice_parameter

def test_case_iron():
    # Iron (Fe) with Cobalt source
    # Wavelength: 1.7890, Angle: 52.38, h, k, l: 1, 1, 0
    theta, d = calculate_d_spacing(1.7890, 52.38)
    a = calculate_lattice_parameter(d, 1, 1, 0)
    
    assert theta == 26.19
    assert round(d, 4) == 2.0267
    assert round(a, 4) == 2.8662

def test_case_silicon():
    # Silicon (Si) with Copper source
    # Wavelength: 1.5406, Angle: 28.44, h, k, l: 1, 1, 1
    theta, d = calculate_d_spacing(1.5406, 28.44)
    a = calculate_lattice_parameter(d, 1, 1, 1)

    assert theta == 14.22
    assert round(d, 4) == 3.1358 
    assert round(a, 4) == 5.4314  

def test_case_aluminum():
    # Aluminum (Al) with Copper source
    # Wavelength: 1.5406, Angle: 38.50, h, k, l: 1, 1, 1
    theta, d = calculate_d_spacing(1.5406, 38.50)
    a = calculate_lattice_parameter(d, 1, 1, 1)
    
    assert theta == 19.25
    assert round(d, 4) == 2.3364
    assert round(a, 4) == 4.0468

def test_invalid_zero_angle():
    # TEST: Passing 0 to the math module
    # Because sin(0) is 0, this causes a mathematical division by zero.
    # We expect the module to crash with a ZeroDivisionError.
    with pytest.raises(ZeroDivisionError):
        calculate_d_spacing(1.5406, 0)
