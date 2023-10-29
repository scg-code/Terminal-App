"""
Unit Tests for News API Access

This module contains unit tests for accessing the News API to ensure it returns a valid response.
It checks whether the API access is working correctly and that it responds with a status code of 200.

External Dependencies:
- `pytest`: Used for running unit tests.
- `requests`: Used for making HTTP requests to the News API.

Usage:
Run this module to perform the tests and verify that the News API access is functioning as expected.
"""
import pytest
import requests


def test_news_api():
    """
    Test the News API access.

    This test makes an API request to the News API to ensure that the API access is working correctly.
    It checks whether the API responds with a status code of 200, indicating a successful request.
    """

    NEWS_API_KEY = "79a4334874264492b20b867ced03d391"
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines"
    NEWS_PARAMS = {
        "country": "us",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_BASE_URL, params=NEWS_PARAMS, timeout=10)
    # Check if the response status code is 200, indicating success
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
