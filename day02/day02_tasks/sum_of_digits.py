"""
6. Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
             Ex:
                 input: A1B2C3

                 output: 6
"""
str1 = "A1B2C3"
summed = 0

for char in str1:
    if char.isdigit():
        summed += int(char)
    else:
        continue

print(summed)
