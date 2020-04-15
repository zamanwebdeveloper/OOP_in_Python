# Multiple Inheritance
# is a relationship
# Car is vehicle
# Truck is vehicle
class Vehicle:
    def __init__(self,name):
        self.vehicle_name = name
    def cname(self):
        print(self.vehicle_name)
class Dirver():
    def __init__(self,name):
        self.driver_name = name
    def dname(self):
        print(self.driver_name)

class Car(Vehicle,Dirver):
    def __init__(self,cname,dname):
        Vehicle.__init__(self,cname)
        Dirver.__init__(self,dname)
    def drive(self):
        print(self.vehicle_name,'is dirve')
class Truck(Vehicle):
    def wheel(self):
        print(self.vehicle_name,'--> has 8 wheel')
a = Car('Toyota','Rahim Islam')
a.cname() #parent class - Vehicle
a.drive() #child class
a.dname() #parent class - diver

b = Truck('tata')
b.cname()
b.wheel()




