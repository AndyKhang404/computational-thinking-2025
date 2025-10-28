class Vector2D:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)
	
	def __str__(self):
		return f"({self.x}, {self.y})"

v1 = Vector2D(2, 3)
v2 = Vector2D(4, 5)
v3 = Vector2D()
print(v1 + v2)
print(v1 + v3)