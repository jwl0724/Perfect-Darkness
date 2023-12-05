"""
Jonathan Liu
A01375621
"""
from unittest import TestCase
from helpers import move
from pygame import constants


class Test(TestCase):
    def test_move_north(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 1, 'SPD': 1}
        move(sample_entity, constants.K_w)
        self.assertEqual(expected, sample_entity)

    def test_move_south(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 4, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 3, 'SPD': 1}
        move(sample_entity, constants.K_s)
        self.assertEqual(expected, sample_entity)

    def test_move_west(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 5, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 4, 'Y': 0, 'Z': 0, 'SPD': 1}
        move(sample_entity, constants.K_a)
        self.assertEqual(expected, sample_entity)

    def test_move_east(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 1, 'Y': 0, 'Z': 0, 'SPD': 1}
        move(sample_entity, constants.K_d)
        self.assertEqual(expected, sample_entity)

    def test_move_up(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 1, 'Z': 0, 'SPD': 1}
        move(sample_entity, constants.K_UP)
        self.assertEqual(expected, sample_entity)

    def test_move_down(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 3, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 2, 'Z': 0, 'SPD': 1}
        move(sample_entity, constants.K_DOWN)
        self.assertEqual(expected, sample_entity)

    def test_speed_given(self):
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 5, 'Y': 0, 'Z': 0, 'SPD': 1}
        move(sample_entity, constants.K_d, 5)
        self.assertEqual(expected, sample_entity)
