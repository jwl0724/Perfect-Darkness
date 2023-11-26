import random
import math
import helpers


def describe_location(player, board):
    description = board[(player['X'], player['Y'], player['Z'])]['Description']
    print(description)


def fight(player, monster):
    fighting = True
    valid_actions = ('attack', 'mend', 'flee', 'help', 'status')

    while fighting:
        print('The creature stares at you with it\'s unblinking eyes...')

        action = helpers.enforced_input('Action: ', valid_actions)
        match action:
            case 'help':
                print("""
                Attack - Spend a turn to attack the enemy, with a 10% chance to miss
                Mend - Spend a turn to heal 80% of your missing HP
                Flee - Spend a turn to try and run away from the enemy, with a 25% chance to fail
                Status - See your current health and the enemy's current condition
                """)
                continue

            case 'status':
                print(f'HP: {player["HP"]}/{player["MAX HP"]}, ATK: {player["ATK"]}, DEF: {player["DEF"]}')
                mon_hp = monster['HP']

                match mon_hp:
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.8, monster['MAX HP']):
                        print('The creature appears to has taken minimal damage...')
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.6, monster['MAX HP'] * 0.8):
                        print('You can hear ragged breathing emanating from the creature, it seems tired...')
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.4, monster['MAX HP'] * 0.6):
                        print('The hear banshee like screeches from the creature, it must be halfway dead...')
                    case mon_hp if helpers.is_between(mon_hp, monster['MAX HP'] * 0.2, monster['MAX HP'] * 0.4):
                        print('The smell of rotting flesh and blood permeate from the creature, almost there...')
                    case mon_hp if helpers.is_between(mon_hp, 0, monster['MAX HP'] * 0.2):
                        print('Your can hear blood dripping in the darkness, the creature must be near death..')
                continue

            case 'attack':
                evade_msg = 'You lunged forward at the creature, but creature used the darkness to evade your attack.'
                hit_msg = 'You lunged forward at the creature and feel flesh tearing as you swing through the darkness.'
                if random.randint(1, 10) == 1:
                    print(evade_msg)
                else:
                    monster['HP'] -= math.ceil(player['ATK'] * (1 - monster['DEF'] / 100))
                    print(hit_msg)

            case 'mend':
                heal_amount = math.floor((player['MAX HP'] - player['HP']) * 0.8)
                player['HP'] += 1 if player['HP'] == 9 else heal_amount
                if player['HP'] == player['MAX HP']:
                    print('You try to abuse your adrenaline rush, but you\'re already at max capacity.')
                print('Your abuse your adrenaline rush, allowing you to take more hits from the creature.')

            case 'flee':
                if random.randint(1, 4) != 1:
                    print('You managed to evade the creature temporarily and live another day.')
                    return
                print('You attempt to run, but the creature shrieks before you can even move, paralyzing you in fear.')

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
                if random.randint(1, 10) == 1:
                    print('The creature slashes from the darkness, but you just barely managed to avoid the hit.')
                else:
                    player['HP'] -= math.ceil(monster['ATK'] * (1 - player['DEF'] / 100))
                    print('The creature ambushes you from the darkness and takes a chunk of flesh from your body.')

            case 'heal':
                monster['HP'] += random.randint(1, 5)
                if monster['HP'] > monster['MAX HP']:
                    monster['HP'] = 50
                print('The creature rushes into the darkness and consumes something, it must have healed...')

            case 'nothing':
                print('The creature observes you from a distance, before letting out an ear piercing screech.')

        fighting = True if helpers.is_alive(player) and helpers.is_alive(monster) else False
