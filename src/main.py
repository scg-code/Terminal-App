import os
from colorama import Fore, Style
from functions import get_weather_data, fetch_and_display_news
from ui import display_menu, display_weather  # Add this import statement
from termcolor import colored

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input(colored("Enter the name of a city: ", "yellow"))
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
