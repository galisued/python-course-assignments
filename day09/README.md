# Solar Power Generation Forecasting

## Overview
This project uses a real-world dataset from a solar power plant in India to predict the DC Power output of solar panels based on real-time meteorological sensor data. 

The project demonstrates data wrangling by merging generation logs with weather logs via Pandas, and applies a `RandomForestRegressor` from `scikit-learn` to model the non-linear relationship between irradiation, panel temperature, and power yield.

## How to Download the Data
The dataset used for this project is the **Solar Power Generation Data** hosted on Kaggle.

1. Go to the Kaggle dataset page: [Solar Power Generation Data](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)
2. Click the **"Download"** button (you may need to log in to your Kaggle account).
3. Unzip the downloaded archive.
4. Locate the following two files from the Plant 1 directory:
   * `Plant_1_Generation_Data.csv`
   * `Plant_1_Weather_Sensor_Data.csv`
5. Move both of these CSV files directly into the same folder as the `predict_solar.py` script.

## How to Run the Example
**1. Install Prerequisites**
Ensure you have Python installed, then install the required data science libraries by running the following command in your terminal.

**1. Install Prerequisites**
Ensure you have Python installed. Use the provided requirements file to install the necessary data science libraries by running this command in your terminal:
```bash
pip install -r requirements.txt
```

**2. Execute the Script**
Open your terminal, navigate to the folder containing the script and the two CSV files, and run:
```bash
python predict_solar.py`
```

**3. Expected Output**
The script will load and merge the datasets on their timestamps, train the machine learning model, and output the Mean Absolute Error (MAE) and R-squared values to show overall accuracy. It will then automatically select a sample array of weather conditions from the test data and display both its real recorded power output and the model's predicted power output.

**4. Run Tests**
you can run the tests by running this command in your terminal:
```bash
pytest test_predict_solar.py -v
```

## AI Usage
I used Gemini for the assignment:

- this is my assignment for this week. can you write me a script that predicts the efficiency of solar panels, using the weather conditions?

- add requirment.txt s