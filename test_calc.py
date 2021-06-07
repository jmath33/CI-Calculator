"""
Tests for calc app
"""
import calc


class TestCalcApp:
    def test_add(self):
        assert 6 == calc.add(2, 4)

    def test_subtract(self):
        assert 6 == calc.subtract(8, 2)

    def test_multiply(self):
        assert 8 == calc.multiply(4, 2)

    def test_divide(self):
        assert 5 == calc.divide(10, 2)
