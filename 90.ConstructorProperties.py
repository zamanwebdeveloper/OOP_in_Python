# Object Oriented Programming 
# Object
# attribute -> 1) propertise
			# 2) method
class Vehicle:
    def __init__(self,name,wheel,driver):
        self.v_name = name # instance variable
        self.v_wheel = wheel
        self.v_driver = driver
    def show(self):
        print('name = ',self.v_name,'=> wheel = ',self.v_wheel,'=> driver = ',self.v_driver)
car = Vehicle('toyota',4,'Solimuddin')
car.show()
truck = Vehicle('tata',8,'Kolimuddin')
truck.show()
