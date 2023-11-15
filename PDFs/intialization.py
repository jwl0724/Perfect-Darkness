import random
import helpers


def introduce_game():
    print("""
    Welcome to Perfect Darkness, you are a captured convict sent into a building under sanction. You are tasked 
    with eliminating the creature confined within the building. The foundation has not provided any tools or weapons 
    to help in your task, armed with nothing but your wits, you must scour through the building to find any 
    semblance of equipment to help you in your task. But be careful, the building is in complete darkness with no 
    hopes of seeing the creature. You must rely on the subtle sounds the creature makes as it roams around, 
    looking for prey within it's domain.
    """)

    print('Press enter to continue.')
    print('----------------------------------------------------------------------------')


def make_board(row, height, col):
    board = {}

    possible_event_types = [
        'Salvage',  # ~15%
        'None',  # ~65%
        'Stairs',  # ~10%
        'Hole'  # ~10%
    ]

    possible_salvage_event_descriptions = [
        'You feel out a trash can from the darkness, you think to yourself that the lid can be quite durable.',
        'You almost trip on something in the darkness, you manage to identify that it\'s a broken beer bottle.',
        'You feel out a dumpster from the darkness, inside it you managed to identify a worn out knife.',
        'You hear some trash bags settle, you decide to investigate and find worn out scissor buried inside.',
        'You feel a mound of debris under you, under all of it you find a worn out gun, perhaps it still works?',
        'You hear squishing sounds as you step, you feel flesh at your feet, but also a set of body armor.'
    ]

    possible_none_event_descriptions = [
        'There\'s nothing here.',
        'There\'s nothing to examine.',
        'You feel nothing around.',
    ]

    for y in range(height):
        for z in range(col):
            for x in range(row):
                coordinates = (x, y, z)
                random_number_event = random.randint(1, 100)

                # for stairs events
                if helpers.is_between(random_number_event, 1, 10) and y != 2:
                    description = 'You feel out some railings, these must be stairs.'
                    board[coordinates] = {'Event': possible_event_types[2], 'Description': description}

                # for holes events
                elif helpers.is_between(random_number_event, 11, 20) and y != 0:
                    description = 'You feel nothing in front of you, this must be a hole to descend down.'
                    board[coordinates] = {'Event': possible_event_types[3], 'Description': description}

                # for salvage events
                elif helpers.is_between(random_number_event, 86, 100):
                    random_number_salvage = random.randint(0, 5)
                    board[coordinates] = {'Event':  possible_event_types[0],
                                          'Description': possible_salvage_event_descriptions[random_number_salvage]}

                # for none events
                else:
                    random_number_none = random.randint(0, 2)
                    board[coordinates] = {'Event': possible_event_types[1],
                                          'Description': possible_none_event_descriptions[random_number_none]}

    # create stairs and holes at set locations, in case random doesn't generate any
    board[(0, 0, 0)] = {'Event': 'Stairs', 'Description': 'You feel some steps in the darkness, these must be stairs.'}
    board[(2, 1, 3)] = {'Event': 'Stairs', 'Description': 'You feel some rungs, it must be a ladder.'}
    board[(2, 1, 3)] = {'Event': 'Hole', 'Description': 'You hear settling debris below, there must be a hole here.'}
    board[(3, 2, 4)] = {'Event': 'Hole', 'Description': 'You almost trip into nothingness, you could descend here.'}

    return board


def create_entity(stats, coordinates, speed, name):
    pass
