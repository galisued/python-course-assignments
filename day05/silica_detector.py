import cv2
import numpy as np
import os
import glob

def calculate_diameters(image_path, pixel_to_nm_ratio=1.0):
    """
    Reads a TEM image, detects circular nanoparticles using the 
    Hough Circle Transform, and calculates their diameters.
    """
    # 1. Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")

    # NEW: Shrink the image to 25% of its original size 
    scale_factor = 0.25
    new_width = int(img.shape[1] * scale_factor)
    new_height = int(img.shape[0] * scale_factor)
    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # CHANGED: Aggressive Gaussian Blur. This melts the internal silica pores 
    # together so the algorithm only sees the solid outer shape.
    img_blurred = cv2.GaussianBlur(img_resized, (31, 31), 0)

    # 3. Apply Hough Circle Transform on the smudged image
    circles = cv2.HoughCircles(
        img_blurred, 
        cv2.HOUGH_GRADIENT, 
        dp=1,            
        minDist=150,     # CHANGED: Forces the big spheres to be distinct
        param1=40,       # CHANGED: Lowered so it can see the softer, blurred outer edge
        param2=30,       
        minRadius=80,    # CHANGED: Minimum size is huge to ignore all background specs
        maxRadius=400    # Maximum size 
    )

    diameters = []
    
   # 4. Extract radii and calculate diameters
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            # This is the small radius from the 25% shrunk image
            shrunk_radius_pixels = circle[2]
            
            # THE FIX: Divide by the scale_factor (0.25) to multiply it back to 100% true size
            true_radius_pixels = shrunk_radius_pixels / scale_factor
            
            # Now do the normal math
            diameter_pixels = true_radius_pixels * 2
            diameter_nm = diameter_pixels * pixel_to_nm_ratio
            diameters.append(diameter_nm)
            
    return diameters

if __name__ == "__main__":
    # --- SETUP & PATH FINDING ---
    # Get the exact path to where this script is running
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    image_folder = os.path.join(script_dir, "silica images")
    
    if not os.path.exists(image_folder):
        print(f"Error: Could not find the folder at '{image_folder}'")
        print("Make sure you created the 'silica images' folder.")
        exit()

    search_pattern = os.path.join(image_folder, "*.tiff")
    image_files = glob.glob(search_pattern)

    if len(image_files) == 0:
        print("No TIFF images found in the 'silica images' folder.")
        exit()

    print(f"Found {len(image_files)} images in the folder.")
    print("-" * 40)

    # --- CALIBRATION ---
    # We know DMSN03C3_02b has a real diameter of ~625 nm.
    # We will find it in the folder to calculate our conversion rate.
    true_conversion_rate = 1.0 # Default fallback
    calibration_file = next((f for f in image_files if "02b" in f), None)

    if calibration_file:
        print("Calibrating pixel-to-nm ratio using standard (625 nm)...")
        pixel_results = calculate_diameters(calibration_file, pixel_to_nm_ratio=1.0)
        
        if len(pixel_results) > 0:
            # THE FIX: Grab the absolute LARGEST circle found in the image.
            # This guarantees we calibrate using the main silica sphere, not a noise artifact.
            detected_pixel_diameter = max(pixel_results)
            
            true_conversion_rate = 625 / detected_pixel_diameter
            print(f"Calibration successful: 1 pixel = {true_conversion_rate:.3f} nm")
        else:
            print("Failed to detect calibration particle. Using 1:1 pixel ratio.")
    print("-" * 40)

    # --- BATCH PROCESSING ---
    for img_path in image_files:
        file_name = os.path.basename(img_path) 
        print(f"\nAnalyzing: {file_name}")
        
        try:
            results = calculate_diameters(img_path, true_conversion_rate)
            
            if len(results) > 0:
                print(f"  Detected {len(results)} nanoparticles.")
                average = sum(results) / len(results)
                print(f"  Average Diameter: {average:.2f} nm")
            else:
                print("  No particles detected. (Adjust Hough Circle parameters).")
                
        except Exception as e:
            print(f"  Error processing {file_name}: {e}")