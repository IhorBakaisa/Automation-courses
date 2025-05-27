import pytest
from src.calculator import Calculator
from src.bank_account import BankAccount

@pytest.fixture(scope="session")
def calculator():
    return Calculator()

@pytest.fixture(scope="session")
def bank_account():
    return BankAccount("Misha", initial_balance=1000)