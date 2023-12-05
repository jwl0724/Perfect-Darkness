from unittest import TestCase
from helpers import convert_dictionary


class Test(TestCase):
    def test_tuple_to_string(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                        (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                        (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                        }
        expected = {'(0, 0, 0)': {'Event': 'None', 'Description': 'Wow'},
                    '(1, 0, 0)': {'Event': 'None', 'Description': 'Cool'},
                    '(2, 0, 0)': {'Event': 'None', 'Description': 'Amazing'}
                    }
        result = convert_dictionary(sample_board)
        self.assertEqual(expected, result)

    def test_string_to_tuple(self):
        sample_board = {'(0, 0, 0)': {'Event': 'None', 'Description': 'Wow'},
                        '(1, 0, 0)': {'Event': 'None', 'Description': 'Cool'},
                        '(2, 0, 0)': {'Event': 'None', 'Description': 'Amazing'}
                        }
        expected = {(0, 0, 0): {'Event': 'None', 'Description': 'Wow'},
                    (1, 0, 0): {'Event': 'None', 'Description': 'Cool'},
                    (2, 0, 0): {'Event': 'None', 'Description': 'Amazing'}
                    }
        result = convert_dictionary(sample_board)
        self.assertEqual(expected, result)
