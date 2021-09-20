class MyObject:
    def __init__(self):
        self.__private_atribute = 0

    @property
    def attribute(self):
        return self.__private_atribute

    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__private_atribute = value


obj = MyObject()

print(obj.attribute)
obj.attribute = 20
print(obj.attribute)
obj.attribute = 200
print(obj.attribute)
