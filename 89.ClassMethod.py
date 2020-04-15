# Object Oriented Programming 
# Object
# attribute -> 1) propertise
			# 2) method

'''
str = 'zamanwebdeveloper'
print(str.__len__())
print(len(str))
'''

class Vehicle:
	def set_value(self,name,wheel,driver):
		self.v_name = name
		self.v_wheel = wheel
		self.v_driver = driver
	def show(self):#self = car, truck
		print(self.v_name, self.v_wheel, self.v_driver)
car = Vehicle()
car.set_value('toyota',4,'Solimuddin')
# car.name = 'toyota'
# car.wheel = 4
# car.driver = 'solimuddin'
car.show()
# Vehicle.shwo(car)

truck = Vehicle()
truck.set_value('tata',8,'Kolimuddin')
truck.show()
# truck.name = 'tata'
# truck.wheel = 8
# truck.driver = 'kolimuddin'

# print(truck.name,truck.driver,truck.wheel)