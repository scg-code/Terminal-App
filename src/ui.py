import os
from tabulate import tabulate
from colorama import Fore, Style
from termcolor import colored
from pyfiglet import Figlet




def generate_welcome_text():
    custom_font = Figlet(font='slant')
    welcome_text = custom_font.renderText("SkyScribe.")
    colored_welcome_text = colored(welcome_text, 'blue',attrs=["bold"])
    return colored_welcome_text

def display_menu():
    os.system('clear')
    print(generate_welcome_text())
    print(colored("Your daily news & weather app.", "yellow", attrs=["bold"]))
    print("===================================")
    print(colored("Main Menu:\n", "blue", attrs=["bold"]))
    print("1. Weather 🌤️")
    print("2. Latest News 🚨")
    print("3. Quit")
    print("===================================")

def display_weather(weather_data):
    if weather_data:
        weather_info = weather_data.temp_print()
        print("\nWeather Information 🌤️")
        print("====================")
        print(tabulate([["City:", weather_data.name], ["Temperature:", f"{weather_data.temp}°C"],
                        ["High:", f"{weather_data.temp_max}°C"], ["Low:", f"{weather_data.temp_min}°C"]],
                       tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "Sorry, I couldn't retrieve weather information for that city." + Style.RESET_ALL)
