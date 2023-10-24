import requests
from termcolor import colored
import time

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = '79a4334874264492b20b867ced03d391'

# Define the base URL for the News API
base_url = 'https://newsapi.org/v2/top-headlines'

# Define parameters for the API request
params = {
    'country': 'us',  # Replace with the country of your choice
    'apiKey': api_key,
}

try:
    # Send an HTTP GET request to the API
    response = requests.get(base_url, params=params)

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

        # Prompt the user to enter an article number
        article_number = int(input("Enter the article number to view: "))

        # Check if the selected article number is valid
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

    else:
        print(f"Error: Unable to fetch news - Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
