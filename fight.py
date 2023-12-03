import random
import math
import helpers
import pygame as pg
import pygame_helpers as pg_help
import constants as con


def start_fight(screen, valid_inputs, player, monster):
    fighting = True
    pg_help.draw_one_line_text(screen, 'The creature stares at you with it\'s unblinking eyes...')

    while fighting:
        pg_help.play_sound(con.player_low_health_sound) if player['HP'] < math.floor(player['MAX HP'] * 0.3) else None
        pg_help.draw_multi_line_text(screen, con.fight_help_msg_list, wait=False)
        key_pressed = pg_help.wait_for_input(valid_inputs)
        match key_pressed:
            case pg.K_3:
                player_stats = f'HP: {player["HP"]}/{player["MAX HP"]}, ATK: {player["ATK"]}, DEF: {player["DEF"]}'
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

                pg_help.draw_multi_line_text(screen, [player_stats, monster_condition])
                continue

            case pg.K_1:
                evade_msg = 'You lunged forward at the creature, but creature used the darkness to evade your attack.'
                hit_msg = 'You lunged forward at the creature and feel flesh tearing as you swing through the darkness.'
                if random.randint(1, 10) == 1:
                    pg_help.draw_one_line_text(screen, evade_msg)
                else:
                    pg_help.play_sound(con.player_attack_sound)
                    monster['HP'] -= math.ceil(player['ATK'] * (1 - monster['DEF'] / 100))
                    pg_help.draw_one_line_text(screen, hit_msg)

            case pg.K_2:
                heal_amount = math.floor((player['MAX HP'] - player['HP']) * 0.8)
                player['HP'] += 1 if player['HP'] == player['MAX HP'] - 1 else heal_amount
                if player['HP'] == player['MAX HP']:
                    fail_heal_msg = 'You try to abuse your adrenaline rush, but you failed'
                    pg_help.draw_one_line_text(screen, fail_heal_msg)
                else:
                    pg_help.play_sound(con.player_heal_sound)
                    heal_msg = 'Your abuse your adrenaline rush, allowing you to take more hits from the creature.'
                    pg_help.draw_one_line_text(screen, heal_msg)

            case pg.K_4:
                if random.randint(1, 4) != 1:
                    pg_help.play_sound(con.chased_sound)
                    esc_msg = 'You managed to evade the creature temporarily'
                    pg_help.draw_one_line_text(screen, esc_msg)
                    return

                fail_esc_msg_list = [
                    'You attempt to run',
                    'But the creature blocks your path',
                    'You are paralyzed in fear'
                ]

                pg_help.draw_one_line_text(screen, fail_esc_msg_list)

        if not helpers.is_alive(monster):
            pg_help.play_sound(con.monster_attack_sound)
            fighting = False
            continue

        monster_actions = ('attack', 'heal', 'nothing')  # 75%, 20%, 5% respectively
        random_num = random.randint(1, 100)

        if helpers.is_between(random_num, 1, 75):
            action = monster_actions[0]
        elif helpers.is_between(random_num, 76, 95):
            action = monster_actions[1] if monster['HP'] != monster['MAX HP'] else monster_actions[0]
        else:
            action = monster_actions[2]

        match action:
            case 'attack':
                pg_help.play_sound(con.monster_attack_sound)
                if random.randint(1, 10) == 1:
                    miss_msg_list = ['The creature slashes from the darkness', 'You just barely avoided the hit']
                    pg_help.draw_one_line_text(screen, miss_msg_list)
                else:
                    player['HP'] -= math.ceil(monster['ATK'] * (1 - player['DEF'] / (100 + player['DEF'])))
                    hit_msg_list = ['The creature ambushes you from the darkness',
                                    'It takes a chunk of flesh from your body']
                    pg_help.draw_one_line_text(screen, hit_msg_list)

            case 'heal':
                pg_help.play_sound(con.monster_heal_sound)
                monster['HP'] += random.randint(1, 5)
                if monster['HP'] > monster['MAX HP']:
                    monster['HP'] = monster['MAX HP']
                monster_heal_msg_list = [
                    'The creature rushes into the darkness', 
                    'You hear the sound of flesh being chewed',
                    'It must have healed...'
                ]
                pg_help.draw_one_line_text(screen, monster_heal_msg_list)

            case 'nothing':
                monster_nothing_msg_list = [
                    'The creature observes you from a distance',
                    'It\'s cautiously analyzing you...',
                ]
                pg_help.draw_one_line_text(screen, monster_nothing_msg_list)

        fighting = True if helpers.is_alive(player) and helpers.is_alive(monster) else False
