"""
Jonathan Liu
A01375621
"""
from unittest import TestCase
from monster import chase_player


class Test(TestCase):
    def test_monster_speed_units_away(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 20}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': True, 'Alert_Counter': 19}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)

    def test_less_than_monster_speed_units_away(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 1, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 20}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': True, 'Alert_Counter': 19}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)

    def test_more_than_monster_speed_units_away(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 4, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 20}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': True, 'Alert_Counter': 19}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)

    def test_multiple_cardinal_directions(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 2, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 20}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 2, 'SPD': 2,
                    'Alerted': True, 'Alert_Counter': 19}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)

    def test_different_height(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 2, 'Z': 0, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 20}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': True, 'Alert_Counter': 19}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)

    def test_last_chase_cycle(self):
        sample_player = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': True, 'Alert_Counter': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        chase_player(sample_player, sample_monster)
        self.assertEqual(expected, sample_monster)