class Box:
    def __init__(self, max_capacity):
        self.inventory = []                
        self.sold_vehicles = []           
        self.funds = 0                     
        self.transaction_log = []          
        self.max_capacity = max_capacity   

    def add_vehicle(self, vehicle):
        if len(self.inventory) < self.max_capacity:
            self.inventory.append(vehicle)
            print(f"{vehicle._model} adicionado ao inventário.")
        else:
            print("Capacidade máxima atingida! Não é possível adicionar mais veículos.")

    def sell_vehicle(self, vehicle):
        if vehicle in self.inventory:
            self.inventory.remove(vehicle)
            self.sold_vehicles.append(vehicle)
            self.funds += vehicle.price
            self.transaction_log.append(f"Vendido: {vehicle._model} por R${vehicle.price:.2f}")
            print(f"Veículo {vehicle._model} vendido por R${vehicle.price:.2f}.")
        else:
            print(f"O veículo {vehicle._model} não está no inventário.")

    def buy_vehicle(self, vehicle):
        if len(self.inventory) < self.max_capacity:
            self.inventory.append(vehicle)
            self.funds -= vehicle.price
            self.transaction_log.append(f"Comprado: {vehicle._model} por R${vehicle.price:.2f}")
            print(f"Veículo {vehicle._model} comprado por R${vehicle.price:.2f}.")
        else:
            print("Capacidade máxima atingida! Não é possível comprar mais veículos.")

    def show_inventory(self):
        if self.inventory:
            print("Veículos disponíveis no inventário:")
            for vehicle in self.inventory:
                print(f"- {vehicle._model} ({vehicle._year_construction}) - R${vehicle.price:.2f}")
        else:
            print("Is empty.")

    def show_sold_vehicles(self):
        if self.sold_vehicles:
            print("Vehicles sold:")
            for vehicle in self.sold_vehicles:
                print(f"- {vehicle._model}: R${vehicle.price:.2f}")
        else:
            print("No vehicles have been sold to date.")

    def total_funds(self):
        print(f"Total: ${self.funds:.2f}")

    def find_vehicle_by_model(self, model):
        for vehicle in self.inventory:
            if vehicle._model.lower() == model.lower():
                return vehicle
        return None

    def remove_vehicle(self, vehicle):
        if vehicle in self.inventory:
            self.inventory.remove(vehicle)
            print(f"{vehicle._model} removed from inventory.")
        else:
            print(f"{vehicle._model} not in inventory.")

    def transaction_history(self):
        if self.transaction_log:
            print("History:")
            for transaction in self.transaction_log:
                print(transaction)
        else:
            print("No transactions carried out so far.")
