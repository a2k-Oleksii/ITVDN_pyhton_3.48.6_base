# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
    
    def __eq__(self, other):
        return self.name == other.name and self.model == other.model and self.price == other.price

    def __repr__(self):
        return "\nCar:{}, model:{}, price:{}".format(self.name, self.model, self.price)

    def get_price(self):
        return self.price


class AutoShop:
    __car_warehous = []
    __cashbox = 0.0

    def __init__(self, cars):
        for i in cars:
            self.__car_warehous.append(i)

    def car_sale(self, car):
        self.__car_warehous.remove(car)
        self.__cashbox += car.get_price()

    def get_warehous_info(self):
        return self.__car_warehous

    def get_cashbox(self):
        return "Cashbox:{}".format(str(self.__cashbox))


list_cars = [
    Car("Audi", "Q5", 50000.00),
    Car("BMW", "350", 45000.00),
    Car("Citroen", "C-Elise", 18000.00),
    Car("Hyndai", "Santa Fe", 40000.00),
    Car("Mercedes", "S500", 65000.00)
]

class main:
    auto_shop = AutoShop(list_cars)

    print(auto_shop.get_warehous_info())
    auto_shop.car_sale(Car("Hyndai", "Santa Fe", 40000.00))
    print(auto_shop.get_warehous_info())
    print(auto_shop.get_cashbox())
    auto_shop.car_sale(Car("Mercedes", "S500", 65000.00))
    print(auto_shop.get_warehous_info())
    print(auto_shop.get_cashbox())

main()