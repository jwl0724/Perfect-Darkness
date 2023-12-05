"""
Jonathan Liu
A01375621
"""
import random
import helpers


def make_board(row: int, height: int, col: int) -> dict:
    """
    Create board

    This function takes in row, height, and col parameters, and creates a dictionary that represents a 3D board with
    length, width and height matching those of row, col, and height parameters respectively, and each coordinate on
    the board being randomly populated with a different event type, and a randomly picked description of the location.

    :param row: An integer that represents the desired length of the board
    :param height: An integer that represents the desired width of the board
    :param col: An integer that represents the desired height of the board
    :precondition: row, height, and col must all be integers
    :precondition: row, col, height must be integers greater than 1
    :postcondition: A randomly populated dictionary representing a 3D board is created
    :return: A dictionary that represents the playable area of the game
    """
    board = {}

    possible_event_types = (
        'Salvage',  # ~15%
        'None',  # ~65%
        'Stairs',  # ~10%
        'Hole'  # ~10%
    )

    possible_salvage_event_descriptions = (
        'You feel out a trash can from the darkness, you think to yourself that the lid can be quite durable.',
        'You almost trip on something in the darkness, you manage to identify that it\'s a broken beer bottle.',
        'You feel out a dumpster from the darkness, inside it you managed to identify a worn out knife.',
        'You hear some trash bags settle, you decide to investigate and find worn out scissor buried inside.',
        'You feel a mound of debris under you, under all of it you find a worn out gun, perhaps it still works?',
        'You hear squishing sounds as you step, you feel flesh at your feet, but also a set of body armor.'
    )

    possible_none_event_descriptions = (
        'There\'s nothing here.',
        'There\'s nothing to examine.',
        'You feel nothing around.',
    )

    for y in range(height):
        for z in range(col):
            for x in range(row):
                coordinates = (x, y, z)
                random_number_event = random.randint(1, 100)

                # for stairs events
                if helpers.is_between(random_number_event, 1, 10) and y != height - 1:
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

    # create guaranteed hole and stairs in case random doesn't generate any
    for y in range(height):
        random_x = random.randint(0, row - 1)
        random_z = random.randint(0, col - 1)

        if y == 0:
            board[(random_x, y, random_z)] = \
                {'Event': 'Stairs', 'Description': 'You feel some rungs, it must be a ladder.'}

        elif y == height - 1:
            board[(random_x, y, random_z)] = \
                {'Event': 'Hole', 'Description': 'You hear settling debris below, there must be a hole here.'}

        else:
            board[(random_x, y, random_z)] = \
                {'Event': 'Stairs', 'Description': 'You feel some steps in the darkness, these must be stairs.'}

            board[(random_x * 2 % row), y, random_z * 2 % col] = \
                {'Event': 'Hole', 'Description': 'You almost trip into nothingness, you could descend here.'}

    return board


def create_entity(stats: tuple, coordinates: tuple, speed: int, **extra_attributes) -> dict:
    """
    Create an entity on the board

    This function creates an entity to be used in the game, an entity referring to either a player character,
    or enemy characters

    :param stats: A tuple of integers representing stats, where indices 0, 1, 2 represent HP, ATK, DEF respectively
    :param coordinates: A tuple of integers representing coordinates, in (x, y, z) format
    :param speed: An integer representing how much steps the entity moves per turn
    :param extra_attributes: Keyword value pairs in which extra attributes can be assigned to the entity
    :precondition: stats, coordinates must be in the correct format
    :postcondition: The inputted parameters are used to create a dictionary representing an entity on the board
    :return: A dictionary representing an entity is returned

    >>> create_entity((69, 69, 69), (0, 0, 0), 1)
    {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}

    >>> create_entity((50, 20, 20), (0, 0, 0), 2, Alerted=False, Alert_Counter=0)
    {'HP': 50, 'MAX HP': 50, 'ATK': 20, 'DEF': 20, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2, 'Alerted': False, 'Alert_Counter': 0}
    """

    entity = {
        'HP': stats[0],
        'MAX HP': stats[0],
        'ATK': stats[1],
        'DEF': stats[2],
        'X': coordinates[0],
        'Y': coordinates[1],
        'Z': coordinates[2],
        'SPD': speed,
    }

    for key, attribute in extra_attributes.items():
        entity[key] = attribute

    return entity
