import cv2
import numpy as np
import os
import glob
from pathlib import Path

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
    # Use pathlib to find the "silica images" folder right next to this script
    # This matches the Path(__file__) logic taught in class!
    current_dir = Path(__file__).parent
    image_folder = current_dir / "silica images"
    
    # Grab all .tiff files in that folder
    image_files = list(image_folder.glob("*.tiff"))

    if not image_files:
        print("No TIFF images found in the 'silica images' folder.")
        exit()

    print(f"Found {len(image_files)} images in the folder.")
    print("-" * 40)

    # --- BATCH PROCESSING ---
    true_conversion_rate = 0.439
    
    for img_path in image_files:
        # Convert the Path object back to a string for OpenCV
        img_path_str = str(img_path)
        file_name = img_path.name 
        
        print(f"\nAnalyzing: {file_name}") 
        
        try:
            results = calculate_diameters(img_path_str, true_conversion_rate)
            
            if len(results) > 0:
                print(f"  Detected {len(results)} nanoparticles.")
                average = sum(results) / len(results)
                
                if len(results) > 1:
                    std_dev = np.std(results, ddof=1) 
                    print(f"  Average Diameter: {average:.2f} ± {std_dev:.2f} nm")
                else:
                    print(f"  Diameter: {average:.2f} nm")
                    
            else:
                print("  No particles detected. (Adjust Hough Circle parameters).")
                
        except Exception as e:
            print(f"  Error processing {file_name}: {e}")