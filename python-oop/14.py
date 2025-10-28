import json

class JSONSerializableMixin:
	def to_json(self):
		return json.dumps(self.__dict__)

class Product(JSONSerializableMixin):
	def __init__(self, name, price):
		self.name = name
		self.price = price
	
product = Product("Laptop", 25_000_000)
print(product.to_json())