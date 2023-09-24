from day02.utility import sum, calculate

result = sum(10, 5)
print(result)

result = calculate(10, 5, '*')
print(result)

print('=======================')

import day02.utility as u

num2 = u.calculate(100, 20, '/')
print(num2)

u.concat("java", 'Python', 2)
