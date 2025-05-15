# Создание фигур
circle = Circle(5)
triangle = Triangle(3, 4, 5)

# Вычисление площадей
print(f"Площадь круга: {calculate_area(circle)}")
print(f"Площадь треугольника: {calculate_area(triangle)}")

# Проверка на прямоугольность
print(f"Треугольник прямоугольный? {is_right_angled(triangle)}")
print(f"Круг прямоугольный? {is_right_angled(circle)}")

# Добавление новой фигуры (пример)
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def is_right_angled(self):
        return True

square = Square(4)
print(f"Площадь квадрата: {calculate_area(square)}")
print(f"Квадрат прямоугольный? {is_right_angled(square)}")