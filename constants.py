knife_img, armor_img, bottle_img = 'Images/knife.jpg', 'Images/armor.jpg', 'Images/bottle.jpg'
gun_img, lid_img, scissor_img = 'Images/gun.jpg', 'Images/lid.jpg', 'Images/scissor.jpg'
monster_img, default_img, flash_img = 'Images/monster.jpg', 'Images/default.jpg', 'Images/flash.jpg'
start_sound, death_sound, take_sound = 'Sounds/initialize_start.mp3', 'Sounds/player_death.mp3', 'Sounds/player_action_take.mp3'
alert_sound, monster_damaged_sound = 'Sounds/ambience_monster_alerted.mp3', 'Sounds/fight_monster_damaged.mp3'
player_move_normal, player_move_chased = 'Sounds/player_move_cardinal_normal.mp3', 'Sounds/player_move_cardinal_chased.mp3'
player_move_up_sound, player_move_down_sound = 'Sounds/player_move_up.mp3', 'Sounds/player_move_down.mp3'
player_low_health_sound, player_attack_sound = 'Sounds/fight_player_lowhealth.mp3', 'Sounds/fight_player_attack.mp3'
monster_heal_sound = 'Sounds/fight_monster_heal.mp3'
ambience_list = ['Sounds/ambience_random_1.mp3', 'Sounds/ambience_random_2.mp3', 'Sounds/ambience_random_3.mp3']

intro_msg_list = (
    'Welcome to Perfect Darkness',
    'You are a capture convict',
    'You are sent into a building under sanction',
    'You are tasked with eliminating a creature',
    'The foundation has not provided any assistance',
    'Armed with nothing but a flashlight',
    'You must scour through the building for equipment',
    'But be careful, the building is completely dark',
    'You have no hopes of seeing the creature',
    'You must rely on subtle sounds cues',
    'While the monster hunts for prey',
    'Try not to die...'
)

overworld_help_msg_list = (
    'Take - Spend a turn to take an item, with a 5% chance of failing',
    'Move - Spend a turn to move in a direction',
    'Listen - Spend a turn to focus listening to estimate where the monster is',
    'Flash - Spend a turn to get your surroundings, also alerts the monster if it\'s on the same floor',
    'Save - Save the current state of the game',
    'Load - Load a previous save file',
    'Delete - Delete a previous save file'
)


losing_end_msg_list = (
    'You tried to defy your fate',
    'However the creature was too much for you to handle',
    'Your body was never recovered',
    'As the monster had consumed everything, bones and all',
    'The monster continues to lurk the abandoned building',
    'And as if nothing had happened',
    'The foundation continues to condemn poor souls',
    'By sending them to their deaths within that cursed building',
    'Even though...',
    'All they\'re doing is feeding the very thing they sought to destroy'
)


winning_end_msg_list = (
    'You somehow managed to slay the creature',
    'The creature lets out a howling shriek before it\'s demise',
    'It\'s body almost immediately begins to decay',
    'The stench of rotting flesh begins to permeate the building',
    'You decide it\'s time to leave the building',
    'You leave the building expecting some sort of reward',
    'Unfortunately, all that was witing for you',
    'Was the foundation\'s armed guards holding you at gun point',
    'Despite overcoming this herculean task',
    'The foundation still views you as a disposable tool',
    'And you have now become a liability to the foundation',
    'As you have seen too much for a mere tool',
    'However your efforts have not gone unacknowledged',
    'Instead of executing you then and there',
    'The higher-ups decide you could potentially be more useful in the future',
    'They decide to keep you locked up to serve as a "hunting dog"',
    'Hoping to send you to future missions',
    'To eliminate the many more anomalous entities on their behalf',
    'You have merely staved off your execution for just a tiny bit...'
)