import Boat

class Motorboard(Boat):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, boat_length, displacement, engine_power):
        super().__init__(year_construction, color, chassis_number, model, price, capacity, boat_length, displacement)
        self._engine_power = engine_power

    @property
    def engine_power(self):
        return self._engine_power

    @engine_power.setter
    def engine_power(self, value):
        self._engine_power = value

    def accelerate(self):
        return f"{self.__model} Accelerating."

    # Método para desacelerar
    def decelerate(self):
        return f"{self.__model} decelerating."