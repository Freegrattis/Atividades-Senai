class Vehicle:
    def __init__(self, year_construction, color, chassis_number, model, price, capacity ):
        self._year_construction = year_construction
        self.color = color
        self.__chassis_number = chassis_number
        self.__model = model
        self.price = price
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def year_construction(self):
        return self._year_construction

    @year_construction.setter
    def year_construction(self, value):
        self._year_construction = value

    @property
    def _chassis_number(self):
        return self.__chassis_number

    @_chassis_number.setter
    def _chassis_number(self, value):
        self.__chassis_number = value

    @property
    def _model(self):
        return self.__model

    @_model.setter
    def _model(self, value):
        self.__model = value

    def start(self):
        return f"{self.__model} ligado."

    def stop(self):
        return f"{self.__model} desligado."