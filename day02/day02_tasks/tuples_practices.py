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

