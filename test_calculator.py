import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 4, 6)

    def test_decimal_addition(self):
        self.assertEqual(2.5 + 1.5, 4.0)

    def test_substraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 5, 10)

    def test_multiplication_by_zero(self):
        self.assertEqual(5 * 0, 0)

    def test_division(self):
        self.assertEqual(6 / 3, 2)

    def test_division_by_zero(self):
        self.assertEqual(0 / 2, 0)

if __name__ == "__main__":
    unittest.main()