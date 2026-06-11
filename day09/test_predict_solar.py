import pytest
import pandas as pd
import numpy as np
from predict_solar import process_data, train_model, evaluate_model

@pytest.fixture
def mock_solar_dataframe():
    """Generates synthetic merged data to test the model functions."""
    np.random.seed(42)
    # Create 100 rows of fake weather and power data
    data = {
        'DATE_TIME': pd.date_range(start='2020-05-15', periods=100, freq='h'),
        'AMBIENT_TEMPERATURE': np.random.uniform(20, 35, 100),
        'MODULE_TEMPERATURE': np.random.uniform(20, 50, 100),
        'IRRADIATION': np.random.uniform(0.0, 1.0, 100),
        'DC_POWER': np.random.uniform(0, 5000, 100)
    }
    return pd.DataFrame(data)

def test_process_data(tmp_path):
    """Tests if the function correctly merges two CSVs based on timestamps."""
    # Create temporary mock CSV files using pytest's tmp_path feature
    gen_file = tmp_path / "mock_gen.csv"
    weather_file = tmp_path / "mock_weather.csv"
    
    gen_file.write_text("DATE_TIME,DC_POWER\n2020-05-15 00:00:00,150.5\n")
    weather_file.write_text("DATE_TIME,AMBIENT_TEMPERATURE,MODULE_TEMPERATURE,IRRADIATION\n2020-05-15 00:00:00,25.0,26.0,0.8\n")
    
    # Run the function
    merged_df = process_data(gen_file, weather_file)
    
    # Assertions
    assert len(merged_df) == 1
    assert 'DC_POWER' in merged_df.columns
    assert 'IRRADIATION' in merged_df.columns

def test_train_model_data_split(mock_solar_dataframe):
    """Tests if the model trains and correctly splits data (80/20)."""
    model, X_test, y_test = train_model(mock_solar_dataframe)
    
    # Assert the model was created
    assert model is not None
    # Assert the 20% test split worked correctly (100 rows * 0.20 = 20 rows)
    assert len(X_test) == 20
    assert len(y_test) == 20

def test_evaluate_model_metrics(mock_solar_dataframe):
    """Tests if the evaluation metrics return standard numerical types."""
    model, X_test, y_test = train_model(mock_solar_dataframe)
    mae, r2 = evaluate_model(model, X_test, y_test)
    
    # Assert the metrics are floats and that Error is not negative
    assert isinstance(mae, float)
    assert isinstance(r2, float)
    assert mae >= 0