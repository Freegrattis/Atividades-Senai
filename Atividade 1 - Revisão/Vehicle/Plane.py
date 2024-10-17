import Air

class Plane(Air):
    def  __init__(self, name, color, year, price, maximum_altitude, n_engine):
            super().__init__(name, color, year, price, maximum_altitude)
            self.n_engine = n_engine

    def get_n_engine(self):
        return self.n_engine

    def set_n_engine(self, n_engine):
        self.n_engine = n_engine
