""""A client program written to verify correctness of the activity
classes.
"""
from shape import *
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""


def main():
    """Test the functionality of the methods encapsulated
    in this project.
    """

    # In the statements coded below, ensure that any statement that
    # could result in an exception is handled.  When exceptions are
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Code a statement which creates an instance of the Triangle
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle = Triangle("Red", 12, 12, 12)
        shapes.append(triangle)
    except ValueError as e:
        print(f"Shape creation failed {e}")

    # 3. Code a statement which creates an instance of the Rectangle
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle = Rectangle("Red", 8, 4)
        shapes.append(rectangle)
    except ValueError as e:
        print(f"Shape creation failed: {e}")

    # 4. Code 3 additional statements which creates an instance of
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        rectangle_blue = Rectangle("Blue", 16, 8)
        rectangle_pink = Rectangle("Pink", 4, 2)
        triangle_white = Triangle("White", 8, 8, 8)
        shapes.extend([rectangle_blue, rectangle_pink, triangle_white])
    except ValueError as e:
        print(f"Shape creation failed. {e}")

    # 5. Iterate through the list of shapes.
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        print(shape)
        shape.calculate_area()
        shape.calculate_perimeter()
        print(f"The perimeter of the shape is: {shape.perimeter}cm")
        print(f" The area of the shape is: {shape.area}cm squared")
        print("\n")

    # *** END PART 1 ***


if __name__ == "__main__":
    main()
