class Person:

    # def __init__(self, name: str, age: int):
    def __init__(self, name="unknown" or str, age=0 or int):
        self.__name = None  # private name
        self.__age = None  # private age
        self.__name = name
        self.__age = age

# compare to the previous version:

    @property
    def person_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')

        return self.__name

    @person_name.setter
    def person_name(self, name):
        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name can not be empty')

        self.__name = name

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age):
        if age < 0 or age > 150:
            raise RuntimeError(f'Inavlid age {age}')

        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{str(self.__dict__).replace("_Person__", "")}'


person1 = Person()

person1.person_name = "Daniel"
print(person1.person_name)
