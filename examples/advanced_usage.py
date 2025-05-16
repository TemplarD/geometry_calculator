from typing import List
from geometry_calculator.shapes import Shape
from geometry_calculator import calculate_area, is_right_angled
from geometry_calculator.shapes import Circle, Triangle


def process_shapes(shapes: List[Shape]) -> None:
    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {calculate_area(shape):.2f}")
        print(f"Right-angled: {is_right_angled(shape)}")
        print()


shapes = [Circle(7), Triangle(5, 12, 13), Triangle(4, 5, 6)]

process_shapes(shapes)
