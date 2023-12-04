from math import pi
import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a < 0 and b < 0 and c < 0:
            raise Exception("Invalid triangle!")
        else:
            self.a = a
            self.b = b
            self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def main():
    circle = Circle(8)
    print(circle.area(), circle.perimeter())

    rectangle = Rectangle(5, 5)
    print(rectangle.area(), rectangle.perimeter())

    triangle = Triangle(8, 9, 7)
    print(triangle.area(), triangle.perimeter())


main()
