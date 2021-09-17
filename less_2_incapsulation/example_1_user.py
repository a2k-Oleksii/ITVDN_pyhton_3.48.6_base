class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


user = User(name='Tom')
user.name = 'Dimon'
print(user.name)


class Worker:
    RIHTS = 'Equal'
    SALARY_MAP = {
        'A': 100,
        'B': 200,
        'C': 500
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    def __get_salary(self, working_class):
        return self.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


w1 = Worker('A')
print(w1.salary)
w2 = Worker('C')
print(w2.salary)