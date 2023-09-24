import json

path = 'C:/Users/ZipZap/PycharmProjects/PracticePython/Days/day04/files/Test.json'

jason_file = open(path, 'r')

dictionary = json.load(jason_file)
print(dictionary)
print(type(dictionary))

"""
Web automation:
    BeautifulSoap4
    request
    pytest
    robotframework
    
Web development:
    Django
    FastAPI
    flask
    ....
"""