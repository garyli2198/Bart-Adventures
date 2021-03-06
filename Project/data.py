# ANova Mentorship Python Project
from game import *

# Mentors:
#how to check whether or not they have the item
#first is item not in backpack, second is item in backpack
stanley = Mentor('Stanley', 'Tickets', ["Here are your TICKETS.... Wait where is my money?", "Nice doing business with you!"])
gary = Mentor('Gary', "Warriors Jersey", ["Want this used WARRIORS JERSEY?" , "You already took my jersey!"])
annie = Mentor('Annie', "Nachos", ["I love nachos, do you happen to want my NACHOS?", "My half eaten nachos are gone! I'm starving :(!"])
angela = Mentor('Angela', "Friend", ["I found your FRIEND Dennis. Do you want to take him?", "I already gave you your friend."])
jesse = Mentor('Jesse', ["Do you happen need to happen to need $200 MONEY from the bank?",
							"You already withdrew all your money."])
sandy = Mentor('Sandy', [""])


# Things:
tickets = Thing('Tickets', 'Tickets to the Warriors Game. Need this to enter Oracle Areana.')
nachos = Thing('Nachos', 'Yummy! Best snack during a game.')
jersey = Thing("Warriors Jersey", '#30 Curry.')
money = Thing('Money', "I'm so rich!")
friend = Thing('Friend', "I'm so popular!")

# Keys:
# dont think we need a key class, just need to check backpack for ticket.

# Places:
downtown_berkeley = Place('Downtown Berkeley', 'Downtown Berkeley - Ah, the scent of struggling college students',
                          [])
oracle_arena = Place('Oracle Arena', 'Oracle Arena - Home of the Warriors!',
					 [])
sliver_pizzeria = Place('Sliver Pizzeria', 'Sliver Pizzeria - Best vegetarian pizza around.',
					 	[stanley])
chase_bank = Place('Chase Bank', 'Chase Bank - There is an ATM here',
                    [])
sfo = Place('SFO', "SFO - Oh man, I'm afraid of heights", [angela])
oakland_airport = Place('Oakland Airport', 'Oakland Airport - Hmm where is my friend?',
						[jesse])
coliseum_bart = Place('Coliseum Bart Station', 'Coliseum Bart Station - Stadiums everywhere',
				[])
fruitvale_bart = Place('Fruitvale Bart Station', 'Fruitvale Bart Station - So does this place sell fruits?',
				[])
convenience_store = Place('Convenience Store', 'Convenience Store - I wonder if I can buy snacks here',
				[annie])
parking_lot = Place('Parking lot', 'Parking lot - There seems to be no cars', [])
macArthur_bart = Place('MacArthur Bart Station', 'MacArthur Bart Station - Transfer Station',
				[])
northBerkeley_bart = Place('North Berkeley Bart Station', 'North Berkeley Bart Station - What there is a North Berkeley?',
				[dennis])
powell_bart = Place('Powell Bart Station', 'Powell Bart Station - Underneath the MALL!',
				[])
macys = Place("Macy's", "Macy's - Hella expensive", [])
warriors_store = Place("Warriors Team Store", "Warriors Team Store - Warriors stuff, Warriors stuff everywhere",
						[])

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
fruitvale_bart.add_exits([convenience_store, parking_lot, coliseum_bart, macArthur_bart, downtown_berkeley, northBerkeley_bart])
convenience_store.add_exits([parking_lot, fruitvale_bart])
parking_lot.add_exits([fruitvale_bart, convenience_store])

# Locked Places
oracle_arena.locked = True

# Player should start at MacArthur Station
""" Change the variable me, to your name """
me = None