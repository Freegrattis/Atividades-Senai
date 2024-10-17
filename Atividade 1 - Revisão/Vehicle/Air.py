import Vehicle

class Air(Vehicle):
    def  __init__(self, name, color, year, price, maximum_altitude):
            super().__init__(name, color, year, price)
            self.maximum_altitude = maximum_altitude

    def get_maximum_altitude(self):
        return self.maximum_altitude

    def set_maximum_altitude(self, maximum_altitude):
        self.maximum_altitude = maximum_altitude
