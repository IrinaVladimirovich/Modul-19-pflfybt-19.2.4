mport pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 4, 2) == 2

    def test_multiply(self):
        assert self.calculator.multiply(self, 4, 2) == 8

    def test_division(self):
        assert self.calculator.division(self, 9, 3) == 3

    def teardown(self):
        print("Выполнение метода Teardown")
