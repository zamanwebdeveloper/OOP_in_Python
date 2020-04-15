# Object Oriented Programming 
# Object
# attribute -> 1) Class Variable
			# 2) Instance Variable
class Vehicle:
    hey = "Hello World" # Class Variable
    def __init__(self,name,wheel,driver):
        self.v_name = name # instance variable
        self.v_wheel = wheel # instance variable
        self.v_driver = driver # instance variable
    def show(self):
        print('name = ',self.v_name,'=> wheel = ',self.v_wheel,'=> hey = ',self.hey)
car = Vehicle('toyota',4,'Solimuddin')
car.show()
print(Vehicle.hey)
print(car.hey)

truck = Vehicle('tata',8,'Kolimuddin')
truck.show()
