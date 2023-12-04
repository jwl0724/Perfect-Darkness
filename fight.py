import random
import math
import helpers
import pygame as pg
import pygame_helpers as pg_help
import constants as con


def start_fight(screen: object, valid_inputs: list[pg.constants], player: dict, monster: dict) -> None:
    """
    Run fight turn-based fight mini-game

    This function runs the fighting portion of the game, where the parameters are used to run and maintain the game.

    :param screen: A pygame surface object, which represents the game window
    :param valid_inputs: A list of pygame constants that represent the allowed keys during the fight
    :param player: A dictionary representing the player
    :param monster: A dictionary representing the monster
    :precondition: Screen must be a pygame surface object and valid inputs
    :precondition: Valid_inputs must be a list of pygame constants that represent key presses
    :precondition: player and monster must be dictionaries that represent a player and monster respectively
    :postcondition: The turn based fight mini-game is run
    :postcondition: Sounds and text will be drawn over the window throughout the course of the fight
    """
    fighting = True
    pg_help.draw_one_line_text(screen, 'The creature stares at you with it\'s unblinking eyes...')

    # enter fight loop
    while fighting:
        # play low health sound if player has less than 30% health remaining
        pg_help.play_sound(con.player_low_health_sound) if player['HP'] < math.floor(player['MAX HP'] * 0.3) else None

        # print out available actions during fight
        pg_help.draw_multi_line_text(screen, con.fight_help_msg_list, wait=False)

        # wait for player input
        key_pressed = pg_help.wait_for_input(valid_inputs)
        match key_pressed:
            # when 3 is pressed, shows player health, and a description of the monster's condition based on it's health
            case pg.K_3:
                # get string for player stats
                player_stats = f'HP: {player["HP"]}/{player["MAX HP"]}, ATK: {player["ATK"]}, DEF: {player["DEF"]}'

                # determine description of monster's condition based on what percentage of health it is at
                # monster condition descriptions are stored in the constants file
                mon_hp = monster['HP']
                match mon_hp:
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.8, monster['MAX HP']):
                        monster_condition = con.monster_condition_desc_list[0]
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.6, monster['MAX HP'] * 0.8):
                        monster_condition = con.monster_condition_desc_list[1]
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.4, monster['MAX HP'] * 0.6):
                        monster_condition = con.monster_condition_desc_list[2]
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.2, monster['MAX HP'] * 0.4):
                        monster_condition = con.monster_condition_desc_list[3]
                    case _:
                        monster_condition = con.monster_condition_desc_list[4]

                # draw the status descriptions on the GUI
                pg_help.draw_multi_line_text(screen, [player_stats, monster_condition])
                continue

            # When 1 is pressed, player damages the monster based on attack stat, with a 10% chance to miss
            case pg.K_1:
                evade_msg = 'You lunged forward at the creature, but creature used the darkness to evade your attack.'
                hit_msg = 'You lunged forward at the creature and feel flesh tearing as you swing through the darkness.'
                # print miss message onto the GUI
                if random.randint(1, 10) == 1:
                    pg_help.draw_one_line_text(screen, evade_msg)
                # print hit message onto the GUI, decrease monster health, and play a slash sfx
                else:
                    pg_help.play_sound(con.player_attack_sound)
                    monster['HP'] -= math.ceil(player['ATK'] * (1 - monster['DEF'] / 100))
                    pg_help.draw_one_line_text(screen, hit_msg)

            # When 2 is pressed, player heals 80% of their missing health
            case pg.K_2:
                # calculate healed amount, rounded to the lowest integer
                heal_amount = math.floor((player['MAX HP'] - player['HP']) * 0.8)
                # ensure health is restored when trying to heal with 1 HP missing
                player['HP'] += 1 if player['HP'] == player['MAX HP'] - 1 else heal_amount
                # prevent healing over the player's max HP and draw the text of the fail onto the  GUI
                if player['HP'] == player['MAX HP']:
                    fail_heal_msg = 'You try to abuse your adrenaline rush, but you failed'
                    pg_help.draw_one_line_text(screen, fail_heal_msg)
                # draw the message of successful healing on the GUI and play sfx for healing
                else:
                    pg_help.play_sound(con.player_heal_sound)
                    heal_msg = 'Your abuse your adrenaline rush, allowing you to take more hits from the creature.'
                    pg_help.draw_one_line_text(screen, heal_msg)

            # when 4 is pressed, player runs away from battle, with a 25% chance of failing to run
            case pg.K_4:
                # draw successful escape message onto the GUI and play sfx for it
                if random.randint(1, 4) != 1:
                    pg_help.play_sound(con.chased_sound)
                    esc_msg = 'You managed to evade the creature temporarily'
                    pg_help.draw_one_line_text(screen, esc_msg)
                    return
                # draw failed escape attempt onto GUI
                fail_esc_msg_list = [
                    'You attempt to run',
                    'But the creature blocks your path',
                    'You are paralyzed in fear'
                ]
                pg_help.draw_one_line_text(screen, fail_esc_msg_list)

        # check if player's attack killed the monster during their turn, play sound if it did
        if not helpers.is_alive(monster):
            pg_help.play_sound(con.monster_attack_sound)
            fighting = False
            continue

        monster_actions = ('attack', 'heal', 'nothing')  # 75%, 20%, 5% respectively

        # generate a random number to determine monster's action
        random_num = random.randint(1, 100)
        if helpers.is_between(random_num, 1, 75):
            action = monster_actions[0]
        elif helpers.is_between(random_num, 76, 95):
            action = monster_actions[1] if monster['HP'] != monster['MAX HP'] else monster_actions[0]
        else:
            action = monster_actions[2]

        # process monster actions
        match action:
            # process monster attack
            case 'attack':
                # play sfx for monster attacking
                pg_help.play_sound(con.monster_attack_sound)
                # generate a random number to see if monster hits, then draw the outcome onto the GUI
                if random.randint(1, 10) == 1:
                    miss_msg_list = ['The creature slashes from the darkness', 'You just barely avoided the hit']
                    pg_help.draw_one_line_text(screen, miss_msg_list)
                else:
                    # decrease player health based on how much defense the player has accumulated throughout the game
                    player['HP'] -= math.ceil(monster['ATK'] * (1 - player['DEF'] / (100 + player['DEF'])))
                    hit_msg_list = ['The creature ambushes you from the darkness',
                                    'It takes a chunk of flesh from your body']
                    pg_help.draw_one_line_text(screen, hit_msg_list)

            # process monster healing
            case 'heal':
                # play sfx for when monster heals
                pg_help.play_sound(con.monster_heal_sound)

                # generate a random healing amount between 5 and 20
                monster['HP'] += random.randint(5, 20)

                # ensure monster does not heal over its max HP
                monster['HP'] = monster['MAX HP'] if monster['HP'] > monster['MAX HP'] else monster['HP']

                # draw monster healing message onto the GUI
                monster_heal_msg_list = [
                    'The creature rushes into the darkness', 
                    'You hear the sound of flesh being chewed',
                    'It must have healed...'
                ]
                pg_help.draw_one_line_text(screen, monster_heal_msg_list)

            # process when monster does nothing
            case 'nothing':
                # draw the eerie message onto the GUI
                monster_nothing_msg_list = [
                    'The creature observes you from a distance',
                    'It\'s cautiously analyzing you...',
                ]
                pg_help.draw_one_line_text(screen, monster_nothing_msg_list)

        # check if player had died during monster's turn, if so then fighting has stopped
        fighting = True if helpers.is_alive(player) else False
