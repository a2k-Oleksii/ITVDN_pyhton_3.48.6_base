class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prin_info(self):
        print(self.name, 'is', self.age)


jhon = Person('Jhon', 22)
lucy = Person('Lucy', 20)

jhon.prin_info()
lucy.prin_info()

Person.prin_info(jhon)
Person.prin_info(lucy)

print(type(Person.prin_info))
print(type(jhon.prin_info))
