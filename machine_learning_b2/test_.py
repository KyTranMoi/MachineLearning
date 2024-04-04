from circle import *
if __name__ == "__main__":
    circle = Circle(radius=3.0, color="blue")
    print(circle)
    print("Area:", circle.get_area())
    cylinder = Cylinder(radius=2.0, height=5.0, color="green")
    print(cylinder)
    print("Volume:", cylinder.get_volume())
