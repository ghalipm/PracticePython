# arithmetic operators: +,-, *, /, %

print(10 - 2)
print(10 + 2)
print(10 * 2)
print(10 / 2)
# not int, but float
print(int(10 / 2))
print(10 / 3)
# not int, but float
print(10 % 3)

a = 10
print(a)
a -= 2
print(a)

a = 100
print(a)
a += 5
print(a)

# logical operators: and, or, not
s = 'Hello World'
print('H' and 'W' in s)
print(True and True)
print(True and False)
print(True or False)

print('Java' or 'C#' in s)
print('Java' not in s)

age = 27
citizenship = 'US'
is_eligible = age > 18 and citizenship == 'US'
print(is_eligible)

print('=========================')
s1 = 'Java'
s2 = 'Java'
print(s1 == s2)
print(s1 is s2)  # check if two variables are referencing to the same objects

