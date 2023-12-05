from unittest import TestCase
from helpers import out_of_bounds
from pygame import constants


class Test(TestCase):
    def test_out_of_bounds_north(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description':  'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_w)
        expected = True
        self.assertEqual(expected, result)

    def test_out_of_bounds_south(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_s)
        expected = True
        self.assertEqual(expected, result)

    def test_out_of_bounds_east(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'Cool'},
                        (0, 0, 2): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_d)
        expected = True
        self.assertEqual(expected, result)

    def test_out_of_bounds_west(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_a)
        expected = True
        self.assertEqual(expected, result)

    def test_out_of_bounds_up(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_UP)
        expected = True
        self.assertEqual(expected, result)

    def test_out_of_bounds_down(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_DOWN)
        expected = True
        self.assertEqual(expected, result)

    def test_speed_given(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_d, 2)
        expected = False
        self.assertEqual(expected, result)

    def test_not_out_of_bounds(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        sample_entity = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 1}
        result = out_of_bounds(sample_entity, sample_board, constants.K_d)
        expected = False
        self.assertEqual(expected, result)
