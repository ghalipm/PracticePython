"""
1. Create a python file named list_practices:

1.5 Write a program that can display the common elements of two lists:
		Ex:
		list1 = [1,2,3,4,5]
		list2 = [4,5,6,7,8]

		Output:
				4
				5

1.6 Write a program that can remove the duplicated elements from a list
	Ex:
	elements = [1,2,3,4,5,1,2,3,4,5]

	Output:
    	[1, 2, 3, 4, 5]

		Notes: Do Not use Set


1.7 Write a program that can remove string elements from a list if the firt and last characters of the string are same
    ex:
		list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

	output:
		["Lan", "Ebrahim", "Farida"]


1.8  Write a program that can display the unique elements of an arrayList:
	ex:
    	list = [1, 1, 2, 3, 3, 4, 5, 5]

	output:
	    	[2, 4]

"""

"""
1.1 Write a program that can move all the zeros to the last indexes of ArrayList
   Ex:
   list: [1,0,2,0,3,0,4,0]

    output:  [1, 2, 3, 4, 0, 0, 0, 0]
"""
int_list = [1, 0, 2, 0, 3, 0, 4, 0]


def zero_filter(input_list: list):
    size = len(input_list)
    new_list = []
    for i in range(0, size):
        print(input_list[i])
        if input_list[i] != 0:
            new_list.insert(i, input_list[i])
        else:
            continue

    for i in range(len(new_list), size):
        new_list.append(0)

    return new_list


print("Newly ordered list:", zero_filter(int_list))

"""
1.2 write a program that can multiply each odd number by 2
   ex:
    list = [1,2,3,4,5];
    output: [2,2,6,4,10]
"""

int_list = [1, 2, 3, 4, 5]


def odd_num_multiplier(input_list: list):
    n = len(input_list)
    for i in range(0, n):
        if input_list[i] % 2 == 1:
            input_list[i] *= 2
        else:
            continue

    return input_list


print("New Odd Number List:", odd_num_multiplier(int_list))

"""
1.3 Write a program that can remove all the names "Ahmed" from a list of strings
Ex:
 list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

output:
["John", "Daniel", "James", "Muhammed"]
"""
name_list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]


def name_filter(names_list: list, name_to_remove: str):
    while name_to_remove in names_list:
        names_list.remove(name_to_remove)
    return names_list


print(name_filter(name_list, "Ahmed"))

"""
1.4 Write a program that can display the palindrome 
strings from a list of String

Ex:
words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

output:
    Anna
    Level

"""


def palindrome(word: str):
    return word.lower() == word[::-1].lower()
    # word[::-1] is reversed string of word,
    # but reversed(word) is not a string


# print("Level:", palindrome("Level"))


def filter_palindrome(word_list: list):
    for word in word_list:
        print("word:", word)
        if word.lower() != palindrome(word.lower()):
            print("Not palindrome:", word)
            word_list.remove(word)

    return word_list


words: list = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

print("Palindromes:", filter_palindrome(words))

"""
1.5 Write a program that can display the common elements of two lists:
Ex: 
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

Output:
4
5
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_list = []

for x in list1:
    if x in list2:
        common_list.append(x)

print(common_list)

"""
1.6 Write a program that can remove the duplicated elements from a list
Ex:
elements = [1,2,3,4,5,1,2,3,4,5]

Output:
[1, 2, 3, 4, 5]
Notes: Do Not use Set
"""
elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

non_duplicates = []
for x in elements:
    if x not in non_duplicates:
        non_duplicates.append(x)
    else:
        continue

print("Non duplicate elements: ", non_duplicates)

"""
1.7 Write a program that can remove string elements from a list 
if the first and last characters of the string are same
ex:
list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

output:
["Lan", "Ebrahim", "Farida"]
"""
name_list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}
new_list2 = []
for x in name_list:
    if x[0].lower() != x[-1].lower():
        new_list2.append(x)

print(new_list2)

"""
1.8  Write a program that can display the unique elements of an arrayList:
ex:
list = [1, 1, 2, 3, 3, 4, 5, 5]

output:
[2, 4]

"""
mix_list = [1, 1, 2, 3, 3, 4, 5, 5]

unique_list = []

for x in mix_list:
    if mix_list.count(x) == 1:
        unique_list.append(x)
    else:
        continue

print("Unique elements list: ", unique_list)
