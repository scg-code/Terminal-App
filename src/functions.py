import requests
from termcolor import colored
import time
import pytest

# Replace 'YOUR_WEATHER_API_KEY' and 'YOUR_NEWS_API_KEY' with your actual API keys
weather_api_key = 'a44aca2461859377ce41b350169592be'
news_api_key = '79a4334874264492b20b867ced03d391'

# Define the base URL for the Weather API
weather_base_url = 'https://api.openweathermap.org/data/2.5/weather'
# Define the base URL for the News API
news_base_url = 'https://newsapi.org/v2/top-headlines'

# Define parameters for the Weather API request
weather_params = {
    'units': 'metric',  # You can change the units to 'imperial' if you prefer Fahrenheit
    'appid': weather_api_key,
}

# Define parameters for the News API request
news_params = {
    'country': 'us',  # Replace with the country of your choice
    'apiKey': news_api_key,
}

class WeatherData:
    def __init__(self, name, temp, temp_min, temp_max, units):
        self.name = name
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.units = units

    def temp_print(self):
        units_symbol = "°C"
        if self.units == "imperial":
            units_symbol = "°F"
        return f"In {self.name} it is currently {self.temp}{units_symbol}\n" \
               f"Today's high: {self.temp_max}{units_symbol}\n" \
               f"Today's Low: {self.temp_min}{units_symbol}"

def get_weather_data(city_name, units="metric"):
    params = {
        'q': city_name,
        'units': units,
        'appid': weather_api_key,
    }

    try:
        response = requests.get(weather_base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            city = data.get("name", "")
            temp = data.get("main", {}).get("temp", 0)
            temp_min = data.get("main", {}).get("temp_min", 0)
            temp_max = data.get("main", {}).get("temp_max", 0)
            return WeatherData(city, temp, temp_min, temp_max, units)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None

def fetch_and_display_news(get_user_input=input):
    try:
        # Send an HTTP GET request to the News API
        response = requests.get(news_base_url, params=news_params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Display only the top 5 articles with a typing effect
            for i, article in enumerate(data['articles'][:5], start=1):
                title = article['title']
                print(f"Article {i}: ", end="")
                for char in title:
                    print(char, end='', flush=True)
                    time.sleep(0.05)  # Adjust this value for typing speed
                print()

            while True:
                choice = get_user_input(colored("Enter an article number to view, (q) to quit, or (m) to return to the main menu: ", "blue"))
                if choice.lower() == "q":
                    break  # Quit and return to the main menu
                elif choice.lower() == "m":
                    return  # Return to the main menu
                try:
                    article_number = int(choice)
                    if 1 <= article_number <= len(data['articles'][:5]):
                        selected_article = data['articles'][article_number - 1]
                        print("=" * 40)
                        print(colored("Selected Article:", 'green'))  # Highlight the header in green
                        print("-" * 40)
                        description = selected_article['description']
                        print(f"Title: {selected_article['title']}")
                        print("Description: ", end="")
                        for char in description:
                            print(char, end='', flush=True)
                            time.sleep(0.05)  # Adjust this value for typing speed
                        print()
                        print(f"URL: {colored(selected_article['url'], 'blue')}")
                        print("=" * 40)
                    else:
                        print("Invalid article number. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid article number or 'q' to quit or 'm' to return to the main menu.")

        else:
            print(f"Error: Unable to fetch news - Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()