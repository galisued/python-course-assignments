## Bragg's Law

This program calculates the distance between layers of atoms inside a crystal. In materials science, this distance is known as **d-spacing**. 

Scientists measure this using an X-Ray Diffraction (XRD) machine. The machine fires X-rays at a sample and measures the angle at which the rays bounce off. To translate those angles into physical distances between the atoms, we use an equation called **Bragg's Law** (specifically, the first order of diffraction).

### The Equation

**λ = 2d * sin(θ)**

Where:
* **λ (Lambda):** The wavelength of the X-ray source.
* **d:** The d-spacing (the distance between atomic layers that we are trying to find).
* **θ (Theta):** The angle of the bounced X-ray.

### How the Program Works
The program requires two inputs from the user:
1. **Wavelength (λ):** This is usually **1.5406 Å** (Angstroms), though it can vary depending on the specific machine.
2. **Angle (2-Theta):** The raw angle measurement provided by the XRD machine.

**Important Note on the Angle:** The machine outputs a value called "2-Theta" (the total angle of the reflected X-ray). However, the Bragg's Law equation only requires "Theta" (half of that angle). To handle this, the program automatically divides the user's 2-Theta input by 2, calculates the true Theta, and then computes the final d-spacing using the formula above. 

### Example

to calculate the d-spacing of (101) plane of silica:

* **Enter Wavelength:** 1.5406
* **Enter 2-Theta:** 26.64

**Expected Output:**
* **Calculated θ:** 13.32
* **d-spacing:** 3.3435 Å

###AI

i used Gemini to write the code. promt:

I'm taking a course in Python. Can you write me a code that calculate d-spacing using Bragg's law? in the code first ask to enter the wavelength of the Xray and mention it is usually 1.5406 angstrom and then ask to enter the 2theta. dont forget that in the measurment they show 2theta so you need to divide it by two  before the calculation 