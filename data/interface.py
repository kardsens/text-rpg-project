"""

for a text interface the assets for the menu must be in the following format:

menu_info = {

	'title': 'Title for your text menu!',
	'options': [
		{"key to access option, eg. '1'":{'option title to display':function_for_option}},
		{"key to access option, eg. '2'":{'option title to display':function_for_option}},
		{'3':{'enter the bar':enter_bar}},
		{'inv':{'inventory options':inv_op}}
	]

}

"""
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


def menu(info):
	clear()
	print(info['title'])
	print('-----------------------------------------')
	for option in info['options']:
		for key, option_info in option.items():
			print(f'[{key}] {list(option_info.keys())[0]}')

	print('[e] Exit') # testing purposes only
	print('-----------------------------------------')
	choice = input('> ').lower().strip()

	if choice == 'e': # standard exit key for text menu
		return None

	for option in info['options']:
		for key, option_info in option.items():
			if choice == key:
				return option_info[list(option_info.keys())[0]] # return corresponding function
	clear()
	print('no such option as "'+choice+'"')
	menu(info)



if __name__ == '__main__':

	def inn():
		print('you have entered and exited the inn')

	def bar():
		print('you have entered and exited the bar')

	def cookie():
		print('you have consumed your cookie')

	def inv_op():
		print('you have nothing so dont bother')

	menu_info = {

		'title': 'Village',
		'options': [
			{"1":{'enter inn':inn}},
			{"2":{'enter bar':bar}},
			{'3':{'have a cookie lmao':cookie}},
			{'inv':{'inventory options':inv_op}}
		]

	}

	menu(menu_info)


	  