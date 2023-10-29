# T1-A3 Terminal Application
## SkyScribe - Weather and News Headlines Application
### Samuel Gifford
---


<div style="margin-top: 100px;"></div>

## 1.Github Repository Link:
[My Terminal APP T1-A3](https://github.com/scg-code/Terminal-App)


<div style="margin-top: 70px;"></div>

## 2. Code styling Conventions
The styling convention used for my code in the application follows the industry-standard PEP 8 style guide, which was created and is maintained by Python.org. PEP 8 provides a comprehensive set of guidelines that enhance code readability and maintainability, making it a widely adopted standard in the Python community.

To ensure that my code aligns with the PEP 8 style guide, I utilised the following tools:
Autopep8

Autopep8 is a utility that automatically formats Python code to comply with PEP 8 standards. It takes care of issues such as indentation, spacing, and code layout. To install Autopep8, you can use pip:

```python
pip install autopep8
```
Autopep8 can be applied to your Python code files using the following command:
```python
autopep8 your_code_name.py --in-place
```
This command formats the code in "your_code_name.py" according to PEP 8 guidelines, making your code more readable and adherent to best practices.

#### Pylint

Pylint is a code analysis tool that checks Python code for programming errors and adherence to coding standards, including PEP 8. It offers suggestions and recommendations for improving code quality. To install Pylint, you can use pip:
```python
pip install pylint
```
To analyze your Python code with Pylint use the following command:
```python
pylint your_code_name.py
```
Pylint will provide a detailed report, highlighting areas where your code can be enhanced for better readability and compliance with PEP 8.

#### Black
Black is an opinionated code formatter that automatically reformats your Python code to meet PEP 8 standards. It enforces a consistent coding style and eliminates debates over code formatting. To install Black, you can use pip:
```python
pip install black
```
You can format your code by running:
```python
black your_code_name.py
```
Black will ensure that your code adheres to PEP 8 guidelines by consistently formatting it, making your codebase more consistent and easier to read.

By incorporating these tools into the development process, I've maintained a clean and consistent coding style in the application, resulting in improved code quality and readability. This adherence to PEP 8 conventions enhances the maintainability of the project and contributes to a more efficient collaborative development environment.

---
<div style="margin-top: 70px;"></div>

## 3. SkyScribe Application Features

### 1. Real-Time Weather Information

Description: The "Real-Time Weather Information" feature allows users to obtain up-to-date weather data for a specified location. Users can input the name of a city, and the application fetches and displays essential weather information, including the current temperature, minimum temperature (low), and maximum temperature (high) for the day. This feature showcases:

* User Interaction: The application interacts with the user, prompting them to enter a city name.
* Data Retrieval: It retrieves weather data from an external source, specifically the OpenWeatherMap API, using an API key and HTTP requests.
* Data Display: The retrieved weather data is formatted and displayed in a user-friendly manner, including the city name, current temperature, and high and low temperatures for the day.
* Error Handling: The feature includes error handling to address potential issues like invalid city names and network-related errors.

![Weather](/docs/weather_Screenshot.png)


### 2. News Article Viewer

Description: The "News Article Viewer" feature provides users with access to the latest news articles from a reliable news source. Users can select an article to view in detail. This feature offers:

* News Retrieval: The application sends HTTP GET requests to a news API (NewsAPI) to fetch the latest news articles, and it supports additional user interaction.
* Interactive Interface: Users are presented with a list of the top 5 news articles with a typewriter-style animation. They can choose an article to view in detail or exit the news section.
* Article Details: When a user selects an article, the application displays the article title, description, and a URL to read the full article.
* Error Handling: The feature manages network-related issues and invalid user input, ensuring a smooth user experience.

![News](/docs/news_screenshot.png)


### 3. Colorful Text Output

Description: The "Colorful Text Output" feature enhances the application's user interface by incorporating colored text. This feature leverages third-party libraries like Colorama and Termcolor to apply different colors and styles to text elements. Key aspects of this feature include:

* Stylish Welcome Banner: The application starts with a stylish welcome banner generated using the PyFiglet library, which adds a visual appeal to the user interface.
* Color-Coded Menus: Menus and headings in the application are color-coded, making it visually appealing and easier to navigate.
* Highlighting Information: Important information and highlights within the application are presented using different text colors, enhancing readability and user engagement.
* Typing Effect: When displaying news article titles, a slow typing effect is used to add a dynamic element to the user experience.

These features collectively provide users with a visually engaging and user-friendly experience while delivering real-time weather information and the latest news articles. The application handles potential errors gracefully, ensuring a smooth user experience throughout.

![main menu](/docs/SkyScribe.png)


---
<div style="margin-top: 70px;"></div>

## 4. My Implementation Plan

For my implementation plan, I employed the project management tool `Linear`. Prior to diving into the code, I crafted a well-structured task list and established clear priorities within Linear's workspace. These tasks held pivotal milestones, including defining the project scope, conducting research on the data sources I would use, configuring essential tools and libraries, shaping the core program architecture, designing the user interface, implenting robust error handling, testing the application, and lastly crafting documentation in the form of a README.md file and slide deck using keynote. With this approach using Linear,  it laid the foundation for the development of my application `SkyScribe`. 

#### Day 1
![Day1](/docs/Day%201.png)


### Day 2
![Day2](/docs/Day%202.png)

#### Define Project Scope Complete ✅
![Day2.1](/docs/Complete%20project%20scope.png)

#### Research and Data Sources Complete ✅
![Day2.2](/docs/Research%20complete.png)

### Day 3-4
#### Completed Setting up tools & libraries and Main program structure
![Day3-4](/docs/Day%203-4.png)
#### Tools and Libraries Complete
![Day3-4](/docs/tools%20and%20libaries%20complete.png)
#### Main Program structure Complete
![Day3-4](/docs/Main%20program%20structure%20complete.png)

### Day 5
#### Completed Desinging User Interface
![Day5](/docs/Day%205.png)
![Day5](/docs/design%20UI%20complete.png)

### Day 5 Continued
#### Completed Testing
![Day5.5](/docs/Day5.5.png)
![Day5.5](/docs/testing%20complete.png)

### Day 6
#### Completed Error handling and README.md
![Day6](/docs/Day%206.png)

![Day6](/docs/Error%20Handling%20complete.png)
![Day6](/docs/Readme-complete.png)

### Day 7
#### Completed Slide Deck
![Day7](/docs/Day%207.png)
![Day7](/docs/Slidedeck-complete.png)

### Day 8
#### Final Review
![Day8](/docs/Day%208.png)
![Day8](/docs/Final%20review%20complete.png)




---
<div style="margin-top: 70px;"></div>

## 5. Running the SkyScribe Application

After you've downloaded and unzipped the SkyScribe source code, follow these steps to run the application:

1. **Open a Terminal:**
   - Open your terminal or command prompt.

2. **Navigate to the Source Code Directory:**
   - Change your working directory to the location of the extracted source code. You can do this with the `cd` command. For example, if the source code is in your Downloads directory:
     ```bash
     cd ~/Downloads/SamuelGifford_T1A3/src
     ```

3. **Execute the Bash Script:**
   - Run the provided bash script to start the SkyScribe application:
     ```bash
     bash run_skyscribe.sh
     ```

4. **Execute Permission Fix (if needed):**
   - If you encounter a permission error when trying to run the script, change the script's permissions to executable by running the following command before retrying step 3:
     ```bash
     chmod +x run_skyscribe.sh
     ```



![bash_script](/docs/bash_Script.png)

The application will launch, providing access to real-time weather information and the latest news. Follow the on-screen instructions to use the application.

**Note:** If you're not already in the `src` directory, make sure to navigate to that directory before running the script as described in step 2.


## 3. Dependencies

SkyScribe relies on the following external Python libraries:

- `requests`: Used to make HTTP requests for data retrieval.
- `termcolor`: Enables colored text output in the terminal.
- `colorama`: Provides additional color and style options.
- `tabulate`: Used for tabular formatting of data in the user interface.
- `pyfiglet`: Generates stylish text for the welcome banner.
- `os`: Part of the Python standard library, used for system-specific operations.
- `time`: Part of the Python standard library, provides timing-related functionality.

These dependencies are automatically installed when you run the bash script.

## 4. System Requirements

SkyScribe is designed to run on a variety of platforms. It has the following system requirements:

- A computer running a modern operating system (Windows, macOS, Linux).
- Python 3.x installed on the system.

## 5. Command Line Arguments

SkyScribe accepts the following command line arguments:

- `bash run_skyscribe.sh` (No arguments): Start the application with the main menu.

The application will guide you through its features using the menu options. To interact with the weather and news features, simply follow the on-screen instructions.

---

## 6. Usage Instructions

Once you've installed SkyScribe, follow these basic usage instructions:

1. **Launching the Application:**
   - Open your terminal or command prompt.

2. **Running the Application:**
   - Execute the provided bash script, `run_skyscribe.sh`, to start the SkyScribe application.

3. **Main Menu:**
   - The main menu provides options to access real-time weather information, the latest news, or information about the application.

4. **Accessing Weather Information:**
   - Choose the weather option from the menu.
   - Enter the name of a city to view real-time weather data.

5. **Reading News Articles:**
   - Select the news option from the menu.
   - The application will display the top 5 news articles for that day.
   - Enter the article number to view details, or press 'q' to return to the menu.

6. **Exiting the Application:**
   - Select the "Quit" option from the main menu to exit the application.

---

## 6. Testing Methods

### 1. Unit Tests for SkyScribe UI Functions
This module contains unit tests for the UI functions in the SkyScribe application.

**Methods Tested:**
- `display_menu`: Tests the display_menu function to ensure it displays the main menu correctly.
- `display_about`: Tests the display_about function to ensure it displays about information correctly.

**How They Were Tested:**

1. **Test for `display_menu` Function:**
   - Display the main menu using `display_menu`.
   - Capture the output using `capsys.readouterr()`.
   - Assert that the captured output contains specific menu items (e.g., "Main Menu," "Weather," "Latest News," "About," and "Quit").

2. **Test for `display_about` Function:**
   - Display the "About" information using `display_about`.
   - Capture the output using `capsys.readouterr()`.
   - Assert that the captured output contains information such as "About SkyScribe," version, developer, and description.

### 2. Test Cases for the `get_weather_data` Function
This module contains test cases for the `get_weather_data` function. It tests various scenarios, including valid and invalid city names, units, and edge cases.

**Methods Tested:**
- `get_weather_data`: Tests the `get_weather_data` function to retrieve weather data for a specified location.

**Test Cases:**
1. Test with a valid city name (e.g., New York) in metric units:
   - Assert that the result is not None.
   - Assert that the city name and units in the result match the input.

2. Test with an invalid city name in imperial units:
   - Assert that the result is None.

3. Test with a city name containing non-alphabet characters (e.g., numbers) in metric units:
   - Assert that the result is None.

4. Test error cases using try-except:
   - Test with a city name that does not exist.
   - Assert that the result is None.

### 3. Unit Tests for News API Access
This module contains unit tests for accessing the News API to ensure it returns a valid response.

**Methods Tested:**
- `test_news_api`: Tests the News API access to check whether the API access is working correctly and that it responds with a status code of 200.

**How It Was Tested:**
1. Make an API request to the News API using a valid API key and parameters.
2. Check whether the API responds with a status code of 200, indicating a successful request.


## 7. Running Tests (Bash Script)

To run the unit tests for the SkyScribe application, you can use a provided bash script that automates the process. Follow these steps:

1. **Open a Terminal:**
   - Open your terminal or command prompt.

2. **Navigate to the Application Directory:**
   - Ensure you are in the directory where you unzipped the SkyScribe application source code. If not, use the `cd` command to navigate to the application directory:
     ```bash
     cd path/to/SamuelGifford_T1A3/src
     ```

3. **Execute the Test Script:**
   - Run the following command to execute the test script:
     ```bash
     bash run_tests.sh
     ```

   This script will automatically check for and install `pytest` if it's not already installed and then run the following tests:
   - UI Function Tests
   - Weather Function Tests
   - News Function Tests

   The results of the tests will be displayed in your terminal.

![bash_script](/docs/test%20bash%20script.png)

