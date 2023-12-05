from unittest import TestCase
from helpers import change_board_event


class Test(TestCase):
    def test_change_only_description(self):
        sample_board = {(0, 0, 0): {'Event': 'None', 'Description': 'Cool description here'}}
        change_board_event(sample_board, (0, 0, 0), 'None', 'bao')
        expected = {(0, 0, 0): {'Event': 'None', 'Description': 'bao'}}
        self.assertEqual(expected, sample_board)

    def test_change_only_event_type(self):
        sample_board = {(0, 0, 0): {'Event': 'Salvage', 'Description': 'Cool description here'}}
        change_board_event(sample_board, (0, 0, 0), 'None', 'Cool description here')
        expected = {(0, 0, 0): {'Event': 'None', 'Description': 'Cool description here'}}
        self.assertEqual(expected, sample_board)

    def test_change_both_description_and_event_type(self):
        sample_board = {(0, 0, 0): {'Event': 'Salvage', 'Description': 'Cool description here'}}
        change_board_event(sample_board, (0, 0, 0), 'None', 'bao')
        expected = {(0, 0, 0): {'Event': 'None', 'Description': 'bao'}}
        self.assertEqual(expected, sample_board)
