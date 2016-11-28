# Bart Adventure Game.
class Player(object):
	def __init__(self, name, place):
		self.name = name
		self.place = place

	def look(self):
		self.place.look()

	def go_to(self, location):
		""" Go to a location
		"""
        return None
        
    def ask(self, person):
        """ Ask the person questions """
        return None

	def talk_to(self, person):
		""" Talk to person if person is at player's current place.
		"""
        return None

	def check_backpack(self):
		""" Prints out all the items in your backpack.
		"""
        return None

	def take(self, thing):
		""" Take a thing if at player's current place.
		"""
        return None

    def pick_up(self, friend):
        """ Pick up a friend at player's current place.
        """
        return None

	def unlock(self, place):
		""" Unlocks player's current place, if place is locked and player has ticket.
		"""
        return None

#requirement, message, bad 
#player can only ask one question, mentor responds with one answer depending on item in backpack
class Mentor(object):
    def __init__(self, item, name, messages):
        self.name = name
        self.item = item
        self.has_item = True
        self.missing_message = message[0]
        self.has_message = message[1]
    
    #response for line of questioning
    def response(self, player):
        #check item in backpack
        if item not in player.check_backpack():
            return self.missing_message
        else:
            return self.has_message
    
    #if player decides they want say take
    def give(self, player):
        if self.has_item and self.item:
            print(self.name, 'gives the ', item)
            player.backpack.append(item)
            self.has_item = False
        print("I do not have anything to give you.")


class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, place):
        print("You can't use a {0} here".format(self.name))

class Friend(object):
    def __init__(self, name, message):
        self.name = name #We can make this an input
        self.message = message

    def talk(self):
        return self.message

class Key(Thing):
    def use(self, place):
        if place.locked:
            place.locked = False
            print(place.name, 'is now unlocked!')
        else:
            print(place.name, 'is already unlocked!')

class Place(object):
    def __init__(self, name, description, characters, things, friend):
        self.name = name
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {}
        self.friend = 

    def look(self):
        print('You are currently at ' + self.name + '. You take a look around and see:')
        print('Characters:')
        if not self.characters:
            print('    no one in particular')
        else:
            for character in self.characters:
                print('   ', character)
        print('Things:')
        if not self.things:
            print('    nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        self.check_exits()

    def get_neighbor(self, exit):
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits:
            exit_place = self.exits[exit][0]
            return exit_place
        else:
            print("Can't go to {} from {}.".format(exit, self.name))
            print("Try looking around to see where to go.")
            return self

    def take(self, thing):
        return self.things.pop(thing)

    def check_exits(self):
        print('You can exit to:')
        for exit in self.exits:
            print('   ', exit)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)