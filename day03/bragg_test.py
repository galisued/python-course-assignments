import pytest
from bragg_module import calculate_d_spacing

def test_case_1():
    # wavelength 1.5406, angle 26.64
    theta, d = calculate_d_spacing(1.5406, 26.64)
    assert theta == 13.32
    assert round(d, 4) == 3.3435

def test_case_2():
    # wavelength 1.5406, angle 44.67
    theta, d = calculate_d_spacing(1.5406, 44.67)
    assert theta == 22.335
    assert round(d, 4) == 2.0270

def test_case_3():
    # wavelength 1.7890, angle 52.38
    theta, d = calculate_d_spacing(1.7890, 52.38)
    assert theta == 26.19
    assert round(d, 4) == 2.0267

def test_invalid_zero_angle():
    # Because Bragg's Law divides by the sine of the angle, an angle of 0 
    # should naturally trigger a ZeroDivisionError in the raw math module.
    # We use 'with pytest.raises' to verify that this exact crash happens.
    with pytest.raises(ZeroDivisionError):
        calculate_d_spacing(1.5406, 0)