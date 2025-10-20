import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bank_account import BankAccount
from src.calculator import Calculator

# Simple tests

def test_number1():
    assert 1 == 1

def test_number2():
    assert 5+3 == 8

def test_number345():
        assert 5 + 3 == 8

def test_number3():
    assert (4-2)/2 == 1

def test_number4():
    a = 4
    k = 8
    assert a == k-a

# Calculator tests

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

# Parametrize

@pytest.mark.parametrize("input_value, expected_result", [(1, 1),(3, 9),(4, 16)])
def test_square(input_value, expected_result):
    result = input_value **2
    assert result == expected_result

@pytest.mark.parametrize("a, b, expected_result", [(4, 5, 9),(3, 2, 5),(7, 2, 9)])
def test_operation(a, b, expected_result):
    result = a + b
    assert result == expected_result

@pytest.mark.parametrize("name, amount, expected_result", [("John", 100, 100), ("Max", 400, 400)])
def test_deposit(name, amount, expected_result):
    assert BankAccount(name).deposit(amount) == expected_result

@pytest.mark.parametrize("name, amount, expected_result", [("John",200 , 300), ("Max", 400, 100)])
def test_withdraw(name, amount, expected_result):
    account = BankAccount(name, 500)
    account.withdraw(amount)
    assert account.balance == expected_result

# Fixture

@pytest.fixture
def bank_account():
    return BankAccount("Ihor", 5000)

@pytest.fixture
def bank_balance(bank_account):
    balance = bank_account.deposit(3000)
    return balance

def test_deposit2(bank_account):
    bank_account.deposit(1000)
    assert bank_account.balance == 6000

def test_deposit3(bank_balance):
    assert bank_balance == 8000