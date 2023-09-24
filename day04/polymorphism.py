from day03.abstraction1 import Shape, Square, Rectangle

shape: Shape = Square(5)

shape2: Shape = Rectangle(3, 5)


def display_area(shape: Shape):
    print(f" the{shape.name}\' area is {shape.area()}")

# need to be checked, first day3 Shape
