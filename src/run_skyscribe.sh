#!/bin/bash

# Check if Python 3 is available
if command -v python3 &> /dev/null
then
    cd "$(dirname "$0")"

    # List of required Python packages
    required_packages=("requests" "termcolor" "colorama" "tabulate" "pyfiglet")

    # Check and install dependencies
    for package in "${required_packages[@]}"; do
        if ! python3 -c "import $package" &> /dev/null; then
            echo "Installing $package..."
            python3 -m pip install $package
        fi
    done

    # Run the main application
    python3 main.py

else
    echo "Error: Python 3 is not installed on your system. Please install Python 3 to use this application."
    exit 1
fi

