unique_element = {}
print(type(unique_element))
print("----------------------")
unique_element = set()
print(type(unique_element))

unique_element.add(10)
unique_element.add(10)
unique_element.add(10)
unique_element.add(20)
unique_element.add(20)

print(unique_element)
print("----------------removing an element-----------------")
unique_element.remove(10)
print(unique_element)

print("----------------adding  a element-----------------")
print(help(set.add)) # to know what set.add method do
"""
add(...)
    Add an element to a set.
"""
unique_element.add(1)
print(unique_element)

print("----------------difference method-----------------")
set1={"java", "C#", "Python", "Cydeo"}
set2={'C++', 'Ruby', 'Swift', 'Python'}

set3=set1.difference(set2)

print(set3)

print("----------------intersection method-----------------")

set4=set1.intersection(set2)
print(set4)