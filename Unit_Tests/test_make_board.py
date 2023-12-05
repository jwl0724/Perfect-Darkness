"""
Jonathan Liu
A01375621
"""
from unittest import TestCase
from unittest.mock import patch
from initialization import make_board


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_same_row_column(self, _):
        row, height, col = 2, 2, 2
        result = make_board(row, height, col)
        expected = {(0, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (0, 0, 1): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 1): {'Event': 'Stairs', 'Description': 'You feel some rungs, it must be a ladder.'},
                    (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 1, 1): {'Event': 'Hole',
                                'Description': 'You hear settling debris below, there must be a hole here.'},
                    }
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=1)
    def test_different_row_col(self, _):
        row, height, col = 3, 2, 2
        result = make_board(row, height, col)
        expected = {(0, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (2, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (0, 0, 1): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 1): {'Event': 'Stairs', 'Description': 'You feel some rungs, it must be a ladder.'},
                    (2, 0, 1): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (0, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (2, 1, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (0, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 1, 1): {'Event': 'Hole',
                                'Description': 'You hear settling debris below, there must be a hole here.'},
                    (2, 1, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    }
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=1)
    def test_greater_than_2_height(self, _):
        row, height, col = 2, 3, 2
        result = make_board(row, height, col)
        expected = {(0, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (0, 0, 1): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 0, 1): {'Event': 'Stairs', 'Description': 'You feel some rungs, it must be a ladder.'},
                    (0, 1, 0): {'Event': 'Hole',
                                'Description': 'You almost trip into nothingness, you could descend here.'},
                    (1, 1, 0): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (0, 1, 1): {'Event': 'Stairs', 'Description': 'You feel out some railings, these must be stairs.'},
                    (1, 1, 1): {'Event': 'Stairs',
                                'Description': 'You feel some steps in the darkness, these must be stairs.'},
                    (0, 2, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 2, 0): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (0, 2, 1): {'Event': 'None', 'Description': 'There\'s nothing to examine.'},
                    (1, 2, 1): {'Event': 'Hole',
                                'Description': 'You hear settling debris below, there must be a hole here.'},
                    }
        self.assertEqual(expected, result)
