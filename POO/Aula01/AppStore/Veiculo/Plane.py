import Air

class Plane(Air):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, wingspan, flight_range, num_engines):
        super().__init__(year_construction, color, chassis_number, model, price, capacity, wingspan, flight_range)
        self._num_engines = num_engines 

    @property
    def num_engines(self):
        return self._num_engines

    @num_engines.setter
    def num_engines(self, value):
        self._num_engines = value

    def retract_landing_gear(self):
        return f"{self.__model} retracted."

    def extend_landing_gear(self):
        return f"{self.__model} extended."
