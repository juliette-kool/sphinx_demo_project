import unittest
from src import loader

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()