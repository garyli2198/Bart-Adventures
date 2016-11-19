# ANova Mentorship Python Project
from game import *

# Mentors:
stanley = Character('Stanley', ['Here is your ticket.... Wait where is my money?', 
					'Nice doing business with you!'])
gary = Character('Gary', [''])
annie = Character('Annie', [''])
angela = Character('Angela',[''])
jesse = Character('Jesse', ['Looking for your friend? Are you sure you are at the right place?',
							'Looking for a friend? You did that already.'])
dennis = Character('Dennis', ["I didn't expect anyone to show up.... There's nothing up here...."])
sandy = Character('Sandy', [''])


# Things:
tickets = Thing('Tickets', 'Tickets to the Warriors Game. Need this to enter Oracle Areana.')
nachos = Thing('Nachos', 'Yummy! Best snack during a game.')
jersey = Thing("Warrior's Jersey", '#30 Curry.')
money = Thing('Money', "I'm so rich!")

# Friend:
""" Change Oski to your friends name! """
friend = Friend('Oski','Best Friends For Life')

# Keys:
# dont think we need a key class, just need to check backpack for ticket.

# Places:
downtown_berkeley = Place('Downtown Berkeley', 'Downtown Berkeley - Ah, the scent of struggling college students',
                          [], [], [])
oracle_arena = Place('Oracle Arena', 'Oracle Arena - Home of the Warriors!',
					 [], [], [])
sliver_pizzeria = Place('Sliver Pizzeria', 'Sliver Pizzeria - Best vegetarian pizza around.',
					 	[stanley], [], [])
chase_bank = Place('Chase Bank', 'Chase Bank - There is an ATM here',
                    [], [money], [])
sfo = Place('SFO', "SFO - Oh man, I'm afraid of heights", [], [], [friend])
oakland_airport = Place('Oakland Airport', 'Oakland Airport - Hmm where is my friend?',
						[jesse], [], [])
coliseum_bart = Place('Coliseum Bart Station', 'Coliseum Bart Station - Stadiums everywhere',
				[], [], [])
fruitvale_bart = Place('Fruitvale Bart Station', 'Fruitvale Bart Station - So does this place sell fruits?',
				[], [], [])
convience_store = Place('Convience Store', 'Convience Store - I wonder if I can buy snacks here',
				[], [nachos], [])
parking_lot = Place('Parking lot', 'Parking lot - There seems to be no cars', [], [], [])
macArthur_bart = Place('MacArthur Bart Station', 'MacArthur Bart Station - Transfer Station',
				[], [], [])
northBerkeley_bart = Place('North Berkeley Bart Station', 'North Berkeley Bart Station - What there is a North Berkeley?',
				[dennis], [], [])
powell_bart = Place('Powell Bart Station', 'Powell Bart Station - Underneath the MALL!',
				[], [], [])
macys = Place("Macy's", "Macy's - Hella expensive", [], [], [])
warriors_store = Place("Warriors Team Store", "Warriors Team Store - Warriors stuff, Warriors stuff everywhere",
						[], [jersey], [])

# Exits:
macArthur_bart.add_exits([northBerkeley_bart, downtown_berkeley, fruitvale_bart, coliseum_bart, powell_bart, sfo])
downtown_berkeley.add_exits([chase_bank, sliver_pizzeria, northBerkeley_bart, macArthur_bart, fruitvale_bart, coliseum_bart])
chase_bank.add_exits([downtown_berkeley])
sliver_pizzeria.add_exits([downtown_berkeley])
northBerkeley_bart.add_exits([downtown_berkeley, macArthur_bart, fruitvale_bart, coliseum_bart])
powell_bart.add_exits([macys, warriors_store, sfo, macArthur_bart, downtown_berkeley, northBerkeley_bart])
macys.add_exits([powell_bart, warriors_store])
warriors_store.add_exits([powell_bart, macys])
sfo.add_exits([powell_bart, macArthur_bart, downtown_berkeley, northBerkeley_bart])
coliseum_bart.add_exits([oracle_arena, oakland_airport, fruitvale_bart, macArthur_bart, downtown_berkeley, northBerkeley_bart])
oakland_airport.add_exits([coliseum_bart])
oracle_arena.add_exits([coliseum_bart])
fruitvale_bart.add_exits([convience_store, parking_lot, coliseum_bart, macArthur_bart, downtown_berkeley, northBerkeley_bart])
convience_store.add_exits([parking_lot, fruitvale_bart])
parking_lot.add_exits([fruitvale_bart, convience_store])

# Locked Places
oracle_arena.locked = True

# Player should start at MacArthur Station
""" Change the variable me, to your name """
me = None