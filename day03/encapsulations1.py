class Person:

    def __init__(self, name='unknown', age=0):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise ValueError("Person name must be a string!")
        if name == '':
            raise ValueError("Person name cannot be empty!")
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Person age must be an integer!")
        if age < 0 or age > 150:
            raise ValueError(f"Invalid age {age}")
        self.__age = age


# only one constructor in Python

person1 = Person()
print(person1.get_name())
print(person1.get_age())

person2 = Person("James")
print(person2.get_name())
print(person2.get_age())

person3 = Person("James", 55)
print(person3.get_name())
print(person3.get_age())
