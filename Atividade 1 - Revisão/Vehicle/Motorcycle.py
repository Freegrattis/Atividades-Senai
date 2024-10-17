import Land

class Motorcycle(Land):
    def  __init__(self, name, color, year, price, n_wheels, capacity_fuel_tank):
        super().__init__(name, color, year, price, n_wheels)
        self.capacity_fuel_tank = capacity_fuel_tank

    def get_capacity_fuel_tank(self):
        return self.capacity_fuel_tank

    def set_capacity_fuel_tank(self, capacity_fuel_tank):
        self.capacity_fuel_tank = capacity_fuel_tank

    @overrides(Land)
    def honk(self):
        print("Bi Bi!")
