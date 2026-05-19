```markdown
# PV Material Screener (Day 6 Assignment)

This repository contains a Python script (`material_filter_PV.py`) developed for the Day 6 assignment of the WIS Python Course.

## Project Overview
This script is designed to discover potential material candidates for photovoltaics or photocatalysis. It queries the web-based Materials Project database for specific elemental compounds (by default, Titanium and Oxygen). The script then processes the data by:
1. Filtering out thermodynamically unstable materials (keeping only those where Formation Energy < 0 and Energy Above Hull <= 0.05).
2. Isolating materials with band gaps in the visible light spectrum (1.5 eV to 3.0 eV).
3. Visualizing the remaining top candidates on a scatter plot (Band Gap vs. Formation Energy, colored by stability).

## About the Database
**Database Used:** [The Materials Project](https://next-gen.materialsproject.org/) (via the `mp-api` Python library).

**Type of Data:** The Materials Project offers computed properties of all known and predicted inorganic materials. It provides comprehensive data sets including crystal structures, thermodynamic stability metrics (formation energy per atom, energy above hull), and electronic properties (like band gaps). This database is widely used in materials engineering and computational chemistry to screen for new functional materials before attempting to synthesize them in the lab.

## How to Run

1. Make sure you are in the `day06` directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt