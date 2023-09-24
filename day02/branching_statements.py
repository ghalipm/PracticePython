print("=========continue - jump==========")
for i in range(0, 7):
    if i % 3 == 0:
        continue
    print(i)
print("========= pass ==========")

for i in range(0, 7):
    if i % 3 == 0:
        pass
    print(i)