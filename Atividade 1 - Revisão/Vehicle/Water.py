import Vehicle

class Water(Vehicle):
    def  __init__(self, name, color, year, price, fuel_type):
        super().__init__(name, color, year, price)
        self.fuel_type = fuel_type

    def get_fuel_type(self):
        return self.fuel_type

    def set_fuel_type(self,  fuel_type):
        self.fuel_type = fuel_type