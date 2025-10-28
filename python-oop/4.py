class Vehicle:
	def __init__(self, max_speed, mileage):
		self.max_speed = max_speed
		self.mileage = mileage
	
	def info(self):
		return f"Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km"
	
class Bus(Vehicle):
	def __init__(self, max_speed, mileage, passengers):
		super().__init__(max_speed, mileage)
		self.passengers = passengers
	
	def info(self):
		base_info = super().info()
		return f"{base_info}, Passengers: {self.passengers}"

bus1 = Bus(100, 15, 50)
print(bus1.info())
bus2 = Bus(80, 12, 30)
print(bus2.info())