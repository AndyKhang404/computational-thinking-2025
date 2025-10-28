class Shape:
	def area(self):
		raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	
	def area(self):
		return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def area(self):
		return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6), Circle(3), Rectangle(2, 8)]
total_area = sum(shape.area() for shape in shapes)
print("Total area:", total_area)