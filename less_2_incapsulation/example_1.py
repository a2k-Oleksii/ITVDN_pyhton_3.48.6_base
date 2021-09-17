class Test:
    def __init__(self, test_value):
        self.__private_attr = test_value

    def get_privet_attr(self):
        return self.__private_attr

    @staticmethod
    def __private_function():
        print('I private function')

    def call_private_function(self):
        self.__private_function()


test = Test(test_value=10)
print(test.get_privet_attr())
test.call_private_function()
