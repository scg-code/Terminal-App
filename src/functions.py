"""SkyScribe Functions Module

This module contains essential functions for the SkyScribe application. It handles
the retrieval of weather data, fetching and displaying news, and any other core
functions required for the application's functionality.

Functions:
- `get_weather_data`: Retrieves weather data for a specified location.
- `fetch_and_display_news`: Fetches and displays the latest news for the user.

External Dependencies:
- `requests`: Used for making HTTP requests to retrieve data.
- `termcolor`: Enables colored text output in the terminal.
- `time`: Provides timing-related functionality for certain operations.

Usage:
This module serves as the backend for the SkyScribe application, providing core
functionality. It is not meant to be run directly but is imported and utilized
by the main module.
"""

import time
import requests
from termcolor import colored


# Constants for Weather & News API keys
WEATHER_API_KEY = "a44aca2461859377ce41b350169592be"
NEWS_API_KEY = "79a4334874264492b20b867ced03d391"

# Constants for base URLs
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines"

# Define parameters for the Weather API request
WEATHER_PARAMS = {
    "units": "metric",  # Metric or fahrenheit
    "appid": WEATHER_API_KEY,
}

# Define parameters for the News API request
NEWS_PARAMS = {
    "country": "us",  # Country code for the news output
    "apiKey": NEWS_API_KEY,
}


class WeatherData:
    """Represents weather information for a city."""

    def __init__(self, name, temp, temp_min, temp_max, units):
        """Initialize a WeatherData instance.

        Args:
            name (str): The city name.
            temp (float): The current temperature.
            temp_min (float): The minimum temperature.
            temp_max (float): The maximum temperature.
            units (str): The unit of temperature (e.g., 'metric', 'imperial').

        Attributes:
            name (str): The city name.
            temp (float): The current temperature.
            temp_min (float): The minimum temperature.
            temp_max (float): The maximum temperature.
            units (str): The unit of temperature (e.g., 'metric', 'imperial').
        """
        self.name = name
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.units = units

    def temp_print(self):
        """Format and return weather information as a string.

        Returns:
            str: A formatted string containing weather information.
        """
        units_symbol = "°C"
        if self.units == "imperial":
            units_symbol = "°F"
        return (
            f"In {self.name} it is currently {self.temp}{units_symbol}\n"
            f"Today's high: {self.temp_max}{units_symbol}\n"
            f"Today's Low: {self.temp_min}{units_symbol}"
        )


def get_weather_data(city_name, units="metric"):
    """Retrieve weather data for a specified location.

    Args:
        city_name (str): The name of the city for which to retrieve weather data.
        units (str, optional): The unit of temperature (e.g., 'metric', 'imperial').
            Defaults to 'metric'.

    Returns:
        WeatherData: An instance of WeatherData containing weather information, or None
        if the city is not found or an error occurs.
    """
    # Validate the units parameter
    if units not in ["metric", "imperial"]:
        raise ValueError("Invalid units. Supported units are 'metric' and 'imperial'.")

    try:
        params = {
            "q": city_name,
            "units": units,
            "appid": WEATHER_API_KEY,
        }
        response = requests.get(WEATHER_BASE_URL, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "name" in data:
                city = data["name"]
                temp = data["main"]["temp"]
                temp_min = data["main"]["temp_min"]
                temp_max = data["main"]["temp_max"]
                return WeatherData(city, temp, temp_min, temp_max, units)
        else:
            print(f"Error: Weather data not found for {city_name}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
    return None


def fetch_and_display_news(get_user_input=input):
    """Fetch and display the latest news articles with user interaction.

    Args:
        get_user_input (callable, optional): A function for getting user input. Defaults to input.

    Returns:
        None: The function displays news articles and interacts with the user.
    """
    try:
        while True:
            # Send a HTTP GET request to the News API
            response = requests.get(NEWS_BASE_URL, params=NEWS_PARAMS, timeout=10)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Display only the top 5 articles with a slow typing effect
                for i, article in enumerate(data["articles"][:5], start=1):
                    title = article["title"]
                    print(f"Article {i}: ", end="")
                    for char in title:
                        print(char, end="", flush=True)
                        time.sleep(0.05)  # Value for typing speed effect
                    print()

                while True:
                    choice = get_user_input(
                        colored(
                            """Enter an article number to view or (q) to quit: """,
                            "blue",
                        )
                    )

                    if choice.lower() == "q":
                        return  # Quit and return to the main menu

                    try:
                        article_number = int(choice)
                        if 1 <= article_number <= len(data["articles"][:5]):
                            selected_article = data["articles"][article_number - 1]
                            print("=" * 40)
                            print(
                                colored("Selected Article:", "green")
                            )  # Highlight the header in green
                            print("-" * 40)
                            description = selected_article["description"]
                            print(f"Title: {selected_article['title']}")
                            print("Description: ", end="")
                            for char in description:
                                print(char, end="", flush=True)
                                # Adjusted value for typing speed
                                time.sleep(0.05)
                            print()
                            print(f"URL: {colored(selected_article['url'], 'blue')}")
                            print("=" * 40)
                        else:
                            print(
                                colored(
                                    "Invalid article number.,"
                                    "Please enter a valid number.",
                                    "red",
                                )
                            )
                    except ValueError:
                        print(
                            colored(
                                "Invalid input. Please enter a valid article,"
                                "number or 'q' to quit.",
                                "red",
                            )
                        )
            else:
                print(
                    f"Error: Unable to fetch news - Status Code: {response.status_code}"
                )
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
