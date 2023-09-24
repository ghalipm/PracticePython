"""
16. Create a python file named fizz_buzz, write a program that asks user to enter an integer and
prints "Fizz" if the number is divisible by 3, prints "Buzz" if the number is divisible by 5,
and prints FizzBuzz if the number is divisible by both 3 and 5.

            Ex:
                number 15
            Output:
                FizzBuzz
"""
num = int(input("Enter an integer: "))
word = ""

if num % 3 == 0:
    if num % 5 == 0:
        word = "FizzBuzz"
    else:
        word = "Fizz"
elif num % 5 == 0:
    word = "Buzz"
else:
    word = "Neither Fizz or Buzz"

print(word)

