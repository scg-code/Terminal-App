"""SkyScribe User Interface Module

The `ui.py` module is responsible for providing a user-friendly interface for the
SkyScribe application. It includes functions to create and display the application
menu, as well as to format and display weather information in an aesthetically pleasing
manner.

Functions:
- `generate_welcome_text`: Generates a stylish welcome banner for the application.
- `display_menu`: Displays the main menu for user interaction.
- `display_weather`: Formats and displays weather information to the user.
- `display_about`: Displays information about the application.

External Dependencies:
- `os`: Utilized for system-specific operations such as clearing the terminal screen.
- `tabulate`: Enables tabular formatting of data for user-friendly display.
- `colorama`: Provides color and style options for terminal text.
- `termcolor`: Supports colored text output in the terminal.
- `pyfiglet`: Used for generating stylish text for the application banner.

Usage:
Import and use the functions from this module in the main module to create a user-friendly
interface for the SkyScribe application. This module is not meant to be run directly.
"""

import os
from tabulate import tabulate
from colorama import Fore, Style
from termcolor import colored
from pyfiglet import Figlet


def generate_welcome_text():
    """Generate a stylish welcome banner for the application.

    Returns:
        str: The welcome banner text with styling.
    """
    custom_font = Figlet(font="slant")
    welcome_text = custom_font.renderText("SkyScribe.")
    colored_welcome_text = colored(welcome_text, "blue", attrs=["bold"])
    return colored_welcome_text


def display_menu():
    """Display the main menu for user interaction."""
    os.system("clear")
    print(generate_welcome_text())
    print(colored("Your daily news & weather app.", "yellow", attrs=["bold"]))
    print("===================================")
    print(colored("Main Menu:\n", "blue", attrs=["bold"]))
    print("1. Weather 🌤️")
    print("2. Latest News 🚨")
    print("3. About ℹ️")
    print("4. Quit")
    print("===================================")


def display_weather(weather_data):
    """Format and display weather information to the user.

    Args:
        weather_data (WeatherData): An instance of WeatherData containing weather information.

    If weather_data is None, a message indicating the inability to retrieve weather
    information will be displayed.
    """
    if weather_data:
        print("\nWeather Information 🌤️")
        print("====================")
        print(
            tabulate(
                [
                    ["City:", weather_data.name],
                    ["Temperature:", f"{weather_data.temp}°C"],
                    ["High:", f"{weather_data.temp_max}°C"],
                    ["Low:", f"{weather_data.temp_min}°C"],
                ],
                tablefmt="fancy_grid",
            )
        )
    else:
        print(
            Fore.RED
            + "Sorry, I couldn't retrieve weather information for that city."
            + Style.RESET_ALL
        )


def display_about():
    """Display information about the application."""
    os.system("clear")
    print(generate_welcome_text())
    print(colored("About SkyScribe", "blue", attrs=["bold"]))
    print("===================================")
    print("SkyScribe is your daily news and weather app.")
    print("Version: 1.0")
    print("Developer: Samuel Gifford")
    print("Description: SkyScribe provides up-to-date weather information,"
          "and the latest news headlines.")
    input("Press Enter to return to the main menu...")
