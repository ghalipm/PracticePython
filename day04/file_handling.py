import os

path = 'C:/Users/ZipZap/PycharmProjects/PracticePython/Days/day04/files/Test.txt'
# for simple txt file open works well, but for others, we need to import
"""
original Test.txt content:
    Wooden Spoon
    Python Programming
    Cydeo School
"""

text_file = open(path, 'r')
print(text_file.read())
text_file.close()

print('----------writing new content---------')
path = 'files/Test.txt'

text_file2 = open(path, 'w')
text_file2.write("This is new text")  # Test.txt content will be : 'This is new text'
text_file2.close()
print('-------------------')
# os.remove(path)
