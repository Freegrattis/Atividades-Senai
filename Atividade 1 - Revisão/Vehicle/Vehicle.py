class Vehicle:
    def __init__(self, name, color, year, price):
        self.__name = name
        self.__color = color
        self.__year = year
        self.__price = price

    def  get_name(self):
        return self.__name

    def set_name(self,  name):
        self.__name = name

    def  get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_year(self):
        return self.__year
    
    def set_year(self,  year):
        self.__year = year

    def get_price(self):
        return self.__price

    def set_price(self,  price):
        self.__price = price

    def move(self):
        print(f"The {self.__name} is moving")

    def stop(self):
        print(f"The {self.__name} has stopped")