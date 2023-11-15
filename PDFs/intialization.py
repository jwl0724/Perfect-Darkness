import random

def introduce_game():
    print("""
    Welcome to The Stairs
    
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

def create_entity(health, coordinates, speed):