# Provided by the course

import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = calculate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = calculate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = calculate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self):
        result = calculate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self):
        result = calculate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7.0)

    def test_expression_with_spaces(self):
        result = calculate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7.0)

if __name__ == "__main__":
    unittest.main()