# ANova Mentorship Python Project
from ... import *

# Characters:
stanley = Character('Stanley', '')
gary = Character('Gary', '')
annie = Character('Annie', '')
angela = Character('Angela','')
jesse = Character('Jesse', '')


# Things:
tickets = Thing('Tickets', '')
nachos = Thing('Nachos', '')
jersey = Thing("Warrior's Jersey", '')

# Keys:

# Places:
downtown_berkeley = Place('Downtown Berkeley', 'Downtown Berkeley - Ah, the scent of struggling college students',
                          [], [])
oracle_arena = Place('Oracle Arena', 'Oracle Arena - Home of the Warriors!', [], [])

# Exits:

# Locked Places
oracle_arena.locked = True

# Player should start at MacArthur Station
