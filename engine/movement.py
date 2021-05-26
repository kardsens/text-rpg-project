# DONT DIE, shit works, just not for 2d and 3d games, you're making a text rpg rn dumbass

class MovementHandler:
	def __init__(self, location=(0,0,0), unit=10):
		self.x = location[0]
		self.y = location[1]
		self.z = location[2]
		self.unit = 10

	def __iter__(self):
		yield self.x
		yield self.y
		yield self.z

	# cant imagine this working for 2d or 3d games
	def move(self, direction, steps=1):

		if direction == 0: # left
			self.x -= steps * self.unit
		elif direction == 1: # right
			self.x += steps * self.unit
		elif direction == 2: # forward
			self.z += steps * self.unit
		elif direction == 3: # backward
			self.z -= steps * self.unit
		elif direction == 4: # up
			self.y += steps * self.unit
		elif direction == 5: # down
			self.y -= steps * self.unit




