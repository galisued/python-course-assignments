import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import warnings

# Suppress warnings for cleaner terminal output
warnings.filterwarnings('ignore')

def process_data(gen_file_path, weather_file_path):
    """Loads CSV files, formats datetimes, and merges the datasets."""
    gen_df = pd.read_csv(gen_file_path)
    weather_df = pd.read_csv(weather_file_path)

    gen_df['DATE_TIME'] = pd.to_datetime(gen_df['DATE_TIME'])
    weather_df['DATE_TIME'] = pd.to_datetime(weather_df['DATE_TIME'])

    df = pd.merge(gen_df, weather_df, on='DATE_TIME', how='inner')
    return df

def train_model(df):
    """Splits data and trains the Random Forest model."""
    X = df[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']]
    y = df['DC_POWER']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    """Calculates accuracy metrics based on test data."""
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mae, r2

def main():
    print("==================================================")
    print("      SOLAR POWER DC YIELD PREDICTIVE MODEL       ")
    print("==================================================\n")
    
    print("Loading weather and generation datasets...")
    try:
        df = process_data('Plant_1_Generation_Data.csv', 'Plant_1_Weather_Sensor_Data.csv')
    except FileNotFoundError:
        print("Error: Dataset CSV files not found. Please check your file paths.")
        return

    print(f"Data merged successfully! Training on {len(df)} time-series records...")
    
    # Train the model
    model, X_test, y_test = train_model(df)

    # Evaluate the model
    mae, r2 = evaluate_model(model, X_test, y_test)
    
    print("\n--------------------------------------------------")
    print("                 MODEL PERFORMANCE                ")
    print("--------------------------------------------------")
    print(f"Mean Absolute Error (MAE): ±{mae:.2f} kW")
    print(f"R-squared (Accuracy):      {r2:.4f}")
    print("*An R2 score close to 1.0 indicates highly accurate forecasting.*")
    
    print("\n--------------------------------------------------")
    print("             SAMPLE PREDICTION TEST               ")
    print("--------------------------------------------------")
    
    # Filter for daytime hours and run a prediction
    daytime_conditions = X_test[X_test['IRRADIATION'] > 0.1]
    daytime_results = y_test.loc[daytime_conditions.index]
    
    sample_index = 50
    sample_conditions = daytime_conditions.iloc[[sample_index]]
    actual_power = daytime_results.iloc[sample_index]
    
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