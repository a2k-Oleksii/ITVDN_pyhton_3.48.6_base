class Base:
    def method(self):
        print("Base method invoked on", type(self).__name__, "instance")


class Chaild(Base):
    def method(self):
        super().method()
        print("Chaild method invoked on", type(self).__name__, "instance")

base = Base()
chaild = Chaild()

base.method()
print('*' * 40)
chaild.method()