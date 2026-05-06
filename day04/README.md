# Day 04 Assignment: Cubic Lattice Parameter Extension

## Overview
This assignment builds upon the modular architecture from Day 03 by introducing a new feature: the ability to calculate the **Cubic Lattice Parameter ($a$)**. 

While Bragg's Law calculates the distance between specific atomic planes ($d$-spacing), the lattice parameter tells us the physical size of the entire unit cell for cubic crystal systems.

## The New Feature: Lattice Parameter Calculation
The core business logic in `bragg_module.py` has been updated with a new function `calculate_lattice_parameter`. It uses the calculated $d$-spacing along with the **Miller Indices** ($h, k, l$) provided by the user.

### The Equation
For cubic crystal systems, the relationship between $d$-spacing and the lattice parameter $a$ is defined as:
**$a = d 	imes \sqrt{h^2 + k^2 + l^2}$**

Where:
* **$a$:** The lattice parameter (size of the unit cell).
* **$d$:** The $d$-spacing calculated via Bragg's Law.
* **$h, k, l$:** The Miller Indices (whole integers representing the crystallographic plane).

## Interface Updates
All three user interfaces have been updated to optionally support this new calculation:
* **`bragg_input.py` (Standard Input):** After calculating $d$-spacing, it prompts the user if they want to calculate '$a$' and asks for $h, k, l$.
* **`bragg_sys.py` (Command Line):** Accepts 3 additional optional arguments. Example: `python bragg_sys.py 26.64 1.5406 1 0 0`
* **`bragg_gui.py` (GUI):** Added a new optional input section for the $h, k, l$ indices. The calculation automatically runs if these fields are filled.

## Updated Test Cases
The test suite (`bragg_test.py`) was entirely overhauled to test real-world material properties, verifying both $d$-spacing and lattice parameter ($a$):
* **Iron (Fe) with Cobalt source:** Wavelength 1.7890, Angle 52.38, $h,k,l$: 1,1,0 ➔ **$a$ = 2.8662 Å**
* **Silicon (Si) with Copper source:** Wavelength 1.5406, Angle 28.44, $h,k,l$: 1,1,1 ➔ **$a$ = 5.4314 Å**
* **Aluminum (Al) with Copper source:** Wavelength 1.5406, Angle 38.50, $h,k,l$: 1,1,1 ➔ **$a$ = 4.0468 Å**
* **Zero Angle Validation:** Still ensuring `ZeroDivisionError` is caught properly.

## AI Usage
I used Gemini for the assignment:

- can you add to each code a calculation for lattice parameter for cubic structure? the input should be h,k,l and the d spacing is the one calculated before. i attached my repository so you can see the code for each app

- can you create a new test file that check also the lattice parameter? plus one with invalid value