# Day 08 Assignment: Interactive PV Material Screener Web Dashboard

## Project Overview
This project transforms a command-line materials informatics script into a fully interactive web application. The tool queries the Materials Project database to discover thermodynamically stable material candidates for photovoltaics and photocatalysis, filtering by formation energy, energy above hull, and visible-light band gaps. 

By migrating from a static terminal output to a modern web interface, the tool now allows for dynamic adjustment of search parameters and interactive exploration of the resulting materials data.

## Architecture & Separation of Concerns
* **Business Logic (`material_filter_PV.py`)**: This file remains completely untouched from a previous assignment. It contains the core scientific algorithms for downloading data and applying thermodynamic and electronic filters. It is completely independent of the web interface.
* **Presentation Layer (`app.py`)**: Built using **Streamlit**. It introduces a web sidebar for user inputs, dynamic data tables, and an interactive scatter plot built with **Plotly** (replacing static Matplotlib images) so users can hover over data points to reveal chemical formulas.

## How to Run

1. Open your command line terminal and navigate to this project folder.
2. Install the required dependencies (which now include the web and graphing frameworks):
   ```bash
   pip3 install -r requirements.txt
   ```
3. Start the local web server:
   ```bash
   streamlit run day08/app.py
   ```
4. The application will automatically open in your default web browser.

## Testing
This project utilizes pytest to verify both the scientific math and the web interface independently:

* Business Logic Tests (test_material_filter.py): Uses a mock dataset to ensure the core algorithm correctly filters out thermodynamically unstable compounds and materials outside the specified band gap, verifying the exact boundaries and edge cases.

* Web Application Tests (test_app.py): Uses Streamlit's AppTest framework to simulate user interactions, verifying that the web page loads correctly, default values are set properly, and the UI accurately catches errors (like missing API keys or element inputs) before making database calls.

Run the full test suite with:
```Bash
pytest
```
## AI Usage
I used Gemini for the assignment:

- i want to use this assignment. can you start from make sure it has a business logic? without changing the code itself
- can you create for me a web application? use this requirments:
Write a web application for it. You can use flask but it would be nicer if you used one of the other web frameworks of python.
Make sure they use the same "business logic" functions.
- write tests to the web application.