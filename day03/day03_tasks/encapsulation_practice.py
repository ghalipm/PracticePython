"""
2. Create a python file named encapsulation_practice:
    create a class called Item
    private variables:
    name, unit_price, quantity

    Encapsulate all the fields:
        Conditions:
        name can not be empty
        unit price can not be negative
        quantity can not be negative

    If invalid data are given to set the field, then make sure to throw an error
    during the runtime.
    (hint: you can use 'raise RuntimeError('Exception message')')


    Add a constructor that allows user to set all the fields when the object is created.
            (If the arguments not valid it should not be set to the instances)
    Methods:
        calcCost(): returns the total cost
        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()


"""


class Item:

    def __init__(self, name: str, unit_price: float, quantity: int):
        self.__name = name
        self.__unit_price = unit_price
        self.__quantity = quantity

    def set_name(self, name: str):
        if not name:
            raise RuntimeError('Name cannot be empty')
        self.__name = name

    def set_unit_price(self, unit_price: float):
        if unit_price < 0:
            raise RuntimeError('Unit price cannot be negative')
        self.__unit_price = unit_price

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise RuntimeError('Quantity cannot be negative')
        self.__quantity = quantity

    def calc_cost(self):
        return self.__unit_price * self.__quantity

    def __str__(self):
        return f'Name: {self.__name}, Unit Price: {self.__unit_price}, Quantity: {self.__quantity}, Total Cost: {self.calc_cost()}'


# Example usage:
try:
    item = Item("Widget", 10.0, 5)
    print(item)
except RuntimeError as e:
    print(f'Error: {e}')
