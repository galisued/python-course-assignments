from streamlit.testing.v1 import AppTest

def test_app_loads_correctly():
    """Test that the application starts up without crashing and displays the correct title."""
    # Initialize the app simulator
    at = AppTest.from_file("app.py").run()
    
    # Assert that no Python exceptions or crashes occurred during load
    assert not at.exception
    
    # Assert that the main title matches exactly
    assert at.title[0].value == "☀️ Photovoltaic Material Screener"


def test_default_sidebar_values():
    """Test that the default input values are correctly set when a user opens the app."""
    at = AppTest.from_file("app.py").run()
    
    # In Streamlit AppTest, elements are indexed by the order they appear.
    # text_input[0] is the API key, text_input[1] is the Elements box.
    assert at.text_input[1].value == "Ti, O"
    
    # number_input[0] is Min Band Gap, number_input[1] is Max Band Gap
    assert at.number_input[0].value == 1.5
    assert at.number_input[1].value == 3.0


def test_missing_api_key_error():
    """Test that clicking the search button without an API key triggers the correct error message."""
    at = AppTest.from_file("app.py").run()
    
    # Simulate a user clicking the first (and only) button on the screen
    at.button[0].click().run()
    
    # Assert that an error box appears and contains the exact warning text
    assert at.error[0].value == "Please provide an API key to continue."


def test_missing_elements_error():
    """Test that deleting the default elements and clicking search triggers an error."""
    at = AppTest.from_file("app.py").run()
    
    # First, fake typing an API key so it passes the first check
    at.text_input[0].input("fake_api_key_12345")
    
    # Next, clear out the default "Ti, O" from the elements box
    at.text_input[1].input("")
    
    # Click the search button
    at.button[0].click().run()
    
    # Assert the correct error shows up
    assert at.error[0].value == "Please provide at least one element."