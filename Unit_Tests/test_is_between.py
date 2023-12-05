from unittest import TestCase
from helpers import is_between


class Test(TestCase):
    def test_below_bounds(self):
        num, lower_bound, upper_bound = 1, 5, 10
        result = is_between(num, lower_bound, upper_bound)
        expected = False
        self.assertEqual(expected, result)

    def test_above_bounds(self):
        num, lower_bound, upper_bound = 90, 5, 10
        result = is_between(num, lower_bound, upper_bound)
        expected = False
        self.assertEqual(expected, result)

    def test_within_bounds(self):
        num, lower_bound, upper_bound = 7, 5, 10
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_equal_to_lower_bounds(self):
        num, lower_bound, upper_bound = 5, 5, 10
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_equal_to_upper_bounds(self):
        num, lower_bound, upper_bound = 10, 5, 10
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_float_comparisons(self):
        num, lower_bound, upper_bound = 6.9, 5.5, 10.425
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_float_and_int_comparisons(self):
        num, lower_bound, upper_bound = 6, 5.3, 15.69
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_within_bounds_same_lower_and_upper_bounds(self):
        num, lower_bound, upper_bound = 69, 69, 69
        result = is_between(num, lower_bound, upper_bound)
        expected = True
        self.assertEqual(expected, result)

    def test_outside_bounds_same_lower_and_upper_bounds(self):
        num, lower_bound, upper_bound = 69, 20, 20
        result = is_between(num, lower_bound, upper_bound)
        expected = False
        self.assertEqual(expected, result)
