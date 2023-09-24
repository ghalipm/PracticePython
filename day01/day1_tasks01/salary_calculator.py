"""
12. Create a python file named salary_calculator
            1.1 Ask the user to enter the following info:
                     1.1.1 "Enter your name"
                     1.1.2 "Enter your hourly rate"
                     1.1.3 "How many hours you work in a week?"

            1.2 write a program that can can culate the salary based on the user given info
                         Hint: number of weeks are 52

                         salary = hourlyRate * weeklyHour * 52

            Ex:
                Given Data:
                    name = Joshua
                    hourly_rate = 40
                    weekly_hours = 45


                Output:
                    Hello Joshua, your salary is $ 93600.00
"""
name = input("Enter your name: ")
hourly_rate = float(input("Enter your hourly rate: "))
hours_per_week = float(input("How many hours you work in a week: "))
annual_salary = hours_per_week * hourly_rate * 52
annual_salary=round(annual_salary,4)

print("Hello", name, ", your annual salary is $", annual_salary)
print(f"Hello {name}, your salary is $ {annual_salary:.2f}")
print(f"Hello {name}, your salary is $ {annual_salary:.1f}")

