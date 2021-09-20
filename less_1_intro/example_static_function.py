class MyObject:
    class_atribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)
    
    @staticmethod
    def static_method():
        print(MyObject.class_atribute)


if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()
