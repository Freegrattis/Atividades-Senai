import Land

class Car(Land):
    def  __init__(self, name, color, year, price, n_wheels, chassi):
        super().__init__(name, color, year, price, n_wheels)
        self.chassi = chassi

    def get_chassi(self):
        return self.chassi

    def set_chassi(self, chassi):
        self.chassi = chassi


    