import pytest
from functions import get_weather_data, fetch_and_display_news

# Define test data, such as a city for weather data retrieval
TEST_CITY = "Brisbane"

# Mock the requests module to avoid making actual HTTP requests
@pytest.fixture(autouse=True)
def mock_requests_get(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if "weather" in args[0]:
            return MockResponse(
                {"name": TEST_CITY, "main": {"temp": 15.0, "temp_min": 12.0, "temp_max": 18.0}},
                200,  # Set the status code to 200
            )
        elif "news" in args[0]:
            return MockResponse(
                {
                    "articles": [
                        {"title": "Article 1", "description": "Description 1", "url": "URL 1"},
                        {"title": "Article 2", "description": "Description 2", "url": "URL 2"},
                        {"title": "Article 3", "description": "Description 3", "url": "URL 3"},
                        {"title": "Article 4", "description": "Description 4", "url": "URL 4"},
                        {"title": "Article 5", "description": "Description 5", "url": "URL 5"},
                    ]
                },
                200,
            )

    monkeypatch.setattr("requests.get", mock_get)

# Test get_weather_data function
def test_get_weather_data():
    weather_data = get_weather_data(TEST_CITY)
    assert weather_data is not None
    assert weather_data.name == TEST_CITY

# Test fetch_and_display_news function
def test_fetch_and_display_news(capsys, monkeypatch):
    # Simulate user input during the test
    user_input = ["1", "q"]
    monkeypatch.setattr("builtins.input", lambda x: user_input.pop(0))

    # Capture printed output
    fetch_and_display_news()

    # Check the captured output to validate the behavior
    captured = capsys.readouterr()
    assert "Article 1: Article 1" in captured.out
    assert "Enter an article number to view, (q) to quit, or (m) to return to the main menu:" in captured.out
