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


class Product:
	def __init__(self, title, cost, developer):
		self.title = title
		self.cost = cost
		self.developer = developer

	def get_discount_price(self, cost, spent):
		if spent < 1000:
			return cost
		if spent > 1000:
			return cost * 0.8


class Manager:
	def __init__(self, products, user):
		self.products = products
		self.user = user

	def buy(self, id_product):
		self.products[id_product].get_discount_price(self.user.reduce_balance(products[id_product].cost), user.spent)
		print(f'Пользователь {user.name} купил {products[id_product].title} за {products[id_product].cost}')

	def interface(self):
		try:
			print(f'Привет {user.name}!')
			products = "\n".join([product.title for product in self.products])
			id_product = int(input(f'Введи айди товара который хочешь купить\n{products}\n\nВведи номер и нажми Enter: ')) - 1
			self.buy(id_product)
			print(f'Оставшийся баланс - {user.get_balance()}')
		except IndexError:
			print('Такого товара нет!')

user = User('Ренат','Якублевич',10000, 0)
products = [Product('Iphone X', 1000, 'Apple'), Product('S10', 900, 'Samsung')]
manager = Manager(products, user)
manager.interface()




