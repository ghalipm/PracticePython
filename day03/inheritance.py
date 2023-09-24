class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):

    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age)  # parent class constructor
        self.name = name
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        return f'{self.name} is working'


class Developer(Employee):
    def __init__(self, name: str, age: int, job_title="Developer", company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title)  # parent class constructor


developer1 = Employee('Hazel', 25, 'SDET', 'Apple')

developer2 = Developer("Daniel", 45, 'Python')

print(developer1)
print(developer1.work())
print(developer2)
print(developer2.work())

# compare
