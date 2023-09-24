"""
21. Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.
    NOTE: MUST use ternary
"""
number = int(input("Enter a digit:"))
valid_digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
number_in_letter = ""

if number in valid_digits:
    if number == 0:
        number_in_letter = "zero"
    elif number == 1:
        number_in_letter = "one"
    elif number == 2:
        number_in_letter = "two"
    elif number == 3:
        number_in_letter = "three"
    elif number == 4:
        number_in_letter = "four"
    elif number == 5:
        number_in_letter = "five"
    elif number == 6:
        number_in_letter = "six"
    elif number == 7:
        number_in_letter = "seven"
    elif number == 8:
        number_in_letter = "eight"
    else:
        number_in_letter = "nine"
else:
    number_in_letter = "invalid"

print(f"Number {number} in letter: ", number_in_letter if number in valid_digits else f"Digit entered is {number_in_letter}")
