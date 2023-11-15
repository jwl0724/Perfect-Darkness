import random


def introduce_game():
    print("""
    Welcome to Perfect Darkness, you are a captured convict sent into a building under sanction. You are tasked 
    with eliminating the creature confined within the building. The foundation has not provided any tools or weapons 
    to help in your task, armed with nothing but your wits, you must scour through the building to find any 
    semblance of equipment to help you in your task. But be careful, the creature is roaming about looking for any 
    prey that has entered it's domain.
    """)

    print('Press enter to continue.')
    print('----------------------------------------------------------------------------')

def make_board(row, height, col):
board = {}
    possible_populating_options = [
        ''
    ]

    for y in range(height):
        for z in range(col):
            for x in range(row):

                coordinates = (x, y, z)


    return board

def create_entity(stats, coordinates, speed, name):