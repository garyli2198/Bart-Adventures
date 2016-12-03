# Bart Adventure Game.
class Player(object):
    backpack = []
	def __init__(self, name, place):
		self.name = name
		self.place = place

	def look(self):
		self.place.look()

	def go_to(self, location):
		""" Go to a location
		"""
        destination_place = self.place.get_neighbor(location)
        if destination_place.locked:
            print(destination_place.name, 'is locked! Go look for a key to unlock it')
        else:
            self.place = destination_place
        print('You are at', self.place.name)
        
    def ask(self, person):
        """ Ask the person questions """
        if type(person) != str:
            print("Mentor has to be a string")
        elif person not in self.place.characters:
            print(person, "is not here.")
        else:
            print(person, "responds: ", self.place.characters[person].response(self))

	def check_backpack(self):
		""" Prints out all the items in your backpack.
		"""
        print('In your backpack:')
        if not self.backpack:
            print('    there is nothing.')
        else:
            for item in self.backpack:
                print('   ', item.name, '-', item.description)
        return [item.name for item in self.backpack]


	def take(self, thing):
		""" Take a thing if at player's current place.
		"""
        if type(thing) != str:
            print('Thing should be a string.')
        elif thing not in self.place.things:
            print(thing, 'is not here.')
        else:
            taken = self.place.take(thing)
            print(self.name, 'takes the', taken.name)
            self.backpack.append(taken)

    def pick_up(self, friend):
        """ Pick up a friend at player's current place.
        """
        if type(friend) != str:
            print("Friend should be a string.")
        elif friend is not self.place.friend.name:
            print(friend, " is not here.")
        else:
            print(self.name, "picks up", self.place.friend.name)
            self.backpack.append(self.place.friend)
            self.place.friend = None

	def unlock(self, place):
		""" Unlocks player's current place, if place is locked and player has ticket.
		"""
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        for item in self.backpack:
            if type(item) == Key:
                key = item
        if not key:
            print(place, " can't be unlocked without a key!")
        else:
            place_to_unlock = self.places.get_neighbor(place)
            key.use(place_to_unlock)

#requirement, message, bad 
#player can only ask one question, mentor responds with one answer depending on item in backpack
class Mentor(object):
    def __init__(self, item, name, messages):
        self.name = name
        self.item = item
        self.has_item = True
        self.missing_message = messages[0]
        self.has_message = messages[1]
    
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

class Key(Thing):
    def use(self, place):
        if place.locked:
            place.locked = False
            print(place.name, 'is now unlocked!')
        else:
            print(place.name, 'is already unlocked!')

class Place(object):
    def __init__(self, name, description, characters, things):
        self.name = name
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {}

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