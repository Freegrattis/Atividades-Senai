import Land

class Truck(Land):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, num_wheels, load_capacity):
        super().__init__(year_construction, color, chassis_number, model, price, capacity, num_wheels)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        self._load_capacity = value

    def unload(self):
        return "Unloaded truck."