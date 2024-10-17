import Vehicle

class Car(Vehicle):
    def __init__(self, year_construction, color, chassis_number, model, price, num_doors, trunk_size):
        super().__init__(year_construction, color, chassis_number, model, price)
        self._num_doors = num_doors
        self._trunk_size = trunk_size

    @property
    def num_doors(self):
        return self._num_doors

    @num_doors.setter
    def num_doors(self, value):
        self._num_doors = value

    @property
    def trunk_size(self):
        return self._trunk_size

    @trunk_size.setter
    def trunk_size(self, value):
        self._trunk_size = value

    def honk(self):
        return "Beep beep!"
