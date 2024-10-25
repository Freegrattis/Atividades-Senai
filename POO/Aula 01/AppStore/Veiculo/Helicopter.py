import Air

class Helicopter(Air):
    def __init__(self, year_construction, color, chassis_number, model, price, wingspan, flight_range, rotor_diameter, max_altitude):
        super().__init__(year_construction, color, chassis_number, model, price, wingspan, flight_range)
        self.max_altitude = max_altitude
        self._rotor_diameter = rotor_diameter

    @property
    def rotor_diameter(self):
        return self._rotor_diameter

    @rotor_diameter.setter
    def rotor_diameter(self, value):
        self._rotor_diameter = value

    def lift_off(self):
        return f"{self.__model} Lifting off ."

    # Método para pairar
    def hover(self):
        return f"{self.__model} is hovering {self._max_altitude}m."
