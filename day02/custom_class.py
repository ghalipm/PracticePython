import numbers


class Employee:
    is_human = True  # Similar to a static variable in Java.

    def __init__(self, name: str = "Unknown", job_title: str = "SDET", salary: numbers = 100000):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working.')

    def __int__(self):
        return f'{type(self).__name__}{self.name}' # type(self).__name__ is same as Class.name in Java


employee1 = Employee()

employee1.work()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee("Daniel")
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee("Daniel", "SDET", 150000)
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

