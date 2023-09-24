days = ("Mon", "Tu", "Wed", "Thu", "Fri", "Sat", "Sun")
# elements of tuple cannot be changed
print(type(days))
print(len(days))
print(days)

print(days[0])
print(days[1:4])

tuple1=10,20,30
tuple2=40,50,60, 30
tuple3=tuple2+tuple1
print(tuple3)

reversed_tuple=days[::-1]
print(reversed_tuple)
print(days.index("Wed"))

print("=============number of Mon in days")
print(days.count("Mon"))

for x in range(0, len(days)):
    print(x+1, days[x])
