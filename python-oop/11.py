class DatabaseConnection:
	__instance = None

	def __new__(cls):
		if cls.__instance is not None:
			raise Exception("Only one instance of DatabaseConnection is allowed.")
		cls.__instance = super().__new__(cls)
		return cls.__instance

	@classmethod
	def get_instance(cls):
		if cls.__instance is None:
			cls.__instance = DatabaseConnection()
		return cls.__instance
		
db1 = DatabaseConnection.get_instance()
db2 = DatabaseConnection.get_instance()
print(db1 is db2) # True
try:
	db3 = DatabaseConnection()
except Exception as e:
	print(e)