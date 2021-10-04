class Base:
    def method(self):
        print("Hello")


class Child(Base):
    def chaild_method(self):
        print("This is chaild method")

    def method(self):
         print("Hello from redefined method")

obj = Child()
obj.method()
obj.chaild_method()
