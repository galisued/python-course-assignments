
# Day 03 Assignment: Bragg's Law Modularization

## Overview
This project takes a procedural Python script from Day 2 and refactors it into a modular architecture. The core business logic (Bragg's Law calculation) has been isolated into a shared library, which is then utilized by three distinct user interfaces.

## Project Structure
* **`bragg_module.py`**: The core library containing the mathematical logic (`calculate_d_spacing`).
* **`bragg_input.py`**: A standard terminal script using Python's built-in `input()` function.
* **`bragg_sys.py`**: A command-line tool that takes arguments directly via `sys.argv`.
* **`bragg_gui.py`**: A graphical user interface built with the `tkinter` library.
* **`bragg_test.py`**: A test suite using Python's built-in `unittest` framework.

## external library

This project utilizes the following external libraries, which must be installed via pip:

* **`customtkinter`**: Used to upgrade the standard `tkinter` Graphical User Interface into a modern, dark-mode compatible desktop window.
* **`pytest`**: Used as the testing framework to verify the mathematical logic and handle expected exceptions (like `ZeroDivisionError`).

**Test Cases & Results:**
* wavelength 1.5406, angle 26.64 ➔ **Calculated d-spacing: 3.3435 Å** (θ = 13.32°)
* wavelength 1.5406, angle 44.67 ➔ **Calculated d-spacing: 2.0270 Å** (θ = 22.335°)
* wavelength 1.7890, angle 52.38 ➔ **Calculated d-spacing: 2.0267 Å** (θ = 26.19°)
* Invalid input (Angle = 0) ➔ **Returns ZeroDivisionError**

## AI

i used Gemini to write the code. prompts:

1. For the python class I'm taking, I need to make a new file to the "business logic" of the code "...". 
   I have this task:
   Create 3 versions of the program for 3 different ways to interact with the users. Each one uses the shared library.

   uses standard input (the input function)

   uses the command line (the sys.argv list)

   uses GUI. You can use tkinter, the one we used in class, or you can use some other library.

   Create a test file with a number of test-cases to verify that your "business logic" (the computation) works as expected.

2. Can you add to the code that if you. gave negative or zero it is not valid and please try again.

3. This is nice but can you make the gui look better?. you dont have to use tkinter library. you can use another one

4. can you do this task again?
Create a test file with a number of test-cases to verify that your "business logic" (the computation) works as expected
the test cases I want are:
- wavelenth 1.5406, angle 26.64
- wavelenth 1.5406, angle 44.67
- wavelenth 1.7890, angle 52.38
- mabye another with 0/minus which is invalid

