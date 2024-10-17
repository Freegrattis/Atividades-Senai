import Air

class Helicopter(Air):
    def  __init__(self, name, color, year, price, maximum_altitude, n_rotor):
            super().__init__(name, color, year, price, maximum_altitude)
            self.n_rotor = n_rotor

    def get_n_rotor(self):
        return self.n_rotor

    def set_n_rotor(self, n_parachute):
        self.n_rotor = n_rotor
