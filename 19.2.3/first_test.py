import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 3) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 9, 3) == 6

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 4) == 6
