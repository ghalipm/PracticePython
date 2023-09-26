"""
3. Create a python file named inheritance_practice:
    Create an abstract class named Animal:
    Variables: name, breed(final), gender(final),  age, size, color(final)
    Encapsulate all the fields
    Add a constructor that can set all the fields

Methods:
    eat() ==> different animals eat different foods
    drink() ==> all the animals drink water
    toString() ==> to display the full info of the animal


Create the following subclasses of Animal:
Dog
eat(): Dog Food

Cat
eat(): Cat Food

Parrot
eat(): Eagle
Displaying 1695215245435-practice_tasks3.txt.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, breed: str, gender: str, age: int, size: int, color: str):
        self.__name = name
        self.__breed = breed
        self.__gender = gender
        self.__age = age
        self.__size = size
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def breed(self):
        return self.__breed

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @property
    def size(self):
        return self.__size

    @property   # kind of final
    def color(self):
        return self.__color

    @abstractmethod
    def eat(self):
        pass

    def drink(self):
        return 'Water'

    def __str__(self):
        return f'Name: {self.__name}, Breed: {self.__breed}, Gender: {self.__gender}, Age: {self.__age}, Size: {self.__size}, Color: {self.__color}'


class Dog(Animal):
    def eat(self):
        return 'Dog Food'


class Cat(Animal):
    def eat(self):
        return 'Cat Food'


class Parrot(Animal):
    def eat(self):
        return 'Eagle'
