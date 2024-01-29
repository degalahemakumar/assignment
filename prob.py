#Create a Class with instance attributes

class Car:
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

    def display_car_info(self):
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Toyota", "Corolla", 2022)
print(my_car.display_car_info())


#Create a Vehicle class without any variables and methods
class Car:
    pass
    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

    def display_car_info(self):
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Toyota", "Corolla", 2022)
print(my_car.display_car_info())

class Vehicle:
    pass

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping.")

# Child class Bus inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)  # Call the constructor of the parent class
        self.capacity = capacity  # Additional attribute for Bus

    def show_capacity(self):
        print(f"This bus can carry {self.capacity} people.")


my_bus = Bus("Volvo", "B9R", 2022, 50)
my_bus.start()  
my_bus.show_capacity()  
