from geometry_calculator import Circle, Triangle

circle = Circle(5)
print(f"Circle area: {circle.area():.2f}")

triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area()}")
print(f"Is right-angled? {triangle.is_right_angled()}")
