class Salary:
	def __init__(self, pay, bonus):
		self.pay = pay
		self.bonus = bonus
	
	def total_compensation(self):
		return self.pay + self.bonus

class Employee:
	def __init__(self, name, age, salary_obj):
		self.name = name
		self.age = age
		self.salary_obj = salary_obj
	
	def total_compensation(self):
		return self.salary_obj.total_compensation()

employee1 = Employee("Khang", 30, Salary(5000000, 100000))
print(f"{employee1.name}'s salary: {employee1.total_compensation()}")