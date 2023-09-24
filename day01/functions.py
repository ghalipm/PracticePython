"""
in python, function and methods are slightly different, in java it was the same.
"""
import numbers


def display_message():
    print('Hello')
    print('Good day')


display_message()


def value():
    # return 1
    return 'Hello'


print(value())


def return_int() -> int:
    return 10


print(return_int())


def square(num: int):
    return num * num


print(square(5))
print(square(5.0))


def add1(num1: float, num2: float):
    return num1 + num2


def add2(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add2(5, 4))
print(add2(5.5, 4.5))

print('---------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 5, '-'))
print(calculate(10, 5, '+'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))


# in python no need for method overloading: dynamic typed
# Java is a statically typed and Python is a dynamically typed.
# Python is strongly but dynamically typed.

def sum(num1: numbers, num2: numbers, num3: numbers = 0, num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + num4


print(sum(2, 5))
print(sum(2, 5, 3))
print(sum(2, 5, 3, 4))

print("============== Function ==================")


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')
concat('Python', 3)
concat('Python', 3, '2.5')
concat('Python', 3, '2.5', True)
concat('Python', 3, '2.5', True, False)
