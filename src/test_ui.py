"""
Unit Tests for SkyScribe UI Functions

This module contains unit tests for the UI functions in the SkyScribe application.
"""

from ui import display_menu, display_about
from unittest.mock import patch

def test_display_menu(capsys):
    """
    Test the display_menu function to ensure it displays the main menu correctly.
    """
    display_menu()
    captured = capsys.readouterr()
    assert "Main Menu:" in captured.out
    assert "1. Weather 🌤️" in captured.out
    assert "2. Latest News 🚨" in captured.out
    assert "3. About ℹ️" in captured.out
    assert "4. Quit" in captured.out

@patch('builtins.input', return_value="")
def test_display_about(mock_input, capsys):
    """
    Test the display_about function to ensure it displays about information correctly.
    """
    display_about()
    captured = capsys.readouterr()
    assert "About SkyScribe" in captured.out
    assert "Version: 1.0" in captured.out
    assert "Developer: Samuel Gifford" in captured.out
    assert "Description: SkyScribe provides up-to-date weather information," in captured.out
