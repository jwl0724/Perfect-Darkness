"""
Jonathan Liu
A01375621
"""
from unittest import TestCase
from helpers import describe_location


class Test(TestCase):
    def test_populated_string_description(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = 'Wow'
        result = describe_location(sample_entity, sample_board)
        self.assertEqual(expected, result)

    def test_different_event_type(self):
        sample_board = {(0, 0, 0): {'Event': 'Salvage', 'Description': 'Things here'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = 'Things here'
        result = describe_location(sample_entity, sample_board)
        self.assertEqual(expected, result)

    def test_empty_string_description(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': ''},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = ''
        result = describe_location(sample_entity, sample_board)
        self.assertEqual(expected, result)
