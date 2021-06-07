"""
Tests for calc app
"""
import calc


class TestCalcApp:
	def test_add(self):
		assert 6 == calc.add(2,4)


	def test_subtract(self):
		assert 6 == calc.subtract(8,2)
