groceries_list = ['Egg', 'Milk', 'Rice', 'Chicken']

groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(len(groceries_list))
print(groceries_list)

groceries_list[-2] = 'Cherry'
print(groceries_list)

print('------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers_list)
numbers_list[2:-1] = [100, 200, 300, 600, 700]
print("==========================")
print(numbers_list)

print('------------------------')
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list1 = characters[2:-3]
print(list1)

list2 = characters[:4]
print(list2)
list3 = characters[4:]
print(list3)

characters[2:5] = ['C', 'D', 'E', 'F', 'X', 'Y', 'Z']
print(characters)

print('-----------Names-------------')
names = ['Jamal', 'Muhtar', 'Kuzzat', 'Ozzi']

for name in names:
    print(name)

numbers_list = [10, 20, 30, 40, 50, 60]
for ind in range(0, len(numbers_list)):
    numbers_list[ind] = numbers_list[ind] / 5
print(numbers_list)

print("===================")
for ind in reversed(range(len(numbers_list))):
    numbers_list[ind] = numbers_list[ind]
print(numbers_list)

for num in reversed(numbers_list):
    print(num)

print('-----------While-------------')
i = 0
while i < len(numbers_list):
    print(numbers_list[i])
    i += 1
print('-----------Sort-------------')
numbers_list.sort()  # acs
print(numbers_list)
print('-----------Sort reversed-------------')
numbers_list.sort(reverse=True)
print(numbers_list)
print('-----------new list-------------')
numbers_list = [2, 5, 3, 7, 8, 9, 10]
numbers_list.sort()
print(numbers_list)
numbers_list.reverse()  # not new list
print(numbers_list)

print('-----------tuple-------------')
tuple_elements = ('Java', 'C#', 'Python', 'Golang')
print('tuple:', tuple_elements)
# tuple is immutable
list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('JS')
print('list:', list_elements)

tuple_elements = tuple(list_elements)
print('tuple:', tuple_elements)

print('-----------remove from the list-------------')
groceries_list = ['Egg', 'Milk', 'Rice', 'Chicken']
groceries_list.remove('Milk')
print(groceries_list)  # ['Egg', 'Rice', 'Chicken']

groceries_list.pop()
print(groceries_list)  # ['Egg', 'Rice']

groceries_list.insert(2, 'Beef')
print(groceries_list)

nums = [1, 3, 2, 1, 1, 1, 1, 3, 4]
print(nums.count(1))

print('-----------Comprehensions-------------')
nums = []
for x in range(1, 51):
    nums.append(x)
print(nums)

divisible_by_five = []

for num in nums:
    if num % 5 == 0:
        divisible_by_five.append(num)
    else:
        continue

print(divisible_by_five)
print('-----------with Comprehension-------------')
nums = []
for x in range(1, 51):
    nums.append(x)
print('nums:', nums)

divisible_by_5 = tuple([x for x in nums if x % 5 == 0])
print('filtered:', divisible_by_5)

even_nums = tuple([x for x in nums if x % 2 == 0])
print('even:', even_nums)

odd_nums = [x for x in nums if x % 2 == 1]
print('odd:', odd_nums)

print('------------------------')
names = ['Python', 'Java', 'Java', 'java', 'JaVA', 'Python', 'C#']
names2 = [x for x in names if x.lower() != 'java']
print(names2)

