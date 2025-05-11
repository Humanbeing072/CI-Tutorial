"""
This module contains unit tests for power functions:
square, cube, and fifth power.
"""

import pytest


# Function to test square
def square(num):
    """Returns the square of a number."""
    return num**2


# Function to test cube
def cube(num):
    """Returns the cube of a number."""
    return num**3


# Function to test fifth power
def fifth_power(num):
    """Returns the fifth power of a number."""
    return num**5


# Testing the square function
def test_square():
    """Tests the square() function."""
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"


# Testing the cube function
def test_cube():
    """Tests the cube() function."""
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"


# Testing the fifth power function
def test_fifth_power():
    """Tests the fifth_power() function."""
    assert fifth_power(2) == 32, "Test Failed: Fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: Fifth power of 3 should be 243"


# Test for invalid input
def test_invalid_input():
    """Tests that square() raises TypeError when input is a string."""
    with pytest.raises(TypeError):
        square("string")
