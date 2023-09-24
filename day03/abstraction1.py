import numbers
from abc import ABC, abstractmethod


# abc: module name
# ABC: Abstract class in abc module
class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape, ABC):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


square = Square(5)
print(square.area())


class Circle(Shape):
    pass


class Volume:
    pass


class Cube(Shape, Volume, ABC):
    pass


class Rectangle(Shape, ABC):
    pass


class Volume(ABC):
    pass


class Cylinder(Shape, Volume, ABC):
    pass
