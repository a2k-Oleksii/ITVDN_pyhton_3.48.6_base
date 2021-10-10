class A:
    def method(self):
        print("A class")


class B(A):
    pass


class C(A):
    def method(self):
        print("C class")


class D(B, C):
    pass


if __name__ == '__main__':
    
    d_class = D()
    d_class.method()

    for cls in [A, B, C, D]:
        print(cls.__name__, ":", cls.mro())

