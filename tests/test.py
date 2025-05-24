from src.calculator import Calculator


def test_number1():
    assert 1 == 1

def test_number2():
    assert 5+3 == 8

def test_number3():
    assert (4-2)/2 == 1

def test_number4():
    a = 4
    k = 8
    assert a == k-a

#-------------------------------------

def test_calculator_add():
    number = Calculator().add(10, 20)
    assert number == 30

def test_calculator_subtract():
    number = Calculator().subtract(10, 20)
    assert number == -10

def test_calculator_multiply():
    number = Calculator().multiply(10, 20)
    assert number != 300

def test_calculator_divide():
    number = Calculator().divide(10, 20)
    assert number < 1

#-------------------------------------