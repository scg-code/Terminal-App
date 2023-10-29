"""SkyScribe Main Module

This is the main module of the SkyScribe application. It serves as the entry point
for running the application and orchestrates the user interface and core functionality.

The main functionality includes displaying a user menu, fetching weather data, and
retrieving the latest news.

Modules:
- `ui`: User interface functions for displaying the application menu and weather information.
- `functions`: Functions for obtaining weather data and fetching and displaying news.

Dependencies:
- `colorama`: Provides color and style options for terminal output.
- `termcolor`: Allows for colored text output in the terminal.

Usage:
Run this module to start the SkyScribe application, which provides access to weather
information and the latest news.
"""

from colorama import Fore, Style
from termcolor import colored
from ui import display_menu, display_weather, display_about
from functions import get_weather_data, fetch_and_display_news


def main():
    """Run the SkyScribe application.

    This function serves as the entry point for the SkyScribe application.
    It displays a user menu, allows the user to fetch weather information or
    retrieve the latest news, and handles user interactions.

    Usage:
    Run this function to start the SkyScribe application.
    """
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input(colored("Enter the name of a city: ", "yellow"))
            weather_data = get_weather_data(city_name)
            display_weather(weather_data)
            input(
                "Press Enter to return..."
            )  # Wait for user input before displaying the menu
        elif choice == "2":
            print(Fore.BLUE + "\nFetching The Latest News..." + Style.RESET_ALL)
            fetch_and_display_news()
        elif choice == "3":
            display_about()  # Show the "About" section
        elif choice == "4":
            print(
                Fore.BLUE
                + "Goodbye! See you next time - SkyScribe"
                + Style.BRIGHT
                + "\033[4m"
                + ""
                + Style.RESET_ALL
            )
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
