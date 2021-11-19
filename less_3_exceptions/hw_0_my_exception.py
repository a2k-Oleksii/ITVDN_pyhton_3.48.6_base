# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class MyException(Exception):
    def __init__(self, text):
        self.text = text


def input_exception():
    try:
        age = int(input("Input your age: "))
        if age < 18:
            raise MyException("You entered incorrect age!!!")
    except ValueError as ex:
        print("Exception: ", ex)
    except MyException as me:
        print(me)
    else:
        print("Your age: ", age)


if __name__ == '__main__':
    input_exception()
