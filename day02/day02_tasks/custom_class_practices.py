"""
9. Create a python file named custom_class_practices:
        9.1 Create a custom class named Pizza:
        Attributes:
            size, numberOfCheeseTopping, numberOfPepperoniTopping

            Add a constructor that can set all the fields

        Actions:
            calcCost(): returns the totalCost of the pizza
            __str__():returns a String containing the pizza size, quantity of each topping, and the pizza cost as calculated by calcCost()

        Pizza cost is determined by:
                        S: $10 + $2 per topping
                        M: $12 + $2 per topping
                        L: $14 + $2 per topping



        9.2 Create a class named Circle:
                Attributes:
                    instance: radius
                    static: pi

                Add a constructor that can set All the fields (instances)

                Actions:
                    calcArea(): returns the area of Circle

                    calcPerimeter(): returns the perimeter of Circle

                    __str__(): displays the radius, diameter, pi, area and perimeter of the circle
                    when the object of circle is passed in the print statement


"""
import math

import numbers


class Pizza:
    def __init__(self, size: str, number_of_cheese_topping: numbers, number_of_pepperoni_topping: numbers):
        self.size = size
        self.number_of_cheese_topping = number_of_cheese_topping
        self.number_of_pepperoni_topping = number_of_pepperoni_topping

    def calc_cost(self):
        base_cost = 0
        if self.size == 'S':
            base_cost = 10
        elif self.size == 'M':
            base_cost = 12
        elif self.size == 'L':
            base_cost = 14

        topping_cost = 2 * (self.number_of_cheese_topping + self.number_of_pepperoni_topping)
        total_cost = base_cost + topping_cost
        return total_cost

    def __str__(self):
        return f"Size: {self.size}\nCheese Toppings: {self.number_of_cheese_topping}\nPepperoni Toppings: {self.number_of_pepperoni_topping}\nTotal Cost: ${self.calc_cost()}"


# Example usage:
pizza1 = Pizza('M', 2, 1)
print(pizza1)


# 9.2:
print("========================================================")
class Circle:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return self.pi * self.radius ** 2

    def calcPerimeter(self):
        return 2 * self.pi * self.radius

    def __str__(self):
        diameter = 2 * self.radius
        return f"Radius: {self.radius}\nDiameter: {diameter}\nPi: {self.pi}\nArea: {self.calcArea()}\nPerimeter: {self.calcPerimeter()}"


# Example usage:
circle1 = Circle(5)
print(circle1)
