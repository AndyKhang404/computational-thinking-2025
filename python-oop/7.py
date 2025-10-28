class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} years old."
	
person1 = Person("Khang", 19)
print(person1)
person1 = Person("Nhan", 20)
print(person1)