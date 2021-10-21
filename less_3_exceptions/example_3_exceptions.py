class ObjectWithDestructor:
    def __del__(self):
        print("Destructor invoke")
        raise Exception


print("Creating object ...")
obj = ObjectWithDestructor()

print("Deleting object ...")
del obj

print("Done")
