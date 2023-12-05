from unittest import TestCase
from monster import move_monster
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', side_effect=[1, 0])
    def test_move_north(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 1, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 1])
    def test_move_south(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 2, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 1, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 3])
    def test_move_west(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 1, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 2])
    def test_move_east(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 1, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 4])
    def test_move_up(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 1, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 5])
    def test_move_down(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 2, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 1, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[2, 2])
    def move_unit_equal_to_speed(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 2, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}
        move_monster(sample_monster, sample_board)
        self.assertEqual(expected, sample_monster)

    @patch('random.randint', side_effect=[1, 3])
    def test_preventing_move_out_of_bounds(self, _):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 0, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                        (1, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'}
                        }
        sample_monster = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                          'Alerted': False, 'Alert_Counter': 0}
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 2,
                    'Alerted': False, 'Alert_Counter': 0}

        with self.assertRaises(StopIteration):
            move_monster(sample_monster, sample_board)

        self.assertEqual(expected, sample_monster)
