import engine.game as game
from engine.new_item_system import Item
from engine.movement import MovementHandler
from engine.environment import Map
from data.content.environments import environment_list

g = game.Game('Poke',100, seed=100, env_list=environment_list)



while True:

	g.map.move(int(input('> ')))
	print(tuple(g.map.coordinates))
	print('location',g.map.location.name)

	g.map.location.enter()


# dont freak out alr, the only messy files are:
# movement.py
# environment.py
# NOTHING WRONG WITH THE OTHERS











