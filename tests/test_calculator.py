import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)       # positive result
        self.assertEqual(subtract(3, 5), -2)      # negative result
        self.assertEqual(subtract(-2, -3), 1)     # subtract negative numbers

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)        # normal division
        self.assertEqual(divide(-6, 3), -2)       # negative dividend
        with self.assertRaises(ValueError):       # division by zero should raise error
            divide(5, 0) 

if __name__ == '__main__':
    unittest.main()