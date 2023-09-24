"""
4. Create a python file named factorial_number, Write a program
that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120
                    ( because: 5! = 5 * 4 * 3 * 2* 1 = 120 )
"""
n=5
factorial = 1
for num in range(1, n+1):
    # print(num)
    factorial *= num
print(factorial)
