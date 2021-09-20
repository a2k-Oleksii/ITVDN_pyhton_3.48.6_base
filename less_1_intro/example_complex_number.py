class Complex:
    def __init__(self, real=0.0, imagenary=0.0):
        self.real = real
        self.imagenary = imagenary

    def __repr__(self) -> str:
        return "Complex({!r}, {!r})".format(self.real, self.imagenary)

    def __str__(self) -> str:
        return "{}{:+d}i".format(self.real, self.imagenary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imagenary + other.imagenary)

    def __neg__(self):
        return Complex(-self.real, -self.imagenary)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.imagenary **2) ** 0.5

   # def __eq__(self, other):
    #    return self.real == other.real and self.imagenary == other.imagenary


c = Complex(2, 5)
d = Complex(2, 5)
print(c)
print(Complex(2, 3) + Complex(2, -1))
print(Complex(2, 3) - Complex(2, -1))
result = Complex(2, 5)
print(-result)
print(abs(Complex(2, 3)))

print(c == d)
    