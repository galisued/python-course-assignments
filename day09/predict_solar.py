import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import warnings

# Suppress warnings for cleaner terminal output
warnings.filterwarnings('ignore')

def main():
    print("==================================================")
    print("      SOLAR POWER DC YIELD PREDICTIVE MODEL       ")
    print("==================================================\n")
    
    print("Loading weather and generation datasets...")
    try:
        # Load the real datasets downloaded from Kaggle
        gen_df = pd.read_csv('Plant_1_Generation_Data.csv')
        weather_df = pd.read_csv('Plant_1_Weather_Sensor_Data.csv')
    except FileNotFoundError:
        print("Error: Dataset CSV files not found.")
        print("Please download and extract them following the README instructions.")
        return

    print("Merging datasets on timestamps...")
    # Merge the generation data with the weather data based on the exact date and time
    df = pd.merge(gen_df, weather_df, on='DATE_TIME', how='inner')

    # Define our inputs (Features) and what we want to predict (Target)
    # We are predicting DC Power based on the ambient heat, panel heat, and sunlight intensity.
    X = df[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']]
    y = df['DC_POWER']

    # Split the dataset: 80% for training the model, 20% for testing its accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"Data merged successfully! Training on {len(X_train)} time-series records...")
    print("Training Random Forest Regressor (this may take a few seconds)...")
    
    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    # Evaluate the model's accuracy on the unseen test data
    test_predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, test_predictions)
    r2 = r2_score(y_test, test_predictions)
    
    print("\n--------------------------------------------------")
    print("                 MODEL PERFORMANCE                ")
    print("--------------------------------------------------")
    print(f"Mean Absolute Error (MAE): ±{mae:.2f} kW")
    print(f"R-squared (Accuracy):      {r2:.4f}")
    print("*An R2 score close to 1.0 indicates highly accurate forecasting.*")
    
    # Run a prediction on a specific row to demonstrate the model working
    print("\n--------------------------------------------------")
    print("             SAMPLE PREDICTION TEST               ")
    print("--------------------------------------------------")
    
    # Take an arbitrary sample from the test set (e.g., index 150)
    sample_index = 150
    sample_conditions = X_test.iloc[[sample_index]]
    actual_power = y_test.iloc[sample_index]
    
    predicted_power = model.predict(sample_conditions)[0]
    
    print("Current Environmental Conditions:")
    print(f"-> Ambient Temperature: {sample_conditions['AMBIENT_TEMPERATURE'].values[0]:.2f} °C")
    print(f"-> Module Temperature:  {sample_conditions['MODULE_TEMPERATURE'].values[0]:.2f} °C")
    print(f"-> Solar Irradiation:   {sample_conditions['IRRADIATION'].values[0]:.4f} W/m²\n")
    
    print(f"Actual DC Power Generated:    {actual_power:.2f} kW")
    print(f"Predicted DC Power Generated: {predicted_power:.2f} kW")
    print("==================================================\n")

if __name__ == "__main__":
    main()