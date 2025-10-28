class BankAccount:
	def __init__(self, account_number, owner, balance=0):
		self.account_number = account_number
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount < 0:
			raise ValueError("Deposit amount must be positive")
		self.balance += amount

	def withdraw(self, amount):
		if amount < 0:
			raise ValueError("Withdrawal amount must be positive")
		if amount > self.balance:
			raise ValueError("Insufficient funds")
		self.balance -= amount

	def get_balance(self):
		return self.balance

try:
	account1 = BankAccount("123456789", "Khang", 1000)
	account1.deposit(500)
	account1.withdraw(200)
	print(account1.get_balance())

	account2 = BankAccount("987654321", "An")
	account2.deposit(300)
	account2.withdraw(400) # Insufficient funds
	print(account2.get_balance())
except ValueError as e:
	print(e)