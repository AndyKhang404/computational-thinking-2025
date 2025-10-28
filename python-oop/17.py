class Product:
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

class Order:
	def __init__(self):
		self.products = {}
		self.discounts = []
	
	def add_product(self, product, quantity):
		if quantity <= 0 or product.stock < quantity:
			raise ValueError("Invalid quantity")
		if product in self.products:
			self.products[product] += quantity
		else:
			self.products[product] = quantity
		product.stock -= quantity
	
	def apply_discount(self, discount):
		self.discounts.append(discount)
	
	def get_total(self):
		total = sum(product.price * qty for product, qty in self.products.items())
		temp_total = total
		for discount in self.discounts:
			total -= int(temp_total * (discount / 100))
		return total

	def __str__(self):
		lines = []
		total = 0
		lines.append(f"{'Name':<30}{'Unit Price':>14}{'Qty':>8}{'Subtotal':>18}")
		lines.append("-" * 70)

		for product, qty in self.products.items():
			price_str = f"{product.price:,.0f}"
			sub_str = f"{product.price * qty:,.0f}"
			lines.append(f"{product.name:<30}{price_str:>14}{qty:>8}{sub_str:>18}")
			total += product.price * qty
		lines.append("-" * 70)

		temp_total = total
		total_str = f"{total:,.0f}"
		lines.append(f"{total_str:>70}")
		lines.append("Discounts:")
		for discount in self.discounts:
			disc_amount = int(temp_total * (discount / 100))
			disc_str = f"-{disc_amount:,.0f}"
			disc_title_str = f"{discount}% off"
			lines.append(f"{disc_title_str:<52}{disc_str:>18}")
			total -= disc_amount
		lines.append("-" * 70)

		total_str = f"{total:,.0f}"
		lines.append(f"{'Total:':<30}{total_str:>40}")

		return "\n".join(lines)

products = [
	Product("Laptop", 25_000_000, 1),
	Product("Smartphone", 15_000_000, 2),
	Product("Tablet", 10_000_000, 1)
]
order = Order()
order.add_product(products[0], 1)
order.add_product(products[1], 1)
order.add_product(products[1], 1)

try:
	order.add_product(products[1], 1)
except ValueError as e:
	print(e)

order.apply_discount(10)
order.apply_discount(5)
print("Total amount:", f"{order.get_total():,.0f}")
print(order)