name = "Python"

print(len(name))
print(name[0])  # P
print(name[-1])  # n
print(name[-2])  # o

s = "Java Programming Languague"

s2 = s[5:16]  # string slicing, no substring
s3 = s[:4]
print(s2)
print(s3)

s4 = s[::-1]  # reverses the string after slicing
print("s4:", s4)

s = 'Python Programming'
s5 = reversed(s)  # s5 no longer string
print("s5:", s5)
print(type(s5))

s6 = s[7:]
print(s6)

s7 = "CYDEO SCHOOL"

s = 'Python Programming. java programming.'

s8 = s.upper()  # PYTHON PROGRAMMING. JAVA PROGRAMMING.
print(s8)
s9 = s.capitalize()
print(s9)
s10 = s.title()  # Python Programming. Java Programming.
print(s10)

s = "               Python        "
t1 = s.strip()
print(t1)

print(t1.index('P'))
print(t1.index('n'))

s = 'Java Java'
s = s.replace('Java', 'Python', 1)
print(s)

s = 'C#, C#, Java'
s1 = s.replace(' C#', 'Java' )
print(s1)

count_c=s.count('C#')
print(count_c)

s1='java'
s2='JAVA'

print(s1==s2)
print(s1.lower()==s2.lower())

print(s1.islower())
print(s2.isupper())

s="12"
print(s.isdigit())

s='Cydeo School'
print(s.istitle())

# methods in python must be created in a class and they self keyword,
# function is created outside the class
