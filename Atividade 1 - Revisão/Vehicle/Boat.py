import Water

class Boat(Water):
    def  __init__(self, name, color, year, price, fuel_type, weight):
        super().__init__(name, color, year, price, fuel_type)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
