import unittest

from src.calculator import suma, resta, division, multiplicacion

class CalculatorTest(unittest.TestCase):
   
    def test_sum(self):
        self.assertEqual(suma(4, 3), 7)

    def test_resta(self):
        self.assertEqual(resta(10, 5), 5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)