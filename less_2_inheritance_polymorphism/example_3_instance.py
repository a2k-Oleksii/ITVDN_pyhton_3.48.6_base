class Base(object):
    def method(self):
        print("Method class: ", __class__.__name__)
        print("Instance class: ", type(self).__name__)

class Chaild(Base):
    pass


def main():
    base = Base()
    base.method()
    print("*" * 30)
    chaild = Chaild()
    chaild.method()

if __name__ == '__main__':
    main()
    