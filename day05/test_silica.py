import os
import pytest

# Import the function you wrote in your main script
# (This assumes your main file is named silica_detector.py)
from silica_detector import calculate_diameters

# The exact pixel-to-nm ratio we verified for the high-res .tiff files
RATIO = 0.439

# Dynamically find the images folder so the test works on any computer
BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "silica images")

def test_02b_large_particles():
    """Test that batch 03C3_02b averages around 610 nm"""
    image_path = os.path.join(IMAGE_DIR, "DMSN03C3_02b.tiff")
    results = calculate_diameters(image_path, RATIO)
    
    # 1. Verify the algorithm actually found particles
    assert len(results) > 0
    
    # 2. Calculate the average
    average = sum(results) / len(results)
    
    # 3. Assert the average is within a valid scientific range (600nm - 620nm)
    assert 600.0 <= average <= 620.0


def test_01c_large_particles():
    """Test that batch 03C3_01c averages around 614 nm"""
    image_path = os.path.join(IMAGE_DIR, "DMSN03C3_01c.tiff")
    results = calculate_diameters(image_path, RATIO)
    
    assert len(results) > 0
    
    average = sum(results) / len(results)
    
    # Assert the average is within the expected range (605nm - 625nm)
    assert 605.0 <= average <= 625.0


def test_02a_small_particles():
    """Test that batch 03C2_02a successfully identifies the smaller ~297 nm synthesis"""
    image_path = os.path.join(IMAGE_DIR, "DMSN03C2_02a.tiff")
    results = calculate_diameters(image_path, RATIO)
    
    assert len(results) > 0
    
    average = sum(results) / len(results)
    
    # Assert the average correctly drops to the small particle range (290nm - 305nm)
    assert 290.0 <= average <= 305.0