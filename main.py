class User:
	def __init__(self, name : str, surname : str, balance : int):
		self.name = f'{name} {surname}'
		self.balance = balance
		self.spent = 0

	def reduce_balance(self, cost):
		self.balance -= cost
		self.spent += cost


class Product:
	def __init__(self, title, cost, developer):
		self.title = title
		self.cost = cost
		self.developer = developer

	def get_discount_price(self, cost : int, spent : int):
		"""
		Функция возвращает цену со скидкой
		Скидка имеет прямую зависимость от потраченной суммы в магазине
		"""
		return cost * (1 - (int(spent / 5000) * 0.05))


	def get_info(self):
		return f'\n{self.title} от {self.developer}\nЦена - {self.cost}$'


class Telephone(Product):
	def __init__(self, battery, *args):
		self.battery = battery
		super().__init__(*args)

class Notebook(Product):
	def __init__(self, weight, *args):
		self.weight = weight
		super().__init__(*args)


class Manager:
	def __init__(self, products):
		self.products = products
		self.register()

	def buy(self, id_product):
		price_with_discount = self.products[id_product].get_discount_price(self.products[id_product].cost, self.user.spent)
		try:
			assert price_with_discount <= self.user.balance
			self.user.reduce_balance(price_with_discount)
			print(f'Пользователь {self.user.name} купил {products[id_product].title} за {price_with_discount}$')
		except AssertionError:
			print('Недостаточно средств!')

	def show_interface(self):
		while True:
			try:
				print(f'Привет {self.user.name}!')
				products = "\n".join([product.get_info() for product in self.products])
				id_product = int(input(f'Введи айди товара который хочешь купить\n{products}\n\nВведи номер и нажми Enter: ')) - 1
				self.buy(id_product)
				print(f'Оставшийся баланс - {self.user.balance}$\n')
			except IndexError:
				print('Такого товара нет!\n')
			except ValueError:
				print('Введите индекс товара!')

	def register(self):
		name = input('Введите своё имя: ')
		surname = input('Введите свою фамилию: ')
		balance = int(input('Введите свой баланс: '))
		self.user = User(name,surname,balance)
		

products = [Telephone(1000,'Iphone X', 1000, 'Apple'), Telephone(600,'S10', 900, 'Samsung'), Notebook(2, 'Macbook Pro 13', 2500, 'Apple')]
manager = Manager(products)
manager.show_interface()
