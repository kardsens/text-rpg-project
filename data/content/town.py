from engine.environment import Environment, Room


class Bar(Room):
	def __init__(self, name):
		super().__init__(name)

	def enter(self):
		print('entered bar')
		print('left bar')


class Bank(Room):
	def __init__(self, name):
		super().__init__(name)

	def enter(self):
		print('entered bank')
		print('left bank')


class Inn(Room):
	def __init__(self, name):
		super().__init__(name)

	def enter(self):
		print('entered Inn')
		print('left Inn')


class Market(Room):
	def __init__(self, name):
		super().__init__(name)

	def enter(self):
		print('entered Market')
		print('left Market')

class Town(Environment):
	def __init__(self, name, sub):
		super().__init__('town',name=name,sub=sub)

	def enter(self):
		self.intro()
		while True:
			n = 1
			for sub in self.sub_environments:
				print(f'{n}. {sub.name}')
				n += 1
			choice = int(input('> '))
			self.sub_environments[choice-1].enter()
