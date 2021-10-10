class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square = False, multipayer = None):
        if square and not multipayer:
            print(self.__a ** 2)
        elif not square and multipayer:
            print(self.__a * multipayer)
        elif square and multipayer:
            print((self.__a ** 2) * multipayer)
        else:
            print(self.__a)


base = Base(4)
base.print_a(square=True, multipayer=2)
