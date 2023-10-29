#!/bin/bash

# Check if pytest is installed, and install it if not
if ! command -v pytest &> /dev/null; then
    echo "pytest is not installed. Installing..."
    pip install pytest
fi

# Run the UI tests
echo "Running UI Tests..."
python -m pytest test_ui.py

# Run the Weather function tests
echo "Running Weather Function Tests..."
python -m pytest test_function_weather.py

# Run the News function tests
echo "Running News Function Tests..."
python -m pytest test_news.py
