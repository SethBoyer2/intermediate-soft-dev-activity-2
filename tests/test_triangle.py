"""This module defines the TestTriangle class.

Usage:
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Seth Boyer"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle


class TestClient(unittest.TestCase):
    """Test suite used to test various functionalities of the triangle subclass"""

    def test_triangle_created_with_input_values(self):
        """Test to ensure that values are properly applied to bject"""
        triangle = Triangle("red", 12, 12, 12)

        self.assertEqual("red", triangle._color)

    def test_exception_raised_when_color_blank(self):
        """Ensure that an exception is raised when the color param is left blank"""
        with self.assertRaises(ValueError):
            Triangle("", 12, 12, 12)

    def test_exception_raised_when_side_1_not_integer(self):
        """Test to ensure that an exception is raised when side_1 is not an integer"""
        with self.assertRaises(ValueError):
            Triangle("red", "hi", 12, 12)

    def test_exception_raised_when_side_2_not_integer(self):
        """Test to ensure that an exception is raised when side_2 is not an integer"""
        with self.assertRaises(ValueError):
            Triangle("red", 12, "hi", 12)

    def test_exception_raised_when_side_3_not_integer(self):
        """Test to ensure that an exception is raised when side_3 is not an integer"""
        with self.assertRaises(ValueError):
            Triangle("red", 12, 12, "hi")

    def setUp(self):
        """Set up a triangle object for following tests"""
        self.triangle = Triangle("Red", 12, 12, 12)

    def test_str_returns_expected_output(self):
        expected = (
            "The shape color is Red.\n"
            " This triangle has three sides with lengths of 12cm, 12cm and 12cm."
        )
        self.assertEqual(expected, str(self.triangle))

    def test_calculate_area_returns_correct_value(self):
        """Test to ensure that calculate_area functions properly and returns correct value"""
        expected = 62.35
        self.triangle.calculate_area()
        self.assertEqual(self.triangle.area, expected)

    def test_calculate_perimeter_returns_correct_value(self):
        """Test to ensure calculate_perimeter functions properly and returns correct value"""
        expected = 36
        self.triangle.calculate_perimeter()
        self.assertEqual(self.triangle.perimeter, expected)
