"""
10. Create a python file named tuples_practices:
        10.1 Write a program that can display the palindrome strings from a tuple of string

                Ex:
                    words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

                    output:
                        Anna
                        Level

        10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5

        10.3 Write a program that can count the even and odd number from a tuple of integers

                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers
"""

words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

palindrome_words = []

for word in words:
    if word.lower() == word[::-1].lower():
        palindrome_words.append(word)
    else:
        continue

print(palindrome_words)

# 10.2:
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
for num in tuple1:
    if num in tuple2:
        print(num)
    else:
        continue

# python-remove-character-from-string
# https://builtin.com/software-engineering-perspectives/python-remove-character-from-string?i=450b0b0e-3adf-4a18-a45b-48af19281d8b&utm_source=transactional&utm_medium=email&utm_campaign=Built-In-Email

str1 = 'Anna4$'.lower()
s1 = "".join(c for c in str1 if c.isalpha())
print(s1)
s2 = "".join(reversed(s1))
print("Palindrome: ", s1 == s2)


s="Hello$ Python3$"
s1=s.replace("$","")
print ("Replacing/removing characters:",s1)


s = "Hello$@ Python3&_"
import re

s1 = re.sub("[^A-Za-z0-9]", "", s)  # replace everything other than A-Z, a-z , 0-9 with empty string in string s.
print(s1)

s = "Hello347 Python3$"
import re

s1 = re.sub("[0-9]", "", s)  # replace 0-9 with empty string in string s.
print(s1)

s = "Hello$@ Python3&"
f = filter(str.isalpha, s)
s1 = "".join(f)
print("Filtering alpha:", s1)

# 10.3:
even_count = 0
odd_count = 0
nums = (1, 2, 3, 4, 5, 6, 7)
for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"There are {even_count} even numbers and {odd_count} odd numbers")
