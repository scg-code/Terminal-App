"""Test cases for the `get_weather_data` function."""

from functions import get_weather_data

def test_get_weather_data():
    """
    Test cases for the `get_weather_data` function.

    This module contains test cases for the `get_weather_data` function. It tests
    various scenarios, including valid and invalid city names, units, and edge cases.

    Test cases:
    1. Test with a valid city name (e.g., New York) in metric units.
    2. Test with an invalid city name in imperial units.
    3. Test with a city name containing non-alphabet characters (e.g., numbers) in metric units.
    4. Add more test cases to cover different scenarios:
        - Test with other cities.
        - Test with various units (metric, imperial).
        - Test with edge cases.
    5. For error cases, you can use try-except to capture exceptions and assert the expected behavior.
    6. Repeat similar tests for different cities and units as needed.
    """

    # Test with a valid city name (e.g., New York)
    result = get_weather_data("New York", units="metric")
    assert result is not None
    assert result.name == "New York"
    assert result.units == "metric"
    
    # Test with an invalid city name
    result = get_weather_data("NonexistentCity", units="imperial")
    assert result is None

    # Test with a city name containing non-alphabet characters (e.g., numbers)
    result = get_weather_data("NewYork123", units="metric")
    assert result is None  # Updated assertion

    # Add more test cases to cover different scenarios:
    # - Test with other cities
    # - Test with various units (metric, imperial)
    # - Test with edge cases

    # For error cases, you can use try-except to capture exceptions and assert the expected behavior
    try:
        result = get_weather_data("InvalidCityName")
        assert result is None
    except Exception as e:
        assert str(e) == "City not found"

    # Repeat similar tests for different cities and units as needed
