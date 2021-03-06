class Human:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print("Hello, I am {}".format(
            self.age
        ))


# human_1 = Human(age=35)
# human_1.say_hello()


class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def say_hello(self):
        print("Hello! I am {} and I am {}".format(
            self.name, self.age
        ))


# human_2 = HumanExtended(age=22, name='Jhon')
# human_2.say_hello()


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
print(c.a)
print(c.b)
