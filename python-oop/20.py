from enum import Enum
from datetime import datetime

class Account:
	def __init__(self, balance, owner):
		self.balance = balance
		self.owner = owner
	
	def __str__(self):
		return f"Owner: {self.owner} - Balance: {self.balance}"

class TransactionType(Enum):
	DEPOSIT = "deposit"
	WITHDRAWAL = "withdrawal"

class Transaction:
	def __init__(self, date, type, amount):
		self.date = date
		self.type = type
		self.amount = amount
	
	def __str__(self):
		return f"{self.date} - {self.type.value.capitalize()}: {self.amount}"

class ATM:
	def __init__(self):
		self.account = None
		self.transaction = None
		self.LOG_FILE = "atm.log"

	def insert_card(self, account):
		self.account = account
		print(f"Card inserted for {account.owner}")
	
	def enter_pin(self, pin):
		# For simplicity, assume any pin is correct
		print("PIN accepted")
	
	def withdraw(self, amount):
		if self.account is None:
			raise Exception("No card inserted")
		if amount > self.account.balance:
			raise Exception("Insufficient funds")
		self.account.balance -= amount
		print(f"Withdrew {amount}. New balance: {self.account.balance}")

		transaction = Transaction(str(datetime.now()), TransactionType.WITHDRAWAL, amount)
		with open(self.LOG_FILE, "a") as f:
			f.write(str(transaction) + "\n" + str(self.account) + "\n")
		return transaction

	def deposit(self, amount):
		if self.account is None:
			raise Exception("No card inserted")
		self.account.balance += amount
		print(f"Deposited {amount}. New balance: {self.account.balance}")

		transaction = Transaction(str(datetime.now()), TransactionType.DEPOSIT, amount)
		with open(self.LOG_FILE, "a") as f:
			f.write(str(transaction) + "\n" + str(self.account) + "\n")
		return transaction
	
	def print_statement(self):
		if self.account is None:
			raise Exception("No card inserted")
		
		print(f"Account statement for {self.account.owner}:")
		print(f"Current balance: {self.account.balance}")
	
account = Account(1000, "John Doe")
atm = ATM()
atm.insert_card(account)
atm.enter_pin("1234")
try:
	atm.deposit(500)
	atm.withdraw(200)
	atm.withdraw(2000)
except Exception as e:
	print(e)
print()
atm.print_statement()