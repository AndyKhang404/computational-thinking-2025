class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
	
	def info(self):
		return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
	def __init__(self, name, salary, department):
		super().__init__(name, salary)
		self.department = department
	
	def info(self):
		return f"{super().info()}, Department: {self.department}"
	
class Executive(Manager):
	def __init__(self, name, salary, department, stock_options):
		super().__init__(name, salary, department)
		self.stock_options = stock_options
	
	def info(self):
		return f"{super().info()}, Stock Options: {self.stock_options}"

employee = Employee("An", 10_000_000)
print(employee.info())
manager = Manager("Trung", 20_000_000, "Sales")
print(manager.info())
executive = Executive("Khang", 50_000_000, "Marketing", 1000)
print(executive.info())