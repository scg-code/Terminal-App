"""Test cases for the `get_weather_data` function."""

from functions import get_weather_data


def test_get_weather_data():
    """
    Test cases for the `get_weather_data` function.

    This module contains test cases for the `get_weather_data` function. It tests
    various scenarios, including valid and invalid city names, units, and edge cases.

    Test cases:
    1. Test with a valid city name (e.g., New York) in metric units.
        - Assert that the result is not None.
        - Assert that the city name and units in the result match the input.

    2. Test with an invalid city name in imperial units.
        - Assert that the result is None.

    3. Test with a city name containing non-alphabet characters (e.g., numbers) in metric units.
        - Assert that the result is None.

    4. Test error cases using try-except:
        - Test with a city name that does not exist.
        - Assert that the result is None."""

    # Test with a valid city name (e.g., New York) in metric units
    result = get_weather_data("New York", units="metric")
    assert result is not None
    assert result.name == "New York"
    assert result.units == "metric"

    # Test with an invalid city name in imperial units
    result = get_weather_data("NonexistentCity", units="imperial")
    assert result is None

    # Test with a city name containing non-alphabet characters (e.g., numbers)
    result = get_weather_data("NewYork123", units="metric")
    assert result is None

    # Test error cases using try-except
    try:
        result = get_weather_data("InvalidCityName")
        assert result is None
    except Exception as e:
        assert str(e) == "City not found"
