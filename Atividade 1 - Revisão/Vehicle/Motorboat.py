import Water

class Motorboat(Water):
    def  __init__(self, name, color, year, price, fuel_type, speed):
        super().__init__(name, color, year, price, fuel_type)
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
