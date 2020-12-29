class User:
	def __init__(self, name, surname, balance, spent):
		self.name = name
		self.surname = surname
		self.balance = balance
		self.spent = spent

	def reduce_balance(self, cost):
		self.balance -= cost
		self.spent += cost

	def get_balance(self):
		return self.balance

	def get_spent(self):
		return self.spent


class Product:
	def __init__(self, title, cost, developer):
		self.title = title
		self.cost = cost
		self.developer = developer

	def get_discount_price(self, cost, spent):
		if spent < 1000:
			return cost
		if spent < 3000:
			return int(cost * 0.8)
		return int(cost * 0.6)
	def get_info(self):
		return f'\n{self.title} от {self.developer}\nЦена - {self.cost}'


class Telephone(Product):
	def __init__(self, battery, *args):
		self.battery = battery
		super().__init__(*args)

class Notebook(Product):
	def __init__(self, weight, *args):
		self.weight = weight
		super().__init__(*args)


class Manager:
	def __init__(self, products, user):
		self.products = products
		self.user = user

	def buy(self, id_product):
		price_with_discount = self.products[id_product].get_discount_price(self.products[id_product].cost, self.user.get_spent())
		if price_with_discount <= self.user.balance:
			self.user.reduce_balance(price_with_discount)
			print(f'Пользователь {user.name} купил {products[id_product].title} за {price_with_discount}')
		else:
			print('Недостаточно средств!\n')

	def interface(self):
		while True:
			try:
				print(f'Привет {user.name}!')
				products = "\n".join([product.get_info() for product in self.products])
				id_product = int(input(f'Введи айди товара который хочешь купить\n{products}\n\nВведи номер и нажми Enter: ')) - 1
				self.buy(id_product)
				print(f'Оставшийся баланс - {user.get_balance()}\n')
			except IndexError:
				print('Такого товара нет!\n')

user = User('Ренат','Якублевич',10000, 1100)
products = [Telephone(1000,'Iphone X', 1000, 'Apple'), Telephone(600,'S10', 900, 'Samsung'), Notebook(2, 'Macbook Pro 13', 2500, 'Apple')]
manager = Manager(products, user)
manager.interface()




