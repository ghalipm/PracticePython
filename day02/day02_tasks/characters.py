"""
5. Create a python file named characters, write a program that can retrieve the digits,
letters and special characters from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!
"""
letters = ''
digits = ""
special = ""

str1 = "mn@#123Ab!"
for char in str1:
    # if char.isdigit():
    if char.isdecimal():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        special += char

print(f"letters: {letters}")
print(f"digits: {digits}")
print(f"special: {special}")