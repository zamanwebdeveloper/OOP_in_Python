# Inheritance
# is a relationship
# Car is vehicle
# Truck is vehicle
class Vehicle:
    def __init__(self,name):
        self.vehicle_name = name
    def name(self):
        print(self.vehicle_name)
class Car(Vehicle):
    pass
a = Car('Toyota')
a.name()




