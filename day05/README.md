# Day 5 Assignment: Automated TEM Silica Nanoparticle Analysis

## Project Overview
This project provides a computer vision pipeline to automate the detection and physical measurement of bio-inspired silica nanoparticles from raw Transmission Electron Microscopy (TEM) images. 

Because these synthesized particles feature a complex dendritic (starburst) pore structure, standard edge-detection algorithms often get confused by the internal texture. This script uses OpenCV to preprocess the massive 4K `.tiff` files, apply aggressive Gaussian blurring to isolate the solid outer skeleton, and utilize the Hough Circle Transform to detect the particles. It then calculates the average diameter and sample standard deviation in nanometers.

## Calibration
The script relies on a scientifically verified calibration ratio for the high-resolution `.tiff` files:
**1 pixel = 0.439 nm**
*(This was calculated by anchoring the high-resolution pixel sizes to a known 625 nm ± 6.8 DLS wet-measurement standard for batch 03C3_02b, accounting for the expected shrinkage due to hydration layer loss in the TEM vacuum).*

## How to Run
1. Ensure all dependencies are installed:
   ```bash
   pip3 install -r requirements.txt

## AI Usage
I used Gemini for the assignment:

- this is my assighnment for day 5. can you write a script that measure the diameter of the silica nanoparticles in the images. 

- the code is running for a few minutes. can you make it faster?

- this is what it showed me but the sizes are not true.

- it worked but i want it to show me the name of the analyzed picture and deviation