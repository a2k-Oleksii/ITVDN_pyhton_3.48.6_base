class MyObject:
    def __init__(self):
        self.__private_atribute = 0

    def get_privet_attribute(self):
        return self.__private_atribute

    def set_privet_atribute(self, value):
        if value < 100:
            self.__private_atribute = value
    
obj = MyObject()

print(obj.get_privet_attribute())

obj.set_privet_atribute(200)
print(obj.get_privet_attribute())

obj.set_privet_atribute(20)
print(obj.get_privet_attribute())
