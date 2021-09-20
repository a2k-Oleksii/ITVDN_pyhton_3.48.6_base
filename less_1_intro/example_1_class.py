class MyObject:
    int_field = 8
    string_field = "a string"


print(MyObject.int_field)
print(MyObject.string_field)
obj_1 = MyObject()
obj_2 = MyObject()
print(obj_1.int_field)
print(obj_2.string_field)
MyObject.int_field = 10
print(MyObject.int_field)
print(obj_1.int_field)
obj_1.string_field = 'another_string'
print(MyObject.string_field)
print(obj_1.string_field)
print(obj_2.string_field)
