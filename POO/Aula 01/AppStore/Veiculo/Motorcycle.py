import Land

class Motorcycle(Land):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, num_wheels, engine_capacity):
        super().__init__(year_construction, color, chassis_number, model, price, capacity, num_wheels)
        self._engine_capacity = engine_capacity

    @property
    def engine_capacity(self):
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value):
        self._engine_capacity = value

    def wheelie(self):
        return f"{self.__model} wheelie!"
