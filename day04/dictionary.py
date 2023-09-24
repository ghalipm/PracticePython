employee1 = {'name': "Daniel"}

employee1['name'] = "Jack"

print(employee1)

employee2 = {
    'name': 'James',
    'age': 25,
    'salary': 80_000,
    'full_time': False
}
print(employee2)
employee2['salary'] += 10_000
print(employee2)

employee2.update({'age': 40})
print(employee2)

print('-----------------Iterating Dictionary---------------')
employee3 = {
    'name': 'Tom',
    'age': 35,
    'salary': 100_000,
    'full_time': True
}

print(list(employee3.keys()))
print(list(employee3.values()))

print('--------------------------------')
for x in employee3.items():
    # print(f'{x[0]}:{x[1]}')
    print(x)

print("=================================")
students = {
    'A01': {
        'name': 'Jane',
        'gender': 'Female',
        'gpa': 3.5,
        'subjects': ('Math', 'Physics')
    },
    'A02': {'name': 'Janet',
            'gender': 'Female',
            'gpa': 3.0,
            'subjects': ('Arts', 'English')
            },
    'A03': {'name': 'Jacky',
            'gender': 'Female',
            'gpa': 2.5,
            'subjects': ['Arts', 'English'],
            'specialty': 'Sports'}
}


# tuple () cannot be updated, but list [] can be updated


print(students)
students['A01']['gpa'] = 4.0
print(students['A01'])

students['A02'].update({'name': 'Tom', 'gender': 'Male'})
print(students['A02'])

students['A03'].update({'subjects':['EE', 'IT']})
print(students['A03'])
