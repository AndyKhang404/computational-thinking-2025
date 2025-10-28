class Circle:
	def __init__(self):
		self._radius = 0

	@property
	def radius(self):
		return self._radius
	
	@radius.setter
	def radius(self, value):
		if value < 0:
			raise ValueError("Radius cannot be negative")
		self._radius = value
	
	def area(self):
		return 3.14 * (self._radius ** 2)

circle = Circle()
print(circle.radius)  # Output: 5
circle.radius = 10
print(circle.radius)  # Output: 10
try:
	circle.radius = -3
except ValueError as e:
	print(e)
finally:
	print(circle.area())