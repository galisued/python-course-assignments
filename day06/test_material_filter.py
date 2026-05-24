import pandas as pd
from material_filter_PV import filter_solar_candidates

def test_filter_solar_candidates_standard():
    """Test that the function correctly filters out bad materials and keeps good ones."""
    
    # 1. SETUP: Create fake data to simulate the Materials Project API response
    fake_data = [
        # This one is perfect (Stable, Band gap is 2.0) -> SHOULD BE KEPT
        {"Formula": "PerfectMat", "Band_Gap_eV": 2.0, "Formation_Energy": -2.5, "Energy_Above_Hull": 0.0},
        
        # Unstable (Positive formation energy) -> SHOULD BE REMOVED
        {"Formula": "UnstableMat", "Band_Gap_eV": 2.1, "Formation_Energy": 1.5, "Energy_Above_Hull": 0.0},
        
        # Wrong Band Gap (0.5 is below the 1.5 minimum) -> SHOULD BE REMOVED
        {"Formula": "LowGapMat", "Band_Gap_eV": 0.5, "Formation_Energy": -3.0, "Energy_Above_Hull": 0.0},
        
        # Too easily decomposes into other phases (Hull > 0.05) -> SHOULD BE REMOVED
        {"Formula": "DecomposingMat", "Band_Gap_eV": 2.2, "Formation_Energy": -1.5, "Energy_Above_Hull": 0.1}
    ]
    
    # Convert it into a Pandas DataFrame just like the real script does
    df = pd.DataFrame(fake_data)

    # 2. ACTION: Run the dataframe through your filter function
    filtered_df = filter_solar_candidates(df, min_bg=1.5, max_bg=3.0)

    # 3. ASSERT: Verify the results
    assert len(filtered_df) == 1  # Only 1 material should have survived
    assert filtered_df.iloc[0]['Formula'] == "PerfectMat"  # Ensure it is the correct one


def test_filter_solar_candidates_empty():
    """Test that the function safely handles an empty dataframe without crashing."""
    
    # Setup an empty dataframe with the required columns
    df = pd.DataFrame(columns=["Formula", "Band_Gap_eV", "Formation_Energy", "Energy_Above_Hull"])
    
    # Action
    filtered_df = filter_solar_candidates(df, min_bg=1.5, max_bg=3.0)
    
    # Assert
    assert len(filtered_df) == 0