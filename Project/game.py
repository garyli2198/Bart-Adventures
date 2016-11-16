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

	def talk_to(self, person):
		""" Talk to person if person is at player's current place.
		"""

	def check_backpack(self):
		""" Prints out all the items in your backpack.
		"""

	def take(self, thing):
		""" Take a thing if at player's current place.
		"""

	def unlock(self, place):
		""" Unlocks player's current place, if place is locked and player has key.
		"""

class Mentor(object):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        return self.message