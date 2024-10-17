import Vehicle

class Boat(Vehicle):
    def __init__(self, year_construction, color, chassis_number, model, price, boat_length, displacement):
        super().__init__(year_construction, color, chassis_number, model, price)
        self._displacement = displacement
        self._boat_length = boat_length

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value

    @property
    def boat_length(self):
        return self._boat_length

    @boat_length.setter
    def boat_length(self, value):
        self._boat_length = value

    def sail(self):
        return f"{self.__model} sailing."

    def anchor(self):
        return f"{self.__model} anchored."
