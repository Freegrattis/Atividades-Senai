import Land

class Truck(Land):
    def  __init__(self, name, color, year, price, n_wheels, capacity):
        super().__init__(name, color, year, price, n_wheels)
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity


    