class Multiplayer:
    def __init__(self, a):
        self.__a = a

    def print_a(self, x):
        print(self.__a * x)



m = Multiplayer(5)
m.print_a(2)

class Exponent(Multiplayer):
    def print_a(self, x):
        print(self.__a ** x)

e = Exponent(5)
e.print_a(2)
