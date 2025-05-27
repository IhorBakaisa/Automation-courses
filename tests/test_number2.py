import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

@pytest.mark.slow
def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

@pytest.mark.slow
def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-1, -1) == -2

@pytest.mark.fast
def test_add_zero():
    calc = Calculator()
    assert calc.add(0, 5) == 5

@pytest.mark.fast
def test_subtract_positive_numbers():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5

@pytest.mark.critical
def test_subtract_negative_numbers():
    calc = Calculator()
    assert calc.subtract(-10, -5) == -5

@pytest.mark.critical
def test_subtract_zero():
    calc = Calculator()
    assert calc.subtract(0, 5) == -5

@pytest.mark.xfail
def test_multiply_positive_numbers():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15

@pytest.mark.skipif(sys.version_info != 0, reason="Fail")
def test_multiply_with_zero():
    calc = Calculator()
    assert calc.multiply(0, 10) == 0

@pytest.mark.smock
def test_multiply_negative_numbers():
    calc = Calculator()
    assert calc.multiply(-4, -2) == 8

@pytest.mark.smock
def test_divide_positive_numbers():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_negative_numbers():
    calc = Calculator()
    assert calc.divide(-9, 3) == -3

def test_divide_negative_by_negative():
    calc = Calculator()
    assert calc.divide(-6, -2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Ділення на нуль неможливе."):
        calc.divide(10, 0)

def test_add_large_numbers():
    calc = Calculator()
    assert calc.add(1000000, 2000000) == 3000000

def test_multiply_large_numbers():
    calc = Calculator()
    assert calc.multiply(1000, 2000) == 2000000
