import unittest
import math

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 4, 6)

    def test_decimal_addition(self):
        self.assertEqual(2.5 + 1.5, 4.0)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 5, 10)

    def test_multiplication_by_zero(self):
        self.assertEqual(5 * 0, 0)

    def test_division(self):
        self.assertEqual(6 / 3, 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            6 / 0

    def test_square_root(self):
        self.assertEqual(math.sqrt(9), 3)

    def test_square_root_of_zero(self):
        self.assertEqual(math.sqrt(0), 0)

    def test_square_root_of_decimal(self):
        self.assertAlmostEqual(math.sqrt(2), 1.41421356, places=7)

    def test_percentage(self):
        self.assertEqual(50 / 100, 0.5)

    def test_positive_to_negative(self):
        self.assertEqual(5 * -1, -5)

    def test_negative_to_positive(self):
        self.assertEqual(-5 * -1, 5)



if __name__ == "__main__":
    unittest.main()