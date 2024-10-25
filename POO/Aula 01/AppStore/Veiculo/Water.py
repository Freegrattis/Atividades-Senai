import Vehicle

class Water(Vehicle):
    def __init__(self, year_construction, color, chassis_number, model, price, capacity, boat_length):
        super().__init__(year_construction, color, chassis_number, model, price, capacity)
        self._boat_length = boat_length

    @property
    def boat_length(self):
        return self._boat_length

    @boat_length.setter
    def boat_length(self, value):
        self._boat_length = value
 