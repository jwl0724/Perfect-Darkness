# Perfect Darkness - 1510 Term Project
<sup>Jonathan Liu (Set F) - A01375621</sup>

## Lore

Perfect Darkness takes place in a world where abominable creatures roam within the alleyways of urban areas. These 
creatures are difficult to dispatch, and are highly dangerous when encountered. The survival rate for such 
encounters is a measly 1%, which is attributed to the supernatural abilities these creatures often possesses. These 
creatures come in all shapes and sizes, some only enjoy scaring humans, others have the ability to wipe out an entire 
city if given the chance. An underground government backed organization has risen to deal with such creatures. No one 
knows how the organization operates, not even it's existence is known to the public. The few that do know of its 
existence refer to it as "The Foundation" and nothing more.

## Premise

You are a captured convict arrested for murder. You were captured by the foundation after murdering one of their 
leaders out of revenge. Seeing your impressive abilities in combat, the foundation has decided to start an 
"experiment" with you as the center. They want you to eliminate a supernatural creature on their behalf, 
without providing any assistance to this task, as they do not trust you in the slightest. They send you to an abandoned 
building to eliminate said creature. Armed with nothing but a flashlight, you must scour the building for any 
semblance of tools you could potentially use to aid you in your task of eliminating the creature. Can you survive?

## Gameplay

Gameplay is divided into exploration and combat modes. 

### Exploration

During exploration, you can move around the map and scour for materials littered around and collect them to boost your 
stats. The map consists of a 10x10 area, with 3 floors. Your movement is normally limited to the cardinal directions 
(North, South, East, West), but if you are on top of a set of stairs, or a hole, you can climb up a floor or down a 
floor respectively. 

Your vision is completely obscured during exploration due to the darkness of the building, you will 
not be able to see anything on the GUI. However, you do have the ability to use your flashlight, which will print 
out a map of the current floor you are at which you can use to help in navigation. Be careful using the flashlight, 
if the creature happens to be on the same floor as you, it will immediately begin chasing you. While chased, there 
is a chance for your movement to fail, so do be careful not to alert the monster prematurely.

You have the ability to listen to your surroundings. This will report back to you the direction the creature is 
relative to your position. However, listening to your surroundings takes a turn, and the monster could move to your 
floor the very next turn, do not blindly trust your ears.

### Combat

During combat you will have 3 options, attack, mend and flee. Attack, will consume your turn to damage the creature 
by an amount that is based on your attack stat, which starts at 1 and has a 5% chance of missing. Mend will consume 
your turn to heal 80% of your missing HP. Flee will consume your turn to attempt to run away from the creature, with a 
20% chance of failing.

After you have consumed your turn, the creature will take their turn. The creature can attack you for lots of damage,
heal itself by a random amount, or if you're lucky it will do nothing. The fight will end when the creature is dead, 
you are dead, or if you managed to flee.

### Goal

You will need to eliminate the creature in order to win the game. However, the creature is significantly more 
powerful than you when you first start the game. You will need to explore the map and pick up as many items as 
possible to bolster your stats, such that you will become strong enough to eliminate the creature. Try not to alert the 
creature early on, as the creature is powerful enough to kill you in two hits when you first start the game.

## Controls

No mouse or typing is required in the game, only key presses that are bound to actions which are listed in the 
following section.

### Text Navigation Controls
```angular2html
Enter - Continue to the next text prompt (occurs during story and some special action prompts)
```

### Exploration Controls

Basic Movement
```angular2html
W - Move North/Up
A - Move West/Left
S - Move South/Down
D - Move East/Right
Up Arrow - Ascend Floor (Only when on top of stairs tile)
Down Arrow - Descend Floor (Only when on top of hole tile)
```

Special Actions
```angular2html
H - Print out a list of controls on menu
L - Listen to surroundings
F - Shine flashlight and print map of floor
Enter - Take item (only if item is present on tile)
ESC - Open Pause Menu
```

Pause Menu Keys
```angular2html
1 - Save current session
2 - Load previous session
3 - Delete previous session
4 - Resume the game
5 - Quit the game
```

Selecting Saves Control
```angular2html
Up Arrow - Go to previous save in list
Down Arrow - Go to next save in list
Enter - Select the save
ESC - Cancel selection
```

### Combat Controls

Combat Menu Keys
```angular2html
1 - Attack
2 - Heal
3 - Check status
4 - Flee
```

## Requirements Checklist

| Python Elements               |              One Example Case              |
|-------------------------------|:------------------------------------------:| 
| Immutable data structures     |         constants.py, lines 15-29          |
| Mutable data structures       |             initialization.py              |   
| Exception handling            |         helpers.py, lines 204-207          |
| List/Dictionary comprehension |         helpers.py, lines 235, 237         | 
| Selection using if-statements |           game.py, lines 99-139            | 
| Repetition using loops        |       initialization.py, lines 49-75       | 
| Membership operator           |           inputs.py, lines 58-72           | 
| Range function                |         initialization.py, line 49         | 
| Itertool function usage       |        pygame_helpers.py, line 188         | 
| Random module                 |            monster.py, line 27             | 
| Function annotations          |             See all functions              | 
| Doctests and Unit Tests       | See all functions and Unit_Tests directory | 
| F-string formatting           |             input.py, line 66              |

## Folder Contents

```angular2html
├── saves # save files go here
├── Unit Tests
│   ├── __init__.py
│   ├── test_change_board_event.py
│   ├── test_chase_player.py
│   ├── test_convert_dictionary.py
│   ├── test_create_entity.py
│   ├── test_describe_location.py
│   ├── test_is_alive.py
│   ├── test_is_between.py
│   ├── test_make_board.py
│   ├── test_move.py
│   └── test_out_of_bounds.py
├── Sounds
│   ├── ambience_monster_alert.mp3
│   ├── ambience_random_1.mp3
│   ├── ambience_random_2.mp3
│   ├── ambience_random_3.mp3
│   ├── fight_encounter.mp3
│   ├── fight_monster_attack.mp3
│   ├── fight_monster_death.mp3
│   ├── fight_monster_heal.mp3
│   ├── fight_player_attack.mp3
│   ├── fight_player_heal.mp3
│   ├── fight_player_lowhealth.mp3
│   ├── initialize_start.mp3
│   ├── player_action_take.mp3
│   ├── player_death.mp3
│   ├── player_flash.mp3
│   ├── player_listen.mp3
│   ├── player_move_cardinal_chased.mp3
│   ├── player_move_cardinal_normal.mp3
│   ├── player_move_down.mp3
│   └── player_move_up.mp3
├── PDFs
│   ├── flowchart.pdf
│   └── image.pdf # Aardwolf Level 10 Picture
├── Images 
│   ├── armor.jpg
│   ├── bottle.jpg
│   ├── default.jpg
│   ├── flash.jpg
│   ├── gun.jpg
│   ├── icon.jpg
│   ├── knife.jpg
│   ├── lid.jpg
│   ├── lose.jpg
│   ├── monster.jpg
│   ├── scissor.jpg
│   ├── win.jpg
│   ├── image_darkener.py
│   └── Unfiltered_Images
│       └── example.jpg # test file for image alteration
├── Fonts 
│   └── Amatic-Bold.ttf
├── .gitignore
├── constants.py
├── game.py
├── helpers.py
├── initialization.py
├── input.py
├── monster.py
├── pygame_helpers.py
└── README.md
```


