"""
3. Create a python file named sum_of_even_odd:
        3.1 Write a program that can return the sum of even numbers
         between 1 and 100

        3.2 Write a program that can return the sum of odd numbers
        between 1 and 100

        3.3 write a program that can calculate the sum of all numbers
        between 1 to any given number
            ex:
                input: 100
                output: 5050

                input: 50
                output: 1275
"""
n = 50
even_sum = 0
odd_sum = 0
for num in range(1, n+1):
    if num % 2 == 1:
        odd_sum += num
    else:
        even_sum += num
print(f"Even numbers sum:{even_sum}")
print(f"Odd numbers sum:{odd_sum}")

print(f"Sum of all numbers between 1 and {n} is:{odd_sum + even_sum}")
