import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)

    def test_divi(self):
        self.assertEqual(self.calc.divi(6, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.divi(5, 0)

if __name__ == "__main__":
    unittest.main()
