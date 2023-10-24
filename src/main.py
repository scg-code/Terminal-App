import os
from functions import get_weather_data, fetch_and_display_news
from tabulate import tabulate
from colorama import Fore, Style, Back, init
from termcolor import colored

def display_menu():
    # Clear the terminal screen and display the main menu.
    os.system('clear')  # This line clears the terminal screen (for macOS and Linux; use 'cls' for Windows)
    text = "Welcome to SkyScribe! - Your Portal to the Latest News and Weather Forecasts"
    formatted_text = colored(text, 'blue', attrs=['bold'])
    print(formatted_text)
    print("===================================")
    print("Main Menu:\n")
    print("1. Weather 🌤️")
    print("2. Latest News 🚨")
    print("3. Quit")
    print("===================================")

def display_weather(weather_data):
    # Display weather information in a structured format.
    if weather_data:
        weather_info = weather_data.temp_print()
        print("\nWeather Information 🌤️")
        print("====================")
        print(tabulate([["City:", weather_data.name], ["Temperature:", f"{weather_data.temp}°C"],
                        ["High:", f"{weather_data.temp_max}°C"], ["Low:", f"{weather_data.temp_min}°C"]],
                       tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "Sorry, I couldn't retrieve weather information for that city." + Style.RESET_ALL)

def main():
    # The main function that displays the menu and controls the user interface.
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter the name of a city: ")
            weather_data = get_weather_data(city_name)
            display_weather(weather_data)
            input("Press Enter to return...")  # Wait for user input before displaying the menu
        elif choice == "2":
            print(Fore.BLUE + "\nFetching The Latest News..." + Style.RESET_ALL)
            fetch_and_display_news()
        elif choice == "3":
            print(Fore.BLUE + "Goodbye! See you next time - " + Style.BRIGHT + '\033[4m' + "SkyScribe" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
