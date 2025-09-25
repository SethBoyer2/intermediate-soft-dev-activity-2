"""This module defines the TestTriangle class.

Usage:
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Seth Boyer"
__version__ = "1.0.0"

import unittest
from shape.shape import Shape
from shape.triangle import Triangle


class TestClient(unittest.TestCase):
    def test_triangle_created_with_input_values(self):
        triangle = Triangle("red", 12, 12, 12)

        self.assertEqual("red", triangle._color)

    def test_exception_raised_when_color_blank(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("", 12, 12, 12)

    def test_exception_raised_when_side_1_not_integer(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", "hi", 12, 12)

    def test_exception_raised_when_side_2_not_integer(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", 12, "hi", 12)

    def test_exception_raised_when_side_3_not_integer(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", 12, 12, "hi")

    def setUp(self):
        self.triangle = Triangle("Red", 12, 12, 12)

    def test_str_returns_expected_output(self):
        expected = (
            "The shape color is Red.\n"
            " This triangle has three sides with lengths of 12cm, 12cm and 12cm."
        )
        self.assertEqual(expected, str(self.triangle))

    def test_calculate_area_returns_correct_value(self):
        expected = 62.35
        self.triangle.calculate_area()
        self.assertEqual(self.triangle.area, expected)

    def test_calculate_perimeter_returns_correct_value(self):
        expected = 36
        self.triangle.calculate_perimeter()
        self.assertEqual(self.triangle.perimeter, expected)
