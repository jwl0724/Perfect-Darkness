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
        random_x = random.randint(0, row)
        random_z = random.randint(0, col)

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


def create_entity(stats, coordinates, speed, is_player):
    """
    Create an entity on the board

    :param stats: A tuple of integers representing stats, where indices 0, 1, 2 represent HP, ATK, DEF respectively
    :param coordinates: A tuple of integers representing coordinates, in (x, y, z) format
    :param speed: An integer representing how much steps the entity moves per turn
    :param is_player: A boolean indicating whether the entity is a player or not
    :precondition: stats, coordinates must be in the correct format, speed can only be 1 or 2
    :postcondition: The inputted parameters are used to create a dictionary representing an entity on the board
    :return: A dictionary representing an entity is returned
    """
    entity = {
        'HP': stats[0],
        'ATK': stats[1],
        'DEF': stats[2],
        'X': coordinates[0],
        'Y': coordinates[1],
        'Z': coordinates[2],
        'SPD': speed,
        'Type': is_player
    }
    return entity


def main():
    print(make_board(5, 3, 5))
    player_stats, monster_stats = (5, 3, 2), (10, 5, 2)
    player_coord, monster_coord = (0, 0, 0), (3, 2, 3)
    player = create_entity(player_stats, player_coord, 1, True)
    monster = create_entity(monster_stats, monster_coord, 2, False)
    print(player)
    print(monster)


if __name__ == '__main__':
    main()
