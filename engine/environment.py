import random

class Room:
	def __init__(self, name):
		self.name = name

class Environment(Room):
	def __init__(self, type_, name=None, enter=None, sub=None, intro=None):
		super().__init__(name)
		self.type = type_ # town, city, forest, etc.
		self.sub_environments = sub
		self.introduction = intro

	# interface related
	def intro(self):
		if self.introduction:
			print(self.introduction)
		else:
			print('You have entered ',end='')
			if self.type[0].lower() in 'aeiou':
				print(f'an {self.type}',end='')
			else:
				print(f'a {self.type}',end='')

			if self.name:
				print(f', called {self.name}')
			else:
				print()


class Map:
	def __init__(self, seed, environment_list, location):
		self.seed = seed
		self.environments = environment_list
		self.coordinates = location

	def move(self, direction, steps=1):
		self.coordinates.move(direction, steps)

	@property	
	def location(self):
		random.seed(self.seed+self.coordinates.x+self.coordinates.y)
		return random.choice(self.environments)






