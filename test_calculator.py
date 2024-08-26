import unittest
from app import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculate("+", 2, 3)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate("/", 5, 0)