import Vehicle

class Land(Vehicle):
    def  __init__(self, name, color, year, price, n_wheels):
        super().__init__(name, color, year, price)
        self.n_wheels = n_wheels

    def get_n_wheels(self):
        return self.n_wheels

    def set_n_wheels(self, n_wheels):
        self.n_wheels = n_wheels

    def honk(self):
        print("")


    