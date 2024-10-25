import Vehicle

class Land(Vehicle):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, num_wheels):
        super().__init__(year_construction, color, chassis_number, model, price, capacity)
        self._num_wheels = num_wheels

    @property
    def num_wheels(self):
        return self._num_wheels

    @num_wheels.setter
    def num_wheels(self, value):
        self._num_wheels = value
 

