class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    @staticmethod
    def drive_forward():
        print("Drive forward")

    @staticmethod
    def drive_backward():
        print("Drive backward")


class Car2(Car):
    @staticmethod
    def turn_left():
        print("Turn left")

    @staticmethod
    def turn_right():
        print("Turn right")


class Airplane:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def up():
        print("Going up")

    @staticmethod
    def land():
        print("Landing")


class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, volume, model):
        Car2.__init__(self, brand, color, volume)
        Airplane.__init__(self, model)


car = Car2(brand="BMW", color="Blue", volume=3.0)
car.turn_right()
car.drive_backward()
car.turn_left()
car.drive_forward()
print('----------------------------------------------------')
fc = FlyingCar(brand='Tesla', color='Black', volume=10, model='F')
fc.turn_left()
fc.drive_forward()
fc.drive_backward()
fc.turn_right()
fc.up()
fc.land()