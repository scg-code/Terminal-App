import npyscreen

class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="SkyScribe - Latest Headlines and Weather Forecasts")

class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="Welcome to SkyScribe!")
        self.add(npyscreen.FixedText, value="Your Portal to the Latest Headlines and Weather Forecasts!")
        self.add(npyscreen.FixedText, value="1. Weather")
        self.add(npyscreen.FixedText, value="2. Latest News")
        self.add(npyscreen.FixedText, value="3. Quit")
        self.choice = self.add(npyscreen.TitleText, name="Enter your choice:")

    def on_ok(self):
        choice = self.choice.value
        if choice == "1":
            self.parentApp.switchForm("WEATHER")
        elif choice == "2":
            self.parentApp.switchForm("NEWS")
        elif choice == "3":
            self.parentApp.switchForm(None)

class WeatherForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="Weather Data")
        self.city = self.add(npyscreen.TitleText, name="Enter the name of a city:")
        self.weather_info = self.add(npyscreen.TitleText, name="Weather Info:")

    def on_ok(self):
        city_name = self.city.value
        # Get weather data and display it here

class NewsForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, value="Latest News")
        # Fetch and display news articles here

if __name__ == '__main__':
    app = MyApplication()
    app.run()
