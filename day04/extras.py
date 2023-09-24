from functools import reduce

print('---------------------closure-----------------')


def display_message():
    def method():
        for i in range(0, 5):
            print('Hello World')
            print('Hello Python')

    method()


display_message()


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s.lower()  # inner function - closure

    for s in strings:
        if is_palindrome(s):
            print(s)


print('Palindrome:')
display_palindromes(['anna', 'bella'])

print('--------map------------')
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums)

nums = list(map(lambda x: x * 10, nums))
print(nums)

names = ['Java', "JAVA", 'java', 'ruby', 'swift']

names = list(map(lambda x: str(x).lower(), names))
print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}

dictionary = dict(map(lambda t: (t[0], t[1] * 10), dictionary.items()))
print(dictionary)

print('--------------------filter---------------------')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [x for x in nums if x % 5 == 0]
print(nums2)

nums3 = list(filter(lambda x: x % 5 == 0, nums))
nums4 = list(filter(lambda x: not x % 5 == 0, nums))
print(nums3)
print(nums4)

print('===============reduce========')
print(reduce(lambda x, y: x + y, nums))

"""
Web automation:
    BeautifulSoap4
    request
    pytest
    robotframework

Web development:
    Django
    FastAPI
    flask
    ....
"""