# Inheritance
# is a relationship
# Car is vehicle
# Truck is vehicle
class Vehicle:
    def __init__(self,name):
        self.vehicle_name = name
    def name(self):
        print(self.vehicle_name)
class Car:
    def __init__(self,name):
        self.car_name = name
    def name(self):
        print(self.car_name)
a = Car('Toyota')
a.name()




