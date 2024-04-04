import math

class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def set_radius(self, radius):
        self.radius = radius

    def set_color(self, color):
        self.color = color

    def get_area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle [radius={self.radius}, color={self.color}]"

class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0, color="red"):
        super().__init__(radius, color)
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_volume(self):
        return self.get_area() * self.height

    def __str__(self):
        return f"Cylinder [radius={self.get_radius()}, color={self.get_color()}, height={self.height}]"


if __name__ == "__main__":
    circle = Circle(radius=3.0, color="blue")
    print("Circle:")
    print(circle)
    print("Area:", circle.get_area())
    print()

    cylinder = Cylinder(radius=2.0, height=5.0, color="green")
    print("Cylinder:")
    print(cylinder)
    print("Volume:", cylinder.get_volume())