import engine.game as game
from engine.item_system import Weapon, Sword, Consumable, Magic, Item
from engine.combat_system import Attack


if __name__ == '__main__':

	game1 = game.Game('new player',0)


	print(game1.player.name)
	print(game1.clock.stats())

	game1.load()

	print(game1.player.name)
	print(game1.clock.stats())
	


	
	

