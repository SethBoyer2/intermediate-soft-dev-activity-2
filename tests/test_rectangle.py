"""This module defines the TestRectangle class.

Usage:
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Seth Boyer"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle


class TestClient(unittest.TestCase):
    """Test suite used to test various functionalities of the rectangle subclass."""

    def test_returns_object_with_expected_values(self):
        """Test to ensure values are properly applied to the object"""
        rectangle = Rectangle("Red", 8, 4)

        self.assertEqual("Red", rectangle._color)

    def test_exception_raised_when_color_blank(self):
        """Ensure that exception is raised if color param is blank"""
        with self.assertRaises(ValueError):
            Rectangle("", 8, 4)

    def test_exception_raised_when_length_invalid_type(self):
        """Ensure that exception is raised if length is not an integer"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("Red", "hi", 4)

    def test_exception_raised_when_width_invalid_type(self):
        """Ensure that excpetion is raised when width is not an integer"""
        with self.assertRaises(ValueError):
            Rectangle("Red", 8, "hi")

    def setUp(self):
        """Set up rectangle objet for following tests"""
        self.rectangle = Rectangle("Red", 8, 4)

    def test_str_returns_expected_output(self):
        """Ensure __str__ returns the expected string"""
        expected = (
            "The shape color is Red.\n"
            + " This rectangle has four sides, with the lengths of 8cm, 4cm, 8cm and 4cm"
        )
        self.assertEqual(expected, str(self.rectangle))

    def test_calculate_area(self):
        """Test calculate area to ensure it functions properly and returns correct value"""
        expected = 32
        self.rectangle.calculate_area()
        self.assertEqual(self.rectangle.area, expected)

    def test_calculate_perimeter(self):
        """Test calculate_perimter to ensure it functions properly and returns correct value"""
        expected = 24
        self.rectangle.calculate_perimeter()
        self.assertEqual(self.rectangle.perimeter, expected)
