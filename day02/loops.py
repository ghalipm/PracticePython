s = "Python"

for each in s:
    print(each)

print("--------------------------")
for i in range(0, 10):
    print(i)

print("===================================")
for i in range(0, len(s)):
    print(i, s[i])

print("================reversing a string===================")
for i in reversed(range(0, len(s))):
    print(i, s[i])

print("================reversing a string other option===================")
result = ''
for x in s[::-1]:
    result += x
print(result)

for i in range(1, 11):
    print(i, "Hello World")

print('--------------while loop--------------')
num = int(input("Enter a positive number:"))

while num <= 0:
    num = int(input("Enter a positive number:"))

print(f"You have entered {num}")

answer = input("Enter yes or no:")

while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input("Enter yes or no:")

print(f"You have entered {answer}")


