monster_img, default_img, flash_img = 'Images/monster.jpg', 'Images/default.jpg', 'Images/flash.jpg'
win_img, lose_img, icon_img = 'Images/win.jpg', 'Images/lose.jpg', 'Images/icon.jpg'
start_sound, death_sound = 'Sounds/initialize_start.mp3', 'Sounds/player_death.mp3'
alert_sound, monster_attack_sound = 'Sounds/ambience_monster_alerted.mp3', 'Sounds/fight_monster_attack.mp3'
move_sound, chased_sound = 'Sounds/player_move_cardinal_normal.mp3', 'Sounds/player_move_cardinal_chased.mp3'
player_move_up_sound, player_move_down_sound = 'Sounds/player_move_up.mp3', 'Sounds/player_move_down.mp3'
player_low_health_sound, player_attack_sound = 'Sounds/fight_player_lowhealth.mp3', 'Sounds/fight_player_attack.mp3'
take_sound, start_fight_sound = 'Sounds/player_action_take.mp3', 'Sounds/fight_encounter.mp3'
monster_death_sound, player_heal_sound = 'Sounds/fight_monster_death.mp3', 'Sounds/fight_player_heal.mp3'
monster_heal_sound, player_listen_sound = 'Sounds/fight_monster_heal.mp3', 'Sounds/player_listen.mp3'
flash_sound = 'Sounds/player_flash.mp3'
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


monster_condition_desc_list = (
    'The creature appears to have taken little to no damage...',
    'You can hear rugged breathing emanating from the creature, you must have done some damage to it...',
    'You hear banshee like screeches within the darkness, it must be halfway dead...',
    'The smell of rotting flesh permeates from the creature, It should be close to dead now...',
    'You can hear the sounds of blood dripping from the creature, It\'s on it\'s last legs...'
)


pause_menu_list = (
    'PAUSED',
    '1. Save',
    '2. Load',
    '3. Delete',
    '4. Resume',
    '5. Quit'
)


flash_help_msg_list = (
    'Tile Legend:',
    'Red - Monster location',
    'Green - Your location',
    'Grey - No special tile',
    'Blue - Salvageable item',
    'Yellow - Stair location',
    'Magenta - Hole location'
)


overworld_help_msg_list = (
    'ENTER - Spend a turn to take an item, with a 5% chance of failing',
    'WASD - Spend a turn to move in a direction',
    'L - Spend a turn to focus listening to estimate where the monster is',
    'F - Spend a turn to get your surroundings, also alerts the monster if it\'s on the same floor',
    'ESC - Pause the game to save, load, or delete your saves'
)


fight_help_msg_list = (
    '1. Attack - Spend a turn to attack the enemy, with a 10% chance to miss',
    '2. Mend - Spend a turn to heal 80% of your missing HP',
    '3. Status - See your current health and the enemy\'s current condition',
    '4. Flee - Spend a turn to try and run, with a 25% chance to fail'
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
    'All they\'re doing is feeding the very thing they sought to destroy',
    'Game over...',
    'The game will now close...'
)


winning_end_msg_list = (
    'You somehow managed to slay the creature',
    'The creature lets out a howling shriek before it\'s demise',
    'It\'s body almost immediately begins to decay',
    'The stench of rotting flesh begins to permeate the building',
    'You decide it\'s time to leave the building',
    'You leave the building expecting some sort of reward',
    'Unfortunately, all that was waiting for you',
    'Was the foundation\'s armed guards holding you at gun point',
    'Despite overcoming this herculean task',
    'The foundation still views you as a disposable tool',
    'And you have now become a liability to the foundation',
    'As you have seen too much for a mere tool',
    'However your efforts have not gone unacknowledged',
    'Instead of executing you then and there',
    'The higher-ups decide you could be an asset',
    'They decide to keep you locked up to serve as a "hunting dog"',
    'Hoping to send you to future missions',
    'To eliminate the many more anomalous entities on their behalf',
    'You have merely staved off your execution for just a tiny bit...',
    'Congratulations, You have won the game',
    'The game will now close'
)
