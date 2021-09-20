class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == "12345":
            return "secret value"
        else:
            return object.__getattribute__(self, item)


obj = MyObject()
print(obj.password)

obj.password = "12345"
print(obj.password, obj.secret_field)

