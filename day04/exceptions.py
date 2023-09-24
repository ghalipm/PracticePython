try:
    num = 10 / 0
    print(num)
except:
    print("Zero dvision")
else:
    print("Nothing went wrong")
finally:
    print("finally block")

print("Test completed")

print("-------------------")

tuple1 = [10, 20, 30, 40]

try:
    # print(tuple1[10])
    print(tuple1[2])
except LookupError:
    print("index number too large")
else:
    print("index value is valid")

print("=========================")

try:
    raise FileNotFoundError("No such an exception")
except SyntaxError:
    print("Syntax error")
except OSError:
    print("OS error")
finally:
    print("finally block")

age = -2
if age < 0:
    raise Exception("Age cannot be less than zero")
    # raise is used to throw manual exception


