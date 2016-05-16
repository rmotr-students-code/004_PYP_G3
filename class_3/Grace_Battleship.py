import random

def update_coordinate(coordinate, coordinate_change):
	"""
	Takes coordinate tuple (x, y) and adds coordinate_change(x, y) to it and 
	returns as a new tuple
	"""
	
	x = coordinate[0]
	y = coordinate[1]
	
	new_x = coordinate_change[0]
	new_y = coordinate_change[1]
	
	new_tuple = (x + new_x, y + new_y)
	
	return new_tuple


class Ship(object):
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.status = 1 # 1 is active, 0 is destroyed
		self.coordinate_dict = {}
	
	def setup_ship(self, coordinate, orientation):
		"""
		Returns all the coordinates for a ship based on the starting coordinate
		and the orientation
		"""
		
		_list = []
		
		_list.append(coordinate)
		new_coordinate = coordinate
		if orientation.startswith('v'):
			for x in range(1, self.size):
				new_coordinate = update_coordinate(new_coordinate, (0, 1))
				_list.append(new_coordinate)
				
		elif orientation.startswith('h'):
			for x in range(1, self.size):
				new_coordinate = update_coordinate(new_coordinate, (1, 0))
				_list.append(new_coordinate)
				
		return tuple(_list)
		
	def add_to_coordinates(self, *coordinates):
		for x in coordinates:
			self.coordinate_dict[x] = 1


class Board(object):
	def __init__(self):
		self.hidden = True
		
	def print_board(self, human, computer):
		"""
		Print board based on player, if the 'player' is a computer, then the
		board should reflect only hits
		"""
		print ""
		print "---Player's Board----"
		print " |A|B|C|D|E|F|G|H|I|J"
		print "0|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(0, human, computer))
		print "1|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(1, human, computer))
		print "2|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(2, human, computer))
		print "3|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(3, human, computer))
		print "4|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(4, human, computer))
		print "5|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(5, human, computer))
		print "6|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(6, human, computer))
		print "7|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(7, human, computer))
		print "8|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(8, human, computer))
		print "9|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(9, human, computer))
		print ""
		print "---------------------"
		print ""
		print "--Computer's Board---"
		print " |A|B|C|D|E|F|G|H|I|J"
		print "0|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(0, computer, human))
		print "1|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(1, computer, human))
		print "2|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(2, computer, human))
		print "3|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(3, computer, human))
		print "4|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(4, computer, human))
		print "5|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(5, computer, human))
		print "6|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(6, computer, human))
		print "7|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(7, computer, human))
		print "8|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(8, computer, human))
		print "9|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}".format(*self.check_space(9, computer, human))
		print ""
		
	def check_space(self, y_coordinate, player, opponent):
		"""
		Returns a list for print_board to read and update each row
		"""
		_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
		if player.ship_list[0].coordinate_dict == {}:
			return [random.choice(("`", "~")) for x in range(0, 10)]
		for x in range(0, 10):
			for ship in player.ship_list:
				if (x, y_coordinate) in ship.coordinate_dict:
					_list[x] = ship.coordinate_dict[(x, y_coordinate)]
					break
				else:
					_list[x] = 2
			
			if (x, y_coordinate) in opponent.misses:
				_list[x] = 3
					
		"""
		Translates each item (0, 1, 2) into an item that's more readable on the
		board. An X indicates a destroyed bit, 0 represents a whole bit, and
		the ~ and ` represent open water
		
		Also checks if the ship list is the computer ship list, and if so,
		displays nothing until the variable 'hidden' is changed
		"""
		
		for x in _list:
			if x == 0:
				_list[_list.index(x)] = "X"
			elif x == 1:
				if self.hidden == True and player.name == "The Computer":
					_list[_list.index(x)] = random.choice(("`", "~"))
				else:
					_list[_list.index(x)] = "S"
			elif x == 2:
				_list[_list.index(x)] = random.choice(("`", "~"))
			elif x == 3:
				if player.name == "The Computer" or self.hidden == False:
					_list[_list.index(x)] = 'O'
				else:
					_list[_list.index(x)] = random.choice(("`", "~"))
				
				
		return _list

		
class Player(object):
	"""
	Small class just to keep ships organized by player/computer
	"""
	def __init__(self, name):
		self.name = name
		self.submarine = Ship("Submarine", 3)
		self.aircraft = Ship("Aircraft Carrier", 5)
		self.patrol_1 = Ship("First Patrol Boat", 2)
		self.patrol_2 = Ship("Second Patrol Boat", 2)
		self.ship_list = (self.submarine,
			self.aircraft,
			self.patrol_1,
			self.patrol_2)
		self.coordinate_list = []
		self.misses = []
		self.health = 12
		self.hits = []


def input_coordinate(_input):
	"""
	reads player input and spits out a coordinate tuple
	"""
	_dict = {'a': 0,
		'b': 1,
		'c': 2,
		'd': 3,
		'e': 4,
		'f': 5,
		'g': 6,
		'h': 7,
		'i': 8,
		'j': 9
		}
	#Inputs as a string 'A3' or similar
	valid_move = False
	while valid_move == False:
		if _input == '':
			_input = raw_input("Please enter a valid coordinate: ")
		try:
			if _input[0].lower() not in _dict or not 10 > int(_input[1]) > -1:
				_input = raw_input("Please enter a valid coordinate: ")
		except ValueError:
			_input = raw_input("Please enter a valid coordinate: ")
		else:
			valid_move = True
			
	coordinate = (_dict[_input[0]], int(_input[1]))
	return coordinate
	
def coordinate_translator(coordinate):
	_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	return _list[coordinate[0]] + str(coordinate[1])

def comp_setup(size):
	"""
	returns the ship setup arguments randomly, making sure that the coordinates
	are valid based on ship size
	"""
	orientation = random.choice(('h', 'v'))
	if orientation == 'h':
		coordinate = (random.randint(0, 10-size), random.randint(0, 9))
	else:
		coordinate = (random.randint(0, 9), random.randint(0, 10-size))
	
	return (coordinate, orientation)
	
def player_setup(name, size):
	"""
	Asks for player to set up her ship. If the ship would end up out-of-bounds,
	it automattically corrects and 'shoves' the ship aside until it fits
	"""
	coordinate = input_coordinate(raw_input("Please enter the starting coordinates for your {}.: ".format(name)).lower())
	orientation = raw_input("Do you want this ship facing vertically or horizontally?: ").lower()
	
	valid_move = False
	while not valid_move:
		if orientation.startswith('h'):
			if coordinate[0] <= 10-size:
				valid_move = True
				break
			else:
				coordinate = (10-size, coordinate[1])
				valid_move = True
				break
		if orientation.startswith('v'):
			if coordinate[1] <= 10-size:
				valid_move = True
				break
			else:
				coordinate = (coordinate[1], 10-size)
				valid_move = True
				break
		else:
			orientation = raw_input("Please enter a valid orientation: ".lower())
	
	return (coordinate, orientation)
	
def collision_detection(ship_coordinates, coordinate_list):
	valid = True
	for x in ship_coordinates:
		if x in coordinate_list:
			valid = False
	
	return valid

def attack(coordinate, opponent, player):
	for x in opponent.ship_list:
		if coordinate in x.coordinate_dict:
			if x.coordinate_dict[coordinate] == 1:
				if player.name == "The Computer":
					check_if_cheating(coordinate, True)
				x.coordinate_dict[coordinate] = 0
				print "{} Hit!".format(player.name)
				opponent.health -= 1
				player.hits.append(coordinate)
				return True
			elif x.coordinate_dict[coordinate] == 0:
				return False
		

	player.misses.append(coordinate)
	if player.name == "The Computer":
		check_if_cheating(coordinate, False)
	print "{} Missed!".format(player.name)
	return True
	
def comp_attack(computer):
	misses = []
	if computer.hits == []:
		while True:
			x = random.randint(0, 9)
			y = random.randint(0, 9)
			if (x, y) in computer.misses:
				continue
			elif (x, y) in computer.hits:
				continue
			else:
				return (x, y)
	else:
		while True:
			xy = random.choice(computer.hits)
			change = random.choice(((0, 1), (1, 0)))
			xy = update_coordinate(xy, change)
			if xy in computer.misses:
				misses.append(0)
			elif xy in computer.hits:
				misses.append(0)
			else:
				return xy
			if len(misses) >= 5:
				while True:
					x = random.randint(0, 9)
					y = random.randint(0, 9)
					if (x, y) in computer.misses:
						continue
					elif (x, y) in computer.hits:
						continue
					else:
						return (x, y)

def check_if_cheating(coordinate, hit):
	answer = raw_input("Do you have a ship at {}? Y/N: ".format(coordinate_translator(coordinate))).lower()
	if answer.startswith('y') and hit == True:
		print "Thank you for telling the truth"
	elif answer.startswith('y') and hit == False:
		print "Why are you trying to trick me?"
	elif answer.startswith('n') and hit == True:
		print "Don't Lie!"
	elif answer.startswith('n') and hit == False:
		print "Darn!"

def play():
	human = Player("You")
	computer = Player("The Computer")
	board = Board()
	
	board.print_board(human, computer)
	
	for x in human.ship_list:
		initial = x.setup_ship(*player_setup(x.name, x.size))
		while not collision_detection(initial, human.coordinate_list):
			initial = x.setup_ship(*player_setup(x.name, x.size))
		for y in initial:
			human.coordinate_list.append(y)
		x.add_to_coordinates(*initial)
		board.print_board(human, computer)
				
		
			
	for x in computer.ship_list:
		initial = x.setup_ship(*comp_setup(x.size))
		while not collision_detection(initial, computer.coordinate_list):
			initial = x.setup_ship(*comp_setup(x.size))
		for y in initial:
			computer.coordinate_list.append(y)
		x.add_to_coordinates(*initial)
		
	while True:
		computer_attack = comp_attack(computer)
		attack(computer_attack, human, computer)
		print "The Computer shot at: {}".format(coordinate_translator(computer_attack))
		board.print_board(human, computer)
		if human.health <= 0:
			print "You Lost!"
			board.hidden == False
			board.print_board(human, computer)
			quit()
		human_attack = input_coordinate(raw_input("Choose where you'd wish to attack: "))
		while not attack(human_attack, computer, human):
			human_attack = input_coordinate(raw_input("Please enter a valid coordinate: "))
		print "You shot at: {}".format(coordinate_translator(human_attack))
		board.print_board(human, computer)
		if computer.health <= 0:
			print "You Won!"
			board.hidden == False
			board.print_board(human, computer)
			quit()
	
play()