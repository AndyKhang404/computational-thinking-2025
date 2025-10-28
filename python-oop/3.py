class Student:
	def __init__(self, name):
		self.__grade = 0
		self.name = name
	
	def set_grade(self, grade):
		if grade < 0 or grade > 100:
			raise ValueError("Grade must be between 0 and 100")
		self.__grade = grade
	
	def get_grade(self):
		return self.__grade

try:
	student1 = Student("Khang")
	student1.set_grade(85)
	print(f"{student1.name}'s grade: {student1.get_grade()}")

	student2 = Student("Hung")
	student2.set_grade(110)  # Invalid grade
	print(f"{student2.name}'s grade: {student2.get_grade()}")
except ValueError as e:
	print(e)