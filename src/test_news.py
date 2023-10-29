"""
Unit Tests for News API Access

This module contains unit tests for accessing the News API to ensure it returns a valid response.
It checks whether the API access is working correctly and that it responds with a status code of 200.

External Dependencies:
- `pytest`: Used for running unit tests.
- `requests`: Used for making HTTP requests to the News API.

Usage:
Run this module to perform the tests and verify that the News API access is functioning as expected.
Ensure that the NEWS_API_KEY is set to your actual News API key before running the tests.

Note: The NEWS_API_KEY must be valid for the tests to work as expected.
"""
import pytest
import requests

def test_news_api():
    """
    Test the News API access.

    This test makes an API request to the News API to ensure that the API access is working correctly.
    It checks whether the API responds with a status code of 200, indicating a successful request.

    External Dependencies:
    - `requests`: Used for making HTTP requests.

    Usage:
    Run this test to verify that the News API is accessible and returns a valid response.

    API Key:
    Replace the value of NEWS_API_KEY with your actual News API key before running the test.
    """
    NEWS_API_KEY = "79a4334874264492b20b867ced03d391"  # Replace with your actual API key
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines"
    NEWS_PARAMS = {
        "country": "us",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_BASE_URL, params=NEWS_PARAMS, timeout=10)
    assert response.status_code == 200  # Check if the response status code is 200, indicating success

if __name__ == '__main__':
    pytest.main()
