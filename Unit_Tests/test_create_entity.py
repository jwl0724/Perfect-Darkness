from unittest import TestCase
from initialization import create_entity


class Test(TestCase):
    def test_no_extra_attributes(self):
        result = create_entity((69, 69, 69), (0, 0, 0), 5)
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 5}
        self.assertEqual(expected, result)

    def test_one_extra_attribute(self):
        result = create_entity((69, 69, 69), (0, 0, 0), 5, Cool=False)
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 5, 'Cool': False}
        self.assertEqual(expected, result)

    def test_more_than_one_extra_attribute(self):
        result = create_entity((69, 69, 69), (0, 0, 0), 5, Needs_Help=True, Status='Debt', Age=77)
        expected = {'HP': 69, 'MAX HP': 69, 'ATK': 69, 'DEF': 69, 'X': 0, 'Y': 0, 'Z': 0, 'SPD': 5,
                    'Needs_Help': True, 'Status': 'Debt', 'Age': 77}
        self.assertEqual(expected, result)
