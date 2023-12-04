class Vehicle:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
    
    def calculate_milage(self):
        pass

    def calculate_towing_capacity(self):
        pass


class Car(Vehicle):
    def __init__(self, maker, model, year, engine_size):
        super().__init__(maker, model, year)
        self.engine_size = engine_size

    def calculate_milage(self):
        return 200 / self.engine_size

    def calculate_towing_capacity(self):
        return 100*self.engine_size


class Truck(Vehicle):
    def __init__(self, maker, model, year, engine_size):
        super().__init__(maker, model, year)
        self.engine_size = engine_size

    def calculate_milage(self):
        return 50 / self.engine_size

    def calculate_towing_capacity(self):
        return 1000*self.engine_size


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, engine_size):
        super().__init__(maker, model, year)
        self.engine_size = engine_size

    def calculate_milage(self):
        return 100 / self.engine_size

    def calculate_towing_capacity(self):
        return 10*self.engine_size


def main():
    car = Car("Ford", "Focus", 2005, 1.6)
    print(car.calculate_milage())
    print(car.calculate_towing_capacity())

    truck = Truck("Ford", "F150", 2010, 5.4)
    print(truck.calculate_milage())
    print(truck.calculate_towing_capacity())

    motorcycle = Motorcycle("Honda", "CBR", 2015, 0.6)
    print(motorcycle.calculate_milage())
    print(motorcycle.calculate_towing_capacity())


main()