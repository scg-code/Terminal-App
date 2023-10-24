import requests

# Define your OpenWeatherMap API key and base URL
api_key = 'a44aca2461859377ce41b350169592be'
base_url = 'https://api.openweathermap.org/data/2.5/weather'

class WeatherData:
    def __init__(self, name, temp, temp_min, temp_max, units):
        self.name = name
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.units = units

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        return f"In {self.name} it is currently {self.temp}°{units_symbol}\n" \
               f"Today's high: {self.temp_max}°{units_symbol}\n" \
               f"Today's Low: {self.temp_min}°{units_symbol}"

def get_weather_data(city_name, units="metric"):
    params = {
        'q': city_name,
        'units': units,
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
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

if __name__ == "__main__":
    while True:
        city_name = input("Enter the name of the city (or 'q' to quit): ")
        if city_name.lower() == 'q':
            break

        weather_data = get_weather_data(city_name)
        if weather_data:
            weather_info = weather_data.temp_print()
            print(weather_info)
        else:
            print("Sorry, I couldn't retrieve weather information for that city.")
