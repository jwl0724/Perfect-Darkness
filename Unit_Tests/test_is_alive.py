"""
Jonathan Liu
A01375621
"""
from unittest import TestCase
from helpers import is_alive


class Test(TestCase):
    def test_HP_in_negatives(self):
        sample_entity = {'HP': -25, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = is_alive(sample_entity)
        expected = False
        self.assertEqual(expected, result)

    def test_HP_0(self):
        sample_entity = {'HP': 0, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = is_alive(sample_entity)
        expected = False
        self.assertEqual(expected, result)

    def test_HP_greater_than_0(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = is_alive(sample_entity)
        expected = True
        self.assertEqual(expected, result)
