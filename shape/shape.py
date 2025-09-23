"""This module defines the Shape class."""
from abc import ABC, abstractmethod
__author__ = "Seth Boyer"
__version__ = "1.0.0"


class Shape(ABC):
    """
    Initializes a shape object using received arguments (if valid)

    args:
    color(str) : The color of the object
    """

    def __init__(self, color: str):
        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError("Color cannot be blank.")

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculates the area of a given shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of a given shape
        """
        pass

    def __Str__(self) -> str:
        return (f"The shape color is {color}.")
