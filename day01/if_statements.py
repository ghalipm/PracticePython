a = 2
if a == 2:
    print('Python')
print("Java")

print('+++++++++++++++++')
score = 80

if score >= 60:
    print("Passed the exam.")

s = "Hello World"
if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

if score >= 60:
    print("Passed the exam.")
else:
    print("Failed the exam")

print('===========================')
age = 27
result = None

if age > 21:
    result = 'Eligible'
else:
    result = 'Not eligible'
print(result)

age = 18
result = 'Eligible' if age > 21 else 'Not eligible'
print(result)

num = 3
result = None
if num > 0:
    result = "positive"
elif num < 0:
    result = "negative"
else:
    result = 'zero'

print(result)

num = -4
result = "positive" if num > 0 else ("negative" if num < 0 else "zero")
print(result)
