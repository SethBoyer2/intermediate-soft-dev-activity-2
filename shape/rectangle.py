"""This module defines the Rectangle class."""

__author__ = "Seth Boyer"
__version__ = "1.0.0"

import math
from shape.shape import Shape


class Rectangle(Shape):
    """
    Initalize a rectangle object using given parameters (if valid)

    Args:
    color(str) : The color of the rectangle
    length (int) : The length of the rectangle
    width (int) : The width of the rectangle
    """

    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)

        if isinstance(length, int):
            self.__length = length
        else:
            raise ValueError

        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError

    def __str__(self):
        """
        Returns a readable string representation of the rectangle.

        Returns:
        str: Formatted string containing color, length and width.
        """
        return (
            super().__str__() +
            f"\n This rectangle has four sides, with the lengths of {self.__length}cm, "
            f"{self.__width}cm, {self.__length}cm and {self.__width}cm"
        )

    def calculate_area(self):
        """
        Calculate the area of a rectangle object using given parameters (if valid)

        Returns:
        area(float) : The area of the rectangle

        """
        self.area = self.__length * self.__width

        self.area = round(self.area, 2)

    def calculate_perimeter(self):
        """
        Calculate the perimeter of a rectangle object using given parameters (if valid)

        Returns:
        perimeter(float) : The perimeter of the rectangle
        """
        self.perimeter = (self.__length * 2) + (self.__width * 2)

        self.perimeter = round(self.perimeter, 2)
