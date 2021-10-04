def check_instance(obj, cls):
    return cls in type(obj).mro()

def check_subclass(child, base):
    return base in child.mro()

print(check_instance(8, int))

print(check_instance(8, str))

print(check_subclass(bool, int))

print(check_subclass(bool, object))

print(check_subclass(bool, str))
    