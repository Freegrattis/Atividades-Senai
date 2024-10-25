import Vehicle

class Air(Vehicle):
    def __init__(self, year_construction, color, chassis_number, model, price, wingspan, flight_range):
        super().__init__(year_construction, color, chassis_number, model, price)

        self._wingspan = wingspan
        self._flight_range = flight_range

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, value):
        self._wingspan = value

    @property
    def flight_range(self):
        return self._flight_range

    @flight_range.setter
    def flight_range(self, value):
        self._flight_range = value

    def take_off(self):
        return f"{self.__model} Taking off."

    def landing(self):
        return f"{self.__model} Landing."